# Модуль `helper`

## Обзор

Модуль `helper` содержит набор вспомогательных функций для обработки текста, включая фильтрацию кода из Markdown блоков, JSON блоков, а также для поиска стоп-слов в тексте и безопасного закрытия асинхронных генераторов.

## Подробней

Этот модуль предоставляет инструменты для извлечения информации из текста, форматированного в Markdown или JSON, а также для управления асинхронными операциями. Он используется для предобработки и очистки данных, полученных из различных источников, таких как ответы от AI-моделей.

## Функции

### `filter_markdown`

```python
def filter_markdown(text: str, allowd_types=None, default=None) -> str:
    """
    Извлекает блок кода из строки.

    Args:
        text (str): Строка, содержащая блок кода.
        allowd_types: Список разрешенных типов кода.
        default: Значение по умолчанию, возвращаемое, если блок кода не найден.

    Returns:
        str: Блок кода, извлеченный из строки.
    """
```

**Назначение**: Извлекает блок кода из строки, форматированной в Markdown.

**Параметры**:
- `text` (str): Строка, содержащая блок кода.
- `allowd_types`: Список разрешенных типов кода. Если `None`, разрешены все типы.
- `default`: Значение по умолчанию, возвращаемое, если блок кода не найден или его тип не разрешен.

**Возвращает**:
- `str`: Блок кода, извлеченный из строки. Если блок кода не найден или его тип не разрешен, возвращается значение `default`.

**Как работает функция**:

1. Функция использует регулярное выражение для поиска блока кода, заключенного между ```.
2. Если `allowd_types` не указан или тип кода входит в список разрешенных, функция возвращает извлеченный блок кода.
3. В противном случае возвращается значение `default`.

**Примеры**:

```python
text = "```python\nprint('Hello, world!')\n```"
code = filter_markdown(text, allowd_types=['python'])
print(code)  # Вывод: print('Hello, world!')

text = "```json\n{'key': 'value'}\n```"
code = filter_markdown(text, allowd_types=['python'], default='No code')
print(code)  # Вывод: No code
```

### `filter_json`

```python
def filter_json(text: str) -> str:
    """
    Извлекает JSON блок кода из строки.

    Args:
        text (str): Строка, содержащая JSON блок кода.

    Returns:
        str: JSON блок кода, извлеченный из строки.
    """
```

**Назначение**: Извлекает JSON блок кода из строки, форматированной в Markdown.

**Параметры**:
- `text` (str): Строка, содержащая JSON блок кода.

**Возвращает**:
- `str`: JSON блок кода, извлеченный из строки.

**Как работает функция**:

1. Функция вызывает `filter_markdown` с параметрами, чтобы извлечь JSON блок кода.
2. Разрешенные типы кода - `""` и `"json"`.
3. Если JSON блок кода не найден, возвращается исходный текст, очищенный от начальных и конечных пробелов и символов новой строки.

**Примеры**:

```python
text = "```json\n{'key': 'value'}\n```"
json_code = filter_json(text)
print(json_code)  # Вывод: {'key': 'value'}

text = "Some text\n{'key': 'value'}\n"
json_code = filter_json(text)
print(json_code)  # Вывод: {'key': 'value'}
```

### `find_stop`

```python
def find_stop(stop: Optional[list[str]], content: str, chunk: str = None):
    """
    Находит первое вхождение стоп-слова в содержимом.

    Args:
        stop (Optional[list[str]]): Список стоп-слов для поиска.
        content (str): Строка, в которой производится поиск.
        chunk (str, optional): Дополнительная строка для поиска. По умолчанию None.

    Returns:
        tuple: Индекс первого вхождения стоп-слова, измененное содержимое и измененный чанк.
    """
```

**Назначение**: Находит первое вхождение стоп-слова в содержимом и обрезает содержимое до этого стоп-слова.

**Параметры**:
- `stop` (Optional[list[str]]): Список стоп-слов для поиска.
- `content` (str): Строка, в которой производится поиск.
- `chunk` (str, optional): Дополнительная строка для поиска. По умолчанию `None`.

**Возвращает**:
- `tuple`: Кортеж, содержащий:
  - Индекс первого вхождения стоп-слова (`first`).
  - Измененное содержимое (`content`), обрезанное до стоп-слова.
  - Измененный чанк (`chunk`), обрезанный до стоп-слова (если `chunk` не `None`).

**Как работает функция**:

1. Функция перебирает стоп-слова из списка `stop`.
2. Для каждого стоп-слова ищет его первое вхождение в `content`.
3. Если стоп-слово найдено, `content` обрезается до этого стоп-слова, и поиск прекращается.
4. Если `chunk` не `None`, то же самое делается и для `chunk`.
5. Возвращается индекс первого вхождения стоп-слова и обрезанные `content` и `chunk`.

**Примеры**:

```python
stop_words = ["stop", "end"]
content = "This is a stop word."
first, content, _ = find_stop(stop_words, content)
print(first, content)  # Вывод: 10 This is a

content = "This is a test end word."
first, content, _ = find_stop(stop_words, content)
print(first, content)  # Вывод: 15 This is a test

stop_words = ["stop", "end"]
content = "This is a stop word."
chunk = "Some additional text."
first, content, chunk = find_stop(stop_words, content, chunk)
print(first, content, chunk)
# Вывод:
# 10 This is a Some additional text.
```

### `filter_none`

```python
def filter_none(**kwargs) -> dict:
    """
    Фильтрует словарь, удаляя элементы со значением None.

    Args:
        **kwargs: Произвольные именованные аргументы.

    Returns:
        dict: Новый словарь, содержащий только элементы с не-None значениями.
    """
```

**Назначение**: Создает новый словарь, содержащий только элементы из входных аргументов, у которых значения не `None`.

**Параметры**:
- `**kwargs`: Произвольные именованные аргументы.

**Возвращает**:
- `dict`: Новый словарь, содержащий только элементы с не-`None` значениями.

**Как работает функция**:

1. Функция принимает произвольные именованные аргументы (`kwargs`).
2. Она создает новый словарь, перебирая элементы `kwargs` и включая в новый словарь только те элементы, у которых значения не `None`.

**Примеры**:

```python
filtered_dict = filter_none(a=1, b=None, c="test")
print(filtered_dict)  # Вывод: {'a': 1, 'c': 'test'}

filtered_dict = filter_none(a=None, b=None)
print(filtered_dict)  # Вывод: {}
```

### `safe_aclose`

```python
async def safe_aclose(generator: AsyncGenerator) -> None:
    """
    Безопасно закрывает асинхронный генератор.

    Args:
        generator (AsyncGenerator): Асинхронный генератор для закрытия.

    Returns:
        None
    """
```

**Назначение**: Безопасно закрывает асинхронный генератор, обрабатывая возможные исключения.

**Параметры**:
- `generator` (AsyncGenerator): Асинхронный генератор для закрытия.

**Возвращает**:
- `None`

**Как работает функция**:

1. Функция проверяет, существует ли генератор и имеет ли он метод `aclose`.
2. Если да, то пытается закрыть генератор, вызывая `await generator.aclose()`.
3. Если во время закрытия возникает исключение, оно перехватывается, и в журнал записывается предупреждение.

**Примеры**:

```python
import asyncio
from src.logger import logger

async def async_generator():
    try:
        for i in range(3):
            yield i
            await asyncio.sleep(0.1)
    finally:
        logger.info("Async generator closed")

async def main():
    gen = async_generator()
    async for i in gen:
        print(i)
        if i == 1:
            await safe_aclose(gen)
            break

asyncio.run(main())