import csv
import json
import os
import shutil
from datetime import datetime

from models.category import Category
from models.movement import Movement
from services.finance_manager import FinanceManager


class DataLoadError(Exception):
    """Raised when persisted finance data cannot be safely loaded."""


def _backup_invalid_file(file_path: str):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_path = f"{file_path}.invalid-{timestamp}.bak"

    try:
        shutil.copy2(file_path, backup_path)
    except OSError:
        return None

    return backup_path


def load_data(file_path: str):
    if not os.path.exists(file_path):
        return [], []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            raw_data = json.load(file)

        if not isinstance(raw_data, dict):
            raise ValueError("The root JSON value must be an object.")

        raw_categories = raw_data.get("categories", [])
        raw_movements = raw_data.get("movements", [])
        if not isinstance(raw_categories, list) or not isinstance(raw_movements, list):
            raise ValueError("Categories and movements must be lists.")

        categories = [Category.from_dict(item) for item in raw_categories]
        movements = [Movement.from_dict(item) for item in raw_movements]
        FinanceManager.validate_loaded_data(categories, movements)
        return categories, movements
    except (OSError, json.JSONDecodeError, TypeError, ValueError, AttributeError) as error:
        backup_path = _backup_invalid_file(file_path)
        message = "Saved data is invalid and was not loaded."
        if backup_path:
            message += f" A backup was created at '{backup_path}'."
        else:
            message += " The original file was left unchanged."
        raise DataLoadError(message) from error


def save_data(file_path: str, categories: list[Category], movements: list[Movement]):

    data = {
        "categories": [category.to_dict() for category in categories],
        "movements": [movement.to_dict() for movement in movements],
    }

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def export_csv(file_path: str, movements: list[Movement]):
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Type", "Title", "Category", "Amount"])

        for movement in movements:
            writer.writerow(
                [
                    movement.date,
                    movement.movement_type,
                    movement.title,
                    movement.category,
                    f"{movement.amount}",
                ]
            )
