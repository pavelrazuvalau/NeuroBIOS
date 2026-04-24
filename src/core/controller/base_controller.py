from abc import ABC, abstractmethod
import inspect


class BaseController(ABC):
    def run(self, **kwargs):
        state = kwargs.get("state", None)
        context = kwargs.get("context", None)

        response = self._execute(state, context)
        result = (yield from response) if inspect.isgenerator(response) else response
        return self._build_response(result)

    @abstractmethod
    def _execute(self, state, context):
        pass

    @abstractmethod
    def _build_response(self, result):
        pass
