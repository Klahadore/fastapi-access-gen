import inspect
from types import ModuleType
from typing import Dict, List, Type, Any, get_type_hints, get_origin, get_args
from pydantic import BaseModel
import inspect

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
