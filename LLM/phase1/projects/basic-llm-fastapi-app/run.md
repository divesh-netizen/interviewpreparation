# Run Guide

## 1. Go to the project

```bash
cd /mnt/e/study/interviewpreparation/LLM/phase1/projects/basic-llm-fastapi-app
```

## 2. Sync dependencies with uv

```bash
uv sync
```

## 3. Add API key

```bash
export OPENAI_API_KEY="your_api_key_here"
```

## 4. Start server

```bash
uv run uvicorn app.main:app --reload
```

## 5. Test health endpoint

```bash
curl http://127.0.0.1:8000/health
```

## 6. Test chat endpoint

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Explain tokens and context windows in simple words"}'
```

## 7. Test extract endpoint

```bash
curl -X POST http://127.0.0.1:8000/extract \
  -H "Content-Type: application/json" \
  -d '{"text":"Divesh has experience in Python, FastAPI, AWS, Docker, CI/CD, and system design."}'
```

## Common Issues

- If `OPENAI_API_KEY` is missing, the app will return an error.
- If dependencies are missing, run `uv sync`.
- If the model call fails, check API key, internet access, and package versions.
