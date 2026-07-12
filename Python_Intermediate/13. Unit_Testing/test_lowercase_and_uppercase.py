from lowercase_and_uppercase import uppercase_in_text, lowercase_in_text

def test_count_mixed_text():
    word = "AbCdeF"
    assert uppercase_in_text(word) == 3
    assert lowercase_in_text(word) == 3


def test_count_all_uppercase():
    word = "XYZ"
    assert uppercase_in_text(word) == 3
    assert lowercase_in_text(word) == 0


def test_count_all_lowercase():
    word = "python"
    assert uppercase_in_text(word) == 0
    assert lowercase_in_text(word) == 6
