# Модуль тестирования асинхронного взаимодействия с ChatCompletion

## Обзор

Этот модуль содержит набор тестов для проверки асинхронной функциональности `ChatCompletion` в библиотеке `g4f`. Он включает тесты для обработки исключений, создания чатов и использования генераторов. Модуль использует mock-объекты для имитации различных поставщиков (providers) и обеспечивает всестороннее тестирование асинхронных возможностей библиотеки.

## Подробней

Модуль предназначен для проверки корректности работы асинхронных вызовов `ChatCompletion` с использованием различных mock-провайдеров. Он включает тесты для обработки исключений, возникающих при отсутствии библиотеки `nest_asyncio`, а также тесты для успешного создания чатов и использования асинхронных генераторов.

## Классы

### `TestChatCompletion`

**Описание**: Класс содержит тесты для синхронного `ChatCompletion` с асинхронными mock-провайдерами.

**Принцип работы**:

1.  Инициализация: Проверяет наличие установленной библиотеки `nest_asyncio`.
2.  Тестирование исключений: Проверяет, что при отсутствии `nest_asyncio` выбрасывается исключение `g4f.errors.NestAsyncioError`.
3.  Тестирование создания чата: Проверяет, что `ChatCompletion.create` возвращает ожидаемый результат при использовании асинхронного mock-провайдера.
4.  Тестирование генератора: Проверяет, что `ChatCompletion.create` возвращает ожидаемый результат при использовании асинхронного mock-провайдера-генератора.
5.  Тестирование асинхронного колбэка: Проверяет, что асинхронный колбэк возвращает ожидаемый результат.

**Методы**:

*   `run_exception`: Асинхронная функция, вызывающая `ChatCompletion.create` для проверки исключения.
*   `test_exception`: Проверяет выброс исключения `g4f.errors.NestAsyncioError` при отсутствии `nest_asyncio`.
*   `test_create`: Проверяет успешное создание чата с асинхронным mock-провайдером.
*   `test_create_generator`: Проверяет успешное создание чата с асинхронным mock-провайдером-генератором.
*   `test_await_callback`: Проверяет успешное выполнение асинхронного колбэка.

#### `run_exception`

```python
async def run_exception(self):
    """
    Вызывает `ChatCompletion.create` для проверки исключения.

    Args:
        self (TestChatCompletion): Экземпляр класса `TestChatCompletion`.

    Returns:
        None

    Raises:
        g4f.errors.NestAsyncioError: Если `nest_asyncio` не установлен.
    """
    ...
```

**Назначение**: Асинхронно вызывает `ChatCompletion.create` с использованием асинхронного mock-провайдера для проверки обработки исключения `NestAsyncioError`.

**Параметры**:

*   `self` (TestChatCompletion): Экземпляр класса `TestChatCompletion`.

**Возвращает**:

*   `None`

**Вызывает исключения**:

*   `g4f.errors.NestAsyncioError`: Если `nest_asyncio` не установлен.

**Как работает функция**:

1.  Вызывает `ChatCompletion.create` с параметрами по умолчанию и асинхронным mock-провайдером.
2.  Если `nest_asyncio` не установлен, ожидается исключение `NestAsyncioError`.

**Примеры**:

```python
# Пример вызова функции
async def test_run_exception(self):
    await self.run_exception()
```

#### `test_exception`

```python
def test_exception(self):
    """
    Проверяет выброс исключения `g4f.errors.NestAsyncioError` при отсутствии `nest_asyncio`.

    Args:
        self (TestChatCompletion): Экземпляр класса `TestChatCompletion`.

    Returns:
        None
    """
    ...
```

**Назначение**: Проверяет, что при отсутствии установленной библиотеки `nest_asyncio` выбрасывается исключение `g4f.errors.NestAsyncioError` при попытке запуска асинхронного кода.

**Параметры**:

*   `self` (TestChatCompletion): Экземпляр класса `TestChatCompletion`.

**Возвращает**:

*   `None`

**Вызывает исключения**:

*   `g4f.errors.NestAsyncioError`: Если `nest_asyncio` не установлен.

**Как работает функция**:

1.  Проверяет, установлена ли библиотека `nest_asyncio`.
2.  Если `nest_asyncio` установлена, тест пропускается.
3.  Если `nest_asyncio` не установлена, функция пытается запустить асинхронную функцию `self.run_exception()` с помощью `asyncio.run()`.
4.  Ожидается, что при этом будет выброшено исключение `g4f.errors.NestAsyncioError`.

**Примеры**:

```python
# Пример вызова функции
def test_test_exception(self):
    self.test_exception()
```

#### `test_create`

```python
def test_create(self):
    """
    Проверяет успешное создание чата с асинхронным mock-провайдером.

    Args:
        self (TestChatCompletion): Экземпляр класса `TestChatCompletion`.

    Returns:
        None
    """
    ...
```

**Назначение**: Проверяет, что функция `ChatCompletion.create` успешно создает чат и возвращает ожидаемый результат "Mock" при использовании асинхронного mock-провайдера `AsyncProviderMock`.

**Параметры**:

*   `self` (TestChatCompletion): Экземпляр класса `TestChatCompletion`.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Вызывает `ChatCompletion.create` с моделью по умолчанию, сообщением по умолчанию и асинхронным mock-провайдером `AsyncProviderMock`.
2.  Проверяет, что возвращаемый результат равен "Mock".

**Примеры**:

```python
# Пример вызова функции
def test_test_create(self):
    self.test_create()
```

#### `test_create_generator`

```python
def test_create_generator(self):
    """
    Проверяет успешное создание чата с асинхронным mock-провайдером-генератором.

    Args:
        self (TestChatCompletion): Экземпляр класса `TestChatCompletion`.

    Returns:
        None
    """
    ...
```

**Назначение**: Проверяет, что функция `ChatCompletion.create` успешно создает чат и возвращает ожидаемый результат "Mock" при использовании асинхронного mock-провайдера-генератора `AsyncGeneratorProviderMock`.

**Параметры**:

*   `self` (TestChatCompletion): Экземпляр класса `TestChatCompletion`.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Вызывает `ChatCompletion.create` с моделью по умолчанию, сообщением по умолчанию и асинхронным mock-провайдером-генератором `AsyncGeneratorProviderMock`.
2.  Проверяет, что возвращаемый результат равен "Mock".

**Примеры**:

```python
# Пример вызова функции
def test_test_create_generator(self):
    self.test_create_generator()
```

#### `test_await_callback`

```python
def test_await_callback(self):
    """
    Проверяет успешное выполнение асинхронного колбэка.

    Args:
        self (TestChatCompletion): Экземпляр класса `TestChatCompletion`.

    Returns:
        None
    """
    ...
```

**Назначение**: Проверяет, что асинхронный колбэк успешно выполняется и возвращает ожидаемый результат "Mock".

**Параметры**:

*   `self` (TestChatCompletion): Экземпляр класса `TestChatCompletion`.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Создает экземпляр класса `Client` с использованием асинхронного mock-провайдера-генератора `AsyncGeneratorProviderMock`.
2.  Вызывает метод `client.chat.completions.create` с параметрами по умолчанию.
3.  Проверяет, что возвращаемый результат `response.choices[0].message.content` равен "Mock".

**Примеры**:

```python
# Пример вызова функции
def test_test_await_callback(self):
    self.test_await_callback()
```

### `TestChatCompletionAsync`

**Описание**: Класс содержит тесты для асинхронного `ChatCompletion` с различными mock-провайдерами.

**Принцип работы**:

1.  Тестирование базового асинхронного вызова: Проверяет, что `ChatCompletion.create_async` возвращает ожидаемый результат при использовании синхронного mock-провайдера.
2.  Тестирование асинхронного вызова: Проверяет, что `ChatCompletion.create_async` возвращает ожидаемый результат при использовании асинхронного mock-провайдера.
3.  Тестирование асинхронного генератора: Проверяет, что `ChatCompletion.create_async` возвращает ожидаемый результат при использовании асинхронного mock-провайдера-генератора.

**Методы**:

*   `test_base`: Проверяет успешное выполнение асинхронного вызова с синхронным mock-провайдером.
*   `test_async`: Проверяет успешное выполнение асинхронного вызова с асинхронным mock-провайдером.
*   `test_create_generator`: Проверяет успешное выполнение асинхронного вызова с асинхронным mock-провайдером-генератором.

#### `test_base`

```python
async def test_base(self):
    """
    Проверяет успешное выполнение асинхронного вызова с синхронным mock-провайдером.

    Args:
        self (TestChatCompletionAsync): Экземпляр класса `TestChatCompletionAsync`.

    Returns:
        None
    """
    ...
```

**Назначение**: Проверяет, что функция `ChatCompletion.create_async` успешно создает чат и возвращает ожидаемый результат "Mock" при использовании синхронного mock-провайдера `ProviderMock`.

**Параметры**:

*   `self` (TestChatCompletionAsync): Экземпляр класса `TestChatCompletionAsync`.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Вызывает `ChatCompletion.create_async` с моделью по умолчанию, сообщением по умолчанию и синхронным mock-провайдером `ProviderMock`.
2.  Проверяет, что возвращаемый результат равен "Mock".

**Примеры**:

```python
# Пример вызова функции
async def test_test_base(self):
    await self.test_base()
```

#### `test_async`

```python
async def test_async(self):
    """
    Проверяет успешное выполнение асинхронного вызова с асинхронным mock-провайдером.

    Args:
        self (TestChatCompletionAsync): Экземпляр класса `TestChatCompletionAsync`.

    Returns:
        None
    """
    ...
```

**Назначение**: Проверяет, что функция `ChatCompletion.create_async` успешно создает чат и возвращает ожидаемый результат "Mock" при использовании асинхронного mock-провайдера `AsyncProviderMock`.

**Параметры**:

*   `self` (TestChatCompletionAsync): Экземпляр класса `TestChatCompletionAsync`.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Вызывает `ChatCompletion.create_async` с моделью по умолчанию, сообщением по умолчанию и асинхронным mock-провайдером `AsyncProviderMock`.
2.  Проверяет, что возвращаемый результат равен "Mock".

**Примеры**:

```python
# Пример вызова функции
async def test_test_async(self):
    await self.test_async()
```

#### `test_create_generator`

```python
async def test_create_generator(self):
    """
    Проверяет успешное выполнение асинхронного вызова с асинхронным mock-провайдером-генератором.

    Args:
        self (TestChatCompletionAsync): Экземпляр класса `TestChatCompletionAsync`.

    Returns:
        None
    """
    ...
```

**Назначение**: Проверяет, что функция `ChatCompletion.create_async` успешно создает чат и возвращает ожидаемый результат "Mock" при использовании асинхронного mock-провайдера-генератора `AsyncGeneratorProviderMock`.

**Параметры**:

*   `self` (TestChatCompletionAsync): Экземпляр класса `TestChatCompletionAsync`.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Вызывает `ChatCompletion.create_async` с моделью по умолчанию, сообщением по умолчанию и асинхронным mock-провайдером-генератором `AsyncGeneratorProviderMock`.
2.  Проверяет, что возвращаемый результат равен "Mock".

**Примеры**:

```python
# Пример вызова функции
async def test_test_create_generator(self):
    await self.test_create_generator()
```

### `TestChatCompletionNestAsync`

**Описание**: Класс содержит тесты для `ChatCompletion` с использованием `nest_asyncio`.

**Принцип работы**:

1.  Инициализация: Проверяет наличие установленной библиотеки `nest_asyncio` и применяет `nest_asyncio.apply()`.
2.  Тестирование создания чата: Проверяет, что `ChatCompletion.create_async` возвращает ожидаемый результат при использовании синхронного mock-провайдера.
3.  Тестирование вложенного асинхронного вызова: Проверяет, что `ChatCompletion.create` возвращает ожидаемый результат при использовании асинхронного mock-провайдера.
4.  Тестирование вложенного асинхронного генератора: Проверяет, что `ChatCompletion.create` возвращает ожидаемый результат при использовании асинхронного mock-провайдера-генератора.

**Методы**:

*   `setUp`: Выполняется перед каждым тестом, проверяет наличие `nest_asyncio` и применяет его.
*   `test_create`: Проверяет успешное создание чата с синхронным mock-провайдером.
*   `_test_nested`: Проверяет успешное выполнение вложенного асинхронного вызова с асинхронным mock-провайдером.
*   `_test_nested_generator`: Проверяет успешное выполнение вложенного асинхронного вызова с асинхронным mock-провайдером-генератором.

#### `setUp`

```python
def setUp(self) -> None:
    """
    Выполняется перед каждым тестом, проверяет наличие `nest_asyncio` и применяет его.

    Args:
        self (TestChatCompletionNestAsync): Экземпляр класса `TestChatCompletionNestAsync`.

    Returns:
        None
    """
    ...
```

**Назначение**: Метод `setUp` вызывается перед каждым тестовым методом в классе. Он проверяет, установлена ли библиотека `nest_asyncio`, и если она не установлена, тест пропускается. Если `nest_asyncio` установлена, то применяется функция `nest_asyncio.apply()`, которая позволяет вкладывать асинхронные вызовы друг в друга.

**Параметры**:

*   `self` (TestChatCompletionNestAsync): Экземпляр класса `TestChatCompletionNestAsync`.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Проверяет, установлена ли библиотека `nest_asyncio` (переменная `has_nest_asyncio`).
2.  Если `nest_asyncio` не установлена, тест пропускается с помощью `self.skipTest('"nest_asyncio" not installed')`.
3.  Если `nest_asyncio` установлена, применяется функция `nest_asyncio.apply()`.

**Примеры**:

```python
# Пример вызова функции
def test_setup(self):
    self.setUp()
```

#### `test_create`

```python
async def test_create(self):
    """
    Проверяет успешное создание чата с синхронным mock-провайдером.

    Args:
        self (TestChatCompletionNestAsync): Экземпляр класса `TestChatCompletionNestAsync`.

    Returns:
        None
    """
    ...
```

**Назначение**: Проверяет, что функция `ChatCompletion.create_async` успешно создает чат и возвращает ожидаемый результат "Mock" при использовании синхронного mock-провайдера `ProviderMock`.

**Параметры**:

*   `self` (TestChatCompletionNestAsync): Экземпляр класса `TestChatCompletionNestAsync`.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Вызывает `ChatCompletion.create_async` с моделью по умолчанию, сообщением по умолчанию и синхронным mock-провайдером `ProviderMock`.
2.  Проверяет, что возвращаемый результат равен "Mock".

**Примеры**:

```python
# Пример вызова функции
async def test_test_create(self):
    await self.test_create()
```

#### `_test_nested`

```python
async def _test_nested(self):
    """
    Проверяет успешное выполнение вложенного асинхронного вызова с асинхронным mock-провайдером.

    Args:
        self (TestChatCompletionNestAsync): Экземпляр класса `TestChatCompletionNestAsync`.

    Returns:
        None
    """
    ...
```

**Назначение**: Проверяет, что функция `ChatCompletion.create` успешно создает чат и возвращает ожидаемый результат "Mock" при использовании асинхронного mock-провайдера `AsyncProviderMock`.

**Параметры**:

*   `self` (TestChatCompletionNestAsync): Экземпляр класса `TestChatCompletionNestAsync`.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Вызывает `ChatCompletion.create` с моделью по умолчанию, сообщением по умолчанию и асинхронным mock-провайдером `AsyncProviderMock`.
2.  Проверяет, что возвращаемый результат равен "Mock".

**Примеры**:

```python
# Пример вызова функции
async def test__test_nested(self):
    await self._test_nested()
```

#### `_test_nested_generator`

```python
async def _test_nested_generator(self):
    """
    Проверяет успешное выполнение вложенного асинхронного вызова с асинхронным mock-провайдером-генератором.

    Args:
        self (TestChatCompletionNestAsync): Экземпляр класса `TestChatCompletionNestAsync`.

    Returns:
        None
    """
    ...
```

**Назначение**: Проверяет, что функция `ChatCompletion.create` успешно создает чат и возвращает ожидаемый результат "Mock" при использовании асинхронного mock-провайдера-генератора `AsyncGeneratorProviderMock`.

**Параметры**:

*   `self` (TestChatCompletionNestAsync): Экземпляр класса `TestChatCompletionNestAsync`.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Вызывает `ChatCompletion.create` с моделью по умолчанию, сообщением по умолчанию и асинхронным mock-провайдером-генератором `AsyncGeneratorProviderMock`.
2.  Проверяет, что возвращаемый результат равен "Mock".

**Примеры**:

```python
# Пример вызова функции
async def test__test_nested_generator(self):
    await self._test_nested_generator()
```

## Функции

### `main`

```python
if __name__ == '__main__':
    unittest.main()
```

**Назначение**: Запускает тесты, если скрипт запущен как основной.

**Как работает функция**:

1.  Проверяет, является ли текущий скрипт основным ( `__name__ == '__main__'` ).
2.  Если да, запускает тесты с помощью `unittest.main()`.

## TOC

*   [TestChatCompletion](#TestChatCompletion)
    *   [run_exception](#run_exception)
    *   [test_exception](#test_exception)
    *   [test_create](#test_create)
    *   [test_create_generator](#test_create_generator)
    *   [test_await_callback](#test_await_callback)
*   [TestChatCompletionAsync](#TestChatCompletionAsync)
    *   [test_base](#test_base)
    *   [test_async](#test_async)
    *   [test_create_generator](#test_create_generator)
*   [TestChatCompletionNestAsync](#TestChatCompletionNestAsync)
    *   [setUp](#setUp)
    *   [test_create](#test_create)
    *   [_test_nested](#_test_nested)
    *   [_test_nested_generator](#_test_nested_generator)
*   [main](#main)