# Модуль для тестирования провайдера с повторными попытками
=====================================================

Модуль содержит набор тестов для проверки функциональности `IterListProvider`, который позволяет последовательно перебирать список провайдеров, пока один из них не вернет успешный результат.

## Обзор

Этот модуль предназначен для тестирования класса `IterListProvider`, который используется для повторных попыток с разными провайдерами в случае неудачи. Он включает в себя тесты для проверки корректной работы `IterListProvider` при различных сценариях, таких как пропуск провайдеров, возвращающих исключения или `None`, а также для проверки потоковой передачи данных.

## Подробней

Модуль использует библиотеку `unittest` для создания и запуска тестов. В тестах используются моки провайдеров (`YieldProviderMock`, `RaiseExceptionProviderMock`, `AsyncRaiseExceptionProviderMock`, `YieldNoneProviderMock`) для имитации различных сценариев поведения провайдеров. Это позволяет проверить, что `IterListProvider` правильно обрабатывает ошибки и переходит к следующему провайдеру в списке.

## Классы

### `TestIterListProvider`

**Описание**: Класс, содержащий набор асинхронных тестов для проверки `IterListProvider`.

**Наследует**:

- `unittest.IsolatedAsyncioTestCase`: Класс для создания асинхронных тестов.

**Методы**:

- `test_skip_provider`: Проверяет, что `IterListProvider` пропускает провайдера, выбрасывающего исключение, и использует следующего провайдера в списке.
- `test_only_one_result`: Проверяет, что `IterListProvider` использует только один результат от первого успешного провайдера.
- `test_stream_skip_provider`: Проверяет, что `IterListProvider` пропускает асинхронного провайдера, выбрасывающего исключение при потоковой передаче, и использует следующего провайдера в списке.
- `test_stream_only_one_result`: Проверяет, что при потоковой передаче `IterListProvider` использует только один результат от первого успешного провайдера.
- `test_skip_none`: Проверяет, что `IterListProvider` пропускает провайдера, возвращающего `None`, и использует следующего провайдера в списке.
- `test_stream_skip_none`: Проверяет, что при потоковой передаче `IterListProvider` пропускает провайдера, возвращающего `None`, и использует следующего провайдера в списке.

## Функции

### `test_skip_provider`

```python
async def test_skip_provider(self):
    """Проверяет, что IterListProvider пропускает провайдера, выбрасывающего исключение, и использует следующего провайдера в списке."""
    ...
```

**Назначение**: Проверка, что `IterListProvider` корректно обрабатывает ситуацию, когда один из провайдеров в списке выбрасывает исключение, и переходит к следующему провайдеру.

**Параметры**:

- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:

- `None`

**Как работает функция**:

1. Создается экземпляр `AsyncClient` с `IterListProvider`, который содержит список из `RaiseExceptionProviderMock` (который выбрасывает исключение) и `YieldProviderMock` (который возвращает успешный результат).
2. Вызывается метод `client.chat.completions.create` с предопределенными сообщениями и пустой строкой.
3. Проверяется, что возвращенный результат является экземпляром `ChatCompletion`.
4. Проверяется, что содержимое сообщения в возвращенном результате равно "Hello", что указывает на то, что был использован `YieldProviderMock`.

```
Создание AsyncClient с IterListProvider
↓
Вызов client.chat.completions.create
↓
Проверка, что возвращенный результат - ChatCompletion
↓
Проверка содержимого сообщения ("Hello")
```

**Примеры**:

```python
# Пример использования в асинхронном тесте
async def test_skip_provider(self):
    client = AsyncClient(provider=IterListProvider([RaiseExceptionProviderMock, YieldProviderMock], False))
    response = await client.chat.completions.create(DEFAULT_MESSAGES, "")
    self.assertIsInstance(response, ChatCompletion)
    self.assertEqual("Hello", response.choices[0].message.content)
```

### `test_only_one_result`

```python
async def test_only_one_result(self):
    """Проверяет, что IterListProvider использует только один результат от первого успешного провайдера."""
    ...
```

**Назначение**: Проверка, что `IterListProvider` использует результат только от первого успешного провайдера и не пытается использовать результаты от последующих провайдеров.

**Параметры**:

- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:

- `None`

**Как работает функция**:

1. Создается экземпляр `AsyncClient` с `IterListProvider`, который содержит список из двух `YieldProviderMock`.
2. Вызывается метод `client.chat.completions.create` с предопределенными сообщениями и пустой строкой.
3. Проверяется, что возвращенный результат является экземпляром `ChatCompletion`.
4. Проверяется, что содержимое сообщения в возвращенном результате равно "Hello", что указывает на то, что был использован только первый `YieldProviderMock`.

```
Создание AsyncClient с IterListProvider
↓
Вызов client.chat.completions.create
↓
Проверка, что возвращенный результат - ChatCompletion
↓
Проверка содержимого сообщения ("Hello")
```

**Примеры**:

```python
# Пример использования в асинхронном тесте
async def test_only_one_result(self):
    client = AsyncClient(provider=IterListProvider([YieldProviderMock, YieldProviderMock]))
    response = await client.chat.completions.create(DEFAULT_MESSAGES, "")
    self.assertIsInstance(response, ChatCompletion)
    self.assertEqual("Hello", response.choices[0].message.content)
```

### `test_stream_skip_provider`

```python
async def test_stream_skip_provider(self):
    """Проверяет, что IterListProvider пропускает асинхронного провайдера, выбрасывающего исключение при потоковой передаче, и использует следующего провайдера в списке."""
    ...
```

**Назначение**: Проверка, что при потоковой передаче `IterListProvider` корректно обрабатывает ситуацию, когда один из асинхронных провайдеров выбрасывает исключение, и переходит к следующему провайдеру.

**Параметры**:

- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:

- `None`

**Как работает функция**:

1. Создается экземпляр `AsyncClient` с `IterListProvider`, который содержит список из `AsyncRaiseExceptionProviderMock` (который выбрасывает исключение) и `YieldProviderMock` (который возвращает успешный результат).
2. Формируются сообщения для запроса, где каждое слово является отдельным сообщением.
3. Вызывается метод `client.chat.completions.create` с потоковой передачей (`stream=True`).
4. В асинхронном цикле перебираются чанки ответа и проверяется, что каждый чанк является экземпляром `ChatCompletionChunk`.
5. Проверяется, что содержимое каждого чанка является строкой.

```
Создание AsyncClient с IterListProvider
↓
Формирование сообщений для запроса
↓
Вызов client.chat.completions.create с stream=True
↓
Асинхронный перебор чанков ответа
↓
Проверка, что каждый чанк - ChatCompletionChunk
↓
Проверка, что содержимое чанка - строка
```

**Примеры**:

```python
# Пример использования в асинхронном тесте
async def test_stream_skip_provider(self):
    client = AsyncClient(provider=IterListProvider([AsyncRaiseExceptionProviderMock, YieldProviderMock], False))
    messages = [{'role': 'user', 'content': chunk} for chunk in ["How ", "are ", "you", "?"]]
    response = client.chat.completions.create(messages, "Hello", stream=True)
    async for chunk in response:
        chunk: ChatCompletionChunk = chunk
        self.assertIsInstance(chunk, ChatCompletionChunk)
        if chunk.choices[0].delta.content is not None:
            self.assertIsInstance(chunk.choices[0].delta.content, str)
```

### `test_stream_only_one_result`

```python
async def test_stream_only_one_result(self):
    """Проверяет, что при потоковой передаче IterListProvider использует только один результат от первого успешного провайдера."""
    ...
```

**Назначение**: Проверка, что при потоковой передаче `IterListProvider` использует результат только от первого успешного провайдера и не пытается использовать результаты от последующих провайдеров.

**Параметры**:

- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:

- `None`

**Как работает функция**:

1. Создается экземпляр `AsyncClient` с `IterListProvider`, который содержит список из двух `YieldProviderMock`.
2. Формируются сообщения для запроса, где каждое слово является отдельным сообщением.
3. Вызывается метод `client.chat.completions.create` с потоковой передачей (`stream=True`) и ограничением на максимальное количество токенов (`max_tokens=2`).
4. В асинхронном цикле перебираются чанки ответа и добавляются в список `response_list`.
5. Проверяется, что длина списка `response_list` равна 3.
6. Проверяется, что содержимое каждого чанка равно "You ", что указывает на то, что был использован только первый `YieldProviderMock`.

```
Создание AsyncClient с IterListProvider
↓
Формирование сообщений для запроса
↓
Вызов client.chat.completions.create с stream=True и max_tokens=2
↓
Асинхронный перебор чанков ответа
↓
Проверка длины списка ответов (3)
↓
Проверка содержимого каждого чанка ("You ")
```

**Примеры**:

```python
# Пример использования в асинхронном тесте
async def test_stream_only_one_result(self):
    client = AsyncClient(provider=IterListProvider([YieldProviderMock, YieldProviderMock], False))
    messages = [{'role': 'user', 'content': chunk} for chunk in ["You ", "You "]]
    response = client.chat.completions.create(messages, "Hello", stream=True, max_tokens=2)
    response_list = []
    async for chunk in response:
        response_list.append(chunk)
    self.assertEqual(len(response_list), 3)
    for chunk in response_list:
        if chunk.choices[0].delta.content is not None:
            self.assertEqual(chunk.choices[0].delta.content, "You ")
```

### `test_skip_none`

```python
async def test_skip_none(self):
    """Проверяет, что IterListProvider пропускает провайдера, возвращающего None, и использует следующего провайдера в списке."""
    ...
```

**Назначение**: Проверка, что `IterListProvider` корректно обрабатывает ситуацию, когда один из провайдеров в списке возвращает `None`, и переходит к следующему провайдеру.

**Параметры**:

- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:

- `None`

**Как работает функция**:

1. Создается экземпляр `AsyncClient` с `IterListProvider`, который содержит список из `YieldNoneProviderMock` (который возвращает `None`) и `YieldProviderMock` (который возвращает успешный результат).
2. Вызывается метод `client.chat.completions.create` с предопределенными сообщениями и пустой строкой.
3. Проверяется, что возвращенный результат является экземпляром `ChatCompletion`.
4. Проверяется, что содержимое сообщения в возвращенном результате равно "Hello", что указывает на то, что был использован `YieldProviderMock`.

```
Создание AsyncClient с IterListProvider
↓
Вызов client.chat.completions.create
↓
Проверка, что возвращенный результат - ChatCompletion
↓
Проверка содержимого сообщения ("Hello")
```

**Примеры**:

```python
# Пример использования в асинхронном тесте
async def test_skip_none(self):
    client = AsyncClient(provider=IterListProvider([YieldNoneProviderMock, YieldProviderMock], False))
    response = await client.chat.completions.create(DEFAULT_MESSAGES, "")
    self.assertIsInstance(response, ChatCompletion)
    self.assertEqual("Hello", response.choices[0].message.content)
```

### `test_stream_skip_none`

```python
async def test_stream_skip_none(self):
    """Проверяет, что при потоковой передаче IterListProvider пропускает провайдера, возвращающего None, и использует следующего провайдера в списке."""
    ...
```

**Назначение**: Проверка, что при потоковой передаче `IterListProvider` корректно обрабатывает ситуацию, когда один из провайдеров возвращает `None`, и переходит к следующему провайдеру.

**Параметры**:

- `self` (TestIterListProvider): Экземпляр класса `TestIterListProvider`.

**Возвращает**:

- `None`

**Как работает функция**:

1. Создается экземпляр `AsyncClient` с `IterListProvider`, который содержит список из `YieldNoneProviderMock` (который возвращает `None`) и `YieldProviderMock` (который возвращает успешный результат).
2. Вызывается метод `client.chat.completions.create` с предопределенными сообщениями и пустой строкой, с включенной потоковой передачей (`stream=True`).
3. В асинхронном цикле перебираются чанки ответа и добавляются в список `response_list`.
4. Проверяется, что длина списка `response_list` равна 2.
5. Проверяется, что содержимое каждого чанка равно "Hello", что указывает на то, что был использован `YieldProviderMock`.

```
Создание AsyncClient с IterListProvider
↓
Вызов client.chat.completions.create с stream=True
↓
Асинхронный перебор чанков ответа
↓
Проверка длины списка ответов (2)
↓
Проверка содержимого каждого чанка ("Hello")
```

**Примеры**:

```python
# Пример использования в асинхронном тесте
async def test_stream_skip_none(self):
    client = AsyncClient(provider=IterListProvider([YieldNoneProviderMock, YieldProviderMock], False))
    response = client.chat.completions.create(DEFAULT_MESSAGES, "", stream=True)
    response_list = [chunk async for chunk in response]
    self.assertEqual(len(response_list), 2)
    for chunk in response_list:
        if chunk.choices[0].delta.content is not None:
            self.assertEqual(chunk.choices[0].delta.content, "Hello")