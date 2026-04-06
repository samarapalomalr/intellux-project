import json
import re
from google import genai
from google.genai import types # Import necessário para tipos de conteúdo multimídia
from app.config import settings
from app.helpers import clean_text, build_ai_prompt

# -----------------------------
# GEMINI CLIENT
# -----------------------------
client = genai.Client(api_key=settings.GEMINI_API_KEY)

# -----------------------------
# SAFE EXTRACT
# -----------------------------
def extract_gemini_text(response) -> str | None:
    try:
        # O SDK da Google GenAI organiza a resposta em candidatos
        return response.text
    except Exception as e:
        print(f"[Gemini parse error]: {e}")
        return None

# -----------------------------
# CLEAN JSON RESPONSE
# -----------------------------
def clean_json_text(text: str) -> str:
    if not text:
        return ""
    text = text.strip()
    if "```" in text:
        text = re.sub(r"```json", "", text)
        text = re.sub(r"```", "", text)
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group(0)
    return text

# -----------------------------
# GEMINI CALL (MULTIMODAL)
# -----------------------------
def call_gemini(prompt: str, image_url: str = None) -> dict:
    try:
        contents = [prompt]
        
        # Se houver uma imagem de capa, adicionamos ao conteúdo da requisição
        if image_url:
            # O Gemini 1.5 Flash consegue processar imagens diretamente via URL pública
            # ou baixando o conteúdo. Aqui passamos como um objeto de parte de imagem.
            image_part = types.Part.from_uri(
                file_uri=image_url,
                mime_type="image/jpeg"
            )
            contents.append(image_part)

        response = client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=contents
        )

        text = extract_gemini_text(response)
        if not text:
            raise Exception("Resposta vazia do Gemini")

        cleaned = clean_json_text(text)
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            print("[RAW GEMINI OUTPUT]:", text)
            raise Exception("Gemini não retornou JSON válido")

    except Exception as e:
        print(f"[Gemini error]: {e}")
        raise Exception(f"Falha no Gemini: {e}")

# -----------------------------
# ENGAGEMENT SCORE
# -----------------------------
def calculate_engagement(likes: int, comments: int):
    likes = likes or 0
    comments = comments or 0
    # Métrica baseada no post (fator de peso maior para comentários)
    score = (likes + 2 * comments) / 1000
    return round(score, 2)

# -----------------------------
# VIRAL CLASSIFICATION
# -----------------------------
def classify_virality(score: float) -> str:
    if score >= 50: return "viral"
    elif score >= 20: return "alto"
    elif score >= 10: return "medio"
    return "baixo"

# -----------------------------
# CONTENT TYPE DETECTION (HÍBRIDO: IA + REGEX)
# -----------------------------
def detect_content_type(text: str, ai_suggestion: str = None) -> str:
    # Se a IA sugeriu um tipo baseado na imagem, damos prioridade a ele
    if ai_suggestion and ai_suggestion.lower() != "geral":
        return ai_suggestion.lower()

    text = (text or "").lower()
    if any(w in text for w in ["😂", "🤣", "kkkk", "meme", "humor"]): return "humor"
    if any(w in text for w in ["dica", "tutorial", "como"]): return "informativo"
    if any(w in text for w in ["promo", "desconto", "oferta"]): return "promocional"
    return "geral"

# -----------------------------
# MAIN SERVICE
# -----------------------------
def analyze_post_with_ai(post_data: dict) -> dict:
    try:
        caption = clean_text(post_data.get("caption", ""))
        likes = int(post_data.get("likes", 0))
        comments = int(post_data.get("comments", 0))
        display_url = post_data.get("display_url") # URL da imagem capturada no instagram_service

        # Ajustamos o prompt para pedir que a IA considere a imagem enviada
        prompt = build_ai_prompt(post_data)
        prompt += "\nIMPORTANTE: Analise também a imagem/capa enviada para identificar o contexto visual do post."
        
        ai_result = call_gemini(prompt, image_url=display_url)

        # Extração de métricas calculadas
        engagement_score = calculate_engagement(likes, comments)
        virality = classify_virality(engagement_score)
        
        # O tipo de conteúdo agora pode vir da análise visual da IA
        content_type = detect_content_type(caption, ai_result.get("content_type"))

        return {
            "metrics": {"likes": likes, "comments": comments},
            "display_url": display_url,
            "engagement_score": engagement_score,
            "viral_classification": virality,
            "content_type": content_type,
            "sentiment": ai_result.get("sentiment", "neutro"),
            "insights": ai_result.get("insights", []),
            "recommendations": ai_result.get("recommendations", [])
        }

    except Exception as error:
        print(f"[AI ERROR]: {error}")
        return {
            "metrics": {"likes": post_data.get("likes", 0), "comments": post_data.get("comments", 0)},
            "engagement_score": 0,
            "viral_classification": "baixo",
            "content_type": "desconhecido",
            "sentiment": "neutro",
            "insights": ["Falha ao analisar com IA multimodal"],
            "recommendations": ["Tente novamente", "Verifique se a imagem do post está acessível"]
        }