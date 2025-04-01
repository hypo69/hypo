# Модуль для интеграции баз данных в ботах Telegram
=======================================================

Модуль содержит middleware для работы с базами данных в ботах Telegram. 
Он предоставляет абстрактные классы для управления сессиями баз данных, 
автоматически открывая и закрывая сессии, а также обрабатывая коммиты и роллбеки.

Пример использования
----------------------

```python
from aiogram import Dispatcher

# Предположим, что async_session_maker уже определен

# Инициализация диспетчера
dp = Dispatcher()

# Регистрация middleware для работы с базой данных
dp.message.middleware(DatabaseMiddlewareWithCommit())
dp.callback_query.middleware(DatabaseMiddlewareWithCommit())

# Теперь в каждом обработчике можно будет получить сессию базы данных через data['session_with_commit']
```

## Обзор

Этот модуль предоставляет middleware для aiogram, который упрощает работу с базами данных, управляя сессиями и транзакциями.
Он предоставляет два основных класса: `BaseDatabaseMiddleware`, который является базовым классом для всех middleware,
и `DatabaseMiddlewareWithCommit`, который автоматически коммитит изменения в базу данных после выполнения обработчика.

## Подробнее

Модуль предназначен для упрощения интеграции баз данных в ботах Telegram, использующих библиотеку aiogram.
Он предоставляет удобный способ управления сессиями баз данных,
автоматически открывая и закрывая сессии, а также обрабатывая коммиты и роллбеки.
Это позволяет избежать boilerplate-кода и упростить разработку ботов, требующих взаимодействия с базами данных.

## Классы

### `BaseDatabaseMiddleware`

**Описание**:
Базовый класс для middleware, управляющего сессиями баз данных.

**Принцип работы**:
Этот класс является базовым для всех middleware, работающих с базами данных. Он предоставляет механизм для открытия сессии,
передачи её в обработчик и закрытия сессии после выполнения обработчика. Также он обрабатывает исключения, выполняя роллбек в случае ошибки.

**Методы**:

- `__call__(handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]], event: Message | CallbackQuery, data: Dict[str, Any]) -> Any`:
    Выполняет middleware. Открывает сессию, передает ее в обработчик, обрабатывает результат и закрывает сессию.

- `set_session(data: Dict[str, Any], session) -> None`:
    Устанавливает сессию в словарь данных. Должен быть реализован в подклассах.

- `after_handler(session) -> None`:
    Выполняет действия после вызова обработчика (например, коммит). Может быть переопределен в подклассах.

### `DatabaseMiddlewareWithoutCommit`

**Описание**:
Middleware для работы с базой данных без автоматического коммита.

**Принцип работы**:
Этот класс наследуется от `BaseDatabaseMiddleware` и предоставляет реализацию метода `set_session`,
который устанавливает сессию в словарь данных под ключом `'session_without_commit'`.
В отличие от `DatabaseMiddlewareWithCommit`, этот middleware не выполняет автоматический коммит изменений в базу данных.

**Методы**:

- `set_session(data: Dict[str, Any], session) -> None`:
    Устанавливает сессию в словарь данных под ключом `'session_without_commit'`.

### `DatabaseMiddlewareWithCommit`

**Описание**:
Middleware для работы с базой данных с автоматическим коммитом.

**Принцип работы**:
Этот класс наследуется от `BaseDatabaseMiddleware` и предоставляет реализацию методов `set_session` и `after_handler`.
Метод `set_session` устанавливает сессию в словарь данных под ключом `'session_with_commit'`,
а метод `after_handler` выполняет коммит изменений в базу данных после выполнения обработчика.

**Методы**:

- `set_session(data: Dict[str, Any], session) -> None`:
    Устанавливает сессию в словарь данных под ключом `'session_with_commit'`.

- `after_handler(session) -> None`:
    Выполняет коммит изменений в базу данных после выполнения обработчика.

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
    Выполняет middleware, оборачивая обработку события сессией базы данных.

    Args:
        handler (Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]]):
            Функция-обработчик, которая будет вызвана с событием и данными.
        event (Message | CallbackQuery):
            Событие (сообщение или callback query), которое необходимо обработать.
        data (Dict[str, Any]):
            Словарь данных, передаваемый в обработчик.

    Returns:
        Any:
            Результат выполнения обработчика.

    Raises:
        Exception:
            Если во время обработки произошла ошибка, выполняется откат транзакции.

    Как работает функция:
    1. Создает асинхронную сессию базы данных с помощью `async_session_maker()`.
    2. Устанавливает сессию в словаре `data`, используя метод `self.set_session(data, session)`.
    3. Вызывает обработчик `handler(event, data)`, передавая событие и данные.
    4. После выполнения обработчика вызывает `self.after_handler(session)` для выполнения дополнительных действий (например, коммита).
    5. В случае возникновения исключения выполняет откат транзакции `await session.rollback()` и пробрасывает исключение дальше.
    6. В блоке `finally` закрывает сессию `await session.close()`.

    ASCII flowchart:
    Начало -> Создание сессии
    Создание сессии -> Установка сессии в data
    Установка сессии в data -> Вызов обработчика
    Вызов обработчика -> После обработки
    После обработки -> Закрытие сессии
    Вызов обработчика -- Exception --> Откат транзакции -> Закрытие сессии
    Закрытие сессии -> Конец
    """
    ...
```
**Назначение**:
Обертка для обработчиков, обеспечивающая управление сессией базы данных.

**Параметры**:

- `handler` (Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]]):
    Функция-обработчик, которая будет вызвана с событием и данными.
- `event` (Message | CallbackQuery):
    Событие (сообщение или callback query), которое необходимо обработать.
- `data` (Dict[str, Any]):
    Словарь данных, передаваемый в обработчик.

**Возвращает**:

- `Any`:
    Результат выполнения обработчика.

**Вызывает исключения**:

- `Exception`:
    Если во время обработки произошла ошибка, выполняется откат транзакции.

**Примеры**:

```python
from aiogram import Dispatcher, types
from aiogram.filters import CommandStart
from bot.dao.database_middleware import DatabaseMiddlewareWithCommit

# Предположим, что async_session_maker определен и настроен

# Создаем диспетчер
dp = Dispatcher()

# Регистрируем middleware
dp.message.middleware(DatabaseMiddlewareWithCommit())
dp.callback_query.middleware(DatabaseMiddlewareWithCommit())

# Создаем обработчик команды /start
@dp.message(CommandStart())
async def start_handler(message: types.Message, data: dict):
    """
    Обработчик команды /start.

    Args:
        message (types.Message): Объект сообщения.
        data (dict): Словарь данных, содержащий сессию базы данных.
    """
    session = data['session_with_commit']  # Получаем сессию из middleware
    await message.answer("Привет! Я бот.")
```

### `BaseDatabaseMiddleware.set_session`

```python
def set_session(self, data: Dict[str, Any], session) -> None:
    """
    Метод для установки сессии в словарь данных.

    Args:
        data (Dict[str, Any]): Словарь данных, в который необходимо установить сессию.
        session: Сессия базы данных.

    Raises:
        NotImplementedError: Если метод не реализован в подклассе.
    """
    ...
```

**Назначение**:
Абстрактный метод для установки сессии базы данных в словарь данных, передаваемый в обработчик.

**Параметры**:

- `data` (Dict[str, Any]):
    Словарь данных, в который необходимо установить сессию.
- `session`:
    Сессия базы данных.

**Вызывает исключения**:

- `NotImplementedError`:
    Если метод не реализован в подклассе.

### `BaseDatabaseMiddleware.after_handler`

```python
async def after_handler(self, session) -> None:
    """
    Метод для выполнения действий после вызова обработчика (например, коммит).

    Args:
        session: Сессия базы данных.
    """
    ...
```

**Назначение**:
Метод для выполнения действий после вызова обработчика (например, коммит).

**Параметры**:

- `session`:
    Сессия базы данных.