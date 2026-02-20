
import functools

def limit_calls(max_calls):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            wrapper.calls += 1
            if wrapper.calls > max_calls:
                raise RuntimeError(f"{func.__name__} exceeded call limit!")
            return func(*args, **kwargs)
        wrapper.calls = 0
        return wrapper
    return decorator
