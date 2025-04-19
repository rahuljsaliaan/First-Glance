from pydantic import BaseModel, Field


class FirstGlanceRequest(BaseModel):
    name: str = Field(..., description="Name of the linked in user")
