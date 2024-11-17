from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import Any, Protocol, TypeVar

from abc import ABC, abstractclassmethod
from asyncio import Future

from .supervisor import SupervisorT

T = TypeVar("T")


class StateT: ...


class ContextT:
    async def self_ref(self): ...

    async def props(self): ...

    async def sender(self): ...

    async def children(self): ...

    async def parent(self): ...

    async def system(self): ...


class QueueT: ...


class ServiceT(ABC):
    supervisor: SupervisorT

    async def on_first_start(self): ...

    async def pre_start(self): ...

    async def start(self): ...

    async def stop(self): ...

    async def post_stop(self): ...

    async def shutdown(self): ...

    async def restart(self): ...


class ActorT(ServiceT):
    state: StateT

    __queue: QueueT
    __scheduled: Any

    @property
    def path(self) -> str: ...

    async def send(self): ...

    async def receive(self, msg, context: ContextT, state: StateT): ...

    async def enqueue(self, future: Future) -> None: ...
