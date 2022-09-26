from typing import TypeVar, Protocol


T = TypeVar("T")


class Subscriber(Protocol):
    def on_subscribe(self):
        ...

    def on_next(self):
        ...

    def on_error(self):
        ...

    def on_complete(self):
        ...
