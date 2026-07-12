from sum_list import sum_list


def test_sum_positive_numbers():
    assert sum_list([1, 2, 3, 4]) == 10


def test_sum_with_negative_numbers():
    assert sum_list([-5, 10, -2]) == 3


def test_sum_empty_list():
    assert sum_list([]) == 0
