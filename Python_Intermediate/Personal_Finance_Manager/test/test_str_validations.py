from services.finance_manager import FinanceManager

def test_str_without_spaces_on_sides():
    word = "Trash food"
    validate_str = FinanceManager._remove_spaces_text(word)
    assert validate_str == "Trash food"


def test_str_with_spaces_on_sides():
    word = "    Trash food  "
    validate_str = FinanceManager._remove_spaces_text(word)
    assert validate_str == "Trash food"