class LMService:
    def __init__(self, lm_client):
        self._lm_client = lm_client

    def send_messages(self, messages, **params):
        return self._lm_client.prompt_model(messages, params)

    def predict_metric(self, messages, criteria):
        response = self.send_messages(messages, stream=False)

        content = response.get("content", "")
        return self.sanitize_metric_response(content, criteria)

    def sanitize_metric_response(self, content, criteria):
        extracted_word = None
        num_of_occurrences = 0

        # print(f"content {content}")
        # print(f"criteria {criteria}")

        for word in criteria:
            if word in content:
                extracted_word = word
                num_of_occurrences += 1

        # print(f"extracted_word {extracted_word}")
        # print(f"num_of_occurrences {num_of_occurrences}")

        return extracted_word if num_of_occurrences == 1 else None
