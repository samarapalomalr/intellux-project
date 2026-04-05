export default function ResultCard({ data }) {
  if (!data) return null;

  const {
    metrics,
    engagement_score,
    viral_classification,
    content_type,
    sentiment,
    insights,
    recommendations,
  } = data;

  return (
    <div className="card result-card">
      <h2>📊 Resultado da Análise</h2>

      {/* MÉTRICAS */}
      <div className="metrics">
        <div className="metric-card">
          <div className="metric-title">Likes</div>
          <div className="metric-value">
            {metrics.likes.toLocaleString()}
          </div>
        </div>

        <div className="metric-card">
          <div className="metric-title">Comentários</div>
          <div className="metric-value">
            {metrics.comments.toLocaleString()}
          </div>
        </div>

        <div className="metric-card">
          <div className="metric-title">Engajamento</div>
          <div className="metric-value">{engagement_score}</div>
        </div>
      </div>

      {/* CLASSIFICAÇÃO */}
      <div className="section">
        <span className="badge">
          🔥 {viral_classification.toUpperCase()}
        </span>
        <span className="badge" style={{ marginLeft: 10 }}>
          📌 {content_type}
        </span>
        <span className="badge" style={{ marginLeft: 10 }}>
          😊 {sentiment}
        </span>
      </div>

      {/* INSIGHTS */}
      <div className="section">
        <h3>🧠 Insights</h3>
        <ul className="list">
          {insights.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </div>

      {/* RECOMENDAÇÕES */}
      <div className="section">
        <h3>🚀 Recomendações</h3>
        <ul className="list">
          {recommendations.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}