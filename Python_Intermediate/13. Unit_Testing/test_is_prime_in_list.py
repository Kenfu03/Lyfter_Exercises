from is_prime_in_list import is_prime, is_prime_in_list


def test_is_prime_with_prime_number():
    assert is_prime(13) is True


def test_is_prime_in_list_with_mixed_numbers():
    assert is_prime_in_list([1, 2, 3, 4, 5, 6]) == [2, 3, 5]


def test_is_prime_in_list_with_no_primes():
    assert is_prime_in_list([0, 1, 4, 6, 8, 9]) == []
