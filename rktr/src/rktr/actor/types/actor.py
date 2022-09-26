from typing import Protocol, TypeVar, Any, Callable, Awaitable

T = TypeVar("T")


AsyncSend = Callable[[T], Awaitable[None]]
AsyncThrow = Callable[[Exception], Awaitable[None]]
AsyncClose = Callable[[], Awaitable[None]]


class StateT:
    ...


class ContextT:
    async def get_self(self):
        ...

    async def get_props(self):
        ...

    async def get_sender(self):
        ...

    async def get_children(self):
        ...

    async def get_parent(self):
        ...

    async def get_system(self):
        ...


class QueueT:
    ...


class SupervisorT:

    supervisor_strategy: str


class ServiceT(Protocol):

    supervisor: SupervisorT

    async def on_first_start(self):
        ...

    async def pre_start(self):
        ...

    async def start(self):
        ...

    async def stop(self):
        ...

    async def post_stop(self):
        ...

    async def shutdown(self):
        ...

    async def restart(self):
        ...


class ActorT(Protocol):

    state: StateT

    __queue: QueueT
    __scheduled: Any

    @property
    def path(self) -> str:
        ...

    async def send(self):
        ...

    async def receive(self, msg, context: ContextT, state: StateT):
        ...
