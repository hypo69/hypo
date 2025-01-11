# Анализ кода модуля `dao.py`

**Качество кода: 7/10**

-   **Плюсы**
    -   Код использует асинхронные запросы к базе данных, что обеспечивает хорошую производительность.
    -   Присутствует базовая обработка ошибок с помощью `try-except`.
    -   Используются `selectinload` для оптимизации запросов к связанным данным.
    -   Присутствует логирование с помощью `logger`.
    -   Код структурирован в классы, каждый из которых отвечает за работу с конкретной моделью БД.
-   **Минусы**
    -   Не все комментарии соответствуют стандарту RST.
    -   Используется `print` вместо `logger.error` для вывода ошибок в некоторых местах.
    -   Отсутствует документация для функций и методов.
    -   В некоторых местах есть избыточное использование `try-except` вместо более точного логирования ошибок.
    -   Не все переменные имеют информативные имена.
    -   Некоторые методы имеют слишком общую логику.
    -   Нет обработки случая когда `stats` может быть пустым `[]`.

**Рекомендации по улучшению**

1.  **Улучшить документацию:**
    -   Добавить docstring к каждому классу и методу, используя формат RST.
    -   Добавить описание модуля в начале файла.
2.  **Унифицировать обработку ошибок:**
    -   Использовать `logger.error` вместо `print` для вывода ошибок.
    -   Сократить избыточное использование `try-except` блоков,  предпочитая `logger.error` для логирования исключений.
3.  **Оптимизировать логику:**
    -   Проверять на пустой результат `stats` в методе `get_payment_stats`
    -   Добавить более информативные имена для переменных и параметров.
4.  **Стандартизация кода:**
    -   Использовать одинарные кавычки (`'`) для строк в коде, а двойные (`"`) только для вывода в консоль.

**Оптимизированный код**

```python
"""
Модуль для доступа к данным моделей базы данных.
=========================================================================================

Этот модуль содержит DAO (Data Access Objects) для работы с моделями User, Purchase, Category и Product.
Он обеспечивает асинхронный доступ к базе данных и включает методы для получения статистики,
покупок и другой информации.

Пример использования
--------------------

Пример использования классов `UserDAO`, `PurchaseDao` и других:

.. code-block:: python

    from sqlalchemy.ext.asyncio import create_async_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.asyncio import AsyncSession

    # Пример использования
    engine = create_async_engine("postgresql+asyncpg://user:password@host:port/database")
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async def main():
        async with async_session() as session:
            # Получение статистики пользователей
            user_stats = await UserDAO.get_statistics(session)
            print(f"Статистика пользователей: {user_stats}")

            # Получение статистики покупок
            purchase_stats = await PurchaseDao.get_payment_stats(session)
            print(f"Статистика покупок: {purchase_stats}")

            # Получение общего дохода
            total_sum = await PurchaseDao.get_full_summ(session)
            print(f"Общий доход: {total_sum}")

            # Получение статистики пользователя
            user_purchase_stats = await UserDAO.get_purchase_statistics(session, 12345)
            print(f"Статистика покупок пользователя: {user_purchase_stats}")

            # Получение продуктов пользователя
            user_products = await UserDAO.get_purchased_products(session, 12345)
            print(f"Покупки пользователя: {user_products}")
    if __name__ == "__main__":
        import asyncio
        asyncio.run(main())
"""
from datetime import datetime, UTC, timedelta
from typing import Optional, List, Dict

from src.logger.logger import logger #  Импорт логгера из src.logger
from sqlalchemy import select, func, case
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from bot.dao.base import BaseDAO
from bot.dao.models import User, Purchase, Category, Product


class UserDAO(BaseDAO[User]):
    """
    DAO для работы с моделью User.

    Предоставляет методы для получения статистики пользователей и их покупок.
    """
    model = User

    @classmethod
    async def get_purchase_statistics(cls, session: AsyncSession, telegram_id: int) -> Optional[Dict[str, int]]:
        """
        Получает статистику покупок пользователя.

        Args:
            session: Асинхронная сессия базы данных.
            telegram_id: Telegram ID пользователя.

        Returns:
            Словарь со статистикой покупок пользователя или None, если пользователь не найден или произошла ошибка.
            Содержит ключи: 'total_purchases' и 'total_amount'.
        """
        try:
            #  Запрос для получения общего числа покупок и общей суммы
            result = await session.execute(
                select(
                    func.count(Purchase.id).label('total_purchases'),
                    func.sum(Purchase.price).label('total_amount')
                ).join(User).filter(User.telegram_id == telegram_id)
            )
            stats = result.one_or_none()

            if stats is None:
                return None

            total_purchases, total_amount = stats
            return {
                'total_purchases': total_purchases,
                'total_amount': total_amount or 0 # Обработка случая, когда сумма может быть None
            }

        except SQLAlchemyError as e:
            #  Обработка ошибок при работе с базой данных
            logger.error(f'Ошибка при получении статистики покупок пользователя: {e}')
            return None

    @classmethod
    async def get_purchased_products(cls, session: AsyncSession, telegram_id: int) -> Optional[List[Purchase]]:
        """
        Получает список покупок пользователя.

        Args:
            session: Асинхронная сессия базы данных.
            telegram_id: Telegram ID пользователя.

        Returns:
            Список покупок пользователя или None, если пользователь не найден или произошла ошибка.
        """
        try:
            #  Запрос для получения пользователя с его покупками и связанными продуктами
            result = await session.execute(
                select(User)
                .options(
                    selectinload(User.purchases).selectinload(Purchase.product)
                )
                .filter(User.telegram_id == telegram_id)
            )
            user = result.scalar_one_or_none()

            if user is None:
                return None

            return user.purchases

        except SQLAlchemyError as e:
            #  Обработка ошибок при работе с базой данных
            logger.error(f'Ошибка при получении информации о покупках пользователя: {e}')
            return None


    @classmethod
    async def get_statistics(cls, session: AsyncSession) -> Dict[str, int]:
        """
        Получает общую статистику пользователей.

        Args:
            session: Асинхронная сессия базы данных.

        Returns:
            Словарь со статистикой пользователей.
            Содержит ключи: 'total_users', 'new_today', 'new_week', 'new_month'.
        """
        try:
            now = datetime.now(UTC)

            query = select(
                func.count().label('total_users'),
                func.sum(case((cls.model.created_at >= now - timedelta(days=1), 1), else_=0)).label('new_today'),
                func.sum(case((cls.model.created_at >= now - timedelta(days=7), 1), else_=0)).label('new_week'),
                func.sum(case((cls.model.created_at >= now - timedelta(days=30), 1), else_=0)).label('new_month')
            )

            result = await session.execute(query)
            stats = result.fetchone()

            statistics = {
                'total_users': stats.total_users,
                'new_today': stats.new_today,
                'new_week': stats.new_week,
                'new_month': stats.new_month
            }

            logger.info(f'Статистика успешно получена: {statistics}')
            return statistics
        except SQLAlchemyError as e:
            logger.error(f'Ошибка при получении статистики: {e}')
            raise


class PurchaseDao(BaseDAO[Purchase]):
    """
    DAO для работы с моделью Purchase.

    Предоставляет методы для получения статистики платежей.
    """
    model = Purchase

    @classmethod
    async def get_payment_stats(cls, session: AsyncSession) -> str:
        """
        Получает статистику платежей по типам.

        Args:
            session: Асинхронная сессия базы данных.

        Returns:
             Cтрока с форматированной статистикой платежей по типам.
        """
        query = select(
            cls.model.payment_type,
            func.sum(cls.model.price).label('total_price')
        ).group_by(cls.model.payment_type)

        result = await session.execute(query)
        stats = result.all()

        # Словарь для хранения результатов
        totals: Dict[str, float] = {
            'yukassa': 0,
            'robocassa': 0,
            'stars': 0
        }

        # Заполняем словарь результатами запроса
        if stats:
           for payment_type, total in stats:
               totals[payment_type] = total or 0
        else:
           logger.warning(f'Нет данных для формирования статистики {stats=}')


        # Форматируем результат
        formatted_stats = (
            f'💳 Юкасса: {totals["yukassa"]:.2f} ₽\n'
            f'🤖 Робокасса: {totals["robocassa"]:.2f} ₽\n'
            f'⭐ STARS: {totals["stars"]:.0f}\n\n'
            f'Статистика актуальна на данный момент.'
        )

        return formatted_stats

    @classmethod
    async def get_full_summ(cls, session: AsyncSession) -> int:
        """
        Получает общую сумму всех покупок.

        Args:
            session: Асинхронная сессия базы данных.

        Returns:
            Общая сумма всех покупок.
        """
        query = select(func.sum(cls.model.price).label('total_price'))
        result = await session.execute(query)
        total_price = result.scalars().one_or_none()
        return total_price if total_price is not None else 0

    @classmethod
    async def get_next_id(cls, session: AsyncSession) -> int:
        """
        Получает следующий свободный ID для новой записи.

        Args:
            session: Асинхронная сессия базы данных.

        Returns:
            Следующий свободный ID.
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
```