from dataclasses import dataclass
from typing import TypeVar, Generic, Optional
import sys

sys.setrecursionlimit(10**6)

V = TypeVar("V")
K = TypeVar("K")


@dataclass
class HashNode(Generic[K, V]):
    key: Optional[K]
    value: Optional[V]
    next: Optional["HashNode[K, V]"]


@dataclass
class HashList(Generic[K, V]):
    index: int
    element: Optional["HashNode[K, V]"]
    next: Optional["HashList[K, V]"]


@dataclass
class HashTable(Generic[K, V]):
    capacity: int
    size: int
    table: Optional[HashList[K, V]]


def create_hash_table() -> HashTable:
    return HashTable(128, 0, create_list(128))


def create_list(size, counter=0) -> HashList:
    if counter == size - 1:
        return HashList(counter, None, None)

    return HashList(counter, None, create_list(size, counter=counter + 1))


def delete_hash_table(hash_table: HashTable) -> None:
    list_items = items(hash_table)
    for pair in list_items:
        remove(hash_table, pair[0])


def put(hash_table: HashTable, key: K, value: V) -> None:
    index = hash(key) % hash_table.capacity

    if not has_key(hash_table, key):
        hash_table.size += 1

    hash_table.table = put_in_list(hash_table.table, index, key, value)

    if hash_table.size / hash_table.capacity >= 0.8:
        hash_table.capacity *= 2
        hash_table.table = create_bigger_list(hash_table)


def put_in_list(cur_list: HashList, index: int, key: K, value: V) -> HashList:
    if cur_list.index == index:

        def put_in_node(cur_node: HashNode) -> HashNode:
            if cur_node is None:
                return HashNode(key, value, None)

            elif cur_node.key == key:
                cur_node.value = value
                return cur_node

            cur_node.next = put_in_node(cur_node.next)
            return cur_node

        cur_list.element = put_in_node(cur_list.element)
        return cur_list

    cur_list.next = put_in_list(cur_list.next, index, key, value)
    return cur_list


def create_bigger_list(hash_table: HashTable) -> HashList:
    new_list = create_list(hash_table.capacity * 2)
    list_items = items(hash_table)

    for pair in list_items:
        index = hash(pair[0]) % (hash_table.capacity * 2)
        put_in_list(new_list, index, pair[0], pair[1])

    return new_list


def remove(hash_table: HashTable, key: K) -> V:
    if not has_key(hash_table, key):
        raise ValueError("This key does not exist")

    index = hash(key) % hash_table.capacity

    def remove_in_list(cur_list: HashList) -> (HashList, V):
        if cur_list.index == index:

            def remove_in_node(cur_node: HashNode) -> (HashNode, V):
                if cur_node.key == key:
                    return cur_node.next, cur_node.value

                cur_node.next, cur_value = remove_in_node(cur_node.next)
                return cur_node, cur_value

            cur_list.element, recur_value = remove_in_node(cur_list.element)
            return cur_list, recur_value

        cur_list.next, recursion_value = remove_in_list(cur_list.next)
        return cur_list, recursion_value

    hash_table.table, value = remove_in_list(hash_table.table)
    hash_table.size -= 1
    return value


def get(hash_table: HashTable, key: K) -> V:
    if not has_key(hash_table, key):
        raise ValueError("This key does not exist")

    index = hash(key) % hash_table.capacity

    def get_in_list(cur_list: HashList) -> V:
        if cur_list.index == index:

            def get_in_node(cur_node: HashNode) -> V:
                if cur_node.key == key:
                    return cur_node.value

                return get_in_node(cur_node.next)

            return get_in_node(cur_list.element)

        return get_in_list(cur_list.next)

    return get_in_list(hash_table.table)


def has_key(hash_table: HashTable, key: K) -> bool:
    if hash_table.size == 0:
        return False

    index = hash(key) % hash_table.capacity

    def has_key_list(cur_list: HashList) -> bool:
        if cur_list.index > index:
            return False

        elif cur_list.index == index:

            def has_key_in_node(cur_node: HashNode) -> bool:
                if cur_node is None:
                    return False

                elif cur_node.key == key:
                    return True

                return has_key_in_node(cur_node.next)

            return has_key_in_node(cur_list.element)

        return has_key_list(cur_list.next)

    return has_key_list(hash_table.table)


def items(hash_table: HashTable) -> list[tuple[K, V]]:
    list_pair = []

    def items_in_list(cur_list: HashList) -> None:
        if len(list_pair) < hash_table.size:
            if cur_list.element:

                def items_in_node(cur_node: HashNode) -> None:
                    if cur_node is not None:
                        list_pair.append((cur_node.key, cur_node.value))
                        items_in_node(cur_node.next)

                items_in_node(cur_list.element)

            items_in_list(cur_list.next)

    items_in_list(hash_table.table)
    return list_pair
