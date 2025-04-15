import fastapi_access_gen
from fastapi_access_gen.generator import *
from fastapi import FastAPI

import test_files.test_models

def test_get_pydantic_classes():
    pass

from fastapi import FastAPI
import ast
import inspect
from fastapi_access_gen import introspector

app = FastAPI()

@app.get("hello/world")
def test_route(input: str, numberrr: int) -> int:
    pass

# print(introspector.get_route_and_method(test_route))
print( parse_path_params("/users/{user_id}"))
