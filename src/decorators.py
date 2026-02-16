from functools import wraps
from typing import Any, Callable, Optional


def log(func: Optional[Callable] = None, *, filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования работы функции."""

    def decorator(inner_func: Callable) -> Callable:
        @wraps(inner_func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = inner_func(*args, **kwargs)
                message = f"{inner_func.__name__} ok"
            except Exception as error:
                message = (
                    f"{inner_func.__name__} error: {type(error).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)

                raise
            else:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)

                return result

        return wrapper

    if func is None:
        return decorator

    return decorator(func)
