def end_flow(**kwargs):
    return {"result": "EOF"}


def escalate_flow(**kwargs):
    return {
        "result": f"Warning! Flow is interrupted. User attention required: {kwargs}"
    }
