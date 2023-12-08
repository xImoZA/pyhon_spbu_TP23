from io import StringIO

from src.practice.practice_9.main_module import *
import pytest


@pytest.mark.parametrize(
    "string,result",
    {
        ("abb", True),
        ("aaaaaaaaaaaaaaabb", True),
        ("bbbbbbbbbbbbabb", True),
        ("abababbababbababb", True),
        ("abbabbabbabbabb", True),
        ("azsxdcfvgbhnj", False),
        ("abababbabababababaaaaa", False),
        ("ababbababaabba", False),
    },
)
def test_validate_string_first_dfa(string, result):
    assert validate_string(create_first_dfa(), string) == result


@pytest.mark.parametrize(
    "string,result",
    {
        ("1234567890", True),
        ("0123456789", True),
        ("123.1234567890", True),
        ("123E1234567890", True),
        ("123E+1234567890", True),
        ("123E-1234567890", True),
        ("123.123E1234567890", True),
        ("123.123E+1234567890", True),
        ("123.123E-1234567890", True),
        ("zasxdcfvgbhn", False),
        (".1234567890", False),
        ("+2345678", False),
        ("E2345678", False),
        ("123.E3456", False),
        ("123E.123456789", False),
        ("123.+1234", False),
        ("123E6+23456", False),
    },
)
def test_validate_string_second_dfa(string, result):
    assert validate_string(create_second_dfa(), string) == result


@pytest.mark.parametrize(
    "mok_input,mok_output",
    [
        ("abb", f"{IN_FIRST_DFA}\n"),
        ("azsxdcfvgbhnj", f"{NOT_IN_FSM}\n"),
        ("1234567890", f"{IN_SECOND_DFA}\n"),
        ("123E+1234567890", f"{IN_SECOND_DFA}\n"),
        ("123E.123456789", f"{NOT_IN_FSM}\n"),
    ],
)
def test_main(monkeypatch, mok_input, mok_output):
    monkeypatch.setattr("builtins.input", lambda _: mok_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == mok_output
