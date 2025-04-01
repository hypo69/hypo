# Модуль mocks.py
## Обзор

Модуль `mocks.py` содержит набор классов, представляющих собой моки (имитации) различных провайдеров для использования в юнит-тестах. Эти моки позволяют изолированно тестировать функциональность, зависящую от внешних провайдеров, без необходимости реального подключения к ним.
Они позволяют имитировать различные сценарии, включая успешные ответы, ошибки аутентификации и исключения.
## Подробнее

Модуль предоставляет классы, имитирующие как синхронные, так и асинхронные провайдеры, а также провайдеры, возвращающие потоковые ответы и изображения. Это позволяет тестировать различные аспекты взаимодействия с провайдерами в контролируемой среде.
## Классы

### `ProviderMock`

**Описание**: Мок для абстрактного провайдера `AbstractProvider`.

**Принцип работы**: Этот класс имитирует базового провайдера, возвращая строку "Mock" при вызове метода `create_completion`.

**Методы**:

- `create_completion(cls, model, messages, stream, **kwargs)`:
  - **Назначение**: Создает имитацию завершения запроса.
  - **Параметры**:
    - `cls`: Ссылка на класс.
    - `model`: Имя модели.
    - `messages`: Список сообщений.
    - `stream`: Флаг потоковой передачи.
    - `**kwargs`: Дополнительные аргументы.
  - **Возвращает**: Генератор, выдающий строку "Mock".

**Примеры**:

```python
# Пример использования ProviderMock
provider = ProviderMock()
result = provider.create_completion(model="test_model", messages=[], stream=False)
print(next(result))  # Вывод: Mock
```

### `AsyncProviderMock`

**Описание**: Мок для асинхронного провайдера `AsyncProvider`.

**Принцип работы**: Этот класс имитирует асинхронного провайдера, возвращая строку "Mock" при вызове асинхронного метода `create_async`.

**Методы**:

- `create_async(cls, model, messages, **kwargs)`:
  - **Назначение**: Создает имитацию асинхронного завершения запроса.
  - **Параметры**:
    - `cls`: Ссылка на класс.
    - `model`: Имя модели.
    - `messages`: Список сообщений.
    - `**kwargs`: Дополнительные аргументы.
  - **Возвращает**: Асинхронная функция, возвращающая строку "Mock".

**Примеры**:

```python
import asyncio
# Пример использования AsyncProviderMock
async def main():
    provider = AsyncProviderMock()
    result = await provider.create_async(model="test_model", messages=[])
    print(result)

asyncio.run(main()) # Вывод: Mock
```

### `AsyncGeneratorProviderMock`

**Описание**: Мок для асинхронного генератора провайдера `AsyncGeneratorProvider`.

**Принцип работы**: Этот класс имитирует асинхронного генератора провайдера, возвращая строку "Mock" при вызове асинхронного метода `create_async_generator`.

**Методы**:

- `create_async_generator(cls, model, messages, stream, **kwargs)`:
  - **Назначение**: Создает имитацию асинхронного генератора завершений запроса.
  - **Параметры**:
    - `cls`: Ссылка на класс.
    - `model`: Имя модели.
    - `messages`: Список сообщений.
    - `stream`: Флаг потоковой передачи.
    - `**kwargs`: Дополнительные аргументы.
  - **Возвращает**: Асинхронный генератор, выдающий строку "Mock".

**Примеры**:

```python
import asyncio
# Пример использования AsyncGeneratorProviderMock
async def main():
    provider = AsyncGeneratorProviderMock()
    async for result in provider.create_async_generator(model="test_model", messages=[], stream=False):
        print(result)

asyncio.run(main()) # Вывод: Mock
```

### `ModelProviderMock`

**Описание**: Мок для провайдера, возвращающего имя модели.

**Принцип работы**: Этот класс имитирует провайдера, возвращая имя модели, переданное в метод `create_completion`.

**Методы**:

- `create_completion(cls, model, messages, stream, **kwargs)`:
  - **Назначение**: Создает имитацию завершения запроса, возвращая имя модели.
  - **Параметры**:
    - `cls`: Ссылка на класс.
    - `model`: Имя модели.
    - `messages`: Список сообщений.
    - `stream`: Флаг потоковой передачи.
    - `**kwargs`: Дополнительные аргументы.
  - **Возвращает**: Генератор, выдающий имя модели.

**Примеры**:

```python
# Пример использования ModelProviderMock
provider = ModelProviderMock()
result = provider.create_completion(model="test_model", messages=[], stream=False)
print(next(result)) # Вывод: test_model
```

### `YieldProviderMock`

**Описание**: Мок для асинхронного генератора провайдера, возвращающего содержимое сообщений.

**Принцип работы**: Этот класс имитирует асинхронного генератора провайдера, возвращая содержимое каждого сообщения из списка `messages`.

**Методы**:

- `create_async_generator(cls, model, messages, stream, **kwargs)`:
  - **Назначение**: Создает имитацию асинхронного генератора завершений запроса, возвращая содержимое сообщений.
  - **Параметры**:
    - `cls`: Ссылка на класс.
    - `model`: Имя модели.
    - `messages`: Список сообщений.
    - `stream`: Флаг потоковой передачи.
    - `**kwargs`: Дополнительные аргументы.
  - **Возвращает**: Асинхронный генератор, выдающий содержимое каждого сообщения.

**Примеры**:

```python
import asyncio
# Пример использования YieldProviderMock
async def main():
    provider = YieldProviderMock()
    messages = [{"content": "Первое сообщение"}, {"content": "Второе сообщение"}]
    async for result in provider.create_async_generator(model="test_model", messages=messages, stream=False):
        print(result)

asyncio.run(main())
# Вывод:
# Первое сообщение
# Второе сообщение
```

### `YieldImageResponseProviderMock`

**Описание**: Мок для асинхронного генератора провайдера, возвращающего объект `ImageResponse`.

**Принцип работы**: Этот класс имитирует асинхронного генератора провайдера, возвращая объект `ImageResponse` с заданным запросом и пустой строкой для URL.

**Методы**:

- `create_async_generator(cls, model, messages, stream, prompt: str, **kwargs)`:
  - **Назначение**: Создает имитацию асинхронного генератора завершений запроса, возвращая объект `ImageResponse`.
  - **Параметры**:
    - `cls`: Ссылка на класс.
    - `model`: Имя модели.
    - `messages`: Список сообщений.
    - `stream`: Флаг потоковой передачи.
    - `prompt` (str): Текст запроса.
    - `**kwargs`: Дополнительные аргументы.
  - **Возвращает**: Асинхронный генератор, выдающий объект `ImageResponse`.

**Примеры**:

```python
import asyncio
from g4f.providers.response import ImageResponse
# Пример использования YieldImageResponseProviderMock
async def main():
    provider = YieldImageResponseProviderMock()
    async for result in provider.create_async_generator(model="test_model", messages=[], stream=False, prompt="test_prompt"):
        print(result)

asyncio.run(main())
# Вывод:
# <g4f.providers.response.ImageResponse object at ...>
```

### `MissingAuthProviderMock`

**Описание**: Мок для провайдера, вызывающего исключение `MissingAuthError`.

**Принцип работы**: Этот класс имитирует провайдера, вызывающего исключение `MissingAuthError` при вызове метода `create_completion`.

**Методы**:

- `create_completion(cls, model, messages, stream, **kwargs)`:
  - **Назначение**: Создает имитацию завершения запроса, вызывая исключение `MissingAuthError`.
  - **Параметры**:
    - `cls`: Ссылка на класс.
    - `model`: Имя модели.
    - `messages`: Список сообщений.
    - `stream`: Флаг потоковой передачи.
    - `**kwargs`: Дополнительные аргументы.
  - **Вызывает исключения**:
    - `MissingAuthError`: Всегда вызывается при вызове метода.

**Примеры**:

```python
# Пример использования MissingAuthProviderMock
provider = MissingAuthProviderMock()
try:
    result = provider.create_completion(model="test_model", messages=[], stream=False)
    print(next(result))
except MissingAuthError as ex:
    print(f"Исключение: {ex}") # Вывод: Исключение: MissingAuthProviderMock
```

### `RaiseExceptionProviderMock`

**Описание**: Мок для провайдера, вызывающего исключение `RuntimeError`.

**Принцип работы**: Этот класс имитирует провайдера, вызывающего исключение `RuntimeError` при вызове метода `create_completion`.

**Методы**:

- `create_completion(cls, model, messages, stream, **kwargs)`:
  - **Назначение**: Создает имитацию завершения запроса, вызывая исключение `RuntimeError`.
  - **Параметры**:
    - `cls`: Ссылка на класс.
    - `model`: Имя модели.
    - `messages`: Список сообщений.
    - `stream`: Флаг потоковой передачи.
    - `**kwargs`: Дополнительные аргументы.
  - **Вызывает исключения**:
    - `RuntimeError`: Всегда вызывается при вызове метода.

**Примеры**:

```python
# Пример использования RaiseExceptionProviderMock
provider = RaiseExceptionProviderMock()
try:
    result = provider.create_completion(model="test_model", messages=[], stream=False)
    print(next(result))
except RuntimeError as ex:
    print(f"Исключение: {ex}") # Вывод: Исключение: RaiseExceptionProviderMock
```

### `AsyncRaiseExceptionProviderMock`

**Описание**: Мок для асинхронного генератора провайдера, вызывающего исключение `RuntimeError`.

**Принцип работы**: Этот класс имитирует асинхронного генератора провайдера, вызывающего исключение `RuntimeError` при вызове метода `create_async_generator`.

**Методы**:

- `create_async_generator(cls, model, messages, stream, **kwargs)`:
  - **Назначение**: Создает имитацию асинхронного генератора завершений запроса, вызывая исключение `RuntimeError`.
  - **Параметры**:
    - `cls`: Ссылка на класс.
    - `model`: Имя модели.
    - `messages`: Список сообщений.
    - `stream`: Флаг потоковой передачи.
    - `**kwargs`: Дополнительные аргументы.
  - **Вызывает исключения**:
    - `RuntimeError`: Всегда вызывается при вызове метода.

**Примеры**:

```python
import asyncio
# Пример использования AsyncRaiseExceptionProviderMock
async def main():
    provider = AsyncRaiseExceptionProviderMock()
    try:
        async for result in provider.create_async_generator(model="test_model", messages=[], stream=False):
            print(result)
    except RuntimeError as ex:
        print(f"Исключение: {ex}")

asyncio.run(main()) # Вывод: Исключение: AsyncRaiseExceptionProviderMock
```

### `YieldNoneProviderMock`

**Описание**: Мок для асинхронного генератора провайдера, возвращающего `None`.

**Принцип работы**: Этот класс имитирует асинхронного генератора провайдера, возвращая `None` при вызове метода `create_async_generator`.

**Методы**:

- `create_async_generator(cls, model, messages, stream, **kwargs)`:
  - **Назначение**: Создает имитацию асинхронного генератора завершений запроса, возвращая `None`.
  - **Параметры**:
    - `cls`: Ссылка на класс.
    - `model`: Имя модели.
    - `messages`: Список сообщений.
    - `stream`: Флаг потоковой передачи.
    - `**kwargs`: Дополнительные аргументы.
  - **Возвращает**: Асинхронный генератор, выдающий `None`.

**Примеры**:

```python
import asyncio
# Пример использования YieldNoneProviderMock
async def main():
    provider = YieldNoneProviderMock()
    async for result in provider.create_async_generator(model="test_model", messages=[], stream=False):
        print(result)

asyncio.run(main()) # Вывод: None
```