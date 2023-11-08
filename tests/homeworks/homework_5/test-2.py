from io import StringIO
from src.homeworks.homework_5.task_2 import *
import pytest


@pytest.mark.parametrize(
    "dna,expected",
    [
        ("aaaabbсaa", "a4b2с1a2"),
        ("abbcccddddeeeee", "a1b2c3d4e5"),
        ("abcdefg", "a1b1c1d1e1f1g1"),
    ],
)
def test_encode(dna, expected):
    actual = encode(dna)
    assert actual == expected


@pytest.mark.parametrize(
    "dna",
    ["asdfg sdfgh", "asdfg@@#$%", "1234567", "dfgh234567", "#$%^&34567fghj"],
)
def test_errors_encode(dna):
    with pytest.raises(ValueError):
        encode(dna)


@pytest.mark.parametrize(
    "dna,expected",
    [
        ("a4b2с1a2", "aaaabbсaa"),
        ("a1b2c3d4e5", "abbcccddddeeeee"),
        ("a1b1c1d1e1f1g1", "abcdefg"),
    ],
)
def test_decode(dna, expected):
    actual = decode(dna)
    assert actual == expected


@pytest.mark.parametrize(
    "dna",
    ["", "zsxdcfvgbh", "12345678", "dfg fghj", "#$%^&*", "a2s3d", "2s3d3", "a2dfghjk5"],
)
def test_errors_decode(dna):
    with pytest.raises(ValueError):
        decode(dna)


@pytest.mark.parametrize(
    "dna,expected",
    [("a4b2с1a2", True), ("a1b2c3d4e5", True), ("a1b1c1d1e1f1g1", True)],
)
def test_is_input_correct(dna, expected):
    actual = is_input_correct(dna)
    assert actual == expected


@pytest.mark.parametrize(
    "dna",
    ["", "zsxdcfvgbh", "12345678", "dfg fghj", "#$%^&*", "a2s3d", "2s3d3", "a2dfghjk5"],
)
def test_errors_is_input_correct(dna):
    with pytest.raises(ValueError):
        is_input_correct(dna)


@pytest.mark.parametrize(
    "mok_input,mok_output",
    [
        (["abcdefg", "1"], "Encode DNA: a1b1c1d1e1f1g1\n"),
        (["a1b1c1d1e1f1g1", "2"], "Decode DNA: abcdefg\n"),
        (["szxdcfvgbhnj", "ghjk"], "Incorrect input. It can only be 1 or 2\n"),
        (["", "1"], "You entered an empty string\n"),
        (["dfgh456", "1"], "DNA must contain only letters\n"),
        (["dfgh ghjk", "1"], "DNA must contain only letters\n"),
        (["dfgh@#$%^&", "1"], "DNA must contain only letters\n"),
        (["", "2"], "You entered an empty string\n"),
        (
            ["sexdcfvgbhnj", "2"],
            "Encode DNA should consist only of letters and numbers\n",
        ),
        (["345678", "2"], "Encode DNA should consist only of letters and numbers\n"),
        (
            ["dfgh34567$%^&*", "2"],
            "Encode DNA should consist only of letters and numbers\n",
        ),
        (["d3f4 g6h8", "2"], "Encode DNA should consist only of letters and numbers\n"),
        (["a3d4f", "2"], "Encode DNA can't end with a letter\n"),
        (["2a3d4f4", "2"], "Encode DNA can't start with a digit\n"),
        (["a3dh4f4", "2"], "Encode DNA can't have several letters successively\n"),
    ],
)
def test_main(monkeypatch, mok_input, mok_output):
    monkeypatch.setattr("builtins.input", lambda _: mok_input.pop(0))
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == mok_output
