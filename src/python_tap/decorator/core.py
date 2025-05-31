from collections.abc import Callable
from functools import partial

from python_tap.store import get_taps


def wrapper(fn: Callable, *args, **kwargs):
    for tapped in get_taps():
        tapped(*args, **kwargs)

    return fn(*args, **kwargs)


def tap(fn: Callable) -> Callable:
    return partial(wrapper, fn)
