# Модуль для работы с базой данных в Telegram боте (middleware)

## Обзор

Модуль предоставляет middleware для интеграции базы данных в обработчики Telegram бота. Он содержит базовый класс `BaseDatabaseMiddleware` и два его подкласса: `DatabaseMiddlewareWithoutCommit` и `DatabaseMiddlewareWithCommit`. Эти middleware обеспечивают управление сессиями базы данных, автоматический коммит или роллбек транзакций, а также обработку исключений.

## Подробней

Этот модуль предназначен для упрощения работы с базой данных в асинхронных обработчиках Telegram бота. Он использует `async_session_maker` из модуля `bot.dao.database` для создания асинхронных сессий базы данных. Основная задача - предоставить сессию базы данных в обработчик и автоматически выполнить коммит или роллбек транзакции после завершения работы обработчика.

## Классы

### `BaseDatabaseMiddleware`

**Описание**: Базовый класс middleware для работы с базой данных. Обеспечивает создание сессии, передачу ее в обработчик, а также обработку результатов и исключений.

**Методы**:

- `__call__(handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]], event: Message | CallbackQuery, data: Dict[str, Any]) -> Any`
- `set_session(data: Dict[str, Any], session) -> None`
- `after_handler(session) -> None`

#### `__call__`

```python
async def __call__(
    self,
    handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
    event: Message | CallbackQuery,
    data: Dict[str, Any]
) -> Any:
    """
    Выполняет middleware.

    Args:
        handler (Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]]):
            Функция-обработчик, которая будет вызвана после middleware.
        event (Message | CallbackQuery):
            Объект события (сообщение или callback query) от Telegram.
        data (Dict[str, Any]):
            Словарь с данными, передаваемыми между middleware и обработчиком.

    Returns:
        Any: Результат выполнения обработчика.

    Raises:
        Exception: Если во время выполнения обработчика или коммита возникает исключение, выполняется откат транзакции.

    Как работает функция:
    1. Создается асинхронная сессия базы данных с помощью `async_session_maker()`.
    2. Вызывается метод `set_session` для установки сессии в словаре `data`.
    3. Вызывается обработчик `handler` с передачей события и данных.
    4. После успешного выполнения обработчика вызывается метод `after_handler` для выполнения дополнительных действий (например, коммита).
    5. В случае возникновения исключения выполняется откат транзакции (`session.rollback()`).
    6. Вне зависимости от результата, сессия закрывается (`session.close()`).

    ASCII flowchart:

    Создание сессии
    ↓
    Установка сессии
    ↓
    Вызов обработчика
    ↓
    Успех? --→ Вызов after_handler → Коммит (если необходимо)
    ↓       
    Ошибка --→ Откат транзакции
    ↓
    Закрытие сессии

    Примеры:
    # Пример использования в aiogram:
    dp.message.middleware(BaseDatabaseMiddleware())
    """
```

#### `set_session`

```python
def set_session(self, data: Dict[str, Any], session) -> None:
    """
    Устанавливает сессию в словарь данных.

    Args:
        data (Dict[str, Any]): Словарь данных, в который будет установлена сессия.
        session: Объект сессии базы данных.

    Raises:
        NotImplementedError: Если метод не переопределен в подклассе.

    Как работает функция:
    1. Генерирует исключение `NotImplementedError`, указывая, что метод должен быть реализован в подклассах.

    ASCII flowchart:

    Вызов метода
    ↓
    Генерация NotImplementedError

    Примеры:
    # Пример переопределения в подклассе:
    class MyDatabaseMiddleware(BaseDatabaseMiddleware):
        def set_session(self, data: Dict[str, Any], session) -> None:
            data['db_session'] = session
    """
```

#### `after_handler`

```python
async def after_handler(self, session) -> None:
    """
    Выполняет действия после вызова хендлера (например, коммит).

    Args:
        session: Объект сессии базы данных.

    Как работает функция:
    1. Ничего не делает, просто пропускает выполнение. Этот метод предназначен для переопределения в подклассах для выполнения специфичных действий, таких как коммит транзакции.

    ASCII flowchart:

    Вызов метода
    ↓
    Пропуск выполнения

    Примеры:
    # Пример переопределения в подклассе:
    class MyDatabaseMiddleware(BaseDatabaseMiddleware):
        async def after_handler(self, session) -> None:
            await session.commit()
    """
```

### `DatabaseMiddlewareWithoutCommit`

**Описание**: Middleware для работы с базой данных без автоматического коммита.

**Наследует**: `BaseDatabaseMiddleware`

**Методы**:
- `set_session(data: Dict[str, Any], session) -> None`

#### `set_session`

```python
def set_session(self, data: Dict[str, Any], session) -> None:
    """
    Устанавливает сессию в словарь данных без коммита.

    Args:
        data (Dict[str, Any]): Словарь данных, в который будет установлена сессия.
        session: Объект сессии базы данных.

    Как работает функция:
    1. Устанавливает сессию в словаре `data` под ключом `'session_without_commit'`.

    ASCII flowchart:

    Вызов метода
    ↓
    Установка сессии в data['session_without_commit']

    Примеры:
    # Пример использования:
    middleware = DatabaseMiddlewareWithoutCommit()
    middleware.set_session(data, session)
    """
```

### `DatabaseMiddlewareWithCommit`

**Описание**: Middleware для работы с базой данных с автоматическим коммитом после выполнения обработчика.

**Наследует**: `BaseDatabaseMiddleware`

**Методы**:
- `set_session(data: Dict[str, Any], session) -> None`
- `after_handler(session) -> None`

#### `set_session`

```python
def set_session(self, data: Dict[str, Any], session) -> None:
    """
    Устанавливает сессию в словарь данных с автоматическим коммитом.

    Args:
        data (Dict[str, Any]): Словарь данных, в который будет установлена сессия.
        session: Объект сессии базы данных.

    Как работает функция:
    1. Устанавливает сессию в словаре `data` под ключом `'session_with_commit'`.

    ASCII flowchart:

    Вызов метода
    ↓
    Установка сессии в data['session_with_commit']

    Примеры:
    # Пример использования:
    middleware = DatabaseMiddlewareWithCommit()
    middleware.set_session(data, session)
    """
```

#### `after_handler`

```python
async def after_handler(self, session) -> None:
    """
    Выполняет коммит сессии после вызова обработчика.

    Args:
        session: Объект сессии базы данных.

    Как работает функция:
    1. Выполняет коммит транзакции (`session.commit()`).

    ASCII flowchart:

    Вызов метода
    ↓
    Коммит транзакции

    Примеры:
    # Пример использования:
    middleware = DatabaseMiddlewareWithCommit()
    await middleware.after_handler(session)
    """
```

## Функции

В данном модуле нет отдельных функций, не входящих в классы.