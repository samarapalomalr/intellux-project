// src/pages/Home.jsx
import TextInput from "../components/TextInput";
import ResultCard from "../components/ResultCard";
import Loader from "../components/Loader";
import { useAnalyze } from "../hooks/useAnalyze";

export default function Home() {
  const { analyze, data, loading, error, reset } = useAnalyze();

  return (
    <div className="container">
      {/* HEADER */}
      <div style={{ marginBottom: 40 }}>
        <h1 className="title">Intellux Analyzer</h1>
        <p className="subtitle">
          Todas as métricas e insights em uma única plataforma com IA
        </p>
      </div>

      {/* INPUT - A dynamic 'key' ensures cleanliness.
          When 'data' changes to null on reset, the component restarts with a clean slate.
      */}
      <TextInput 
        key={data ? "analisado" : "novo"} 
        onSubmit={analyze} 
        loading={loading} 
      />

      {/* ERROR */}
      {error && (
        <div className="card" style={{ marginTop: 20 }}>
          <p style={{ color: "#ef4444" }}>❌ {error}</p>
        </div>
      )}

      {/* LOADING */}
      {loading && <Loader />}

      {/* RESULT */}
      {data && !loading && (
        <>
          <ResultCard data={data} />

          <div style={{ marginTop: 20 }}>
            <button className="button" onClick={reset}>
              Nova análise
            </button>
          </div>
        </>
      )}
    </div>
  );
}