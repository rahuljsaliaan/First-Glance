from typing import List
from pydantic import BaseModel, Field


class Summary(BaseModel):
    summary: str = Field(..., description="Summary of the user")
    facts: List[str] = Field(..., description="Interesting facts about the user")
