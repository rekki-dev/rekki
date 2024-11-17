from __future__ import annotations


class Arbiter(ActorT):
    """A special actor who knows all the other actors and always has
    access to a top level nursery.
    The arbiter is by default the first actor spawned on each host
    and is responsible for keeping track of all other actors for
    coordination purposes. If a new main process is launched and an
    arbiter is already running that arbiter will be used.

    > https://github.com/goodboy/tractor/blob/6a0337b69d660378fc19a598d771016cb64a71cc/tractor/_runtime.py#L1596
    """

    is_arbiter = True
