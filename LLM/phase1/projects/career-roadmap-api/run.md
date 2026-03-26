# Run Guide

## 1. Go to the project

```bash
cd /mnt/e/study/interviewpreparation/LLM/phase1/projects/career-roadmap-api
```

## 2. Sync dependencies

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

## 6. Test profile analysis

```bash
curl -X POST http://127.0.0.1:8000/analyze-profile \
  -H "Content-Type: application/json" \
  -d '{"profile_summary":"Python backend developer with FastAPI, Docker, AWS, and CI/CD experience.","target_role":"AI Backend Engineer"}'
```

## 7. Test plan generation

```bash
curl -X POST http://127.0.0.1:8000/generate-plan \
  -H "Content-Type: application/json" \
  -d '{"current_skills":["Python","FastAPI","AWS","Docker","CI/CD"],"target_role":"LLM Application Engineer","duration_weeks":6}'
```

## 8. Test answer review

```bash
curl -X POST http://127.0.0.1:8000/review-answer \
  -H "Content-Type: application/json" \
  -d '{"question":"Explain RAG in simple words.","answer":"RAG combines retrieval and generation to answer using outside information."}'
```
