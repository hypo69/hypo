Как использовать функции из модуля tinytroupe.utils
==========================================================================================

Описание
-------------------------
Этот код содержит тесты для функций `name_or_empty`, `extract_json` и `repeat_on_error` из модуля `tinytroupe.utils`.  Функции `name_or_empty` возвращает имя сущности, а если сущность `None`, возвращает пустую строку. Функция `extract_json` извлекает JSON из строки и возвращает его, если JSON валиден. Если JSON не найден или невалиден, возвращает пустой словарь. Функция `repeat_on_error` повторно выполняет декорированную функцию, если произойдет исключение из списка указанных типов.

Шаги выполнения
-------------------------
1. **`extract_json(text)`:** Функция принимает строку `text` в качестве аргумента.
2. **Парсинг JSON:**  Функция пытается распарсить JSON из строки.
3. **Обработка успешного парсинга:** Если парсинг успешен, функция возвращает полученный JSON.
4. **Обработка невалидного JSON:** Если строка не содержит JSON или JSON невалиден, функция возвращает пустой словарь `{}`.
5. **`name_or_empty(entity)`:** Функция принимает сущность `entity`.
6. **Проверка на None:**  Если `entity` равна `None`, функция возвращает пустую строку.
7. **Возврат имени:** Если `entity` не `None`, функция возвращает свойство `name` этой сущности.
8. **`repeat_on_error(retries=retries, exceptions=exceptions)(decorated_function)`:** Функция принимает количество попыток `retries`, список исключений `exceptions`, и декорируемую функцию `decorated_function`.
9. **Вызов декорированной функции:** Функция пытается вызвать декорированную функцию.
10. **Обработка исключения:** Если происходит исключение из списка `exceptions`, функция повторяет вызов декорированной функции до исчерпания числа попыток.
11. **Обработка других исключений:** Если исключение не из списка `exceptions`, функция перебрасывает его.
12. **Возврат результата:** Если функция выполнилась без исключений, функция возвращает результат.


Пример использования
-------------------------
.. code-block:: python

    from tinytroupe.utils import extract_json, name_or_empty, repeat_on_error
    from unittest.mock import MagicMock
    import pytest


    # Пример использования extract_json
    text = 'Some text before {"key": "value"} some text after'
    json_data = extract_json(text)
    print(json_data)  # Выведет: {'key': 'value'}


    # Пример использования name_or_empty
    class MockEntity:
        def __init__(self, name):
            self.name = name

    entity = MockEntity("Test")
    name = name_or_empty(entity)
    print(name)  # Выведет: Test


    entity = None
    name = name_or_empty(entity)
    print(name)  # Выведет:


    # Пример использования repeat_on_error
    class DummyException(Exception):
        pass

    retries = 3
    dummy_function = MagicMock(side_effect=DummyException())

    @repeat_on_error(retries=retries, exceptions=[DummyException])
    def decorated_function():
        dummy_function()
    with pytest.raises(DummyException):
        decorated_function()
    print(dummy_function.call_count)  # Выведет 3