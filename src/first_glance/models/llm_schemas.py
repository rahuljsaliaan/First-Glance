from typing import List
from pydantic import BaseModel, Field


class LinkedinLookupPrompt(BaseModel):
    name_of_person: str = Field(
        ..., description="Name of the person to be searched in linked in"
    )
