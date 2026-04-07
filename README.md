# 🚀 Intellux - Analisador de Conteúdo com IA

## 📌 Sobre o projeto

O projeto é uma solução Full-Stack de Inteligência de Dados que utiliza IA Generativa e Visão Computacional para analisar redes sociais. Através de uma arquitetura com FastAPI e React, a aplicação automatiza o ciclo completo desde a coleta de métricas brutas até a geração de relatórios. O sistema utiliza o Google Gemini 2.5 Flash para processar legendas e imagens simultaneamente, garantindo insights contextuais profundos. O fluxo transforma interações em pontuações de engajamento e classificações de viralidade com rigor técnico. Tudo é entregue em uma interface moderna e responsiva, projetada para facilitar a leitura de dados estratégicos.

---

## 🧠 Funcionalidades

O fluxo de dados foi projetado para ser linear e eficiente:

1. Entrada: O usuário insere a URL de um post do Instagram na interface.

2. Coleta (Scraping): O backend via FastAPI aciona o Apify para extrair métricas brutas (likes, comentários, legenda e URL da imagem).

3. Processamento Multimodal: Os dados e a imagem do post são enviados ao Google Gemini. A IA "enxerga" o conteúdo visual e lê a legenda simultaneamente.

4. Inteligência: O sistema calcula o Engagement Score com pesos científicos e classifica a viralidade.

5. Entrega: O frontend renderiza um dashboard com métricas neon, sentimentos, insights estratégicos e recomendações de próximos passos.

---

## 🏗️ Arquitetura do Sistema

A aplicação segue uma arquitetura cliente-servidor:

Frontend (React - Vercel) -> Backend (FastAPI - Render) -> API de IA (Google Gemini) -> Coleta de dados (Apify)

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

```bash

🔹 1. Clone o repositório

git clone https://github.com/samarapalomalr/data-ai-portfolio

🔹 2. Backend

Entre na pasta do backend e instale as dependências:
cd backend
pip install -r requirements.txt

Crie um arquivo .env dentro da pasta backend/ com suas credenciais:

.env
APIFY_API_KEY=sua_chave_apify

AI_PROVIDER=gemini

GEMINI_API_KEY=sua_chave_gemini
GEMINI_MODEL=gemini-2.5-flash

Importante: Para rodar o servidor, permaneça na pasta backend/ (não entre na pasta app):
uvicorn app.main:app --reload

🔹 3. Frontend

cd frontend
npm install
npm run dev

🔹 4. Acesse no navegador

http://localhost:5173

🔹 5. Acesso ao sistema

Você pode acessar o sistema diretamente em produção, sem precisar rodar localmente: 

https://intellux-project.vercel.app/

```

### 🛠️ Decisões Técnicas

- Separação entre frontend e backend para melhor organização
- Uso de FastAPI pela performance e facilidade de integração
- Uso de IA generativa para análise automatizada
- Estrutura modular para facilitar manutenção e escalabilidade
- Uso de proxy no Vite para integração local entre front e back
- Deploy separado:
      Frontend → Vercel
      Backend → Render

### ⚠️ Limitações

- Sincronização de Métricas: Em alguns casos, o número de comentários pode apresentar divergências momentâneas em relação ao post real devido ao cache das APIs de scraping (Apify) ou ao atraso na propagação de dados das próprias redes sociais.
- Dependência de Terceiros: A velocidade da análise está atrelada ao tempo de resposta das APIs externas, o que pode causar variações no tempo de carregamento.
- Posts Privados: O sistema só consegue analisar perfis e posts públicos, respeitando as políticas de privacidade das plataformas.

### 🔮 Próximos Passos

- Sincronização em Tempo Real: Implementar uma rotina de validação dupla para garantir que a contagem de interações (likes/comentários) seja 100% fiel ao momento exato da consulta.
- Análise de Vídeo (Reels): Expandir a capacidade multimodal para processar frames de vídeos curtos.
- Benchmark: Comparar o post analisado com a média de engajamento do perfil.

### 📄 Documentação

O projeto contém um arquivo PDF com:
- Explicação da implementação
- Arquitetura do sistema
- Exemplos de uso
- Prints da aplicação

### 👩‍💻 Autora

Projeto desenvolvido por Samara Paloma
Estudante de Ciência da Computação 

### ⭐ Considerações finais

Este projeto foi desenvolvido com foco em aprendizado prático de integração entre frontend, backend e Inteligência Artificial, priorizando organização, usabilidade e aplicação real.