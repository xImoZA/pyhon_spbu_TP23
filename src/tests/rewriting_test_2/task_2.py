import datetime
import functools
import inspect
from typing import Callable, Iterator


def write_in_file(
    file_name: str, day: str, time: str, name: str, parameters: list[str], result: str
) -> None:
    with open(file_name, "a") as output_file:
        output_file.writelines(f"{day} {time} {name} {' '.join(parameters)} {result}\n")


def clear_file(file_name: str) -> None:
    with open(file_name, "w") as file:
        file.truncate(0)


def logger(file_path: str) -> Callable:
    clear_file(file_path)

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def inner(*args, **kwargs) -> Callable:
            time = datetime.datetime.now()
            start_day = f"{time.day}/{time.month}/{time.year}"
            start_time = f"{time.hour}:{time.minute}:{time.second}"

            true_order = inspect.getcallargs(func, *args, *kwargs.values())
            parameters = inspect.getcallargs(func, *args, **kwargs)
            for i in true_order.keys():
                true_order[i] = parameters[i]

            parameters = [f"{item[0]}={item[1]}" for item in true_order.items()]
            result = func(*args, **kwargs)

            write_in_file(
                file_path, start_day, start_time, func.__name__, parameters, str(result)
            )

            return result

        return inner

    return decorator
