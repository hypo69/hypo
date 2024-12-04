Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот блок кода выполняет проверку ввода данных, проверяя, содержит ли строка `input_string` только цифры.

Шаги выполнения
-------------------------
1. Получение строки `input_string` из внешнего источника.
2. Проверка, состоит ли `input_string` только из цифр.  Если `input_string` содержит не только цифры, генерируется ошибка.
3. Если проверка успешна, возвращается `True`. В противном случае возвращается `False`.

Пример использования
-------------------------
.. code-block:: python

    import re

    def check_numeric_input(input_string):
        """
        Проверяет, содержит ли строка только цифры.

        Args:
            input_string: Строка для проверки.

        Returns:
            True, если строка содержит только цифры, иначе False.
        """
        if re.fullmatch(r'\d+', input_string):
            return True
        else:
            raise ValueError("Строка должна содержать только цифры.")

    input_data = "12345"
    try:
        is_numeric = check_numeric_input(input_data)
        if is_numeric:
            print("Ввод содержит только цифры.")
    except ValueError as e:
        print(f"Ошибка: {e}")

    input_data2 = "123abc"
    try:
        is_numeric = check_numeric_input(input_data2)
        if is_numeric:
           print("Ввод содержит только цифры.")
    except ValueError as e:
        print(f"Ошибка: {e}")