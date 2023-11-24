import pytest
from src.tests.test_2.task_2 import *


@spy
def foo_args(a, b):
    return a, b


def test_print_usage_statistic():
    result = []
    for i in range(10):
        foo_args(i, i + 1)
        time = datetime.datetime.now()
        start_time = f"{time.day}.{time.month}.{time.year} {time.hour}:{time.minute}"
        result.append((start_time, {"a": i, "b": i + 1}))

    assert list(print_usage_statistic(foo_args)) == result


@spy
def foo_kwargs(a, b, **kwargs):
    return a, b


def test_print_usage_statistic_with_kwargs():
    result = []
    for i in range(10):
        foo_kwargs(i, i + 1, c="𓆏")
        time = datetime.datetime.now()
        start_time = f"{time.day}.{time.month}.{time.year} {time.hour}:{time.minute}"
        result.append((start_time, {"a": i, "b": i + 1, "kwargs": {"c": "𓆏"}}))

    assert list(print_usage_statistic(foo_kwargs)) == result


def foo_error(a, b):
    return a, b


def test_errors_print_usage_statistic() -> None:
    for _ in range(3):
        foo_error("𓆏", "お尻")

    with pytest.raises(AttributeError):
        list(print_usage_statistic(foo_error))
