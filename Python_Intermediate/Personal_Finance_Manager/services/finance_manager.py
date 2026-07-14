from datetime import datetime

from models.category import Category
from models.movement import Movement


class FinanceManager:
    VALID_CATEGORY_TYPES = {"income", "expense"}

    def __init__(self, save_callback):
        self.categories: list[Category] = []
        self.movements: list[Movement] = []
        self.save_callback = save_callback

    def set_data(self, categories: list[Category], movements: list[Movement]):
        self.categories = categories
        self.movements = movements

    def add_category(self, name: str, category_type: str, color: str):
        clean_name = self._remove_spaces_text(name)
        clean_type = self._remove_spaces_text(category_type).lower()
        clean_color = self._remove_spaces_text(color)

        if not clean_name:
            raise ValueError("Category name is required.")

        if clean_type not in self.VALID_CATEGORY_TYPES:
            raise ValueError("Category type must be income or expense.")

        if not clean_color:
            raise ValueError("Category color is required.")

        if self._category_exists(clean_name):
            raise ValueError("Category already exists.")

        category = Category(clean_name, clean_type, clean_color)
        self.categories.append(category)
        self._auto_save()
        return category

    def add_income(self, title: str, amount: str, category_name: str, date_text: str):
        return self._add_movement(title, amount, category_name, date_text, "income")

    def add_expense(self, title: str, amount: str, category_name: str, date_text: str):
        return self._add_movement(title, amount, category_name, date_text, "expense")

    def get_balance(self):
        balance = 0.0

        for movement in self.movements:
            if movement.movement_type == "income":
                balance += movement.amount
            else:
                balance -= movement.amount

        return balance

    def get_all_movements(self):
        return list(self.movements)

    def get_filtered_movements(self, start_date_text: str = "", end_date_text: str = ""):
        start_date = self._parse_optional_date(start_date_text)
        end_date = self._parse_optional_date(end_date_text)

        if start_date and end_date and start_date > end_date:
            raise ValueError("Start date cannot be after end date.")

        filtered_movements = []

        for movement in self.movements:
            movement_date = datetime.strptime(movement.date, "%d/%m/%Y").date()

            if start_date and movement_date < start_date:
                continue

            if end_date and movement_date > end_date:
                continue

            filtered_movements.append(movement)

        return filtered_movements

    def get_category_names(self, movement_type: str | None = None):
        clean_type = self._remove_spaces_text(movement_type).lower()

        if clean_type and clean_type not in self.VALID_CATEGORY_TYPES:
            raise ValueError("Movement type must be income or expense.")

        if not clean_type:
            return [category.name for category in self.categories]

        return [
            category.name
            for category in self.categories
            if category.category_type in ("", clean_type)
        ]

    def get_category_color(self, category_name: str):
        category = self._get_category(category_name)
        return category.color if category is not None else ""

    def _add_movement(self, title: str, amount: str, category_name: str, date_text: str, movement_type: str):
        clean_title = self._remove_spaces_text(title)
        clean_category = self._remove_spaces_text(category_name)
        clean_date = self._remove_spaces_text(date_text)

        if not clean_title:
            raise ValueError("Title is required.")

        valid_amount = self._validate_amount(amount)
        self._validate_category(clean_category, movement_type)
        date_obj = self._validate_date(clean_date)
        date_str = date_obj.strftime("%d/%m/%Y")

        movement = Movement(
            title=clean_title,
            amount=valid_amount,
            category=clean_category,
            date=date_str,
            movement_type=movement_type,
        )
        self.movements.append(movement)
        self._auto_save()
        return movement

    def _validate_category(self, category_name: str, movement_type: str):
        if not category_name:
            raise ValueError("Category is required.")

        category = self._get_category(category_name)

        if category is None:
            raise ValueError("Category must exist before using it.")

        if category.category_type not in ("", movement_type):
            raise ValueError(f"Category must belong to {movement_type}.")
    
    @staticmethod
    def _validate_amount(amount: str):
        try:
            value = float(str(amount).strip())
        except ValueError as exc:
            raise ValueError("Amount must be numeric.") from exc

        if value <= 0:
            raise ValueError("Amount must be greater than zero.")

        return value

    @staticmethod
    def _validate_date(date_text: str):
        try:
            if date_text == "":
                movement_date = datetime.today().date()
            else:
                movement_date = datetime.strptime(date_text, "%d/%m/%Y").date()

        except ValueError as exc:
            raise ValueError("Date must be in dd/mm/yyyy format.") from exc

        if movement_date > datetime.today().date():
            raise ValueError("Date cannot be in the future.")

        return movement_date

    @staticmethod
    def _remove_spaces_text(value: str):
        if value is None:
            return ""

        return value.strip()

    def _parse_optional_date(self, date_text: str):
        clean_date = self._remove_spaces_text(date_text)

        if clean_date == "":
            return None

        return self._validate_date(clean_date)

    def _category_exists(self, category_name: str):
        return self._get_category(category_name) is not None

    def _get_category(self, category_name: str):
        category_name_lower = category_name.lower()

        for category in self.categories:
            if category.name.lower() == category_name_lower:
                return category

        return None

    def _auto_save(self):
        if self.save_callback is not None:
            self.save_callback(self.categories, self.movements)
