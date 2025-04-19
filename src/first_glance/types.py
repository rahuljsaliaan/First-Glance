from typing import TypeVar, Callable, Any


DynamicFunctionType = TypeVar(name="DynamicFunctionType", bound=Callable[..., Any])
