from pydantic import BaseModel, Field

class LLM(BaseModel):
    text: str = Field(...)