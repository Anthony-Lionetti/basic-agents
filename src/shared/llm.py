from anthropic import Anthropic
from anthropic.types import Message, ToolParam
from src.conf import ANTRHOPIC_CONF
from dotenv import load_dotenv

load_dotenv()

class LLM:

    def __init__(self):
        self.client = Anthropic()
    
    def chat(self, 
        messages:list, 
        system:str=None, 
        temperature:int=0.7, 
        stream:bool=False,
        stop_sequences=[],
        tools:list[ToolParam] = []
        ) -> Message:
        
        params = {
            "model":ANTRHOPIC_CONF.MODEL,
            "max_tokens":ANTRHOPIC_CONF.MAX_TOKENS,
            "messages":messages,
            "temperature": temperature,
            "stream": stream,
            "stop_sequences": stop_sequences,
            "tools": tools
        }

        if system:
            params["system"] = system

        message = self.client.messages.create(**params)

        return message
