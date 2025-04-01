# Модуль mocks.py
## Обзор

Модуль `mocks.py` содержит набор мок-классов провайдеров для использования в юнит-тестах, связанных с `gpt4free`. Эти моки позволяют имитировать различные сценарии поведения провайдеров, такие как успешное завершение, асинхронная генерация, генерация изображений, отсутствие аутентификации и возникновение исключений.

## Подробнее

Этот модуль предоставляет инструменты для изоляции и тестирования компонентов, взаимодействующих с провайдерами `gpt4free`, без необходимости реального подключения к внешним сервисам. Моки позволяют контролировать поведение провайдеров и проверять реакцию тестируемого кода на различные ситуации.

## Классы

### `ProviderMock`

**Описание**: Мок-класс обычного провайдера, возвращающий "Mock" при создании завершения.

**Принцип работы**:
Этот класс переопределяет метод `create_completion` и возвращает строку "Mock" при вызове. Это позволяет имитировать успешное выполнение запроса к провайдеру.

**Методы**:

- `create_completion(model, messages, stream, **kwargs)`: Генерирует строку "Mock".

**Параметры**:

- `model`: Модель для завершения.
- `messages`: Список сообщений.
- `stream`: Флаг потоковой передачи.
- `**kwargs`: Дополнительные аргументы.

```python
class ProviderMock(AbstractProvider):
    working = True

    @classmethod
    def create_completion(
        cls, model, messages, stream, **kwargs
    ):
        yield "Mock"
```

### `AsyncProviderMock`

**Описание**: Мок-класс асинхронного провайдера, возвращающий "Mock" при асинхронном создании.

**Принцип работы**:
Этот класс переопределяет метод `create_async` и возвращает строку "Mock" при асинхронном вызове. Это позволяет имитировать асинхронное выполнение запроса к провайдеру.

**Методы**:

- `create_async(model, messages, **kwargs)`: Асинхронно генерирует строку "Mock".

**Параметры**:

- `model`: Модель для завершения.
- `messages`: Список сообщений.
- `**kwargs`: Дополнительные аргументы.

```python
class AsyncProviderMock(AsyncProvider):
    working = True

    @classmethod
    async def create_async(
        cls, model, messages, **kwargs
    ):
        return "Mock"
```

### `AsyncGeneratorProviderMock`

**Описание**: Мок-класс асинхронного провайдера-генератора, выдающий "Mock" при асинхронной генерации.

**Принцип работы**:
Этот класс переопределяет метод `create_async_generator` и выдает строку "Mock" при асинхронном вызове. Это позволяет имитировать асинхронную потоковую передачу данных от провайдера.

**Методы**:

- `create_async_generator(model, messages, stream, **kwargs)`: Асинхронно генерирует строку "Mock".

**Параметры**:

- `model`: Модель для завершения.
- `messages`: Список сообщений.
- `stream`: Флаг потоковой передачи.
- `**kwargs`: Дополнительные аргументы.

```python
class AsyncGeneratorProviderMock(AsyncGeneratorProvider):
    working = True

    @classmethod
    async def create_async_generator(
        cls, model, messages, stream, **kwargs
    ):
        yield "Mock"
```

### `ModelProviderMock`

**Описание**: Мок-класс провайдера, возвращающий имя модели при создании завершения.

**Принцип работы**:
Этот класс переопределяет метод `create_completion` и возвращает имя модели, переданной в функцию. Это позволяет проверить, какая модель используется в запросе.

**Методы**:

- `create_completion(model, messages, stream, **kwargs)`: Генерирует имя модели.

**Параметры**:

- `model`: Модель для завершения.
- `messages`: Список сообщений.
- `stream`: Флаг потоковой передачи.
- `**kwargs`: Дополнительные аргументы.

```python
class ModelProviderMock(AbstractProvider):
    working = True

    @classmethod
    def create_completion(
        cls, model, messages, stream, **kwargs
    ):
        yield model
```

### `YieldProviderMock`

**Описание**: Мок-класс асинхронного провайдера-генератора, выдающий содержимое сообщений.

**Принцип работы**:
Этот класс переопределяет метод `create_async_generator` и выдает содержимое каждого сообщения из списка сообщений. Это позволяет имитировать провайдера, возвращающего содержимое запросов.

**Методы**:

- `create_async_generator(model, messages, stream, **kwargs)`: Асинхронно генерирует содержимое сообщений.

**Параметры**:

- `model`: Модель для завершения.
- `messages`: Список сообщений.
- `stream`: Флаг потоковой передачи.
- `**kwargs`: Дополнительные аргументы.

```python
class YieldProviderMock(AsyncGeneratorProvider):
    working = True

    @classmethod
    async def create_async_generator(
        cls, model, messages, stream, **kwargs
    ):
        for message in messages:
            yield message["content"]
```

### `YieldImageResponseProviderMock`

**Описание**: Мок-класс асинхронного провайдера-генератора, выдающий объект `ImageResponse`.

**Принцип работы**:
Этот класс переопределяет метод `create_async_generator` и выдает объект `ImageResponse` с заданным промптом. Это позволяет имитировать провайдера, возвращающего изображение.

**Методы**:

- `create_async_generator(model, messages, stream, prompt: str, **kwargs)`: Асинхронно генерирует объект `ImageResponse`.

**Параметры**:

- `model`: Модель для завершения.
- `messages`: Список сообщений.
- `stream`: Флаг потоковой передачи.
- `prompt` (str): Промпт для генерации изображения.
- `**kwargs`: Дополнительные аргументы.

```python
class YieldImageResponseProviderMock(AsyncGeneratorProvider):
    working = True

    @classmethod
    async def create_async_generator(
        cls, model, messages, stream, prompt: str, **kwargs
    ):
        yield ImageResponse(prompt, "")
```

### `MissingAuthProviderMock`

**Описание**: Мок-класс провайдера, выбрасывающий исключение `MissingAuthError`.

**Принцип работы**:
Этот класс переопределяет метод `create_completion` и выбрасывает исключение `MissingAuthError`, имитируя ситуацию, когда отсутствует аутентификация для доступа к провайдеру.

**Методы**:

- `create_completion(model, messages, stream, **kwargs)`: Выбрасывает исключение `MissingAuthError`.

**Параметры**:

- `model`: Модель для завершения.
- `messages`: Список сообщений.
- `stream`: Флаг потоковой передачи.
- `**kwargs`: Дополнительные аргументы.

```python
class MissingAuthProviderMock(AbstractProvider):
    working = True

    @classmethod
    def create_completion(
        cls, model, messages, stream, **kwargs
    ):
        raise MissingAuthError(cls.__name__)
        yield cls.__name__
```

### `RaiseExceptionProviderMock`

**Описание**: Мок-класс провайдера, выбрасывающий исключение `RuntimeError`.

**Принцип работы**:
Этот класс переопределяет метод `create_completion` и выбрасывает исключение `RuntimeError`, имитируя возникновение ошибки во время выполнения запроса к провайдеру.

**Методы**:

- `create_completion(model, messages, stream, **kwargs)`: Выбрасывает исключение `RuntimeError`.

**Параметры**:

- `model`: Модель для завершения.
- `messages`: Список сообщений.
- `stream`: Флаг потоковой передачи.
- `**kwargs`: Дополнительные аргументы.

```python
class RaiseExceptionProviderMock(AbstractProvider):
    working = True

    @classmethod
    def create_completion(
        cls, model, messages, stream, **kwargs
    ):
        raise RuntimeError(cls.__name__)
        yield cls.__name__
```

### `AsyncRaiseExceptionProviderMock`

**Описание**: Мок-класс асинхронного провайдера-генератора, выбрасывающий исключение `RuntimeError`.

**Принцип работы**:
Этот класс переопределяет метод `create_async_generator` и выбрасывает исключение `RuntimeError`, имитируя возникновение ошибки во время асинхронного выполнения запроса к провайдеру.

**Методы**:

- `create_async_generator(model, messages, stream, **kwargs)`: Выбрасывает исключение `RuntimeError`.

**Параметры**:

- `model`: Модель для завершения.
- `messages`: Список сообщений.
- `stream`: Флаг потоковой передачи.
- `**kwargs`: Дополнительные аргументы.

```python
class AsyncRaiseExceptionProviderMock(AsyncGeneratorProvider):
    working = True

    @classmethod
    async def create_async_generator(
        cls, model, messages, stream, **kwargs
    ):
        raise RuntimeError(cls.__name__)
        yield cls.__name__
```

### `YieldNoneProviderMock`

**Описание**: Мок-класс асинхронного провайдера-генератора, выдающий `None`.

**Принцип работы**:
Этот класс переопределяет метод `create_async_generator` и выдает значение `None`.  Имитирует ситуацию, когда провайдер не возвращает никаких данных.

**Методы**:

- `create_async_generator(model, messages, stream, **kwargs)`: Асинхронно генерирует `None`.

**Параметры**:

- `model`: Модель для завершения.
- `messages`: Список сообщений.
- `stream`: Флаг потоковой передачи.
- `**kwargs`: Дополнительные аргументы.

```python
class YieldNoneProviderMock(AsyncGeneratorProvider):
    working = True

    @classmethod
    async def create_async_generator(
        cls, model, messages, stream, **kwargs
    ):
        yield None
```

## Функции

В данном модуле нет отдельных функций, только классы с методами, которые имитируют поведение провайдеров.

## Примеры

Примеры использования мок-классов в юнит-тестах:

```python
# Пример использования ProviderMock для имитации успешного завершения
provider = ProviderMock()
result = provider.create_completion(model="test_model", messages=[])
print(next(result))  # Вывод: Mock

# Пример использования MissingAuthProviderMock для имитации ошибки аутентификации
try:
    provider = MissingAuthProviderMock()
    result = provider.create_completion(model="test_model", messages=[])
    next(result)
except MissingAuthError as ex:
    print(f"Исключение: {ex}")  # Вывод: Исключение: MissingAuthProviderMock