from sort_word_in_list import string_to_list, sort_words_in_list, list_to_string

def test_string_to_list():
    assert string_to_list("banana-apple-cherry") == ["banana", "apple", "cherry"]


def test_sort_words_in_list():
    assert sort_words_in_list(["banana", "Apple", "cherry"]) == ["Apple", "banana", "cherry"]


def test_list_to_string():
    assert list_to_string(["Apple", "banana", "cherry"]) == "Apple-banana-cherry"
