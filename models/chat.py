from pydantic import BaseModel, Field, field_validator
from typing import Any

class ChatRequest(BaseModel):
    prompt: str = Field(min_length=10, max_length=500)

    @field_validator("prompt", mode="before")
    @classmethod
    def prompt_validate(cls, value: Any) -> Any:
        if not isinstance(value, str):
            return value
        if not value.strip():
            raise ValueError("Prompt cannot be empty.")

        return value.strip()