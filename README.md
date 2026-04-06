# 🚀 Intellux - Analisador de Conteúdo com IA

## 📌 Sobre o projeto

É uma aplicação full-stack que utiliza Inteligência Artificial generativa para analisar conteúdos de redes sociais a partir de uma URL de post.

O projeto consiste em construir uma solução full-stack capaz de consultar dados do Instagram e apresentá-los no frontend em formato de relatório visual.

O objetivo é transformar dados de engajamento em insights estratégicos automatizados, simulando um sistema real de análise de performance de conteúdo.

A aplicação integra coleta de dados, processamento via IA e interface web, unindo conceitos de frontend, backend e integração com APIs externas em um único sistema.

Além disso, o projeto demonstra a capacidade de integrar diferentes tecnologias, desenvolver uma interface responsiva e estruturar um fluxo completo de dados entre frontend, backend e serviços externos.

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

Frontend (React - Vercel)
↓
Backend (FastAPI - Render)
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
- Vercel (deploy)

### Backend
- Python
- FastAPI
- Render (deploy)

### Inteligência Artificial
- Google Gemini

### Coleta de Dados
- Apify

---

## ▶️ Como rodar o projeto localmente

🔹 1. Clone o repositório

```bash
git clone https://github.com/samarapalomalr/data-ai-portfolio

🔹 2. Backend

cd backend
pip install -r requirements.txt

Crie um arquivo `.env` dentro da pasta `backend/` com:

```env
APIFY_API_KEY=sua_chave_apify

AI_PROVIDER=gemini

GEMINI_API_KEY=sua_chave_gemini
GEMINI_MODEL=gemini-2.5-flash

Execute: uvicorn app.main:app --reload

🔹 3. Frontend

cd frontend
npm install
npm run dev

🔹 4. Acesse no navegador

http://localhost:5173

## 🌐 Acesso ao sistema

Você pode acessar o sistema diretamente em produção, sem precisar rodar localmente: 

https://intellux-project.vercel.app/

🧠 Decisões Técnicas

- Separação entre frontend e backend para melhor organização
- Uso de FastAPI pela performance e facilidade de integração
- Uso de IA generativa para análise automatizada
- Estrutura modular para facilitar manutenção e escalabilidade
- Uso de proxy no Vite para integração local entre front e back
- Deploy separado:
      Frontend → Vercel
      Backend → Render

⚠️ Limitações

- Dependência de APIs externas (Apify e Gemini), que podem impactar a disponibilidade e o tempo de resposta
- Em alguns casos, o sistema pode apresentar instabilidade momentânea na primeira requisição, sendo necessário clicar novamente em “Analisar” para obter os insights corretamente
- Resultados podem variar dependendo do modelo de IA

🔮 Próximos Passos

- Salvar histórico de análises
- Melhorar score de engajamento

📄 Documentação

O projeto contém um arquivo PDF com:
- Explicação da implementação
- Arquitetura do sistema
- Exemplos de uso
- Prints da aplicação

👩‍💻 Autora

Projeto desenvolvido por Samara Paloma
Estudante de Ciência da Computação 

⭐ Considerações finais

Este projeto foi desenvolvido com foco em aprendizado prático de integração entre frontend, backend e Inteligência Artificial, priorizando organização, usabilidade e aplicação real.