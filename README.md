# IC Chatbot

Bot do Telegram que responde perguntas de alunos sobre disciplinas, locais e contatos do Instituto de Computação (IC) — UFAL.

> Projeto para a disciplina de **Sistemas de Informação** — UFAL.

## Como funciona

O aluno envia uma mensagem em linguagem natural. O Gemini classifica a intenção e extrai o termo de busca. O bot pesquisa em um banco de dados JSON local e responde com uma mensagem formatada.

```
Mensagem do usuário → Gemini (intenção + termo) → busca no JSON → resposta formatada
```

## Configuração

**1. Clone e instale as dependências**
```bash
git clone <repo-url>
cd ic-chatbot-si
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**2. Configure as credenciais**
```bash
cp .env.example .env
```

Edite o `.env` com:
- `TELEGRAM_TOKEN` — crie um bot via @BotFather no Telegram
- `GEMINI_API_KEY` — obtenha uma chave em [aistudio.google.com](https://aistudio.google.com)

**3. Execute**
```bash
python main.py
```

## Estrutura do projeto

```
data/
  dados_ic.json       # Base de dados do IC — atualizar a cada semestre
src/
  ai/                 # Classificação de intenção via Gemini
  bot/                # Handlers e teclados do Telegram
  data/               # Loader do JSON e funções de busca
  utils/              # Formatadores de resposta
tests/                # Suite de testes com pytest
main.py               # Ponto de entrada
```

## Rodando os testes

```bash
python -m pytest tests/ -v
```

## Tecnologias

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) v20
- [Google Gemini](https://ai.google.dev/) (`gemini-1.5-flash`)
- Python 3.10+

---

# IC Chatbot

Telegram bot that answers students' questions about disciplines, locations, and contacts at the Instituto de Computação (IC) — UFAL.

> Project for the **Sistemas de Informação** course — UFAL.

## How it works

The user sends a message in natural language. Gemini classifies the intent and extracts the search term. The bot searches a local JSON database and replies with a formatted message.

```
User message → Gemini (intent + term) → JSON search → formatted reply
```

## Setup

**1. Clone and install dependencies**
```bash
git clone <repo-url>
cd ic-chatbot-si
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**2. Configure credentials**
```bash
cp .env.example .env
```

Edit `.env` with:
- `TELEGRAM_TOKEN` — create a bot via @BotFather on Telegram
- `GEMINI_API_KEY` — get a key at [aistudio.google.com](https://aistudio.google.com)

**3. Run**
```bash
python main.py
```

## Project structure

```
data/
  dados_ic.json       # IC database — update each semester
src/
  ai/                 # Gemini intent classification
  bot/                # Telegram handlers and keyboards
  data/               # JSON loader and search functions
  utils/              # Response formatters
tests/                # pytest test suite
main.py               # Entry point
```

## Running tests

```bash
python -m pytest tests/ -v
```

## Tech stack

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) v20
- [Google Gemini](https://ai.google.dev/) (`gemini-1.5-flash`)
- Python 3.10+
