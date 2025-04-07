# Модуль интеграционных тестов для gpt4free
## Обзор

Модуль содержит интеграционные тесты для проверки взаимодействия с различными поставщиками (providers) в библиотеке `gpt4free`. Он использует модуль `unittest` для определения тестовых случаев и проверяет успешность интеграции с поставщиками Copilot и DDG.

## Подробнее

Этот модуль важен для проверки корректности работы `gpt4free` с различными API, предоставляющими доступ к моделям генерации текста. Интеграционные тесты гарантируют, что взаимодействие с внешними сервисами работает ожидаемым образом, и позволяют выявлять проблемы совместимости или изменения в API поставщиков.

## Содержание

- [Классы](#Классы)
    - [TestProviderIntegration](#TestProviderIntegration)
    - [TestChatCompletionAsync](#TestChatCompletionAsync)
- [Переменные](#Переменные)
    - [DEFAULT_MESSAGES](#DEFAULT_MESSAGES)

## Переменные

### `DEFAULT_MESSAGES`
```python
DEFAULT_MESSAGES = [{"role": "system", "content": 'Response in json, Example: {"success": false}'},
                    {"role": "user", "content": "Say success true in json"}]
```
Содержит список сообщений по умолчанию, используемых в тестах для запроса ответа в формате JSON с полем "success".

## Классы

### `TestProviderIntegration`

**Описание**:
Класс `TestProviderIntegration` содержит интеграционные тесты для синхронного взаимодействия с поставщиками Copilot и DDG.

**Наследует**:
`unittest.TestCase`

**Методы**:

- `test_bing()`: Проверяет интеграцию с поставщиком Copilot.
- `test_openai()`: Проверяет интеграцию с поставщиком DDG.

#### `test_bing`

```python
def test_bing(self):
    """
    Тестирует интеграцию с поставщиком Copilot.

    Args:
        self (TestProviderIntegration): Экземпляр класса TestProviderIntegration.

    Raises:
        AssertionError: Если ответ от поставщика не соответствует ожидаемому формату.

    Как работает функция:
    1. Создает экземпляр клиента с поставщиком Copilot.
    2. Выполняет запрос к API для генерации текста в формате JSON.
    3. Проверяет, что полученный ответ является экземпляром класса ChatCompletion.
    4. Проверяет, что ответ содержит поле "success" в JSON.

    ASCII flowchart:
    Создание клиента --> Запрос к API --> Проверка типа ответа --> Проверка наличия "success"

    Примеры:
        >>> test = TestProviderIntegration()
        >>> test.test_bing()
    """
    ...
```

#### `test_openai`

```python
def test_openai(self):
    """
    Тестирует интеграцию с поставщиком DDG (DuckDuckGo).

    Args:
        self (TestProviderIntegration): Экземпляр класса TestProviderIntegration.

    Raises:
        AssertionError: Если ответ от поставщика не соответствует ожидаемому формату.

    Как работает функция:
    1. Создает экземпляр клиента с поставщиком DDG.
    2. Выполняет запрос к API для генерации текста в формате JSON.
    3. Проверяет, что полученный ответ является экземпляром класса ChatCompletion.
    4. Проверяет, что ответ содержит поле "success" в JSON.

    ASCII flowchart:
    Создание клиента --> Запрос к API --> Проверка типа ответа --> Проверка наличия "success"

    Примеры:
        >>> test = TestProviderIntegration()
        >>> test.test_openai()
    """
    ...
```

### `TestChatCompletionAsync`

**Описание**:
Класс `TestChatCompletionAsync` содержит интеграционные тесты для асинхронного взаимодействия с поставщиками Copilot и DDG.

**Наследует**:
`unittest.IsolatedAsyncioTestCase`

**Методы**:

- `test_bing()`: Проверяет асинхронную интеграцию с поставщиком Copilot.
- `test_openai()`: Проверяет асинхронную интеграцию с поставщиком DDG.

#### `test_bing`

```python
async def test_bing(self):
    """
    Асинхронно тестирует интеграцию с поставщиком Copilot.

    Args:
        self (TestChatCompletionAsync): Экземпляр класса TestChatCompletionAsync.

    Raises:
        AssertionError: Если ответ от поставщика не соответствует ожидаемому формату.

    Как работает функция:
    1. Создает экземпляр асинхронного клиента с поставщиком Copilot.
    2. Выполняет асинхронный запрос к API для генерации текста в формате JSON.
    3. Проверяет, что полученный ответ является экземпляром класса ChatCompletion.
    4. Проверяет, что ответ содержит поле "success" в JSON.

    ASCII flowchart:
    Создание клиента --> Асинхронный запрос к API --> Проверка типа ответа --> Проверка наличия "success"

    Примеры:
        >>> import asyncio
        >>> test = TestChatCompletionAsync()
        >>> asyncio.run(test.test_bing())
    """
    ...
```

#### `test_openai`

```python
async def test_openai(self):
    """
    Асинхронно тестирует интеграцию с поставщиком DDG (DuckDuckGo).

    Args:
        self (TestChatCompletionAsync): Экземпляр класса TestChatCompletionAsync.

    Raises:
        AssertionError: Если ответ от поставщика не соответствует ожидаемому формату.

    Как работает функция:
    1. Создает экземпляр асинхронного клиента с поставщиком DDG.
    2. Выполняет асинхронный запрос к API для генерации текста в формате JSON.
    3. Проверяет, что полученный ответ является экземпляром класса ChatCompletion.
    4. Проверяет, что ответ содержит поле "success" в JSON.

    ASCII flowchart:
    Создание клиента --> Асинхронный запрос к API --> Проверка типа ответа --> Проверка наличия "success"

    Примеры:
        >>> import asyncio
        >>> test = TestChatCompletionAsync()
        >>> asyncio.run(test.test_openai())
    """
    ...
```