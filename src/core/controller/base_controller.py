from abc import ABC, abstractmethod
import inspect


class BaseController(ABC):
    def __init__(self, dependencies):
        self._dependencies = dependencies

    def run(self, *, state, context):
        response = self._execute(state, context)
        result = (yield from response) if inspect.isgenerator(response) else response
        return self._build_response(result)

    @abstractmethod
    def _execute(self, state, context):
        pass

    @abstractmethod
    def _build_response(self, result):
        pass
