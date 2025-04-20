from typing import List
from pydantic import BaseModel, Field


class Summary(BaseModel):
    name: str = Field(..., description="Name of the user")
    photo_url: str = Field(..., description="The url of the user profile photo")
    summary: str = Field(..., description="Summary of the user")
    facts: List[str] = Field(..., description="Interesting facts about the user")
