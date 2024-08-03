from constants import MENU_OPTIONS


def display_menu() -> None:
    """Отображает список команд библиотеки."""
    print("\nСписок команд библиотеки:")
    for key, value in MENU_OPTIONS.items():
        print(f"{key}. {value}")
    print("\n")
