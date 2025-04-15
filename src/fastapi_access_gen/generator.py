from .introspector import *
from .codegen import *


def parse_path_params(path_str: str) -> dict:
    param_pattern = r'{([^{}:]+)(?::([^{}]+))?}'

    # Find all matches
    matches = re.findall(param_pattern, path_str)

    # Extract parameter names and types
    params = {match[0]: match[1] or None for match in matches}

    return params

def separate_path_params_and_query_params(
    function_params: dict[str, str],
    path_params: dict
) -> tuple[dict, dict]:

    query_params = {}
    if 'return' in function_params:
        del function_params['return']

    for param, type in function_params.items():
        if param not in path_params:
            query_params[param] = type

    return query_params, path_params
