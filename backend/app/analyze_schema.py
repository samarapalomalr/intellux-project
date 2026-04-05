from pydantic import BaseModel
from typing import List


# -----------------------------
# REQUEST
# -----------------------------
class AnalyzeRequest(BaseModel):
    post_url: str


# -----------------------------
# METRICS (SEM FOLLOWERS)
# -----------------------------
class Metrics(BaseModel):
    likes: int = 0
    comments: int = 0


# -----------------------------
# RESPONSE
# -----------------------------
class AnalyzeResponse(BaseModel):
    metrics: Metrics
    engagement_score: float
    viral_classification: str
    content_type: str
    sentiment: str
    insights: List[str]
    recommendations: List[str]