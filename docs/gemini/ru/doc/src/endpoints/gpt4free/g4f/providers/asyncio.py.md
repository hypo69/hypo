# Модуль asyncio

## Обзор

Модуль предоставляет асинхронные утилиты, необходимые для работы с провайдерами, использующими асинхронный ввод-вывод. Он включает в себя функции для получения текущего event loop, преобразования асинхронных генераторов в списки и синхронные генераторы, а также для конвертации синхронных итераторов в асинхронные.

## Подробней

Этот модуль содержит функции для упрощения работы с асинхронным кодом, особенно в контексте интеграции с библиотеками, которые могут быть как синхронными, так и асинхронными. Он обеспечивает совместимость и упрощает обработку асинхронных генераторов и итераторов.
В проекте этот модуль используется для асинхронной работы с различными поставщиками API, такими как GPT-4, обеспечивая неблокирующие операции.

## Функции

### `get_running_loop`

```python
def get_running_loop(check_nested: bool) -> Optional[AbstractEventLoop]:
    """
    Возвращает текущий event loop. При необходимости применяет патч nest_asyncio для поддержки вложенных event loop.

    Args:
        check_nested (bool): Флаг, указывающий, нужно ли проверять поддержку вложенности.

    Returns:
        Optional[AbstractEventLoop]: Текущий event loop или None, если event loop не запущен.

    Raises:
        NestAsyncioError: Если `check_nested` установлен в True, `nest_asyncio` не установлен, и обнаружена попытка запуска вложенного event loop.

    Как работает функция:
     1. Пытается получить текущий запущенный event loop с помощью `asyncio.get_running_loop()`.
     2. Проверяет, используется ли `uvloop`. Если да, и если текущий loop является экземпляром `uvloop.Loop`, возвращает его без применения патчей.
     3. Если `nest_asyncio` не был применен к текущему loop, применяет его, если `has_nest_asyncio` True, иначе выбрасывает исключение `NestAsyncioError`, если `check_nested` True.
     4. Возвращает текущий event loop.
     5. Если event loop не запущен, возвращает `None`.

    A - Попытка получить текущий event loop
    |
    B - Проверка на использование uvloop
    |
    C - Проверка на применение nest_asyncio
    |
    D - Возврат event loop

    Примеры:
        >>> loop = get_running_loop(check_nested=False)
        >>> if loop:
        ...     print("Event loop получен")
    """
```

### `await_callback`

```python
async def await_callback(callback: Callable):
    """
    Оборачивает функцию обратного вызова в корутину и ожидает ее выполнения.

    Args:
        callback (Callable): Функция обратного вызова для выполнения.

    Returns:
        любое: Результат выполнения функции обратного вызова.

    Как работает функция:
    1. Преобразует переданную функцию обратного вызова в корутину.
    2. Ожидает выполнения корутины и возвращает результат.

    A - Преобразование callback в корутину
    |
    B - Ожидание выполнения корутины
    |
    C - Возврат результата

    Примеры:
        >>> async def my_callback():
        ...     return "Hello"
        >>> result = await await_callback(my_callback)
        >>> print(result)
        Hello
    """
```

### `async_generator_to_list`

```python
async def async_generator_to_list(generator: AsyncIterator) -> list:
    """
    Преобразует асинхронный генератор в список.

    Args:
        generator (AsyncIterator): Асинхронный генератор.

    Returns:
        list: Список, содержащий все элементы, сгенерированные асинхронным генератором.

    Как работает функция:
    1. Использует асинхронное включение списка для итерации по асинхронному генератору.
    2. Собирает все элементы, возвращаемые генератором, в список.

    A - Итерация по асинхронному генератору
    |
    B - Сбор элементов в список
    |
    C - Возврат списка

    Примеры:
        >>> async def my_generator():
        ...     yield 1
        ...     yield 2
        >>> result = await async_generator_to_list(my_generator())
        >>> print(result)
        [1, 2]
    """
```

### `to_sync_generator`

```python
def to_sync_generator(generator: AsyncIterator, stream: bool = True) -> Iterator:
    """
    Преобразует асинхронный генератор в синхронный генератор.

    Args:
        generator (AsyncIterator): Асинхронный генератор для преобразования.
        stream (bool, optional): Если True, возвращает элементы по мере их генерации. Если False, ожидает завершения генератора и возвращает все элементы сразу. По умолчанию True.

    Returns:
        Iterator: Синхронный генератор, выдающий элементы из асинхронного генератора.

    Как работает функция:
    1. Получает текущий event loop с помощью `get_running_loop(check_nested=False)`.
    2. Если `stream` установлен в False, запускает асинхронный генератор до завершения с помощью `asyncio.run(async_generator_to_list(generator))` и возвращает элементы списком.
    3. Если event loop не существует, создает новый event loop и устанавливает его как текущий.
    4. Итерируется по асинхронному генератору, используя `loop.run_until_complete(await_callback(gen.__anext__))` для получения каждого элемента.
    5. Перехватывает исключение `StopAsyncIteration`, когда асинхронный генератор завершается.
    6. Если был создан новый event loop, завершает все задачи, асинхронные генераторы и executor, а затем закрывает loop.

    A - Получение текущего event loop
    |
    B - Проверка значения stream
    |
    C - Создание нового event loop (если необходимо)
    |
    D - Итерация по асинхронному генератору
    |
    E - Завершение работы с event loop (если он был создан)

    Примеры:
        >>> async def my_generator():
        ...     yield 1
        ...     yield 2
        >>> sync_generator = to_sync_generator(my_generator())
        >>> for item in sync_generator:
        ...     print(item)
        1
        2
    """
```

### `to_async_iterator`

```python
async def to_async_iterator(iterator) -> AsyncIterator:
    """
    Преобразует синхронный итератор, асинхронный итератор или корутину в асинхронный итератор.

    Args:
        iterator (iterator): Синхронный итератор, асинхронный итератор или корутина.

    Yields:
        AsyncIterator: Асинхронный итератор.

    Как работает функция:
    1. Проверяет, является ли входной итератор асинхронным итератором (с помощью `hasattr(iterator, '__aiter__')`).
    2. Если это асинхронный итератор, итерируется по нему и выдает элементы.
    3. Если это корутина (с помощью `asyncio.iscoroutine(iterator)`), ожидает ее выполнения и выдает результат.
    4. Если это синхронный итератор, итерируется по нему и выдает элементы.

    A - Проверка на асинхронный итератор
    |
    B - Проверка на корутину
    |
    C - Итерация по итератору и выдача элементов

    Примеры:
        >>> async def my_async_generator():
        ...     yield 1
        ...     yield 2
        >>> async def print_async_iterator(iterator):
        ...     async for item in iterator:
        ...         print(item)
        >>> await print_async_iterator(to_async_iterator(my_async_generator()))
        1
        2
    """