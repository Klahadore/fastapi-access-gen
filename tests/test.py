import fastapi_access_gen
from fastapi_access_gen.generator import *
from fastapi import FastAPI
import ast
import inspect
from fastapi_access_gen import introspector
from typing import get_type_hints
import test_files.test_models
from fastapi_access_gen import generator

def test_get_pydantic_classes():
    pass


app = FastAPI()

@app.get("hello/world/{input:int}/{numberrr}")
def test_route(input: str, numberrr: int, hello: int) -> int:
    pass

# print(introspector.get_route_and_method(test_route))

the_type = get_type_hints(test_route)
print(int == the_type['numberrr'])
route = introspector.get_routes_and_methods(test_route)[0][1]

path_params =  generator.parse_path_params(route)
print(path_params)
print(generator.separate_path_params_and_query_params(the_type, path_params))
