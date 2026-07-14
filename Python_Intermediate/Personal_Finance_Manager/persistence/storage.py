import csv
import json
import os

from models.category import Category
from models.movement import Movement


def load_data(file_path: str) -> tuple[list[Category], list[Movement]]:
    if not os.path.exists(file_path):
        return [], []

    with open(file_path, "r", encoding="utf-8") as file:
        raw_data = json.load(file)

    categories = []
    movements = []

    for item in raw_data.get("categories", []):
        categories.append(Category.from_dict(item))

    for item in raw_data.get("movements", []):
        movements.append(Movement.from_dict(item))

    movement_types_by_category: dict[str, set[str]] = {}

    for movement in movements:
        movement_types_by_category.setdefault(movement.category.lower(), set()).add(
            movement.movement_type
        )

    for category in categories:
        if category.category_type:
            continue

        matched_types = movement_types_by_category.get(category.name.lower(), set())
        if len(matched_types) == 1:
            category.category_type = next(iter(matched_types))

    return categories, movements


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
