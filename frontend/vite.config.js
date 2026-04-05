// vite.config.js

import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/analyze": {
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/analyze/, "/analyze"),
        configure: (proxy) => {
          proxy.on("proxyReq", (proxyReq, req) => {
            console.log("[PROXY]", req.method, req.url);
          });
        }
      }
    }
  }
});