from src.homeworks.homework_6.AVL import *
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
        (
            get_tree((1, "A"), (2, "p"), (6, "q"), (4, "s")),
            3,
            "B",
            get_tree((1, "A"), (2, "p"), (4, "s"), (3, "B"), (6, "q")),
        ),
        (
            get_tree((1, "A"), (2, "p"), (4, "s"), (3, "B"), (6, "q")),
            5,
            "C",
            get_tree((4, "s"), (2, "p"), (1, "A"), (3, "B"), (6, "q"), (5, "C")),
        ),
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
        (
            get_tree(
                (4, "s"), (2, "p"), (1, "A"), (3, "B"), (6, "q"), (5, "C"), (8, "D")
            ),
            2,
            get_tree((4, "s"), (3, "B"), (6, "q"), (1, "A"), (5, "C"), (8, "D")),
        ),
        (
            get_tree((4, "s"), (3, "B"), (6, "q"), (5, "C"), (8, "D")),
            3,
            get_tree((6, "q"), (4, "s"), (8, "D"), (5, "C")),
        ),
    ],
)
def test_remove(source_tree, key, result_tree):
    remove(source_tree, key)
    assert source_tree == result_tree


@pytest.mark.parametrize(
    "source_tree,key",
    [
        (get_tree(), 4),
        (get_tree((4, "*")), 5),
        (get_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 3),
    ],
)
def test_errors_remove(source_tree, key):
    with pytest.raises(ValueError):
        remove(source_tree, key)


@pytest.mark.parametrize(
    "source_tree,key,value",
    [
        (get_tree((4, "*"), (1, "x")), 1, "x"),
        (get_tree((4, "*"), (2, "+"), (3, "y")), 2, "+"),
        (get_tree((4, "*"), (2, "+"), (1, "x"), (3, "y")), 3, "y"),
        (get_tree((4, "s"), (2, "p"), (1, "A"), (3, "B"), (6, "q"), (5, "C")), 6, "q"),
        (get_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 8, "D"),
    ],
)
def test_get(source_tree, key, value):
    actual = get(source_tree, key)
    assert actual == value


@pytest.mark.parametrize(
    "source_tree,key",
    [
        (get_tree(), 3),
        (get_tree((4, "*"), (2, "+"), (1, "x")), 5),
        (get_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 1),
        (get_tree((4, "s"), (2, "p"), (1, "A"), (3, "B"), (6, "q")), 8),
    ],
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
        (get_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 1, False),
        (get_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 8, True),
    ],
)
def test_has_key(source_tree, key, output_bool):
    actual = has_key(source_tree, key)
    assert actual == output_bool


@pytest.mark.parametrize(
    "source_tree,key,min_key",
    [
        (get_tree((4, "*"), (1, "x")), 1, 1),
        (get_tree((4, "*"), (2, "+"), (3, "y")), 2, 2),
        (get_tree((4, "*"), (2, "+"), (1, "x"), (3, "y")), 3, 3),
        (get_tree((4, "s"), (2, "p"), (1, "A"), (3, "B"), (7, "q"), (5, "C")), 6, 7),
        (get_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 7, 8),
    ],
)
def test_get_lower_bound(source_tree, key, min_key):
    actual = get_lower_bound(source_tree, key)
    assert actual == min_key


@pytest.mark.parametrize(
    "source_tree,key",
    [
        (get_tree(), 3),
        (get_tree((4, "*"), (2, "+"), (1, "x")), 5),
        (get_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 9),
        (get_tree((4, "s"), (2, "p"), (1, "A"), (3, "B"), (6, "q")), 8),
    ],
)
def test_errors_get_lower_bound(source_tree, key):
    with pytest.raises(ValueError):
        get_lower_bound(source_tree, key)


@pytest.mark.parametrize(
    "source_tree,key,min_key",
    [
        (get_tree((4, "*"), (1, "x")), 1, 4),
        (get_tree((4, "*"), (2, "+"), (3, "y")), 2, 3),
        (get_tree((4, "*"), (2, "+"), (1, "x"), (3, "y")), 3, 4),
        (get_tree((4, "s"), (2, "p"), (1, "A"), (3, "B"), (7, "q"), (5, "C")), 6, 7),
        (get_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 7, 8),
    ],
)
def test_get_higher_bound(source_tree, key, min_key):
    actual = get_higher_bound(source_tree, key)
    assert actual == min_key


@pytest.mark.parametrize(
    "source_tree,key",
    [
        (get_tree(), 3),
        (get_tree((4, "*"), (2, "+"), (1, "x")), 5),
        (get_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 9),
        (get_tree((4, "s"), (2, "p"), (1, "A"), (3, "B"), (6, "q")), 8),
    ],
)
def test_errors_get_lower_bound(source_tree, key):
    with pytest.raises(ValueError):
        get_higher_bound(source_tree, key)


@pytest.mark.parametrize(
    "source_tree,max_key",
    [
        (get_tree((4, "*"), (1, "x")), 4),
        (get_tree((4, "*"), (2, "+"), (3, "y")), 4),
        (get_tree((4, "*"), (2, "+"), (1, "x"), (3, "y")), 4),
        (get_tree((4, "s"), (2, "p"), (1, "A"), (3, "B"), (7, "q"), (5, "C")), 7),
        (get_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 8),
    ],
)
def test_get_max(source_tree, max_key):
    actual = get_max(source_tree)
    assert actual == max_key


@pytest.mark.parametrize("source_tree", [get_tree()])
def test_errors_get_max(source_tree):
    with pytest.raises(ValueError):
        get_max(source_tree)


@pytest.mark.parametrize(
    "source_tree,max_key",
    [
        (get_tree((4, "*"), (1, "x")), 1),
        (get_tree((4, "*"), (2, "+"), (3, "y")), 2),
        (get_tree((4, "*"), (2, "+"), (1, "x"), (3, "y")), 1),
        (get_tree((4, "s"), (2, "p"), (1, "A"), (3, "B"), (7, "q"), (5, "C")), 1),
        (get_tree((6, "q"), (4, "s"), (5, "C"), (8, "D")), 4),
    ],
)
def test_get_min(source_tree, max_key):
    actual = get_min(source_tree)
    assert actual == max_key


@pytest.mark.parametrize("source_tree", [get_tree()])
def test_errors_get_min(source_tree):
    with pytest.raises(ValueError):
        get_min(source_tree)
