# Модуль `base`

## Обзор

Модуль `base` предоставляет базовый класс `BaseDAO` для реализации Data Access Objects (DAO) для работы с базой данных, используя SQLAlchemy и Pydantic. Он содержит общие методы для выполнения операций CRUD (Create, Read, Update, Delete) и других операций, таких как пагинация и подсчет записей. Этот класс предназначен для наследования другими DAO, специфичными для конкретных моделей базы данных.

## Подробней

Этот модуль предоставляет абстракцию над SQLAlchemy для упрощения взаимодействия с базой данных. `BaseDAO` реализует общие методы, которые могут быть использованы для выполнения стандартных операций с базой данных, таких как добавление, обновление, удаление и выборка данных. Он также включает методы для выполнения пагинации и массового обновления записей. Использование этого класса позволяет избежать дублирования кода и обеспечивает единообразный интерфейс для работы с различными моделями базы данных.

## Классы

### `BaseDAO`

**Описание**:
Базовый класс для Data Access Objects. Предоставляет общие методы для работы с базой данных.

**Методы**:

- `find_one_or_none_by_id`: Найти запись по ID.
- `find_one_or_none`: Найти одну запись по фильтрам.
- `find_all`: Найти все записи по фильтрам.
- `add`: Добавить одну запись.
- `add_many`: Добавить несколько записей.
- `update`: Обновить записи по фильтрам.
- `delete`: Удалить записи по фильтру.
- `count`: Подсчитать количество записей.
- `paginate`: Пагинация записей.
- `find_by_ids`: Найти несколько записей по списку ID.
- `upsert`: Создать запись или обновить существующую.
- `bulk_update`: Массовое обновление записей.

**Параметры**:

- `model` (type[T]): Тип модели SQLAlchemy, с которой работает DAO.

### `find_one_or_none_by_id`

```python
@classmethod
async def find_one_or_none_by_id(cls, data_id: int, session: AsyncSession):
    """
    Args:
        data_id (int): ID записи для поиска.
        session (AsyncSession): Асинхронная сессия SQLAlchemy.

    Returns:
        T | None: Найденная запись или None, если запись не найдена.

    Raises:
        SQLAlchemyError: В случае ошибки при выполнении запроса к базе данных.
    """
```

**Описание**:
Поиск записи в базе данных по её ID.

**Параметры**:
- `data_id` (int): ID записи для поиска.
- `session` (AsyncSession): Асинхронная сессия SQLAlchemy.

**Возвращает**:
- `T | None`: Найденная запись или `None`, если запись не найдена.

**Вызывает исключения**:
- `SQLAlchemyError`: В случае ошибки при выполнении запроса к базе данных.

**Примеры**:
```python
# Пример вызова
# record = await BaseDAO.find_one_or_none_by_id(data_id=1, session=session)
```

### `find_one_or_none`

```python
@classmethod
async def find_one_or_none(cls, session: AsyncSession, filters: BaseModel):
    """
    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy.
        filters (BaseModel): Pydantic модель с фильтрами для поиска.

    Returns:
        T | None: Найденная запись или None, если запись не найдена.

    Raises:
        SQLAlchemyError: В случае ошибки при выполнении запроса к базе данных.
    """
```

**Описание**:
Поиск одной записи в базе данных по заданным фильтрам.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия SQLAlchemy.
- `filters` (BaseModel): Pydantic модель с фильтрами для поиска.

**Возвращает**:
- `T | None`: Найденная запись или `None`, если запись не найдена.

**Вызывает исключения**:
- `SQLAlchemyError`: В случае ошибки при выполнении запроса к базе данных.

**Примеры**:
```python
# Пример вызова
# record = await BaseDAO.find_one_or_none(session=session, filters=filters)
```

### `find_all`

```python
@classmethod
async def find_all(cls, session: AsyncSession, filters: BaseModel | None = None):
    """
    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy.
        filters (BaseModel | None, optional): Pydantic модель с фильтрами для поиска. Defaults to None.

    Returns:
        List[T]: Список найденных записей.

    Raises:
        SQLAlchemyError: В случае ошибки при выполнении запроса к базе данных.
    """
```

**Описание**:
Поиск всех записей в базе данных по заданным фильтрам.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия SQLAlchemy.
- `filters` (BaseModel | None, optional): Pydantic модель с фильтрами для поиска. По умолчанию `None`.

**Возвращает**:
- `List[T]`: Список найденных записей.

**Вызывает исключения**:
- `SQLAlchemyError`: В случае ошибки при выполнении запроса к базе данных.

**Примеры**:
```python
# Пример вызова
# records = await BaseDAO.find_all(session=session, filters=filters)
```

### `add`

```python
@classmethod
async def add(cls, session: AsyncSession, values: BaseModel):
    """
    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy.
        values (BaseModel): Pydantic модель с данными для добавления.

    Returns:
        T: Добавленная запись.

    Raises:
        SQLAlchemyError: В случае ошибки при выполнении запроса к базе данных.
    """
```

**Описание**:
Добавление одной записи в базу данных.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия SQLAlchemy.
- `values` (BaseModel): Pydantic модель с данными для добавления.

**Возвращает**:
- `T`: Добавленная запись.

**Вызывает исключения**:
- `SQLAlchemyError`: В случае ошибки при выполнении запроса к базе данных.

**Примеры**:
```python
# Пример вызова
# new_record = await BaseDAO.add(session=session, values=values)
```

### `add_many`

```python
@classmethod
async def add_many(cls, session: AsyncSession, instances: List[BaseModel]):
    """
    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy.
        instances (List[BaseModel]): Список Pydantic моделей с данными для добавления.

    Returns:
        List[T]: Список добавленных записей.

    Raises:
        SQLAlchemyError: В случае ошибки при выполнении запроса к базе данных.
    """
```

**Описание**:
Добавление нескольких записей в базу данных.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия SQLAlchemy.
- `instances` (List[BaseModel]): Список Pydantic моделей с данными для добавления.

**Возвращает**:
- `List[T]`: Список добавленных записей.

**Вызывает исключения**:
- `SQLAlchemyError`: В случае ошибки при выполнении запроса к базе данных.

**Примеры**:
```python
# Пример вызова
# new_records = await BaseDAO.add_many(session=session, instances=instances)
```

### `update`

```python
@classmethod
async def update(cls, session: AsyncSession, filters: BaseModel, values: BaseModel):
    """
    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy.
        filters (BaseModel): Pydantic модель с фильтрами для обновления.
        values (BaseModel): Pydantic модель с данными для обновления.

    Returns:
        int: Количество обновленных записей.

    Raises:
        SQLAlchemyError: В случае ошибки при выполнении запроса к базе данных.
    """
```

**Описание**:
Обновление записей в базе данных по заданным фильтрам.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия SQLAlchemy.
- `filters` (BaseModel): Pydantic модель с фильтрами для обновления.
- `values` (BaseModel): Pydantic модель с данными для обновления.

**Возвращает**:
- `int`: Количество обновленных записей.

**Вызывает исключения**:
- `SQLAlchemyError`: В случае ошибки при выполнении запроса к базе данных.

**Примеры**:
```python
# Пример вызова
# updated_count = await BaseDAO.update(session=session, filters=filters, values=values)
```

### `delete`

```python
@classmethod
async def delete(cls, session: AsyncSession, filters: BaseModel):
    """
    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy.
        filters (BaseModel): Pydantic модель с фильтрами для удаления.

    Returns:
        int: Количество удаленных записей.

    Raises:
        SQLAlchemyError: В случае ошибки при выполнении запроса к базе данных.
        ValueError: Если не указаны фильтры для удаления.
    """
```

**Описание**:
Удаление записей из базы данных по заданным фильтрам.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия SQLAlchemy.
- `filters` (BaseModel): Pydantic модель с фильтрами для удаления.

**Возвращает**:
- `int`: Количество удаленных записей.

**Вызывает исключения**:
- `SQLAlchemyError`: В случае ошибки при выполнении запроса к базе данных.
- `ValueError`: Если не указаны фильтры для удаления.

**Примеры**:
```python
# Пример вызова
# deleted_count = await BaseDAO.delete(session=session, filters=filters)
```

### `count`

```python
@classmethod
async def count(cls, session: AsyncSession, filters: BaseModel | None = None):
    """
    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy.
        filters (BaseModel | None, optional): Pydantic модель с фильтрами для подсчета. Defaults to None.

    Returns:
        int: Количество записей, соответствующих фильтрам.

    Raises:
        SQLAlchemyError: В случае ошибки при выполнении запроса к базе данных.
    """
```

**Описание**:
Подсчет количества записей в базе данных по заданным фильтрам.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия SQLAlchemy.
- `filters` (BaseModel | None, optional): Pydantic модель с фильтрами для подсчета. По умолчанию `None`.

**Возвращает**:
- `int`: Количество записей, соответствующих фильтрам.

**Вызывает исключения**:
- `SQLAlchemyError`: В случае ошибки при выполнении запроса к базе данных.

**Примеры**:
```python
# Пример вызова
# count = await BaseDAO.count(session=session, filters=filters)
```

### `paginate`

```python
@classmethod
async def paginate(cls, session: AsyncSession, page: int = 1, page_size: int = 10, filters: BaseModel = None):
    """
    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy.
        page (int, optional): Номер страницы для пагинации. Defaults to 1.
        page_size (int, optional): Размер страницы для пагинации. Defaults to 10.
        filters (BaseModel, optional): Pydantic модель с фильтрами для пагинации. Defaults to None.

    Returns:
        List[T]: Список записей на указанной странице.

    Raises:
        SQLAlchemyError: В случае ошибки при выполнении запроса к базе данных.
    """
```

**Описание**:
Пагинация записей в базе данных по заданным фильтрам.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия SQLAlchemy.
- `page` (int, optional): Номер страницы для пагинации. По умолчанию `1`.
- `page_size` (int, optional): Размер страницы для пагинации. По умолчанию `10`.
- `filters` (BaseModel, optional): Pydantic модель с фильтрами для пагинации. По умолчанию `None`.

**Возвращает**:
- `List[T]`: Список записей на указанной странице.

**Вызывает исключения**:
- `SQLAlchemyError`: В случае ошибки при выполнении запроса к базе данных.

**Примеры**:
```python
# Пример вызова
# records = await BaseDAO.paginate(session=session, page=page, page_size=page_size, filters=filters)
```

### `find_by_ids`

```python
@classmethod
async def find_by_ids(cls, session: AsyncSession, ids: List[int]) -> List[Any]:
    """Найти несколько записей по списку ID"""
    """
    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy.
        ids (List[int]): Список ID записей для поиска.

    Returns:
        List[Any]: Список найденных записей.

    Raises:
        SQLAlchemyError: В случае ошибки при выполнении запроса к базе данных.
    """
```

**Описание**:
Найти несколько записей по списку ID.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия SQLAlchemy.
- `ids` (List[int]): Список ID записей для поиска.

**Возвращает**:
- `List[Any]`: Список найденных записей.

**Вызывает исключения**:
- `SQLAlchemyError`: В случае ошибки при выполнении запроса к базе данных.

**Примеры**:
```python
# Пример вызова
# records = await BaseDAO.find_by_ids(session=session, ids=ids)
```

### `upsert`

```python
@classmethod
async def upsert(cls, session: AsyncSession, unique_fields: List[str], values: BaseModel):
    """Создать запись или обновить существующую"""
    """
    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy.
        unique_fields (List[str]): Список уникальных полей для поиска существующей записи.
        values (BaseModel): Pydantic модель с данными для создания или обновления записи.

    Returns:
        T: Созданная или обновленная запись.

    Raises:
        SQLAlchemyError: В случае ошибки при выполнении запроса к базе данных.
    """
```

**Описание**:
Создать запись или обновить существующую.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия SQLAlchemy.
- `unique_fields` (List[str]): Список уникальных полей для поиска существующей записи.
- `values` (BaseModel): Pydantic модель с данными для создания или обновления записи.

**Возвращает**:
- `T`: Созданная или обновленная запись.

**Вызывает исключения**:
- `SQLAlchemyError`: В случае ошибки при выполнении запроса к базе данных.

**Примеры**:
```python
# Пример вызова
# record = await BaseDAO.upsert(session=session, unique_fields=unique_fields, values=values)
```

### `bulk_update`

```python
@classmethod
async def bulk_update(cls, session: AsyncSession, records: List[BaseModel]) -> int:
    """Массовое обновление записей"""
    """
    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy.
        records (List[BaseModel]): Список Pydantic моделей с данными для массового обновления.

    Returns:
        int: Количество обновленных записей.

    Raises:
        SQLAlchemyError: В случае ошибки при выполнении запроса к базе данных.
    """
```

**Описание**:
Массовое обновление записей.

**Параметры**:
- `session` (AsyncSession): Асинхронная сессия SQLAlchemy.
- `records` (List[BaseModel]): Список Pydantic моделей с данными для массового обновления.

**Возвращает**:
- `int`: Количество обновленных записей.

**Вызывает исключения**:
- `SQLAlchemyError`: В случае ошибки при выполнении запроса к базе данных.

**Примеры**:
```python
# Пример вызова
# updated_count = await BaseDAO.bulk_update(session=session, records=records)