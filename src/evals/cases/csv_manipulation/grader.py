from src.shared import LLM
import json

EVAL_PROMPT = """
You are an expert Python code reviewer. 
Your task is to evaluate the following AI-generated code to manipulate csv data.

Original Task:
<task>
{task}
</task>

Solution to Evaluate:
<solution>
{output}
</solution>

Criteria you should use to evaluate the solution:
<criteria>
{success_criteria}
</criteria>

Output Format
Provide your evaluation as a structured JSON object with the following fields, in this specific order:
- "strengths": An array of 1-3 key strengths
- "weaknesses": An array of 1-3 key areas for improvement
- "reasoning": A concise explanation of your overall assessment
- "score": A number between 1-10

Respond with JSON. Keep your response concise and direct.
Example response shape:
{{
    "strengths": string[],
    "weaknesses": string[],
    "reasoning": string,
    "score": number
}}
    """

def grader(input:dict, output:str) -> dict:
    llm = LLM()
    content = EVAL_PROMPT.format(
        output=output, 
        task=input['task'], 
        success_criteria=input['success_criteria']
        )
    messages = [
        {"role":"user", "content":content}, 
        {"role":"assistant", "content":"```json"}
        ]

    response = llm.chat(messages, stop_sequences=['```'])
    result = response.content[0].text

    data = json.loads(result)

    return data