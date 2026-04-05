from fastapi import APIRouter, HTTPException

from app.analyze_schema import AnalyzeRequest, AnalyzeResponse
from app.helpers import validate_instagram_url
from app.ai_service import analyze_post_with_ai
from app.instagram_service import fetch_instagram_data

router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_post(request: AnalyzeRequest):

    # -----------------------------
    # VALIDAR URL
    # -----------------------------
    if not validate_instagram_url(request.post_url):
        raise HTTPException(
            status_code=400,
            detail="URL inválida. Use um link do Instagram."
        )

    try:
        # -----------------------------
        # BUSCAR DADOS DO INSTAGRAM
        # -----------------------------
        post_data = fetch_instagram_data(request.post_url)

        # fallback defensivo (NUNCA deixar quebrar pipeline)
        if not post_data:
            post_data = {
                "caption": "",
                "likes": 0,
                "comments": 0,
                "hashtags": []
            }

        # -----------------------------
        # ANALISAR COM IA
        # -----------------------------
        result = analyze_post_with_ai(post_data)

        # validação final (evita resposta quebrada)
        if not result:
            raise HTTPException(
                status_code=500,
                detail="Falha ao gerar análise da IA."
            )

        return result

    except HTTPException:
        # re-raise HTTP errors (não mascarar)
        raise

    except Exception as e:
        print(f"[ANALYZE ERROR] {str(e)}")

        raise HTTPException(
            status_code=500,
            detail="Erro interno na análise. Tente novamente em alguns segundos."
        )