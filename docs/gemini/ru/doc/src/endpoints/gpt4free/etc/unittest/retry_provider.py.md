# Модуль unittest для retry_provider

## Обзор

Модуль `retry_provider.py` содержит набор тестов для проверки функциональности класса `IterListProvider`, который предназначен для организации повторных попыток при использовании различных провайдеров в асинхронном клиенте. В тестах используются моки провайдеров для эмуляции различных сценариев, включая успешное выполнение, выброс исключений и возврат `None`.

## Подробнее

Этот модуль предоставляет юнит-тесты, чтобы убедиться, что `IterListProvider` правильно обрабатывает различные ситуации при работе с провайдерами, такими как `RaiseExceptionProviderMock`, `YieldProviderMock` и `YieldNoneProviderMock`. Тесты охватывают как обычные запросы, так и потоковую передачу данных, а также проверяют корректность обработки исключений и значений `None`.

## Классы

### `TestIterListProvider`

**Описание**: Класс `TestIterListProvider` наследуется от `unittest.IsolatedAsyncioTestCase` и содержит набор асинхронных тестов для проверки `IterListProvider`.

**Принцип работы**:

Класс использует асинхронные тесты для проверки различных сценариев работы `IterListProvider`. В тестах создаются экземпляры `AsyncClient` с различными конфигурациями `IterListProvider`, включающими моки провайдеров, которые эмулируют успешное выполнение, выброс исключений и возврат `None`. Тесты проверяют, что `IterListProvider` правильно обрабатывает эти сценарии как для обычных запросов, так и для потоковой передачи данных.

**Методы**:

- `test_skip_provider`: Проверяет, что `IterListProvider` пропускает провайдера, выбрасывающего исключение, и использует следующего провайдера в списке.
- `test_only_one_result`: Проверяет, что `IterListProvider` использует только один результат от первого успешного провайдера.
- `test_stream_skip_provider`: Проверяет, что `IterListProvider` пропускает провайдера, выбрасывающего исключение, при потоковой передаче данных и использует следующего провайдера.
- `test_stream_only_one_result`: Проверяет, что при потоковой передаче данных используется только один результат от первого успешного провайдера.
- `test_skip_none`: Проверяет, что `IterListProvider` пропускает провайдера, возвращающего `None`, и использует следующего провайдера в списке.
- `test_stream_skip_none`: Проверяет, что `IterListProvider` пропускает провайдера, возвращающего `None`, при потоковой передаче данных и использует следующего провайдера.

## Функции

### `test_skip_provider`

```python
    async def test_skip_provider(self):
        """
        Проверяет, что `IterListProvider` пропускает провайдера, выбрасывающего исключение, и использует следующего провайдера в списке.

        Args:
            self: Экземпляр класса `TestIterListProvider`.

        Returns:
            None

        Raises:
            AssertionError: Если результат не соответствует ожидаемому.

        Как работает функция:
        1. Создается экземпляр `AsyncClient` с `IterListProvider`, который содержит `RaiseExceptionProviderMock` (выбрасывает исключение) и `YieldProviderMock` (возвращает успешный результат).
        2. Выполняется запрос `client.chat.completions.create` с предопределенными сообщениями и пустой строкой.
        3. Проверяется, что возвращенный результат является экземпляром `ChatCompletion`.
        4. Проверяется, что содержимое сообщения в результате равно "Hello", что указывает на использование `YieldProviderMock` после пропуска `RaiseExceptionProviderMock`.
        """
```

**Примеры**:

```python
# Пример использования внутри класса TestIterListProvider
await self.test_skip_provider()
```

### `test_only_one_result`

```python
    async def test_only_one_result(self):
        """
        Проверяет, что `IterListProvider` использует только один результат от первого успешного провайдера.

        Args:
            self: Экземпляр класса `TestIterListProvider`.

        Returns:
            None

        Raises:
            AssertionError: Если результат не соответствует ожидаемому.

        Как работает функция:
        1. Создается экземпляр `AsyncClient` с `IterListProvider`, который содержит два экземпляра `YieldProviderMock` (оба возвращают успешный результат).
        2. Выполняется запрос `client.chat.completions.create` с предопределенными сообщениями и пустой строкой.
        3. Проверяется, что возвращенный результат является экземпляром `ChatCompletion`.
        4. Проверяется, что содержимое сообщения в результате равно "Hello", что указывает на использование только первого `YieldProviderMock`.
        """
```

**Примеры**:

```python
# Пример использования внутри класса TestIterListProvider
await self.test_only_one_result()
```

### `test_stream_skip_provider`

```python
    async def test_stream_skip_provider(self):
        """
        Проверяет, что `IterListProvider` пропускает провайдера, выбрасывающего исключение, при потоковой передаче данных и использует следующего провайдера.

        Args:
            self: Экземпляр класса `TestIterListProvider`.

        Returns:
            None

        Raises:
            AssertionError: Если результат не соответствует ожидаемому.

        Как работает функция:
        1. Создается экземпляр `AsyncClient` с `IterListProvider`, который содержит `AsyncRaiseExceptionProviderMock` (асинхронно выбрасывает исключение) и `YieldProviderMock` (возвращает успешный результат).
        2. Создаются сообщения для потоковой передачи, каждое содержащее часть фразы.
        3. Выполняется запрос `client.chat.completions.create` с этими сообщениями, строкой "Hello" и параметром `stream=True`.
        4. Асинхронно перебираются чанки в ответе.
        5. Проверяется, что каждый чанк является экземпляром `ChatCompletionChunk`.
        6. Проверяется, что содержимое дельты каждого чанка является строкой, если оно не `None`.
        """
```

**Примеры**:

```python
# Пример использования внутри класса TestIterListProvider
await self.test_stream_skip_provider()
```

### `test_stream_only_one_result`

```python
    async def test_stream_only_one_result(self):
        """
        Проверяет, что при потоковой передаче данных используется только один результат от первого успешного провайдера.

        Args:
            self: Экземпляр класса `TestIterListProvider`.

        Returns:
            None

        Raises:
            AssertionError: Если результат не соответствует ожидаемому.

        Как работает функция:
        1. Создается экземпляр `AsyncClient` с `IterListProvider`, который содержит два экземпляра `YieldProviderMock` (оба возвращают успешный результат).
        2. Создаются сообщения для потоковой передачи.
        3. Выполняется запрос `client.chat.completions.create` с этими сообщениями, строкой "Hello", параметром `stream=True` и `max_tokens=2`.
        4. Асинхронно перебираются чанки в ответе и добавляются в список `response_list`.
        5. Проверяется, что длина списка `response_list` равна 3.
        6. Проверяется, что содержимое дельты каждого чанка (если оно не `None`) равно "You ".
        """
```

**Примеры**:

```python
# Пример использования внутри класса TestIterListProvider
await self.test_stream_only_one_result()
```

### `test_skip_none`

```python
    async def test_skip_none(self):
        """
        Проверяет, что `IterListProvider` пропускает провайдера, возвращающего `None`, и использует следующего провайдера в списке.

        Args:
            self: Экземпляр класса `TestIterListProvider`.

        Returns:
            None

        Raises:
            AssertionError: Если результат не соответствует ожидаемому.

        Как работает функция:
        1. Создается экземпляр `AsyncClient` с `IterListProvider`, который содержит `YieldNoneProviderMock` (возвращает `None`) и `YieldProviderMock` (возвращает успешный результат).
        2. Выполняется запрос `client.chat.completions.create` с предопределенными сообщениями и пустой строкой.
        3. Проверяется, что возвращенный результат является экземпляром `ChatCompletion`.
        4. Проверяется, что содержимое сообщения в результате равно "Hello", что указывает на использование `YieldProviderMock` после пропуска `YieldNoneProviderMock`.
        """
```

**Примеры**:

```python
# Пример использования внутри класса TestIterListProvider
await self.test_skip_none()
```

### `test_stream_skip_none`

```python
    async def test_stream_skip_none(self):
        """
        Проверяет, что `IterListProvider` пропускает провайдера, возвращающего `None`, при потоковой передаче данных и использует следующего провайдера.

        Args:
            self: Экземпляр класса `TestIterListProvider`.

        Returns:
            None

        Raises:
            AssertionError: Если результат не соответствует ожидаемому.

        Как работает функция:
        1. Создается экземпляр `AsyncClient` с `IterListProvider`, который содержит `YieldNoneProviderMock` (возвращает `None`) и `YieldProviderMock` (возвращает успешный результат).
        2. Выполняется запрос `client.chat.completions.create` с предопределенными сообщениями, пустой строкой и параметром `stream=True`.
        3. Асинхронно перебираются чанки в ответе и добавляются в список `response_list`.
        4. Проверяется, что длина списка `response_list` равна 2.
        5. Проверяется, что содержимое дельты каждого чанка (если оно не `None`) равно "Hello".
        """
```

**Примеры**:

```python
# Пример использования внутри класса TestIterListProvider
await self.test_stream_skip_none()
```