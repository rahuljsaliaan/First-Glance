from typing import Optional, Callable
from functools import wraps

from first_glance.types import DynamicFunctionType


def handle_error(
    error_type: Optional[Exception] = Exception,
    on_error: Optional[Callable[..., None]] = None,
):
    """A decorator to handle exceptions by either printing them or executing a callback."""

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
