import re
from pathlib import Path

def read_prompt(path:Path) -> str:
    with open(path, "r") as f:
        return f.read()

def render(template_string:str, variables:dict):
        placeholders = re.findall(r"{([^{}]+)}", template_string)

        result = template_string
        for placeholder in placeholders:

            if placeholder in variables:
                result = result.replace(
                    "{" + placeholder + "}", str(variables[placeholder])
                )

        return result.replace("{{", "{").replace("}}", "}")