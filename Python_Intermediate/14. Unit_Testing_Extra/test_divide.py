import pytest
from divide import divide


def test_divide_with_numbers():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)


def test_divide_with_strings():
    with pytest.raises(TypeError):
        divide(5, "Hello")
