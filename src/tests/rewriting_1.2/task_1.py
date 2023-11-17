from sys import argv
import os.path


def sort_lines(line1: list[int], line2: list[int]) -> list[int]:
    sorted_lines = line1[::]
    now_index = 0

    for number in line2:
        while now_index < len(sorted_lines) and number > sorted_lines[now_index]:
            now_index += 1

        sorted_lines.insert(now_index, number)
        now_index += 1

    return sorted_lines


def read_file(file: str) -> list[list[int]]:
    numbers = []

    with open(file, "r") as open_file:
        for line in open_file.readlines():
            numbers.append(list(map(int, line.split())))

    return numbers


def write_in_file(file: str, numbers: list[int]) -> None:
    with open(file, "w") as writing_file:
        writing_file.write(" ".join(map(str, numbers)))


if __name__ == "__main__":
    f, g = argv[1:]

    if not os.path.exists(f):
        print(f"File {f} not exist")

    elif os.path.exists(g):
        print(f"File {g} already exist")

    else:
        num = read_file(f)
        write_in_file(g, sort_lines(num[0], num[1]))
