from sys import argv

from AVL import *
from copy import copy


def remove_keys(tree_map: TreeMap[K, V], left: K, right: K) -> None:
    for item in get_items(tree_map, inorder_comparator):
        if left <= item[0] < right:
            remove(tree_map, item[0])


def getAll(tree_map: TreeMap, left: K, right: K) -> list[K]:
    keys = []

    for item in get_items(tree_map, inorder_comparator):
        if left <= item[0] < right:
            keys.append(item[0])

    return keys


def split(tree_map: TreeMap, key: K) -> tuple[TreeMap, TreeMap]:
    smaller_tree = create_tree_map()
    bigger_tree = copy(tree_map)

    smaller_tree.root = get_node_in_tree(tree_map.root, key, get_left_child=True)
    remove_keys(bigger_tree, get_min_in_node(smaller_tree.root)[0], key)
    return smaller_tree, bigger_tree


def add_tree_in_tree(small_tree: TreeMap[K, V], big_tree: TreeMap[K, V]) -> None:
    for item in get_items(small_tree, inorder_comparator):
        put(big_tree, item[0], item[1])


def join(tree_map: TreeMap[K, V], another: TreeMap[K, V]) -> TreeMap[K, V]:
    if another.root.key > get_max(tree_map) or another.root.key < get_min(tree_map):
        put(tree_map, another.root.key, another)
        return tree_map

    if tree_map.root.height > another.root.height:
        add_tree_in_tree(another, tree_map)
        return tree_map

    add_tree_in_tree(tree_map, another)
    return another


def create(tree_map: TreeMap[K, V], address: str, index: str) -> None:
    list_address = address.split()
    put(tree_map, [list_address[0], int(list_address[1]), int(list_address[2])], index)


def get_index(tree_map: TreeMap[K, V], address: str) -> str:
    list_address = address.split()
    return get(tree_map, [list_address[0], int(list_address[1]), int(list_address[2])])


def rename(tree_map: TreeMap[K, V], street: str, new_name: str) -> None:
    for item in get_items(tree_map, inorder_comparator):
        if street == item[0][0]:
            tree_map.root = get_node_in_tree(
                tree_map.root, item, new_key=[new_name, item[1], item[2]]
            )


def delete_block(tree_map: TreeMap[K, V], address: str) -> None:
    list_address = address.split()
    remove(tree_map, [list_address[0], int(list_address[1]), int(list_address[2])])


def delete_house(tree_map: TreeMap[K, V], address: str) -> None:
    list_address = address.split()

    for item in get_items(tree_map, inorder_comparator):
        if item[0][0] == list_address[0] and item[0][1] == int(list_address[1]):
            remove(tree_map, item)


def delete_street(tree_map: TreeMap[K, V], address: str) -> None:
    list_address = address.split()

    for item in get_items(tree_map, inorder_comparator):
        if item[0][0] == list_address[0]:
            remove(tree_map, item)


def get_list(tree_map: TreeMap[K, V], address_1: str, address_2: str) -> list[K]:
    list_address_1 = map(lambda x: [x[0], int(x[1]), int(x[2])], address_1.split())
    list_address_2 = map(lambda x: [x[0], int(x[1]), int(x[2])], address_2.split())

    return getAll(tree_map, list_address_1, list_address_2)


#
# def main():
#     f, g = argv[1:]
