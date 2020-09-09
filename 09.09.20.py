"""Для функций, возвращающих любые значения, написать декоратор в json формате."""
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
