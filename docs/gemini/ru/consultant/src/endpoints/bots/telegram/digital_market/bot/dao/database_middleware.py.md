# Анализ кода модуля `database_middleware.py`

**Качество кода**
8
- Плюсы
    - Код реализует middleware для работы с базой данных, используя асинхронные сессии SQLAlchemy.
    - Используется `async with` для управления сессиями, что обеспечивает правильное закрытие и обработку исключений.
    - Присутствует базовый класс `BaseDatabaseMiddleware` с абстрактным методом `set_session`, который должен быть реализован в подклассах.
    -  Реализованы два подкласса, `DatabaseMiddlewareWithoutCommit` и `DatabaseMiddlewareWithCommit`, которые предоставляют функциональность с коммитом и без.
- Минусы
    - Отсутствует импорт `from src.logger.logger import logger` для логирования ошибок.
    - Не хватает docstring для модуля, классов и методов.
    -  Использование `raise e` в `except` блоке может усложнить отладку, так как теряется исходный traceback.
    -   `after_handler` не имеет try-except и может вызвать проблемы если в нём будут ошибки.
    -  Нет обработки возможных ошибок в `finally` блоке.

**Рекомендации по улучшению**
1. Добавить описание модуля в начале файла.
2. Добавить docstring для всех классов и методов, в соответствии со стандартами reStructuredText.
3. Заменить `raise e` на `logger.error` и перевыбрасывать исключение, чтобы сохранить traceback.
4. Добавить обработку ошибок в `after_handler`.
5. Добавить обработку ошибок в `finally` блоке.
6.  Использовать `from src.logger.logger import logger` для логирования ошибок.

**Оптимизированный код**

```python
"""
Модуль middleware для работы с базой данных в Telegram боте.
==============================================================

Этот модуль предоставляет middleware для управления сессиями базы данных
с использованием SQLAlchemy в контексте aiogram.
Он включает базовый класс `BaseDatabaseMiddleware` и его производные классы
`DatabaseMiddlewareWithoutCommit` и `DatabaseMiddlewareWithCommit`
для обработки сессий с коммитом и без.

Пример использования
--------------------

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

# импортируем сессию для работы с бд
from bot.dao.database import async_session_maker
# импортируем logger для логирования ошибок
from src.logger.logger import logger


class BaseDatabaseMiddleware(BaseMiddleware):
    """
    Базовый класс middleware для управления сессиями базы данных.

    Предоставляет общую структуру для обработки сессий, включая открытие,
    передачу сессии в обработчик и закрытие сессии.
    """
    async def __call__(
            self,
            handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        """
        Выполняет middleware-логику для управления сессией БД.

        Args:
            handler (Callable): Функция-обработчик, вызываемая после middleware.
            event (Message | CallbackQuery): Событие, которое вызвало обработчик.
            data (Dict[str, Any]): Словарь данных, передаваемый между middleware и обработчиком.

        Returns:
            Any: Результат выполнения обработчика.
        """
        try:
            # код исполняет открытие сессии
            async with async_session_maker() as session:
                # код исполняет установку сессии
                self.set_session(data, session)
                try:
                    # код исполняет вызов обработчика и передачу ему сессии
                    result = await handler(event, data)
                    # код исполняет действия после вызова обработчика
                    await self.after_handler(session)
                    return result
                except Exception as e:
                     #  код исполняет откат сессии в случае ошибки
                    await session.rollback()
                    logger.error('Ошибка при выполнении обработчика', exc_info=True)
                    raise e
        except Exception as ex:
            logger.error('Ошибка при работе с сессией', exc_info=True)
            raise ex
        finally:
           try:
               # код исполняет закрытие сессии
                await session.close()
           except Exception as ex:
               logger.error('Ошибка при закрытии сессии', exc_info=True)


    def set_session(self, data: Dict[str, Any], session) -> None:
        """
        Устанавливает сессию в словарь данных.

        Args:
            data (Dict[str, Any]): Словарь данных, в который нужно установить сессию.
            session: Сессия базы данных.

        Raises:
            NotImplementedError: Если метод не реализован в подклассе.
        """
        raise NotImplementedError('Этот метод должен быть реализован в подклассах.')

    async def after_handler(self, session) -> None:
        """
        Выполняет действия после вызова обработчика.
        Args:
            session: Сессия базы данных.
        """
        # Метод для выполнения действий после вызова хендлера (например, коммит).
        pass


class DatabaseMiddlewareWithoutCommit(BaseDatabaseMiddleware):
    """
    Middleware для работы с базой данных без коммита.

    Устанавливает сессию без коммита в словарь данных.
    """
    def set_session(self, data: Dict[str, Any], session) -> None:
        """
        Устанавливает сессию в словарь данных.

        Args:
            data (Dict[str, Any]): Словарь данных, в который нужно установить сессию.
            session: Сессия базы данных.
        """
        #  код устанавливает сессию в словарь данных без коммита
        data['session_without_commit'] = session


class DatabaseMiddlewareWithCommit(BaseDatabaseMiddleware):
    """
    Middleware для работы с базой данных с коммитом.

    Устанавливает сессию с коммитом в словарь данных.
    """
    def set_session(self, data: Dict[str, Any], session) -> None:
        """
        Устанавливает сессию в словарь данных.

        Args:
            data (Dict[str, Any]): Словарь данных, в который нужно установить сессию.
            session: Сессия базы данных.
        """
        # код устанавливает сессию в словарь данных c коммитом
        data['session_with_commit'] = session

    async def after_handler(self, session) -> None:
        """
        Выполняет коммит сессии после выполнения обработчика.
        Args:
           session: Сессия базы данных.
        """
        try:
            # код исполняет коммит сессии
            await session.commit()
        except Exception as ex:
            # код исполняет откат сессии в случае ошибки
            await session.rollback()
            logger.error('Ошибка при коммите сессии', exc_info=True)
            raise ex
```