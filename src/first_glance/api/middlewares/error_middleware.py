from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import ValidationError


class ErrorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except HTTPException as e:
            return JSONResponse(
                status_code=e.status_code, content={"detail": f"HTTP Error: {e.detail}"}
            )
        except (RequestValidationError, ValidationError) as e:
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={
                    "detail": "Validation Error",
                    "errors": e.errors(),
                },
            )
        except ValueError as e:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"detail": f"Bad Request: {str(e)}"},
            )
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"detail": f"Internal Server Error: {str(e)}"},
            )
