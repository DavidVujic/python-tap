from collections.abc import Callable, Generator

taps: dict[str, Callable | None] = {}


def add_tap(fn: Callable) -> None:
    key = fn.__name__

    taps[key] = fn


def remove_tap(fn: Callable) -> None:
    key = fn.__name__

    taps[key] = None


def get_taps() -> Generator[Callable]:
    return (v for v in taps.values() if v)
