# Модуль `dao.py`

## Обзор

Модуль `dao.py` содержит Data Access Objects (DAO) для работы с моделями базы данных, такими как `User`, `Purchase`, `Category` и `Product`. Он предоставляет методы для выполнения операций CRUD (создание, чтение, обновление, удаление) и других запросов к базе данных, специфичных для каждой модели.

## Подробней

Этот модуль обеспечивает абстракцию доступа к данным, упрощая взаимодействие с базой данных и позволяя избежать дублирования кода. DAO классы используют SQLAlchemy для выполнения запросов к базе данных асинхронно.

## Классы

### `UserDAO`

**Описание**: DAO для работы с моделью `User`. Предоставляет методы для получения статистики покупок пользователя, получения списка приобретенных продуктов и общей статистики пользователей.

**Методы**:
- `get_purchase_statistics`: Получает статистику покупок пользователя.
- `get_purchased_products`: Получает список приобретенных продуктов пользователя.
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
        Optional[Dict[str, int]]: Словарь со статистикой покупок пользователя, содержащий общее количество покупок и общую сумму покупок. Возвращает `None` в случае ошибки или отсутствия данных.

    Raises:
        SQLAlchemyError: В случае ошибки при работе с базой данных.

    Example:
        >>> session = AsyncSession()
        >>> telegram_id = 123456789
        >>> stats = await UserDAO.get_purchase_statistics(session, telegram_id)
        >>> if stats:
        ...     print(f"Total purchases: {stats['total_purchases']}")
        ...     print(f"Total amount: {stats['total_amount']}")
    """
```

**Описание**: Получает статистику покупок пользователя, такую как общее количество покупок и общая сумма покупок.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия базы данных.
- `telegram_id` (int): Telegram ID пользователя.

**Возвращает**:
- `Optional[Dict[str, int]]`: Словарь со статистикой покупок пользователя, содержащий общее количество покупок (`total_purchases`) и общую сумму покупок (`total_amount`). Возвращает `None` в случае ошибки или отсутствия данных.

**Вызывает исключения**:
- `SQLAlchemyError`: В случае ошибки при работе с базой данных.

#### `get_purchased_products`

```python
@classmethod
async def get_purchased_products(cls, session: AsyncSession, telegram_id: int) -> Optional[List[Purchase]]:
    """
    Args:
        session (AsyncSession): Асинхронная сессия базы данных.
        telegram_id (int): Telegram ID пользователя.

    Returns:
        Optional[List[Purchase]]: Список покупок пользователя. Возвращает `None` в случае ошибки или отсутствия данных.

    Raises:
        SQLAlchemyError: В случае ошибки при работе с базой данных.

    Example:
        >>> session = AsyncSession()
        >>> telegram_id = 123456789
        >>> purchases = await UserDAO.get_purchased_products(session, telegram_id)
        >>> if purchases:
        ...     for purchase in purchases:
        ...         print(f"Purchase ID: {purchase.id}, Product: {purchase.product.name}, Price: {purchase.price}")
    """
```

**Описание**: Получает список приобретенных продуктов пользователя.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия базы данных.
- `telegram_id` (int): Telegram ID пользователя.

**Возвращает**:
- `Optional[List[Purchase]]`: Список покупок пользователя. Возвращает `None` в случае ошибки или отсутствия данных.

**Вызывает исключения**:
- `SQLAlchemyError`: В случае ошибки при работе с базой данных.

#### `get_statistics`

```python
@classmethod
async def get_statistics(cls, session: AsyncSession):
    """
    Args:
        session (AsyncSession): Асинхронная сессия базы данных.

    Returns:
        statistics (Dict[str, int]): Cловарь со статистикой пользователей, содержащий общее количество, новых за сегодня, за неделю, за месяц.

    Raises:
        SQLAlchemyError: В случае ошибки при работе с базой данных.

    Example:
        >>> session = AsyncSession()
        >>> statistics = await UserDAO.get_statistics(session)
        >>> if statistics:
        ...     print(f"Total users: {statistics['total_users']}")
        ...     print(f"New users today: {statistics['new_today']}")
        ...     print(f"New users this week: {statistics['new_week']}")
        ...     print(f"New users this month: {statistics['new_month']}")
    """
```

**Описание**: Получает общую статистику пользователей, такую как общее количество пользователей, количество новых пользователей за сегодня, за неделю и за месяц.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия базы данных.

**Возвращает**:
- `Dict[str, int]`: Словарь со статистикой пользователей, содержащий общее количество пользователей (`total_users`), количество новых пользователей за сегодня (`new_today`), за неделю (`new_week`) и за месяц (`new_month`).

**Вызывает исключения**:
- `SQLAlchemyError`: В случае ошибки при работе с базой данных.

### `PurchaseDao`

**Описание**: DAO для работы с моделью `Purchase`. Предоставляет методы для получения статистики платежей, общей суммы покупок и следующего свободного ID для новой записи.

**Методы**:
- `get_payment_stats`: Получает статистику платежей по типам.
- `get_full_summ`: Получает общую сумму покупок.
- `get_next_id`: Получает следующий свободный ID для новой записи.

#### `get_payment_stats`

```python
@classmethod
async def get_payment_stats(cls, session: AsyncSession) -> str:
    """
    Args:
        session (AsyncSession): Асинхронная сессия базы данных.

    Returns:
        str: Форматированная строка со статистикой платежей по типам.

    Raises:
        SQLAlchemyError: В случае ошибки при работе с базой данных.

    Example:
        >>> session = AsyncSession()
        >>> payment_stats = await PurchaseDao.get_payment_stats(session)
        >>> print(payment_stats)
    """
```

**Описание**: Получает статистику платежей по типам, таким как Юкасса, Робокасса и STARS.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия базы данных.

**Возвращает**:
- `str`: Форматированная строка со статистикой платежей по типам.

**Вызывает исключения**:
- `SQLAlchemyError`: В случае ошибки при работе с базой данных.

#### `get_full_summ`

```python
@classmethod
async def get_full_summ(cls, session: AsyncSession) -> int:
    """
    Args:
        session (AsyncSession): Асинхронная сессия базы данных.

    Returns:
        int: Общая сумма покупок.

    Raises:
        SQLAlchemyError: В случае ошибки при работе с базой данных.

    Example:
        >>> session = AsyncSession()
        >>> total_amount = await PurchaseDao.get_full_summ(session)
        >>> print(f"Total amount: {total_amount}")
    """
```

**Описание**: Получает общую сумму покупок.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия базы данных.

**Возвращает**:
- `int`: Общая сумма покупок.

**Вызывает исключения**:
- `SQLAlchemyError`: В случае ошибки при работе с базой данных.

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
        SQLAlchemyError: В случае ошибки при работе с базой данных.

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
- `SQLAlchemyError`: В случае ошибки при работе с базой данных.

### `CategoryDao`

**Описание**: DAO для работы с моделью `Category`.

### `ProductDao`

**Описание**: DAO для работы с моделью `Product`.