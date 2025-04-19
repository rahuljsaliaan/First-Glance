from typing import Optional, Callable, TypeVar, Any
from functools import wraps

DynamicFunctionType = TypeVar(name="DynamicFunctionType", bound=Callable[..., Any])


def handle_error(
    error_type: Optional[Exception] = Exception,
    on_error: Optional[Callable[..., None]] = None,
):
    def decorator(func: DynamicFunctionType) -> DynamicFunctionType:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)

            except error_type as e:
                if on_error is None:
                    print(f"Error occurred {e}")
                else:
                    on_error(e)

        return wrapper

    return decorator
