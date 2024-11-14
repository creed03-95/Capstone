from pydantic import BaseModel, Field
from typing import Optional, List

class ChatPrompt(BaseModel):
    prompt: str = Field(
        ...,
        description="The user's input message or question",
        example="What is the capital of France?"
    )
    context: Optional[str] = Field(
        None,
        description="Additional context to help guide the response",
        example="Discussing geography and European capitals"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "prompt": "What is the capital of France?",
                "context": "Discussing geography and European capitals"
            }
        }

class ChatResponse(BaseModel):
    response: str = Field(
        ...,
        description="The AI-generated response",
        example="The capital of France is Paris."
    )
    prompt: str = Field(
        ...,
        description="The original prompt that was submitted",
        example="What is the capital of France?"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "response": "The capital of France is Paris.",
                "prompt": "What is the capital of France?"
            }
        }