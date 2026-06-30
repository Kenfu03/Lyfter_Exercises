import menu



if __name__ == "__main__":
    try:
        menu.options_menu()
    except Exception as ex:
        print(f"Something goes wrong: {ex}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
