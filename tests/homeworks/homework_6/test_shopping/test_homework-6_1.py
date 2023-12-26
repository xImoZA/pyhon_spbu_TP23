from src.homeworks.homework_6.task_1 import *
from src.homeworks.homework_6.AVL import *
from tests.homeworks.homework_6.test_AVL.test_AVL import create_test_tree
import pytest


file_logs = "tests/homeworks/homework_6/test_shopping/shop_logs.txt"
file_results = "tests/homeworks/homework_6/test_shopping/shop_results.txt"
file_balance = "tests/homeworks/homework_6/test_shopping/shop_balance.txt"


@pytest.mark.parametrize(
    "source_tree,size,count,result_tree",
    [
        (create_test_tree((4, 2)), 5, 3, create_test_tree((4, 2), (5, 3))),
        (create_test_tree((4, 1), (2, 3)), 4, 4, create_test_tree((4, 5), (2, 3))),
        (create_test_tree((4, 2)), 0, 3, create_test_tree((4, 2), (0, 3))),
    ],
)
def test_add(source_tree, size, count, result_tree):
    add(source_tree, size, count)
    assert source_tree == result_tree


@pytest.mark.parametrize(
    "source_tree,size,out_str",
    [
        (create_test_tree((4, 2)), 5, "0\n"),
        (create_test_tree((4, 1), (2, 3)), 4, "1\n"),
        (create_test_tree((4, 2)), 0, "0\n"),
        (create_test_tree((4, 5), (2, 3)), 4, "5\n"),
    ],
)
def test_count(source_tree, size, out_str):
    assert get_count(source_tree, size) == out_str


@pytest.mark.parametrize(
    "source_tree,size,out_str,result_tree",
    [
        (create_test_tree((4, 2)), 5, "SORRY\n", (create_test_tree((4, 2)))),
        (create_test_tree((4, 1), (2, 3)), 4, "4\n", create_test_tree((2, 3))),
        (create_test_tree((4, 2)), 0, "4\n", create_test_tree((4, 1))),
        (create_test_tree((4, 5), (2, 3)), 3, "4\n", create_test_tree((4, 4), (2, 3))),
    ],
)
def test_select(source_tree, size, out_str, result_tree):
    assert select(source_tree, size) == out_str and source_tree == result_tree


def test_read_file_result():
    result_list = read_file(file_logs)[1]
    with open(file_results, "r") as result:
        for i in range(len(result_list)):
            assert result_list[i] == result.readline()


def test_balance_result():
    tree = read_file(file_logs)[0]
    balance_list = [
        f"{key} {value}\n" for (key, value) in get_items(tree, inorder_comparator)
    ]
    with open(file_balance, "r") as balance:
        for i in range(len(balance_list)):
            assert balance_list[i] == balance.readline()
