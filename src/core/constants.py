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
