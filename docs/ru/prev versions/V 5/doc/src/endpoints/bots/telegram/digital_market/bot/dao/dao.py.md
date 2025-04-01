# Модуль DAO для работы с цифровым рынком в Telegram боте

## Обзор

Модуль содержит Data Access Objects (DAO) для взаимодействия с базой данных, используемой в Telegram боте цифрового рынка. Он включает DAO для моделей `User`, `Purchase`, `Category` и `Product`, предоставляя методы для выполнения операций CRUD, а также получения статистической информации.

## Подробней

Этот модуль обеспечивает абстракцию доступа к данным, что позволяет упростить взаимодействие с базой данных и уменьшить зависимость бизнес-логики от конкретной реализации базы данных. Он включает классы DAO для каждой модели, которые содержат методы для выполнения запросов к базе данных, таких как получение статистики покупок пользователей, получение списка приобретенных продуктов, получение статистики по пользователям и платежам.

## Классы

### `UserDAO`

**Описание**: DAO для работы с моделью `User`.

**Как работает класс**:
`UserDAO` наследуется от `BaseDAO` и предоставляет методы для получения информации о пользователях, их покупках и статистике. Класс содержит методы для получения статистики покупок пользователя, получения списка приобретенных продуктов и получения общей статистики по пользователям.

**Методы**:
- `get_purchase_statistics`: Получает статистику покупок пользователя.
- `get_purchased_products`: Получает список приобретенных продуктов пользователя.
- `get_statistics`: Получает общую статистику по пользователям.

### `PurchaseDao`

**Описание**: DAO для работы с моделью `Purchase`.

**Как работает класс**:
`PurchaseDao` наследуется от `BaseDAO` и предоставляет методы для получения информации о покупках, включая статистику по типам платежей и общую сумму покупок. Класс содержит методы для получения статистики по типам платежей, получения общей суммы покупок и получения следующего свободного ID для новой записи.

**Методы**:
- `get_payment_stats`: Получает статистику по типам платежей.
- `get_full_summ`: Получает общую сумму покупок.
- `get_next_id`: Получает следующий свободный ID для новой записи.

### `CategoryDao`

**Описание**: DAO для работы с моделью `Category`.

**Как работает класс**:
`CategoryDao` наследуется от `BaseDAO` и предоставляет методы для работы с категориями продуктов.

### `ProductDao`

**Описание**: DAO для работы с моделью `Product`.

**Как работает класс**:
`ProductDao` наследуется от `BaseDAO` и предоставляет методы для работы с продуктами.

## Функции

### `UserDAO.get_purchase_statistics`

```python
@classmethod
async def get_purchase_statistics(cls, session: AsyncSession, telegram_id: int) -> Optional[Dict[str, int]]:
    """
    Args:
        session (AsyncSession): Асинхронная сессия базы данных.
        telegram_id (int): Telegram ID пользователя.

    Returns:
        Optional[Dict[str, int]]: Словарь со статистикой покупок пользователя или `None` в случае ошибки.

    Raises:
        SQLAlchemyError: При возникновении ошибки при работе с базой данных.

    Example:
        >>> session = AsyncSession()
        >>> telegram_id = 123456789
        >>> stats = await UserDAO.get_purchase_statistics(session, telegram_id)
        >>> if stats:
        ...     print(f"Total purchases: {stats['total_purchases']}")
        ...     print(f"Total amount: {stats['total_amount']}")
    """
```

**Описание**: Получает статистику покупок пользователя.

**Как работает функция**:
Функция выполняет запрос к базе данных для получения общего числа покупок и общей суммы, потраченной пользователем с указанным `telegram_id`. Результаты возвращаются в виде словаря, содержащего ключи `total_purchases` и `total_amount`. В случае ошибки при работе с базой данных возвращается `None`.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия базы данных.
- `telegram_id` (int): Telegram ID пользователя.

**Возвращает**:
- `Optional[Dict[str, int]]`: Словарь со статистикой покупок пользователя или `None` в случае ошибки.

**Вызывает исключения**:
- `SQLAlchemyError`: При возникновении ошибки при работе с базой данных.

### `UserDAO.get_purchased_products`

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
        SQLAlchemyError: При возникновении ошибки при работе с базой данных.

    Example:
        >>> session = AsyncSession()
        >>> telegram_id = 123456789
        >>> purchases = await UserDAO.get_purchased_products(session, telegram_id)
        >>> if purchases:
        ...     for purchase in purchases:
        ...         print(f"Product: {purchase.product.name}, Price: {purchase.price}")
    """
```

**Описание**: Получает список приобретенных продуктов пользователя.

**Как работает функция**:
Функция выполняет запрос к базе данных для получения пользователя с указанным `telegram_id` и его покупок. Возвращается список объектов `Purchase`, связанных с пользователем. В случае ошибки при работе с базой данных возвращается `None`.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия базы данных.
- `telegram_id` (int): Telegram ID пользователя.

**Возвращает**:
- `Optional[List[Purchase]]`: Список покупок пользователя или `None` в случае ошибки.

**Вызывает исключения**:
- `SQLAlchemyError`: При возникновении ошибки при работе с базой данных.

### `UserDAO.get_statistics`

```python
@classmethod
async def get_statistics(cls, session: AsyncSession):
    """
    Args:
        session (AsyncSession): Асинхронная сессия базы данных.

    Returns:
        dict: Словарь со статистикой по пользователям.

    Raises:
        SQLAlchemyError: При возникновении ошибки при работе с базой данных.

    Example:
        >>> session = AsyncSession()
        >>> stats = await UserDAO.get_statistics(session)
        >>> print(f"Total users: {stats['total_users']}")
        >>> print(f"New users today: {stats['new_today']}")
        >>> print(f"New users this week: {stats['new_week']}")
        >>> print(f"New users this month: {stats['new_month']}")
    """
```

**Описание**: Получает общую статистику по пользователям.

**Как работает функция**:
Функция выполняет запрос к базе данных для получения общего числа пользователей, а также количества новых пользователей, зарегистрированных сегодня, на этой неделе и в этом месяце. Результаты возвращаются в виде словаря, содержащего ключи `total_users`, `new_today`, `new_week` и `new_month`.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия базы данных.

**Возвращает**:
- `dict`: Словарь со статистикой по пользователям.

**Вызывает исключения**:
- `SQLAlchemyError`: При возникновении ошибки при работе с базой данных.

### `PurchaseDao.get_payment_stats`

```python
@classmethod
async def get_payment_stats(cls, session: AsyncSession) -> str:
    """
    Args:
        session (AsyncSession): Асинхронная сессия базы данных.

    Returns:
        str: Форматированная строка со статистикой по типам платежей.

    Example:
        >>> session = AsyncSession()
        >>> stats = await PurchaseDao.get_payment_stats(session)
        >>> print(stats)
    """
```

**Описание**: Получает статистику по типам платежей.

**Как работает функция**:
Функция выполняет запрос к базе данных для получения статистики по типам платежей (`yukassa`, `robocassa`, `stars`) и возвращает форматированную строку с результатами.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия базы данных.

**Возвращает**:
- `str`: Форматированная строка со статистикой по типам платежей.

### `PurchaseDao.get_full_summ`

```python
@classmethod
async def get_full_summ(cls, session: AsyncSession) -> int:
    """
    Args:
        session (AsyncSession): Асинхронная сессия базы данных.

    Returns:
        int: Общая сумма покупок.

    Example:
        >>> session = AsyncSession()
        >>> total_sum = await PurchaseDao.get_full_summ(session)
        >>> print(f"Total sum: {total_sum}")
    """
```

**Описание**: Получает общую сумму покупок.

**Как работает функция**:
Функция выполняет запрос к базе данных для получения общей суммы всех покупок.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия базы данных.

**Возвращает**:
- `int`: Общая сумма покупок.

### `PurchaseDao.get_next_id`

```python
@classmethod
async def get_next_id(cls, session: AsyncSession) -> int:
    """
    Args:
        session (AsyncSession): Асинхронная сессия базы данных.

    Returns:
        int: Следующий свободный ID для новой записи.

    Example:
        >>> session = AsyncSession()
        >>> next_id = await PurchaseDao.get_next_id(session)
        >>> print(f"Next ID: {next_id}")
    """
```

**Описание**: Возвращает следующий свободный ID для новой записи.

**Как работает функция**:
Функция выполняет запрос к базе данных для получения максимального значения `id` в таблице `Purchase` и возвращает следующее свободное значение. Если таблица пуста, возвращается 1.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия базы данных.

**Возвращает**:
- `int`: Следующий свободный ID.