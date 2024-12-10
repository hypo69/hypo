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

1. Принимает строку `text` на вход.
2. Ищет JSON-объект (или массив) в строке.
3. Если JSON найден, парсит его и возвращает.
4. Если JSON не найден или при парсинге возникает ошибка, возвращает пустой словарь `{}`.

**Функция `name_or_empty`:**

1. Принимает объект `entity` на вход.
2. Если объект не `None` и у него есть атрибут `name`, возвращает его значение.
3. Если объект `None` или атрибут `name` отсутствует, возвращает пустую строку `""`.

**Функция `repeat_on_error`:**

1. Принимает функцию `decorated_function` на вход.
2. Устанавливает максимальное количество попыток `retries` и список исключений `exceptions`.
3. При вызове `decorated_function` пытается выполнить ее.
4. Если происходит исключение, указанное в `exceptions`, повторно выполняет функцию, до тех пор пока попытки не исчерпаны или не будет достигнуто успешное выполнение.
5. Возвращает результат выполнения, либо вызывает исключение, если все попытки закончились неудачей.

**Пример (extract_json):**

Вход: `'Some text before {"key": "value"} some text after'`
Выход: `{'key': 'value'}`

**Пример (name_or_empty):**

Вход: `MockEntity("Test")` (где `MockEntity` имеет атрибут `name`)
Выход: `"Test"`

**Пример (repeat_on_error):**

Вход: функция, которая вызывает `dummy_function`, которая может кидать `DummyException`
Выход: повторение функции, пока не получится без `DummyException`, либо сброс исключения.


# <mermaid>

```mermaid
graph TD
    subgraph "extract_json"
        A[text] --> B{Find JSON};
        B -- Yes --> C[Parse JSON];
        B -- No --> D[Return {}];
        C --> E[Return JSON];
        D --> E;
    end

    subgraph "name_or_empty"
        F[entity] --> G{entity is None?};
        G -- Yes --> H[Return ""];
        G -- No --> I{entity has 'name'?};
        I -- Yes --> J[Return entity.name];
        I -- No --> H;
        H --> K[Return];
    end

    subgraph "repeat_on_error"
        L[decorated_function] --> M{Exception in exceptions?};
        M -- Yes --> N[Retry];
        M -- No --> O[Return Result];
        N --> L;
        O --> P[Return];

        subgraph "Retry"
          N --  --> Q[Attempt Count < retries?];
          Q -- Yes --> L;
          Q -- No --> R[Raise Exception];
        end
    end
        E --> Result;
        J --> Result;
        K --> Result;
        P --> Result;
        R --> Result;

```

# <explanation>

**Импорты:**

- `pytest`: фреймворк для тестирования.
- `unittest.mock.MagicMock`: для создания "моков" (заглушек) функций и объектов.
- `sys`: для изменения пути поиска модулей.
- `tinytroupe.utils`: собственный модуль проекта, содержащий полезные функции, такие как парсинг JSON и обработка ошибок.
- `testing_utils`:  предполагаемый модуль для тестирования, возможно, содержащий вспомогательные функции или классы.

**Классы:**

- `MockEntity`:  Простой класс для тестирования, он содержит атрибут `name` для хранения имени. Использовался только для тестирования функции `name_or_empty`.

**Функции:**

- `extract_json(text)`:  Парсит JSON из строки. Возвращает JSON-объект или пустой словарь, если JSON не найден или ошибка. Используется для извлечения JSON фрагментов.
- `name_or_empty(entity)`: Возвращает имя сущности, если оно задано, или пустую строку, если сущность `None` или у нее нет имени.
- `repeat_on_error(retries, exceptions, decorated_function)`: Декоратор, который повторяет вызов функции, пока не достигнут `retries` или не возникнет исключение, не указанное в `exceptions`.  Это полезно для обработки ситуаций, где может возникнуть временная ошибка при запросе к внешнему API или другому ресурсу.

**Переменные:**

- `text`, `result`: строковые и словарике переменные, использующиеся при тестировании для хранения входных данных и результатов извлечения JSON.

**Возможные ошибки или улучшения:**

- Нет проверки типов входных данных для `extract_json` (может быть ошибка, если `text` не строка).
- Отсутствие документации для функций `extract_json` и `name_or_empty`.
- `repeat_on_error` обрабатывает только заданные исключения. Следовало бы использовать более общие обработки ошибок, например `except Exception` для большей гибкости.
- Не совсем понятно назначение `sys.path.append`  , оно может привести к проблемам импортирования, если вложенные пути не корректны. Рекомендуется использовать `relative imports` ('.', '..') где это возможно.
- Лучше было бы сделать `extract_json` более универсальной, обрабатывая разные типы JSON (например, массивы).
- `TODO` комментарий указывает на не реализованную функцию, что требует более подробного пояснения.


**Взаимосвязь с другими частями проекта:**

Функции `extract_json`, `name_or_empty` и `repeat_on_error` входят в модуль `utils` проекта `tinytroupe`. Вероятно, эти функции используются в других частях проекта для обработки данных. Модуль `testing_utils` явно используется для тестирования.  Без контекста проекта трудно сказать, как эти функции используются в других частях кода.