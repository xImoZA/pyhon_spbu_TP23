from io import StringIO
from src.practice.practice_7.practice_7_task_1 import *
from collections import Counter
import pytest


@pytest.mark.parametrize(
    "numbers,expected",
    [
        ("1", True),
        ("-1", True),
        ("-1.5", True),
        ("w", False),
        ("-w", False),
        ("-w.e", False),
        ("w.2", False),
        ("-w.2", False),
    ],
)
def test_is_float_numbers(numbers, expected):
    actual = is_float_number(numbers)
    assert actual == expected


@pytest.mark.parametrize(
    "user_input,expected",
    [
        (["1", "2", "3"], [1.0, 2.0, 3.0]),
        (["-1", "-2", "-3"], [-1.0, -2.0, -3.0]),
        (["1.1", "2.2", "3.3"], [1.1, 2.2, 3.3]),
        (["-1.1", "-2.2", "-3.3"], [-1.1, -2.2, -3.3]),
        (["-1", "2.2", "-3.3"], [-1.0, 2.2, -3.3]),
    ],
)
def test_parse_input(user_input, expected):
    actual = parse_input(user_input)
    assert actual == expected


@pytest.mark.parametrize(
    "user_input",
    [
        (["1", "2", "3", "4"]),
        (["w", "m", "q"]),
        (["w", "m", "q", "#"]),
        (["1", "2", "w"]),
        (["w", "2", "m", "3"]),
    ],
)
def test_errors_parse_input(user_input):
    with pytest.raises(ValueError):
        parse_input(user_input)


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (3, 0, 0, (0,)),
        (-3, 0, 0, (0,)),
        (2, 0, -18, (-3, 3)),
        (-2, 0, 18, (-3, 3)),
        (3, 6, 0, (0, -2)),
        (3, -6, 0, (0, 2)),
        (-3, 6, 0, (0, 2)),
        (-3, -6, 0, (0, -2)),
        (2, -1, -15, (-2.5, 3)),
        (1, 4, 4, (-2,)),
    ],
)
def test_solution_quadratic_equation(a, b, c, expected):
    actual = solution_quadratic_equation(a, b, c)
    if len(actual) == 2:
        assert len(actual) == len(expected) and (Counter(expected) == Counter(actual))
    else:
        assert len(actual) == len(expected) and actual == expected


@pytest.mark.parametrize(
    "a,b,c",
    [
        (2, 0, 18),
        (-2, 0, -18),
        (1, 2, 3),
    ],
)
def test_value_errors_solution_quadratic_equation(a, b, c):
    with pytest.raises(ArithmeticError):
        solution_quadratic_equation(a, b, c)


@pytest.mark.parametrize(
    "b,c,expected", [(2, 1, (-0.5,)), (-2, 1, (0.5,)), (2, -6, (3.0,))]
)
def test_solving_linear_equation(b, c, expected):
    actual = solving_linear_equation(b, c)
    assert actual == expected


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (0, 2, 1, (-0.5,)),
        (2, -1, -15, (-2.5, 3)),
        (1, 4, 4, (-2,)),
    ],
)
def test_solve_equation(a, b, c, expected):
    actual = solve_equation(a, b, c)
    if len(actual) == 2:
        assert len(actual) == len(expected) and (Counter(expected) == Counter(actual))
    else:
        assert len(actual) == len(expected) and actual == expected


@pytest.mark.parametrize(
    "a,b,c",
    [
        (0, 0, 0),
        (0, 0, 5),
        (0, 0, 18),
    ],
)
def test_value_error_solve_equation(a, b, c):
    with pytest.raises(ValueError):
        solve_equation(a, b, c)


@pytest.mark.parametrize(
    "a,b,c",
    [
        (2, 0, 18),
        (-2, 0, -18),
        (1, 2, 3),
    ],
)
def test_arithmetic_error_solve_equation(a, b, c):
    with pytest.raises(ArithmeticError):
        solve_equation(a, b, c)


@pytest.mark.parametrize(
    "numbers,expected",
    [((-0.0,), (0,)), ((-2.5,), (-2.5,)), ((2.0,), (2,)), ((-1.0, 2.5), (-1, 2.5))],
)
def test_get_beautiful_numbers(numbers, expected):
    actual = get_beautiful_numbers(numbers)
    assert actual == expected


@pytest.mark.parametrize(
    "mok_input,mok_output",
    [("2 -1 -15", "Solution of the equation: 3 -2.5\n"),
     ("0 2 1", "Solution of the equation: -0.5\n"),
     ("1 2 3 4", "Error: More than 3 arguments have been entered\n"),
     ("1 w 2", "Error: Invalid argument №2\n"),
     ("0 0 0", "X can be anything\n"),
     ("0 0 3", "Error: The equation has no solutions\n"),
     ("2 0 18", "Error: The discriminant is less than zero\n")],
)
def test_main(monkeypatch, mok_input, mok_output):
    monkeypatch.setattr("builtins.input", lambda _: mok_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == mok_output
