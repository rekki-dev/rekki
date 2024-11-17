"""Text and string manipulation utilities."""

from __future__ import annotations

from collections.abc import Iterable
from typing import AnyStr

__all__ = (
    "abbr",
    "abbr_fqdn",
    "enumeration",
    "maybe_concat",
    "pluralize",
    "shorten_fqdn",
    "title",
    "want_bytes",
    "want_str",
)


def want_bytes(s: AnyStr) -> bytes:
    """Convert string to bytes."""
    if isinstance(s, str):
        return s.encode()
    return s


def want_str(s: AnyStr) -> str:
    """Convert bytes to string."""
    if isinstance(s, bytes):
        return s.decode()
    return s


def title(s: str) -> str:
    """Capitalize sentence.

    ``"foo bar" -> "Foo Bar"``

    ``"foo-bar" -> "Foo Bar"``
    """
    return " ".join(
        p.capitalize() for p in s.replace("-", " ").replace("_", " ").split()
    )


def enumeration(
    items: Iterable[str],
    *,
    start: int = 1,
    sep: str = "\n",
    template: str = "{index}) {item}",
) -> str:
    r"""Enumerate list of strings.

    Example:
        >>> enumeration(["x", "y", "..."])
        "1) x\n2) y\n3) ..."
    """
    return sep.join(
        template.format(index=index, item=item)
        for index, item in enumerate(items, start=start)
    )


def _abbr_word_boundary(s: str, max: int, suffix: str) -> str:
    # Do not cut-off any words, but means the limit is even harder
    # and we won't include any partial words.
    if len(s) > max:
        return (suffix and (s[: max - len(suffix)] + suffix)) or s[:max]
    return s


def _abbr_abrupt(s: str, max: int, suffix: str = "...") -> str:
    # hard limit (can cut off in the middle of a word).
    if max and len(s) >= max:
        return s[:max].rsplit(" ", 1)[0] + suffix
    return s


def abbr(s: str, max: int, suffix: str = "...", words: bool = False) -> str:
    """Abbreviate word."""
    if words:
        return _abbr_word_boundary(s, max, suffix)
    return _abbr_abrupt(s, max, suffix)


def abbr_fqdn(origin: str, name: str, *, prefix: str = "") -> str:
    """Abbreviate fully-qualified Python name, by removing origin.

    ``app.origin`` is the package where the app is defined,
    so if this is ``examples.simple``::

        >>> app.origin
        'examples.simple'
        >>> abbr_fqdn(app.origin, 'examples.simple.Withdrawal', prefix='[...]')
        '[...]Withdrawal'

        >>> abbr_fqdn(app.origin, 'examples.other.Foo', prefix='[...]')
        'examples.other.foo'

    :func:`shorten_fqdn` is similar, but will always shorten a too long name,
    abbr_fqdn will only remove the origin portion of the name.
    """
    if name.startswith(origin):
        name = name[len(origin) + 1 :]
        return f"{prefix}{name}"
    return name


def shorten_fqdn(s: str, max: int = 32) -> str:
    """Shorten fully-qualified Python name (like "os.path.isdir")."""
    if len(s) > max:
        module, sep, cls = s.rpartition(".")
        if sep:
            module = abbr(module, max - len(cls) - 3, "", words=True)
            return module + "[.]" + cls
    return s


def pluralize(n: int, text: str, suffix: str = "s") -> str:
    """Pluralize term when n is greater than one."""
    if n != 1:
        return text + suffix
    return text


def maybe_concat(s: AnyStr | None, suffix: str = "", *, prefix: str = "") -> str | None:
    """Concatenate string only if existing string ``s`` is defined.

    Keyword Arguments:
        suffix: add suffix if string ``s`` is defined.
        prefix: add prefix is string ``s`` is defined.
    """
    if s is not None:
        return prefix + want_str(s) + suffix
    return s
