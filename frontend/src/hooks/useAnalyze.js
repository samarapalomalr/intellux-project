// src/hooks/useAnalyze.js

import { useState } from "react";
import api from "../services/api";

export function useAnalyze() {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  // -----------------------------
  // UTIL: delay (retry)
  // -----------------------------
  const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

  // -----------------------------
  // ANALYZE (com retry leve)
  // -----------------------------
  const analyze = async (post_url) => {
    if (!post_url || post_url.trim() === "") {
      setError("⚠️ Informe uma URL válida");
      return;
    }

    setLoading(true);
    setError(null);
    setData(null);

    const url = post_url.trim();

    let attempts = 0;
    const maxAttempts = 2;

    while (attempts <= maxAttempts) {
      try {
        const response = await api.post("/analyze", {
          post_url: url,
        });

        // -----------------------------
        // validação defensiva
        // -----------------------------
        if (!response?.data) {
          throw new Error("Resposta vazia da API");
        }

        if (!response.data.metrics) {
          throw new Error("Formato de resposta inválido");
        }

        setData(response.data);
        setLoading(false);
        return;
      } catch (err) {
        attempts++;

        console.error(`[ANALYZE ERROR] tentativa ${attempts}`, err.message);

        // -----------------------------
        // última tentativa falhou
        // -----------------------------
        if (attempts > maxAttempts) {
          setError(
            err.message ||
              "❌ Não foi possível processar o post no momento. Tente novamente."
          );
          setLoading(false);
          return;
        }

        // -----------------------------
        // retry com delay (backend dormindo / instabilidade)
        // -----------------------------
        setError("🔁 Servidor demorando para responder... tentando novamente");

        await sleep(2000);
      }
    }
  };

  // -----------------------------
  // RESET STATE
  // -----------------------------
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