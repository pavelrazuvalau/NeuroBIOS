from enum import Enum
from typing import Any
from pydantic import BaseModel, Field

from neurobios.core.constants import StreamingEvent
from neurobios.lm.models import Message


class ControllerState(BaseModel):
    context: list[Message] = Field(default_factory=list)
    agent_state: dict[str, Any] = Field(default_factory=dict)


class AgentStepResult(BaseModel):
    success: bool = True
    next_state: Enum | None = None
    context_delta: list[Message] = Field(default_factory=list)
    state_delta: dict[str, Any] = Field(default_factory=dict)


class AgentStreamingEvent(BaseModel):
    event: StreamingEvent
    payload: Any
