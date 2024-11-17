## FAQ

### Child actors are stopped when parent is restarting

Child actors are often started in a setup block that is run again when the
parent actor is restarted. The child actors will be stopped and new child actors
will be created each time while the parent is restarted.

If child actors are created from setup like in the previous example and they
should remain intact (not stopped) when parent is restarted the supervise should
be placed inside the setup and using
SupervisorStrategy.restart.withStopChildren(false) like this:
