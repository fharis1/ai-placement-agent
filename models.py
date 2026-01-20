"""
Pydantic models for request and response validation.
These models ensure the API receives and returns data in the correct format.
"""

from pydantic import BaseModel, Field


class PlacementRequest(BaseModel):
    """Request model for placement preparation plan generation."""
    
    resume_text: str = Field(
        ...,
        description="The full text content of the user's resume",
        min_length=50,
        max_length=5000
    )
    target_role: str = Field(
        ...,
        description="The target job role or position the user is applying for",
        min_length=3,
        max_length=200
    )
    weak_areas: str = Field(
        ...,
        description="Areas where the user needs improvement (e.g., 'Data structures, System design')",
        min_length=10,
        max_length=500
    )


class StudyPlan(BaseModel):
    """Structure for the study plan section."""
    plan: str = Field(..., description="Detailed study plan with timeline and resources")


class InterviewQuestions(BaseModel):
    """Structure for interview questions section."""
    questions: list[str] = Field(..., description="List of relevant interview questions for the target role")


class ResumeFeedback(BaseModel):
    """Structure for resume feedback section."""
    feedback: str = Field(..., description="Detailed feedback on the resume")
    suggestions: list[str] = Field(..., description="List of improvement suggestions")


class PlacementResponse(BaseModel):
    """Response model containing all placement preparation outputs."""
    
    study_plan: StudyPlan = Field(..., description="Personalized study plan")
    interview_questions: InterviewQuestions = Field(..., description="Targeted interview questions")
    resume_feedback: ResumeFeedback = Field(..., description="Resume analysis and feedback")
