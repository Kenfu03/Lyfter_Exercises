import FreeSimpleGUI as sg


from services.finance_manager import FinanceManager


class FinanceAppUI:
    CATEGORY_TYPE_OPTIONS = {
        "Expense": "expense",
        "Income": "income",
    }
    CATEGORY_COLOR_PRESETS = {
        "expense": [
            "#d9534f",
            "#f0ad4e",
            "#ffd166",
            "#c06c84",
            "#9b5de5",
            "#ff7f50",
        ],
        "income": [
            "#2e8b57",
            "#20b2aa",
            "#3a86ff",
            "#00b4d8",
            "#4cc9f0",
            "#90be6d",
        ],
    }

    def __init__(self, manager: FinanceManager, export_callback):
        self.manager = manager
        self.export_callback = export_callback
        self.filter_start_date = ""
        self.filter_end_date = ""
        sg.theme("LightBlue3")

    def run(self):
        window = self._create_main_window()
        self._refresh_main_window(window)

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, "Exit"):
                if self._save_before_exit():
                    break
                continue

            if event == "Add Category":
                self._open_add_category_window()
                self._refresh_main_window(window)

            if event == "Add Income":
                self._open_add_movement_window("income")
                self._refresh_main_window(window)

            if event == "Add Expense":
                self._open_add_movement_window("expense")
                self._refresh_main_window(window)

            if event == "Apply Filter":
                try:
                    self._apply_filters(values)
                except ValueError as error:
                    sg.popup_error(str(error))
                else:
                    self._refresh_main_window(window)

            if event == "Clear Filter":
                self._clear_filters(window)
                self._refresh_main_window(window)

            if event == "Export CSV":
                self._export_movements()

        window.close()

    def _save_before_exit(self):
        """Save on every exit path and keep the window open if saving fails."""
        try:
            self.manager.save_current_state()
        except Exception as error:
            sg.popup_error(
                "The data could not be saved. The application will remain open.\n\n"
                f"Details: {error}"
            )
            return False

        return True

    def _create_main_window(self):
        layout = [
            [sg.Text("Personal Finance Manager", font=("Helvetica", 16, "bold"))],
            [
                sg.Text("Current Balance:"),
                sg.Text("", key="BALANCE", font=("Helvetica", 12, "bold")),
                sg.Push(),
                sg.Text("From"),
                sg.Input(key="FILTER_START", size=(12, 1)),
                sg.Text("To"),
                sg.Input(key="FILTER_END", size=(12, 1)),
                sg.Button("Apply Filter", size=(10, 1)),
                sg.Button("Clear Filter", size=(10, 1)),
            ],
            [
                sg.Table(
                    values=[],
                    headings=["Date", "Type", "Title", "Category", "Amount"],
                    key="MOVEMENTS_TABLE",
                    auto_size_columns=False,
                    col_widths=[12, 10, 20, 18, 12],
                    justification="center",
                    num_rows=14,
                    expand_x=True,
                    expand_y=True,
                    alternating_row_color="#e8f4ff",
                )
            ],
            [
                sg.Button("Add Category", size=(12, 1)),
                sg.Button("Add Income", size=(12, 1)),
                sg.Button("Add Expense", size=(12, 1)),
                sg.Button("Export CSV", size=(12, 1)),
                sg.Button("Exit", size=(12, 1)),
            ],
        ]

        return sg.Window("Personal Finance Manager", layout, resizable=True, finalize=True)

    def _refresh_main_window(self, window):
        table_rows, row_colors = self._build_table_display(window)
        window["MOVEMENTS_TABLE"].update(values=table_rows, row_colors=row_colors)
        window["BALANCE"].update(f"₡{self.manager.get_balance():,g}")
        window["FILTER_START"].update(self.filter_start_date)
        window["FILTER_END"].update(self.filter_end_date)

    def _build_table_display(self, window):
        rows = []
        row_colors = []

        for index, movement in enumerate(
            self.manager.get_filtered_movements(
                self.filter_start_date,
                self.filter_end_date,
            )
        ):
            sign = "+" if movement.movement_type == "income" else "-"
            rows.append(
                [
                    movement.date,
                    movement.movement_type.title(),
                    movement.title,
                    movement.category,
                    f"{sign}₡{movement.amount:,g}",
                ]
            )

            category_color = self.manager.get_category_color(movement.category)
            if category_color:
                text_color = self._get_contrast_text_color(window, category_color)
                row_colors.append((index, text_color, category_color))

        return rows, row_colors

    def _apply_filters(self, values):
        start_date = values["FILTER_START"].strip()
        end_date = values["FILTER_END"].strip()
        self.manager.get_filtered_movements(start_date, end_date)
        self.filter_start_date = start_date
        self.filter_end_date = end_date

    def _clear_filters(self, window):
        self.filter_start_date = ""
        self.filter_end_date = ""
        window["FILTER_START"].update("")
        window["FILTER_END"].update("")

    def _open_add_category_window(self):
        default_type_label = "Expense"
        layout = [
            [sg.Text("Category Name"), sg.Input(key="NAME")],
            [
                sg.Text("Category Type"),
                sg.Combo(
                    values=list(self.CATEGORY_TYPE_OPTIONS.keys()),
                    default_value=default_type_label,
                    key="CATEGORY_TYPE",
                    readonly=True,
                    enable_events=True,
                    expand_x=True,
                ),
            ],
            [sg.Text("Preset Colors")],
            self._build_color_preset_row(default_type_label),
            [
                sg.Text("Selected Color"),
                sg.Input(key="COLOR", readonly=True, expand_x=True),
                sg.Text("      ", key="COLOR_PREVIEW", relief="sunken", background_color="#ffffff"),
                sg.ColorChooserButton("More Colors", target="COLOR"),
            ],
            [sg.Button("Save"), sg.Button("Cancel")],
        ]

        window = sg.Window("Add Category", layout, modal=True, finalize=True)
        selected_color = ""
        self._update_color_preset_buttons(window, default_type_label)

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, "Cancel"):
                break

            current_color = values["COLOR"].strip()
            if current_color != selected_color:
                selected_color = current_color
                self._update_color_preview(window, selected_color)

            if event == "CATEGORY_TYPE":
                self._update_color_preset_buttons(window, values["CATEGORY_TYPE"])
                selected_color = ""
                window["COLOR"].update("")
                self._update_color_preview(window, "")

            if isinstance(event, str) and event.startswith("PRESET_COLOR_"):
                color_value = window[event].metadata
                selected_color = color_value
                window["COLOR"].update(color_value)
                self._update_color_preview(window, color_value)

            if event == "Save":
                try:
                    self.manager.add_category(
                        values["NAME"],
                        self.CATEGORY_TYPE_OPTIONS[values["CATEGORY_TYPE"]],
                        values["COLOR"],
                    )
                except ValueError as error:
                    sg.popup_error(str(error))
                else:
                    sg.popup("Category added successfully.")
                    break

        window.close()

    def _open_add_movement_window(self, movement_type: str):
        category_names = self.manager.get_category_names(movement_type)
        title = "Add Income" if movement_type == "income" else "Add Expense"

        if not category_names:
            sg.popup_error(f"Create an {movement_type} category first.")
            return

        layout = [
            [sg.Text("Title"), sg.Input(key="TITLE")],
            [sg.Text("Amount"), sg.Input(key="AMOUNT")],
            [
                sg.Text("Category"),
                sg.Combo(
                    values=category_names,
                    key="CATEGORY",
                    readonly=True,
                    expand_x=True,
                ),
            ],
            [sg.Text("Date (dd/mm/yyyy)"), sg.Input(key="DATE")],
            [sg.Button("Save"), sg.Button("Cancel")],
        ]

        window = sg.Window(title, layout, modal=True)

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, "Cancel"):
                break

            if event == "Save":
                try:
                    if movement_type == "income":
                        self.manager.add_income(
                            values["TITLE"],
                            values["AMOUNT"],
                            values["CATEGORY"],
                            values["DATE"],
                        )
                    else:
                        self.manager.add_expense(
                            values["TITLE"],
                            values["AMOUNT"],
                            values["CATEGORY"],
                            values["DATE"],
                        )
                except ValueError as error:
                    sg.popup_error(str(error))
                else:
                    sg.popup(f"{movement_type.title()} added successfully.")
                    break

        window.close()

    def _export_movements(self):
        file_path = sg.popup_get_file(
            "Choose where to save the CSV file",
            save_as=True,
            default_extension=".csv",
            file_types=(("CSV Files", "*.csv"),),
            no_window=True,
        )

        if not file_path:
            return

        movements = self.manager.get_filtered_movements(
            self.filter_start_date,
            self.filter_end_date,
        )
        self.export_callback(file_path, movements)
        sg.popup("CSV exported successfully.")

    def _build_color_preset_row(self, type_label: str):
        color_buttons = []

        for index, color in enumerate(self._get_preset_colors(type_label)):
            color_buttons.append(
                sg.Button(
                    "",
                    key=f"PRESET_COLOR_{index}",
                    size=(3, 1),
                    button_color=("black", color),
                    metadata=color,
                )
            )

        return color_buttons

    def _get_preset_colors(self, type_label: str):
        category_type = self.CATEGORY_TYPE_OPTIONS.get(type_label, "expense")
        return self.CATEGORY_COLOR_PRESETS[category_type]

    def _update_color_preset_buttons(self, window, type_label: str):
        for index, color in enumerate(self._get_preset_colors(type_label)):
            window[f"PRESET_COLOR_{index}"].update(button_color=("black", color))
            window[f"PRESET_COLOR_{index}"].metadata = color

    def _update_color_preview(self, window, color: str):
        preview_color = color or "#ffffff"
        text_color = self._get_contrast_text_color(window, preview_color)
        window["COLOR_PREVIEW"].update(background_color=preview_color, text_color=text_color)

    def _get_contrast_text_color(self, window, color: str):
        try:
            red, green, blue = window.TKroot.winfo_rgb(color)
        except Exception:
            return "#000000"

        brightness = ((red / 256) * 0.299) + ((green / 256) * 0.587) + ((blue / 256) * 0.114)
        return "#000000" if brightness > 186 else "#ffffff"
