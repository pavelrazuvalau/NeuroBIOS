from typing import Any
from pydantic import BaseModel


class ToolCallFunction(BaseModel):
    name: str
    arguments: str


class ToolCall(BaseModel):
    id: str
    type: str = "function"
    function: ToolCallFunction


class Message(BaseModel):
    role: str
    content: str | None = None
    tool_calls: list[ToolCall] | None = None
    tool_call_id: str | None = None
    name: str | None = None


class ToolFunctionSchema(BaseModel):
    name: str
    description: str | None = None
    parameters: dict[str, Any] | None = None


class ToolSchema(BaseModel):
    type: str = "function"
    function: ToolFunctionSchema


class LMRequestConfig(BaseModel):
    stream: bool = True
    tools: list[ToolSchema] | None = None
    temperature: float = 0.7
