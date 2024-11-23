import signal
import functools
from typing import Any, Callable, Optional, TypeVar, ParamSpec

P = ParamSpec('P')
R = TypeVar('R')

class TimeoutError(Exception):
    """Custom exception for timeout scenarios."""
    pass

def timeout(seconds: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Decorator that timeout a function after specified seconds.
    
    Args:
        seconds (int): Maximum allowed execution time in seconds
        
    Returns:
        Callable: Decorated function that will raise TimeoutError if execution exceeds specified time
        
    Example:
        @timeout(5)
        def long_running_function():
            time.sleep(10)
    """
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            def handler(signum: int, frame: Optional[Any]) -> None:
                raise TimeoutError(f"Function '{func.__name__}' timed out after {seconds} seconds")

            # Set up the timeout handler
            original_handler = signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)

            try:
                result = func(*args, **kwargs)
            finally:
                # Restore the original handler and disable the alarm
                signal.alarm(0)
                signal.signal(signal.SIGALRM, original_handler)

            return result
        return wrapper
    return decorator