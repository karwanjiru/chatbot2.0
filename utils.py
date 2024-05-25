import time
from functools import wraps

def debounce(wait):
    def decorator(fn):
        last_call = [0]

        @wraps(fn)
        def debounced(*args, **kwargs):
            now = time.time()
            if now - last_call[0] >= wait:
                last_call[0] = now
                return fn(*args, **kwargs)
        return debounced
    return decorator
