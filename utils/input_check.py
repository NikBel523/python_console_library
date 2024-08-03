def check_if_int(prompt: str) -> int:
    """Запрашивает у пользователя ввод числа, пока не получит корректное значение."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное целое число.")
