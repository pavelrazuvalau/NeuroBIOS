verify_task_prompt = f"""
    Analyze the current session and give a verdict on the initial plan completion

    You're allowed to answer with an exact word in the list: [True, False]

    Rules:
    - All steps from the initial plan are done: True
    - There're ongoing steps to complete from the initial plan: False
"""
