from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import Any, TypeVar

from types import FrameType, TracebackType

T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)

ExcInfo = tuple[type[BaseException], BaseException, TracebackType]
OptExcInfo = ExcInfo | tuple[None, None, None]

# Objects suitable to be passed to sys.setprofile, threading.setprofile, and similar
ProfileFunction = Callable[[FrameType, str, Any], object]
# Objects suitable to be passed to sys.settrace, threading.settrace, and similar
# TraceFunction = Callable[[FrameType, str, Any], "TraceFunction" | None]

AsyncSend = Callable[[T], Awaitable[None]]
AsyncThrow = Callable[[Exception], Awaitable[None]]
AsyncClose = Callable[[], Awaitable[None]]
