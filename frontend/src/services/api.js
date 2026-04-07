import axios from "axios";

// 🌐 Backend 
const BASE_URL = "https://intellux-project-1.onrender.com";

const api = axios.create({
  baseURL: BASE_URL,
  timeout: 30000,
  headers: {
    "Content-Type": "application/json",
  },
});

// -----------------------------
// RETRY CONFIG
// -----------------------------
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

// -----------------------------
// 🔥 WAKE UP BACKEND 
// -----------------------------
export const wakeUpBackend = async () => {
  try {
    console.log("🔄 Acordando backend...");

    await fetch(BASE_URL + "/", {
      method: "GET",
    });

    console.log("✅ Backend acordado");
  } catch (err) {
    console.log("⚠️ Backend ainda iniciando...");
  }
};

// -----------------------------
// RESPONSE INTERCEPTOR
// -----------------------------
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const config = error.config;

    if (!config._retryCount) {
      config._retryCount = 0;
    }

    // -----------------------------
    // 🔁 RETRY
    // -----------------------------
    if (
      config._retryCount < 2 &&
      (!error.response || error.code === "ECONNABORTED")
    ) {
      config._retryCount++;

      console.warn(
        `🔁 Tentativa ${config._retryCount} de 2... aguardando backend responder`
      );

      await sleep(2000);
      return api(config);
    }

    // -----------------------------
    // 🔴 ERROR WITH BACKEND RESPONSE
    // -----------------------------
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

    // -----------------------------
    // 🌐 CONNECTION ERROR / BACKEND OFFLINE
    // -----------------------------
    if (error.request) {
      console.error("[NETWORK ERROR]", error.request);

      throw new Error(
        "Servidor demorou para responder. Ele pode estar iniciando, tente novamente em alguns segundos."
      );
    }

    // -----------------------------
    // ⚠️ UNEXPECTED ERROR
    // -----------------------------
    console.error("[UNKNOWN ERROR]", error.message);

    throw new Error("Erro inesperado ao processar a requisição");
  }
);

export default api;