from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Callable, Iterable

V = TypeVar("V")
K = TypeVar("K")


@dataclass
class TreeNode(Generic[K, V]):
    key: K
    value: V
    left_child: Optional["TreeNode[K, V]"]
    right_child: Optional["TreeNode[K, V]"]


@dataclass
class Tree(Generic[K, V]):
    root: Optional[TreeNode[K, V]]
    size: int


def create_tree_map() -> Tree[K, V]:
    return Tree(None, 0)


def delete_tree_map(tree: Tree[K, V]) -> None:
    tree.root = None
    tree.size = 0


def put(tree: Tree[K, V], key: K, value: V) -> None:
    if not has_key(tree, key):
        tree.size += 1

    if tree.root is None:
        tree.root = TreeNode(key, value, None, None)

    else:

        def put_recursion(
            cur_node: TreeNode[K, V], cur_key: K, cur_value: V
        ) -> TreeNode[K, V]:
            if cur_node is None:
                return TreeNode(cur_key, cur_value, None, None)

            elif cur_key == cur_node.key:
                return TreeNode(
                    cur_key, cur_value, cur_node.left_child, cur_node.right_child
                )

            elif cur_key < cur_node.key:
                cur_node.left_child = put_recursion(
                    cur_node.left_child, cur_key, cur_value
                )

            elif cur_key > cur_node.key:
                cur_node.right_child = put_recursion(
                    cur_node.right_child, cur_key, cur_value
                )

            return cur_node

        tree.root = put_recursion(tree.root, key, value)


def remove(tree: Tree[K, V], key: K) -> V:
    if tree.root is None:
        raise ValueError("Tree is empty")

    elif not has_key(tree, key):
        raise ValueError("Key not found")

    def remove_recursion(cur_node: TreeNode[K, V], cur_key: K) -> (TreeNode[K, V], V):
        if cur_key < cur_node.key:
            new_left_child, return_value = remove_recursion(
                cur_node.left_child, cur_key
            )
            cur_node.left_child = new_left_child
            return cur_node, return_value

        elif cur_key > cur_node.key:
            new_right_child, return_value = remove_recursion(
                cur_node.right_child, cur_key
            )
            cur_node.right_child = new_right_child
            return cur_node, return_value

        if cur_node.left_child is None and cur_node.right_child is None:
            return None, cur_node.value

        elif cur_node.left_child is None:
            return cur_node.right_child, cur_node.value

        elif cur_node.right_child is None:
            return cur_node.left_child, cur_node.value

        else:
            key_min, value_min = get_min(cur_node.right_child)
            return_value = cur_node.value
            cur_map = TreeNode(
                key_min,
                value_min,
                cur_node.left_child,
                remove_recursion(cur_node.right_child, key_min)[0],
            )
            return cur_map, return_value

    tree.root, value = remove_recursion(tree.root, key)
    tree.size -= 1
    return value


def get_min(node: TreeNode[K, V]) -> (K, V):
    if node is None:
        raise ValueError("Root is None")
    if node.left_child is None:
        return node.key, node.value

    return get_min(node.left_child)


def get(tree: Tree[K, V], key: K) -> V:
    if not has_key(tree, key):
        raise ValueError("Key not found")

    def get_recursion(cur_node: TreeNode[K, V], cur_key: K) -> V:
        if cur_key < cur_node.key:
            return get_recursion(cur_node.left_child, cur_key)

        elif cur_key > cur_node.key:
            return get_recursion(cur_node.right_child, cur_key)

        elif cur_key == cur_node.key:
            return cur_node.value

    return get_recursion(tree.root, key)


def has_key(tree: Tree[K, V], key: K) -> bool:
    if tree is None:
        return False

    def has_kay_recursion(cur_node: TreeNode[K, V], cur_key: K) -> bool:
        if cur_node is None:
            return False

        elif cur_key == cur_node.key:
            return True

        elif cur_key < cur_node.key:
            return has_kay_recursion(cur_node.left_child, cur_key)

        elif cur_key > cur_node.key:
            return has_kay_recursion(cur_node.right_child, cur_key)

    return has_kay_recursion(tree.root, key)


def _preorder_comparator(node: TreeNode[K, V]) -> Optional[Iterable[TreeNode[K, V]]]:
    return filter(None, (node, node.left_child, node.right_child))


def _inorder_comparator(node: TreeNode[K, V]) -> Iterable[TreeNode[K, V]]:
    return filter(None, (node.left_child, node, node.right_child))


def _postorder_comparator(node: TreeNode[K, V]) -> Iterable[TreeNode[K, V]]:
    return filter(None, (node.left_child, node.right_child, node))


def traverse(tree: Tree[K, V], order: str) -> Optional[list[V]]:
    if tree.root is None:
        return None

    values = []

    def traverse_recursion(cur_map: TreeNode[K, V], other_func: Callable) -> None:
        map_order = other_func(cur_map)
        for node in map_order:
            if node is not cur_map:
                traverse_recursion(node, other_func)
            else:
                values.append(node.value)

    if order == "preorder":
        traverse_recursion(tree.root, _preorder_comparator)

    elif order == "inorder":
        traverse_recursion(tree.root, _inorder_comparator)

    elif order == "postorder":
        traverse_recursion(tree.root, _postorder_comparator)

    return values
