// src/services/api.js

import axios from "axios";

// ⚠️ IMPORTANTE:
// Com o proxy do Vite, NÃO usamos http://127.0.0.1:8000 aqui
// Isso evita problemas de CORS e facilita deploy

const api = axios.create({
  baseURL: "", // usa o proxy do vite.config.js
  timeout: 15000,
  headers: {
    "Content-Type": "application/json",
  },
});

// -----------------------------
// RESPONSE INTERCEPTOR
// -----------------------------
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // 🔴 Erro vindo do backend
    if (error.response) {
      console.error("[API ERROR]", {
        status: error.response.status,
        data: error.response.data,
      });

      const message =
        error.response.data?.detail ||
        error.response.data?.message ||
        "Erro no servidor";

      throw new Error(message);
    }

    // 🌐 Sem resposta (backend offline, timeout, etc)
    if (error.request) {
      console.error("[NETWORK ERROR]", error.request);

      throw new Error(
        "Não foi possível conectar ao servidor. Verifique se o backend está rodando."
      );
    }

    // ⚠️ Erro inesperado
    console.error("[UNKNOWN ERROR]", error.message);

    throw new Error("Erro inesperado ao processar a requisição");
  }
);

export default api;