# Модуль для тестирования веб-поиска

## Обзор

Модуль содержит юнит-тесты для проверки функциональности веб-поиска, интегрированного в проект `hypotez`. Он использует `unittest` для тестирования асинхронного клиента с мокированным провайдером (`YieldProviderMock`). В частности, проверяется корректность работы функции `search_tool` с различными параметрами.

## Подробнее

Этот модуль предназначен для автоматизированной проверки интеграции веб-поиска DuckDuckGo с асинхронным клиентом `AsyncClient`. Он выполняет несколько тестов, имитируя вызовы `search_tool` с разными наборами аргументов и проверяя, что возвращаемые ответы содержат ожидаемый текст. Модуль также обрабатывает возможные исключения, возникающие при использовании DuckDuckGoSearch.

## Классы

### `TestIterListProvider`

**Описание**: Класс, содержащий асинхронные юнит-тесты для проверки функциональности веб-поиска.

**Наследует**:
- `unittest.IsolatedAsyncioTestCase`

**Методы**:

- `setUp`: Подготавливает тестовую среду, проверяя наличие необходимых зависимостей.
- `test_search`: Тестирует функцию `search_tool` с полным набором параметров, включая `query`, `max_results`, `max_words`, `backend`, `add_text`, `timeout`, `region` и `instructions`.
- `test_search2`: Тестирует функцию `search_tool` с минимальным набором параметров, включающим только `query`.
- `test_search3`: Тестирует функцию `search_tool`, передавая параметры в формате JSON.

## Функции

### `setUp`

```python
def setUp(self) -> None:
    """
    Подготавливает тестовую среду, проверяя наличие необходимых зависимостей.

    Args:
        self (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

    Returns:
        None

    Raises:
        unittest.SkipTest: Если не установлены необходимые зависимости (`web search requirements`).
    """
    ...
```

**Назначение**:
Подготовка тестовой среды перед выполнением каждого теста. Проверяет, установлены ли необходимые зависимости (в данном случае, библиотеки для веб-поиска). Если зависимости не установлены, тест пропускается.

**Как работает функция**:

1.  Проверяется глобальная переменная `has_requirements`. Если она `False`, это означает, что необходимые библиотеки не установлены.
2.  Если зависимости отсутствуют, вызывается `self.skipTest` с сообщением о причине пропуска теста.

**Примеры**:

```python
class TestIterListProvider(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        if not has_requirements:
            self.skipTest('web search requirements not passed')
```

### `test_search`

```python
async def test_search(self):
    """
    Тестирует функцию `search_tool` с полным набором параметров, включая `query`, `max_results`, `max_words`, `backend`, `add_text`, `timeout`, `region` и `instructions`.

    Args:
        self (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

    Returns:
        None

    Raises:
        unittest.SkipTest: Если возникает исключение `DuckDuckGoSearchException`.
    """
    ...
```

**Назначение**:
Проверка корректной работы функции `search_tool` при передаче всех возможных параметров. Это включает в себя параметры запроса, максимальное количество результатов, максимальное количество слов, бэкенд, добавление текста, таймаут, регион и инструкции.

**Как работает функция**:

1.  Создается экземпляр `AsyncClient` с мокированным провайдером `YieldProviderMock`.
2.  Определяется структура `tool_calls`, содержащая параметры для `search_tool`.
3.  Вызывается метод `client.chat.completions.create` с передачей структуры `tool_calls`.
4.  Проверяется, что ответ содержит ожидаемый текст "Using the provided web search results".
5.  В случае возникновения исключения `DuckDuckGoSearchException`, тест пропускается.

**Примеры**:

```python
async def test_search(self):
    client = AsyncClient(provider=YieldProviderMock)
    tool_calls = [
        {
            "function": {
                "arguments": {
                    "query": "search query",
                    "max_results": 5,
                    "max_words": 500,
                    "backend": "html",
                    "add_text": True,
                    "timeout": 5,
                    "region": "wt-wt",
                    "instructions": "Using the provided web search results, to write a comprehensive reply to the user request.\n"
                                    "Make sure to add the sources of cites using [[Number]](Url) notation after the reference. Example: [[0]](http://google.com)",
                },
                "name": "search_tool"
            },
            "type": "function"
        }
    ]
    try:
        response = await client.chat.completions.create([{"content": "", "role": "user"}], "", tool_calls=tool_calls)
        self.assertIn("Using the provided web search results", response.choices[0].message.content)
    except DuckDuckGoSearchException as e:
        self.skipTest(f'DuckDuckGoSearchException: {e}')
```

### `test_search2`

```python
async def test_search2(self):
    """
    Тестирует функцию `search_tool` с минимальным набором параметров, включающим только `query`.

    Args:
        self (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

    Returns:
        None

    Raises:
        unittest.SkipTest: Если возникает исключение `DuckDuckGoSearchException`.
    """
    ...
```

**Назначение**:
Проверка работы `search_tool` при передаче минимального набора параметров, а именно только параметра `query`. Это позволяет убедиться, что функция корректно обрабатывает случай, когда остальные параметры не указаны.

**Как работает функция**:

1.  Создается экземпляр `AsyncClient` с мокированным провайдером `YieldProviderMock`.
2.  Определяется структура `tool_calls`, содержащая только параметр `query` для `search_tool`.
3.  Вызывается метод `client.chat.completions.create` с передачей структуры `tool_calls`.
4.  Проверяется, что ответ содержит ожидаемый текст "Using the provided web search results".
5.  В случае возникновения исключения `DuckDuckGoSearchException`, тест пропускается.

**Примеры**:

```python
async def test_search2(self):
    client = AsyncClient(provider=YieldProviderMock)
    tool_calls = [
        {
            "function": {
                "arguments": {
                    "query": "search query",
                },
                "name": "search_tool"
            },
            "type": "function"
        }
    ]
    try:
        response = await client.chat.completions.create([{"content": "", "role": "user"}], "", tool_calls=tool_calls)
        self.assertIn("Using the provided web search results", response.choices[0].message.content)
    except DuckDuckGoSearchException as e:
        self.skipTest(f'DuckDuckGoSearchException: {e}')
```

### `test_search3`

```python
async def test_search3(self):
    """
    Тестирует функцию `search_tool`, передавая параметры в формате JSON.

    Args:
        self (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

    Returns:
        None

    Raises:
        unittest.SkipTest: Если возникает исключение `DuckDuckGoSearchException`.
    """
    ...
```

**Назначение**:
Проверка работы `search_tool` при передаче параметров в формате JSON. Это необходимо для проверки совместимости с различными способами передачи аргументов.

**Как работает функция**:

1.  Создается экземпляр `AsyncClient` с мокированным провайдером `YieldProviderMock`.
2.  Определяется структура `tool_calls`, содержащая параметры для `search_tool`, сериализованные в JSON.
3.  Вызывается метод `client.chat.completions.create` с передачей структуры `tool_calls`.
4.  Проверяется, что ответ содержит ожидаемый текст "Using the provided web search results".
5.  В случае возникновения исключения `DuckDuckGoSearchException`, тест пропускается.

**Примеры**:

```python
async def test_search3(self):
    client = AsyncClient(provider=YieldProviderMock)
    tool_calls = [
        {
            "function": {
                "arguments": json.dumps({
                    "query": "search query",
                    "max_results": 5,
                    "max_words": 500,
                }),
                "name": "search_tool"
            },
            "type": "function"
        }
    ]
    try:
        response = await client.chat.completions.create([{"content": "", "role": "user"}], "", tool_calls=tool_calls)
        self.assertIn("Using the provided web search results", response.choices[0].message.content)
    except DuckDuckGoSearchException as e:
        self.skipTest(f'DuckDuckGoSearchException: {e}')