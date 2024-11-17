from __future__ import annotations

from typing import Literal, TypeVar

SupervisorStrategy = Literal[
    "resume",  # Resume the subordinate, keeping its accumulated internal state
    "restart",  # Restart the subordinate, clearing out its accumulated internal state
    "stop",  # Stop the subordinate permanently
    "escalate",  # Thrown to up level node
]
