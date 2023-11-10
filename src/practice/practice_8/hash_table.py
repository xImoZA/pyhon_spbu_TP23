from dataclasses import dataclass
from typing import TypeVar, Generic, Optional


V = TypeVar("V")
K = TypeVar("K")


@dataclass
class HashNode(Generic[K, V]):
    key: Optional[K]
    value: Optional[V]
    next: Optional["HashNode[K, V]"]


@dataclass
class HashTable(Generic[K, V]):
    capacity: int
    size: int
    table: list[Optional[HashNode]]


def create_hash_table() -> HashTable:
    return HashTable(128, 0, [None] * 128)


def delete_hash_table(hash_table: HashTable) -> None:
    list_items = items(hash_table)
    for pair in list_items:
        remove(hash_table, pair[0])


def put(hash_table: HashTable, key: K, value: V) -> None:
    index = hash(key) % hash_table.capacity

    if not has_key(hash_table, key):
        hash_table.size += 1

    def put_in_node(cur_node: HashNode) -> HashNode:
        if cur_node is None:
            return HashNode(key, value, None)

        elif cur_node.key == key:
            cur_node.value = value
            return cur_node

        cur_node.next = put_in_node(cur_node.next)
        return cur_node

    hash_table.table[index] = put_in_node(hash_table.table[index])

    if hash_table.size / hash_table.capacity >= 0.8:
        hash_table.capacity *= 2

        new_list = [None] * (hash_table.capacity * 2)
        list_items = items(hash_table)

        for pair in list_items:
            index = hash(pair[0]) % (hash_table.capacity * 2)
            new_list[index] = put_in_node(new_list[index])
            remove(hash_table, pair[0])

        hash_table.table = new_list


def remove(hash_table: HashTable, key: K) -> V:
    if not has_key(hash_table, key):
        raise ValueError("This key does not exist")

    index = hash(key) % hash_table.capacity

    def remove_in_node(cur_node: HashNode) -> (HashNode, V):
        if cur_node.key == key:
            return cur_node.next, cur_node.value

        cur_node.next, cur_value = remove_in_node(cur_node.next)
        return cur_node, cur_value

    hash_table.table[index], value = remove_in_node(hash_table.table[index])
    hash_table.size -= 1
    return value


def get(hash_table: HashTable, key: K) -> V:
    if not has_key(hash_table, key):
        raise ValueError("This key does not exist")

    index = hash(key) % hash_table.capacity

    def get_in_node(cur_node: HashNode) -> V:
        if cur_node.key == key:
            return cur_node.value

        return get_in_node(cur_node.next)

    return get_in_node(hash_table.table[index])


def has_key(hash_table: HashTable, key: K) -> bool:
    if hash_table.size == 0:
        return False

    index = hash(key) % hash_table.capacity

    def has_key_in_node(cur_node: HashNode) -> bool:
        if cur_node is None:
            return False

        elif cur_node.key == key:
            return True

        return has_key_in_node(cur_node.next)

    return has_key_in_node(hash_table.table[index])


def items(hash_table: HashTable) -> list[tuple[K, V]]:
    list_pair = []

    for i in range(hash_table.capacity):
        if len(list_pair) == hash_table.size:
            break
        if hash_table.table[i] is not None:

            def items_in_node(cur_node: HashNode) -> None:
                if cur_node is not None:
                    list_pair.append((cur_node.key, cur_node.value))
                    items_in_node(cur_node.next)

            items_in_node(hash_table.table[i])

    return list_pair
