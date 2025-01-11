# Анализ кода модуля `throttling`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и выполняет поставленную задачу.
    - Использует `TTLCache` для реализации троттлинга, что является эффективным решением.
    - Код достаточно читаемый и понятный.
- Минусы
    - Отсутствует docstring для модуля и класса.
    - Нет логирования ошибок.
    - Нет обработки возможных исключений.
    - Отсутствуют комментарии для функций и методов.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля, класса и методов для лучшей документации кода.
2.  Использовать `logger.error` для логирования ошибок.
3.  Добавить try-except блок для обработки исключений.
4.  Добавить комментарии, объясняющие логику работы кода.

**Оптимизированный код**

```python
"""
Модуль для реализации троттлинга сообщений в Telegram боте.
=============================================================

Этот модуль содержит класс :class:`ThrottlingMiddleware`, который используется для ограничения частоты
отправки сообщений от пользователей, чтобы избежать перегрузки бота.

Пример использования
--------------------

Пример использования класса `ThrottlingMiddleware`:

.. code-block:: python

    from aiogram import Dispatcher
    from aiogram.types import Message
    from middlewares.throttling import ThrottlingMiddleware

    dp = Dispatcher()
    dp.message.middleware(ThrottlingMiddleware(time_limit=2))

    @dp.message()
    async def handle_message(message: Message):
        await message.answer('Сообщение получено!')

"""
from typing import Any, Awaitable, Callable, Dict
# Импорт модуля logger
from src.logger.logger import logger
from aiogram import BaseMiddleware
from aiogram.types import Message

from cachetools import TTLCache


class ThrottlingMiddleware(BaseMiddleware):
    """
    Мидлварь для ограничения частоты запросов от одного пользователя.

    Args:
        time_limit (int): Время в секундах, в течение которого запросы от одного пользователя будут игнорироваться.
    """

    def __init__(self, time_limit: int = 2) -> None:
        """
        Инициализирует мидлварь с заданным временем ожидания.

        Args:
            time_limit (int): Время в секундах, в течение которого запросы от одного пользователя будут игнорироваться.
        """
        # Инициализация кэша с максимальным размером 10_000 и временем жизни ключа time_limit
        self.limit = TTLCache(maxsize=10_000, ttl=time_limit)

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        """
        Выполняет проверку на троттлинг перед вызовом обработчика.

        Args:
            handler (Callable): Обработчик сообщения.
            event (Message): Объект сообщения.
            data (Dict[str, Any]): Дополнительные данные.

        Returns:
            Any: Результат работы обработчика.
        """
        try:
            # Проверка, есть ли chat_id пользователя в кэше
            if event.chat.id in self.limit:
                # Если есть, то запрос игнорируется
                return
            else:
                # Если нет, добавляем chat_id в кэш
                self.limit[event.chat.id] = None
            # Вызываем обработчик
            return await handler(event, data)
        except Exception as ex:
            # Логируем ошибку в случае исключения
            logger.error('Ошибка при выполнении ThrottlingMiddleware', exc_info=ex)
            return
```