from .introspector import *
from .codegen import *


def parse_path_params(path_str: str) -> dict:
    param_pattern = r'{([^{}:]+)(?::([^{}]+))?}'

    # Find all matches
    matches = re.findall(param_pattern, path_str)

    # Extract parameter names and types
    params = {match[0]: match[1] or None for match in matches}

    return params

def get_path_params_and_query_params(
    function_params: dict[str, str],
    path_params: tuple[list[str], dict[str, str]]
) -> tuple[dict, dict]:


    if 'return' in function_params:
        del function_params['return']
