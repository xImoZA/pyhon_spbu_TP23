import datetime
import functools
import inspect
from typing import Callable, Iterator


def spy(func: Callable) -> Callable:
    @functools.wraps(func)
    def inner(*args, **kwargs) -> Callable:
        time = datetime.datetime.now()
        start_time = f"{time.day}.{time.month}.{time.year} {time.hour}:{time.minute}"

        parameters = inspect.getcallargs(func, *args, **kwargs)

        inner.statistic.append((start_time, parameters))

        return func(*args, **kwargs)

    inner.statistic = []

    return inner


def print_usage_statistic(function: Callable) -> Iterator[tuple[str, list]]:
    try:
        for parameter in function.statistic:
            yield parameter

    except AttributeError:
        raise AttributeError(
            "It is impossible to find out the parameters of an undecorated function"
        )
