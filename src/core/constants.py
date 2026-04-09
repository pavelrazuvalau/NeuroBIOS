from enum import Enum


class SystemState(str, Enum):
    IDLE = "IDLE"
    END = "END"
    ESCALATE = "ESCALATE"


SYSTEM_STOP_STATES = (SystemState.END, SystemState.ESCALATE)


class MessageRole(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


class StreamingEvent(str, Enum):
    EXECUTING_NEXT_STEP = "EXECUTING_NEXT_STEP"
    REASONING_STREAM = "REASONING_STREAM"
    CONTENT_STREAM = "CONTENT_STREAM"
    TOOL_CALL = "TOOL_CALL"
    RESPONSE_END = "RESPONSE_END"
