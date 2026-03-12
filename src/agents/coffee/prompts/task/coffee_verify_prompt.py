verify_task_prompt = f"""
    Analyze the current session and give a verdict on the task completion based on the conversation history.

    You're allowed to answer with an exact word in the list: [True, False]

    Rules:
    - All steps are done: True
    - There're ongoing steps to complete task: False
"""
