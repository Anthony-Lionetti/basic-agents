from pathlib import Path
from pydantic import BaseModel, Field
from typing import Optional


class TestCase(BaseModel):

    prompt_inputs: Optional[dict] = Field(
        default=None, 
        description="Dictionary containing relavent variable data for prompt"
        )
    eval_criteria: Optional[dict] = Field(
        default=None, 
        description="Dictionary containing information to guide evaluations"
        )

class TestingSuiteSetup(BaseModel):
    name:str
    description:str
    cases:int=5
    prompt_path:Path
    prompt_input_spec:dict