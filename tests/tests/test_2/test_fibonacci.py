from io import StringIO

import pytest
from src.tests.test_2.task_1 import *


@pytest.mark.parametrize(
    "number,result",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (10, 55),
        (11, 89),
        (13, 233),
        (18, 2584),
        (90, 2880067194370816120),
    ],
)
def test_get_fibonacci(number, result):
    assert get_fibonacci(number) == result


@pytest.mark.parametrize(
    "mok_input,mok_output",
    [
        ("f", ERROR_NOT_NUMBER),
        ("cdfvgbhnjm", ERROR_NOT_NUMBER),
        ("-1", INVALID_NUMBER),
        ("100", INVALID_NUMBER),
        ("0", "The 0 fibonacci number: 0"),
        ("10", "The 10 fibonacci number: 55"),
        ("11", "The 11 fibonacci number: 89"),
        ("17", "The 17 fibonacci number: 1597"),
        ("15", "The 15 fibonacci number: 610"),
    ],
)
def test_main(monkeypatch, mok_input, mok_output):
    monkeypatch.setattr("builtins.input", lambda _: mok_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == mok_output + "\n"
