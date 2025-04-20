from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from first_glance.models import response_dtos, request_dtos
from first_glance.services import first_glance_with

router = APIRouter()


@router.post("/summary", response_model=response_dtos.Summary)
async def get_first_glance(data: request_dtos.FirstGlanceRequest):
    data = first_glance_with(name=data.name)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=data.model_dump(),
    )
