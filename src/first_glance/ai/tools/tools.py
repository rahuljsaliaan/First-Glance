from typing import Type
from langchain.tools import BaseTool
from langchain_community.tools.tavily_search import TavilySearchResults

from first_glance.models import llm_schemas


class ProfileURLTavilyTool(BaseTool):
    """LangChain tool to search for a person's LinkedIn profile using Tavily."""

    name: str = "Crawl Google for LinkedIn Profile."
    description: str = "Search Google to find a LinkedIn profile URL for a person."
    args_schema: Type[BaseTool] = llm_schemas.LinkedinLookupPrompt

    def _get_profile_url_tavily(self, name_of_person: str) -> str:
        """Runs Tavily search for a person's profile."""
        return TavilySearchResults().run(f"{name_of_person}")

    def _run(self, name_of_person: str) -> str:
        """Sync run method for LangChain."""
        return self._get_profile_url_tavily(name_of_person)

    async def _arun(self, name_of_person: str) -> str:
        """Async run method for LangChain."""
        return await self._get_profile_url_tavily(name_of_person)
