from __future__ import annotations

from collections.abc import Awaitable, Iterable
from typing import Self

from abc import ABCMeta, abstractmethod
from types import TracebackType


class AbstractTaskGroup(metaclass=ABCMeta):
    """
    Groups several asynchronous tasks together.

    Args:
    """

    @property
    def cancelled_caught(self) -> bool:
        """
        ``True`` if this scope suppressed a cancellation exception it itself raised.

        This is typically used to check if any work was interrupted, or to see if the
        scope was cancelled due to its deadline being reached. The value will, however,
        only be ``True`` if the cancellation was triggered by the scope itself (and not
        an outer scope).
        """
        raise NotImplementedError

    @property
    def shield(self) -> bool:
        """
        ``True`` if this scope is shielded from external cancellation.

        While a scope is shielded, it will not receive cancellations from outside.
        """
        raise NotImplementedError

    @classmethod
    def from_awaitables(cls, aws: Iterable[Awaitable]) -> AbstractTaskGroup:
        """
        Create a new task group from a series of awaitable object.

        Args:
            aws (Iterable[Awaitable]):
                an series of async function or coroutine to run

        Returns:
            a new task group
        """
        raise NotImplementedError

    @abstractmethod
    def add(self, aw: Awaitable, name: str | None = None) -> None:
        """
        Start a new task in this task group.

        Args:
            aw (Awaitable):
                an async function or coroutine to run
            name (str | None):
                name of the task, for the purposes of introspection and debugging
        """

    async def __aenter__(self) -> Self:
        """Enter the task group context and allow starting new tasks."""
        return self

    @abstractmethod
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool | None:
        """Exit the task group context waiting for all tasks to finish."""
