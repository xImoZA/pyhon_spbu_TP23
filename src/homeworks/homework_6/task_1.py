import os

from src.homeworks.homework_6.AVL import *


def add(tree: TreeMap[int, int], size: int, count: int) -> None:
    if has_key(tree, size):
        put(tree, size, get(tree, size) + count)
    else:
        put(tree, size, count)


def get_count(tree: TreeMap[int, int], size: int) -> str:
    try:
        return str(get(tree, size)) + "\n"

    except ValueError:
        return "0\n"


def select(tree: TreeMap[int, int], size: int) -> str:
    try:
        out = get_lower_bound(tree, size)

        count_this_size = get(tree, out) - 1
        if count_this_size != 0:
            put(tree, out, count_this_size)
        else:
            remove(tree, out)

        return str(out) + "\n"

    except ValueError:
        return "SORRY\n"


def read_file(file: str) -> (TreeMap[int, int], list[str]):
    catalog = create_tree_map()

    with open(file, "r") as log:
        n = int(log.readline())
        result = []

        for _ in range(n):
            operation = log.readline().split()
            size = int(operation[1])

            if operation[0] == "ADD":
                count = int(operation[2])
                add(catalog, size, count)

            elif operation[0] == "GET":
                result.append(get_count(catalog, size))

            else:
                result.append(select(catalog, size))

    return catalog, result


def write_in_file(file: str, value_list: list[str]) -> None:
    with open(file, "w") as output_file:
        output_file.writelines(value_list)


def _inorder_comparator(node: TreeNode[int, int]) -> Iterable[TreeNode[int, int]]:
    return filter(None, (node.left_child, node, node.right_child))


def get_balance_list(tree: TreeMap[int, int]) -> list[str]:
    if tree.root is None:
        return []

    items = []

    def items_recursion(cur_map: TreeNode[int, int]) -> None:
        for node in _inorder_comparator(cur_map):
            if node is not cur_map:
                items_recursion(node)
            else:
                items.append(f"{node.key} {node.value}\n")

    items_recursion(tree.root)
    return items


def find_file(name: str, path: str):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def main():
    log_file = input("Enter the name of the input file: ")
    if not os.path.exists(log_file):
        print(f"File {log_file} not exist")

    result_file = input("Enter the name of the results file: ")
    if os.path.exists(result_file):
        print(f"File {result_file} already exist")

    balance_file = input("Enter the name of the file with the stock balance: ")
    if os.path.exists(balance_file):
        print(f"File {balance_file} already exist")

    balance, result_list = read_file(find_file(log_file, "/"))
    write_in_file(result_file, result_list)
    write_in_file(balance_file, get_balance_list(balance))


if __name__ == "__main__":
    main()
