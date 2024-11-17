from __future__ import annotations

from typing import TYPE_CHECKING

from datetime import timedelta
from functools import singledispatch

if TYPE_CHECKING:
    from rekki.typing import Millisecond, Second


@singledispatch
def want_second(s: Second) -> float:
    """Convert :data:`Second` to float."""
    raise TypeError(f"Unexpected type {type(s)}")


@want_second.register(int)
@want_second.register(float)
def _want_second_float(s: int | float) -> float:
    return float(s)


@want_second.register(timedelta)
def _want_second_timedelta(s: timedelta) -> float:
    return s.total_seconds()


@singledispatch
def want_millisecond(ms: Millisecond) -> float:
    """Convert :data:`Millisecond` to float."""
    raise TypeError(f"Unexpected type {type(ms)}")


@want_millisecond.register(int)
@want_millisecond.register(float)
def _want_millisecond_float(ms: int | float) -> float:
    return float(ms)


@want_millisecond.register(timedelta)
def _want_millisecond_timedelta(ms: timedelta) -> float:
    return ms.total_seconds() * 1000
