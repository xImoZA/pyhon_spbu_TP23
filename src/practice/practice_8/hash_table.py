from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Callable

V = TypeVar("V")
K = TypeVar("K")

DEFAULT_HASH_TABLE_SIZE = 8
LOAD_FACTOR_THRESHOLD = 0.8


@dataclass
class HashNode(Generic[K, V]):
    key: Optional[K]
    value: Optional[V]
    next: Optional["HashNode[K, V]"]


@dataclass
class HashTable(Generic[K, V]):
    capacity: int
    size: int
    buckets: list[Optional[HashNode]]
    not_empty_buckets: list[int]
    hash_fn: Callable[[K], int]


def create_hash_table(function=hash) -> HashTable:
    return HashTable(
        DEFAULT_HASH_TABLE_SIZE, 0, [None] * DEFAULT_HASH_TABLE_SIZE, [], function
    )


def delete_hash_table(hash_table: HashTable) -> None:
    list_items = items(hash_table)
    for pair in list_items:
        remove(hash_table, pair[0])


def put(hash_table: HashTable, key: K, value: V) -> None:
    if not has_key(hash_table, key):
        hash_table.size += 1

    index = hash_table.hash_fn(key) % hash_table.capacity
    if hash_table.buckets[index] is None:
        hash_table.not_empty_buckets.append(index)

    hash_table.buckets[index] = _get_node_in_bucket(
        hash_table.buckets[index], key, value=value
    )

    if load_factor(hash_table) >= LOAD_FACTOR_THRESHOLD:
        resize(hash_table)


def resize(hash_table: HashTable) -> None:
    new_list = [None] * (hash_table.capacity * 2)
    new_not_empty_buckets = []
    list_items = items(hash_table)

    for pair in list_items:
        index = hash_table.hash_fn(pair[0]) % (hash_table.capacity * 2)
        if new_list[index] is None:
            new_not_empty_buckets.append(index)
        new_list[index] = _get_node_in_bucket(new_list[index], pair[0], pair[1])
        remove(hash_table, pair[0])

    del hash_table.buckets
    del hash_table.not_empty_buckets

    hash_table.buckets = new_list
    hash_table.not_empty_buckets = new_not_empty_buckets
    hash_table.capacity *= 2


def load_factor(hash_table: HashTable) -> float:
    return hash_table.size / hash_table.capacity


def _get_node_in_bucket(cur_node: HashNode, key: K, value=None) -> HashNode | None:
    if cur_node is None:
        if value is not None:
            return HashNode(key, value, None)
        return None

    if cur_node.key == key:
        if value is not None:
            cur_node.value = value

        return cur_node
    if value is not None:
        cur_node.next = _get_node_in_bucket(cur_node.next, key, value=value)
        return cur_node
    return _get_node_in_bucket(cur_node.next, key, value=value)


def remove(hash_table: HashTable, key: K) -> V:
    if not has_key(hash_table, key):
        raise ValueError("This key does not exist")

    index = hash_table.hash_fn(key) % hash_table.capacity

    def remove_in_node(cur_node: HashNode) -> (HashNode, V):
        if cur_node.key == key:
            return cur_node.next, cur_node.value

        cur_node.next, cur_value = remove_in_node(cur_node.next)
        return cur_node, cur_value

    hash_table.buckets[index], value = remove_in_node(hash_table.buckets[index])
    hash_table.size -= 1

    if hash_table.buckets[index] is None:
        hash_table.not_empty_buckets.remove(index)

    return value


def get(hash_table: HashTable, key: K) -> V:
    if not has_key(hash_table, key):
        raise ValueError("This key does not exist")

    index = hash_table.hash_fn(key) % hash_table.capacity

    return _get_node_in_bucket(hash_table.buckets[index], key).value


def has_key(hash_table: HashTable, key: K) -> bool:
    if hash_table.size == 0:
        return False

    index = hash_table.hash_fn(key) % hash_table.capacity

    if index not in hash_table.not_empty_buckets:
        return False

    return bool(_get_node_in_bucket(hash_table.buckets[index], key))


def items(hash_table: HashTable) -> list[tuple[K, V]]:
    list_pair = []

    for i in hash_table.not_empty_buckets:

        def items_in_node(cur_node: HashNode) -> None:
            if cur_node is not None:
                list_pair.append((cur_node.key, cur_node.value))
                items_in_node(cur_node.next)

        items_in_node(hash_table.buckets[i])

    return list_pair
