# 1 вариант
def decorate(func_to_decorate):
    """A function - decorator."""
    import json
    import functools

    @functools.wraps(func_to_decorate)
    def wrapped(*args, **kwargs):
        """The decorated function."""
        result = func_to_decorate(*args, **kwargs)
        return json.dumps(result)
    return wrapped

@decorate
def fun(*args):
    return args

print(fun.__name__)






