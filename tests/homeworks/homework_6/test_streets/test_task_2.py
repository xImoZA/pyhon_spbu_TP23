from io import StringIO
from src.homeworks.homework_6.task_2 import *
from src.homeworks.homework_6.AVL import *
from collections import Counter
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


@pytest.mark.parametrize(
    "tree_1,tree_2,expected",
    [
        (
            # ключи первого строго меньше ключей второго и высота первого меньше второго
            create_test_tree((2, 2), (1, 1), (3, 3), (4, 4)),
            create_test_tree(
                (8, 8), (6, 6), (10, 10), (5, 5), (7, 7), (9, 9), (11, 11)
            ),
            create_test_tree(
                (8, 8),
                (4, 4),
                (10, 10),
                (9, 9),
                (11, 11),
                (2, 2),
                (6, 6),
                (1, 1),
                (3, 3),
                (5, 5),
                (7, 7),
            ),
        ),
        (
            # ключи второго строго меньше ключей первого и высота второго меньше первого
            create_test_tree(
                (8, 8), (6, 6), (10, 10), (5, 5), (7, 7), (9, 9), (11, 11)
            ),
            create_test_tree((2, 2), (1, 1), (3, 3), (4, 4)),
            create_test_tree(
                (8, 8),
                (4, 4),
                (10, 10),
                (9, 9),
                (11, 11),
                (2, 2),
                (6, 6),
                (1, 1),
                (3, 3),
                (5, 5),
                (7, 7),
            ),
        ),
        (
            # ключи первого строго меньше ключей второго и высота первого больше второго
            create_test_tree((4, 4), (2, 2), (6, 6), (1, 1), (3, 3), (5, 5), (7, 7)),
            create_test_tree((9, 9), (8, 8), (10, 10)),
            create_test_tree(
                (4, 4),
                (2, 2),
                (7, 7),
                (1, 1),
                (3, 3),
                (6, 6),
                (9, 9),
                (5, 5),
                (8, 8),
                (10, 10),
            ),
        ),
        (
            # ключи второго строго меньше ключей первого и высота второго больше первого
            create_test_tree((9, 9), (8, 8), (10, 10)),
            create_test_tree((4, 4), (2, 2), (6, 6), (1, 1), (3, 3), (5, 5), (7, 7)),
            create_test_tree(
                (4, 4),
                (2, 2),
                (7, 7),
                (1, 1),
                (3, 3),
                (6, 6),
                (9, 9),
                (5, 5),
                (8, 8),
                (10, 10),
            ),
        ),
        (
            create_test_tree((7, 7), (1, 1), (10, 10), (9, 9)),
            create_test_tree((8, 8), (5, 5), (15, 15)),
            create_test_tree(
                (7, 7), (1, 1), (10, 10), (9, 9), (5, 5), (15, 15), (8, 8)
            ),
        ),
    ],
)
def test_merge(tree_1, tree_2, expected):
    actual_tree = merge(tree_1, tree_2)
    assert actual_tree == expected


@pytest.mark.parametrize(
    "tree,key,small_tree,big_tree",
    [
        (
            create_test_tree((4, 4), (2, 2), (6, 6), (1, 1), (3, 3), (5, 5), (7, 7)),
            4,
            create_test_tree((2, 2), (1, 1), (3, 3)),
            create_test_tree((6, 6), (5, 5), (7, 7), (4, 4)),
        ),
        (
            create_test_tree(
                (30, 30),
                (20, 20),
                (39, 39),
                (15, 15),
                (25, 25),
                (36, 36),
                (43, 43),
                (1, 1),
                (23, 23),
                (28, 28),
                (42, 42),
                (50, 50),
            ),
            20,
            create_test_tree((1, 1), (15, 15)),
            create_test_tree(
                (39, 39),
                (28, 28),
                (43, 43),
                (23, 23),
                (36, 36),
                (42, 42),
                (50, 50),
                (20, 20),
                (25, 25),
                (30, 30),
            ),
        ),
        (
            create_test_tree(
                (30, 30),
                (20, 20),
                (39, 39),
                (15, 15),
                (25, 25),
                (36, 36),
                (43, 43),
                (1, 1),
                (23, 23),
                (28, 28),
                (42, 42),
                (50, 50),
            ),
            39,
            create_test_tree(
                (20, 20),
                (15, 15),
                (25, 25),
                (1, 1),
                (23, 23),
                (30, 30),
                (28, 28),
                (36, 36),
            ),
            create_test_tree((43, 43), (42, 42), (50, 50), (39, 39)),
        ),
    ],
)
def test_split(tree, key, small_tree, big_tree):
    actual_small, actual_big = split(tree, key)
    assert actual_big == big_tree and actual_small == small_tree


@pytest.mark.parametrize(
    "tree,left,right,keys",
    [
        (
            create_test_tree((4, 4), (2, 2), (6, 6), (1, 1), (3, 3), (5, 5), (7, 7)),
            1,
            4,
            [1, 2, 3],
        ),
        (
            create_test_tree((4, 4), (2, 2), (6, 6), (1, 1), (3, 3), (5, 5), (7, 7)),
            1,
            6,
            [1, 2, 3, 4, 5],
        ),
        (
            create_test_tree((4, 4), (2, 2), (6, 6), (1, 1), (3, 3), (5, 5), (7, 7)),
            3,
            6,
            [3, 4, 5],
        ),
    ],
)
def test_get_all(tree, left, right, keys):
    actual_keys = get_all(tree, left, right)
    assert Counter(actual_keys) == Counter(keys)
