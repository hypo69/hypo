# Модуль для работы с асинхронностью

## Обзор

Модуль предоставляет утилиты для работы с асинхронным кодом, включая получение текущего event loop, преобразование асинхронных генераторов и итераторов. Он также включает обработку ошибок, связанных с вложенными event loop.

## Подробней

Этот модуль содержит функции для облегчения работы с асинхронным кодом, особенно в контексте, где требуется совместимость с синхронным кодом или обработка вложенных асинхронных задач.

## Функции

### `get_running_loop`

```python
def get_running_loop(check_nested: bool) -> Optional[AbstractEventLoop]:
    """
    Возвращает текущий event loop, при необходимости применяя патч для поддержки вложенности.

    Args:
        check_nested (bool): Флаг, указывающий, следует ли проверять необходимость применения патча для вложенности.

    Returns:
        Optional[AbstractEventLoop]: Текущий event loop или None, если event loop не запущен.

    Raises:
        NestAsyncioError: Если `check_nested` равен `True`, и требуется установка пакета `nest_asyncio`.
    """
```

**Как работает функция**:

1. Пытается получить текущий event loop с помощью `asyncio.get_running_loop()`.
2. Если `uvloop` установлен, проверяет, является ли текущий event loop экземпляром `uvloop.Loop`. Если да, возвращает его. Патчить `uvloop` не нужно, так как он несовместим с `nest_asyncio`.
3. Проверяет, был ли уже применен патч для поддержки вложенности (`_nest_patched`).
4. Если патч еще не был применен, и `nest_asyncio` установлен, применяет патч.
5. Если `nest_asyncio` не установлен, и `check_nested` равен `True`, выбрасывает исключение `NestAsyncioError`.
6. Если event loop не запущен, возвращает `None`.

**Примеры**:

```python
loop = get_running_loop(check_nested=True)
if loop:
    print("Event loop получен")
else:
    print("Event loop не запущен")
```

### `await_callback`

```python
async def await_callback(callback: Callable):
    """
    Асинхронно ожидает выполнения переданной функции обратного вызова.

    Args:
        callback (Callable): Функция обратного вызова для асинхронного выполнения.

    Returns:
        await callback(): Результат выполнения функции обратного вызова.
    """
```

**Как работает функция**:

1. Асинхронно вызывает переданную функцию обратного вызова и возвращает результат.

**Примеры**:

```python
import asyncio

async def my_callback():
    await asyncio.sleep(1)
    return "Callback выполнена"

async def main():
    result = await await_callback(my_callback)
    print(result)  # Выводит: Callback выполнена

asyncio.run(main())
```

### `async_generator_to_list`

```python
async def async_generator_to_list(generator: AsyncIterator) -> list:
    """
    Преобразует асинхронный генератор в список.

    Args:
        generator (AsyncIterator): Асинхронный генератор.

    Returns:
        list: Список, содержащий элементы, сгенерированные асинхронным генератором.
    """
```

**Как работает функция**:

1. Итерируется по асинхронному генератору и собирает все элементы в список.
2. Возвращает полученный список.

**Примеры**:

```python
async def my_generator():
    for i in range(3):
        await asyncio.sleep(0.1)
        yield i

async def main():
    result = await async_generator_to_list(my_generator())
    print(result)  # Выводит: [0, 1, 2]

asyncio.run(main())
```

### `to_sync_generator`

```python
def to_sync_generator(generator: AsyncIterator, stream: bool = True) -> Iterator:
    """
    Преобразует асинхронный генератор в синхронный генератор.

    Args:
        generator (AsyncIterator): Асинхронный генератор.
        stream (bool): Если `True`, элементы генерируются по одному. Если `False`, генератор полностью преобразуется в список перед возвратом.

    Yields:
        Any: Элементы, сгенерированные асинхронным генератором.
    """
```

**Как работает функция**:

1. Получает текущий event loop с помощью `get_running_loop()`.
2. Если event loop не запущен, создает новый event loop и устанавливает его в качестве текущего.
3. Итерируется по асинхронному генератору, выполняя каждый шаг в event loop.
4. Если `stream` равен `True`, возвращает элементы по одному.
5. Если `stream` равен `False`, преобразует весь генератор в список и возвращает элементы из списка.
6. После завершения генерации, если был создан новый event loop, закрывает его.

**Внутренние функции**:
- Отсутствуют

**Примеры**:

```python
import asyncio

async def my_generator():
    for i in range(3):
        await asyncio.sleep(0.1)
        yield i

def main():
    sync_generator = to_sync_generator(my_generator())
    for item in sync_generator:
        print(item)  # Выводит: 0, 1, 2

main()
```

### `to_async_iterator`

```python
async def to_async_iterator(iterator) -> AsyncIterator:
    """
    Преобразует синхронный итератор или корутину в асинхронный итератор.

    Args:
        iterator: Синхронный итератор или корутина.

    Yields:
        Any: Элементы, предоставляемые итератором.
    """
```

**Как работает функция**:

1. Проверяет, является ли итератор асинхронным итератором (`__aiter__`).
2. Если да, итерируется по нему и возвращает элементы.
3. Если итератор является корутиной, ожидает ее выполнения и возвращает результат.
4. Если итератор является синхронным, итерируется по нему и возвращает элементы.

**Примеры**:

```python
import asyncio

async def main():
    async def async_gen():
        for i in range(3):
            yield i

    async def async_func():
        return "Async result"

    def sync_gen():
        for i in range(3):
            yield i

    async def process_iterator(iterator):
        async for item in to_async_iterator(iterator):
            print(item)

    print("Асинхронный генератор:")
    await process_iterator(async_gen())  # Выводит: 0, 1, 2

    print("Асинхронная функция:")
    await process_iterator(async_func())  # Выводит: Async result

    print("Синхронный генератор:")
    await process_iterator(sync_gen())  # Выводит: 0, 1, 2

asyncio.run(main())
```