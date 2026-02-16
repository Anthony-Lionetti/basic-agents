from .generator import TestSuiteGenerator
from .models import TestingSuiteSetup
from src import ROOT
from src.shared.prompt_helpers import read_prompt
from pathlib import Path
import shutil
import re

def get_case_params() -> dict:
    name = input("New Eval Name: ")
    description = input("New Eval Description: ")

    cases = int(input("# of initial cases: "))

    return {
        "name":name,
        "description":description,
        "cases":cases
        }

def select_prompt_path() -> Path:
    prompts_dir = ROOT / "prompts"
    prompt_files = sorted(prompts_dir.glob("*.md"))

    if not prompt_files:
        raise FileNotFoundError(f"No .md prompt files found in {prompts_dir}")

    print("\nAvailable prompts to run evals on:")
    for i, p in enumerate(prompt_files, 1):
        print(f"  {i}. {p.stem}")

    while True:
        choice = input(f"\nSelect a prompt (1-{len(prompt_files)}): ")
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(prompt_files):
                selected = prompt_files[idx]
                print(f"Selected: {selected.stem}")
                return selected
        except ValueError:
            pass
        print("Invalid selection, try again.")

def fetch_prompt_variables(path:Path) -> dict:
    template = read_prompt(path)

    variables = re.findall(r"\{\{(\w+)\}\}", template)
    variables = list(dict.fromkeys(variables))  # dedupe, preserve order

    if not variables:
        print("No template variables found.")
        return {}

    print(f"\nFound {len(variables)} template variable(s): {', '.join(variables)}")
    variable_spec = {}
    for variable in variables:
        description = input(f"  Describe '{variable}': ")
        variable_spec[variable] = description

    return variable_spec



if __name__ == "__main__":

    params = get_case_params()

    prompt_path = select_prompt_path()
    params['prompt_path']=prompt_path
    params["prompt_input_spec"] = fetch_prompt_variables(prompt_path)

    setup = TestingSuiteSetup(**params)

    gen = TestSuiteGenerator()
    gen.run(setup)

    # # copy grader template: src/evals/cases/grader_template.py
    # # to new use
    sanitized_name = params['name'].replace(" ", "_").lower()
    shutil.copy("src/evals/cases/grader_template.py", Path("src/evals/cases") / sanitized_name / "grader.py")


