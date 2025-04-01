# Модуль unittest для асинхронного тестирования g4f

## Обзор

Модуль содержит набор тестов для асинхронной функциональности библиотеки `g4f`, в частности, для `ChatCompletion`. Тесты проверяют правильность обработки асинхронных запросов, исключений и генераторов.

## Подробней

Этот модуль предназначен для тестирования асинхронных возможностей библиотеки `g4f`. Он использует `unittest` и `asyncio` для проверки корректности работы `ChatCompletion` с различными типами асинхронных провайдеров.

## Классы

### `TestChatCompletion`

**Описание**: Класс содержит тесты для синхронной проверки `ChatCompletion` с использованием асинхронных моков.

**Наследует**: `unittest.TestCase`

**Методы**:

- `run_exception()`:

   ```python
   async def run_exception(self):
       """
       Выполняет `ChatCompletion.create` с асинхронным провайдером и возвращает результат.

       Returns:
           Any: Результат выполнения `ChatCompletion.create`.
       """
       ...
   ```

- `test_exception()`:

   ```python
   def test_exception(self):
       """
       Проверяет, что при попытке запуска асинхронного кода в синхронном контексте возникает исключение `g4f.errors.NestAsyncioError`, если `nest_asyncio` не установлен.
       """
       ...
   ```

- `test_create()`:

   ```python
   def test_create(self):
       """
       Проверяет, что `ChatCompletion.create` возвращает ожидаемый результат ("Mock") при использовании `AsyncProviderMock`.
       """
       ...
   ```

- `test_create_generator()`:

   ```python
   def test_create_generator(self):
       """
       Проверяет, что `ChatCompletion.create` возвращает ожидаемый результат ("Mock") при использовании `AsyncGeneratorProviderMock`.
       """
       ...
   ```

- `test_await_callback()`:

   ```python
   def test_await_callback(self):
       """
       Проверяет, что `client.chat.completions.create` возвращает ожидаемый результат ("Mock") при использовании `AsyncGeneratorProviderMock`.
       """
       ...
   ```

### `TestChatCompletionAsync`

**Описание**: Класс содержит тесты для асинхронной проверки `ChatCompletion` с использованием различных моков.

**Наследует**: `unittest.IsolatedAsyncioTestCase`

**Методы**:

- `test_base()`:

   ```python
   async def test_base(self):
       """
       Проверяет, что `ChatCompletion.create_async` возвращает ожидаемый результат ("Mock") при использовании `ProviderMock`.
       """
       ...
   ```

- `test_async()`:

   ```python
   async def test_async(self):
       """
       Проверяет, что `ChatCompletion.create_async` возвращает ожидаемый результат ("Mock") при использовании `AsyncProviderMock`.
       """
       ...
   ```

- `test_create_generator()`:

   ```python
   async def test_create_generator(self):
       """
       Проверяет, что `ChatCompletion.create_async` возвращает ожидаемый результат ("Mock") при использовании `AsyncGeneratorProviderMock`.
       """
       ...
   ```

### `TestChatCompletionNestAsync`

**Описание**: Класс содержит тесты для асинхронной проверки `ChatCompletion` с использованием `nest_asyncio`.

**Наследует**: `unittest.IsolatedAsyncioTestCase`

**Методы**:

- `setUp()`:

   ```python
   def setUp(self) -> None:
       """
       Настраивает тестовый случай, пропуская тест, если `nest_asyncio` не установлен, и применяет `nest_asyncio`.
       """
       ...
   ```

- `test_create()`:

   ```python
   async def test_create(self):
       """
       Проверяет, что `ChatCompletion.create_async` возвращает ожидаемый результат ("Mock") при использовании `ProviderMock` и `nest_asyncio`.
       """
       ...
   ```

- `_test_nested()`:

   ```python
   async def _test_nested(self):
       """
       Проверяет, что `ChatCompletion.create` возвращает ожидаемый результат ("Mock") при использовании `AsyncProviderMock` и `nest_asyncio`.
       """
       ...
   ```

- `_test_nested_generator()`:

   ```python
   async def _test_nested_generator(self):
       """
       Проверяет, что `ChatCompletion.create` возвращает ожидаемый результат ("Mock") при использовании `AsyncGeneratorProviderMock` и `nest_asyncio`.
       """
       ...
   ```

## Функции

### `run_exception`

```python
async def run_exception(self):
    """
    Выполняет `ChatCompletion.create` с асинхронным провайдером и возвращает результат.

    Returns:
        Any: Результат выполнения `ChatCompletion.create`.
    """
    ...
```

**Назначение**:
Запускает асинхронную операцию `ChatCompletion.create` с использованием мок-провайдера `AsyncProviderMock`.

**Как работает функция**:

1.  Вызывает `ChatCompletion.create` с моделью по умолчанию (`g4f.models.default`), сообщением по умолчанию (`DEFAULT_MESSAGES`) и асинхронным мок-провайдером (`AsyncProviderMock`).

ASCII Flowchart:

```
ChatCompletion.create(model, messages, provider)
|
Возвращает результат
```

### `test_exception`

```python
def test_exception(self):
    """
    Проверяет, что при попытке запуска асинхронного кода в синхронном контексте возникает исключение `g4f.errors.NestAsyncioError`, если `nest_asyncio` не установлен.
    """
    ...
```

**Назначение**:
Проверяет возникновение исключения `g4f.errors.NestAsyncioError` при попытке запуска асинхронного кода в синхронном контексте, если `nest_asyncio` не установлен.

**Как работает функция**:

1.  Проверяет, установлен ли `nest_asyncio`. Если да, то тест пропускается.
2.  Вызывает `asyncio.run` с функцией `self.run_exception()`.
3.  Проверяет, что при этом возникает исключение `g4f.errors.NestAsyncioError`.

ASCII Flowchart:

```
Проверка наличия nest_asyncio
|
Если nest_asyncio установлен -> Пропуск теста
|
Вызов asyncio.run(self.run_exception())
|
Проверка возникновения исключения g4f.errors.NestAsyncioError
```

### `test_create` (в `TestChatCompletion`)

```python
def test_create(self):
    """
    Проверяет, что `ChatCompletion.create` возвращает ожидаемый результат ("Mock") при использовании `AsyncProviderMock`.
    """
    ...
```

**Назначение**:
Проверяет, что функция `ChatCompletion.create` возвращает ожидаемое значение "Mock" при использовании мок-провайдера `AsyncProviderMock`.

**Как работает функция**:

1.  Вызывает `ChatCompletion.create` с моделью по умолчанию (`g4f.models.default`), сообщением по умолчанию (`DEFAULT_MESSAGES`) и асинхронным мок-провайдером (`AsyncProviderMock`).
2.  Сравнивает результат с ожидаемым значением "Mock".

ASCII Flowchart:

```
ChatCompletion.create(model, messages, provider)
|
Сравнение результата с "Mock"
```

### `test_create_generator` (в `TestChatCompletion`)

```python
def test_create_generator(self):
    """
    Проверяет, что `ChatCompletion.create` возвращает ожидаемый результат ("Mock") при использовании `AsyncGeneratorProviderMock`.
    """
    ...
```

**Назначение**:
Проверяет, что функция `ChatCompletion.create` возвращает ожидаемое значение "Mock" при использовании мок-провайдера `AsyncGeneratorProviderMock`.

**Как работает функция**:

1.  Вызывает `ChatCompletion.create` с моделью по умолчанию (`g4f.models.default`), сообщением по умолчанию (`DEFAULT_MESSAGES`) и асинхронным мок-провайдером `AsyncGeneratorProviderMock`.
2.  Сравнивает результат с ожидаемым значением "Mock".

ASCII Flowchart:

```
ChatCompletion.create(model, messages, provider)
|
Сравнение результата с "Mock"
```

### `test_await_callback`

```python
def test_await_callback(self):
    """
    Проверяет, что `client.chat.completions.create` возвращает ожидаемый результат ("Mock") при использовании `AsyncGeneratorProviderMock`.
    """
    ...
```

**Назначение**:
Проверяет, что асинхронный клиент возвращает ожидаемый результат "Mock" при использовании `AsyncGeneratorProviderMock`.

**Как работает функция**:

1.  Создает экземпляр `Client` с `AsyncGeneratorProviderMock` в качестве провайдера.
2.  Вызывает `client.chat.completions.create` с сообщением по умолчанию (`DEFAULT_MESSAGES`), пустой строкой и `max_tokens=0`.
3.  Сравнивает содержимое сообщения первого выбора с ожидаемым значением "Mock".

ASCII Flowchart:

```
Создание экземпляра Client с AsyncGeneratorProviderMock
|
Вызов client.chat.completions.create(messages, "", max_tokens=0)
|
Сравнение результата с "Mock"
```

### `test_base` (в `TestChatCompletionAsync`)

```python
async def test_base(self):
    """
    Проверяет, что `ChatCompletion.create_async` возвращает ожидаемый результат ("Mock") при использовании `ProviderMock`.
    """
    ...
```

**Назначение**:
Проверяет, что асинхронная функция `ChatCompletion.create_async` возвращает ожидаемое значение "Mock" при использовании мок-провайдера `ProviderMock`.

**Как работает функция**:

1.  Вызывает `ChatCompletion.create_async` с моделью по умолчанию (`g4f.models.default`), сообщением по умолчанию (`DEFAULT_MESSAGES`) и мок-провайдером (`ProviderMock`).
2.  Сравнивает результат с ожидаемым значением "Mock".

ASCII Flowchart:

```
ChatCompletion.create_async(model, messages, provider)
|
Сравнение результата с "Mock"
```

### `test_async` (в `TestChatCompletionAsync`)

```python
async def test_async(self):
    """
    Проверяет, что `ChatCompletion.create_async` возвращает ожидаемый результат ("Mock") при использовании `AsyncProviderMock`.
    """
    ...
```

**Назначение**:
Проверяет, что асинхронная функция `ChatCompletion.create_async` возвращает ожидаемое значение "Mock" при использовании мок-провайдера `AsyncProviderMock`.

**Как работает функция**:

1.  Вызывает `ChatCompletion.create_async` с моделью по умолчанию (`g4f.models.default`), сообщением по умолчанию (`DEFAULT_MESSAGES`) и асинхронным мок-провайдером (`AsyncProviderMock`).
2.  Сравнивает результат с ожидаемым значением "Mock".

ASCII Flowchart:

```
ChatCompletion.create_async(model, messages, provider)
|
Сравнение результата с "Mock"
```

### `test_create_generator` (в `TestChatCompletionAsync`)

```python
async def test_create_generator(self):
    """
    Проверяет, что `ChatCompletion.create_async` возвращает ожидаемый результат ("Mock") при использовании `AsyncGeneratorProviderMock`.
    """
    ...
```

**Назначение**:
Проверяет, что асинхронная функция `ChatCompletion.create_async` возвращает ожидаемое значение "Mock" при использовании мок-провайдера `AsyncGeneratorProviderMock`.

**Как работает функция**:

1.  Вызывает `ChatCompletion.create_async` с моделью по умолчанию (`g4f.models.default`), сообщением по умолчанию (`DEFAULT_MESSAGES`) и асинхронным мок-провайдером `AsyncGeneratorProviderMock`.
2.  Сравнивает результат с ожидаемым значением "Mock".

ASCII Flowchart:

```
ChatCompletion.create_async(model, messages, provider)
|
Сравнение результата с "Mock"
```

### `setUp` (в `TestChatCompletionNestAsync`)

```python
def setUp(self) -> None:
    """
    Настраивает тестовый случай, пропуская тест, если `nest_asyncio` не установлен, и применяет `nest_asyncio`.
    """
    ...
```

**Назначение**:
Выполняет настройку перед каждым тестом в классе `TestChatCompletionNestAsync`.

**Как работает функция**:

1.  Проверяет, установлен ли пакет `nest_asyncio`. Если нет, тест пропускается.
2.  Применяет `nest_asyncio.apply()`, чтобы разрешить вложенные циклы событий asyncio.

ASCII Flowchart:

```
Проверка наличия nest_asyncio
|
Если nest_asyncio не установлен -> Пропуск теста
|
Применение nest_asyncio.apply()
```

### `test_create` (в `TestChatCompletionNestAsync`)

```python
async def test_create(self):
    """
    Проверяет, что `ChatCompletion.create_async` возвращает ожидаемый результат ("Mock") при использовании `ProviderMock` и `nest_asyncio`.
    """
    ...
```

**Назначение**:
Проверяет, что асинхронная функция `ChatCompletion.create_async` возвращает ожидаемое значение "Mock" при использовании мок-провайдера `ProviderMock` и установленном `nest_asyncio`.

**Как работает функция**:

1.  Вызывает `ChatCompletion.create_async` с моделью по умолчанию (`g4f.models.default`), сообщением по умолчанию (`DEFAULT_MESSAGES`) и мок-провайдером `ProviderMock`.
2.  Сравнивает результат с ожидаемым значением "Mock".

ASCII Flowchart:

```
ChatCompletion.create_async(model, messages, provider)
|
Сравнение результата с "Mock"
```

### `_test_nested` (в `TestChatCompletionNestAsync`)

```python
async def _test_nested(self):
    """
    Проверяет, что `ChatCompletion.create` возвращает ожидаемый результат ("Mock") при использовании `AsyncProviderMock` и `nest_asyncio`.
    """
    ...
```

**Назначение**:
Проверяет, что функция `ChatCompletion.create` возвращает ожидаемое значение "Mock" при использовании асинхронного мок-провайдера `AsyncProviderMock` и установленном `nest_asyncio`.

**Как работает функция**:

1.  Вызывает `ChatCompletion.create` с моделью по умолчанию (`g4f.models.default`), сообщением по умолчанию (`DEFAULT_MESSAGES`) и мок-провайдером `AsyncProviderMock`.
2.  Сравнивает результат с ожидаемым значением "Mock".

ASCII Flowchart:

```
ChatCompletion.create(model, messages, provider)
|
Сравнение результата с "Mock"
```

### `_test_nested_generator` (в `TestChatCompletionNestAsync`)

```python
async def _test_nested_generator(self):
    """
    Проверяет, что `ChatCompletion.create` возвращает ожидаемый результат ("Mock") при использовании `AsyncGeneratorProviderMock` и `nest_asyncio`.
    """
    ...
```

**Назначение**:
Проверяет, что функция `ChatCompletion.create` возвращает ожидаемое значение "Mock" при использовании асинхронного мок-провайдера `AsyncGeneratorProviderMock` и установленном `nest_asyncio`.

**Как работает функция**:

1.  Вызывает `ChatCompletion.create` с моделью по умолчанию (`g4f.models.default`), сообщением по умолчанию (`DEFAULT_MESSAGES`) и мок-провайдером `AsyncGeneratorProviderMock`.
2.  Сравнивает результат с ожидаемым значением "Mock".

ASCII Flowchart:

```
ChatCompletion.create(model, messages, provider)
|
Сравнение результата с "Mock"
```

## Примеры

Пример использования классов для тестирования асинхронных функций `ChatCompletion`:

```python
import unittest
import asyncio

class TestChatCompletionAsync(unittest.IsolatedAsyncioTestCase):

    async def test_base(self):
        result = await ChatCompletion.create_async(g4f.models.default, DEFAULT_MESSAGES, ProviderMock)
        self.assertEqual("Mock",result)

if __name__ == '__main__':
    unittest.main()