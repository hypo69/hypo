Как использовать модуль src.utils.string
========================================================================================

Описание
-------------------------
Этот модуль предоставляет инструменты для работы со строками, целыми числами, числами с плавающей точкой и булевыми значениями. Он включает в себя форматирование строк, валидацию полей продукта и нормализацию данных.

Шаги выполнения
-------------------------
1. Импортирует необходимые классы и функции из подмодулей `formatter`, `validator` и `normalizer`.
2. Определяет константу `MODE` со значением 'dev'.  Скорее всего, это переменная, определяющая режим работы (например, разработки или производства).
3. Обеспечивает доступ к функциональности форматирования строк через класс `StringFormatter`.
4. Обеспечивает доступ к валидации полей продукта через класс `ProductFieldsValidator`.
5. Предоставляет функции для нормализации строк (`normalize_string`), целых чисел (`normalize_int`), чисел с плавающей точкой (`normalize_float`) и булевых значений (`normalize_boolean`).


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.utils.string import StringFormatter, normalize_string, normalize_int
    
    # Форматирование строки
    formatter = StringFormatter()
    formatted_string = formatter.format_string("Hello, {name}!", name="World")
    print(formatted_string) # Выведет Hello, World!
    
    # Нормализация строки
    normalized_string = normalize_string("   Hello world   ")
    print(normalized_string) # Выведет Hello world

    # Нормализация целого числа (предполагается, что функция обрабатывает невалидные значения)
    normalized_int = normalize_int("123")
    print(normalized_int) # Выведет 123
    
    normalized_int_invalid = normalize_int("abc")
    print(normalized_int_invalid) # Результат зависит от реализации normalize_int