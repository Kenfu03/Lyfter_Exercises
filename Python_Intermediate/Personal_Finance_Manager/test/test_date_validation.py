import pytest
from services.finance_manager import FinanceManager
from datetime import datetime


def test_valid_date():
    good_date = "28/11/2025"
    validate_date = FinanceManager._validate_date(good_date)
    assert validate_date == datetime.strptime(good_date, "%d/%m/%Y").date()


def test_invalid_date():
    wrong_date = "11/28/2025"
    with pytest.raises(ValueError):
        FinanceManager._validate_date(wrong_date)


def test_future_date():
    future_date = "1/12/2026"
    with pytest.raises(ValueError):
        FinanceManager._validate_date(future_date)


def test_empty_date():
    validate_date = FinanceManager._validate_date("")
    assert validate_date == datetime.today().date()