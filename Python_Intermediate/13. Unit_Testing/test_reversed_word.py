from reversed_word import reversed_word


def test_reverse_simple_word():
    assert reversed_word("hello") == "olleh"


def test_reverse_empty_string():
    assert reversed_word("") == ""


def test_reverse_with_spaces():
    assert reversed_word("reconocer") == "reconocer"
