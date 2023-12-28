from io import StringIO
from src.homeworks.homework_5.task_1 import *
import pytest


@pytest.mark.parametrize(
    "symbol,expected",
    [
        ("H", "U+0048"),
        ("e", "U+0065"),
        (" ", "U+0020"),
        (",", "U+002C"),
        ("☎", "U+260E"),
        ("𐀂", "U+10002"),
    ],
)
def test_get_unicode(symbol, expected):
    actual = get_unicode(symbol)
    assert actual == expected


@pytest.mark.parametrize(
    "symbol,expected",
    [
        ("H", ["00000000", "01001000"]),
        ("e", ["00000000", "01100101"]),
        (" ", ["00000000", "00100000"]),
        (",", ["00000000", "00101100"]),
        ("☎", ["00100110", "00001110"]),
        ("𐀂", ["11011000", "00000000", "11011100", "00000010"]),
    ],
)
def test_get_utf16(symbol, expected):
    actual = get_utf16(symbol)
    assert actual == expected


@pytest.mark.parametrize(
    "mok_input,mok_output",
    [
        (
            "Вошь",
            "UTF-16 encoding:\nВ 	 U+0412 	 00000100 00010010\nо 	 U+043E 	 00000100 00111110\nш 	 "
            "U+0448 	 00000100 01001000\nь 	 U+044C 	 00000100 01001100\n",
        ),
        (
            "お尻",
            "UTF-16 encoding:\nお 	 U+304A 	 00110000 01001010\n尻 	 U+5C3B 	 01011100 00111011\n",
        ),
        ("𓆏", "UTF-16 encoding:\n𓆏 	 U+1318F 	 11011000 00001100 11011101 10001111\n"),
        ("⚢", "UTF-16 encoding:\n⚢ 	 U+26A2 	 00100110 10100010\n"),
        ("𐀂", "UTF-16 encoding:\n𐀂 	 U+10002 	 11011000 00000000 11011100 00000010\n"),
    ],
)
def test_main(monkeypatch, mok_input, mok_output):
    monkeypatch.setattr("builtins.input", lambda _: mok_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == mok_output
