"""Store function input data."""

import inspect
from collections.abc import Callable
from typing import Any

_storage: dict = {}


def _collect(fn: Callable, args: Any, kwargs: dict) -> dict:  # noqa: ANN401
    params = inspect.signature(fn).parameters

    data = dict(zip(params, args, strict=False))

    return data | kwargs


def _calculate_namespace(fn: Callable) -> str:
    module = fn.__module__
    name = fn.__qualname__

    return f"{module}.{name}"


def store(*args, **kwargs) -> None:  # noqa: ANN002, ANN003
    """Store the input data from a function call."""
    fn = kwargs["tap_fn"]

    ns = _calculate_namespace(fn)
    data = _collect(fn, args, kwargs)

    _storage[ns] = data
