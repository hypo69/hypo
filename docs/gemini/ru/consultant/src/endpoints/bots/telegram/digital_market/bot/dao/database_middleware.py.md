# Анализ кода модуля `database_middleware`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Использование асинхронного контекстного менеджера для работы с сессией БД.
    - Наличие базового класса `BaseDatabaseMiddleware` для повторного использования логики.
    - Разделение middleware с коммитом и без него.
- **Минусы**:
    - Отсутствие документации в формате RST для классов и методов.
    - Не используется `logger` для логирования ошибок.
    - Общий `try-except` блок с `raise e` может затруднить отслеживание ошибок.
    - Использование одинарных кавычек для ключей словаря не соответствует стандарту.
    - Нет выравнивания для названий функций, переменных и импортов.

**Рекомендации по улучшению:**

1. Добавить RST-документацию для классов и методов.
2. Использовать `logger` для логирования ошибок вместо `raise e`.
3. Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` при работе с JSON, если это необходимо.
4. Использовать одинарные кавычки для строковых литералов в Python.
5. Выровнять названия функций, переменных и импортов.
6. Избегать чрезмерного использования `try-except`.

**Оптимизированный код:**

```python
"""
Модуль для middleware работы с базой данных.
==================================================

Этот модуль предоставляет middleware для работы с базой данных,
включая управление сессиями и транзакциями.

Пример использования
----------------------
.. code-block:: python

    from aiogram import Dispatcher
    from bot.dao.database_middleware import DatabaseMiddlewareWithCommit, DatabaseMiddlewareWithoutCommit

    dp = Dispatcher()
    dp.middleware.setup(DatabaseMiddlewareWithCommit())
    dp.middleware.setup(DatabaseMiddlewareWithoutCommit())
"""
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from bot.dao.database import async_session_maker
from src.logger import logger  # corrected import

class BaseDatabaseMiddleware(BaseMiddleware):
    """
    Базовый класс middleware для работы с базой данных.

    Этот класс обеспечивает общую логику для создания сессии,
    выполнения действий до и после вызова хендлера, а также
    обработку ошибок.
    """
    async def __call__(
            self,
            handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        """
        Выполняет middleware для работы с базой данных.

        :param handler: Функция-handler, которую необходимо вызвать.
        :type handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]]
        :param event: Событие, которое вызвало handler.
        :type event: Message | CallbackQuery
        :param data: Словарь с данными.
        :type data: Dict[str, Any]
        :return: Результат работы handler.
        :rtype: Any
        """
        async with async_session_maker() as session:
            self.set_session(data, session)
            try:
                result = await handler(event, data)
                await self.after_handler(session)
                return result
            except Exception as e:
                await session.rollback()
                logger.error(f'Error during database operation: {e}') # Changed from `raise e` to `logger.error`
                return None # added return None to prevent further errors
            finally:
                await session.close()

    def set_session(self, data: Dict[str, Any], session) -> None:
        """
        Устанавливает сессию в словарь данных.

        :param data: Словарь с данными.
        :type data: Dict[str, Any]
        :param session: Сессия базы данных.
        :type session: Any
        :raises NotImplementedError: Если метод не реализован в подклассе.
        """
        raise NotImplementedError('Этот метод должен быть реализован в подклассах.')

    async def after_handler(self, session) -> None:
        """
        Метод для выполнения действий после вызова хендлера (например, коммит).

        :param session: Сессия базы данных.
        :type session: Any
        """
        pass


class DatabaseMiddlewareWithoutCommit(BaseDatabaseMiddleware):
    """
    Middleware для работы с базой данных без коммита.

    Этот middleware устанавливает сессию в данные,
    но не выполняет коммит изменений.
    """
    def set_session(self, data: Dict[str, Any], session) -> None:
        """
        Устанавливает сессию в словарь данных без коммита.

        :param data: Словарь с данными.
        :type data: Dict[str, Any]
        :param session: Сессия базы данных.
        :type session: Any
        """
        data['session_without_commit'] = session


class DatabaseMiddlewareWithCommit(BaseDatabaseMiddleware):
    """
    Middleware для работы с базой данных с коммитом.

    Этот middleware устанавливает сессию в данные и
    выполняет коммит изменений после выполнения хендлера.
    """
    def set_session(self, data: Dict[str, Any], session) -> None:
        """
        Устанавливает сессию в словарь данных для коммита.

        :param data: Словарь с данными.
        :type data: Dict[str, Any]
        :param session: Сессия базы данных.
        :type session: Any
        """
        data['session_with_commit'] = session

    async def after_handler(self, session) -> None:
        """
        Выполняет коммит изменений после выполнения хендлера.

        :param session: Сессия базы данных.
        :type session: Any
        """
        await session.commit()
```