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

**Функция extract_json:**

1. Принимает строку `text`.
2. Использует регулярное выражение для поиска JSON внутри строки.
3. Если JSON найден, парсит его и возвращает.
4. Если JSON не найден, возвращает пустой словарь.

**Функция name_or_empty:**

1. Принимает объект `entity`.
2. Если `entity` не равен `None` и имеет атрибут `name`, возвращает значение `entity.name`.
3. Иначе возвращает пустую строку.

**Функция repeat_on_error:**

1. Принимает количество повторений `retries` и список исключений `exceptions`.
2. Используя декоратор, обворачивает функцию `decorated_function`.
3. При выполнении `decorated_function` ловит исключения из списка `exceptions`.
4. Если исключение возникает, повторяет выполнение `decorated_function` до `retries` раз.
5. Если исключения не возникают, выполняет `decorated_function` один раз.


# <mermaid>

```mermaid
graph TD
    subgraph "Модуль utils"
        A[extract_json(text)] --> B{Поиск JSON};
        B -- JSON найден --> C[Парсинг JSON];
        B -- JSON не найден --> D[Возврат {}];
        C --> E[Возврат JSON];
        D --> E;
        
        F[name_or_empty(entity)] --> G{entity == None?};
        G -- Да --> H[Возврат ""];
        G -- Нет --> I{entity.name существует?};
        I -- Да --> J[Возврат entity.name];
        I -- Нет --> H;
        
        K[repeat_on_error(retries, exceptions)] --> L{Проверка исключения};
        L -- Исключение в exceptions --> M[Повторить];
        L -- Исключение не в exceptions --> N[Выполнение функции];
        M --> K;
        N --> O[Возврат результата];

    end
    
    subgraph "Тесты"
        P[test_extract_json()] --> A;
        Q[test_name_or_empty()] --> F;
        R[test_repeat_on_error()] --> K;
        
    end
    
    
    E --> P;
    J --> Q;
    O --> R;
```

# <explanation>

**Импорты:**

- `pytest`: Фреймворк для тестирования.
- `unittest.mock.MagicMock`:  Для создания моков функций.
- `sys`:  Для добавления директорий в `sys.path` для импорта из других модулей.
- `tinytroupe.utils`: Модуль с полезными функциями, например, `name_or_empty`, `extract_json`, `repeat_on_error`.
- `testing_utils`: Модуль с вспомогательными функциями для тестов.  Судя по коду, вероятно создан внутри проекта TinyTroupe для использования в тестах.


**Классы:**

- `MockEntity`:  Простой класс, созданный для тестирования `name_or_empty`.  Используется в тесте для имитации объекта с именем.  В данном случае он не используется в каком-либо значимом функционале за пределами тестов.


**Функции:**

- `extract_json(text)`:  Извлекает JSON из строки `text`.  Обрабатывает различные случаи, включая корректный JSON, JSON-массивы, экранированные символы, невалидный JSON и отсутствие JSON в строке.  Возвращает JSON как результат или пустой словарь, если ничего не найдено или невалидный JSON.
- `name_or_empty(entity)`:  Возвращает имя объекта, если оно доступно, и пустую строку, если объект `None` или не содержит атрибут `name`.
- `repeat_on_error(retries, exceptions, decorated_function)`:  Декоратор, который повторяет вызов функции `decorated_function` заданное количество `retries` раз в случае возникновения исключения из списка `exceptions`.

**Переменные:**

Переменные `text`, `result`, `entity`, `retries`, `dummy_function`, `decorated_function` используются для хранения данных, передаваемых в функции и хранящих результат выполнения тестируемых функций.


**Возможные ошибки или улучшения:**

- **Обработка исключений:** В `extract_json` используется `try-except` для обработки ошибок при парсинге JSON. Это хорошо, но стоит проверить, достаточно ли это.  Возможно, стоит использовать более специфические исключения для разных видов ошибок парсинга.
- **Чёткость имени функции extract_json:** Возможно, стоит добавить в имя функции информацию о том, что происходит, например, `extract_json_from_string` или `parse_json_from_text`.


**Взаимосвязи с другими частями проекта:**

`extract_json` и `name_or_empty` вероятно используются в других частях проекта TinyTroupe, например, в обработке данных, полученных из внешних источников (файлов, API). `repeat_on_error` используется для улучшения надежности кода, предотвращая падения при возникновении ошибок.  `testing_utils` предоставляет вспомогательные функции, используемые для тестирования модуля `utils`.