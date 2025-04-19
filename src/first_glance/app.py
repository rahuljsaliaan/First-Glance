from fastapi import FastAPI

from first_glance.api.middlewares import ErrorMiddleware
from first_glance.api import first_glance_router

app = FastAPI()

app.add_middleware(middleware_class=ErrorMiddleware)


@app.get("/")
async def root():
    return {"message": "First Glance"}


app.include_router(router=first_glance_router, prefix="/api/v1", tags=["summary"])
