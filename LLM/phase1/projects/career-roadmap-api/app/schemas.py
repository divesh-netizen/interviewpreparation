from pydantic import BaseModel, Field


class AnalyzeProfileRequest(BaseModel):
    profile_summary: str = Field(min_length=10)
    target_role: str = Field(min_length=2)


class GeneratePlanRequest(BaseModel):
    current_skills: list[str] = Field(min_length=1)
    target_role: str = Field(min_length=2)
    duration_weeks: int = Field(ge=1, le=12)


class ReviewAnswerRequest(BaseModel):
    question: str = Field(min_length=5)
    answer: str = Field(min_length=5)
