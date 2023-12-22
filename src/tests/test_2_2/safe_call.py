import functools
import sys
import traceback
import warnings
from typing import Callable, Optional


def get_info():
    info = traceback.extract_tb(sys.exc_info()[2])[-1]
    return info.name, info.lineno, info.line


def safe_call(func: Callable) -> Optional[Callable]:
    @functools.wraps(func)
    def inner(*args, **kwargs) -> Optional[Callable]:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            function_name, line_number, line = get_info()
            warnings.warn(
                f"\nFunction: {function_name}\nType of Exception: {e.__class__.__name__}\nMessage: {e}\nIn line {line_number}: {line}",
                category=Warning,
            )

    return inner


@safe_call
def foo():
    def goo():
        print("a" + 1)

    goo()


foo()
