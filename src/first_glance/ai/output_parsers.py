from langchain_core.output_parsers import PydanticOutputParser


from first_glance.models import response_dtos

summary_parser = PydanticOutputParser(pydantic_object=response_dtos.Summary)
