# 🚀 Intellux - Analisador de Conteúdo com IA

## 📌 Sobre o projeto

O Intellux é uma aplicação web que utiliza Inteligência Artificial para analisar conteúdos de forma automática, fornecendo insights relevantes como:

- 📊 Análise de sentimento
- 🧠 Insights estratégicos
- 🚀 Recomendações de melhoria

O objetivo do projeto é centralizar o processo de análise em uma única interface, tornando mais simples e eficiente a tomada de decisões baseada em dados.

---

## 🧠 Funcionalidades

- Inserção de URL de posts do Instagram
- Coleta automática de métricas (likes, comentários)
- Processamento via IA generativa
- Retorno com:
  - Sentimento
  - Classificação de viralização
  - Tipo de conteúdo
  - Insights
  - Recomendações
- Interface moderna, responsiva e interativa

---

## 🏗️ Arquitetura do Sistema

A aplicação segue uma arquitetura cliente-servidor:

Frontend (React)  
↓  
Backend (FastAPI)  
↓  
API de IA (Google Gemini)  
↓  
Coleta de dados (Apify)

---

### 🔄 Fluxo da aplicação

1. Usuário insere a URL de um post do Instagram  
2. O frontend envia os dados para o backend  
3. O backend coleta métricas via Apify  
4. Os dados são enviados para a IA (Gemini)  
5. A IA gera insights e recomendações  
6. O backend organiza a resposta  
7. O frontend exibe os resultados  

---

## ⚙️ Tecnologias Utilizadas

### Frontend
- React
- Vite
- Axios

### Backend
- Python
- FastAPI

### Inteligência Artificial
- Google Gemini

### Coleta de Dados
- Apify

---

## ▶️ Como rodar o projeto localmente

### 🔹 1. Clone o repositório

```bash
git clone https://github.com/samarapalomalr/intellux.git
cd intellux/frontend

🔹 2. Instale as dependências

npm install

🔹 3. Configure as variáveis de ambiente

Crie um arquivo `.env` dentro da pasta `backend/` com:

```env
APIFY_API_KEY=sua_chave_apify

AI_PROVIDER=gemini

GEMINI_API_KEY=sua_chave_gemini
GEMINI_MODEL=gemini-2.5-flash

🔹 4. Execute o projeto no diretorio do frontend 

npm run start

🔹 5. Acesse no navegador

http://localhost:5173

✅ Observações

O comando npm run start inicia frontend + backend simultaneamente
Certifique-se de ter instalado:
Node.js
Python 3.10+

🧠 Decisões Técnicas

Separação entre frontend e backend para melhor organização
Uso de FastAPI pela performance e facilidade de integração
Uso de IA generativa para análise automatizada
Estrutura modular para facilitar manutenção e escalabilidade
Uso de proxy no Vite para integração local entre front e back

⚠️ Limitações

Dependência de APIs externas (Apify e Gemini)
Resultados podem variar dependendo do modelo de IA
Não possui autenticação de usuários

🔮 Próximos Passos

Salvar histórico de análises
Criar dashboard com gráficos
Melhorar score de engajamento
Deploy em nuvem (Vercel + Render)

📄 Documentação

O projeto contém um arquivo PDF com:
Explicação da implementação
Arquitetura do sistema
Exemplos de uso
Prints da aplicação

👩‍💻 Autora

Projeto desenvolvido por Samara Paloma
Estudante de Ciência da Computação 

⭐ Considerações finais

Este projeto foi desenvolvido com foco em aprendizado prático de integração entre frontend, backend e Inteligência Artificial, priorizando organização, usabilidade e aplicação real.