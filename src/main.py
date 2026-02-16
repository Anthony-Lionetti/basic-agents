from src.shared import LLM
from src.tools import get_current_datetime_schema, set_reminder_schema, add_duration_to_datetime_schema
from src.shared.message_helpers import add_assistant_message, add_user_message, get_text_from_message
from src.shared.tool_helpers import run_tools

TOOLS = [get_current_datetime_schema, set_reminder_schema, add_duration_to_datetime_schema]

def run_conversation(llm, messages):
    
    while True:
        response = llm.chat(messages, tools=TOOLS)

        add_assistant_message(messages, response)
        print(get_text_from_message(response))

        if response.stop_reason != "tool_use":
            break

        tool_results = run_tools(response)
        add_user_message(messages, tool_results)

    return messages

if __name__ == "__main__":

    llm = LLM()

    messages = []
    add_user_message(messages, "Set a reminder for my doctors appointment. Its 177 day after Jan 1st, 2050.")

    run_conversation(llm, messages)