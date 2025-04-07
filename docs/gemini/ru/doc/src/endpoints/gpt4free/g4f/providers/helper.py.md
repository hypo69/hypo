# Модуль `helper.py`

## Обзор

Модуль `helper.py` содержит набор вспомогательных функций, используемых для обработки и форматирования текста, работы со строками, куками и сообщениями. Эти функции используются в различных частях проекта для подготовки данных к отправке в языковые модели и обработки ответов от них.

## Подробнее

Модуль предоставляет функции для преобразования данных в строковый формат, форматирования промптов для языковых моделей, генерации случайных строк, фильтрации `None` значений из словарей, конкатенации чанков данных и форматирования куки. Он играет важную роль в подготовке данных для взаимодействия с внешними API и обеспечивает единообразный подход к обработке текста.

## Функции

### `to_string`

```python
def to_string(value) -> str:
    """
    Преобразует значение в строку.

    Args:
        value: Значение для преобразования.

    Returns:
        str: Строковое представление значения.

    Как работает функция:
    1. Проверяет, является ли входное значение строкой. Если да, возвращает его.
    2. Если значение является словарем, проверяет наличие ключей "name" или "bucket_id".
       - Если есть "name", возвращает пустую строку.
       - Если есть "bucket_id", читает содержимое bucket и возвращает его.
       - Если есть "type" равный "text", возвращает значение ключа "text".
    3. Если значение является списком, рекурсивно преобразует каждый элемент списка в строку и объединяет их.
    4. В противном случае, преобразует значение в строку с помощью `str()`.

    ASCII flowchart:
    Value -> Is String?
      |  Yes: Return Value
      |  No: Is Dict?
      |    | Yes: Check 'name'/'bucket_id'/'type'
      |    | No: Is List?
      |    |   | Yes: Recursively convert elements to string and join
      |    |   | No: Convert to string using str()

    Примеры:
        >>> to_string("hello")
        'hello'
        >>> to_string({"type": "text", "text": "world"})
        'world'
    """
    ...
```

### `format_prompt`

```python
def format_prompt(messages: Messages, add_special_tokens: bool = False, do_continue: bool = False, include_system: bool = True) -> str:
    """
    Форматирует список сообщений в строку для использования в запросах к языковой модели.

    Args:
        messages (Messages): Список словарей, содержащих роли и содержимое сообщений.
        add_special_tokens (bool, optional): Флаг добавления специальных токенов форматирования. По умолчанию `False`.
        do_continue (bool, optional): Флаг для продолжения форматирования. По умолчанию `False`.
        include_system (bool, optional): Флаг, указывающий, следует ли включать системные сообщения. По умолчанию `True`.

    Returns:
        str: Отформатированная строка, содержащая все сообщения.

    Как работает функция:
    1. Если `add_special_tokens` равно `False` и количество сообщений меньше или равно 1, возвращает содержимое первого сообщения, преобразованное в строку.
    2. Фильтрует системные сообщения в зависимости от значения `include_system`.
    3. Форматирует сообщения в виде строк "Role: Content".
    4. Объединяет отформатированные сообщения в одну строку, разделенную символом новой строки.
    5. Если `do_continue` равно `True`, возвращает отформатированную строку.
    6. В противном случае, добавляет "Assistant:" в конец строки.

    ASCII flowchart:
    Messages -> Check add_special_tokens & len(messages)
      |  Yes: Return to_string(messages[0]["content"])
      |  No: Filter system messages based on include_system
      |  -> Format messages as "Role: Content"
      |  -> Join formatted messages with newline
      |  -> Check do_continue
      |     | Yes: Return formatted
      |     | No: Add "Assistant:" and return

    Примеры:
        >>> messages = [{"role": "user", "content": "hello"}, {"role": "assistant", "content": "world"}]
        >>> format_prompt(messages)
        'User: hello\\nAssistant: world\\nAssistant:'
        >>> format_prompt(messages, add_special_tokens=True)
        'User: hello\\nAssistant: world\\nAssistant:'
    """
    ...
```

### `get_system_prompt`

```python
def get_system_prompt(messages: Messages) -> str:
    """
    Извлекает системные промпты из списка сообщений.

    Args:
        messages (Messages): Список словарей, содержащих роли и содержимое сообщений.

    Returns:
        str: Объединенная строка, содержащая все системные промпты.

    Как работает функция:
    1. Фильтрует сообщения, оставляя только те, у которых роль равна "system".
    2. Извлекает содержимое каждого системного сообщения.
    3. Объединяет содержимое системных сообщений в одну строку, разделенную символом новой строки.

    ASCII flowchart:
    Messages -> Filter messages where role == "system"
      |  -> Extract content from each system message
      |  -> Join content with newline
      |  -> Return joined string

    Примеры:
        >>> messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "hello"}]
        >>> get_system_prompt(messages)
        'You are a helpful assistant.'
    """
    ...
```

### `get_last_user_message`

```python
def get_last_user_message(messages: Messages) -> str:
    """
    Извлекает последнее сообщение пользователя из списка сообщений.

    Args:
        messages (Messages): Список словарей, содержащих роли и содержимое сообщений.

    Returns:
        str: Последнее сообщение пользователя.

    Как работает функция:
    1. Создает копию списка сообщений.
    2. Итерируется по сообщениям в обратном порядке, пока не найдет сообщение с ролью "user".
    3. Если находит сообщение пользователя, извлекает его содержимое, удаляет пробелы в начале и конце и добавляет в список пользовательских сообщений.
    4. Если встречает сообщение с любой другой ролью, возвращает объединенную строку пользовательских сообщений в обратном порядке.
    5. Если список сообщений пуст или не содержит сообщений пользователя, возвращает объединенную строку пользовательских сообщений в обратном порядке.

    ASCII flowchart:
    Messages -> Create copy of messages
      |  -> Iterate through messages in reverse order
      |     | -> If message["role"] == "user":
      |     |    | -> Extract and strip content
      |     |    | -> Append to user_messages
      |     | -> Else:
      |     |    | -> Return joined user_messages in reverse order
      |  -> Return joined user_messages in reverse order

    Примеры:
        >>> messages = [{"role": "assistant", "content": "hi"}, {"role": "user", "content": "hello"}, {"role": "user", "content": "world"}]
        >>> get_last_user_message(messages)
        'world\\nhello'
    """
    ...
```

### `format_image_prompt`

```python
def format_image_prompt(messages, prompt: str = None) -> str:
    """
    Форматирует промпт для генерации изображений.

    Args:
        messages: Список сообщений.
        prompt (str, optional): Промпт. По умолчанию `None`.

    Returns:
        str: Сформулированный промпт для генерации изображений.

    Как работает функция:
    1. Если prompt равен None, возвращает последнее сообщение пользователя, полученное с помощью функции get_last_user_message.
    2. В противном случае возвращает prompt.

    ASCII flowchart:
    prompt -> Is None?
      |  Yes: Return get_last_user_message(messages)
      |  No: Return prompt

    Примеры:
        >>> messages = [{"role": "user", "content": "hello"}]
        >>> format_image_prompt(messages)
        'hello'
        >>> format_image_prompt(messages, prompt="world")
        'world'
    """
    ...
```

### `format_prompt_max_length`

```python
def format_prompt_max_length(messages: Messages, max_lenght: int) -> str:
    """
    Форматирует промпт, обрезая его до максимальной длины.

    Args:
        messages (Messages): Список сообщений.
        max_lenght (int): Максимальная длина промпта.

    Returns:
        str: Отформатированный и обрезанный промпт.

    Как работает функция:
    1. Форматирует сообщения с помощью `format_prompt`.
    2. Проверяет длину отформатированного промпта. Если она превышает `max_lenght`:
       - Если количество сообщений больше 6, форматирует только первые 3 и последние 3 сообщения.
       - Если длина все еще превышает `max_lenght`, и количество сообщений больше 2, форматирует только системные сообщения и последнее сообщение.
       - Если длина все еще превышает `max_lenght`, берет содержимое только последнего сообщения.
    3. Логирует информацию об урезании сообщения.

    ASCII flowchart:
    Messages, max_lenght -> format_prompt(messages)
      |  -> prompt_length > max_lenght?
      |     | Yes: len(messages) > 6?
      |     |    | Yes: format_prompt(messages[:3] + messages[-3:])
      |     |    | No: len(messages) > 2?
      |     |    |    | Yes: format_prompt([m for m in messages if m["role"] == "system"] + messages[-1:])
      |     |    |    | No: messages[-1]["content"]
      |  -> Return prompt

    Примеры:
        >>> messages = [{"role": "user", "content": "hello" * 1000}]
        >>> format_prompt_max_length(messages, 100)
        'hellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohello'
    """
    ...
```

### `get_random_string`

```python
def get_random_string(length: int = 10) -> str:
    """
    Генерирует случайную строку заданной длины, содержащую строчные буквы и цифры.

    Args:
        length (int, optional): Длина случайной строки. По умолчанию 10.

    Returns:
        str: Случайная строка заданной длины.

    Как работает функция:
    1. Генерирует случайную строку, выбирая символы из строчных букв и цифр.
    2. Повторяет выбор символов `length` раз.
    3. Объединяет выбранные символы в строку.

    ASCII flowchart:
    length -> Generate random string
      |  -> Choose from lowercase letters and digits
      |  -> Repeat length times
      |  -> Join characters into string
      |  -> Return random string

    Примеры:
        >>> get_random_string(5)
        'f3gh7'
    """
    ...
```

### `get_random_hex`

```python
def get_random_hex(length: int = 32) -> str:
    """
    Генерирует случайную шестнадцатеричную строку заданной длины.

    Args:
        length (int, optional): Длина шестнадцатеричной строки. По умолчанию 32.

    Returns:
        str: Случайная шестнадцатеричная строка.

    Как работает функция:
    1. Генерирует случайную шестнадцатеричную строку, выбирая символы из "abcdef" и цифр.
    2. Повторяет выбор символов `length` раз.
    3. Объединяет выбранные символы в строку.

    ASCII flowchart:
    length -> Generate random hex string
      |  -> Choose from "abcdef" and digits
      |  -> Repeat length times
      |  -> Join characters into string
      |  -> Return random hex string

    Примеры:
        >>> get_random_hex(5)
        'a4b2f'
    """
    ...
```

### `filter_none`

```python
def filter_none(**kwargs) -> dict:
    """
    Фильтрует словарь, удаляя элементы со значением `None`.

    Args:
        **kwargs: Произвольные именованные аргументы.

    Returns:
        dict: Отфильтрованный словарь.

    Как работает функция:
    1. Создает новый словарь.
    2. Итерируется по переданным аргументам.
    3. Если значение аргумента не равно `None`, добавляет ключ и значение в новый словарь.
    4. Возвращает новый словарь.

    ASCII flowchart:
    kwargs -> Create new dict
      |  -> Iterate through kwargs
      |     | -> value is not None?
      |     |    | Yes: Add key-value to new dict
      |  -> Return new dict

    Примеры:
        >>> filter_none(a=1, b=None, c=2)
        {'a': 1, 'c': 2}
    """
    ...
```

### `async_concat_chunks`

```python
async def async_concat_chunks(chunks: AsyncIterator) -> str:
    """
    Асинхронно объединяет чанки (асинхронный итератор) в строку.

    Args:
        chunks (AsyncIterator): Асинхронный итератор чанков.

    Returns:
        str: Объединенная строка.

    Как работает функция:
    1. Асинхронно итерируется по чанкам.
    2. Использует `concat_chunks` для объединения чанков в строку.

    ASCII flowchart:
    chunks -> Async iterate through chunks
      |  -> Use concat_chunks to join into string
      |  -> Return joined string

    Примеры:
        >>> import asyncio
        >>> async def generate_chunks():
        ...     yield "hello"
        ...     yield "world"
        >>> asyncio.run(async_concat_chunks(generate_chunks()))
        'helloworld'
    """
    ...
```

### `concat_chunks`

```python
def concat_chunks(chunks: Iterator) -> str:
    """
    Объединяет чанки (итератор) в строку.

    Args:
        chunks (Iterator): Итератор чанков.

    Returns:
        str: Объединенная строка.

    Как работает функция:
    1. Итерируется по чанкам.
    2. Преобразует каждый чанк в строку.
    3. Исключает чанки, которые равны `None` или являются экземпляром исключения.
    4. Объединяет чанки в строку.

    ASCII flowchart:
    chunks -> Iterate through chunks
      |  -> Convert each chunk to string
      |  -> Exclude None or Exception chunks
      |  -> Join chunks into string
      |  -> Return joined string

    Примеры:
        >>> concat_chunks(["hello", "world"])
        'helloworld'
    """
    ...
```

### `format_cookies`

```python
def format_cookies(cookies: Cookies) -> str:
    """
    Форматирует словарь куки в строку для отправки в HTTP-запросе.

    Args:
        cookies (Cookies): Словарь куки.

    Returns:
        str: Строка, содержащая отформатированные куки.

    Как работает функция:
    1. Итерируется по элементам словаря куки.
    2. Форматирует каждую пару ключ-значение в строку "key=value".
    3. Объединяет отформатированные строки куки в одну строку, разделенную "; ".

    ASCII flowchart:
    cookies -> Iterate through cookie items
      |  -> Format each key-value pair as "key=value"
      |  -> Join formatted cookie strings with "; "
      |  -> Return formatted string

    Примеры:
        >>> cookies = {"name": "value", "name2": "value2"}
        >>> format_cookies(cookies)
        'name=value; name2=value2'
    """
    ...