from src.shared import LLM
from src import ROOT
from src.evals import EVAL_ROOT
from src.shared.message_helpers import add_assistant_message, add_user_message
from src.shared.prompt_helpers import render, read_prompt

import json

from .models import TestingSuiteSetup


class TestSuiteGenerator:

    def __init__(self, max_concurrent_tasks=3):
        self.max_concurrent_tasks = max_concurrent_tasks
        self.llm = LLM()

    def run(self, setup:TestingSuiteSetup) -> None:
        """
        Generates a set of tests for a specific task description. 
        """
        # 1. generate ideas
        ideas = self._create_test_case_ideas(setup)

        # 2. generate and compile test cases
        cases = []
        for idea in ideas:
            test_case = self._create_test_case(setup, idea)
            cases.append(test_case)

        # 4. Write testing suite to json file
        self._write_to_json(setup.name, cases)

    
    def _generate_structured_json(self, system_prompt:str, rendered_prompt:str) -> str:
        # messages setup w/ prefilling
        messages = []
        add_user_message(messages, rendered_prompt)
        add_assistant_message(messages, "```json")

        # generate json & return as python list
        response = self.llm.chat(messages, system=system_prompt, stop_sequences=["```"])
        text = response.content[0].text
        return text

    
    def _create_test_case_ideas(self, setup:TestingSuiteSetup) -> list:
        # prompt setup
        system_prompt = "You are a test scenario designer specialized in creating diverse, unique testing scenarios."
        prompt_template = read_prompt(EVAL_ROOT / "generator" / "idea_prompt.md")

        rendered_prompt = render(
            prompt_template, 
            {
                "task_description": setup.description,
                "cases": setup.cases,
                "prompt_input_spec": setup.prompt_input_spec
            }
        )

        text = self._generate_structured_json(system_prompt, rendered_prompt)
        
        return json.loads(text)       

    def _create_test_case(self, setup:TestingSuiteSetup, idea:str) -> dict:
        # prompt setup
        system_prompt = "You are a test case creator specializing in designing evaluation scenarios."
        prompt_template = read_prompt(EVAL_ROOT / "generator" / "case_prompt.md")

        example_prompt_inputs = ""
        for key, value in setup.prompt_input_spec.items():
            val = value.replace("\n", "\\n")
            example_prompt_inputs += f'"{key}": "EXAMPLE_VALUE", // {val}\n'

        allowed_keys = ", ".join([f'"{key}"' for key in setup.prompt_input_spec.keys()])

        rendered_prompt = render(
            prompt_template, 
            {
                "task_description": setup.description,
                "idea": idea,
                "allowed_keys": allowed_keys,
                "example_prompt_inputs": example_prompt_inputs
            }
        )
        
        text = self._generate_structured_json(system_prompt, rendered_prompt)

        # finalize case
        test_case = json.loads(text)
        test_case["task_description"] = setup.description
        test_case["scenario"] = idea
        
        return test_case

    
    def _write_to_json(self, name:str, data:list[dict]) -> None:
        sanitized_path = name.replace(" ", "_").lower()
        path = ROOT / "evals" / "cases" / sanitized_path
        path.mkdir(parents=True)

        with open(path / "cases.json", "w") as f:
            json.dump(data, f, indent=2)