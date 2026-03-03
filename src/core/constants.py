from enum import Enum


class SystemState(str, Enum):
    IDLE = "IDLE"
    END = "END"
    ESCALATE = "ESCALATE"
    
SYSTEM_STOP_STATES = (SystemState.END, SystemState.ESCALATE)