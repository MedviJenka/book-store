import logfire
from functools import cached_property
from dataclasses import dataclass
from backend.settings import Config


@dataclass(frozen=True)
class Logfire:

    name: str

    @cached_property
    def fire(self) -> logfire:
        log = logfire.configure(service_name=self.name, token=Config.LOGFIRE_TOKEN)
        return log
