# Модуль для интеграции базы данных в обработчики Telegram бота
=================================================================

Модуль предоставляет middleware для работы с базой данных в Telegram боте.
Он включает классы для управления сессиями базы данных: `BaseDatabaseMiddleware`, `DatabaseMiddlewareWithoutCommit` и `DatabaseMiddlewareWithCommit`.
`BaseDatabaseMiddleware` является базовым классом, обеспечивающим создание и закрытие сессии, а также обработку исключений.
`DatabaseMiddlewareWithoutCommit` и `DatabaseMiddlewareWithCommit` являются подклассами, которые определяют, нужно ли автоматически выполнять коммит изменений в базе данных после обработки запроса.

## Обзор

Этот модуль предоставляет механизм для удобной интеграции сессий баз данных в обработчики (handlers) Telegram бота, используя middleware.
Он позволяет автоматически создавать сессию перед вызовом обработчика, передавать её в обработчик через словарь `data`,
а также автоматически выполнять коммит изменений или откат транзакции в случае ошибки.

## Подробнее

Модуль содержит три основных класса:

- `BaseDatabaseMiddleware`: Базовый класс для middleware, управляющего сессиями базы данных.
- `DatabaseMiddlewareWithoutCommit`: Middleware, который не выполняет автоматический коммит изменений в базе данных.
- `DatabaseMiddlewareWithCommit`: Middleware, который автоматически выполняет коммит изменений в базе данных после обработки запроса.

Эти классы позволяют упростить работу с базой данных в обработчиках Telegram бота, обеспечивая автоматическое управление сессиями и транзакциями.

## Классы

### `BaseDatabaseMiddleware`

**Описание**:
Базовый класс middleware для управления сессиями базы данных.
Он обеспечивает создание сессии перед вызовом обработчика, передачу её в обработчик через словарь `data`,
а также автоматическое закрытие сессии после обработки запроса.
В случае возникновения исключения во время обработки запроса, выполняется откат транзакции.

**Наследует**:
- `aiogram.BaseMiddleware`

**Атрибуты**:
- Нет

**Методы**:
- `__call__`: Основной метод middleware, вызывается для обработки каждого события.
- `set_session`: Метод для установки сессии в словарь данных. Должен быть реализован в подклассах.
- `after_handler`: Метод для выполнения действий после вызова хендлера (например, коммит).

### `DatabaseMiddlewareWithoutCommit`

**Описание**:
Middleware, который не выполняет автоматический коммит изменений в базе данных.
Сессия добавляется в `data` со ключом `session_without_commit`.

**Наследует**:
- `BaseDatabaseMiddleware`

**Атрибуты**:
- Нет

**Методы**:
- `set_session`: Устанавливает сессию в словарь `data` без автоматического коммита.

### `DatabaseMiddlewareWithCommit`

**Описание**:
Middleware, который автоматически выполняет коммит изменений в базе данных после обработки запроса.
Сессия добавляется в `data` со ключом `session_with_commit`.

**Наследует**:
- `BaseDatabaseMiddleware`

**Атрибуты**:
- Нет

**Методы**:
- `set_session`: Устанавливает сессию в словарь `data` для последующего коммита.
- `after_handler`: Выполняет коммит изменений в базе данных после обработки запроса.

## Функции

### `BaseDatabaseMiddleware.__call__`

```python
async def __call__(
    self,
    handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
    event: Message | CallbackQuery,
    data: Dict[str, Any]
) -> Any:
    """
    Асинхронный метод, вызываемый для обработки каждого события.

    Args:
        handler (Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]]): Функция-обработчик события.
        event (Message | CallbackQuery): Объект события (сообщение или callback-запрос).
        data (Dict[str, Any]): Словарь данных, передаваемый в обработчик.

    Returns:
        Any: Результат выполнения обработчика.

    Raises:
        Exception: Если во время обработки события возникает исключение.

    Как работает функция:
    1. Создает асинхронную сессию базы данных с использованием `async_session_maker`.
    2. Устанавливает сессию в словаре данных `data` с помощью метода `self.set_session`.
    3. Вызывает обработчик `handler` с событием `event` и данными `data`.
    4. После успешного выполнения обработчика вызывает метод `self.after_handler` для выполнения дополнительных действий (например, коммита).
    5. В случае возникновения исключения выполняет откат транзакции `session.rollback()`.
    6. Закрывает сессию `session.close()` в блоке `finally`, чтобы гарантировать закрытие сессии независимо от результата обработки.

    ASCII flowchart:

    Создание сессии
    ↓
    Установка сессии в data
    ↓
    Вызов обработчика
    ├──→ Успех: Вызов after_handler → Завершение
    └──→ Ошибка: Откат транзакции → Завершение

    Примеры:
    Пример использования в обработчике:
    ```python
    from aiogram import types, Dispatcher
    from aiogram.filters import CommandStart

    async def start(message: types.Message, session_with_commit):
        await message.answer("Привет! Это пример бота с middleware для работы с базой данных.")

    def register_handlers(dp: Dispatcher):
        dp.message.register(start, CommandStart())
    ```
    """
    ...
```

### `BaseDatabaseMiddleware.set_session`

```python
def set_session(self, data: Dict[str, Any], session) -> None:
    """
    Метод для установки сессии в словарь данных.

    Args:
        data (Dict[str, Any]): Словарь данных, в который нужно установить сессию.
        session: Объект сессии базы данных.

    Raises:
        NotImplementedError: Если метод не реализован в подклассе.
    """
    ...
```

### `BaseDatabaseMiddleware.after_handler`

```python
async def after_handler(self, session) -> None:
    """
    Метод для выполнения действий после вызова обработчика (например, коммит).

    Args:
        session: Объект сессии базы данных.
    """
    ...
```

### `DatabaseMiddlewareWithoutCommit.set_session`

```python
def set_session(self, data: Dict[str, Any], session) -> None:
    """
    Устанавливает сессию в словарь данных без автоматического коммита.

    Args:
        data (Dict[str, Any]): Словарь данных, в который нужно установить сессию.
        session: Объект сессии базы данных.
    """
    ...
```

### `DatabaseMiddlewareWithCommit.set_session`

```python
def set_session(self, data: Dict[str, Any], session) -> None:
    """
    Устанавливает сессию в словарь данных для последующего коммита.

    Args:
        data (Dict[str, Any]): Словарь данных, в который нужно установить сессию.
        session: Объект сессии базы данных.
    """
    ...
```

### `DatabaseMiddlewareWithCommit.after_handler`

```python
async def after_handler(self, session) -> None:
    """
    Выполняет коммит изменений в базе данных после обработки запроса.

    Args:
        session: Объект сессии базы данных.
    """
    ...