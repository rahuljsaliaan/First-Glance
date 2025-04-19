from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    openai_api_key: str = Field(..., description="API key for OpenAI.")
    scrapein_api_key: str = Field(..., description="API key for ScrapeIn.")
    tavily_api_key: str = Field(..., description="API key for Tavily AI search.")

    scrapein_url: str = Field(..., description="URL of ScrapeIn API.")
    profile_data_gist_url: str = Field(
        ..., description="URL containing the default LinkedIn profile JSON."
    )
    linkedin_profile_url: str = Field(
        ..., description="URL of the default LinkedIn profile."
    )

    request_time_out: int = Field(
        default=10,
        description="Maximum time (in seconds) to wait for a response before the request times out.",
    )


settings = Settings()
