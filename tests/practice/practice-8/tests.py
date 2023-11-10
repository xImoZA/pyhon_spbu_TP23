from src.practice.practice_8.hash_table import *
import pytest
from collections import Counter


def get_hash_table(*args):
    hash_table = create_hash_table()
    for node in args:
        put(hash_table, node[0], node[1])
    return hash_table


def get_big_table(size):
    hash_table = create_hash_table()
    for char in range(size):
        put(hash_table, str(char), char)
    return hash_table


@pytest.mark.parametrize(
    "output",
    [get_hash_table()],
)
def test_create_hash_table(output):
    assert create_hash_table() == output


@pytest.mark.parametrize(
    "table,empty_table",
    [
        (get_hash_table(), get_hash_table()),
        (get_hash_table(("Eren Yeager", "without head")), get_hash_table()),
        (
            get_hash_table(("Eren Yeager", "without head"), ("Tony Stark", "dead")),
            get_hash_table(),
        ),
    ],
)
def test_delete_hash_table(table, empty_table):
    delete_hash_table(table)
    assert table == empty_table


@pytest.mark.parametrize(
    "table,key,value,result_table",
    [
        (get_hash_table(), "", "", get_hash_table(("", ""))),
        (
            get_hash_table(),
            "Eren Yeager",
            "without head",
            get_hash_table(("Eren Yeager", "without head")),
        ),
        (
            get_hash_table(("Eren Yeager", "without head")),
            "Tony Stark",
            "dead",
            get_hash_table(("Eren Yeager", "without head"), ("Tony Stark", "dead")),
        ),
        (get_big_table(9), "10", 10, get_big_table(10)),
    ],
)
def test_put(table, key, value, result_table):
    put(table, key, value)
    assert table == result_table


@pytest.mark.parametrize(
    "table,key,result_table",
    [
        (get_hash_table(("", "")), "", get_hash_table()),
        (
            get_hash_table(("Eren Yeager", "without head")),
            "Eren Yeager",
            get_hash_table(),
        ),
        (
            get_hash_table(("Eren Yeager", "without head"), ("Tony Stark", "dead")),
            "Tony Stark",
            get_hash_table(("Eren Yeager", "without head")),
        ),
    ],
)
def test_remove(table, key, result_table):
    remove(table, key)
    assert table == result_table


@pytest.mark.parametrize(
    "table,key",
    [
        (get_hash_table(), "Eren Yeager"),
        (get_hash_table(("Eren Yeager", "without head")), "Tony Stark"),
    ],
)
def test_errors_remove(table, key):
    with pytest.raises(ValueError):
        remove(table, key)


@pytest.mark.parametrize(
    "table,key,value",
    [
        (get_hash_table(("", "")), "", ""),
        (
            get_hash_table(("Eren Yeager", "without head")),
            "Eren Yeager",
            "without head",
        ),
        (
            get_hash_table(("Eren Yeager", "without head"), ("Tony Stark", "dead")),
            "Tony Stark",
            "dead",
        ),
    ],
)
def test_get(table, key, value):
    assert get(table, key) == value


@pytest.mark.parametrize(
    "table,key,result",
    [
        (get_hash_table(("", "")), "", True),
        (get_hash_table(("Eren Yeager", "without head")), "Eren Yeager", True),
        (get_hash_table(("Eren Yeager", "without head")), "Tony Stark", False),
    ],
)
def test_has_key(table, key, result):
    assert has_key(table, key) == result


@pytest.mark.parametrize(
    "table,result",
    [
        (get_hash_table(("", "")), [("", "")]),
        (
            get_hash_table(("Eren Yeager", "without head")),
            [("Eren Yeager", "without head")],
        ),
        (
            get_hash_table(("Eren Yeager", "without head"), ("Tony Stark", "dead")),
            [("Eren Yeager", "without head"), ("Tony Stark", "dead")],
        ),
    ],
)
def test_items(table, result):
    assert Counter(items(table)) == Counter(result)
