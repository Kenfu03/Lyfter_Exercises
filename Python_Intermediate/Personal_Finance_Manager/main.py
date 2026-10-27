from pathlib import Path

import FreeSimpleGUI as sg

from persistence.storage import DataLoadError, export_csv, load_data, save_data
from services.finance_manager import FinanceManager
from ui.interface import FinanceAppUI


def main():
    data_file = Path(__file__).resolve().parent / "data.json"

    manager = FinanceManager(
        save_callback=lambda categories, movements: save_data(
            data_file, categories, movements
        )
    )

    try:
        categories, movements = load_data(data_file)
    except DataLoadError as error:
        sg.popup_error(f"The application will start with empty data.\n\n{error}")
        categories, movements = [], []
    manager.set_data(categories, movements)

    ui = FinanceAppUI(
        manager=manager,
        export_callback=lambda file_path, movements: export_csv(
            file_path, movements
        ),
    )
    ui.run()


if __name__ == "__main__":
    main()
