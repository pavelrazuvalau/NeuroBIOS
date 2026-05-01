from pydantic import BaseModel

from neurobios.lm.lm_client import LMClient
from neurobios.lm.lm_service import LMService


class CoreConfig(BaseModel):
    base_url: str
    api_key: str
    model: str


class CoreDependencies:
    lm_service: LMService

    def _init_core_dependencies(self, config: CoreConfig) -> None:
        lm_client = LMClient(
            base_url=config.base_url,
            api_key=config.api_key,
            model=config.model,
        )
        self.lm_service = LMService(lm_client)
