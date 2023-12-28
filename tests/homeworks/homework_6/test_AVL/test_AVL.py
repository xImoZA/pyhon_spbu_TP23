from random import randint
from src.homeworks.homework_6.AVL import _balance_factor
from src.homeworks.homework_6.AVL import *
import pytest


def create_test_tree(*args):
    tree = create_tree_map()
    for key, value in args:
        put(tree, key, value)
    return tree


@pytest.mark.parametrize(
    "output",
    [create_test_tree()],
)
def test_create_tree_map(output):
    actual = create_tree_map()
    assert actual == output


@pytest.mark.parametrize(
    "source_tree",
    [
        create_test_tree((4, "*")),
        create_test_tree((4, "*"), (2, "+")),
        create_test_tree((4, "*"), (2, "+"), (1, "x")),
        create_test_tree((4, "*"), (2, "+"), (1, "x"), (6, "-")),
        create_test_tree((4, "*"), (2, "+"), (1, "x"), (6, "-"), (5, "w")),
    ],
)
def test_delete_tree_map(source_tree):
    delete_tree_map(source_tree)
    assert source_tree == create_test_tree()


@pytest.mark.parametrize("size", (5, 10, 15, 20, 25, 100))
def test_put(size):
    tree = create_tree_map()

    def test_put_recursion(tree_node):
        assert abs(_balance_factor(tree_node)) < 2
        if tree_node.left_child is not None:
            test_put_recursion(tree_node.left_child)
            assert tree_node.left_child.key < tree_node.key

        if tree_node.right_child is not None:
            test_put_recursion(tree_node.right_child)
            assert tree_node.right_child.key > tree_node.key

    for i in range(size):
        key_value = randint(0, 10000)
        put(tree, key_value, key_value)
        test_put_recursion(tree.root)


@pytest.mark.parametrize(
    "source_tree,key,result_tree",
    [
        (create_test_tree((4, "*")), 4, create_test_tree()),
        (create_test_tree((4, "*"), (2, "+")), 2, create_test_tree((4, "*"))),
        (
            create_test_tree((4, "*"), (2, "+"), (6, "-")),
            4,
            create_test_tree((6, "-"), (2, "+")),
        ),
        (
            create_test_tree(
                (4, "s"), (2, "p"), (1, "A"), (3, "B"), (6, "q"), (5, "C"), (8, "D")
            ),
            2,
            create_test_tree(
                (4, "s"), (3, "B"), (6, "q"), (1, "A"), (5, "C"), (8, "D")
            ),
        ),
        (
            create_test_tree((4, "s"), (3, "B"), (6, "q"), (5, "C"), (8, "D")),
            3,
            create_test_tree((6, "q"), (4, "s"), (8, "D"), (5, "C")),
        ),
    ],
)
def test_remove(source_tree, key, result_tree):
    remove(source_tree, key)
    assert source_tree == result_tree


@pytest.mark.parametrize(
    "source_tree,key",
    [
        (create_test_tree(), 4),
        (create_test_tree((4, "*")), 5),
        (create_test_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 3),
    ],
)
def test_errors_remove(source_tree, key):
    with pytest.raises(ValueError):
        remove(source_tree, key)


@pytest.mark.parametrize(
    "source_tree,key,value",
    [
        (create_test_tree((4, "*"), (1, "x")), 1, "x"),
        (create_test_tree((4, "*"), (2, "+"), (3, "y")), 2, "+"),
        (create_test_tree((4, "*"), (2, "+"), (1, "x"), (3, "y")), 3, "y"),
        (
            create_test_tree(
                (4, "s"), (2, "p"), (1, "A"), (3, "B"), (6, "q"), (5, "C")
            ),
            6,
            "q",
        ),
        (create_test_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 8, "D"),
    ],
)
def test_get(source_tree, key, value):
    actual = get(source_tree, key)
    assert actual == value


@pytest.mark.parametrize(
    "source_tree,key",
    [
        (create_test_tree(), 3),
        (create_test_tree((4, "*"), (2, "+"), (1, "x")), 5),
        (create_test_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 1),
        (create_test_tree((4, "s"), (2, "p"), (1, "A"), (3, "B"), (6, "q")), 8),
    ],
)
def test_errors_get(source_tree, key):
    with pytest.raises(ValueError):
        get(source_tree, key)


@pytest.mark.parametrize(
    "source_tree,key,output_bool",
    [
        (create_test_tree((4, "*"), (2, "+"), (1, "x")), 1, True),
        (create_test_tree((4, "*"), (2, "+"), (3, "y")), 5, False),
        (create_test_tree(), 3, False),
        (create_test_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 1, False),
        (create_test_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 8, True),
    ],
)
def test_has_key(source_tree, key, output_bool):
    actual = has_key(source_tree, key)
    assert actual == output_bool


@pytest.mark.parametrize(
    "source_tree,key,min_key",
    [
        (create_test_tree((4, "*"), (1, "x")), 1, 1),
        (create_test_tree((4, "*"), (2, "+"), (3, "y")), 2, 2),
        (create_test_tree((4, "*"), (2, "+"), (1, "x"), (3, "y")), 3, 3),
        (
            create_test_tree(
                (4, "s"), (2, "p"), (1, "A"), (3, "B"), (7, "q"), (5, "C")
            ),
            6,
            7,
        ),
        (create_test_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 7, 8),
    ],
)
def test_get_lower_bound(source_tree, key, min_key):
    actual = get_lower_bound(source_tree, key)
    assert actual == min_key


@pytest.mark.parametrize(
    "source_tree,key",
    [
        (create_test_tree(), 3),
        (create_test_tree((4, "*"), (2, "+"), (1, "x")), 5),
        (create_test_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 9),
        (create_test_tree((4, "s"), (2, "p"), (1, "A"), (3, "B"), (6, "q")), 8),
    ],
)
def test_errors_get_lower_bound(source_tree, key):
    with pytest.raises(ValueError):
        get_lower_bound(source_tree, key)


@pytest.mark.parametrize(
    "source_tree,key,min_key",
    [
        (create_test_tree((4, "*"), (1, "x")), 1, 4),
        (create_test_tree((4, "*"), (2, "+"), (3, "y")), 2, 3),
        (create_test_tree((4, "*"), (2, "+"), (1, "x"), (3, "y")), 3, 4),
        (
            create_test_tree(
                (4, "s"), (2, "p"), (1, "A"), (3, "B"), (7, "q"), (5, "C")
            ),
            6,
            7,
        ),
        (create_test_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 7, 8),
    ],
)
def test_get_higher_bound(source_tree, key, min_key):
    actual = get_higher_bound(source_tree, key)
    assert actual == min_key


@pytest.mark.parametrize(
    "source_tree,key",
    [
        (create_test_tree(), 3),
        (create_test_tree((4, "*"), (2, "+"), (1, "x")), 5),
        (create_test_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 9),
        (create_test_tree((4, "s"), (2, "p"), (1, "A"), (3, "B"), (6, "q")), 8),
    ],
)
def test_errors_get_lower_bound(source_tree, key):
    with pytest.raises(ValueError):
        get_higher_bound(source_tree, key)


@pytest.mark.parametrize(
    "source_tree,max_key",
    [
        (create_test_tree((4, "*"), (1, "x")), 4),
        (create_test_tree((4, "*"), (2, "+"), (3, "y")), 4),
        (create_test_tree((4, "*"), (2, "+"), (1, "x"), (3, "y")), 4),
        (
            create_test_tree(
                (4, "s"), (2, "p"), (1, "A"), (3, "B"), (7, "q"), (5, "C")
            ),
            7,
        ),
        (create_test_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 8),
    ],
)
def test_get_max(source_tree, max_key):
    actual = get_max(source_tree)
    assert actual == max_key


@pytest.mark.parametrize("source_tree", [create_test_tree()])
def test_errors_get_max(source_tree):
    with pytest.raises(ValueError):
        get_max(source_tree)


@pytest.mark.parametrize(
    "source_tree,max_key",
    [
        (create_test_tree((4, "*"), (1, "x")), 1),
        (create_test_tree((4, "*"), (2, "+"), (3, "y")), 2),
        (create_test_tree((4, "*"), (2, "+"), (1, "x"), (3, "y")), 1),
        (
            create_test_tree(
                (4, "s"), (2, "p"), (1, "A"), (3, "B"), (7, "q"), (5, "C")
            ),
            1,
        ),
        (create_test_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 4),
    ],
)
def test_get_min(source_tree, max_key):
    actual = get_min(source_tree)
    assert actual == max_key


@pytest.mark.parametrize("source_tree", [create_test_tree()])
def test_errors_get_min(source_tree):
    with pytest.raises(ValueError):
        get_min(source_tree)
