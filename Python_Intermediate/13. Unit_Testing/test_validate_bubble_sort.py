import pytest
from validate_bubble_sort import bubble_sort  # change this to your file name


# Small list
def test_small_list():
    arr = [5, 2, 9, 1]
    result = bubble_sort(arr)
    assert result == [1, 2, 5, 9]


# Large list (>100 elements)
def test_large_list():
    arr = list(range(200, 0, -1))  # 200 → 1
    result = bubble_sort(arr)
    assert result == list(range(1, 201))


# Empty list
def test_empty_list():
    with pytest.raises(ValueError):
        bubble_sort([])


# Non-list inputs
def test_invalid_input():
    with pytest.raises(TypeError):
        bubble_sort("not a list")