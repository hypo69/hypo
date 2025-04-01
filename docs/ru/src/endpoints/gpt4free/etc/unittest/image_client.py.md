# Модуль тестирования асинхронного клиента для работы с изображениями

## Обзор

Модуль содержит набор тестов для проверки корректной работы асинхронного клиента, предназначенного для генерации изображений с использованием различных провайдеров. В тестах используются моки провайдеров для эмуляции различных сценариев, таких как пропуск провайдера, получение одного результата, пропуск `None` значений и обработка исключений.

## Подробнее

Этот модуль является частью системы автоматизированного тестирования проекта `hypotez`. Он проверяет, как `AsyncClient` взаимодействует с различными реализациями провайдеров изображений, особенно при использовании `IterListProvider`, который позволяет перебирать список провайдеров до тех пор, пока не будет получен валидный результат. Это гарантирует, что клиент может корректно обрабатывать ситуации, когда один или несколько провайдеров не работают или возвращают невалидные данные.

## Классы

### `TestIterListProvider`

**Описание**: Класс, содержащий набор асинхронных тестов для проверки `IterListProvider`.

**Наследует**:

- `unittest.IsolatedAsyncioTestCase`: Обеспечивает изоляцию тестов, позволяя запускать их асинхронно.

**Атрибуты**:

- `DEFAULT_MESSAGES (list)`: Список сообщений по умолчанию, используемых в тестах.

**Методы**:

- `test_skip_provider()`: Тестирует ситуацию, когда первый провайдер пропускается из-за отсутствия аутентификации, а используется второй провайдер.
- `test_only_one_result()`: Тестирует ситуацию, когда несколько провайдеров возвращают результат, но используется только один.
- `test_skip_none()`: Тестирует ситуацию, когда один из провайдеров возвращает `None`, и он должен быть пропущен.
- `test_raise_exception()`: Тестирует ситуацию, когда один из провайдеров вызывает исключение, и оно должно быть корректно обработано.

## Функции

### `test_skip_provider`

```python
async def test_skip_provider(self):
    """
    Тестирует пропуск провайдера из-за MissingAuthProviderMock и использование YieldImageResponseProviderMock.

    Args:
        self (TestIterListProvider): Экземпляр класса TestIterListProvider.

    Returns:
        None

    Raises:
        AssertionError: Если результат не соответствует ожидаемому.
    """
```

**Назначение**: Проверяет, что если первый провайдер в списке не может быть использован (например, из-за отсутствия аутентификации), то клиент переходит к следующему провайдеру и использует его результат.

**Как работает функция**:

1.  Создается экземпляр `AsyncClient` с `IterListProvider`, содержащим `MissingAuthProviderMock` и `YieldImageResponseProviderMock`.
2.  Вызывается метод `client.images.generate` для генерации изображения.
3.  Проверяется, что возвращенный объект является экземпляром `ImagesResponse`.
4.  Проверяется, что URL изображения соответствует ожидаемому значению ("Hello"), полученному от `YieldImageResponseProviderMock`.

**ASCII flowchart**:

```
Создание AsyncClient с IterListProvider
    ↓
Вызов client.images.generate("Hello", "", response_format="orginal")
    ↓
Проверка, что response является ImagesResponse
    ↓
Проверка, что response.data[0].url == "Hello"
```

**Примеры**:

```python
# Пример использования в тестовом классе
async def test_skip_provider(self):
    client = AsyncClient(image_provider=IterListProvider([MissingAuthProviderMock, YieldImageResponseProviderMock], False))
    response = await client.images.generate("Hello", "", response_format="orginal")
    self.assertIsInstance(response, ImagesResponse)
    self.assertEqual("Hello", response.data[0].url)
```

### `test_only_one_result`

```python
async def test_only_one_result(self):
    """
    Тестирует получение только одного результата от IterListProvider при наличии нескольких провайдеров.

    Args:
        self (TestIterListProvider): Экземпляр класса TestIterListProvider.

    Returns:
        None

    Raises:
        AssertionError: Если результат не соответствует ожидаемому.
    """
```

**Назначение**: Проверяет, что даже если несколько провайдеров могут вернуть результат, `IterListProvider` возвращает только один результат.

**Как работает функция**:

1.  Создается экземпляр `AsyncClient` с `IterListProvider`, содержащим два экземпляра `YieldImageResponseProviderMock`.
2.  Вызывается метод `client.images.generate` для генерации изображения.
3.  Проверяется, что возвращенный объект является экземпляром `ImagesResponse`.
4.  Проверяется, что URL изображения соответствует ожидаемому значению ("Hello").

**ASCII flowchart**:

```
Создание AsyncClient с IterListProvider
    ↓
Вызов client.images.generate("Hello", "", response_format="orginal")
    ↓
Проверка, что response является ImagesResponse
    ↓
Проверка, что response.data[0].url == "Hello"
```

**Примеры**:

```python
# Пример использования в тестовом классе
async def test_only_one_result(self):
    client = AsyncClient(image_provider=IterListProvider([YieldImageResponseProviderMock, YieldImageResponseProviderMock], False))
    response = await client.images.generate("Hello", "", response_format="orginal")
    self.assertIsInstance(response, ImagesResponse)
    self.assertEqual("Hello", response.data[0].url)
```

### `test_skip_none`

```python
async def test_skip_none(self):
    """
    Тестирует пропуск None-значений от провайдера и использование следующего провайдера.

    Args:
        self (TestIterListProvider): Экземпляр класса TestIterListProvider.

    Returns:
        None

    Raises:
        AssertionError: Если результат не соответствует ожидаемому.
    """
```

**Назначение**: Проверяет, что если провайдер возвращает `None`, `IterListProvider` пропускает этот результат и переходит к следующему провайдеру.

**Как работает функция**:

1.  Создается экземпляр `AsyncClient` с `IterListProvider`, содержащим `YieldNoneProviderMock` и `YieldImageResponseProviderMock`.
2.  Вызывается метод `client.images.generate` для генерации изображения.
3.  Проверяется, что возвращенный объект является экземпляром `ImagesResponse`.
4.  Проверяется, что URL изображения соответствует ожидаемому значению ("Hello"), полученному от `YieldImageResponseProviderMock`.

**ASCII flowchart**:

```
Создание AsyncClient с IterListProvider
    ↓
Вызов client.images.generate("Hello", "", response_format="orginal")
    ↓
Проверка, что response является ImagesResponse
    ↓
Проверка, что response.data[0].url == "Hello"
```

**Примеры**:

```python
# Пример использования в тестовом классе
async def test_skip_none(self):
    client = AsyncClient(image_provider=IterListProvider([YieldNoneProviderMock, YieldImageResponseProviderMock], False))
    response = await client.images.generate("Hello", "", response_format="orginal")
    self.assertIsInstance(response, ImagesResponse)
    self.assertEqual("Hello", response.data[0].url)
```

### `test_raise_exception`

```python
def test_raise_exception(self):
    """
    Тестирует возникновение исключения при генерации изображения.

    Args:
        self (TestIterListProvider): Экземпляр класса TestIterListProvider.

    Returns:
        None

    Raises:
        RuntimeError: Если исключение не было вызвано.
    """
```

**Назначение**: Проверяет, что если провайдер вызывает исключение, оно корректно обрабатывается и пробрасывается.

**Как работает функция**:

1.  Определяется асинхронная функция `run_exception`, которая создает экземпляр `AsyncClient` с `IterListProvider`, содержащим `YieldNoneProviderMock` и `AsyncRaiseExceptionProviderMock`.
2.  В `run_exception` вызывается метод `client.images.generate` для генерации изображения.
3.  Используется `self.assertRaises` для проверки, что при запуске `run_exception` будет вызвано исключение `RuntimeError`.

**Внутренние функции**:

#### `run_exception`

```python
async def run_exception():
    """
    Внутренняя асинхронная функция для запуска теста с исключением.

    Args:
        None

    Returns:
        None

    Raises:
        RuntimeError: Если `AsyncRaiseExceptionProviderMock` вызывает исключение.
    """
```

**Назначение**: Запускает процесс генерации изображения с провайдером, который вызывает исключение.

**Как работает функция**:

1. Создается экземпляр `AsyncClient` с `IterListProvider`, содержащим `YieldNoneProviderMock` и `AsyncRaiseExceptionProviderMock`.
2. Вызывается метод `client.images.generate` для генерации изображения, что приводит к вызову исключения `RuntimeError` внутри `AsyncRaiseExceptionProviderMock`.

**ASCII flowchart**:

```
Определение асинхронной функции run_exception
    ↓
Создание AsyncClient с IterListProvider
    ↓
Вызов client.images.generate("Hello", "")
    ↓
Проверка, что RuntimeError было вызвано
```

**Примеры**:

```python
# Пример использования в тестовом классе
def test_raise_exception(self):
    async def run_exception():
        client = AsyncClient(image_provider=IterListProvider([YieldNoneProviderMock, AsyncRaiseExceptionProviderMock], False))
        await client.images.generate("Hello", "")
    self.assertRaises(RuntimeError, asyncio.run, run_exception())
```

### `__main__`
```python
if __name__ == '__main__':
    unittest.main()
```
**Назначение**: Запускает юнит тесты, если скрипт запущен напрямую.

**Как работает функция**:

Проверяет, является ли текущий модуль главным модулем, запущенным в Python. Если да, то запускает юнит тесты, определенные в модуле, с использованием `unittest.main()`.
```