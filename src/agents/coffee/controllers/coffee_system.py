def end_flow(context):
    return {"result": "EOF"}


def escalate_flow(context):
    return {
        "result": f"Warning! Flow is interrupted. User attention required: {context}"
    }
