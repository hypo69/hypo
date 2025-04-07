# Модуль `helper.py`

## Обзор

Модуль `helper.py` содержит набор вспомогательных функций, предназначенных для обработки текста, извлечения информации из кода, фильтрации данных и безопасного закрытия асинхронных генераторов. Он используется в проекте `hypotez` для предобработки и фильтрации данных, получаемых из различных источников, например, ответах от GPT4Free.

## Подробней

Этот модуль предоставляет функции для извлечения блоков кода из текста, фильтрации JSON, поиска стоп-слов, фильтрации `None` значений и безопасного закрытия асинхронных генераторов. Он играет важную роль в подготовке данных для дальнейшей обработки и анализе в других частях проекта.

## Функции

### `filter_markdown`

```python
def filter_markdown(text: str, allowd_types=None, default=None) -> str:
    """
    Parses code block from a string.

    Args:
        text (str): A string containing a code block.
        allowd_types: list of allowed types
        default: default value

    Returns:
        dict: A dictionary parsed from the code block.
    """
```

**Назначение**: Извлекает блок кода из строки, используя регулярное выражение для поиска блоков, заключенных в тройные обратные кавычки (markdown code fences).

**Параметры**:
- `text` (str): Строка, содержащая блок кода.
- `allowd_types`: Список разрешенных типов блоков кода. Если `None`, то принимаются все типы.
- `default`: Значение по умолчанию, которое возвращается, если блок кода не найден или его тип не разрешен.

**Возвращает**:
- `str`: Извлеченный блок кода или значение по умолчанию, если блок не найден или не соответствует разрешенным типам.

**Как работает функция**:
1. Функция использует регулярное выражение для поиска блоков кода, заключенных в тройные обратные кавычки.
2. Если блок кода найден, проверяется, разрешен ли его тип (если `allowd_types` не `None`).
3. Если блок кода найден и его тип разрешен, функция возвращает содержимое блока кода.
4. Если блок кода не найден или его тип не разрешен, функция возвращает значение по умолчанию.

```
A: Поиск блока кода с использованием регулярного выражения
|
B: Проверка, найден ли блок кода
|
C: Проверка, разрешен ли тип блока кода (если allowd_types не None)
|
D: Возврат содержимого блока кода (если найден и разрешен)
|
E: Возврат значения по умолчанию (если не найден или не разрешен)
```

**Примеры**:

```python
text = "```python\nprint('Hello, world!')\n```"
code = filter_markdown(text)
print(code)  # Вывод: print('Hello, world!')

text = "```json\n{\"key\": \"value\"}\n```"
code = filter_markdown(text, allowd_types=['python'])
print(code)  # Вывод: None

text = "Не содержит блока кода"
code = filter_markdown(text, default="No code found")
print(code)  # Вывод: No code found
```

### `filter_json`

```python
def filter_json(text: str) -> str:
    """
    Parses JSON code block from a string.

    Args:
        text (str): A string containing a JSON code block.

    Returns:
        dict: A dictionary parsed from the JSON code block.
    """
```

**Назначение**: Извлекает JSON блок из строки. Вызывает функцию `filter_markdown` с указанием, что разрешены только типы блоков кода `"json"` или пустой тип (`""`).

**Параметры**:
- `text` (str): Строка, содержащая JSON блок.

**Возвращает**:
- `str`: Извлеченный JSON блок или исходную строку, если блок не найден.

**Как работает функция**:
1.  Функция вызывает `filter_markdown` с параметрами `text`, `allowd_types=["", "json"]` и `default=text.strip("^\\n ")`.
2.  Функция `filter_markdown` ищет блоки кода с типом `json` или без указания типа и возвращает их содержимое. Если блок не найден, возвращается исходная строка.

**Примеры**:

```python
text = "```json\n{\"key\": \"value\"}\n```"
json_code = filter_json(text)
print(json_code)  # Вывод: {"key": "value"}

text = "```python\nprint('Hello, world!')\n```"
json_code = filter_json(text)
print(json_code)  # Вывод: ```python\nprint('Hello, world!')\n```

text = "Не содержит JSON блока"
json_code = filter_json(text)
print(json_code)  # Вывод: Не содержит JSON блока
```

### `find_stop`

```python
def find_stop(stop: Optional[list[str]], content: str, chunk: str = None):
    first = -1
    word = None
    if stop is not None:
        for word in list(stop):
            first = content.find(word)
            if first != -1:
                content = content[:first]
                break
        if chunk is not None and first != -1:
            first = chunk.find(word)
            if first != -1:
                chunk = chunk[:first]
            else:
                first = 0
    return first, content, chunk
```

**Назначение**: Ищет первое вхождение одного из стоп-слов в строке `content` и, если найдено, обрезает строку до этого вхождения.

**Параметры**:
- `stop` (Optional[list[str]]): Список стоп-слов, которые нужно искать. Если `None`, поиск не производится.
- `content` (str): Строка, в которой производится поиск стоп-слов.
- `chunk` (str, optional): Дополнительная строка, которая также обрезается, если стоп-слово найдено. По умолчанию `None`.

**Возвращает**:
- `tuple[int, str, str | None]`: Кортеж, содержащий индекс первого найденного стоп-слова, обрезанную строку `content` и обрезанную строку `chunk` (если она была передана).

**Как работает функция**:

1.  Инициализирует `first` как `-1` и `word` как `None`.
2.  Проверяет, что список стоп-слов `stop` не `None`.
3.  Если `stop` не `None`, перебирает стоп-слова в списке.
4.  Для каждого стоп-слова ищет его первое вхождение в строке `content` с помощью метода `find()`.
5.  Если стоп-слово найдено (индекс не `-1`), обрезает строку `content` до этого индекса.
6.  Если `chunk` не `None` и стоп-слово было найдено в `content`, ищет это же стоп-слово в `chunk`.
7.  Если стоп-слово найдено в `chunk`, обрезает строку `chunk` до этого индекса. Если не найдено, устанавливает `first` в `0`.
8.  Возвращает кортеж, содержащий индекс первого найденного стоп-слова (`first`), обрезанную строку `content` и обрезанную строку `chunk` (если она была передана).

```
A: Проверка, что список стоп-слов `stop` не `None`
|
B: Перебор стоп-слов в списке
|
C: Поиск стоп-слова в строке `content`
|
D: Проверка, найдено ли стоп-слово
|
E: Обрезка строки `content` до индекса стоп-слова
|
F: Проверка, что `chunk` не `None` и стоп-слово было найдено в `content`
|
G: Поиск стоп-слова в строке `chunk`
|
H: Проверка, найдено ли стоп-слово в `chunk`
|
I: Обрезка строки `chunk` до индекса стоп-слова
|
J: Возврат кортежа с результатами
```

**Примеры**:

```python
stop_words = ["stop", "end"]
content = "This is a stop word example."
chunk = "This is a chunk example."
first, content, chunk = find_stop(stop_words, content, chunk)
print(first, content, chunk)  # Вывод: 10 This is a  This is a chunk example.

stop_words = ["stop", "end"]
content = "This is a test example."
chunk = "This is a chunk end example."
first, content, chunk = find_stop(stop_words, content, chunk)
print(first, content, chunk)  # Вывод: -1 This is a test example. This is a chunk end example.

stop_words = ["stop", "end"]
content = "This is a test example."
chunk = None
first, content, chunk = find_stop(stop_words, content, chunk)
print(first, content, chunk)  # Вывод: -1 This is a test example. None

stop_words = ["stop", "end"]
content = "This is a stop word example."
chunk = "This is a chunk stop example."
first, content, chunk = find_stop(stop_words, content, chunk)

print(first, content, chunk)  # Вывод: 10 This is a   This is a chunk
```

### `filter_none`

```python
def filter_none(**kwargs) -> dict:
    return {
        key: value
        for key, value in kwargs.items()
        if value is not None
    }
```

**Назначение**: Фильтрует словарь, удаляя элементы, значения которых равны `None`.

**Параметры**:
- `**kwargs`: Произвольное количество именованных аргументов, представляющих собой словарь.

**Возвращает**:
- `dict`: Новый словарь, содержащий только элементы, значения которых не равны `None`.

**Как работает функция**:
1.  Использует генератор словаря для итерации по всем элементам входного словаря (`kwargs`).
2.  Для каждого элемента проверяет, является ли его значение `None`.
3.  Если значение не `None`, элемент включается в новый словарь.
4.  Возвращает новый словарь, содержащий только элементы с не-`None` значениями.

```
A: Получение именованных аргументов в виде словаря `kwargs`
|
B: Итерация по элементам словаря `kwargs`
|
C: Проверка, является ли значение элемента `None`
|
D: Включение элемента в новый словарь (если значение не `None`)
|
E: Возврат нового словаря
```

**Примеры**:

```python
filtered_dict = filter_none(a=1, b=None, c="hello")
print(filtered_dict)  # Вывод: {'a': 1, 'c': 'hello'}

filtered_dict = filter_none(a=None, b=None)
print(filtered_dict)  # Вывод: {}

filtered_dict = filter_none(a=1, b=2, c=3)
print(filtered_dict)  # Вывод: {'a': 1, 'b': 2, 'c': 3}
```

### `safe_aclose`

```python
async def safe_aclose(generator: AsyncGenerator) -> None:
    try:
        if generator and hasattr(generator, 'aclose'):
            await generator.aclose()
    except Exception as e:
        logging.warning(f"Error while closing generator: {e}")
```

**Назначение**: Безопасно закрывает асинхронный генератор, обрабатывая возможные исключения.

**Параметры**:
- `generator` (AsyncGenerator): Асинхронный генератор, который нужно закрыть.

**Возвращает**:
- `None`

**Как работает функция**:
1.  Проверяет, что `generator` не `None` и имеет атрибут `aclose`.
2.  Если обе проверки пройдены, пытается вызвать метод `aclose` для закрытия генератора.
3.  Если во время закрытия генератора возникает исключение, перехватывает его и записывает предупреждение в лог.

```
A: Проверка, что `generator` не `None` и имеет атрибут `aclose`
|
B: Вызов метода `aclose` для закрытия генератора
|
C: Перехват исключений, возникающих во время закрытия
|
D: Запись предупреждения в лог (если исключение возникло)
```

**Примеры**:

```python
import asyncio
import logging
import sys

from typing import AsyncGenerator

async def example_generator() -> AsyncGenerator[int, None]:
    for i in range(3):
        yield i

async def main():
    generator = example_generator()
    try:
        async for value in generator:
            print(value)
    finally:
        await safe_aclose(generator)

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING, stream=sys.stdout)
    asyncio.run(main())