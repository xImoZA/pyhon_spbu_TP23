from src.homeworks.homework_6.task_1 import *
from src.homeworks.homework_6.AVL import *
import pytest


def get_tree(*args):
    tree = create_tree_map()
    for node in args:
        put(tree, node[0], node[1])
    return tree


@pytest.mark.parametrize(
    "source_tree,size,count,result_tree",
    [
        (get_tree((4, 2)), 5, 3, get_tree((4, 2), (5, 3))),
        (get_tree((4, 1), (2, 3)), 4, 4, get_tree((4, 5), (2, 3))),
        (get_tree((4, 2)), 0, 3, get_tree((4, 2), (0, 3))),
    ],
)
def test_add(source_tree, size, count, result_tree):
    add(source_tree, size, count)
    assert source_tree == result_tree


@pytest.mark.parametrize(
    "source_tree,size,out_str",
    [
        (get_tree((4, 2)), 5, "0\n"),
        (get_tree((4, 1), (2, 3)), 4, "1\n"),
        (get_tree((4, 2)), 0, "0\n"),
        (get_tree((4, 5), (2, 3)), 4, "5\n"),
    ],
)
def test_count(source_tree, size, out_str):
    assert get_count(source_tree, size) == out_str


@pytest.mark.parametrize(
    "source_tree,size,out_str,result_tree",
    [
        (get_tree((4, 2)), 5, "SORRY\n", (get_tree((4, 2)))),
        (get_tree((4, 1), (2, 3)), 4, "4\n", get_tree((2, 3))),
        (get_tree((4, 2)), 0, "4\n", get_tree((4, 1))),
        (get_tree((4, 5), (2, 3)), 3, "4\n", get_tree((4, 4), (2, 3))),
    ],
)
def test_select(source_tree, size, out_str, result_tree):
    assert select(source_tree, size) == out_str and source_tree == result_tree


def test_read_file_result():
    result_list = read_file("tests/homeworks/homework_6/test_shopping/shop_logs.txt")[1]
    with open(
        "tests/homeworks/homework_6/test_shopping/shop_results.txt", "r"
    ) as result:
        for i in range(len(result_list)):
            assert result_list[i] == result.readline()


def test_balance_result():
    balance_list = list(
        map(
            lambda item: f"{item[0]} {item[1]}\n",
            get_items(
                read_file("tests/homeworks/homework_6/test_shopping/shop_logs.txt")[0],
                inorder_comparator,
            ),
        )
    )
    with open(
        "tests/homeworks/homework_6/test_shopping/shop_balance.txt", "r"
    ) as balance:
        for i in range(len(balance_list)):
            assert balance_list[i] == balance.readline()
