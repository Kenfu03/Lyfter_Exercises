from persistence.storage import export_csv, load_data, save_data
from services.finance_manager import FinanceManager
from ui.interface import FinanceAppUI


def main():
    data_file = "data.json"

    manager = FinanceManager(
        save_callback=lambda categories, movements: save_data(
            data_file, categories, movements
        )
    )

    categories, movements = load_data(data_file)
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
