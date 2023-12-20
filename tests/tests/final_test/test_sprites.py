from io import StringIO

from src.tests.final_test.sprites import *
import pytest


@pytest.mark.parametrize(
    "string",
    ["2", "3", "1234567890"],
)
def test_is_digit(string):
    assert is_digit(string) == int(string)


@pytest.mark.parametrize(
    "string",
    ["1", "fvgbhnjmk", "a"],
)
def test_errors_is_digit(string):
    with pytest.raises(ValueError):
        is_digit(string)


@pytest.mark.parametrize(
    "matrix, output_matrix",
    [
        ([[1, 2], [1, 3]], [[1, 1], [2, 3]]),
        ([[3, 2, 1], [0, 1, 2]], [[3, 0], [2, 1], [1, 2]]),
        ([[1, -1, 5], [4, 2, 7], [6, -2, 3]], [[1, 4, 6], [-1, 2, -2], [5, 7, 3]]),
        ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
    ],
)
def test_transposition_matrix(matrix, output_matrix):
    assert get_transposition_matrix(matrix) == output_matrix


@pytest.mark.parametrize(
    "matrix, output_matrix",
    [
        ([1, 0], [0, 1]),
        ([1, 0, 1, 0, 0], [0, 0, 1, 0, 1]),
        ([[1, 0], [0, 1]], [[0, 1], [1, 0]]),
        ([[1, 0, 0, 1], [0, 1, 1, 0]], [[0, 1, 1, 0], [1, 0, 0, 1]]),
        ([[1, 0, 1], [0, 1, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 0], [1, 0, 1]]),
    ],
)
def test_create_reflection_matrix(matrix, output_matrix):
    assert create_reflection_matrix(matrix) == output_matrix


@pytest.mark.parametrize(
    "size,format_sprite",
    [(2, 0), (2, 1), (3, 0), (3, 1), (10, 0), (21, 1), (30, 1), (50, 1)],
)
def test_create_vertical_or_horizontal_sprite(size, format_sprite):
    sprite_matrix = create_vertical_or_horizontal_sprite(size, format_sprite)
    for i in range(size):
        assert len((sprite_matrix[i])) == size
    assert len(sprite_matrix) == size


@pytest.mark.parametrize(
    "size",
    [2, 3, 4, 5, 10, 11, 20, 21, 30, 31],
)
def test_create_vertical_and_horizontal_sprite(size):
    sprite_matrix = create_vertical_and_horizontal_sprite(size)
    for i in range(size):
        assert len((sprite_matrix[i])) == size
    assert len(sprite_matrix) == size


@pytest.mark.parametrize(
    "size,format_sprite",
    [(2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (10, 0), (21, 1), (30, 2)],
)
def test_create_sprite(size, format_sprite):
    sprite_matrix = create_sprite(size, format_sprite)
    for i in range(size):
        assert len((sprite_matrix[i])) == size
    assert len(sprite_matrix) == size


@pytest.mark.parametrize(
    "sprite,expected",
    [
        (
            [
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
            ],
            "░▒▒▒░\n" "░░▒░░\n" "▒▒▒▒▒\n" "▒░░░▒\n" "▒░░░▒\n",
        ),
        (
            [[0, 0, 0], [1, 0, 1], [1, 1, 1]],
            "░░░\n" "▒░▒\n" "▒▒▒\n",
        ),
        (
            [[0, 1, 1, 1], [0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 1, 1]],
            "░▒▒▒\n" "░░▒░\n" "░░▒░\n" "░▒▒▒\n",
        ),
    ],
)
def test_print_sprite(monkeypatch, sprite, expected):
    monkeypatch.setattr("builtins.input", lambda _: "")
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    print_sprite(sprite)
    output = fake_output.getvalue()
    assert output.split() == expected.split()


@pytest.mark.parametrize(
    "mok_input,mok_output",
    [
        ("1", "The wrong size was entered\n"),
        ("dcfvgbhnjk", "The wrong size was entered\n"),
    ],
)
def test_errors_main(monkeypatch, mok_input, mok_output):
    monkeypatch.setattr("builtins.input", lambda _: mok_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == mok_output
