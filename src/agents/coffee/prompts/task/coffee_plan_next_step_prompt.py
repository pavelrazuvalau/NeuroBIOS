plan_step_prompt = """
    Plan the next step based on the conversation history.

    Rules:
      - Describe each step you make
      - When the history contains a tool call that returned a result, verify whether it's successful.
      - When the recent tool call has failed, run it again.
      - Call a tool that strictly follows the order of the plan. Do no skip any steps from the initial plan.
"""
