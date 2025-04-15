import inspect
from types import ModuleType
from typing import Dict, List, Type, Any, get_type_hints, get_origin, get_args
from pydantic import BaseModel
import inspect
import ast
import re
import warnings

def get_pydantic_classes(module: ModuleType) -> Dict[str, Type[BaseModel]]:
    """
    Extract all Pydantic model classes from a given module.

    Args:
        module: The module to inspect

    Returns:
        Dictionary mapping class names to class objects
    """
    return {
        name: obj
        for name, obj in inspect.getmembers(module)
        if inspect.isclass(obj)
        and issubclass(obj, BaseModel)
        and obj != BaseModel
    }


def get_fields_and_types(model) -> list[tuple[str, str]]:
    params = inspect.signature(model).parameters

    names, annotations = [], []
    for name, param in params.items():
        names.append(name)
        annotations.append(param.annotation)

    return list(zip(names, annotations))

# Gets decorators of fastapi routes
#
def extract_method_from_decorator(decorator_str):
    """
    Extract the HTTP method from a FastAPI route decorator string.

    Args:
        decorator_str: String like '@app.post("/users/create")'

    Returns:
        The HTTP method (GET, POST, etc.) or None if not found
    """
    pattern = r'@\w+\.(get|post|put|delete|patch|options|head)'
    match = re.search(pattern, decorator_str, re.IGNORECASE)

    if match:
        return match.group(1).upper()
    return None


def extract_route_from_decorator(decorator_str):
    """
    Extract the route path from a FastAPI route decorator string.

    Args:
        decorator_str: String like '@app.post("/users/create")'

    Returns:
        The route path as a string, or None if no path is found
    """
    # Pattern to match the route path inside quotes
    # This handles both single and double quotes
    pattern = r'@\w+\.(?:get|post|put|delete|patch|options|head)\s*\(\s*[\'"]([^\'"]*)[\'"]'
    match = re.search(pattern, decorator_str)

    if match:
        return match.group(1)

    # If no path with quotes is found, check for path without quotes (rare but possible)
    alt_pattern = r'@\w+\.(?:get|post|put|delete|patch|options|head)\s*\(\s*([^,\)]+)'
    alt_match = re.search(alt_pattern, decorator_str)

    if alt_match:
        # Clean up any whitespace
        return alt_match.group(1).strip()

    return None


def get_route_and_method(func) -> list[tuple[str, str]] :
    """Get decorators using AST parsing."""
    source = inspect.getsource(func)
    tree = ast.parse(source)

    # Find the function definition
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == func.__name__:
            # Extract decorator information
            routes = []

            for decorator in node.decorator_list:
                decorator_str = f"@{ast.unparse(decorator)}"
                method = extract_method_from_decorator(decorator_str)
                if method is None:
                    continue

                if method in ["PATCH", "OPTIONS", "HEAD", "DELETE", "PUT"]:
                    warnings.warn("We have only implemented GET and POST so far, other HTTP functions will be ignored", RuntimeWarning)
                    continue
                route_str = extract_route_from_decorator(decorator_str)


                routes.append((method, route_str))

            return routes
    return []
