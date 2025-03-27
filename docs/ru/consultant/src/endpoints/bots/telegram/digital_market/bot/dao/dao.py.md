### Анализ кода модуля `dao.py`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код разбит на классы DAO для каждой модели.
    - Используется асинхронная работа с базой данных.
    - Присутствуют методы для получения статистики и данных по моделям.
    - Используется `selectinload` для оптимизации запросов.
- **Минусы**:
    - Не везде используется `logger.error` для обработки ошибок.
    - Используются f-строки с двойными кавычками, что противоречит стандарту.
    - В некоторых местах используется `print` для вывода ошибок, вместо `logger`.
    - Отсутствует RST документация для большинства методов и классов.
    - Не все импорты выровнены в алфавитном порядке.

**Рекомендации по улучшению:**

1.  **Документирование**:
    - Добавить RST-документацию для всех классов и методов, описывая их назначение, параметры, возвращаемые значения и возможные исключения.
2.  **Логирование**:
    - Заменить все `print` на `logger.error` для логирования ошибок.
    - Использовать `logger.info` для логирования важных событий.
3.  **Обработка ошибок**:
    - Убрать `try-except` блоки где они не несут полезной нагрузки.
4.  **Форматирование**:
    - Использовать одинарные кавычки для строк в коде, кроме `print`, `input` и `logger`.
    - Выровнять все импорты в алфавитном порядке.
5.  **Именование**:
    - Проверить и при необходимости переименовать переменные для большей ясности.
6. **Импорты**:
   -  Импортировать `logger` из `src.logger`.

**Оптимизированный код:**

```python
"""
Модуль для работы с базой данных моделей Telegram бота цифрового рынка
======================================================================

Модуль содержит классы DAO (Data Access Object) для взаимодействия с различными моделями,
такими как User, Purchase, Category и Product.

Пример использования
----------------------
.. code-block:: python

    from sqlalchemy.ext.asyncio import AsyncSession
    from src.endpoints.bots.telegram.digital_market.bot.dao.dao import UserDAO, PurchaseDao
    
    async def main():
        session: AsyncSession = ... #  Получение сессии
        user_stats = await UserDAO.get_purchase_statistics(session, 123456)
        payment_stats = await PurchaseDao.get_payment_stats(session)
        print(user_stats)
        print(payment_stats)
"""
from datetime import datetime, timedelta, UTC
from typing import Dict, List, Optional

from sqlalchemy import func, select, case
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.logger import logger #  Импортируем logger
from bot.dao.base import BaseDAO
from bot.dao.models import Category, Product, Purchase, User


class UserDAO(BaseDAO[User]):
    """
    DAO для работы с моделью User.
    """
    model = User

    @classmethod
    async def get_purchase_statistics(cls, session: AsyncSession, telegram_id: int) -> Optional[Dict[str, int]]:
        """
        Получает статистику покупок пользователя.

        :param session: Асинхронная сессия базы данных.
        :type session: AsyncSession
        :param telegram_id: ID пользователя в Telegram.
        :type telegram_id: int
        :return: Словарь со статистикой покупок (общее число покупок и общая сумма), или None, если пользователь не найден.
        :rtype: Optional[Dict[str, int]]
        :raises SQLAlchemyError: В случае ошибки при работе с базой данных.
        
        Пример:
            >>> async def test():
            >>>     session = ... #  Получение сессии
            >>>     stats = await UserDAO.get_purchase_statistics(session, 123456)
            >>>     print(stats)
        """
        try:
            result = await session.execute(
                select(
                    func.count(Purchase.id).label('total_purchases'),
                    func.sum(Purchase.price).label('total_amount'),
                )
                .join(User)
                .filter(User.telegram_id == telegram_id)
            )
            stats = result.one_or_none()

            if stats is None:
                return None

            total_purchases, total_amount = stats
            return {
                'total_purchases': total_purchases,
                'total_amount': total_amount or 0,  # Обработка случая, когда сумма может быть None
            }
        except SQLAlchemyError as e:
            logger.error(f'Ошибка при получении статистики покупок пользователя: {e}') #  Используем logger.error вместо print
            return None

    @classmethod
    async def get_purchased_products(cls, session: AsyncSession, telegram_id: int) -> Optional[List[Purchase]]:
        """
        Получает список покупок пользователя.

        :param session: Асинхронная сессия базы данных.
        :type session: AsyncSession
        :param telegram_id: ID пользователя в Telegram.
        :type telegram_id: int
        :return: Список покупок пользователя или None, если пользователь не найден.
        :rtype: Optional[List[Purchase]]
        :raises SQLAlchemyError: В случае ошибки при работе с базой данных.

        Пример:
            >>> async def test():
            >>>     session = ... #  Получение сессии
            >>>     purchases = await UserDAO.get_purchased_products(session, 123456)
            >>>     print(purchases)
        """
        try:
            result = await session.execute(
                select(User)
                .options(selectinload(User.purchases).selectinload(Purchase.product))
                .filter(User.telegram_id == telegram_id)
            )
            user = result.scalar_one_or_none()

            if user is None:
                return None

            return user.purchases
        except SQLAlchemyError as e:
            logger.error(f'Ошибка при получении информации о покупках пользователя: {e}') #  Используем logger.error вместо print
            return None

    @classmethod
    async def get_statistics(cls, session: AsyncSession) -> Dict[str, int]:
        """
        Получает общую статистику по пользователям (общее количество, новые за сегодня, неделю и месяц).

        :param session: Асинхронная сессия базы данных.
        :type session: AsyncSession
        :return: Словарь со статистикой по пользователям.
        :rtype: Dict[str, int]
        :raises SQLAlchemyError: В случае ошибки при работе с базой данных.

        Пример:
            >>> async def test():
            >>>     session = ... #  Получение сессии
            >>>     stats = await UserDAO.get_statistics(session)
            >>>     print(stats)
        """
        try:
            now = datetime.now(UTC)

            query = select(
                func.count().label('total_users'),
                func.sum(case((cls.model.created_at >= now - timedelta(days=1), 1), else_=0)).label('new_today'),
                func.sum(case((cls.model.created_at >= now - timedelta(days=7), 1), else_=0)).label('new_week'),
                func.sum(case((cls.model.created_at >= now - timedelta(days=30), 1), else_=0)).label('new_month'),
            )

            result = await session.execute(query)
            stats = result.fetchone()

            statistics = {
                'total_users': stats.total_users,
                'new_today': stats.new_today,
                'new_week': stats.new_week,
                'new_month': stats.new_month,
            }

            logger.info(f'Статистика успешно получена: {statistics}') #  Используем logger.info
            return statistics
        except SQLAlchemyError as e:
            logger.error(f'Ошибка при получении статистики: {e}') #  Используем logger.error
            raise


class PurchaseDao(BaseDAO[Purchase]):
    """
    DAO для работы с моделью Purchase.
    """
    model = Purchase

    @classmethod
    async def get_payment_stats(cls, session: AsyncSession) -> str:
        """
        Получает статистику платежей по типам.

        :param session: Асинхронная сессия базы данных.
        :type session: AsyncSession
        :return: Отформатированная строка со статистикой платежей.
        :rtype: str
        
        Пример:
            >>> async def test():
            >>>     session = ... #  Получение сессии
            >>>     stats = await PurchaseDao.get_payment_stats(session)
            >>>     print(stats)
        """
        query = select(
            cls.model.payment_type, func.sum(cls.model.price).label('total_price')
        ).group_by(cls.model.payment_type)

        result = await session.execute(query)
        stats = result.all()

        totals: Dict[str, float] = {
            'yukassa': 0,
            'robocassa': 0,
            'stars': 0,
        }

        for payment_type, total in stats:
            totals[payment_type] = total or 0

        formatted_stats = (
            f'💳 Юкасса: {totals["yukassa"]:.2f} ₽\n'
            f'🤖 Робокасса: {totals["robocassa"]:.2f} ₽\n'
            f'⭐ STARS: {totals["stars"]:.0f}\n\n'
            'Статистика актуальна на данный момент.'
        )

        return formatted_stats

    @classmethod
    async def get_full_summ(cls, session: AsyncSession) -> int:
        """
        Получает общую сумму всех покупок.

        :param session: Асинхронная сессия базы данных.
        :type session: AsyncSession
        :return: Общая сумма покупок.
        :rtype: int

        Пример:
            >>> async def test():
            >>>     session = ... #  Получение сессии
            >>>     total_sum = await PurchaseDao.get_full_summ(session)
            >>>     print(total_sum)
        """
        query = select(func.sum(cls.model.price).label('total_price'))
        result = await session.execute(query)
        total_price = result.scalars().one_or_none()
        return total_price if total_price is not None else 0

    @classmethod
    async def get_next_id(cls, session: AsyncSession) -> int:
        """
        Возвращает следующий свободный ID для новой записи.

        :param session: Асинхронная сессия базы данных
        :type session: AsyncSession
        :return: Следующий свободный ID
        :rtype: int

        Пример:
            >>> async def test():
            >>>     session = ... #  Получение сессии
            >>>     next_id = await PurchaseDao.get_next_id(session)
            >>>     print(next_id)
        """
        query = select(func.coalesce(func.max(cls.model.id) + 1, 1))
        result = await session.execute(query)
        return result.scalar()


class CategoryDao(BaseDAO[Category]):
    """
    DAO для работы с моделью Category.
    """
    model = Category


class ProductDao(BaseDAO[Product]):
    """
    DAO для работы с моделью Product.
    """
    model = Product