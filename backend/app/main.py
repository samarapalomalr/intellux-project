from fastapi import FastAPI

from app.analyze import router as analyze_router

app = FastAPI(
    title="Intellux AI Backend",
    description="API para análise de posts do Instagram com IA generativa",
    version="1.0.0"
)


# -----------------------------
# ROTAS
# -----------------------------
app.include_router(analyze_router)


# -----------------------------
# HEALTH CHECK
# -----------------------------
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Intellux API rodando 🚀"
    }