from typing import Any
from fastapi import Request


def https_url_for(request: Request, name: str, **path_params: Any) -> str:
    http_url = request.url_for(name, **path_params)
    return str(http_url).replace("http://", "https://", 1)
