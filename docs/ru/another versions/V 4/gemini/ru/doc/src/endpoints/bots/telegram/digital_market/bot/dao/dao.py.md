# Модуль dao.py

## Обзор

Модуль `dao.py` содержит классы для доступа к данным (DAO) для моделей `User`, `Purchase`, `Category` и `Product`.
Он предоставляет методы для выполнения операций с базой данных, таких как получение статистики покупок пользователей, информации о покупках и общей статистики.

## Подробней

Этот модуль является частью системы управления цифровым рынком Telegram-бота. Он обеспечивает взаимодействие с базой данных для выполнения различных операций, связанных с пользователями, покупками, категориями и продуктами.
DAO классы абстрагируют логику доступа к данным, что упрощает взаимодействие с базой данных и обеспечивает гибкость при изменении схемы базы данных.

## Классы

### `UserDAO`

**Описание**: DAO для работы с моделью `User`.

**Методы**:
- `get_purchase_statistics`: Получает статистику покупок пользователя.
- `get_purchased_products`: Получает информацию о покупках пользователя.
- `get_statistics`: Получает общую статистику пользователей.

#### `get_purchase_statistics`

```python
@classmethod
async def get_purchase_statistics(cls, session: AsyncSession, telegram_id: int) -> Optional[Dict[str, int]]:
    """
    Args:
        session (AsyncSession): Асинхронная сессия базы данных.
        telegram_id (int): Telegram ID пользователя.

    Returns:
        Optional[Dict[str, int]]: Словарь со статистикой покупок пользователя или `None` в случае ошибки.
        Содержит ключи 'total_purchases' (общее количество покупок) и 'total_amount' (общая сумма покупок).

    Raises:
        SQLAlchemyError: Если возникает ошибка при работе с базой данных.

    Example:
        >>> session = AsyncSession()
        >>> telegram_id = 123456789
        >>> stats = await UserDAO.get_purchase_statistics(session, telegram_id)
        >>> if stats:
        ...     print(f"Total purchases: {stats['total_purchases']}, Total amount: {stats['total_amount']}")
    """
```

**Описание**: Получает статистику покупок пользователя, включая общее количество покупок и общую сумму покупок.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия базы данных.
- `telegram_id` (int): Telegram ID пользователя.

**Возвращает**:
- `Optional[Dict[str, int]]`: Словарь со статистикой покупок пользователя или `None` в случае ошибки.
  Содержит ключи `'total_purchases'` (общее количество покупок) и `'total_amount'` (общая сумма покупок).

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при работе с базой данных.

#### `get_purchased_products`

```python
@classmethod
async def get_purchased_products(cls, session: AsyncSession, telegram_id: int) -> Optional[List[Purchase]]:
    """
    Args:
        session (AsyncSession): Асинхронная сессия базы данных.
        telegram_id (int): Telegram ID пользователя.

    Returns:
        Optional[List[Purchase]]: Список покупок пользователя или `None` в случае ошибки.

    Raises:
        SQLAlchemyError: Если возникает ошибка при работе с базой данных.

    Example:
        >>> session = AsyncSession()
        >>> telegram_id = 123456789
        >>> purchases = await UserDAO.get_purchased_products(session, telegram_id)
        >>> if purchases:
        ...     for purchase in purchases:
        ...         print(f"Purchase ID: {purchase.id}, Product ID: {purchase.product_id}")
    """
```

**Описание**: Получает информацию о покупках пользователя.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия базы данных.
- `telegram_id` (int): Telegram ID пользователя.

**Возвращает**:
- `Optional[List[Purchase]]`: Список покупок пользователя или `None` в случае ошибки.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при работе с базой данных.

#### `get_statistics`

```python
@classmethod
async def get_statistics(cls, session: AsyncSession):
    """
    Args:
        session (AsyncSession): Асинхронная сессия базы данных.

    Returns:
        statistics (Dict[str, int]): Словарь со статистикой пользователей.
        Содержит ключи 'total_users' (общее количество пользователей), 'new_today' (новых пользователей сегодня),
        'new_week' (новых пользователей за последнюю неделю) и 'new_month' (новых пользователей за последний месяц).

    Raises:
        SQLAlchemyError: Если возникает ошибка при работе с базой данных.

    Example:
        >>> session = AsyncSession()
        >>> stats = await UserDAO.get_statistics(session)
        >>> print(f"Total users: {stats['total_users']}, New today: {stats['new_today']}")
    """
```

**Описание**: Получает общую статистику пользователей, такую как общее количество пользователей, новых пользователей сегодня, новых пользователей за последнюю неделю и новых пользователей за последний месяц.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия базы данных.

**Возвращает**:
- `Dict[str, int]`: Словарь со статистикой пользователей.
  Содержит ключи `'total_users'` (общее количество пользователей), `'new_today'` (новых пользователей сегодня),
  `'new_week'` (новых пользователей за последнюю неделю) и `'new_month'` (новых пользователей за последний месяц).

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при работе с базой данных.

### `PurchaseDao`

**Описание**: DAO для работы с моделью `Purchase`.

**Методы**:
- `get_payment_stats`: Получает статистику платежей.
- `get_full_summ`: Получает полную сумму покупок.
- `get_next_id`: Возвращает следующий свободный ID для новой записи.

#### `get_payment_stats`

```python
@classmethod
async def get_payment_stats(cls, session: AsyncSession) -> str:
    """
    Args:
        session (AsyncSession): Асинхронная сессия базы данных.

    Returns:
        str: Отформатированная строка со статистикой платежей.

    Raises:
        SQLAlchemyError: Если возникает ошибка при работе с базой данных.

    Example:
        >>> session = AsyncSession()
        >>> stats = await PurchaseDao.get_payment_stats(session)
        >>> print(stats)
    """
```

**Описание**: Получает статистику платежей по типам (Юкасса, Робокасса, STARS) и возвращает отформатированную строку.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия базы данных.

**Возвращает**:
- `str`: Отформатированная строка со статистикой платежей.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при работе с базой данных.

#### `get_full_summ`

```python
@classmethod
async def get_full_summ(cls, session: AsyncSession) -> int:
    """
    Args:
        session (AsyncSession): Асинхронная сессия базы данных.

    Returns:
        int: Полная сумма покупок.

    Raises:
        SQLAlchemyError: Если возникает ошибка при работе с базой данных.

    Example:
        >>> session = AsyncSession()
        >>> total_sum = await PurchaseDao.get_full_summ(session)
        >>> print(f"Total sum: {total_sum}")
    """
```

**Описание**: Получает полную сумму покупок.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия базы данных.

**Возвращает**:
- `int`: Полная сумма покупок.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при работе с базой данных.

#### `get_next_id`

```python
@classmethod
async def get_next_id(cls, session: AsyncSession) -> int:
    """
    Args:
        session (AsyncSession): Асинхронная сессия базы данных

    Returns:
        int: Следующий свободный ID

    Raises:
        SQLAlchemyError: Если возникает ошибка при работе с базой данных.

    Example:
        >>> session = AsyncSession()
        >>> next_id = await PurchaseDao.get_next_id(session)
        >>> print(f"Next ID: {next_id}")
    """
```

**Описание**: Возвращает следующий свободный ID для новой записи.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия базы данных.

**Возвращает**:
- `int`: Следующий свободный ID.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при работе с базой данных.

### `CategoryDao`

**Описание**: DAO для работы с моделью `Category`.

### `ProductDao`

**Описание**: DAO для работы с моделью `Product`.

## Функции

В данном модуле функции отсутствуют.