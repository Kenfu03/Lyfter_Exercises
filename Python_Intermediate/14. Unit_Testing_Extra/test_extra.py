

def test_with_positive_numbers():
    assert 10 + 2 == 12
    assert sum([2, 4, 6]) / 3 == 4.0
    assert int(3.8) == 3

def test_with_negative_numbers():
    assert -10 + -2 == -12
    assert sum([-2, -4, -6]) / 3 == -4.0
    assert int(-3.8) == -3

def test_with_zero():
    assert 0 + 0 == 0
    assert sum([0, 0, 0]) / 1 == 0.0
    assert int(0.0) == 0
