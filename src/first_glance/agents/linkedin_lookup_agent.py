from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, BasePromptTemplate
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor

from first_glance.core import settings
from first_glance.models import llm_schemas
from first_glance.tools import ProfileURLTavilyTool


def lookup(name: str) -> str:
    lookup_prompt_schema = llm_schemas.LinkedinLookupPrompt(name_of_person=name)

    # Create LLM chat instance with configurations
    llm = ChatOpenAI(
        api_key=settings.openai_api_key, model_name="gpt-3.5-turbo", temperature=0
    )
    # Create a prompt template
    template = """
        given the full name {name_of_person} I want you to get it me a link to their profile page. 
        Your answer should contain only a URL
    """
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    # Get better react supportive prompt
    react_prompt: BasePromptTemplate = hub.pull("hwchase17/react")
    # Create tools for the agent
    tools_for_agent = [ProfileURLTavilyTool()]
    # Create agent and agent executor
    # NOTE: This is to not store the tools but create logic of when and why to use the tool.
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    # NOTE: This is to store the tools so as to use them when executing the agent.
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    # Generate results
    result = agent_executor.invoke(
        input={
            "input": prompt_template.format_prompt(**lookup_prompt_schema.model_dump())
        }
    )
    return result["output"]


if __name__ == "__main__":
    linkedin_url = lookup(name="Rahul J Saliaan")
    print(linkedin_url)
