from __future__ import annotations


class LifecycleT:
    """Lifecycle interface.

    When calling ``await service.start()`` this happens:

    .. code-block:: text

        +--------------------+
        | INIT (not started) |
        +--------------------+
                V
        +--------------------+
        | on_pre_start       |
        +--------------------+
                V
        .-----------------------.
        / await service.start() |
        `-----------------------'
                V
        +--------------------+
        | on_first_start     |
        +--------------------+
                V
        +--------------------+
        | on_start           |
        +--------------------+
                V
        +--------------------+
        | on_started         |
        +--------------------+

    When stopping and ``wait_for_shutdown`` is unset, this happens:

    .. code-block:: text

        .-----------------------.
        / await service.stop()  |
        `-----------------------'
                V
        +--------------------+
        | on_stop            |
        +--------------------+
                V
        +--------------------+
        | on_shutdown        |
        +--------------------+

    When stopping and ``wait_for_shutdown`` is set, the stop operation
    will wait for something to set the shutdown flag ``self.set_shutdown()``:

    .. code-block:: text

        .-----------------------.
        / await service.stop()  |
        `-----------------------'
                V
        +--------------------+
        | on_stop             |
        +--------------------+
                V
        .-------------------------.
        / service.set_shutdown()  |
        `-------------------------'
                V
        +--------------------+
        | on_shutdown        |
        +--------------------+

    When restarting the order is as follows (assuming
    ``wait_for_shutdown`` unset):

    .. code-block:: text

        .-------------------------.
        / await service.restart() |
        `-------------------------'
                V
        +--------------------+
        | on_stop             |
        +--------------------+
                V
        +--------------------+
        | on_shutdown        |
        +--------------------+
                V
        +--------------------+
        | on_restart         |
        +--------------------+
                V
        +--------------------+
        | on_start           |
        +--------------------+
                V
        +--------------------+
        | on_started         |
        +--------------------+
    """

    async def start(self): ...
    async def pre_start(self): ...
    async def stop(self): ...
    async def post_stop(self): ...
    async def shutdown(self): ...
    async def restart(self): ...

    async def on_first_start(self) -> None:
        """Service started for the first time in this process."""
        ...

    async def on_start(self) -> None:
        """Service is starting."""
        ...

    async def on_stop(self) -> None:
        """Service is being stopped/restarted."""
        ...

    async def on_shutdown(self) -> None:
        """Service is being stopped/restarted."""
        ...

    async def on_restart(self) -> None:
        """Service is being restarted."""
        ...
