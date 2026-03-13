analyze_completion_prompt = f"""
    Analyze the conversation history for a plan, step results, and compare the initial plan with the executed steps to give a verdict on the task completion.
"""

verify_task_prompt = f"""
    Analyze the conversation history for a plan, step results, and compare the initial plan with the executed steps.

    Rules:
    - If all planned steps are fully executed and confirmed: output True
    - If any planned step is missing, pending, or not yet started: output False

    Now analyze the current session.
    Output EXACTLY ONE WORD: True or False.
"""
