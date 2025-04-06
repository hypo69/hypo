# Модуль для модульного тестирования image_client

## Обзор

Модуль содержит юнит-тесты для асинхронного клиента, работающего с image_provider. Основная цель - проверка корректности работы IterListProvider с различными моками (MissingAuthProviderMock, YieldImageResponseProviderMock, AsyncRaiseExceptionProviderMock, YieldNoneProviderMock) в асинхронном режиме.

## Подробнее

Этот модуль выполняет тестирование логики выбора провайдеров изображений при запросе через асинхронный клиент. Он проверяет, как клиент обрабатывает различные сценарии, такие как пропуск недоступных провайдеров, использование только одного результата, пропуск провайдеров, возвращающих None, и обработку исключений. Используются моки для имитации поведения различных провайдеров.

## Классы

### `TestIterListProvider`

**Описание**: Класс, содержащий набор асинхронных тестов для проверки работы IterListProvider.

**Наследует**
- `unittest.IsolatedAsyncioTestCase`:  Используется для создания асинхронных тестов, обеспечивая изоляцию между тестами.

**Методы**:

- `test_skip_provider()`: Проверяет, что клиент пропускает провайдера, требующего аутентификацию, и использует следующего доступного провайдера.
- `test_only_one_result()`: Проверяет, что клиент использует только один результат, даже если несколько провайдеров возвращают результат.
- `test_skip_none()`: Проверяет, что клиент пропускает провайдера, возвращающего `None`, и использует следующего доступного провайдера.
- `test_raise_exception()`: Проверяет, что исключение, возникающее у провайдера, правильно обрабатывается и вызывает исключение `RuntimeError`.

## Функции

### `test_skip_provider`

```python
    async def test_skip_provider(self):
        """ Проверяет, что клиент пропускает провайдера, требующего аутентификацию, и использует следующего доступного провайдера.
        Args:
            self (TestIterListProvider): Экземпляр класса TestIterListProvider.

        Returns:
            None

        Raises:
            AssertionError: Если утверждение о типе или значении ответа не выполняется.
        """
```

**Назначение**: Проверка пропуска провайдера, требующего аутентификацию.

**Параметры**:

- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если утверждение о типе или значении ответа не выполняется.

**Как работает функция**:

1.  Создается экземпляр `AsyncClient` с `IterListProvider`, содержащим `MissingAuthProviderMock` и `YieldImageResponseProviderMock`.
2.  Вызывается `client.images.generate` для генерации изображения.
3.  Проверяется, что полученный ответ является экземпляром `ImagesResponse`.
4.  Проверяется, что URL в ответе соответствует ожидаемому значению ("Hello").

**Примеры**:

```python
import unittest
from unittest.mock import MagicMock
from g4f.client import AsyncClient, ImagesResponse
from g4f.providers.retry_provider import IterListProvider

class MissingAuthProviderMock:
    def __init__(self):
        pass

    async def create_completion(self, *args, **kwargs):
        raise Exception("Missing auth")

class YieldImageResponseProviderMock:
    def __init__(self):
        pass

    async def create_completion(self, *args, **kwargs):
        class MockImage:
            url = "Hello"

        class MockImagesResponse:
            data = [MockImage()]

        return MockImagesResponse()

class TestIterListProvider(unittest.IsolatedAsyncioTestCase):

    async def test_skip_provider(self):
        client = AsyncClient(image_provider=IterListProvider([MissingAuthProviderMock(), YieldImageResponseProviderMock()], False))
        response = await client.images.generate("Hello", "", response_format="orginal")
        self.assertIsInstance(response, ImagesResponse)
        self.assertEqual("Hello", response.data[0].url)
```

### `test_only_one_result`

```python
    async def test_only_one_result(self):
        """ Проверяет, что клиент использует только один результат, даже если несколько провайдеров возвращают результат.
        Args:
            self (TestIterListProvider): Экземпляр класса TestIterListProvider.

        Returns:
            None

        Raises:
            AssertionError: Если утверждение о типе или значении ответа не выполняется.
        """
```

**Назначение**: Проверка использования только одного результата от провайдеров.

**Параметры**:

- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если утверждение о типе или значении ответа не выполняется.

**Как работает функция**:

1.  Создается экземпляр `AsyncClient` с `IterListProvider`, содержащим два экземпляра `YieldImageResponseProviderMock`.
2.  Вызывается `client.images.generate` для генерации изображения.
3.  Проверяется, что полученный ответ является экземпляром `ImagesResponse`.
4.  Проверяется, что URL в ответе соответствует ожидаемому значению ("Hello").

**Примеры**:

```python
import unittest
from unittest.mock import MagicMock
from g4f.client import AsyncClient, ImagesResponse
from g4f.providers.retry_provider import IterListProvider

class MissingAuthProviderMock:
    def __init__(self):
        pass

    async def create_completion(self, *args, **kwargs):
        raise Exception("Missing auth")

class YieldImageResponseProviderMock:
    def __init__(self):
        pass

    async def create_completion(self, *args, **kwargs):
        class MockImage:
            url = "Hello"

        class MockImagesResponse:
            data = [MockImage()]

        return MockImagesResponse()

class TestIterListProvider(unittest.IsolatedAsyncioTestCase):

    async def test_only_one_result(self):
        client = AsyncClient(image_provider=IterListProvider([YieldImageResponseProviderMock(), YieldImageResponseProviderMock()], False))
        response = await client.images.generate("Hello", "", response_format="orginal")
        self.assertIsInstance(response, ImagesResponse)
        self.assertEqual("Hello", response.data[0].url)
```

### `test_skip_none`

```python
    async def test_skip_none(self):
        """ Проверяет, что клиент пропускает провайдера, возвращающего `None`, и использует следующего доступного провайдера.
        Args:
            self (TestIterListProvider): Экземпляр класса TestIterListProvider.

        Returns:
            None

        Raises:
            AssertionError: Если утверждение о типе или значении ответа не выполняется.
        """
```

**Назначение**: Проверка пропуска провайдера, возвращающего `None`.

**Параметры**:

- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если утверждение о типе или значении ответа не выполняется.

**Как работает функция**:

1.  Создается экземпляр `AsyncClient` с `IterListProvider`, содержащим `YieldNoneProviderMock` и `YieldImageResponseProviderMock`.
2.  Вызывается `client.images.generate` для генерации изображения.
3.  Проверяется, что полученный ответ является экземпляром `ImagesResponse`.
4.  Проверяется, что URL в ответе соответствует ожидаемому значению ("Hello").

**Примеры**:

```python
import unittest
from unittest.mock import MagicMock
from g4f.client import AsyncClient, ImagesResponse
from g4f.providers.retry_provider import IterListProvider

class MissingAuthProviderMock:
    def __init__(self):
        pass

    async def create_completion(self, *args, **kwargs):
        raise Exception("Missing auth")

class YieldImageResponseProviderMock:
    def __init__(self):
        pass

    async def create_completion(self, *args, **kwargs):
        class MockImage:
            url = "Hello"

        class MockImagesResponse:
            data = [MockImage()]

        return MockImagesResponse()

class YieldNoneProviderMock:
    def __init__(self):
        pass

    async def create_completion(self, *args, **kwargs):
        return None

class TestIterListProvider(unittest.IsolatedAsyncioTestCase):

    async def test_skip_none(self):
        client = AsyncClient(image_provider=IterListProvider([YieldNoneProviderMock(), YieldImageResponseProviderMock()], False))
        response = await client.images.generate("Hello", "", response_format="orginal")
        self.assertIsInstance(response, ImagesResponse)
        self.assertEqual("Hello", response.data[0].url)
```

### `test_raise_exception`

```python
    def test_raise_exception(self):
        """ Проверяет, что исключение, возникающее у провайдера, правильно обрабатывается и вызывает исключение `RuntimeError`.
        Args:
            self (TestIterListProvider): Экземпляр класса TestIterListProvider.

        Returns:
            None

        Raises:
            RuntimeError: Если при генерации изображения возникает исключение.
        """
```

**Назначение**: Проверка обработки исключений от провайдеров.

**Параметры**:

- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `RuntimeError`: Если при генерации изображения возникает исключение.

**Как работает функция**:

1. Определяется внутренняя асинхронная функция `run_exception`.
2. В `run_exception` создается экземпляр `AsyncClient` с `IterListProvider`, содержащим `YieldNoneProviderMock` и `AsyncRaiseExceptionProviderMock`.
3. Вызывается `client.images.generate` для генерации изображения.
4. Функция `test_raise_exception` проверяет, что вызов `asyncio.run(run_exception())` вызывает исключение `RuntimeError`.

**Внутренние функции**:

#### `run_exception`

```python
        async def run_exception():
            """ Внутренняя асинхронная функция, создающая клиента и генерирующая изображение, чтобы вызвать исключение.
            Args:
                None

            Returns:
                None

            Raises:
                RuntimeError: Если при генерации изображения возникает исключение.
            """
```

**Назначение**: Внутренняя функция для запуска процесса генерации изображения и вызова исключения.

**Параметры**:

- Нет параметров.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `RuntimeError`: Если при генерации изображения возникает исключение.

**Как работает функция**:

1.  Создается экземпляр `AsyncClient` с `IterListProvider`, содержащим `YieldNoneProviderMock` и `AsyncRaiseExceptionProviderMock`.
2.  Вызывается `client.images.generate` для генерации изображения.

**Примеры**:

```python
import unittest
import asyncio
from unittest.mock import MagicMock
from g4f.client import AsyncClient, ImagesResponse
from g4f.providers.retry_provider import IterListProvider

class MissingAuthProviderMock:
    def __init__(self):
        pass

    async def create_completion(self, *args, **kwargs):
        raise Exception("Missing auth")

class YieldImageResponseProviderMock:
    def __init__(self):
        pass

    async def create_completion(self, *args, **kwargs):
        class MockImage:
            url = "Hello"

        class MockImagesResponse:
            data = [MockImage()]

        return MockImagesResponse()

class YieldNoneProviderMock:
    def __init__(self):
        pass

    async def create_completion(self, *args, **kwargs):
        return None

class AsyncRaiseExceptionProviderMock:
    def __init__(self):
        pass

    async def create_completion(self, *args, **kwargs):
        raise RuntimeError("Async exception")

class TestIterListProvider(unittest.IsolatedAsyncioTestCase):

    def test_raise_exception(self):
        async def run_exception():
            client = AsyncClient(image_provider=IterListProvider([YieldNoneProviderMock(), AsyncRaiseExceptionProviderMock()], False))
            await client.images.generate("Hello", "")
        self.assertRaises(RuntimeError, asyncio.run, run_exception())
```