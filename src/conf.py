from pydantic_settings import BaseSettings

class AnthropicConfig(BaseSettings):
    MODEL:str = "claude-haiku-4-5-20251001"
    MAX_TOKENS:int = 1000


ANTRHOPIC_CONF = AnthropicConfig()