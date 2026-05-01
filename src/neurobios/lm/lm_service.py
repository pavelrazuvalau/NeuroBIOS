from typing import Generator
from neurobios.lm.lm_client import LMClient
from neurobios.core.models import AgentStreamingEvent
from neurobios.lm.models import Message, LMRequestConfig


class LMService:
    def __init__(self, lm_client: LMClient):
        self._lm_client = lm_client

    def send_messages(
        self, messages: list[Message], config: LMRequestConfig
    ) -> Message | Generator[AgentStreamingEvent, None, Message]:
        return self._lm_client.prompt_model(messages, config)

    def predict_metric(
        self, messages: list[Message], criteria: list[str]
    ) -> str | None:
        config = LMRequestConfig(stream=False)
        response = self.send_messages(messages, config)

        content = response.content or ""
        return self.sanitize_metric_response(content, criteria)

    def sanitize_metric_response(self, content: str, criteria: list[str]) -> str | None:
        extracted_word = None
        num_of_occurrences = 0

        for word in criteria:
            if word in content:
                extracted_word = word
                num_of_occurrences += 1

        return extracted_word if num_of_occurrences == 1 else None
