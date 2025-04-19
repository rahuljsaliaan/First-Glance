from typing import List
from pydantic import BaseModel, Field


class FirstGlanceResponse(BaseModel):
    name: str = Field(..., description="Full name of the linked in user")
    summary: str = Field(..., description="Summary of the user")
    interesting_facts: List[str] = Field(..., description="Two interesting facts")
