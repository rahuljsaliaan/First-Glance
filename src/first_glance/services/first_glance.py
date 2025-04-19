from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from first_glance.services import scrape_linkedin_profile
from first_glance.ai.agents import lookup


def first_glance_with(name: str) -> str:
    """Generates a brief summary and two interesting facts about a person using their LinkedIn data"""

    linkedin_url = lookup(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url)

    summary_prompt_template = PromptTemplate(
        template="""
            Given the linkedin information {information} about a person I want you to create:
            1. A short summary
            2. Two interesting facts about them
        """,
        input_variables=["information"],
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": linkedin_data})

    return res.content


if __name__ == "__main__":
    res = first_glance_with(name="Rahul J Saliaan")
    print(res)
