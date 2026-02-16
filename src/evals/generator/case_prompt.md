Generate a single detailed test case for a prompt evaluation based on:

<task_description>
{task_description}
</task_description>

<specific_idea>
{idea}
</specific_idea>

<allowed_input_keys>
{allowed_keys}
</allowed_input_keys>

Output Format:

```json
{{
    "prompt_inputs": {{
    {example_prompt_inputs}
    }},
    "solution_criteria": ["criterion 1", "criterion 2", ...] // Concise list of criteria for evaluating the solution, 1 to 4 items
}}
```

IMPORTANT REQUIREMENTS:

- You MUST ONLY use these exact input keys in your prompt_inputs: {allowed_keys}
- Do NOT add any additional keys to prompt_inputs
- All keys listed in allowed_input_keys must be included in your response
- Make the test case realistic and practically useful
- Include measurable, concise solution criteria
- The solution criteria should ONLY address the direct requirements of the task description and the generated prompt_inputs
- Avoid over-specifying criteria with requirements that go beyond the core task
- Keep solution criteria simple, focused, and directly tied to the fundamental task
- The test case should be tailored to the specific idea provided
- Quick to solve without requiring extensive computation or multi-step processing
- Solvable with no more than 400 tokens of output
- DO NOT include any fields beyond those specified in the output format

Here's an example of a sample input with an ideal output:
<sample_input>
<sample_task_description>
Extract topics out of a passage of text
</sample_task_description>
<sample_specific_idea>
Testing with a text that contains multiple nested topics and subtopics (e.g., a passage about renewable energy that covers solar power economics, wind turbine technology, and policy implications simultaneously)
</sample_specific_idea>

<sample_allowed_input_keys>
"content"
</sample_allowed_input_keys>
</sample_input>
<ideal_output>

```json
{
  "prompt_inputs": {
    "content": "The transition to renewable energy encompasses numerous interdependent dimensions. Solar photovoltaic technology has seen dramatic cost reductions, with panel efficiency improving 24% since 2010 while manufacturing costs declined by 89%, making it economically competitive with fossil fuels in many markets. Concurrently, wind energy has evolved through innovative turbine designs featuring carbon-fiber composite blades and advanced control systems that increase energy capture by 35% in low-wind conditions."
  },
  "solution_criteria": ["Includes all topics mentioned"]
}
```

</ideal_output>
This is ideal output because the solution criteria is concise and doesn't ask for anything outside of the scope of the task description.
