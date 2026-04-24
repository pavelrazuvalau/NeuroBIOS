import inspect

from core.constants import MessageRole, StreamingEvent
from core.fsm import StateMachine
from core.utils import deep_merge
from core.context_manager import ContextManager


class AgentCore:
    def __init__(self, controllers):
        fsm_actions = {}

        for fsm_state, controller in controllers.items():
            controller_instance = controller()
            fsm_actions[fsm_state] = controller_instance.run

        self._fsm = StateMachine(fsm_actions)
        self._context_manager = ContextManager()
        self._agent_state = {}

    def run(self, flow, user_prompt):
        self._context_manager.append_message(MessageRole.USER, user_prompt)

        self._fsm.set_flow(flow)
        yield from self._run_fsm()

    def _run_fsm(self):
        while self._fsm.is_flow_running:
            current_context = self._context_manager.get_messages_history()

            yield {"event": StreamingEvent.EXECUTING_NEXT_STEP, "payload": {}}

            step_response = self._fsm.execute_state(
                context=current_context, state=self._agent_state
            )

            step_result = (
                (yield from step_response)
                if inspect.isgenerator(step_response)
                else step_response
            )

            if step_result:
                step_messages_delta = step_result.get("context_delta", [])
                self._context_manager.append_messages_list(step_messages_delta)

                step_state_delta = step_result.get("state_delta", {})
                self._update_agent_state(step_state_delta)

            self._fsm.go_to_next_state()

        yield {"event": StreamingEvent.RESPONSE_END, "payload": {}}

    def _update_agent_state(self, delta):
        deep_merge(self._agent_state, delta)
