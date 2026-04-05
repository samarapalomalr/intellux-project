import json
import re

from google import genai

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
# GEMINI CALL
# -----------------------------
def call_gemini(prompt: str) -> dict:
    try:
        response = client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt
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
# ENGAGEMENT SCORE (SEM FOLLOWERS)
# -----------------------------
def calculate_engagement(likes: int, comments: int):
    likes = likes or 0
    comments = comments or 0

    # métrica baseada só no post (escala ajustada)
    score = (likes + 2 * comments) / 1000
    return round(score, 2)


# -----------------------------
# VIRAL CLASSIFICATION (AJUSTADA)
# -----------------------------
def classify_virality(score: float) -> str:
    if score >= 50:
        return "viral"
    elif score >= 20:
        return "alto"
    elif score >= 10:
        return "medio"
    return "baixo"


# -----------------------------
# CONTENT TYPE DETECTION
# -----------------------------
def detect_content_type(text: str) -> str:
    text = (text or "").lower()

    if any(w in text for w in ["😂", "🤣", "kkkk", "meme", "humor"]):
        return "humor"
    if any(w in text for w in ["dica", "tutorial", "como"]):
        return "informativo"
    if any(w in text for w in ["promo", "desconto", "oferta"]):
        return "promocional"
    if any(w in text for w in ["eu", "minha vida", "meu"]):
        return "pessoal"
    if any(w in text for w in ["polêmica", "controverso"]):
        return "polêmico"

    return "geral"


# -----------------------------
# MAIN SERVICE
# -----------------------------
def analyze_post_with_ai(post_data: dict) -> dict:
    try:
        caption = clean_text(post_data.get("caption", ""))

        likes = int(post_data.get("likes", 0))
        comments = int(post_data.get("comments", 0))

        # IA → apenas análise
        prompt = build_ai_prompt(post_data)
        ai_result = call_gemini(prompt)

        # 📊 METRICS (SEM FOLLOWERS)
        metrics = {
            "likes": likes,
            "comments": comments,
        }

        # 📈 ENGAGEMENT
        engagement_score = calculate_engagement(likes, comments)

        # 🔥 VIRALIDADE
        virality = classify_virality(engagement_score)

        # 🧠 TIPO DE CONTEÚDO
        content_type = detect_content_type(caption)

        # 📦 RESPOSTA FINAL
        return {
            "metrics": metrics,
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
            "metrics": {
                "likes": post_data.get("likes", 0),
                "comments": post_data.get("comments", 0),
            },
            "engagement_score": 0,
            "viral_classification": "baixo",
            "content_type": "desconhecido",
            "sentiment": "neutro",
            "insights": [
                "Falha ao analisar com IA"
            ],
            "recommendations": [
                "Verifique API key do Gemini",
                "Verifique modelo configurado",
                "Tente novamente mais tarde"
            ]
        }