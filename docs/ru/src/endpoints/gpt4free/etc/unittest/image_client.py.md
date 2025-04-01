# Модуль тестирования image_client

## Обзор

Модуль содержит юнит-тесты для проверки функциональности асинхронного клиента, генерирующего изображения, с использованием различных мок-провайдеров. Он проверяет правильность обработки различных сценариев, включая пропуск недоступных провайдеров, получение только одного результата и обработку исключений.

## Подробнее

Этот модуль является частью набора тестов для библиотеки `g4f`, которая позволяет взаимодействовать с различными провайдерами изображений. Он использует `unittest` и `asyncio` для написания и запуска асинхронных тестов. Модуль проверяет, что клиент корректно обрабатывает различные ситуации, такие как недоступные провайдеры, провайдеры, возвращающие `None`, и провайдеры, выбрасывающие исключения.

## Классы

### `TestIterListProvider`

**Описание**:
Класс `TestIterListProvider` содержит набор асинхронных тестов для проверки функциональности `IterListProvider`.

**Принцип работы**:
Класс наследуется от `unittest.IsolatedAsyncioTestCase` и использует асинхронные методы для выполнения тестов. Каждый метод тестирует определенный сценарий взаимодействия с провайдерами изображений через асинхронный клиент `AsyncClient`. В тестах используются мок-провайдеры для имитации различных ситуаций, таких как недоступность провайдера, возврат `None` или выброс исключения.

**Методы**:

- `test_skip_provider`: Тестирует сценарий, когда один из провайдеров в списке недоступен и должен быть пропущен.
- `test_only_one_result`: Тестирует сценарий, когда несколько провайдеров возвращают результат, но должен быть использован только один.
- `test_skip_none`: Тестирует сценарий, когда один из провайдеров возвращает `None` и должен быть пропущен.
- `test_raise_exception`: Тестирует сценарий, когда провайдер выбрасывает исключение, и проверяет, что исключение правильно обрабатывается.

## Функции

### `run_exception`

```python
async def run_exception():
    """Внутренняя функция для запуска теста исключения.
    
    Функция создает асинхронный клиент с использованием `IterListProvider`, который содержит `YieldNoneProviderMock` и `AsyncRaiseExceptionProviderMock`. Затем она пытается сгенерировать изображение и ожидает, что будет выброшено исключение `RuntimeError`.
    
    Args:
        None
    
    Returns:
        None
    
    Raises:
        RuntimeError: Если не было выброшено исключение при генерации изображения.
    """
```

**Как работает функция**:

1. **Создание асинхронного клиента**:
   - Создается экземпляр `AsyncClient` с использованием `IterListProvider`.
   - Провайдеру передается список, содержащий `YieldNoneProviderMock` (который возвращает `None`) и `AsyncRaiseExceptionProviderMock` (который выбрасывает исключение).

2. **Генерация изображения**:
   - Вызывается метод `client.images.generate` с параметрами `"Hello"` и `""`.
   - Ожидается, что `AsyncRaiseExceptionProviderMock` выбросит исключение `RuntimeError`.

**Примеры**:
```python
import asyncio
import unittest

from g4f.client import AsyncClient
from g4f.providers.retry_provider import IterListProvider
from .mocks import YieldNoneProviderMock, AsyncRaiseExceptionProviderMock

class TestIterListProvider(unittest.IsolatedAsyncioTestCase):
    def test_raise_exception(self):
        async def run_exception():
            client = AsyncClient(image_provider=IterListProvider([YieldNoneProviderMock, AsyncRaiseExceptionProviderMock], False))
            await client.images.generate("Hello", "")
        self.assertRaises(RuntimeError, asyncio.run, run_exception())
```

### `TestIterListProvider.test_skip_provider`

```python
async def test_skip_provider(self):
    """Тестирует сценарий, когда один из провайдеров в списке недоступен и должен быть пропущен.

    Создает асинхронный клиент с использованием `IterListProvider`, который содержит `MissingAuthProviderMock` и `YieldImageResponseProviderMock`.
    Генерирует изображение и проверяет, что возвращенный ответ является экземпляром `ImagesResponse` и содержит ожидаемый URL.

    Args:
        self (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

    Returns:
        None

    Raises:
        AssertionError: Если возвращенный ответ не является экземпляром `ImagesResponse` или URL не соответствует ожидаемому.
    """
```

**Как работает функция**:

1.  **Создание асинхронного клиента**:

    *   Создается экземпляр `AsyncClient` с использованием `IterListProvider`.
    *   Провайдеру передается список, содержащий `MissingAuthProviderMock` (который имитирует недоступного провайдера) и `YieldImageResponseProviderMock` (который возвращает изображение).

2.  **Генерация изображения**:

    *   Вызывается метод `client.images.generate` с параметрами `"Hello"`, `""` и `response_format="orginal"`.
    *   Метод возвращает объект `ImagesResponse`.

3.  **Проверка результата**:

    *   Проверяется, что возвращенный ответ является экземпляром `ImagesResponse`.
    *   Проверяется, что URL первого изображения в ответе соответствует `"Hello"`.

**Примеры**:

```python
import unittest
import asyncio
from g4f.client import AsyncClient, ImagesResponse
from g4f.providers.retry_provider import IterListProvider
from .mocks import MissingAuthProviderMock, YieldImageResponseProviderMock

class TestIterListProvider(unittest.IsolatedAsyncioTestCase):
    async def test_skip_provider(self):
        client = AsyncClient(image_provider=IterListProvider([MissingAuthProviderMock, YieldImageResponseProviderMock], False))
        response = await client.images.generate("Hello", "", response_format="orginal")
        self.assertIsInstance(response, ImagesResponse)
        self.assertEqual("Hello", response.data[0].url)
```

### `TestIterListProvider.test_only_one_result`

```python
async def test_only_one_result(self):
    """Тестирует сценарий, когда несколько провайдеров возвращают результат, но должен быть использован только один.

    Создает асинхронный клиент с использованием `IterListProvider`, который содержит два экземпляра `YieldImageResponseProviderMock`.
    Генерирует изображение и проверяет, что возвращенный ответ является экземпляром `ImagesResponse` и содержит ожидаемый URL.

    Args:
        self (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

    Returns:
        None

    Raises:
        AssertionError: Если возвращенный ответ не является экземпляром `ImagesResponse` или URL не соответствует ожидаемому.
    """
```

**Как работает функция**:

1.  **Создание асинхронного клиента**:

    *   Создается экземпляр `AsyncClient` с использованием `IterListProvider`.
    *   Провайдеру передается список, содержащий два экземпляра `YieldImageResponseProviderMock` (которые возвращают изображение).

2.  **Генерация изображения**:

    *   Вызывается метод `client.images.generate` с параметрами `"Hello"`, `""` и `response_format="orginal"`.
    *   Метод возвращает объект `ImagesResponse`.

3.  **Проверка результата**:

    *   Проверяется, что возвращенный ответ является экземпляром `ImagesResponse`.
    *   Проверяется, что URL первого изображения в ответе соответствует `"Hello"`.

**Примеры**:

```python
import unittest
import asyncio
from g4f.client import AsyncClient, ImagesResponse
from g4f.providers.retry_provider import IterListProvider
from .mocks import YieldImageResponseProviderMock

class TestIterListProvider(unittest.IsolatedAsyncioTestCase):
    async def test_only_one_result(self):
        client = AsyncClient(image_provider=IterListProvider([YieldImageResponseProviderMock, YieldImageResponseProviderMock], False))
        response = await client.images.generate("Hello", "", response_format="orginal")
        self.assertIsInstance(response, ImagesResponse)
        self.assertEqual("Hello", response.data[0].url)
```

### `TestIterListProvider.test_skip_none`

```python
async def test_skip_none(self):
    """Тестирует сценарий, когда один из провайдеров возвращает `None` и должен быть пропущен.

    Создает асинхронный клиент с использованием `IterListProvider`, который содержит `YieldNoneProviderMock` и `YieldImageResponseProviderMock`.
    Генерирует изображение и проверяет, что возвращенный ответ является экземпляром `ImagesResponse` и содержит ожидаемый URL.

    Args:
        self (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

    Returns:
        None

    Raises:
        AssertionError: Если возвращенный ответ не является экземпляром `ImagesResponse` или URL не соответствует ожидаемому.
    """
```

**Как работает функция**:

1.  **Создание асинхронного клиента**:

    *   Создается экземпляр `AsyncClient` с использованием `IterListProvider`.
    *   Провайдеру передается список, содержащий `YieldNoneProviderMock` (который возвращает `None`) и `YieldImageResponseProviderMock` (который возвращает изображение).

2.  **Генерация изображения**:

    *   Вызывается метод `client.images.generate` с параметрами `"Hello"`, `""` и `response_format="orginal"`.
    *   Метод возвращает объект `ImagesResponse`.

3.  **Проверка результата**:

    *   Проверяется, что возвращенный ответ является экземпляром `ImagesResponse`.
    *   Проверяется, что URL первого изображения в ответе соответствует `"Hello"`.

**Примеры**:

```python
import unittest
import asyncio
from g4f.client import AsyncClient, ImagesResponse
from g4f.providers.retry_provider import IterListProvider
from .mocks import YieldNoneProviderMock, YieldImageResponseProviderMock

class TestIterListProvider(unittest.IsolatedAsyncioTestCase):
    async def test_skip_none(self):
        client = AsyncClient(image_provider=IterListProvider([YieldNoneProviderMock, YieldImageResponseProviderMock], False))
        response = await client.images.generate("Hello", "", response_format="orginal")
        self.assertIsInstance(response, ImagesResponse)
        self.assertEqual("Hello", response.data[0].url)
```

### `TestIterListProvider.test_raise_exception`

```python
def test_raise_exception(self):
    """Тестирует сценарий, когда провайдер выбрасывает исключение, и проверяет, что исключение правильно обрабатывается.

    Определяет внутреннюю асинхронную функцию `run_exception`, которая создает асинхронный клиент с использованием `IterListProvider`, содержащий `YieldNoneProviderMock` и `AsyncRaiseExceptionProviderMock`.
    Вызывает `run_exception` через `asyncio.run` и проверяет, что было выброшено исключение `RuntimeError`.

    Args:
        self (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

    Returns:
        None

    Raises:
        AssertionError: Если не было выброшено исключение `RuntimeError`.
    """
```

**Как работает функция**:

1.  **Определение внутренней функции `run_exception`**:

    *   Определяется асинхронная функция `run_exception`, которая создает асинхронный клиент с использованием `IterListProvider`.
    *   Провайдеру передается список, содержащий `YieldNoneProviderMock` (который возвращает `None`) и `AsyncRaiseExceptionProviderMock` (который выбрасывает исключение).
    *   Внутри `run_exception` вызывается метод `client.images.generate` с параметрами `"Hello"` и `""`.

2.  **Запуск и проверка исключения**:

    *   Функция `run_exception` запускается с использованием `asyncio.run`.
    *   Метод `self.assertRaises` проверяет, что при выполнении `asyncio.run(run_exception())` будет выброшено исключение `RuntimeError`.

**Примеры**:

```python
import unittest
import asyncio
from g4f.client import AsyncClient
from g4f.providers.retry_provider import IterListProvider
from .mocks import YieldNoneProviderMock, AsyncRaiseExceptionProviderMock

class TestIterListProvider(unittest.IsolatedAsyncioTestCase):
    def test_raise_exception(self):
        async def run_exception():
            client = AsyncClient(image_provider=IterListProvider([YieldNoneProviderMock, AsyncRaiseExceptionProviderMock], False))
            await client.images.generate("Hello", "")
        self.assertRaises(RuntimeError, asyncio.run, run_exception())