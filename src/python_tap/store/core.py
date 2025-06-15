from collections.abc import Callable, Generator

_stored_taps: dict[str, Callable | None] = {}


def add(fn: Callable) -> None:
    key = fn.__name__

    _stored_taps[key] = fn


def remove(fn: Callable) -> None:
    key = fn.__name__

    _stored_taps[key] = None


def get() -> Generator[Callable]:
    return (v for v in _stored_taps.values() if v)
