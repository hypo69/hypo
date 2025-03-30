# Модуль middleware для работы с базой данных в Telegram боте

## Обзор

Этот модуль содержит middleware для интеграции базы данных в обработчики Telegram бота. Он предоставляет базовый класс `BaseDatabaseMiddleware` и два его подкласса: `DatabaseMiddlewareWithoutCommit` и `DatabaseMiddlewareWithCommit`. Middleware обеспечивает управление сессиями базы данных, автоматический коммит или откат транзакций, а также обработку исключений.

## Подробней

Этот код играет важную роль в обеспечении доступа к базе данных в обработчиках сообщений и колбэков Telegram бота. `BaseDatabaseMiddleware` служит основой для создания middleware, которые управляют сессиями базы данных. Подклассы `DatabaseMiddlewareWithoutCommit` и `DatabaseMiddlewareWithCommit` предоставляют различные стратегии управления транзакциями. Этот подход позволяет упростить взаимодействие с базой данных, автоматизировать управление сессиями и обеспечить консистентность данных.

## Классы

### `BaseDatabaseMiddleware`

**Описание**: Базовый класс middleware для работы с базой данных. Обеспечивает создание сессии, передачу её в обработчик, а также обработку исключений и закрытие сессии.

**Методы**:
- `__call__`: Выполняет middleware, создаёт сессию, вызывает обработчик, обрабатывает исключения и закрывает сессию.
- `set_session`: Метод для установки сессии в словарь данных (должен быть реализован в подклассах).
- `after_handler`: Метод для выполнения действий после вызова хендлера (например, коммит).

**Параметры**:
- Нет параметров для конструктора класса.

**Примеры**

```python
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from typing import Callable, Dict, Any, Awaitable

class BaseDatabaseMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        async with async_session_maker() as session:
            self.set_session(data, session)
            try:
                result = await handler(event, data)
                await self.after_handler(session)
                return result
            except Exception as e:
                await session.rollback()
                raise e
            finally:
                await session.close()

    def set_session(self, data: Dict[str, Any], session) -> None:
        """Метод для установки сессии в словарь данных."""
        raise NotImplementedError("Этот метод должен быть реализован в подклассах.")

    async def after_handler(self, session) -> None:
        """Метод для выполнения действий после вызова хендлера (например, коммит)."""
        pass
```

### `DatabaseMiddlewareWithoutCommit`

**Описание**: Middleware для работы с базой данных без автоматического коммита.

**Методы**:
- `set_session`: Устанавливает сессию в словарь данных под ключом `session_without_commit`.

**Параметры**:
  - Нет параметров для конструктора класса.

**Примеры**

```python
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from typing import Callable, Dict, Any, Awaitable

class DatabaseMiddlewareWithoutCommit(BaseDatabaseMiddleware):
    def set_session(self, data: Dict[str, Any], session) -> None:
        data['session_without_commit'] = session
```

### `DatabaseMiddlewareWithCommit`

**Описание**: Middleware для работы с базой данных с автоматическим коммитом после выполнения обработчика.

**Методы**:
- `set_session`: Устанавливает сессию в словарь данных под ключом `session_with_commit`.
- `after_handler`: Выполняет коммит сессии после вызова обработчика.

**Параметры**:
  - Нет параметров для конструктора класса.

**Примеры**

```python
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from typing import Callable, Dict, Any, Awaitable

class DatabaseMiddlewareWithCommit(BaseDatabaseMiddleware):
    def set_session(self, data: Dict[str, Any], session) -> None:
        data['session_with_commit'] = session

    async def after_handler(self, session) -> None:
        await session.commit()
```

## Функции

### `__call__`

```python
    async def __call__(
            self,
            handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        """
        Args:
            handler (Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]]): Обработчик события.
            event (Message | CallbackQuery): Объект события (сообщение или колбэк).
            data (Dict[str, Any]): Словарь данных.

        Returns:
            Any: Результат выполнения обработчика.

        Raises:
            Exception: Если во время обработки возникла ошибка, выполняется откат транзакции и исключение перевыбрасывается.
        """
        ...
```

**Описание**: Выполняет middleware, создаёт сессию базы данных, передаёт её в обработчик, обрабатывает исключения и закрывает сессию.

**Параметры**:
- `handler` (Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]]): Обработчик события.
- `event` (Message | CallbackQuery): Объект события (сообщение или колбэк).
- `data` (Dict[str, Any]): Словарь данных.

**Возвращает**:
- `Any`: Результат выполнения обработчика.

**Вызывает исключения**:
- `Exception`: Если во время обработки возникла ошибка, выполняется откат транзакции и исключение перевыбрасывается.

**Примеры**:
```python
# Пример использования __call__ в контексте aiogram
from aiogram import Dispatcher, types
from aiogram.filters import CommandStart

async def my_handler(message: types.Message, data: dict):
    session = data['session_with_commit']  # Или 'session_without_commit' в другом middleware
    # ... работа с базой данных через session ...
    await message.answer("Hello!")

async def main():
    dp = Dispatcher()
    dp.message.register(my_handler, CommandStart())

    # Подключение middleware происходит при регистрации Dispatcher
    # dp.middleware.setup(DatabaseMiddlewareWithCommit())
```

### `set_session`

```python
    def set_session(self, data: Dict[str, Any], session) -> None:
        """Метод для установки сессии в словарь данных."""
        raise NotImplementedError("Этот метод должен быть реализован в подклассах.")
```

**Описание**: Метод для установки сессии базы данных в словарь данных. Должен быть реализован в подклассах.

**Параметры**:
- `data` (Dict[str, Any]): Словарь данных.
- `session`: Сессия базы данных.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `NotImplementedError`: Если метод не реализован в подклассе.

### `after_handler`

```python
    async def after_handler(self, session) -> None:
        """Метод для выполнения действий после вызова хендлера (например, коммит)."""
        pass
```

**Описание**: Метод для выполнения действий после вызова обработчика (например, коммит транзакции).

**Параметры**:
- `session`: Сессия базы данных.

**Возвращает**:
- `None`