# Модуль `throttling`

## Обзор

Модуль `throttling.py` реализует middleware для aiogram, предназначенный для ограничения частоты запросов от пользователей в Telegram-боте. Он использует `TTLCache` из библиотеки `cachetools` для хранения идентификаторов чатов и временных меток, чтобы предотвратить слишком частые запросы.

## Оглавление

- [Классы](#классы)
    - [`ThrottlingMiddleware`](#throttlingmiddleware)
- [Функции](#функции)
    - [`__call__`](#__call__)

## Классы

### `ThrottlingMiddleware`

**Описание**: Middleware для ограничения частоты запросов от пользователей.

**Методы**:
- `__init__`: Инициализация middleware.
- `__call__`: Обработчик middleware.

#### `__init__`

```python
def __init__(self, time_limit: int = 2) -> None:
    """
    Args:
        time_limit (int, optional): Время в секундах, в течение которого разрешен только один запрос от пользователя. По умолчанию `2`.
    
    Returns:
        None
    
    Raises:
        None
    """
```
**Описание**: Инициализирует `ThrottlingMiddleware` с заданным временем ограничения.

**Параметры**:
- `time_limit` (int, optional): Время в секундах, в течение которого разрешен только один запрос от пользователя. По умолчанию `2`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

## Функции

### `__call__`

```python
async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
) -> Any:
    """
    Args:
        handler (Callable[[Message, Dict[str, Any]], Awaitable[Any]]): Обработчик запроса.
        event (Message): Событие сообщения.
        data (Dict[str, Any]): Дополнительные данные.

    Returns:
        Any: Результат работы обработчика.

    Raises:
        None
    """
```

**Описание**: Обрабатывает входящие сообщения, проверяя, не превысил ли пользователь лимит запросов. Если лимит не превышен, то запрос обрабатывается дальше, иначе игнорируется.

**Параметры**:
- `handler` (Callable[[Message, Dict[str, Any]], Awaitable[Any]]): Обработчик запроса.
- `event` (Message): Событие сообщения.
- `data` (Dict[str, Any]): Дополнительные данные.

**Возвращает**:
- `Any`: Результат работы обработчика.

**Вызывает исключения**:
- Отсутствуют