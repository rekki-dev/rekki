"""Custom exceptions."""

__all__ = ["MaxRestartsExceeded"]


class InternalException(Exception):
    ...


class MaxRestartsExceeded(InternalException):
    """Supervisor found restarting service too frequently."""
