import requests
from app.config import settings


# Endpoint do Apify Instagram Scraper (actor público)
APIFY_URL = "https://api.apify.com/v2/acts/apify~instagram-scraper/run-sync-get-dataset-items"


def fetch_instagram_data(url: str):
    """
    Busca dados do Instagram via Apify.
    Retorna um formato padronizado para o backend.
    """

    if not settings.APIFY_API_KEY:
        raise Exception("APIFY_API_KEY não configurada no .env")

    payload = {
        "directUrls": [url],
        "resultsType": "posts",
        "resultsLimit": 1
    }

    try:
        response = requests.post(
            f"{APIFY_URL}?token={settings.APIFY_API_KEY}",
            json=payload,
            timeout=60
        )

        response.raise_for_status()
        data = response.json()

        # Se não vier nada
        if not data or len(data) == 0:
            return {
                "caption": "",
                "likes": 0,
                "comments": 0,
                "hashtags": []
            }

        post = data[0]

        # Normalização (importante para IA funcionar bem)
        return {
            "caption": post.get("caption", "") or "",
            "likes": post.get("likesCount", 0) or 0,
            "comments": post.get("commentsCount", 0) or 0,
            "hashtags": post.get("hashtags", []) or []
        }

    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro ao acessar Apify: {str(e)}")

    except Exception as e:
        raise Exception(f"Erro ao processar dados do Instagram: {str(e)}")