# rekki

Async actor model for Python

What should a Actor do?

- Creating the `Actor` instance as child
- Handling received message
- Managing lifecycles of `Actor`
- Providing scheduling and concurrency

Actors do not share state (i.e. memory), but they may maintain their own
internal state.

## Credits

- thespianpy
- Akka
- tractor
- ray

Messages are sent to an Actor through one of the following methods.

    ! means “fire-and-forget”, e.g. send a message asynchronously and return immediately. Also known as tell.
    ? sends a message asynchronously and returns a Future representing a possible reply. Also known as ask.

Message ordering is guaranteed on a per-sender basis.

- https://blog.orsinium.dev/posts/py/logging/
- https://mypy.readthedocs.io/en/stable/config_file.html
