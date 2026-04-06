import TextInput from "../components/TextInput";
import ResultCard from "../components/ResultCard";
import Loader from "../components/Loader";
import { useAnalyze } from "../hooks/useAnalyze";

export default function Home() {
  const { analyze, data, loading, error, reset } = useAnalyze();

  // Função para resetar a interface e os dados
  const handleNewAnalysis = () => {
    reset(); // Limpa os dados no Hook (data, error, etc)
  };

  return (
    <div className="container">
      {/* HEADER */}
      <div style={{ marginBottom: 40, textAlign: 'center' }}>
        <h1 className="title">Intellux Analyzer</h1>
        <p className="subtitle">
          Todas as métricas e insights em uma única plataforma com IA
        </p>
      </div>

      {/* INPUT - Só aparece se não houver dados ou se estiver carregando */}
      {(!data || loading) && (
        <TextInput onSubmit={analyze} loading={loading} />
      )}

      {/* ERRO */}
      {error && (
        <div className="card" style={{ marginTop: 20 }}>
          <p style={{ color: "#ef4444" }}>❌ {error}</p>
        </div>
      )}

      {/* LOADING */}
      {loading && <Loader />}

      {/* RESULTADO */}
      {data && !loading && (
        <>
          <ResultCard data={data} />

          <div style={{ marginTop: 30, textAlign: 'center', marginBottom: 40 }}>
            <button 
              className="button" 
              onClick={handleNewAnalysis}
              style={{ maxWidth: '300px' }}
            >
              🔄 Nova análise
            </button>
          </div>
        </>
      )}
    </div>
  );
}