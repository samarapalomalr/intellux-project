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

        if not post_data:
            raise HTTPException(
                status_code=500,
                detail="Não foi possível obter dados do Instagram."
            )

        # -----------------------------
        # ANALISAR COM IA + BACKEND
        # -----------------------------
        result = analyze_post_with_ai(post_data)

        # ✅ AGORA RETORNA TUDO (CORRETO)
        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro interno na análise: {str(e)}"
        )