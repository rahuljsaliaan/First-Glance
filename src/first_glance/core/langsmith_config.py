from langsmith import Client
from langchain_core.tracers import LangChainTracer
from first_glance.core import settings

from langchain_core.callbacks.manager import CallbackManager

# Initialize the tracer if both URL and API Key are available
tracer = None
if settings.langsmith_url and settings.langsmith_api_key:
    client = Client(
        api_url=settings.langsmith_url,
        api_key=settings.langsmith_api_key,
    )
    tracer = LangChainTracer(client=client, project_name=settings.langchain_project)

    # Optionally, set up the global callback manager or use the tracer
    CallbackManager.configure(inheritable_callbacks=[tracer])
    print("LangSmith tracer initialized")
else:
    print("LangSmith URL or API key not provided. Skipping tracer initialization.")
