# Модуль для тестирования асинхронного ChatCompletion с использованием unittest и asyncio
=========================================================================================

Модуль содержит набор тестов, проверяющих функциональность асинхронного создания чат-завершений (ChatCompletion) с использованием различных мок-провайдеров. Он также проверяет обработку исключений, связанных с `nest_asyncio`.

## Обзор

Этот модуль предназначен для тестирования асинхронного функционала, связанного с созданием чат-завершений, используя библиотеку `g4f`. В частности, он проверяет корректность работы `ChatCompletion.create` и `ChatCompletion.create_async` с различными типами провайдеров (синхронными, асинхронными и генераторами). Также модуль проверяет обработку ошибок, возникающих при отсутствии установленной библиотеки `nest_asyncio`.

## Подробней

Файл содержит три основных класса для тестирования:

1.  `TestChatCompletion`: Класс для тестирования синхронного API `ChatCompletion` в асинхронном контексте.
2.  `TestChatCompletionAsync`: Класс для тестирования асинхронного API `ChatCompletion` с использованием `unittest.IsolatedAsyncioTestCase`.
3.  `TestChatCompletionNestAsync`: Класс для тестирования вложенных асинхронных вызовов `ChatCompletion` с использованием `nest_asyncio`.

## Классы

### `TestChatCompletion`

**Описание**: Класс для тестирования синхронного API `ChatCompletion` в асинхронном контексте.

**Принцип работы**:
Класс содержит тесты для проверки создания чат-завершений с использованием `ChatCompletion.create` и различных мок-провайдеров. Он также проверяет генерацию исключений, когда `nest_asyncio` не установлен.

**Методы**:

-   `run_exception`: Асинхронный метод, который вызывает `ChatCompletion.create` с мок-провайдером для генерации исключения.
-   `test_exception`: Тестирует генерацию исключения `g4f.errors.NestAsyncioError`, когда `nest_asyncio` не установлен.
-   `test_create`: Тестирует создание чат-завершения с использованием асинхронного мок-провайдера и проверяет результат.
-   `test_create_generator`: Тестирует создание чат-завершения с использованием асинхронного мок-провайдера-генератора и проверяет результат.
-   `test_await_callback`: Тестирует асинхронный вызов `client.chat.completions.create` и проверяет, что возвращаемое значение соответствует ожидаемому.

#### `run_exception`

```python
async def run_exception(self):
    """
    Асинхронно вызывает ChatCompletion.create с AsyncProviderMock для генерации исключения.

    Args:
        self (TestChatCompletion): Экземпляр класса TestChatCompletion.

    Returns:
        Any: Результат ChatCompletion.create.

    Raises:
        None.
    """
    ...
```

**Как работает функция**:

1.  Вызывает асинхронную функцию `ChatCompletion.create` с использованием модели по умолчанию, предопределенных сообщений и мок-провайдера `AsyncProviderMock`.
2.  Возвращает результат вызова `ChatCompletion.create`.

#### `test_exception`

```python
def test_exception(self):
    """
    Проверяет генерацию исключения NestAsyncioError при отсутствии установленной библиотеки nest_asyncio.

    Args:
        self (TestChatCompletion): Экземпляр класса TestChatCompletion.

    Returns:
        None.

    Raises:
        None.
    """
    ...
```

**Как работает функция**:

1.  Проверяет, установлена ли библиотека `nest_asyncio`. Если установлена, то тест пропускается.
2.  Вызывает `asyncio.run` с функцией `self.run_exception()`. Ожидается, что будет выброшено исключение `g4f.errors.NestAsyncioError`.

#### `test_create`

```python
def test_create(self):
    """
    Тестирует создание чат-завершения с использованием асинхронного мок-провайдера.

    Args:
        self (TestChatCompletion): Экземпляр класса TestChatCompletion.

    Returns:
        None.

    Raises:
        None.
    """
    ...
```

**Как работает функция**:

1.  Вызывает `ChatCompletion.create` с использованием модели по умолчанию, предопределенных сообщений и мок-провайдера `AsyncProviderMock`.
2.  Проверяет, что результат равен "Mock".

#### `test_create_generator`

```python
def test_create_generator(self):
    """
    Тестирует создание чат-завершения с использованием асинхронного мок-провайдера-генератора.

    Args:
        self (TestChatCompletion): Экземпляр класса TestChatCompletion.

    Returns:
        None.

    Raises:
        None.
    """
    ...
```

**Как работает функция**:

1.  Вызывает `ChatCompletion.create` с использованием модели по умолчанию, предопределенных сообщений и мок-провайдера `AsyncGeneratorProviderMock`.
2.  Проверяет, что результат равен "Mock".

#### `test_await_callback`

```python
def test_await_callback(self):
    """
    Тестирует асинхронный вызов client.chat.completions.create и проверяет, что возвращаемое значение соответствует ожидаемому.

    Args:
        self (TestChatCompletion): Экземпляр класса TestChatCompletion.

    Returns:
        None.

    Raises:
        None.
    """
    ...
```

**Как работает функция**:

1.  Создает экземпляр класса `Client` с использованием мок-провайдера `AsyncGeneratorProviderMock`.
2.  Вызывает метод `client.chat.completions.create` с предопределенными сообщениями, пустой строкой и `max_tokens=0`.
3.  Проверяет, что содержимое первого элемента в списке `response.choices` равно "Mock".

### `TestChatCompletionAsync`

**Описание**: Класс для тестирования асинхронного API `ChatCompletion` с использованием `unittest.IsolatedAsyncioTestCase`.

**Принцип работы**:
Этот класс использует `unittest.IsolatedAsyncioTestCase` для тестирования асинхронных вызовов `ChatCompletion.create_async` с различными типами мок-провайдеров.

**Методы**:

-   `test_base`: Тестирует базовый асинхронный вызов `ChatCompletion.create_async` с синхронным мок-провайдером.
-   `test_async`: Тестирует асинхронный вызов `ChatCompletion.create_async` с асинхронным мок-провайдером.
-   `test_create_generator`: Тестирует асинхронный вызов `ChatCompletion.create_async` с асинхронным мок-провайдером-генератором.

#### `test_base`

```python
async def test_base(self):
    """
    Тестирует базовый асинхронный вызов ChatCompletion.create_async с синхронным мок-провайдером.

    Args:
        self (TestChatCompletionAsync): Экземпляр класса TestChatCompletionAsync.

    Returns:
        None.

    Raises:
        None.
    """
    ...
```

**Как работает функция**:

1.  Вызывает асинхронную функцию `ChatCompletion.create_async` с использованием модели по умолчанию, предопределенных сообщений и мок-провайдера `ProviderMock`.
2.  Проверяет, что результат равен "Mock".

#### `test_async`

```python
async def test_async(self):
    """
    Тестирует асинхронный вызов ChatCompletion.create_async с асинхронным мок-провайдером.

    Args:
        self (TestChatCompletionAsync): Экземпляр класса TestChatCompletionAsync.

    Returns:
        None.

    Raises:
        None.
    """
    ...
```

**Как работает функция**:

1.  Вызывает асинхронную функцию `ChatCompletion.create_async` с использованием модели по умолчанию, предопределенных сообщений и мок-провайдера `AsyncProviderMock`.
2.  Проверяет, что результат равен "Mock".

#### `test_create_generator`

```python
async def test_create_generator(self):
    """
    Тестирует асинхронный вызов ChatCompletion.create_async с асинхронным мок-провайдером-генератором.

    Args:
        self (TestChatCompletionAsync): Экземпляр класса TestChatCompletionAsync.

    Returns:
        None.

    Raises:
        None.
    """
    ...
```

**Как работает функция**:

1.  Вызывает асинхронную функцию `ChatCompletion.create_async` с использованием модели по умолчанию, предопределенных сообщений и мок-провайдера `AsyncGeneratorProviderMock`.
2.  Проверяет, что результат равен "Mock".

### `TestChatCompletionNestAsync`

**Описание**: Класс для тестирования вложенных асинхронных вызовов `ChatCompletion` с использованием `nest_asyncio`.

**Принцип работы**:
Этот класс проверяет корректность работы `ChatCompletion.create` и `ChatCompletion.create_async` во вложенных асинхронных контекстах, когда применена библиотека `nest_asyncio`.

**Методы**:

-   `setUp`: Устанавливает окружение для тестов, проверяя наличие `nest_asyncio` и применяя его.
-   `test_create`: Тестирует асинхронный вызов `ChatCompletion.create_async` с синхронным мок-провайдером.
-   `_test_nested`: Тестирует вложенный вызов `ChatCompletion.create` с асинхронным мок-провайдером.
-   `_test_nested_generator`: Тестирует вложенный вызов `ChatCompletion.create` с асинхронным мок-провайдером-генератором.

#### `setUp`

```python
def setUp(self) -> None:
    """
    Устанавливает окружение для тестов, проверяя наличие nest_asyncio и применяя его.

    Args:
        self (TestChatCompletionNestAsync): Экземпляр класса TestChatCompletionNestAsync.

    Returns:
        None.

    Raises:
        unittest.SkipTest: Если nest_asyncio не установлен.
    """
    ...
```

**Как работает функция**:

1.  Проверяет, установлена ли библиотека `nest_asyncio`. Если не установлена, то тест пропускается.
2.  Применяет `nest_asyncio.apply()` для поддержки вложенных асинхронных вызовов.

#### `test_create`

```python
async def test_create(self):
    """
    Тестирует асинхронный вызов ChatCompletion.create_async с синхронным мок-провайдером.

    Args:
        self (TestChatCompletionNestAsync): Экземпляр класса TestChatCompletionNestAsync.

    Returns:
        None.

    Raises:
        None.
    """
    ...
```

**Как работает функция**:

1.  Вызывает асинхронную функцию `ChatCompletion.create_async` с использованием модели по умолчанию, предопределенных сообщений и мок-провайдера `ProviderMock`.
2.  Проверяет, что результат равен "Mock".

#### `_test_nested`

```python
async def _test_nested(self):
    """
    Тестирует вложенный вызов ChatCompletion.create с асинхронным мок-провайдером.

    Args:
        self (TestChatCompletionNestAsync): Экземпляр класса TestChatCompletionNestAsync.

    Returns:
        None.

    Raises:
        None.
    """
    ...
```

**Как работает функция**:

1.  Вызывает функцию `ChatCompletion.create` с использованием модели по умолчанию, предопределенных сообщений и мок-провайдера `AsyncProviderMock`.
2.  Проверяет, что результат равен "Mock".

#### `_test_nested_generator`

```python
async def _test_nested_generator(self):
    """
    Тестирует вложенный вызов ChatCompletion.create с асинхронным мок-провайдером-генератором.

    Args:
        self (TestChatCompletionNestAsync): Экземпляр класса TestChatCompletionNestAsync.

    Returns:
        None.

    Raises:
        None.
    """
    ...
```

**Как работает функция**:

1.  Вызывает функцию `ChatCompletion.create` с использованием модели по умолчанию, предопределенных сообщений и мок-провайдера `AsyncGeneratorProviderMock`.
2.  Проверяет, что результат равен "Mock".

## Функции

В данном модуле нет отдельных функций, не принадлежащих классам.