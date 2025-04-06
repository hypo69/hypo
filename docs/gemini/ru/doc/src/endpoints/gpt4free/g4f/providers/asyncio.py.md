# Модуль для асинхронных операций

## Обзор

Модуль `asyncio.py` предоставляет набор утилит для работы с асинхронностью в Python. Он содержит функции для управления event loop, преобразования асинхронных генераторов и итераторов, а также обработку ошибок, связанных с вложенными event loop. Модуль предназначен для упрощения работы с асинхронным кодом и повышения его надежности.

## Подробней

Этот модуль предоставляет функции для работы с асинхронными операциями, включая получение текущего event loop, преобразование асинхронных генераторов в списки и синхронные генераторы, а также преобразование синхронных итераторов в асинхронные. Он также включает обработку ошибок, связанных с вложенными event loop, и обеспечивает совместимость с различными реализациями event loop, такими как `uvloop`.

## Функции

### `get_running_loop`

```python
def get_running_loop(check_nested: bool) -> Optional[AbstractEventLoop]:
    """
    Возвращает текущий event loop, если он запущен.

    Args:
        check_nested (bool): Флаг, указывающий, следует ли проверять вложенность event loop.

    Returns:
        Optional[AbstractEventLoop]: Текущий event loop или `None`, если event loop не запущен.
    
    Как работает функция:
    1. Пытается получить текущий event loop с помощью `asyncio.get_running_loop()`.
    2. Если `uvloop` установлен и текущий loop является экземпляром `uvloop.Loop`, возвращает его.
    3. Если loop еще не был "патчен" (т.е. к нему не были применены исправления для поддержки вложенности), проверяет наличие `nest_asyncio`.
    4. Если `nest_asyncio` установлен, применяет его к текущему loop.
    5. Если `nest_asyncio` не установлен, но `check_nested` равен `True`, вызывает исключение `NestAsyncioError`.
    6. Если все проверки пройдены, возвращает текущий loop.
    7. Если event loop не запущен, перехватывает исключение `RuntimeError` и возвращает `None`.
    

    Блок-схема функции:

    Начало
    ↓
    Получение текущего event loop
    ↓
    Проверка uvloop
    ├─Да→ Возврат loop
    └─Нет→ Проверка nest_patched
        ├─Да→ Возврат loop
        └─Нет→ Проверка nest_asyncio
            ├─Да→ Применение nest_asyncio
            │   ↓
            │   Возврат loop
            └─Нет→ Проверка check_nested
                ├─Да→ Вызов NestAsyncioError
                └─Нет→ Возврат loop
    """
    ...
```

### `await_callback`

```python
async def await_callback(callback: Callable):
    """
    Оборачивает функцию обратного вызова для асинхронного ожидания.

    Args:
        callback (Callable): Функция обратного вызова, которую нужно выполнить.

    Returns:
        await callback(): Результат выполнения функции обратного вызова.
    """
    ...
```

### `async_generator_to_list`

```python
async def async_generator_to_list(generator: AsyncIterator) -> list:
    """
    Преобразует асинхронный генератор в список.

    Args:
        generator (AsyncIterator): Асинхронный генератор.

    Returns:
        list: Список элементов, сгенерированных асинхронным генератором.
    """
    ...
```

### `to_sync_generator`

```python
def to_sync_generator(generator: AsyncIterator, stream: bool = True) -> Iterator:
    """
    Преобразует асинхронный генератор в синхронный генератор.

    Args:
        generator (AsyncIterator): Асинхронный генератор.
        stream (bool): Если `True`, генерирует элементы по одному. Если `False`, преобразует весь генератор в список перед генерацией. По умолчанию `True`.

    Yields:
        loop.run_until_complete(await_callback(gen.__anext__)): Элементы, генерируемые асинхронным генератором.
    
    Как работает функция:
    1. Получает текущий event loop с помощью `get_running_loop(check_nested=False)`.
    2. Если `stream` равен `False`, преобразует асинхронный генератор в список с помощью `asyncio.run(async_generator_to_list(generator))` и генерирует элементы из списка.
    3. Если event loop не запущен, создает новый event loop и устанавливает его как текущий.
    4. Получает асинхронный итератор из генератора.
    5. В цикле генерирует элементы, выполняя `gen.__anext__()` в event loop с помощью `loop.run_until_complete(await_callback(gen.__anext__))`.
    6. Перехватывает исключение `StopAsyncIteration`, когда генератор завершается.
    7. Если был создан новый event loop, отменяет все задачи в loop, завершает асинхронные генераторы и закрывает loop.
    

    Блок-схема функции:

    Начало
    ↓
    Получение текущего event loop
    ↓
    Проверка stream
    ├─False→ Преобразование в список
    │   ↓
    │   Генерация из списка
    └─True→ Проверка наличия event loop
        ├─Нет→ Создание нового event loop
        │   ↓
        │   Установка нового event loop
        └─Да→ -
        ↓
        Получение асинхронного итератора
        ↓
        Цикл генерации элементов
        ↓
        Обработка StopAsyncIteration
        ↓
        Завершение и закрытие event loop (если был создан новый)
    """
    ...
```

### `to_async_iterator`

```python
async def to_async_iterator(iterator) -> AsyncIterator:
    """
    Преобразует синхронный итератор в асинхронный итератор.

    Args:
        iterator: Синхронный итератор.

    Yields:
        item: Элементы, генерируемые итератором.

    Примеры:
        Пример 1: Преобразование синхронного итератора в асинхронный

        >>> async def main():
        ...     sync_iterator = [1, 2, 3]
        ...     async_iterator = to_async_iterator(sync_iterator)
        ...     async for item in async_iterator:
        ...         print(item)
        ...
        >>> asyncio.run(main())
        1
        2
        3

        Пример 2: Преобразование корутины в асинхронный итератор

        >>> async def my_coroutine():
        ...     return "Hello"
        ...
        >>> async def main():
        ...     async_iterator = to_async_iterator(my_coroutine())
        ...     async for item in async_iterator:
        ...         print(item)
        ...
        >>> asyncio.run(main())
        Hello
    """
    ...
```