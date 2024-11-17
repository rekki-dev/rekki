from __future__ import annotations

from collections.abc import Callable
from typing import Any

from types import FrameType, TracebackType

type ExcInfo = tuple[type[BaseException], BaseException, TracebackType]
type OptExcInfo = ExcInfo | tuple[None, None, None]

# Objects suitable to be passed to sys.setprofile, threading.setprofile, and similar
type ProfileFunction = Callable[[FrameType, str, Any], object]

# Objects suitable to be passed to sys.settrace, threading.settrace, and similar
type TraceFunction = Callable[[FrameType, str, Any], "TraceFunction" | None]
