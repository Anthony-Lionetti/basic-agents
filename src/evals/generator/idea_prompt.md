Generate {cases} unique, diverse ideas for testing a prompt that accomplishes this task:

< <task_description>
{task_description}
</task_description>

The prompt will receive the following inputs
<prompt_inputs>
{prompt_inputs_spec}
</prompt_inputs>

Each idea should represent a distinct scenario or example that tests different aspects of the task.

Output Format:
Provide your response as a structured JSON array where each item is a brief description of the idea.

Example:

```json
[
    "Testing with technical computer science terminology",
    "Testing with medical research findings",
    "Testing with complex mathematical concepts",
    ...
]
```

Ensure each idea is:

- Clearly distinct from the others
- Relevant to the task description
- Specific enough to guide generation of a full test case
- Quick to solve without requiring extensive computation or multi-step processing
- Solvable with no more than 400 tokens of output

Remember, only generate {cases} unique ideas>
