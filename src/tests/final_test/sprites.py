from random import randint

PIXEl = "▒"
EMPTY = "░"


def is_digit(string: str) -> int:
    if not string.isdigit() or int(string) < 2:
        raise ValueError("The wrong size was entered")

    return int(string)


def get_transposition_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [
        [matrix[score_str][score_column] for score_str in range(len(matrix))]
        for score_column in range(len(matrix[0]))
    ]


def create_reflection_matrix(matrix: list) -> list:
    reflection_matrix = []

    for i in range(len(matrix) - 1, -1, -1):
        reflection_matrix.append(matrix[i])

    return reflection_matrix


def create_vertical_or_horizontal_sprite(
    size: int, format_sprite: int
) -> list[list[int]]:
    sprite_matrix = [[randint(0, 1) for _ in range(size)] for _ in range(size // 2)]
    reflection_sprite_matrix = create_reflection_matrix(sprite_matrix)

    if size % 2 != 0:
        line = [randint(0, 1) for _ in range(size // 2)]
        sprite_matrix.append(line + [randint(0, 1)] + create_reflection_matrix(line))

    full_sprite_matrix = sprite_matrix + reflection_sprite_matrix

    if format_sprite == 0:
        return get_transposition_matrix(full_sprite_matrix)

    return full_sprite_matrix


def create_vertical_and_horizontal_sprite(size: int) -> list[list[int]]:
    quarter_sprite = [
        [randint(0, 1) for _ in range(size // 2)] for _ in range(size // 2)
    ]
    reflection_quarter_sprite = create_reflection_matrix(quarter_sprite)

    if size % 2 != 0:
        quarter_sprite.append([randint(0, 1) for _ in range(size // 2)])

    half_sprite = get_transposition_matrix(quarter_sprite + reflection_quarter_sprite)
    reflection_half_sprite = create_reflection_matrix(half_sprite)

    if size % 2 != 0:
        line = [randint(0, 1) for _ in range(size // 2)]
        half_sprite.append(line + [randint(0, 1)] + create_reflection_matrix(line))

    full_sprite_matrix = half_sprite + reflection_half_sprite

    return full_sprite_matrix


def create_sprite(size: int, format_sprite: int) -> list[list[int]]:
    if format_sprite == 0 or format_sprite == 1:
        return create_vertical_or_horizontal_sprite(size, format_sprite)

    return create_vertical_and_horizontal_sprite(size)


def print_sprite(matrix: list[list[int]]) -> None:
    for line in matrix:
        string = ""
        for pixel in line:
            if pixel == 1:
                string += PIXEl
            else:
                string += EMPTY
        print(string)


def main():
    size = input("Enter the sprite size: ")
    try:
        size = is_digit(size)
    except ValueError as e:
        print(e)
        return

    replay = "1"
    while replay == "1":
        format_sprite = randint(0, 2)
        sprite = create_sprite(size, format_sprite)
        print_sprite(sprite)
        replay = input("If you want to continue, enter 1: ")


if __name__ == "__main__":
    main()
