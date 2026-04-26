import inspect

from neurobios.core.constants import MessageRole, StreamingEvent
from neurobios.core.fsm import StateMachine
from neurobios.core.utils import deep_merge
from neurobios.core.context_manager import ContextManager
from neurobios.lm.lm_client import LMClient
from neurobios.lm.lm_service import LMService


class AgentCore:
    def __init__(self, **config):
        self._fsm = StateMachine(self._init_fsm_state_actions(**config))
        self._context_manager = ContextManager()
        self._agent_state = {}

    def run(self, flow, user_prompt):
        self._context_manager.append_message(MessageRole.USER, user_prompt)

        self._fsm.set_flow(flow)
        yield from self._run_fsm()

    def _init_fsm_state_actions(self, **config):
        dependencies = self._init_dependencies(**config)
        states_config = config.get("states_config", {})

        fsm_state_actions = {}

        for fsm_state, controller in states_config.items():
            controller_instance = controller(dependencies)
            fsm_state_actions[fsm_state] = controller_instance.run

        return fsm_state_actions

    def _init_dependencies(self, **config):
        dependencies = config.get("dependencies", {})

        lm_client = LMClient(
            base_url=config.get("base_url"),
            api_key=config.get("api_key"),
            model=config.get("model"),
        )
        lm_service = LMService(lm_client)

        return {"lm_service": lm_service, **dependencies}

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
