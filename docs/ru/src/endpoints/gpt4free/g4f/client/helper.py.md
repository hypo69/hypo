# Модуль `helper.py`

## Обзор

Модуль `helper.py` содержит набор вспомогательных функций, предназначенных для обработки текстовых данных, в частности, для извлечения кода из блоков Markdown и JSON, поиска стоп-слов, фильтрации None значений и безопасного закрытия асинхронных генераторов. Эти функции используются для предварительной обработки и очистки данных, получаемых от AI-моделей, таких как GPT-4.

## Подробнее

Модуль предоставляет инструменты для работы со строками, содержащими код, и асинхронными генераторами. Функции модуля позволяют извлекать необходимую информацию из текста, отфильтровывать нежелательные данные и корректно завершать работу с асинхронными потоками данных. Этот код играет важную роль в обеспечении надежной и эффективной работы с текстовыми данными, особенно при взаимодействии с внешними источниками, такими как AI-модели.

## Функции

### `filter_markdown`

```python
def filter_markdown(text: str, allowd_types=None, default=None) -> str:
    """
    Parses code block from a string.

    Args:
        text (str): A string containing a code block.
        allowd_types: Список разрешенных типов кода (например, "python", "json"). Если `None`, разрешены все типы.
        default: Значение, возвращаемое, если блок кода не найден или его тип не разрешен. По умолчанию `None`.

    Returns:
        str: Код, извлеченный из блока Markdown, или значение `default`, если блок не найден или его тип не разрешен.
    """
```

**Назначение**: Извлекает блок кода из строки, содержащей Markdown.

**Параметры**:
- `text` (str): Строка, содержащая блок кода Markdown.
- `allowd_types`: Список разрешенных типов кода (например, "python", "json"). Если `None`, разрешены все типы.
- `default`: Значение, возвращаемое, если блок кода не найден или его тип не разрешен.

**Возвращает**:
- `str`: Код, извлеченный из блока Markdown, или значение `default`, если блок не найден или его тип не разрешен.

**Как работает функция**:

1.  Функция `filter_markdown` использует регулярное выражение для поиска блоков кода, заключенных в тройные обратные кавычки (`` ` ``).
2.  Она проверяет, соответствует ли тип кода (указанный после первых кавычек) одному из разрешенных типов в `allowd_types`.
3.  Если блок кода найден и его тип разрешен (или `allowd_types` не указан), функция возвращает извлеченный код.
4.  В противном случае функция возвращает значение `default`.

**Примеры**:

```python
text = "```python\nprint('Hello, world!')\n```"
code = filter_markdown(text, allowd_types=["python"])
print(code)  # Вывод: print('Hello, world!')

text = "```json\n{\"key\": \"value\"}\n```"
code = filter_markdown(text, allowd_types=["python"], default="No code found")
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

**Назначение**: Извлекает JSON из блока кода в строке.

**Параметры**:
- `text` (str): Строка, содержащая блок кода JSON.

**Возвращает**:
- `str`: JSON, извлеченный из блока кода.

**Как работает функция**:

1.  Функция `filter_json` вызывает функцию `filter_markdown` с параметрами, настроенными для извлечения JSON из блока кода.
2.  Она передает список `["", "json"]` в качестве `allowd_types`, чтобы разрешить блоки кода без указания типа или с типом "json".
3.  Также удаляет символы `^\\n ` из переданного текста

**Примеры**:

```python
text = "```json\n{\"key\": \"value\"}\n```"
json_code = filter_json(text)
print(json_code)  # Вывод: {"key": "value"}

text = "```\n{\"key\": \"value\"}\n```"
json_code = filter_json(text)
print(json_code)  # Вывод: {"key": "value"}
```

### `find_stop`

```python
def find_stop(stop: Optional[list[str]], content: str, chunk: str = None):
    """
    Находит первое вхождение одного из стоп-слов в тексте и обрезает текст до этого слова.

    Args:
        stop (Optional[list[str]]): Список стоп-слов для поиска. Если `None`, функция ничего не делает.
        content (str): Строка, в которой производится поиск.
        chunk (str, optional): Дополнительная строка, в которой также производится поиск. Defaults to None.

    Returns:
        tuple[int, str, str]: Кортеж, содержащий индекс первого найденного стоп-слова, обрезанный текст `content` и обрезанный текст `chunk`.
    """
```

**Назначение**: Находит первое вхождение одного из стоп-слов в тексте и обрезает текст до этого слова.

**Параметры**:
- `stop` (Optional[list[str]]): Список стоп-слов для поиска. Если `None`, функция ничего не делает.
- `content` (str): Строка, в которой производится поиск.
- `chunk` (str, optional): Дополнительная строка, в которой также производится поиск. По умолчанию `None`.

**Возвращает**:
- `tuple[int, str, str]`: Кортеж, содержащий индекс первого найденного стоп-слова, обрезанный текст `content` и обрезанный текст `chunk`.

**Как работает функция**:

1.  Функция `find_stop` ищет первое вхождение одного из стоп-слов в строке `content`.
2.  Если стоп-слова не указаны (`stop is None`), функция возвращает исходные значения.
3.  Если стоп-слово найдено, функция обрезает строку `content` до этого слова.
4.  Если также указана строка `chunk`, функция также обрезает ее до первого вхождения стоп-слова (если оно найдено).
5.  Функция возвращает индекс первого найденного стоп-слова, обрезанный текст `content` и обрезанный текст `chunk`.

**Примеры**:

```python
stop_words = ["stop", "end"]
content = "This is a stop word."
chunk = "Another chunk of text."
index, content, chunk = find_stop(stop_words, content, chunk)
print(index, content, chunk)  # Вывод: 10 This is a   Another chunk of text.

stop_words = ["stop", "end"]
content = "This is a content word."
chunk = "Another chunk of end text."
index, content, chunk = find_stop(stop_words, content, chunk)
print(index, content, chunk) # Вывод: (-1, 'This is a content word.', 'Another chunk of end text.')
```

### `filter_none`

```python
def filter_none(**kwargs) -> dict:
    """
    Создает новый словарь, содержащий только элементы из входного словаря, значения которых не равны `None`.

    Args:
        **kwargs: Произвольный набор именованных аргументов.

    Returns:
        dict: Новый словарь, содержащий только элементы из входного словаря, значения которых не равны `None`.
    """
```

**Назначение**: Создает новый словарь, содержащий только элементы из входного словаря, значения которых не равны `None`.

**Параметры**:
- `**kwargs`: Произвольный набор именованных аргументов.

**Возвращает**:
- `dict`: Новый словарь, содержащий только элементы из входного словаря, значения которых не равны `None`.

**Как работает функция**:

1.  Функция `filter_none` принимает произвольный набор именованных аргументов (`kwargs`).
2.  Она создает новый словарь, содержащий только те элементы из `kwargs`, значения которых не равны `None`.

**Примеры**:

```python
data = {"key1": "value1", "key2": None, "key3": "value3"}
filtered_data = filter_none(**data)
print(filtered_data)  # Вывод: {'key1': 'value1', 'key3': 'value3'}
```

### `safe_aclose`

```python
async def safe_aclose(generator: AsyncGenerator) -> None:
    """
    Безопасно закрывает асинхронный генератор, обрабатывая возможные исключения.

    Args:
        generator (AsyncGenerator): Асинхронный генератор, который необходимо закрыть.
    """
```

**Назначение**: Безопасно закрывает асинхронный генератор, обрабатывая возможные исключения.

**Параметры**:
- `generator` (AsyncGenerator): Асинхронный генератор, который необходимо закрыть.

**Как работает функция**:

1.  Функция `safe_aclose` пытается закрыть асинхронный генератор, вызывая метод `aclose()`.
2.  Если во время закрытия генератора возникает исключение, функция перехватывает его и логирует предупреждение.
3.  Функция проверяет наличие атрибута `aclose` у объекта `generator`, чтобы избежать ошибок при попытке закрытия объектов, не являющихся генераторами.
4.  Для логгирования используется модуль `logging`.

**Примеры**:

```python
import asyncio
import logging
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[int, None]:
    for i in range(3):
        yield i

async def main():
    gen = async_generator()
    try:
        async for value in gen:
            print(value)
            break
    finally:
        await safe_aclose(gen)

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    asyncio.run(main())