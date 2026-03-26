from fastapi import FastAPI

from app.openai_client import LOCKED_MODEL, create_json_response
from app.schemas import AnalyzeProfileRequest, GeneratePlanRequest, ReviewAnswerRequest


app = FastAPI(title="Career Roadmap API")


@app.get("/health")
async def health() -> dict:
    return {
        "status": "ok",
        "project": "career-roadmap-api",
        "model": LOCKED_MODEL,
        "model_selection": "locked",
    }


@app.post("/analyze-profile")
async def analyze_profile(request: AnalyzeProfileRequest) -> dict:
    system_prompt = (
        "You analyze career profiles for technical learners. "
        "Return valid JSON only with keys: strengths, gaps, role_fit, next_focus. "
        "All values must be arrays of short strings except role_fit, which must be a short string."
    )
    user_prompt = (
        f"Profile summary: {request.profile_summary}\n"
        f"Target role: {request.target_role}"
    )
    data = create_json_response(system_prompt=system_prompt, user_prompt=user_prompt)
    return {"model": LOCKED_MODEL, "data": data}


@app.post("/generate-plan")
async def generate_plan(request: GeneratePlanRequest) -> dict:
    system_prompt = (
        "You create realistic weekly technical learning plans. "
        "Return valid JSON only with keys: target_role, duration_weeks, weekly_plan, final_outcome. "
        "weekly_plan must be an array of objects with keys: week, goal, tasks. "
        "tasks must be an array of short strings."
    )
    user_prompt = (
        f"Current skills: {', '.join(request.current_skills)}\n"
        f"Target role: {request.target_role}\n"
        f"Duration in weeks: {request.duration_weeks}"
    )
    data = create_json_response(system_prompt=system_prompt, user_prompt=user_prompt)
    return {"model": LOCKED_MODEL, "data": data}


@app.post("/review-answer")
async def review_answer(request: ReviewAnswerRequest) -> dict:
    system_prompt = (
        "You review technical interview answers. "
        "Return valid JSON only with keys: score, strengths, weaknesses, improved_answer. "
        "score must be an integer from 1 to 10. strengths and weaknesses must be arrays of short strings. "
        "improved_answer must be a concise improved version of the answer."
    )
    user_prompt = f"Question: {request.question}\nAnswer: {request.answer}"
    data = create_json_response(system_prompt=system_prompt, user_prompt=user_prompt)
    return {"model": LOCKED_MODEL, "data": data}
