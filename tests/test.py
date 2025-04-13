import fastapi_access_gen

import test_files.test_models


def test_get_pydantic_classes():
    pass

def test_get_fields_and_types():
    pass

from fastapi import FastAPI

app = FastAPI()
import inspect
def get_decorator(function):
    """Returns list of decorators names

    Args:
        function (Callable): decorated method/function

    Return:
        List of decorators as strings

    Example:
        Given:

        @my_decorator
        @another_decorator
        def decorated_function():
            pass

        >>> get_decorators(decorated_function)
        ['@my_decorator', '@another_decorator']

    """
    source = inspect.getsource(function)
    index = source.find("def ")
    return [
        line.strip().split()[0]
        for line in source[:index].strip().splitlines()
        if line.strip()[0] == "@"
        ][0]

@app.get("/")
async def root():
    return {"message": "Hello World"}


print(get_decorator(root))
