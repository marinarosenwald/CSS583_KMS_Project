import uuid
from typing import Optional, List
from pydantic import BaseModel, Field

class Definition(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    word: str = Field(...)
    definition: str = Field(...)
    keywords: Optional[List[str]] = Field(default=[List])

class DefinitionUpdate(BaseModel):
    word: Optional[str]
    definition: Optional[str]
    keywords: Optional[List[str]]

class LLM(BaseModel):
    text: str = Field(...)