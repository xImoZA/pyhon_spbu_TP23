from io import StringIO

import pytest
from src.practice.practice_10.main_module import *


@pytest.mark.parametrize(
    "mok_input,mok_output",
    [
        (
            "5 + 3 * 8",
            "START\n"
            ".....T\n"
            "......TOKEN\n"
            "...........id(5)\n"
            "......PROD\n"
            "..........eps\n"
            ".....SUM\n"
            "........+\n"
            "........T\n"
            ".........TOKEN\n"
            "..............id(3)\n"
            ".........PROD\n"
            ".............*\n"
            ".............TOKEN\n"
            "..................id(8)\n"
            ".............PROD\n"
            ".................eps\n"
            "........SUM\n"
            "...........eps\n",
        ),
        (
            "5",
            "START\n"
            ".....T\n"
            "......TOKEN\n"
            "...........id(5)\n"
            "......PROD\n"
            "..........eps\n"
            ".....SUM\n"
            "........eps\n",
        ),
        (
            "( 5 + 3 ) * 8",
            "START\n"
            ".....T\n"
            "......TOKEN\n"
            "...........(\n"
            "...........START\n"
            "................T\n"
            ".................TOKEN\n"
            "......................id(5)\n"
            ".................PROD\n"
            ".....................eps\n"
            "................SUM\n"
            "...................+\n"
            "...................T\n"
            "....................TOKEN\n"
            ".........................id(3)\n"
            "....................PROD\n"
            "........................eps\n"
            "...................SUM\n"
            "......................eps\n"
            "...........)\n"
            "......PROD\n"
            "..........*\n"
            "..........TOKEN\n"
            "...............id(8)\n"
            "..........PROD\n"
            "..............eps\n"
            ".....SUM\n"
            "........eps\n",
        ),
    ],
)
def test_main(monkeypatch, mok_input, mok_output):
    monkeypatch.setattr("builtins.input", lambda _: mok_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == mok_output


@pytest.mark.parametrize(
    "mok_input",
    ["5 *", "(", ")", "5 + ( * )", "( )", "5+3*8"],
)
def test_errors_main(monkeypatch, mok_input):
    monkeypatch.setattr("builtins.input", lambda _: mok_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == "The string does not match the grammar\n"
