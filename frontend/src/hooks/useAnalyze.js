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
  // ANALYZE (com retry leve e controlado)
  // -----------------------------
  const analyze = async (post_url) => {
    if (!post_url || post_url.trim() === "") {
      setError("⚠️ Informe uma URL válida");
      return;
    }

    const url = post_url.trim();

    setLoading(true);
    setError(null);
    setData(null);

    const maxAttempts = 2;
    let attempts = 0;

    while (attempts < maxAttempts) {
      try {
        const response = await api.post("/analyze", {
          post_url: url,
        });

        // -----------------------------
        // validação defensiva
        // -----------------------------
        if (!response) {
          throw new Error("Sem resposta do servidor");
        }

        if (!response.data) {
          throw new Error("Resposta vazia da API");
        }

        if (!response.data.metrics) {
          throw new Error("Formato de resposta inválido");
        }

        // -----------------------------
        // sucesso
        // -----------------------------
        setData(response.data);
        setLoading(false);
        return;

      } catch (err) {
        attempts++;

        console.warn(
          `[ANALYZE ERROR] tentativa ${attempts}/${maxAttempts}:`,
          err.message
        );

        // -----------------------------
        // se ainda pode tentar novamente
        // -----------------------------
        if (attempts < maxAttempts) {
          setError("🔁 Servidor instável... tentando novamente");

          // espera antes do retry (evita flood no backend)
          await sleep(2500);
          continue;
        }

        // -----------------------------
        // falhou todas as tentativas
        // -----------------------------
        setError(
          err.message ||
            "❌ Não foi possível processar o post no momento. Tente novamente."
        );

        setLoading(false);
        return;
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