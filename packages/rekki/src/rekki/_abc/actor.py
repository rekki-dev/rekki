from __future__ import annotations

from collections.abc import Awaitable

from abc import ABC

from .context import ContextT, StateT
from .lifecycle import LifecycleT


class AbstractActor(ABC, LifecycleT):
    state: StateT

    @property
    def path(self) -> str: ...

    async def send(self) -> None: ...

    async def receive(self, msg, context: ContextT, state: StateT) -> None: ...

    async def enqueue(self, aw: Awaitable) -> None: ...
