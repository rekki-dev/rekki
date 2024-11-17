from __future__ import annotations

from collections.abc import Awaitable, Iterable
from typing import TYPE_CHECKING

import anyio
from anyio import Event, create_memory_object_stream

from rekki._abc import AbstractTaskGroup
from rekki.utils.chrono import want_second

if TYPE_CHECKING:
    from rekki.typing import Second

    from anyio.abc import TaskGroup as AnyioTaskGroup
    from anyio.streams.memory import MemoryObjectReceiveStream, MemoryObjectSendStream


class BaseTaskGroup(AbstractTaskGroup):
    _started: Event
    _stopped: Event
    _crashed: Event
    _cancelled: Event

    _crash_reason: BaseException | None
    """The reason for last crash (an exception instance)."""

    _tg: AnyioTaskGroup


class TaskSet(BaseTaskGroup):
    _tasks: set[Awaitable]

    def __init__(self, aws: Iterable[Awaitable] | None = None):
        super().__init__()
        self._crash_reason = None
        self._tg = anyio.create_task_group()
        self._send_stream, self._rece_stream = create_memory_object_stream[Awaitable]()

    def add(self, aw: Awaitable, name: str | None = None):
        self._tg.start_soon(lambda: aw, name=name)

    # def run(self):
    #     self._started.set()


class TaskQueue(BaseTaskGroup):
    _send_stream: MemoryObjectSendStream[Awaitable]
    _rece_stream: MemoryObjectReceiveStream[Awaitable]

    def __init__(self):
        super().__init__()
        self._crash_reason = None
        self._tg = anyio.create_task_group()

        self._tasks = set()

    def add(self, aw: Awaitable, name: str | None = None):
        self._send_stream.send_nowait(aw)
