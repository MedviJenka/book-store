import logfire
from dataclasses import dataclass, field
from backend.settings import Config


@dataclass
class Logfire:

    name: str
    _logger: logfire = field(init=False, default=None)

    @property
    def fire(self) -> logfire:
        self._logger = logfire.configure(service_name=self.name, token=Config.LOGFIRE_TOKEN)
        return self._logger
