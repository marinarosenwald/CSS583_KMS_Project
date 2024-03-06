from pydantic import BaseModel, Field

class LLM(BaseModel):
    text: str = Field(...)

class InputData(BaseModel):
    text: str = Field(...)

class Definition(BaseModel):
    text: str = Field(...)

class Keywords(BaseModel):
    text: list = Field(...)