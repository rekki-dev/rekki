from __future__ import annotations

from rekki.typing import SupervisorStrategy
from typing import TYPE_CHECKING

from abc import ABC

__all__ = ("AbstractSupervisor",)


if TYPE_CHECKING:
    from .actor import ServiceT


class AbstractSupervisor(ABC):
    """Base type for all supervisor strategies."""

    strategy: SupervisorStrategy

    max_restarts: float
    over: float
    raises: type[BaseException]

    _service: ServiceT
