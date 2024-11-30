# <input code>

```python
import pytest
from unittest.mock import MagicMock

import sys
sys.path.append('../../tinytroupe/')
sys.path.append('../../')
sys.path.append('..')


from tinytroupe.utils import name_or_empty, extract_json, repeat_on_error
from testing_utils import *

def test_extract_json():
    # Test with a simple JSON string
    text = 'Some text before {"key": "value"} some text after'
    result = extract_json(text)
    assert result == {"key": "value"}

    # Test with a JSON array
    text = 'Some text before [{"key": "value"}, {"key2": "value2"}] some text after'
    result = extract_json(text)
    assert result == [{"key": "value"}, {"key2": "value2"}]

    # Test with escaped characters
    text = 'Some text before {"key": "\\\'value\\\'"} some text after'
    result = extract_json(text)
    assert result == {"key": "\'value\'"}

    # Test with invalid JSON
    text = 'Some text before {"key": "value",} some text after'
    result = extract_json(text)
    assert result == {}

    # Test with no JSON
    text = 'Some text with no JSON'
    result = extract_json(text)
    assert result == {}


def test_name_or_empty():
    class MockEntity:
        def __init__(self, name):
            self.name = name

    # Test with a named entity
    entity = MockEntity("Test")
    result = name_or_empty(entity)
    assert result == "Test"

    # Test with None
    result = name_or_empty(None)
    assert result == ""


def test_repeat_on_error():
    class DummyException(Exception):
        pass

    # Test with retries and an exception occurring
    retries = 3
    dummy_function = MagicMock(side_effect=DummyException())
    with pytest.raises(DummyException):
        @repeat_on_error(retries=retries, exceptions=[DummyException])
        def decorated_function():
            dummy_function()
        decorated_function()
    assert dummy_function.call_count == retries

    # Test without any exception occurring
    retries = 3
    dummy_function = MagicMock()  # no exception raised
    @repeat_on_error(retries=retries, exceptions=[DummyException])
    def decorated_function():
        dummy_function()
    decorated_function()
    assert dummy_function.call_count == 1

    # Test with an exception that is not specified in the exceptions list
    retries = 3
    dummy_function = MagicMock(side_effect=RuntimeError())
    with pytest.raises(RuntimeError):
        @repeat_on_error(retries=retries, exceptions=[DummyException])
        def decorated_function():
            dummy_function()
        decorated_function()
    assert dummy_function.call_count == 1


# TODO
#def test_json_serializer():
```

# <algorithm>

**Функция `extract_json`:**

1. Принимает строку `text`.
2. Ищет JSON-объект или массив внутри строки.
3. Если найден, парсит его в Python-объект с помощью `json.loads`.
4. Если не найден, возвращает пустой словарь `{}`.
5. Возвращает результат парсинга.

**Функция `name_or_empty`:**

1. Принимает объект `entity`.
2. Если объект `entity` не `None` и имеет атрибут `name`, возвращает значение этого атрибута.
3. В противном случае возвращает пустую строку.


**Функция `repeat_on_error`:**

1. Принимает функцию `decorated_function` и параметры `retries`, `exceptions`.
2. Декорирует функцию `decorated_function` так, что она будет вызываться повторно `retries` раз, если произойдет исключение из списка `exceptions`.
3. Если исключения не происходит, функция выполняется один раз и возвращает результат.
4. Отслеживает количество вызовов `dummy_function` с помощью `dummy_function.call_count`.

**Пример:**

```
Вход: extract_json('{"name": "John"}')
Вывод: {"name": "John"}

Вход: extract_json('{"name": "John", "age": 30}')
Вывод: {"name": "John", "age": 30}

Вход: name_or_empty(MockEntity("Test"))
Вывод: "Test"

Вход: name_or_empty(None)
Вывод: ""
```


# <mermaid>

```mermaid
graph TD
    subgraph TinyTroupe
        A[extract_json] --> B{JSON Parse};
        B -- Success --> C[Return parsed JSON];
        B -- Failure --> D[Return {}];
        subgraph Tests
        E[test_extract_json] --> A;
        E --> F[Assertions];
        subgraph Utils
        G[name_or_empty] --> H{Check for None};
        H -- Not None --> I[Return entity.name];
        H -- None --> J[Return ""];
        subgraph Tests
        K[test_name_or_empty] --> G;
        K --> F;

        L[repeat_on_error] --> M{Exception Occur?};
        M -- Yes --> N[Retry];
        M -- No --> O[Return result];
        subgraph Tests
        P[test_repeat_on_error] --> L;
        P --> Q[Assertions];

    end
    end
    end
    end
```

# <explanation>

**Импорты:**

* `pytest`: Фреймворк для написания тестов.
* `unittest.mock.MagicMock`: Для создания моков (заглушек) функций.
* `sys`: Модуль для работы со средой выполнения, необходим для изменения пути поиска модулей.
* `tinytroupe.utils`: Модуль с утилитами, `name_or_empty`, `extract_json`, `repeat_on_error`.
* `testing_utils`:  Не определен, но очевидно, содержит вспомогательные функции для тестирования.

**Классы:**

* `MockEntity`: Простой класс, используемый в тестах для имитации сущности с именем.

**Функции:**

* `extract_json(text)`: Извлекает JSON из строки.  Возвращает парсированный JSON, или пустой словарь, если JSON не найден или строка не валидная.
* `name_or_empty(entity)`: Возвращает имя объекта, если он есть, или пустую строку.  Используется для безопасного доступа к атрибуту `name`.
* `repeat_on_error(retries, exceptions, decorated_function)`: Декоратор, который повторяет вызов функции `decorated_function` заданное число раз, если произойдёт исключение из переданного списка. 

**Переменные:**

* `text`, `result`: Хранят данные, используемые в тестах.

**Возможные ошибки или улучшения:**

* Необходим `import json` для парсинга JSON. Код предполагает, что это уже импортировано в `tinytroupe.utils`.
* Отсутствие обработки ошибок при парсинге JSON (например, если строка не соответствует формату JSON). В `extract_json` можно добавить обработку `json.JSONDecodeError` для более надежного кода.
* Тестирование `extract_json` с различными типами валидных JSON-строк, а также с валидными JSON-строками, которые содержат различные символы экранирования.

**Цепочка взаимосвязей:**

Тесты в `test_utils.py` проверяют функции из `tinytroupe.utils`.  Функции в `tinytroupe.utils`  вероятно, используются в других частях проекта `tinytroupe` для работы с именами и JSON.  `testing_utils` содержит вспомогательные функции, упрощающие создание тестов.


```
tinytroupe.utils -> test_utils.py
                   -> Другие части tinytroupe