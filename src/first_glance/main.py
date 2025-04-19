from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from first_glance.third_parties import scrape_linkedin_profile
from first_glance.agents import lookup


def first_glance_with(name: str) -> str:
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

    print(res)


def main():
    first_glance_with(name="Rahul J Saliaan")


if __name__ == "__main__":
    main()
