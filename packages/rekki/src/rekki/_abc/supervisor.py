from __future__ import annotations

from rekki.typing import SupervisorStrategy

from abc import ABCMeta

__all__ = ("AbstractSupervisor",)


class AbstractSupervisor(metaclass=ABCMeta):
    """Base type for all supervisor strategies."""

    strategy: SupervisorStrategy

    max_restarts: float
    over: float
    raises: type[BaseException]

    def on_exception(self, exc: type[BaseException]) -> SupervisorStrategy:
        """Return a strategy for handling the exception."""
        raise NotImplementedError
