from src.tests.test_2_2.safe_call import *
import pytest


@safe_call
def foo1(string: str) -> Optional[int]:
    try:
        return int(string)
    except ValueError:
        raise ValueError("Testing")


@pytest.mark.parametrize(
    "foo_input",
    ["1", "2", "1234567890", "987654321"],
)
def test_safe_call_without_exception(foo_input):
    with warnings.catch_warnings(record=True) as w:
        output = foo1(foo_input)

        assert output == int(foo_input)
        assert len(w) == 0


@pytest.mark.parametrize(
    "foo_input",
    [
        "You're Heisenberg. You're goddamn right.",
        "szsxdcfvgbhjnkml",
        "234567.345678",
        "-456789jk",
    ],
)
def test_safe_call_with_exception(foo_input):
    with warnings.catch_warnings(record=True) as w:
        foo1(foo_input)

        assert len(w) == 1
        assert issubclass(w[-1].category, Warning)
        assert (
            str(w[-1].message)
            == "\nFunction: foo1\nType of Exception: ValueError\nMessage: Testing\nIn line 10: raise ValueError("
            "'Testing')"
        )


@safe_call
def foo():
    def goo():
        print("a" + 1)

    goo()


def test_safe_call_with_nested_functions():
    with warnings.catch_warnings(record=True) as w:
        foo()

        assert len(w) == 1
        assert issubclass(w[-1].category, Warning)
        assert (
            str(w[-1].message)
            == '\nFunction: goo\nType of Exception: TypeError\nMessage: can only concatenate str (not "int") to '
            'str\nIn line 49: print("a" + 1)'
        )
