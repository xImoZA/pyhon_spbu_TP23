from io import StringIO
from src.practice.practice_7.practice_7_task_1 import *
import pytest


@pytest.mark.parametrize(
    "numbers,expected",
    [([1, 2, 3], True), (["w", 2, 3], False), (["#", "w", "4"], False)],
)
def test_is_float_numbers(numbers, expected):
    actual = is_float_numbers(numbers)
    assert actual == expected


@pytest.mark.parametrize(
    "user_input,expected",
    [
        (["1", "2", "3"], True),
        (["1", "2", "3", "4"], False),
        (["w", "m", "q"], False),
        (["w", "m", "q", "#"], False),
        (["1", "2", "w"], False),
        (["w", "2", "m", "3"], False),
    ],
)
def test_get_corrected_input(user_input, expected):
    actual = get_corrected_input(user_input)
    assert actual == expected


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (3, 0, 0, [0]),
        (-3, 0, 0, [0]),
        (2, 0, -18, (-3, 3)),
        (-2, 0, 18, (-3, 3)),
        (2, 0, 18, ValueError),
        (-2, 0, -18, ValueError),
        (3, 6, 0, (0, -2)),
        (3, -6, 0, (0, 2)),
        (-3, 6, 0, (0, 2)),
        (-3, -6, 0, (0, -2)),
        (1, 2, 3, ValueError),
        (2, -1, -15, (-2.5, 3)),
        (1, 4, 4, [-2]),
    ],
)
def test_solution_quadratic_equation(a, b, c, expected):
    if expected == ValueError:
        with pytest.raises(ValueError):
            solution_quadratic_equation(a, b, c)
    else:
        actual = solution_quadratic_equation(a, b, c)
        if len(actual) == 2:
            assert len(actual) == len(expected) and (
                (actual[0] == expected[0] and actual[1] == expected[1])
                or (actual[0] == expected[1] and actual[1] == expected[0])
            )
        else:
            assert len(actual) == len(expected) and actual == expected


@pytest.mark.parametrize("b,c,expected", [(2, 1, [-0.5]), (-2, 1, [0.5]), (2, -6, [3.0])])
def test_solving_linear_equation(b, c, expected):
    actual = solving_linear_equation(b, c)
    assert actual == expected


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (0, 0, 0, ["X can be anything"]),
        (0, 0, 5, ValueError),
        (0, 2, 1, [-0.5]),
        (2, 0, 18, ValueError),
        (2, -1, -15, (-2.5, 3)),
        (1, 4, 4, [-2]),
    ],
)
def test_solving_equation(a, b, c, expected):
    if expected == ValueError:
        with pytest.raises(ValueError):
            solution_equation(a, b, c)
    else:
        actual = solution_equation(a, b, c)
        if len(actual) == 2:
            assert len(actual) == len(expected) and (
                (actual[0] == expected[0] and actual[1] == expected[1])
                or (actual[0] == expected[1] and actual[1] == expected[0])
            )
        else:
            assert len(actual) == len(expected) and actual == expected


def test_main(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2 -1 -15")
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert (
        output == "Solution of the equation: -2.5 3.0\n"
        or output == "Solution of the equation: 3.0 -2.5\n"
    )
