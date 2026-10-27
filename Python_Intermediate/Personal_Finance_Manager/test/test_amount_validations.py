import pytest
from services.finance_manager import FinanceManager

def test_good_amount():
    str_number = "10000"
    validate_amount = FinanceManager._validate_amount(str_number)
    assert validate_amount == 10000.0


def test_amount_minus_zero():
    str_number = "-50"
    with pytest.raises(ValueError):
        FinanceManager._validate_amount(str_number)


def test_amount_minus_zero():
    str_number = "five"
    with pytest.raises(ValueError):
        FinanceManager._validate_amount(str_number)