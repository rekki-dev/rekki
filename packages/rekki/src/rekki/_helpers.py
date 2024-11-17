from __future__ import annotations

from typing import Callable


def get_callable_name(func: Callable) -> str:
    module = getattr(func, "__module__", None)
    qualname = getattr(func, "__qualname__", None)
    return ".".join([x for x in (module, qualname) if x])
