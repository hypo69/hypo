# Модуль для валидации данных в TinyTroupe

## Обзор

Модуль `validation.py` предоставляет набор функций для проверки и очистки данных, используемых в проекте TinyTroupe. Он включает в себя функции для проверки допустимости полей в словарях и для очистки строк от недопустимых символов.

## Подробней

Этот модуль содержит функции, которые помогают обеспечить целостность и безопасность данных, используемых в TinyTroupe. Валидация и очистка данных являются важными шагами для предотвращения ошибок и защиты от потенциальных угроз безопасности.

## Функции

### `check_valid_fields`

```python
def check_valid_fields(obj: dict, valid_fields: list) -> None:
    """
    Checks whether the fields in the specified dict are valid, according to the list of valid fields. If not, raises a ValueError.
    """
```

**Назначение**: Проверяет, являются ли поля в указанном словаре допустимыми, согласно списку допустимых полей. Если нет, вызывает исключение `ValueError`.

**Параметры**:
- `obj` (dict): Словарь, поля которого необходимо проверить.
- `valid_fields` (list): Список допустимых полей.

**Возвращает**:
- `None`: Функция ничего не возвращает. Если поля недопустимы, вызывается исключение.

**Вызывает исключения**:
- `ValueError`: Если обнаружено недопустимое поле в словаре.

**Как работает функция**:

1. Функция перебирает все ключи в словаре `obj`.
2. Для каждого ключа проверяется, присутствует ли он в списке допустимых полей `valid_fields`.
3. Если ключ отсутствует в списке допустимых полей, вызывается исключение `ValueError` с сообщением об ошибке, указывающим недопустимый ключ и список допустимых ключей.

```
Проверка полей
│
└── Проверка каждого ключа в словаре
    │
    ├── Ключ в списке допустимых полей?
    │   ├── Да: переход к следующему ключу
    │   └── Нет: Вызов ValueError
    │
    └── Все ключи проверены
```

**Примеры**:

```python
# Пример 1: Успешная проверка
data = {"name": "John", "age": 30}
valid_keys = ["name", "age"]
check_valid_fields(data, valid_keys)  # Функция не вызовет исключение

# Пример 2: Неуспешная проверка (вызов ValueError)
data = {"name": "John", "age": 30, "city": "New York"}
valid_keys = ["name", "age"]
# check_valid_fields(data, valid_keys)  # Вызовет ValueError: Invalid key city in dictionary. Valid keys are: ['name', 'age']
```

### `sanitize_raw_string`

```python
def sanitize_raw_string(value: str) -> str:
    """
    Sanitizes the specified string by: 
      - removing any invalid characters.
      - ensuring it is not longer than the maximum Python string length.
    
    This is for an abundance of caution with security, to avoid any potential issues with the string.
    """
```

**Назначение**: Очищает указанную строку путем удаления любых недопустимых символов и обеспечения ее длины не больше максимальной длины строки в Python.

**Параметры**:
- `value` (str): Строка, которую необходимо очистить.

**Возвращает**:
- `str`: Очищенная строка.

**Как работает функция**:

1. Преобразует строку в кодировку UTF-8, игнорируя недопустимые символы.
2. Нормализует строку, используя форму NFC (Normalization Form C).
3. Обрезает строку до максимальной длины строки в Python (`sys.maxsize`).

```
Очистка строки
│
├── Кодирование в UTF-8 (игнорирование ошибок)
│
├── Нормализация NFC
│
└── Обрезка до максимальной длины строки
```

**Примеры**:

```python
# Пример 1: Очистка строки с недопустимыми символами
raw_string = "H\x00e\x01l\x02l\x03o"
sanitized_string = sanitize_raw_string(raw_string)
print(sanitized_string)  # Вывод: Hello

# Пример 2: Очистка строки с символами Unicode
raw_string = "éàçüö"
sanitized_string = sanitize_raw_string(raw_string)
print(sanitized_string)  # Вывод: éàçüö

# Пример 3: Обрезка длинной строки
import sys
long_string = "A" * (sys.maxsize + 100)
sanitized_string = sanitize_raw_string(long_string)
print(len(sanitized_string))  # Вывод: <максимальная длина строки в Python>
```

### `sanitize_dict`

```python
def sanitize_dict(value: dict) -> dict:
    """
    Sanitizes the specified dictionary by:
      - removing any invalid characters.
      - ensuring that the dictionary is not too deeply nested.
    """
```

**Назначение**: Очищает указанный словарь путем удаления любых недопустимых символов из строковых значений и обеспечения того, что словарь не является слишком глубоко вложенным.

**Параметры**:
- `value` (dict): Словарь, который необходимо очистить.

**Возвращает**:
- `dict`: Очищенный словарь.

**Как работает функция**:

1. Функция перебирает все элементы словаря `value`.
2. Для каждого значения проверяется, является ли оно строкой.
3. Если значение является строкой, оно очищается с помощью функции `sanitize_raw_string`.
4. Возвращает очищенный словарь.

```
Очистка словаря
│
└── Перебор элементов словаря
    │
    ├── Значение - строка?
    │   ├── Да: Очистка строки с помощью sanitize_raw_string
    │   └── Нет: Пропустить
    │
    └── Все элементы проверены
```

**Примеры**:

```python
# Пример 1: Очистка словаря со строковыми значениями
data = {"name": "John\x00", "age": "30", "city": "New York"}
sanitized_data = sanitize_dict(data)
print(sanitized_data)  # Вывод: {'name': 'John', 'age': '30', 'city': 'New York'}

# Пример 2: Словарь без строковых значений
data = {"name": 123, "age": 30, "city": True}
sanitized_data = sanitize_dict(data)
print(sanitized_data)  # Вывод: {'name': 123, 'age': 30, 'city': True}