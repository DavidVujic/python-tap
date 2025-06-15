from collections.abc import Callable
from functools import partial

from python_tap import store


def wrapper(fn: Callable, *args, **kwargs):
    for tapped in store.get():
        tapped(*args, **kwargs)

    return fn(*args, **kwargs)


def tap(fn: Callable) -> Callable:
    return partial(wrapper, fn)
