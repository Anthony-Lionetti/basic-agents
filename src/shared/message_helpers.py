from anthropic.types import Message

def add_assistant_message(messages:list, message:Message|str) -> None:
    """
    Updates the messages list with the assistant content
    """
    messages.append(
        {
            "role":"assistant",
            "content": message.content if isinstance(message, Message) else message 
        }
    )

def add_user_message(messages:list, message:Message|str) -> None:
    """
    Updates the messages list with the assistant content
    """
    messages.append(
        {
            "role":"user",
            "content": message.content if isinstance(message, Message) else message
        }
    )

def get_text_from_message(message:Message) -> str:

    return "\n".join(
        [block.text for block in message.content if block.type=="text"]
    )
