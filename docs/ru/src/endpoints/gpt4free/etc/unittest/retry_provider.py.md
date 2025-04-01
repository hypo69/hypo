# Документация для `retry_provider.py`

## Обзор

Файл `retry_provider.py` содержит юнит-тесты для проверки функциональности `IterListProvider` в контексте асинхронного клиента (`AsyncClient`) библиотеки `g4f`. Тесты охватывают различные сценарии, включая пропуск проблемных провайдеров, обработку потоковых ответов и проверку корректности результатов.

## Подробнее

Этот файл содержит тесты, которые проверяют, как `IterListProvider` обрабатывает различные сценарии, такие как пропуск провайдеров, возвращающих ошибки или `None`, а также как он работает с потоковыми ответами. Эти тесты важны для обеспечения надежности и отказоустойчивости системы, использующей несколько провайдеров для получения ответов от языковой модели.

## Классы

### `TestIterListProvider`

**Описание**: Класс, содержащий асинхронные юнит-тесты для `IterListProvider`.

**Наследует**:

- `unittest.IsolatedAsyncioTestCase`: Обеспечивает изоляцию при выполнении асинхронных тестов.

**Методы**:

- `test_skip_provider()`: Проверяет, что `IterListProvider` корректно пропускает провайдера, который вызывает исключение, и использует следующего провайдера в списке.
- `test_only_one_result()`: Проверяет, что `IterListProvider` использует только один результат от первого успешного провайдера, даже если в списке есть другие рабочие провайдеры.
- `test_stream_skip_provider()`: Проверяет, что `IterListProvider` корректно обрабатывает потоковые ответы, пропуская провайдеров, вызывающих исключения.
- `test_stream_only_one_result()`: Проверяет, что при потоковой передаче данных используется только один провайдер, и данные передаются корректно.
- `test_skip_none()`: Проверяет, что `IterListProvider` пропускает провайдера, который возвращает `None`, и использует следующего провайдера.
- `test_stream_skip_none()`: Проверяет, что при потоковой передаче данных `IterListProvider` пропускает провайдера, возвращающего `None`, и использует следующего провайдера.

## Функции

### `test_skip_provider`

```python
async def test_skip_provider(self):
    """Проверяет, что IterListProvider пропускает провайдера, который вызывает исключение, и использует следующего провайдера в списке.

    Args:
        self (TestIterListProvider): Экземпляр класса TestIterListProvider.

    Returns:
        None

    Raises:
        AssertionError: Если результат не соответствует ожидаемому.
    """
```

**Назначение**: Проверка корректной работы `IterListProvider` при наличии провайдера, вызывающего исключение.

**Параметры**:

- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- Отсутствуют явные исключения, но тест может завершиться с ошибкой `AssertionError`, если проверка не пройдена.

**Как работает функция**:

1.  Создается экземпляр `AsyncClient` с `IterListProvider`, который содержит два провайдера: `RaiseExceptionProviderMock` (который вызывает исключение) и `YieldProviderMock` (который возвращает корректный результат).
2.  Вызывается метод `client.chat.completions.create` с предопределенными сообщениями и пустой строкой.
3.  Проверяется, что возвращенный объект является экземпляром `ChatCompletion`.
4.  Проверяется, что содержимое сообщения в ответе равно `"Hello"`, что указывает на то, что был использован `YieldProviderMock` после пропуска `RaiseExceptionProviderMock`.

**Примеры**:

```python
# Пример вызова функции в контексте класса TestIterListProvider
await self.test_skip_provider()
```

### `test_only_one_result`

```python
async def test_only_one_result(self):
    """Проверяет, что IterListProvider использует только один результат от первого успешного провайдера, даже если в списке есть другие рабочие провайдеры.

    Args:
        self (TestIterListProvider): Экземпляр класса TestIterListProvider.

    Returns:
        None

    Raises:
        AssertionError: Если результат не соответствует ожидаемому.
    """
```

**Назначение**: Проверка использования только одного провайдера при наличии нескольких работоспособных.

**Параметры**:

- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- Отсутствуют явные исключения, но тест может завершиться с ошибкой `AssertionError`, если проверка не пройдена.

**Как работает функция**:

1.  Создается экземпляр `AsyncClient` с `IterListProvider`, содержащим два экземпляра `YieldProviderMock`.
2.  Вызывается метод `client.chat.completions.create` с предопределенными сообщениями и пустой строкой.
3.  Проверяется, что возвращенный объект является экземпляром `ChatCompletion`.
4.  Проверяется, что содержимое сообщения в ответе равно `"Hello"`, что указывает на то, что был использован только первый `YieldProviderMock`.

**Примеры**:

```python
# Пример вызова функции в контексте класса TestIterListProvider
await self.test_only_one_result()
```

### `test_stream_skip_provider`

```python
async def test_stream_skip_provider(self):
    """Проверяет, что IterListProvider корректно обрабатывает потоковые ответы, пропуская провайдеров, вызывающих исключения.

    Args:
        self (TestIterListProvider): Экземпляр класса TestIterListProvider.

    Returns:
        None

    Raises:
        AssertionError: Если результат не соответствует ожидаемому.
    """
```

**Назначение**: Проверка корректной работы с потоковыми ответами при наличии провайдера, вызывающего исключение.

**Параметры**:

- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- Отсутствуют явные исключения, но тест может завершиться с ошибкой `AssertionError`, если проверка не пройдена.

**Как работает функция**:

1.  Создается экземпляр `AsyncClient` с `IterListProvider`, содержащим `AsyncRaiseExceptionProviderMock` (который вызывает исключение в асинхронном режиме) и `YieldProviderMock`.
2.  Формируются сообщения для потоковой передачи.
3.  Вызывается метод `client.chat.completions.create` с потоковой передачей (`stream=True`).
4.  Асинхронно итерируется по чанкам ответа.
5.  Для каждого чанка проверяется, что он является экземпляром `ChatCompletionChunk`.
6.  Если в чанке есть содержимое, проверяется, что это строка.

**Примеры**:

```python
# Пример вызова функции в контексте класса TestIterListProvider
await self.test_stream_skip_provider()
```

### `test_stream_only_one_result`

```python
async def test_stream_only_one_result(self):
    """Проверяет, что при потоковой передаче данных используется только один провайдер, и данные передаются корректно.

    Args:
        self (TestIterListProvider): Экземпляр класса TestIterListProvider.

    Returns:
        None

    Raises:
        AssertionError: Если результат не соответствует ожидаемому.
    """
```

**Назначение**: Проверка использования только одного провайдера при потоковой передаче данных.

**Параметры**:

- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- Отсутствуют явные исключения, но тест может завершиться с ошибкой `AssertionError`, если проверка не пройдена.

**Как работает функция**:

1.  Создается экземпляр `AsyncClient` с `IterListProvider`, содержащим два экземпляра `YieldProviderMock`.
2.  Формируются сообщения для потоковой передачи.
3.  Вызывается метод `client.chat.completions.create` с потоковой передачей (`stream=True`) и ограничением на 2 токена (`max_tokens=2`).
4.  Асинхронно итерируется по чанкам ответа, собирая их в список `response_list`.
5.  Проверяется, что длина списка `response_list` равна 3.
6.  Для каждого чанка проверяется, что если в чанке есть содержимое, то оно равно `"You "`.

**Примеры**:

```python
# Пример вызова функции в контексте класса TestIterListProvider
await self.test_stream_only_one_result()
```

### `test_skip_none`

```python
async def test_skip_none(self):
    """Проверяет, что IterListProvider пропускает провайдера, который возвращает None, и использует следующего провайдера.

    Args:
        self (TestIterListProvider): Экземпляр класса TestIterListProvider.

    Returns:
        None

    Raises:
        AssertionError: Если результат не соответствует ожидаемому.
    """
```

**Назначение**: Проверка корректной работы `IterListProvider` при получении `None` от провайдера.

**Параметры**:

- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- Отсутствуют явные исключения, но тест может завершиться с ошибкой `AssertionError`, если проверка не пройдена.

**Как работает функция**:

1.  Создается экземпляр `AsyncClient` с `IterListProvider`, содержащим `YieldNoneProviderMock` (который возвращает `None`) и `YieldProviderMock`.
2.  Вызывается метод `client.chat.completions.create` с предопределенными сообщениями и пустой строкой.
3.  Проверяется, что возвращенный объект является экземпляром `ChatCompletion`.
4.  Проверяется, что содержимое сообщения в ответе равно `"Hello"`, что указывает на то, что был использован `YieldProviderMock` после пропуска `YieldNoneProviderMock`.

**Примеры**:

```python
# Пример вызова функции в контексте класса TestIterListProvider
await self.test_skip_none()
```

### `test_stream_skip_none`

```python
async def test_stream_skip_none(self):
    """Проверяет, что при потоковой передаче данных IterListProvider пропускает провайдера, возвращающего None, и использует следующего провайдера.

    Args:
        self (TestIterListProvider): Экземпляр класса TestIterListProvider.

    Returns:
        None

    Raises:
        AssertionError: Если результат не соответствует ожидаемому.
    """
```

**Назначение**: Проверка корректной работы с потоковыми ответами при получении `None` от провайдера.

**Параметры**:

- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- Отсутствуют явные исключения, но тест может завершиться с ошибкой `AssertionError`, если проверка не пройдена.

**Как работает функция**:

1.  Создается экземпляр `AsyncClient` с `IterListProvider`, содержащим `YieldNoneProviderMock` и `YieldProviderMock`.
2.  Вызывается метод `client.chat.completions.create` с предопределенными сообщениями и пустой строкой, а также с потоковой передачей (`stream=True`).
3.  Асинхронно итерируется по чанкам ответа, собирая их в список `response_list`.
4.  Проверяется, что длина списка `response_list` равна 2.
5.  Для каждого чанка проверяется, что если в чанке есть содержимое, то оно равно `"Hello"`.

**Примеры**:

```python
# Пример вызова функции в контексте класса TestIterListProvider
await self.test_stream_skip_none()
```