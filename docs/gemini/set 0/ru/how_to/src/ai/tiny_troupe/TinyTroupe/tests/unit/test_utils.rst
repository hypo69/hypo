Как использовать функции из модуля utils
========================================================================================

Описание
-------------------------
Этот код содержит тесты для функций `name_or_empty`, `extract_json` и `repeat_on_error` из модуля `tinytroupe.utils`.  Функции проверяют различные сценарии использования и обработку исключений.  `extract_json` извлекает JSON из строки, `name_or_empty` возвращает имя объекта или пустую строку, если объект `None` или не имеет атрибута `name`, а `repeat_on_error` повторяет функцию до определенного числа попыток, если возникнет исключение из указанного списка.

Шаги выполнения
-------------------------
1. **`test_extract_json`:** Проверяет функцию `extract_json` на различных входных данных:
    - корректные JSON строки,
    - JSON массивы,
    - JSON строки с экранированными символами,
    - некорректные JSON строки,
    - строки без JSON.
    В каждом случае функция `extract_json` должна возвращать ожидаемый результат.

2. **`test_name_or_empty`:** Проверяет функцию `name_or_empty` на различных входных данных:
    - объект с атрибутом `name`,
    - `None`.
    В каждом случае функция `name_or_empty` должна возвращать ожидаемый результат.

3. **`test_repeat_on_error`:** Проверяет функцию `repeat_on_error`:
    - вызов функции с исключением, которое должно быть перехвачено (и функция вызывается заданное количество раз).
    - вызов функции без исключений.
    - вызов функции с исключением, не указанным в списке исключений.
    В случае перехвата ожидаемого исключения функция `repeat_on_error` повторяет вызов заданное количество раз. В случае другого исключения - вызов завершается без повторений.


Пример использования
-------------------------
.. code-block:: python

    from tinytroupe.utils import extract_json, name_or_empty, repeat_on_error
    import pytest
    from unittest.mock import MagicMock

    # Пример использования extract_json
    json_string = '{"name": "John Doe", "age": 30}'
    extracted_data = extract_json(json_string)
    print(extracted_data)  # Вывод: {'name': 'John Doe', 'age': 30}

    # Пример использования name_or_empty
    class Person:
        def __init__(self, name):
            self.name = name
    person = Person("Alice")
    name = name_or_empty(person)
    print(name)  # Вывод: Alice

    # Пример использования repeat_on_error (с подмоделированием ошибки)

    class MyException(Exception):
        pass

    @repeat_on_error(retries=3, exceptions=[MyException])
    def my_function():
        try:
            raise MyException
        except MyException as e:
            print("Перехвачено исключение")
            return 0 # Обработка исключения внутри функции
    result = my_function()
    print(result) # Вывод: 0

    # Пример использования repeat_on_error без ошибки
    @repeat_on_error(retries=3, exceptions=[MyException])
    def my_function_no_error():
        return 1
    result = my_function_no_error()
    print(result) # Вывод: 1