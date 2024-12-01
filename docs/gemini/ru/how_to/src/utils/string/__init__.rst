Как использовать модуль hypotez/src/utils/string
========================================================================================

Описание
-------------------------
Модуль `hypotez/src/utils/string` содержит инструменты для работы со строками, числами и логическими значениями. Он предоставляет классы для форматирования строк (`StringFormatter`), валидации полей продуктов (`ProductFieldsValidator`), а также функции для нормализации строк, целых чисел, чисел с плавающей точкой и логических значений.

Шаги выполнения
-------------------------
1. Импортируйте необходимые функции или классы из модуля.
2. Используйте функции для нормализации данных (например, `normalize_string`, `normalize_int`, `normalize_float`, `normalize_boolean`).  Эти функции преобразуют входные данные в определённый формат.
3. Используйте класс `StringFormatter` для форматирования строк. Этот класс позволяет контролировать формат строки.
4. Используйте класс `ProductFieldsValidator` для валидации полей данных продукта.  Это гарантирует, что данные соответствуют определённым требованиям.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.utils.string import normalize_string, normalize_int, StringFormatter, ProductFieldsValidator

    # Нормализация строки
    input_string = "  тест строка  "
    normalized_string = normalize_string(input_string)
    print(f"Нормализованная строка: {normalized_string}")

    # Нормализация целого числа
    input_int = "123"
    normalized_int = normalize_int(input_int)
    print(f"Нормализованное целое число: {normalized_int}")


    # Пример использования StringFormatter
    formatter = StringFormatter()
    formatted_string = formatter.format_string("Пример строки", uppercase=True)
    print(f"Отформатированная строка: {formatted_string}")

    # Пример использования ProductFieldsValidator (требуется пример данных продукта)
    # Предположим, что у нас есть структура данных продукта:
    product_data = {
        "name": "Продукт 1",
        "price": "10.99",
        "available": "True"
    }

    validator = ProductFieldsValidator()
    validation_results = validator.validate(product_data)
    print(f"Результаты валидации: {validation_results}")