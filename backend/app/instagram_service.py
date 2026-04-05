import requests
from app.config import settings


APIFY_URL = "https://api.apify.com/v2/acts/apify~instagram-scraper/run-sync-get-dataset-items"


def fetch_instagram_data(url: str):
    """
    Busca dados do Instagram via Apify com fallback seguro.
    Nunca quebra o backend — sempre retorna estrutura válida.
    """

    if not settings.APIFY_API_KEY:
        print("[WARNING] APIFY_API_KEY não configurada")
        return {
            "caption": "",
            "likes": 0,
            "comments": 0,
            "hashtags": []
        }

    payload = {
        "directUrls": [url],
        "resultsType": "posts",
        "resultsLimit": 1
    }

    try:
        response = requests.post(
            f"{APIFY_URL}?token={settings.APIFY_API_KEY}",
            json=payload,
            timeout=30  # 🔥 reduzido para evitar travamento
        )

        response.raise_for_status()
        data = response.json()

        # -----------------------------
        # fallback se não vier dados
        # -----------------------------
        if not data or len(data) == 0:
            return {
                "caption": "",
                "likes": 0,
                "comments": 0,
                "hashtags": []
            }

        post = data[0] if isinstance(data, list) else {}

        # -----------------------------
        # normalização segura
        # -----------------------------
        return {
            "caption": post.get("caption") or "",
            "likes": post.get("likesCount") or 0,
            "comments": post.get("commentsCount") or 0,
            "hashtags": post.get("hashtags") or []
        }

    except requests.exceptions.Timeout:
        print("[APIFY ERROR] Timeout na requisição")
        return {
            "caption": "",
            "likes": 0,
            "comments": 0,
            "hashtags": []
        }

    except requests.exceptions.RequestException as e:
        print(f"[APIFY REQUEST ERROR] {str(e)}")

        # 🔥 fallback em vez de crash
        return {
            "caption": "",
            "likes": 0,
            "comments": 0,
            "hashtags": []
        }

    except Exception as e:
        print(f"[APIFY UNKNOWN ERROR] {str(e)}")

        return {
            "caption": "",
            "likes": 0,
            "comments": 0,
            "hashtags": []
        }