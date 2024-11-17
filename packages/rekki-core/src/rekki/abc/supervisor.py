from __future__ import annotations

from typing import TYPE_CHECKING, Any, Awaitable, Callable, Optional, Type

from abc import ABC

__all__ = ("Strategy", "SupervisorT")

from enum import Enum

if TYPE_CHECKING:
    from .actor import ServiceT


class SupervisorStrategy(Enum):
    # RESUME = "RESUME"  # Resume the subordinate, keeping its accumulated internal state
    RESTART = "RESTART"  # Restart the subordinate, clearing out its accumulated internal state
    STOP = "STOP"  # Stop the subordinate permanently
    ESCALATE = "ESCALATE"  # Thrown to up level node


class SupervisorT(ABC):
    """Base type for all supervisor strategies."""

    strategy: SupervisorStrategy

    max_restarts: float
    over: float
    raises: Type[BaseException]

    _service: ServiceT
