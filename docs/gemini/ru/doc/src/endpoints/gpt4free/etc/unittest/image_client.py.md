# Модуль тестирования image_client

## Обзор

Этот модуль содержит набор модульных тестов для проверки функциональности асинхронного клиента, использующего различных поставщиков изображений, включая моки для имитации различных сценариев, таких как успешное получение изображения, отсутствие аутентификации и возникновение исключений.

## Подробнее

Модуль использует `unittest` и `asyncio` для создания и запуска асинхронных тестов. Он проверяет, как `AsyncClient` обрабатывает различных поставщиков изображений, включая случаи, когда поставщики возвращают `None`, пропускаются из-за проблем с аутентификацией или выбрасывают исключения. Это позволяет убедиться, что клиент устойчив к различным ситуациям и корректно обрабатывает ошибки.

## Классы

### `TestIterListProvider`

**Описание**: Класс, содержащий асинхронные тесты для проверки логики `IterListProvider`.

**Наследует**: `unittest.IsolatedAsyncioTestCase`

**Методы**:

- `test_skip_provider`: Проверяет, что клиент пропускает поставщика, если отсутствует аутентификация, и использует следующего доступного поставщика.
- `test_only_one_result`: Проверяет, что клиент использует только один результат, даже если есть несколько поставщиков, возвращающих результат.
- `test_skip_none`: Проверяет, что клиент пропускает поставщика, если он возвращает `None`, и использует следующего доступного поставщика.
- `test_raise_exception`: Проверяет, что исключение, выброшенное поставщиком, правильно обрабатывается клиентом.

## Функции

### `test_skip_provider`

```python
    async def test_skip_provider(self):
        """Проверяет, что клиент пропускает поставщика, если отсутствует аутентификация, и использует следующего доступного поставщика.
        Args:
            self (TestIterListProvider): Экземпляр класса TestIterListProvider.
        Returns:
            None
        """
```

**Назначение**: Проверяет, что клиент пропускает поставщика изображений, если тот требует аутентификацию и не может быть использован, и переходит к следующему поставщику в списке.

**Параметры**:
- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Создает экземпляр `AsyncClient` с `IterListProvider`, содержащим два поставщика: `MissingAuthProviderMock` (имитирует отсутствие аутентификации) и `YieldImageResponseProviderMock` (возвращает успешный ответ).
2.  Вызывает метод `images.generate` у клиента для генерации изображения.
3.  Проверяет, что полученный ответ является экземпляром `ImagesResponse`.
4.  Проверяет, что URL в ответе соответствует ожидаемому значению ("Hello"), что указывает на то, что был использован второй поставщик (`YieldImageResponseProviderMock`).

**ASCII flowchart**:

```
    Создание AsyncClient с IterListProvider
    ↓
    Вызов client.images.generate
    ↓
    Проверка instance ImagesResponse
    ↓
    Проверка URL в ответе == "Hello"
```

**Примеры**:

```python
    async def test_skip_provider(self):
        client = AsyncClient(image_provider=IterListProvider([MissingAuthProviderMock, YieldImageResponseProviderMock], False))
        response = await client.images.generate("Hello", "", response_format="orginal")
        self.assertIsInstance(response, ImagesResponse)
        self.assertEqual("Hello", response.data[0].url)
```

### `test_only_one_result`

```python
    async def test_only_one_result(self):
        """Проверяет, что клиент использует только один результат, даже если есть несколько поставщиков, возвращающих результат.
        Args:
            self (TestIterListProvider): Экземпляр класса TestIterListProvider.
        Returns:
            None
        """
```

**Назначение**: Проверяет, что клиент использует только один результат, даже если несколько поставщиков возвращают валидные ответы.

**Параметры**:
- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Создает экземпляр `AsyncClient` с `IterListProvider`, содержащим два экземпляра `YieldImageResponseProviderMock` (оба возвращают успешный ответ).
2.  Вызывает метод `images.generate` у клиента для генерации изображения.
3.  Проверяет, что полученный ответ является экземпляром `ImagesResponse`.
4.  Проверяет, что URL в ответе соответствует ожидаемому значению ("Hello"), что указывает на то, что был использован один из поставщиков.

**ASCII flowchart**:

```
    Создание AsyncClient с IterListProvider
    ↓
    Вызов client.images.generate
    ↓
    Проверка instance ImagesResponse
    ↓
    Проверка URL в ответе == "Hello"
```

**Примеры**:

```python
    async def test_only_one_result(self):
        client = AsyncClient(image_provider=IterListProvider([YieldImageResponseProviderMock, YieldImageResponseProviderMock], False))
        response = await client.images.generate("Hello", "", response_format="orginal")
        self.assertIsInstance(response, ImagesResponse)
        self.assertEqual("Hello", response.data[0].url)
```

### `test_skip_none`

```python
    async def test_skip_none(self):
        """Проверяет, что клиент пропускает поставщика, если он возвращает `None`, и использует следующего доступного поставщика.
        Args:
            self (TestIterListProvider): Экземпляр класса TestIterListProvider.
        Returns:
            None
        """
```

**Назначение**: Проверяет, что клиент пропускает поставщика изображений, если тот возвращает `None`, и переходит к следующему поставщику в списке.

**Параметры**:
- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Создает экземпляр `AsyncClient` с `IterListProvider`, содержащим два поставщика: `YieldNoneProviderMock` (всегда возвращает `None`) и `YieldImageResponseProviderMock` (возвращает успешный ответ).
2.  Вызывает метод `images.generate` у клиента для генерации изображения.
3.  Проверяет, что полученный ответ является экземпляром `ImagesResponse`.
4.  Проверяет, что URL в ответе соответствует ожидаемому значению ("Hello"), что указывает на то, что был использован второй поставщик (`YieldImageResponseProviderMock`).

**ASCII flowchart**:

```
    Создание AsyncClient с IterListProvider
    ↓
    Вызов client.images.generate
    ↓
    Проверка instance ImagesResponse
    ↓
    Проверка URL в ответе == "Hello"
```

**Примеры**:

```python
    async def test_skip_none(self):
        client = AsyncClient(image_provider=IterListProvider([YieldNoneProviderMock, YieldImageResponseProviderMock], False))
        response = await client.images.generate("Hello", "", response_format="orginal")
        self.assertIsInstance(response, ImagesResponse)
        self.assertEqual("Hello", response.data[0].url)
```

### `test_raise_exception`

```python
    def test_raise_exception(self):
        """Проверяет, что исключение, выброшенное поставщиком, правильно обрабатывается клиентом.
        Args:
            self (TestIterListProvider): Экземпляр класса TestIterListProvider.
        Returns:
            None
        """
```

**Назначение**: Проверяет, что исключение, выброшенное поставщиком изображений, правильно обрабатывается и вызывает исключение `RuntimeError` в вызывающем коде.

**Параметры**:
- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Определяет внутреннюю асинхронную функцию `run_exception`, которая создает экземпляр `AsyncClient` с `IterListProvider`, содержащим два поставщика: `YieldNoneProviderMock` (возвращает `None`) и `AsyncRaiseExceptionProviderMock` (выбрасывает исключение).
2.  Вызывает метод `images.generate` у клиента для генерации изображения.
3.  Использует `self.assertRaises` для проверки, что при запуске `run_exception` через `asyncio.run` выбрасывается исключение `RuntimeError`.

**Внутренние функции**:

#### `run_exception`

```python
        async def run_exception():
            """Внутренняя асинхронная функция, которая создает клиент и вызывает генерацию изображения, ожидая исключение.
            Args:
                None
            Returns:
                None
            """
```

**Назначение**: Создает асинхронного клиента и вызывает генерацию изображения, ожидая исключение.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Как работает функция**:

1.  Создает экземпляр `AsyncClient` с `IterListProvider`, содержащим `YieldNoneProviderMock` и `AsyncRaiseExceptionProviderMock`.
2.  Вызывает `client.images.generate` для генерации изображения. Ожидается, что `AsyncRaiseExceptionProviderMock` вызовет исключение.

**ASCII flowchart**:

```
    Определение run_exception
    ↓
    Создание AsyncClient с IterListProvider
    ↓
    Вызов client.images.generate
    ↓
    Ожидание исключения
```

**ASCII flowchart (test_raise_exception)**:

```
    Определение test_raise_exception
    ↓
    Определение run_exception
    ↓
    Вызов asyncio.run(run_exception()) с проверкой на RuntimeError
```

**Примеры**:

```python
    def test_raise_exception(self):
        async def run_exception():
            client = AsyncClient(image_provider=IterListProvider([YieldNoneProviderMock, AsyncRaiseExceptionProviderMock], False))
            await client.images.generate("Hello", "")
        self.assertRaises(RuntimeError, asyncio.run, run_exception())