from collections.abc import Callable
from functools import partial


def wrapper(fn: Callable, *args, **kwargs):
    return fn(*args, **kwargs)


def tap(fn: Callable) -> Callable:
    return partial(wrapper, fn)
