from __future__ import annotations

from typing import Type

from rekki._abc import AbstractSupervisor

__all__ = ("OneForAllSupervisor", "OneForOneSupervisor")


class BaseSupervisor(AbstractSupervisor):
    def __init__(self, max_restarts, backoff) -> None: ...

    def on_exception(self, exc: Type[Exception]) -> SupervisorStrategy:
        return SupervisorStrategy.RESTART

    async def restart_service(self, service: ServiceT) -> None:
        self.log.info(
            "Restarting dead %r! Last crash reason: %r",
            service,
            service.crash_reason,
            exc_info=1,
        )
        try:
            async with self._bucket:
                if self.replacement:
                    index = self._index[service]
                    new_service = await self.replacement(service, index)
                    new_service.supervisor = self
                    self.insert(index, new_service)
                else:
                    await service.restart()
        except MaxRestartsExceeded as exc:
            self.log.warning("Max restarts exceeded: %r", exc, exc_info=1)
            raise SystemExit(1)


class OneForOneSupervisor(BaseSupervisor):
    """Supervisor simply restarts any crashed service."""

    ...


class OneForAllSupervisor(BaseSupervisor):
    """Supervisor that restarts all services when a service crashes."""

    ...
