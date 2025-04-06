# Модуль тестирования веб-поиска

## Обзор

Модуль содержит юнит-тесты для проверки функциональности веб-поиска, используемого в проекте `hypotez`. Он использует библиотеку `duckduckgo_search` для выполнения поисковых запросов и `BeautifulSoup` для парсинга результатов. Тесты проверяют, что поисковый инструмент работает корректно и возвращает ожидаемые результаты.

## Подробней

Этот модуль предназначен для автоматизированного тестирования интеграции веб-поиска с AI-клиентом. Он проверяет, что при использовании различных конфигураций `tool_calls`, ответы AI-клиента содержат ожидаемые результаты веб-поиска. Модуль использует моки для имитации ответов провайдера, чтобы изолировать тесты от внешних зависимостей.
Расположение файла в проекте указывает на то, что это юнит-тесты для функциональности веб-поиска в контексте `gpt4free`.

## Классы

### `TestIterListProvider`

**Описание**: Класс `TestIterListProvider` содержит асинхронные тесты для проверки функциональности веб-поиска.

**Наследует**:
- `unittest.IsolatedAsyncioTestCase`: Этот класс является базовым классом для написания асинхронных юнит-тестов.

**Методы**:
- `setUp()`: Метод для подготовки к тестам. Проверяет, установлены ли необходимые зависимости для веб-поиска. Если зависимости не установлены, тест пропускается.
- `test_search()`: Тест для проверки базовой функциональности поиска с различными параметрами, такими как `max_results`, `max_words`, `backend`, `add_text`, `timeout`, `region` и `instructions`.
- `test_search2()`: Тест для проверки базовой функциональности поиска с минимальным набором параметров, а именно только с `query`.
- `test_search3()`: Тест для проверки функциональности поиска с параметрами, переданными в формате JSON.

## Функции

### `setUp`

```python
def setUp(self) -> None:
    """
    Метод подготовки к тестам. Проверяет наличие необходимых зависимостей для веб-поиска.
    Если зависимости не установлены, тест пропускается.
    """
    ...
```

**Назначение**: Метод `setUp` выполняется перед каждым тестом. Он проверяет, установлены ли необходимые библиотеки (`duckduckgo_search`, `BeautifulSoup`) для выполнения тестов веб-поиска. Если библиотеки не установлены, тест пропускается.

**Параметры**:
- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:
- `None`

**Как работает функция**:
1. Проверяет, установлены ли необходимые библиотеки `duckduckgo_search` и `BeautifulSoup`.
2. Если хотя бы одна из библиотек не установлена, тест пропускается с помощью `self.skipTest`.

**Примеры**:
```python
class TestIterListProvider(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        if not has_requirements:
            self.skipTest('web search requirements not passed')
```

### `test_search`

```python
async def test_search(self):
    """
    Тест для проверки базовой функциональности поиска с различными параметрами, такими как `max_results`, `max_words`, `backend`, `add_text`, `timeout`, `region` и `instructions`.
    """
    ...
```

**Назначение**: Метод `test_search` является асинхронным тестом, который проверяет базовую функциональность поиска с различными параметрами. Он создает `tool_calls` с параметрами для `search_tool`, выполняет поисковый запрос и проверяет, что ответ содержит ожидаемый текст.

**Параметры**:
- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `DuckDuckGoSearchException`: Если возникает ошибка при выполнении поискового запроса.

**Как работает функция**:

```
Создание клиента -> Определение tool_calls -> Выполнение поискового запроса -> Проверка результата
```

1. Создает экземпляр `AsyncClient` с моковым провайдером `YieldProviderMock`.
2. Определяет структуру `tool_calls` с различными параметрами для `search_tool`, такими как `query`, `max_results`, `max_words`, `backend`, `add_text`, `timeout`, `region` и `instructions`.
3. Выполняет поисковый запрос с помощью `client.chat.completions.create`.
4. Проверяет, что ответ содержит текст "Using the provided web search results".
5. Если возникает исключение `DuckDuckGoSearchException`, тест пропускается.

**Примеры**:
```python
    async def test_search(self):
        client = AsyncClient(provider=YieldProviderMock)
        tool_calls = [
            {
                "function": {
                    "arguments": {
                        "query": "search query", # content of last message: messages[-1]["content"]
                        "max_results": 5, # maximum number of search results
                        "max_words": 500, # maximum number of used words from search results for generating the response
                        "backend": "html", # or "lite", "api": change it to pypass rate limits
                        "add_text": True, # do scraping websites
                        "timeout": 5, # in seconds for scraping websites
                        "region": "wt-wt",
                        "instructions": "Using the provided web search results, to write a comprehensive reply to the user request.\n"\
                                        "Make sure to add the sources of cites using [[Number]](Url) notation after the reference. Example: [[0]](http://google.com)",
                    },\n                    "name": "search_tool"\n                },\n                "type": "function"\n            }\n        ]\n        try:\n            response = await client.chat.completions.create([{"content": "", "role": "user"}], "", tool_calls=tool_calls)
            self.assertIn("Using the provided web search results", response.choices[0].message.content)
        except DuckDuckGoSearchException as e:
            self.skipTest(f'DuckDuckGoSearchException: {e}')
```

### `test_search2`

```python
async def test_search2(self):
    """
    Тест для проверки базовой функциональности поиска с минимальным набором параметров, а именно только с `query`.
    """
    ...
```

**Назначение**: Метод `test_search2` является асинхронным тестом, который проверяет базовую функциональность поиска с минимальным набором параметров. Он создает `tool_calls` только с параметром `query` для `search_tool`, выполняет поисковый запрос и проверяет, что ответ содержит ожидаемый текст.

**Параметры**:
- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `DuckDuckGoSearchException`: Если возникает ошибка при выполнении поискового запроса.

**Как работает функция**:

```
Создание клиента -> Определение tool_calls -> Выполнение поискового запроса -> Проверка результата
```

1. Создает экземпляр `AsyncClient` с моковым провайдером `YieldProviderMock`.
2. Определяет структуру `tool_calls` только с параметром `query` для `search_tool`.
3. Выполняет поисковый запрос с помощью `client.chat.completions.create`.
4. Проверяет, что ответ содержит текст "Using the provided web search results".
5. Если возникает исключение `DuckDuckGoSearchException`, тест пропускается.

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
    Тест для проверки функциональности поиска с параметрами, переданными в формате JSON.
    """
    ...
```

**Назначение**: Метод `test_search3` является асинхронным тестом, который проверяет функциональность поиска с параметрами, переданными в формате JSON. Он создает `tool_calls` с параметрами для `search_tool`, закодированными в JSON, выполняет поисковый запрос и проверяет, что ответ содержит ожидаемый текст.

**Параметры**:
- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `DuckDuckGoSearchException`: Если возникает ошибка при выполнении поискового запроса.

**Как работает функция**:

```
Создание клиента -> Определение tool_calls -> Выполнение поискового запроса -> Проверка результата
```

1. Создает экземпляр `AsyncClient` с моковым провайдером `YieldProviderMock`.
2. Определяет структуру `tool_calls` с параметрами для `search_tool`, закодированными в JSON. Параметры включают `query`, `max_results` и `max_words`.
3. Выполняет поисковый запрос с помощью `client.chat.completions.create`.
4. Проверяет, что ответ содержит текст "Using the provided web search results".
5. Если возникает исключение `DuckDuckGoSearchException`, тест пропускается.

**Примеры**:
```python
    async def test_search3(self):
        client = AsyncClient(provider=YieldProviderMock)
        tool_calls = [
            {
                "function": {
                    "arguments": json.dumps({
                        "query": "search query", # content of last message: messages[-1]["content"]
                        "max_results": 5, # maximum number of search results
                        "max_words": 500, # maximum number of used words from search results for generating the response
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