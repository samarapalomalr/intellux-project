import { useEffect } from "react";

import Home from "./pages/Home";
import "./styles/global.css";

import { wakeUpBackend } from "./services/api";

export default function App() {
  // 🔥 acorda o backend quando o app abre
  useEffect(() => {
    wakeUpBackend();
  }, []);

  return <Home />;
}