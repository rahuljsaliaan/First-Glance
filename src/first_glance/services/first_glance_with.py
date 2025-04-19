from typing import TypedDict
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI

from first_glance.services import scrape_linkedin_profile
from first_glance.ai.agents import lookup
from first_glance.ai.output_parsers import summary_parser
from first_glance.models import response_dtos, llm_schemas


def first_glance_with(name: str):
    """Generates a brief summary and two interesting facts about a person using their LinkedIn data."""

    linkedin_url = lookup(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url)

    summary_prompt_template = PromptTemplate(
        template="""
            Given the linkedin information {information} about a person I want you to create:
            1. A short summary
            2. Two interesting facts about them
            {format_instructions}
        """,
        input_variables=["information"],
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

    chain: Runnable[llm_schemas.SummaryPromptInput, response_dtos.Summary] = (
        summary_prompt_template | llm | summary_parser
    )

    res = chain.invoke(input={"information": linkedin_data})

    return res.model_dump()


if __name__ == "__main__":
    res = first_glance_with(name="Rahul J Saliaan")
    print(res)
