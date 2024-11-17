"""rekki exceptions."""

from __future__ import annotations

__all__ = ["MaxRestartsExceededError", "RekkiError"]


class RekkiError(Exception):
    """Base exception for rekki."""


class MaxRestartsExceededError(RekkiError):
    """Supervisor found restarting service too frequently."""
