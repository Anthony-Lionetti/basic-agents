import json
from anthropic.types import ToolUseBlock

from src.tools.tool_registry import TOOL_REGISTRY


def run_tool(tool_name, tool_input):
    if tool_name not in TOOL_REGISTRY:
        raise ValueError("Tool definition does not exsist")
    
    return TOOL_REGISTRY[tool_name](**tool_input)


def create_tool_result_block(id:str, content:any, is_error:bool=False) -> dict:

    return  {
        "type": "tool_result",
        "tool_use_id": id,
        "content": content,
        "is_error": is_error
    }


def run_tools(message):
    tool_requests:list[ToolUseBlock] = [block for block in message.content if block.type == "tool_use"]
    tool_result_blocks = []

    for tool_request in tool_requests:

        tool_id = tool_request.id
        try:
            print(f"== Calling tool {tool_request.name} with {tool_request.input}")
            tool_output = run_tool(tool_request.name, tool_request.input)
            tool_output = json.dumps(tool_output)
            tool_result_block = create_tool_result_block(tool_id, tool_output)
            
        except Exception as e:
            tool_result_block = create_tool_result_block(
                tool_id, f"Error: {e}", is_error=True
                )

        tool_result_blocks.append(tool_result_block)

    return tool_result_blocks