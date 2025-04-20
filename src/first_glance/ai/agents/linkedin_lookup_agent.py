from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, BasePromptTemplate
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor, BaseSingleActionAgent

from first_glance.core import settings
from first_glance.models import llm_schemas
from first_glance.ai.tools import ProfileURLTavilyTool


class LinkedInLookupAgent:
    """Agent to fetch LinkedIn profile URL."""

    _default_prompt_template = PromptTemplate(
        template="""
        given the full name {name_of_person} I want you to get it me a link to their profile page. 
        Your answer should contain only a URL
    """,
        input_variables=["name_of_person"],
    )

    def __init__(self, prompt_template: PromptTemplate = None):
        if prompt_template is None:
            prompt_template = self._default_prompt_template

        self.llm = ChatOpenAI(
            api_key=settings.openai_api_key, model_name="gpt-4o-mini", temperature=0
        )
        self.prompt: BasePromptTemplate = hub.pull("hwchase17/react")
        self.prompt_template = prompt_template
        self.tools = [ProfileURLTavilyTool()]
        # NOTE: This is to not store the tools but create logic of when and why to use the tool.
        self.agent = create_react_agent(
            llm=self.llm, tools=self.tools, prompt=self.prompt
        )
        # NOTE: This is to store the tools so as to use them when executing the agent.
        self.executor = AgentExecutor(agent=self.agent, tools=self.tools, verbose=True)

    def _format_prompt(self, name_of_person: str):
        """Formats the prompt with the person's name."""
        lookup_prompt_schema = llm_schemas.LinkedinLookupPrompt(
            name_of_person=name_of_person
        )
        return self.prompt_template.format_prompt(**lookup_prompt_schema.model_dump())

    def run(self, name_of_person: str):
        """Executes the agent to fetch the LinkedIn profile URL."""
        return self.executor.invoke(
            input={"input": self._format_prompt(name_of_person=name_of_person)}
        )


def lookup(name: str) -> str:
    agent = LinkedInLookupAgent()
    # Generate results
    result = agent.run(name_of_person=name)
    return result["output"]


if __name__ == "__main__":
    linkedin_url = lookup(name="Rahul J Saliaan")
    print(linkedin_url)
