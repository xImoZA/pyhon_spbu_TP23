from io import StringIO

from src.homeworks.homework_6.task_2 import *
from src.homeworks.homework_6.AVL import *
from tests.homeworks.homework_6.test_AVL.test_AVL import create_test_tree
import pytest


file_logs = "tests/homeworks/homework_6/test_streets/streets_logs.txt"
file_results = "tests/homeworks/homework_6/test_streets/streets_results.txt"
my_result = "tests/homeworks/homework_6/test_streets/my_result.txt"


def test_static():
    static_mode(file_logs, my_result)

    with open(file_results, "r") as results, open(my_result, "r") as output:
        for line in results:
            assert line == output.readline()


@pytest.mark.parametrize(
    "user_input,expected",
    [
        (
            ["2", "EXIT"],
            "To exit program enter EXIT\nIncorrect command\n",
        ),
        (
            ["2", "Ilovepython", "EXIT"],
            "To exit program enter EXIT\nIncorrect command\nIncorrect command\n",
        ),
        (
            ["2", "CREATE ONLY THREE ARGS", "EXIT"],
            "To exit program enter EXIT\nIncorrect command\nIncorrect command\n",
        ),
    ],
)
def test_main(monkeypatch, user_input, expected) -> None:
    monkeypatch.setattr("builtins.input", lambda _: user_input.pop(0))
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    interactive_mode()
    output = fake_output.getvalue()
    assert output == expected


@pytest.mark.parametrize(
    "user_input,expected",
    [
        (
            ["1", "EXIT"],
            "1) Read the file and create new file with result\n2) Interactive mode\nFile EXIT not exist\n",
        ),
        (
            ["1", "Ilovepython", "EXIT"],
            "1) Read the file and create new file with result\n2) Interactive mode\nFile Ilovepython not exist\n",
        ),
        (
            ["1", "CREATE ONLY THREE ARGS", "EXIT"],
            "1) Read the file and create new file with result\n2) Interactive mode\nFile CREATE ONLY THREE ARGS not exist\n",
        ),
    ],
)
def test_main(monkeypatch, user_input, expected) -> None:
    monkeypatch.setattr("builtins.input", lambda _: user_input.pop(0))
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == expected
