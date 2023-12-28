import operator
from copy import deepcopy
from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Iterable, Callable

V = TypeVar("V")
K = TypeVar("K")


@dataclass
class TreeNode(Generic[K, V]):
    key: K
    value: Optional[V]
    height: int = 1
    left_child: Optional["TreeNode[K, V]"] = None
    right_child: Optional["TreeNode[K, V]"] = None


@dataclass
class TreeMap(Generic[K, V]):
    root: Optional[TreeNode[K, V]] = None
    size: int = 0


def _get_height(node: TreeNode[K, V]) -> int:
    if node is None:
        return 0

    return node.height


def _balance_factor(node: TreeNode[K, V]) -> int:
    return _get_height(node.left_child) - _get_height(node.right_child)


def _fix_height(tree_node: TreeNode[K, V]):
    height_left_child = _get_height(tree_node.left_child)
    height_right_child = _get_height(tree_node.right_child)

    if height_left_child > height_right_child:
        tree_node.height = height_left_child + 1

    else:
        tree_node.height = height_right_child + 1


def _left_small_rotate(tree_node: TreeNode[K, V]) -> TreeNode[K, V]:
    new_node = tree_node.right_child

    tree_node.right_child = new_node.left_child
    new_node.left_child = tree_node

    if new_node.left_child is not None:
        _fix_height(new_node.left_child)

    if new_node.right_child is not None:
        _fix_height(new_node.right_child)

    _fix_height(new_node)
    return new_node


def _right_small_rotate(node: TreeNode[K, V]) -> TreeNode[K, V]:
    new_node = node.left_child

    node.left_child = new_node.right_child
    new_node.right_child = node

    if new_node.left_child is not None:
        _fix_height(new_node.left_child)

    if new_node.right_child is not None:
        _fix_height(new_node.right_child)

    _fix_height(new_node)
    return new_node


def _balance(node: TreeNode[K, V]) -> TreeNode[K, V]:
    _fix_height(node)

    if _balance_factor(node) == 2:
        if _balance_factor(node.left_child) < 0:
            node.left_child = _left_small_rotate(node.left_child)

        return _right_small_rotate(node)

    elif _balance_factor(node) == -2:
        if _balance_factor(node.right_child) > 0:
            node.right_child = _right_small_rotate(node.right_child)

        return _left_small_rotate(node)

    return node


def create_tree_map() -> TreeMap[K, V]:
    return TreeMap(None, 0)


def postorder_comparator(node: TreeNode[K, V]) -> Iterable[TreeNode[K, V]]:
    return filter(None, (node.left_child, node.right_child, node))


def inorder_comparator(node: TreeNode[K, V]) -> Iterable[TreeNode[K, V]]:
    return filter(None, (node.left_child, node, node.right_child))


def get_items(tree: TreeMap[K, V], order: Callable) -> list[(K, V)]:
    def items_recursion(cur_map: TreeNode[K, V]) -> None:
        map_order = order(cur_map)
        for node in map_order:
            if node is cur_map:
                items.append((node.key, node.value))
            else:
                items_recursion(node)

    items = []
    if tree.root is not None:
        items_recursion(tree.root)

    return items


def delete_tree_map(tree: TreeMap[K, V]) -> None:
    for key, _ in get_items(tree, postorder_comparator):
        remove(tree, key)
    del tree


def get_node_in_tree(
    node: TreeNode[K, V], key: K, value: Optional[V] = None
) -> Optional[TreeNode[K, V]]:
    if node is None:
        if value is not None:
            return TreeNode(key, value, 1, None, None)
        return None

    elif key < node.key:
        if value is not None:
            node.left_child = get_node_in_tree(node.left_child, key, value=value)
            return _balance(node)
        return get_node_in_tree(node.left_child, key, value=value)

    elif key > node.key:
        if value is not None:
            node.right_child = get_node_in_tree(node.right_child, key, value=value)
            return _balance(node)
        return get_node_in_tree(node.right_child, key, value=value)

    if value is not None:
        node.value = value
        return _balance(node)
    return node


def put(tree: TreeMap[K, V], key: K, value: V) -> None:
    if not has_key(tree, key):
        tree.size += 1

    tree.root = get_node_in_tree(tree.root, key, value=value)


def remove_recursion(
    cur_node: TreeNode[K, V], cur_key: K
) -> (Optional[TreeNode[K, V]], V):
    if cur_key < cur_node.key:
        new_left_child, return_value = remove_recursion(cur_node.left_child, cur_key)
        cur_node.left_child = new_left_child
        return _balance(cur_node), return_value

    if cur_key > cur_node.key:
        new_right_child, return_value = remove_recursion(cur_node.right_child, cur_key)
        cur_node.right_child = new_right_child
        return _balance(cur_node), return_value

    if cur_node.left_child is None and cur_node.right_child is None:
        return None, cur_node.value

    if cur_node.left_child is None:
        return cur_node.right_child, cur_node.value

    if cur_node.right_child is None:
        return cur_node.left_child, cur_node.value

    key_min, value_min = get_min_in_node(cur_node.right_child)
    return_value = cur_node.value
    new_cur_node = TreeNode(
        key_min,
        value_min,
        1,
        cur_node.left_child,
        remove_recursion(cur_node.right_child, key_min)[0],
    )
    return _balance(new_cur_node), return_value


def remove(tree: TreeMap[K, V], key: K) -> V:
    if tree.root is None:
        raise ValueError("Tree is empty")

    elif not has_key(tree, key):
        raise ValueError("Key not found")

    tree.root, value = remove_recursion(tree.root, key)
    tree.size -= 1
    return value


def get_min_in_node(node: TreeNode[K, V]) -> (K, V):
    if node is None:
        return ValueError("Root is None")

    while node.left_child is not None:
        node = node.left_child

    return node.key, node.value


def get(tree: TreeMap[K, V], key: K) -> V:
    node = get_node_in_tree(tree.root, key)

    if node is None:
        raise ValueError("Key not found")

    return node.value


def has_key(tree: TreeMap[K, V], key: K) -> bool:
    node = get_node_in_tree(tree.root, key)
    return node is not None


def _recursion_get_bound(
    cur_node: TreeNode[K, V], key: K, cur_min: K, cmp: operator
) -> K:
    if key < cur_node.key and cur_node.left_child is not None:
        return _recursion_get_bound(
            cur_node.left_child, key, min(cur_node.key, cur_min), cmp
        )

    elif key > cur_node.key and cur_node.right_child is not None:
        return _recursion_get_bound(cur_node.right_child, key, cur_min, cmp)

    if cmp(cur_node.key, key):
        return cur_node.key
    return cur_min


def get_lower_bound(tree: TreeMap[K, V], key: K) -> K:
    max_key = get_max(tree)

    if max_key < key:
        raise ValueError("There is no key larger than entered")
    if max_key == key:
        return key

    return _recursion_get_bound(tree.root, key, max_key, operator.ge)


def get_higher_bound(tree: TreeMap[K, V], key: K) -> K:
    max_key = get_max(tree)

    if max_key <= key:
        raise ValueError("There is no key strictly greater than entered")

    return _recursion_get_bound(tree.root, key, max_key, operator.gt)


def get_max(tree: TreeMap[K, V]) -> K:
    if tree.root is None:
        raise ValueError("Tree is empty")

    return get_max_in_node(tree.root)[0]


def get_min(tree: TreeMap[K, V]) -> K:
    if tree.root is None:
        raise ValueError("Tree is empty")

    return get_min_in_node(tree.root)[0]


def get_max_in_node(node: TreeNode[K, V]) -> (K, V):
    if node is None:
        return ValueError("Root is None")

    while node.right_child is not None:
        node = node.right_child

    return node.key, node.value


def remove_keys(tree_map: TreeMap, left: K, right: K) -> None:
    small_tree, _ = split(tree_map, left)
    _, big_tree = split(tree_map, right)
    tree_map.root = merge(small_tree, big_tree).root


def merge_node(
    tree_node_1: TreeNode[K, V], tree_node_2: TreeNode[K, V]
) -> TreeNode[K, V]:
    key_max_1, value_max_1 = get_max_in_node(tree_node_1)
    tree_node_1 = remove_recursion(tree_node_1, key_max_1)[0]

    def recursion(node: TreeNode[K, V]) -> TreeNode[K, V]:
        if tree_node_1 is None or node is None or node.height <= tree_node_1.height:
            if node is not None:
                return _balance(
                    TreeNode(key_max_1, value_max_1, node.height + 1, tree_node_1, node)
                )
            return _balance(
                TreeNode(
                    key_max_1, value_max_1, tree_node_1.height + 1, tree_node_1, node
                )
            )

        node.left_child = recursion(node.left_child)
        return _balance(node)

    return recursion(tree_node_2)


def merge_with_smaller(
    tree_map_1: TreeMap[K, V], tree_map_2: TreeMap[K, V]
) -> TreeMap[K, V]:
    tree_map_2.root = merge_node(tree_map_1.root, tree_map_2.root)
    tree_map_2.size += tree_map_1.size
    return tree_map_2


def merge_with_bigger(
    tree_map_1: TreeMap[K, V], tree_map_2: TreeMap[K, V]
) -> TreeMap[K, V]:
    tree_map_1.root = merge_node_with_bigger(tree_map_1.root, tree_map_2.root)
    tree_map_1.size += tree_map_2.size
    return tree_map_1


def merge_node_with_bigger(
    node_1: TreeNode[K, V], node_2: TreeNode[K, V]
) -> TreeNode[K, V]:
    if node_1.height > node_2.height:
        node_1.right_child = merge_node_with_bigger(node_1.right_child, node_2)
        return _balance(node_1)

    return merge_node(node_1, node_2)


def merge_trees(tree_map_1: TreeMap[K, V], tree_map_2: TreeMap[K, V]) -> TreeMap[K, V]:
    min_tree = min(tree_map_1, tree_map_2, key=lambda x: x.size)
    result_tree = max(tree_map_1, tree_map_2, key=lambda x: x.size)

    for key, value in get_items(min_tree, postorder_comparator):
        put(result_tree, key, value)

    return result_tree


def merge(tree_map_1: TreeMap[K, V], tree_map_2: TreeMap[K, V]) -> TreeMap[K, V]:
    max_value_1 = get_max(tree_map_1)
    min_value_1 = get_min(tree_map_1)
    max_value_2 = get_max(tree_map_2)
    min_value_2 = get_min(tree_map_2)

    if max_value_1 < min_value_2 and tree_map_1.root.height <= tree_map_2.root.height:
        return merge_with_smaller(tree_map_1, tree_map_2)

    if max_value_2 < min_value_1 and tree_map_1.root.height >= tree_map_2.root.height:
        return merge_with_smaller(tree_map_2, tree_map_1)

    if max_value_1 < min_value_2 and tree_map_1.root.height > tree_map_2.root.height:
        return merge_with_bigger(tree_map_1, tree_map_2)

    if max_value_2 < min_value_1 and tree_map_1.root.height < tree_map_2.root.height:
        return merge_with_bigger(tree_map_2, tree_map_1)

    return merge_trees(tree_map_1, tree_map_2)


def split(tree_map: TreeMap, key: K) -> tuple[TreeMap, TreeMap]:
    smaller_tree = create_tree_map()
    bigger_tree = create_tree_map()

    def recursion(
        node: TreeNode[K, V],
        small_tree: TreeMap[K, V],
        big_tree: TreeMap[K, V],
    ) -> (TreeMap, TreeMap):
        if node:
            if node.key < key:
                new_node = get_node_in_tree(node.left_child, node.key, value=node.value)
                if small_tree.root:
                    small_tree = merge(small_tree, TreeMap(new_node, 0))
                else:
                    small_tree = TreeMap(new_node, 0)

                return recursion(node.right_child, small_tree, big_tree)

            elif node.key >= key:
                new_node = get_node_in_tree(
                    node.right_child, node.key, value=node.value
                )
                if big_tree.root:
                    big_tree = merge(big_tree, TreeMap(new_node, 0))
                else:
                    big_tree = TreeMap(new_node, 0)

                return recursion(node.left_child, small_tree, big_tree)
        return small_tree, big_tree

    smaller_tree, bigger_tree = recursion(tree_map.root, smaller_tree, bigger_tree)
    # я не придумала ничего адекватного (((
    smaller_tree.size = len(get_items(smaller_tree, postorder_comparator))
    bigger_tree.size = len(get_items(bigger_tree, postorder_comparator))

    return smaller_tree, bigger_tree


def get_all(tree_map: TreeMap, left: K, right: K) -> list[K]:
    work_tree = deepcopy(tree_map)
    small_tree, _ = split(work_tree, right)
    _, result_tree = split(small_tree, left)
    items = get_items(result_tree, postorder_comparator)
    return [item[0] for item in items]
