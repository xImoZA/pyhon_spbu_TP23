from src.practice.practice_7.BST import *
import pytest


def get_tree(*args):
    tree = create_tree_map()
    for node in args:
        put(tree, node[0], node[1])
    return tree


@pytest.mark.parametrize(
    "output",
    [get_tree()],
)
def test_create_tree_map(output):
    actual = create_tree_map()
    assert actual == output


@pytest.mark.parametrize(
    "source_tree",
    [
        get_tree((4, "*")),
        get_tree((4, "*"), (2, "+")),
        get_tree((4, "*"), (2, "+"), (1, "x")),
        get_tree((4, "*"), (2, "+"), (1, "x"), (6, "-")),
        get_tree((4, "*"), (2, "+"), (1, "x"), (6, "-"), (5, "w")),
    ],
)
def test_delete_tree_map(source_tree):
    delete_tree_map(source_tree)
    assert source_tree == get_tree()


@pytest.mark.parametrize(
    "source_tree,key,value,result_tree",
    [
        (get_tree(), 4, "*", get_tree((4, "*"))),
        (get_tree((4, "*"), (2, "+")), 1, "x", get_tree((4, "*"), (2, "+"), (1, "x"))),
        (get_tree((4, "*"), (2, "+")), 4, "z", get_tree((4, "z"), (2, "+"))),
    ],
)
def test_put(source_tree, key, value, result_tree):
    put(source_tree, key, value)
    assert source_tree == result_tree


@pytest.mark.parametrize(
    "source_tree,key,result_tree",
    [
        (get_tree((4, "*")), 4, get_tree()),
        (get_tree((4, "*"), (2, "+")), 2, get_tree((4, "*"))),
        (get_tree((4, "*"), (2, "+"), (6, "-")), 4, get_tree((6, "-"), (2, "+"))),
    ],
)
def test_remove(source_tree, key, result_tree):
    remove(source_tree, key)
    assert source_tree == result_tree


@pytest.mark.parametrize(
    "source_tree,key",
    [(get_tree(), 4), (get_tree((4, "*")), 5)],
)
def test_errors_remove(source_tree, key):
    with pytest.raises(ValueError):
        remove(source_tree, key)


@pytest.mark.parametrize(
    "source_tree,node",
    [
        (get_tree((4, "*"), (2, "+"), (1, "x")), (1, "x")),
        (get_tree((4, "*"), (2, "+"), (3, "y")), (2, "+")),
        (get_tree((4, "*"), (2, "+"), (1, "x"), (3, "y")), (1, "x")),
    ],
)
def test_get_min(source_tree, node):
    actual = get_min(source_tree.root)
    assert actual == node


@pytest.mark.parametrize("source_tree", [get_tree()])
def test_errors_get_min(source_tree):
    with pytest.raises(ValueError):
        get_min(source_tree.root)


@pytest.mark.parametrize(
    "source_tree,key,value",
    [
        (get_tree((4, "*"), (1, "x")), 1, "x"),
        (get_tree((4, "*"), (2, "+"), (3, "y")), 2, "+"),
        (get_tree((4, "*"), (2, "+"), (1, "x"), (3, "y")), 3, "y"),
    ],
)
def test_get(source_tree, key, value):
    actual = get(source_tree, key)
    assert actual == value


@pytest.mark.parametrize(
    "source_tree,key", [(get_tree(), 3), (get_tree((4, "*"), (2, "+"), (1, "x")), 5)]
)
def test_errors_get(source_tree, key):
    with pytest.raises(ValueError):
        get(source_tree, key)


@pytest.mark.parametrize(
    "source_tree,key,output_bool",
    [
        (get_tree((4, "*"), (2, "+"), (1, "x")), 1, True),
        (get_tree((4, "*"), (2, "+"), (3, "y")), 5, False),
        (get_tree(), 3, False),
    ],
)
def test_get(source_tree, key, output_bool):
    actual = has_key(source_tree, key)
    assert actual == output_bool


@pytest.mark.parametrize(
    "source_tree,traverse_type,output_list",
    [
        (get_tree(), "preorder", None),
        (get_tree(), "inorder", None),
        (get_tree(), "postorder", None),
        (
            get_tree(
                (4, "*"), (2, "+"), (3, "y"), (1, "x"), (6, "-"), (5, "w"), (7, "z")
            ),
            "preorder",
            ["*", "+", "x", "y", "-", "w", "z"],
        ),
        (
            get_tree(
                (4, "*"), (2, "+"), (3, "y"), (1, "x"), (6, "-"), (5, "w"), (7, "z")
            ),
            "inorder",
            ["x", "+", "y", "*", "w", "-", "z"],
        ),
        (
            get_tree(
                (4, "*"), (2, "+"), (3, "y"), (1, "x"), (6, "-"), (5, "w"), (7, "z")
            ),
            "postorder",
            ["x", "y", "+", "w", "z", "-", "*"],
        ),
    ],
)
def test_traverse(source_tree, traverse_type, output_list):
    actual = traverse(source_tree, traverse_type)
    assert actual == output_list
