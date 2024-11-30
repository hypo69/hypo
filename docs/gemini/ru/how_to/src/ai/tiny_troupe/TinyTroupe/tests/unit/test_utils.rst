Как использовать функции `extract_json`, `name_or_empty` и `repeat_on_error`
==========================================================================================

Описание
-------------------------
Этот код содержит тесты для функций `extract_json`, `name_or_empty` и `repeat_on_error` из модуля `tinytroupe.utils`. Функции проверяют работу с JSON-строками, обработку отсутствующих значений и повторное выполнение функции при возникновении исключения.


Шаги выполнения
-------------------------
1. **Функция `extract_json`**:
    - Принимает строку в качестве входных данных.
    - Анализирует строку, проверяя наличие корректного JSON-формата внутри.
    - Если JSON присутствует, то функция извлекает и возвращает его десериализованное представление (словарь или список).
    - Если JSON не обнаружен или некорректен, возвращает пустой словарь `{}`.
2. **Функция `name_or_empty`**:
    - Принимает объект в качестве входных данных.
    - Если объект не равен `None` и содержит атрибут `name`, то функция возвращает значение этого атрибута.
    - В противном случае возвращает пустую строку `""`.
3. **Функция `repeat_on_error`**:
    - Принимает количество попыток (`retries`) и список исключений (`exceptions`) в качестве аргументов.
    - Декорирует функцию, что оборачивает ее код в цикл.
    - В цикле выполняет декорируемую функцию.
    - Если во время выполнения функции возникает исключение, которое указано в списке `exceptions`, то цикл повторяется до тех пор, пока количество попыток не исчерпается.
    - Если исключение не указано в `exceptions`, то функция `repeat_on_error` не обрабатывает его и поднимает исключение дальше.
    - Если выполнение прошло успешно, то функция возвращает результат выполнения декорируемой функции.

Пример использования
-------------------------
.. code-block:: python

    import json
    from tinytroupe.utils import extract_json, name_or_empty, repeat_on_error
    from unittest.mock import MagicMock
    import pytest

    #Пример использования extract_json
    text = 'Some text before {"key": "value"} some text after'
    extracted_json = extract_json(text)
    print(json.dumps(extracted_json, indent=2))  # Output: {"key": "value"}

    # Пример использования name_or_empty
    class MockEntity:
        def __init__(self, name):
            self.name = name

    entity = MockEntity("Example")
    result = name_or_empty(entity)
    print(result)  # Output: Example

    result = name_or_empty(None)
    print(result)  # Output: 

    class DummyException(Exception):
        pass


    # Пример использования repeat_on_error

    retries = 3
    dummy_function = MagicMock(side_effect=DummyException())

    @repeat_on_error(retries=retries, exceptions=[DummyException])
    def decorated_function():
        dummy_function()
        return "Success"

    try:
        result = decorated_function()
    except DummyException:
        print("Function failed after multiple retries.")
    else:
        print(result)  # Output: Success