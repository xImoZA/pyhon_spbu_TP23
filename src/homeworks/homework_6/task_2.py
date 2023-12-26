import os

from src.homeworks.homework_6.AVL import *


def create(
    tree_map: TreeMap[K, V], street: str, house: int, building: int, index: int
) -> None:
    if has_key(tree_map, street):
        houses = get_node_in_tree(tree_map.root, street).value
        if has_key(houses, house):
            buildings = get_node_in_tree(houses.root, house).value
            buildings.append((building, index))
            buildings.sort()
        else:
            put(houses, house, [(building, index)])
    else:
        house_tree = create_tree_map()
        buildings = [(building, index)]
        put(house_tree, house, buildings)

        put(tree_map, street, house_tree)


def get_index(
    tree_map: TreeMap[K, V], street: str, house: int, building: int
) -> Optional[int]:
    try:
        houses = get_node_in_tree(tree_map.root, street).value
        buildings = get(houses, house)

    except:
        return None

    for block in buildings:
        if block[0] == building:
            return block[1]


def rename(tree_map: TreeMap[K, V], street: str, new_name: str) -> None:
    try:
        houses = get(tree_map, street)
        remove(tree_map, street)
        put(tree_map, new_name, houses)

    except:
        return None


def delete_block(
    tree_map: TreeMap[K, V], street: str, house: int, building: int
) -> None:
    try:
        houses = get_node_in_tree(tree_map.root, street).value
        buildings = get_node_in_tree(houses.root, house).value
    except:
        return None

    for i in range(len(buildings)):
        if buildings[i][0] == building:
            del buildings[i]
            break

    if not buildings:
        remove(houses, int(house))
    if houses.root is None:
        remove(tree_map, street)


def delete_house(tree_map: TreeMap[K, V], street: str, house: int) -> None:
    try:
        houses = get_node_in_tree(tree_map.root, street).value
        remove(houses, int(house))

    except:
        return None

    if houses.root is None:
        remove(tree_map, street)


def delete_street(tree_map: TreeMap[K, V], street: str) -> None:
    try:
        remove(tree_map, street)
    except:
        return None


def get_items_in_node(node: TreeNode[K, V], order: Callable) -> list[(K, V)]:
    def items_recursion(cur_map: TreeNode[K, V]) -> None:
        map_order = order(cur_map)
        for node in map_order:
            if node is cur_map:
                items.append((node.key, node.value))
            else:
                items_recursion(node)

    items = []
    if node is not None:
        items_recursion(node)

    return items


def print_list(
    tree_map: TreeMap[K, V],
    street_1: str,
    house_1: int,
    building_1: int,
    street_2: str,
    house_2: int,
    building_2: int,
):
    streets = []

    def recursion(tree_node: TreeNode):
        left_child = tree_node.left_child
        right_child = tree_node.right_child

        if street_1 <= tree_node.key <= street_2:
            street_0 = tree_node.key
            houses = get_items_in_node(tree_node.value.root, postorder_comparator)

            for house in houses:
                for corpus in house[1]:
                    address = [street_0, house[0], corpus[0]]
                    sort_list = [
                        [street_1, house_1, building_1],
                        address,
                        [street_2, house_2, building_2],
                    ]
                    sort_list.sort()
                    if (
                        sort_list.index(address) == 0
                        and address == sort_list[1]
                        and address != sort_list[2]
                    ) or (sort_list.index(address) == 1 and address != sort_list[-1]):
                        streets.append(address)

            if left_child is not None:
                recursion(left_child)

            if right_child is not None:
                recursion(right_child)
        elif tree_node.key > street_2 and left_child is not None:
            recursion(left_child)
        elif tree_node.key < street_1 and right_child is not None:
            recursion(right_child)

    recursion(tree_map.root)
    streets.sort()

    result = [" ".join(map(str, address)) + "\n" for address in streets]

    return result + ["\n"]


def commands(tree_map: TreeMap[K, V], instruction: list) -> Optional[list[str]]:
    command = instruction[0]
    try:
        if command == "CREATE":
            street = instruction[1]
            house, building, index = list(map(int, instruction[2:]))
            create(tree_map, street, house, building, index)

        elif command == "RENAME":
            old_name, new_name = instruction[1:]
            rename(tree_map, old_name, new_name)

        elif command == "LIST":
            street_1 = instruction[1]
            house_1, building_1 = list(map(int, instruction[2:4]))
            street_2 = instruction[4]
            house_2, building_2 = list(map(int, instruction[5:7]))

            return print_list(
                tree_map, street_1, house_1, building_1, street_2, house_2, building_2
            )

        elif command == "DELETE_STREET":
            street = instruction[1]
            delete_street(tree_map, street)

        elif command == "DELETE_HOUSE":
            street = instruction[1]
            house = int(instruction[2])
            delete_house(tree_map, street, house)

        elif command == "DELETE_BLOCK":
            street = instruction[1]
            house, building = list(map(int, instruction[2:]))
            delete_block(tree_map, street, house, building)

        elif command == "GET":
            street = instruction[1]
            house, building = list(map(int, instruction[2:]))
            index = get_index(tree_map, street, house, building)
            return [str(index) + "\n"]

        else:
            return ["Incorrect command"]

    except:
        return ["Incorrect command"]


def interactive_mode() -> None:
    tree = create_tree_map()
    print("To exit program enter EXIT")
    instruction = input("Enter your command: ").split()
    while instruction != ["EXIT"]:
        result = commands(tree, instruction)
        if result:
            print("".join(result))

        instruction = input("Enter your command: ").split()


def static_mode(log_file: str, result_file: str) -> None:
    tree = create_tree_map()
    with open(result_file, "w") as output_file, open(log_file, "r") as input_file:
        input_file.readline()
        for line in input_file.readlines():
            command = line.split()
            out_line = commands(tree, command)
            if out_line:
                output_file.writelines(out_line)


def main():
    print("1) Read the file and create new file with result\n2) Interactive mode")
    user_choice = input("Enter your action: ")

    if user_choice == "1":
        log_file = input("Enter the name of the input file: ")
        if not os.path.exists(log_file):
            print(f"File {log_file} not exist")
            return
        result_file = input("Enter the name of the results file: ")
        if os.path.exists(result_file):
            print(f"File {result_file} already exist")
            return
        static_mode(log_file, result_file)

    elif user_choice == "2":
        interactive_mode()
    else:
        print("You chosen incorrect action, try again")


if __name__ == "__main__":
    main()
