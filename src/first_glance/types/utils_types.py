from typing import TypeVar, Callable, Any


DynamicFunctionType = TypeVar("DynamicFunctionType", bound=Callable[..., Any])
