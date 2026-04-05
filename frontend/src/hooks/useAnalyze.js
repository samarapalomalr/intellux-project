// src/hooks/useAnalyze.js

import { useState } from "react";
import api from "../services/api";

export function useAnalyze() {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  const analyze = async (post_url) => {
    if (!post_url || post_url.trim() === "") {
      setError("Informe uma URL válida");
      return;
    }

    setLoading(true);
    setError(null);
    setData(null);

    try {
      const response = await api.post("/analyze", {
        post_url: post_url.trim(),
      });

      // validação defensiva (nível profissional)
      if (!response.data || !response.data.metrics) {
        throw new Error("Resposta inválida da API");
      }

      setData(response.data);
    } catch (err) {
      console.error("[ANALYZE ERROR]", err.message);
      setError(err.message || "Erro ao analisar o post");
    } finally {
      setLoading(false);
    }
  };

  const reset = () => {
    setData(null);
    setError(null);
    setLoading(false);
  };

  return {
    analyze,
    data,
    loading,
    error,
    reset,
  };
}