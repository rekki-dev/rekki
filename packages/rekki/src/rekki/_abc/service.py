from __future__ import annotations

from abc import ABC

from .lifecycle import LifecycleT
from .supervisor import AbstractSupervisor


class AbstractService(ABC, LifecycleT):
    supervisor: AbstractSupervisor
