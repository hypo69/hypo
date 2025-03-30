# Модуль `base.py`

## Обзор

Модуль `base.py` содержит базовый класс `BaseDAO`, который предоставляет набор общих методов для доступа к данным в базе данных. Он использует `SQLAlchemy` для взаимодействия с базой данных и предоставляет асинхронные методы для выполнения операций `CRUD` (создание, чтение, обновление, удаление). Этот класс предназначен для наследования другими `DAO` (Data Access Object) классами, которые будут работать с конкретными моделями базы данных.

## Подробней

`BaseDAO` предоставляет абстракцию над базовыми операциями с базой данных, такими как поиск, добавление, обновление и удаление записей. Он использует `AsyncSession` из `SQLAlchemy` для асинхронного взаимодействия с базой данных, что позволяет избежать блокировок и повысить производительность.
Модуль включает в себя обработку исключений `SQLAlchemyError` и использует `logger` для регистрации информации об операциях и ошибках.

## Классы

### `BaseDAO`

**Описание**:
Базовый класс для объектов доступа к данным (DAO). Предоставляет общие методы для выполнения операций CRUD с использованием `SQLAlchemy`.

**Параметры**:

- `model` (Type[T]): Тип модели базы данных, с которой работает DAO.

**Методы**:

- `find_one_or_none_by_id`: Находит запись по её ID.
- `find_one_or_none`: Находит одну запись по заданным фильтрам.
- `find_all`: Находит все записи, соответствующие заданным фильтрам.
- `add`: Добавляет одну запись в базу данных.
- `add_many`: Добавляет несколько записей в базу данных.
- `update`: Обновляет записи в базе данных, соответствующие заданным фильтрам.
- `delete`: Удаляет записи из базы данных, соответствующие заданным фильтрам.
- `count`: Подсчитывает количество записей, соответствующих заданным фильтрам.
- `paginate`: Получает записи постранично с учетом заданных фильтров.
- `find_by_ids`: Находит несколько записей по списку ID.
- `upsert`: Создает новую запись или обновляет существующую на основе уникальных полей.
- `bulk_update`: Массово обновляет записи в базе данных.

## Функции

### `find_one_or_none_by_id`

```python
@classmethod
async def find_one_or_none_by_id(cls, data_id: int, session: AsyncSession):
    """Найти запись по ID"""
```

**Описание**:

Находит запись в базе данных по указанному ID.

**Параметры**:

- `data_id` (int): ID записи, которую нужно найти.
- `session` (AsyncSession): Асинхронная сессия базы данных `SQLAlchemy`.

**Возвращает**:

- `T | None`: Возвращает найденную запись типа `T` или `None`, если запись не найдена.

**Вызывает исключения**:

- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример вызова функции
async def example():
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy.orm import declarative_base
    from typing import Optional
    from pydantic import BaseModel

    # Определите базовый класс для моделей SQLAlchemy
    Base = declarative_base()

    # Определите модель данных (пример)
    class MyModel(Base):
        __tablename__ = 'my_table'
        id = Column(Integer, primary_key=True)
        name = Column(String)

    # Создайте движок SQLAlchemy (замените URL на ваш реальный URL базы данных)
    engine = create_async_engine('sqlite+aiosqlite:///:memory:')

    # Асинхронная функция для создания таблиц
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    # Вызовите функцию для создания таблиц
    await create_tables()

    # Создайте сессию
    async with AsyncSession(engine) as session:
        # Пример использования find_one_or_none_by_id
        record_id = 1
        found_record = await BaseDAO[MyModel].find_one_or_none_by_id(record_id, session)

        if found_record:
            print(f"Record with ID {record_id} found: {found_record.name}")
        else:
            print(f"Record with ID {record_id} not found.")
```

### `find_one_or_none`

```python
@classmethod
async def find_one_or_none(cls, session: AsyncSession, filters: BaseModel):
    """Найти одну запись по фильтрам"""
```

**Описание**:

Находит одну запись в базе данных, соответствующую заданным фильтрам.

**Параметры**:

- `session` (AsyncSession): Асинхронная сессия базы данных `SQLAlchemy`.
- `filters` (BaseModel): Объект `BaseModel`, содержащий фильтры для поиска.

**Возвращает**:

- `T | None`: Возвращает найденную запись типа `T` или `None`, если запись не найдена.

**Вызывает исключения**:

- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример вызова функции
async def example():
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy.orm import declarative_base
    from typing import Optional
    from pydantic import BaseModel, Field

    # Определите базовый класс для моделей SQLAlchemy
    Base = declarative_base()

    # Определите модель данных (пример)
    class MyModel(Base):
        __tablename__ = 'my_table'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        value = Column(Integer)

    # Создайте движок SQLAlchemy (замените URL на ваш реальный URL базы данных)
    engine = create_async_engine('sqlite+aiosqlite:///:memory:')

    # Асинхронная функция для создания таблиц
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    # Вызовите функцию для создания таблиц
    await create_tables()

    # Создайте сессию
    async with AsyncSession(engine) as session:

        # Определите фильтры с использованием pydantic BaseModel
        class MyModelFilters(BaseModel):
            name: Optional[str] = Field(None, description="Name to filter by")
            value: Optional[int] = Field(None, description="Value to filter by")

        # Пример использования find_one_or_none
        filters = MyModelFilters(name="example_name", value=123)
        found_record = await BaseDAO[MyModel].find_one_or_none(session, filters)

        if found_record:
            print(f"Record found: {found_record.name}, {found_record.value}")
        else:
            print("Record not found.")
```

### `find_all`

```python
@classmethod
async def find_all(cls, session: AsyncSession, filters: BaseModel | None = None):
    """Найти все записи по фильтрам"""
```

**Описание**:

Находит все записи в базе данных, соответствующие заданным фильтрам.

**Параметры**:

- `session` (AsyncSession): Асинхронная сессия базы данных `SQLAlchemy`.
- `filters` (BaseModel | None, optional): Объект `BaseModel`, содержащий фильтры для поиска. По умолчанию `None`.

**Возвращает**:

- `List[T]`: Список найденных записей типа `T`.

**Вызывает исключения**:

- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример вызова функции
async def example():
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy.orm import declarative_base
    from typing import Optional, List
    from pydantic import BaseModel, Field
    from sqlalchemy import Column, Integer, String

    # Определите базовый класс для моделей SQLAlchemy
    Base = declarative_base()

    # Определите модель данных (пример)
    class MyModel(Base):
        __tablename__ = 'my_table'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        value = Column(Integer)

    # Создайте движок SQLAlchemy (замените URL на ваш реальный URL базы данных)
    engine = create_async_engine('sqlite+aiosqlite:///:memory:')

    # Асинхронная функция для создания таблиц
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    # Вызовите функцию для создания таблиц
    await create_tables()

    # Создайте сессию
    async with AsyncSession(engine) as session:

        # Определите фильтры с использованием pydantic BaseModel
        class MyModelFilters(BaseModel):
            name: Optional[str] = Field(None, description="Name to filter by")
            value: Optional[int] = Field(None, description="Value to filter by")

        # Пример использования find_all
        filters = MyModelFilters(name="example_name")
        found_records = await BaseDAO[MyModel].find_all(session, filters)

        if found_records:
            print(f"Found {len(found_records)} records.")
            for record in found_records:
                print(f"Record: {record.name}, {record.value}")
        else:
            print("No records found.")
```

### `add`

```python
@classmethod
async def add(cls, session: AsyncSession, values: BaseModel):
    """Добавить одну запись"""
```

**Описание**:

Добавляет одну запись в базу данных.

**Параметры**:

- `session` (AsyncSession): Асинхронная сессия базы данных `SQLAlchemy`.
- `values` (BaseModel): Объект `BaseModel`, содержащий значения для новой записи.

**Возвращает**:

- `T`: Возвращает созданную запись типа `T`.

**Вызывает исключения**:

- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример вызова функции
async def example():
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy.orm import declarative_base
    from typing import Optional
    from pydantic import BaseModel, Field
    from sqlalchemy import Column, Integer, String

    # Определите базовый класс для моделей SQLAlchemy
    Base = declarative_base()

    # Определите модель данных (пример)
    class MyModel(Base):
        __tablename__ = 'my_table'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        value = Column(Integer)

    # Создайте движок SQLAlchemy (замените URL на ваш реальный URL базы данных)
    engine = create_async_engine('sqlite+aiosqlite:///:memory:')

    # Асинхронная функция для создания таблиц
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    # Вызовите функцию для создания таблиц
    await create_tables()

    # Создайте сессию
    async with AsyncSession(engine) as session:
        # Определите модель данных с использованием pydantic BaseModel
        class MyModelCreate(BaseModel):
            name: str = Field(..., description="Name to create")
            value: int = Field(..., description="Value to create")

        # Пример использования add
        values = MyModelCreate(name="new_example", value=456)
        new_record = await BaseDAO[MyModel].add(session, values)

        print(f"New record added: {new_record.name}, {new_record.value}")
```

### `add_many`

```python
@classmethod
async def add_many(cls, session: AsyncSession, instances: List[BaseModel]):
    """Добавить несколько записей"""
```

**Описание**:

Добавляет несколько записей в базу данных.

**Параметры**:

- `session` (AsyncSession): Асинхронная сессия базы данных `SQLAlchemy`.
- `instances` (List[BaseModel]): Список объектов `BaseModel`, содержащих значения для новых записей.

**Возвращает**:

- `List[T]`: Список созданных записей типа `T`.

**Вызывает исключения**:

- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример вызова функции
async def example():
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy.orm import declarative_base
    from typing import Optional, List
    from pydantic import BaseModel, Field
    from sqlalchemy import Column, Integer, String

    # Определите базовый класс для моделей SQLAlchemy
    Base = declarative_base()

    # Определите модель данных (пример)
    class MyModel(Base):
        __tablename__ = 'my_table'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        value = Column(Integer)

    # Создайте движок SQLAlchemy (замените URL на ваш реальный URL базы данных)
    engine = create_async_engine('sqlite+aiosqlite:///:memory:')

    # Асинхронная функция для создания таблиц
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    # Вызовите функцию для создания таблиц
    await create_tables()

    # Создайте сессию
    async with AsyncSession(engine) as session:
        # Определите модель данных с использованием pydantic BaseModel
        class MyModelCreate(BaseModel):
            name: str = Field(..., description="Name to create")
            value: int = Field(..., description="Value to create")

        # Пример использования add_many
        instances = [
            MyModelCreate(name="new_example_1", value=456),
            MyModelCreate(name="new_example_2", value=789)
        ]
        new_records = await BaseDAO[MyModel].add_many(session, instances)

        print(f"Added {len(new_records)} new records.")
        for record in new_records:
            print(f"Record: {record.name}, {record.value}")
```

### `update`

```python
@classmethod
async def update(cls, session: AsyncSession, filters: BaseModel, values: BaseModel):
    """Обновить записи по фильтрам"""
```

**Описание**:

Обновляет записи в базе данных, соответствующие заданным фильтрам.

**Параметры**:

- `session` (AsyncSession): Асинхронная сессия базы данных `SQLAlchemy`.
- `filters` (BaseModel): Объект `BaseModel`, содержащий фильтры для поиска записей для обновления.
- `values` (BaseModel): Объект `BaseModel`, содержащий значения для обновления.

**Возвращает**:

- `int`: Количество обновленных записей.

**Вызывает исключения**:

- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример вызова функции
async def example():
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy.orm import declarative_base
    from typing import Optional, List
    from pydantic import BaseModel, Field
    from sqlalchemy import Column, Integer, String

    # Определите базовый класс для моделей SQLAlchemy
    Base = declarative_base()

    # Определите модель данных (пример)
    class MyModel(Base):
        __tablename__ = 'my_table'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        value = Column(Integer)

    # Создайте движок SQLAlchemy (замените URL на ваш реальный URL базы данных)
    engine = create_async_engine('sqlite+aiosqlite:///:memory:')

    # Асинхронная функция для создания таблиц
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    # Вызовите функцию для создания таблиц
    await create_tables()

    # Создайте сессию
    async with AsyncSession(engine) as session:
        # Определите модель данных с использованием pydantic BaseModel
        class MyModelFilters(BaseModel):
            id: int = Field(..., description="ID to filter by")

        class MyModelUpdate(BaseModel):
            name: Optional[str] = Field(None, description="Name to update")
            value: Optional[int] = Field(None, description="Value to update")

        # Пример использования update
        filters = MyModelFilters(id=1)
        values = MyModelUpdate(name="updated_example", value=789)
        updated_count = await BaseDAO[MyModel].update(session, filters, values)

        print(f"Updated {updated_count} records.")
```

### `delete`

```python
@classmethod
async def delete(cls, session: AsyncSession, filters: BaseModel):
    """Удалить записи по фильтру"""
```

**Описание**:

Удаляет записи из базы данных, соответствующие заданным фильтрам.

**Параметры**:

- `session` (AsyncSession): Асинхронная сессия базы данных `SQLAlchemy`.
- `filters` (BaseModel): Объект `BaseModel`, содержащий фильтры для поиска записей для удаления.

**Возвращает**:

- `int`: Количество удаленных записей.

**Вызывает исключения**:

- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.
- `ValueError`: Если не указаны фильтры для удаления.

**Примеры**:

```python
# Пример вызова функции
async def example():
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy.orm import declarative_base
    from typing import Optional, List
    from pydantic import BaseModel, Field
    from sqlalchemy import Column, Integer, String

    # Определите базовый класс для моделей SQLAlchemy
    Base = declarative_base()

    # Определите модель данных (пример)
    class MyModel(Base):
        __tablename__ = 'my_table'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        value = Column(Integer)

    # Создайте движок SQLAlchemy (замените URL на ваш реальный URL базы данных)
    engine = create_async_engine('sqlite+aiosqlite:///:memory:')

    # Асинхронная функция для создания таблиц
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    # Вызовите функцию для создания таблиц
    await create_tables()

    # Создайте сессию
    async with AsyncSession(engine) as session:
        # Определите модель данных с использованием pydantic BaseModel
        class MyModelFilters(BaseModel):
            id: int = Field(..., description="ID to filter by")

        # Пример использования delete
        filters = MyModelFilters(id=1)
        deleted_count = await BaseDAO[MyModel].delete(session, filters)

        print(f"Deleted {deleted_count} records.")
```

### `count`

```python
@classmethod
async def count(cls, session: AsyncSession, filters: BaseModel | None = None):
    """Подсчитать количество записей"""
```

**Описание**:

Подсчитывает количество записей в базе данных, соответствующих заданным фильтрам.

**Параметры**:

- `session` (AsyncSession): Асинхронная сессия базы данных `SQLAlchemy`.
- `filters` (BaseModel | None, optional): Объект `BaseModel`, содержащий фильтры для поиска. По умолчанию `None`.

**Возвращает**:

- `int`: Количество записей, соответствующих заданным фильтрам.

**Вызывает исключения**:

- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример вызова функции
async def example():
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy.orm import declarative_base
    from typing import Optional, List
    from pydantic import BaseModel, Field
    from sqlalchemy import Column, Integer, String

    # Определите базовый класс для моделей SQLAlchemy
    Base = declarative_base()

    # Определите модель данных (пример)
    class MyModel(Base):
        __tablename__ = 'my_table'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        value = Column(Integer)

    # Создайте движок SQLAlchemy (замените URL на ваш реальный URL базы данных)
    engine = create_async_engine('sqlite+aiosqlite:///:memory:')

    # Асинхронная функция для создания таблиц
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    # Вызовите функцию для создания таблиц
    await create_tables()

    # Создайте сессию
    async with AsyncSession(engine) as session:
        # Определите модель данных с использованием pydantic BaseModel
        class MyModelFilters(BaseModel):
            name: Optional[str] = Field(None, description="Name to filter by")

        # Пример использования count
        filters = MyModelFilters(name="example_name")
        count = await BaseDAO[MyModel].count(session, filters)

        print(f"Found {count} records.")
```

### `paginate`

```python
@classmethod
async def paginate(cls, session: AsyncSession, page: int = 1, page_size: int = 10, filters: BaseModel = None):
    """Пагинация записей"""
```

**Описание**:

Получает записи из базы данных постранично с учетом заданных фильтров.

**Параметры**:

- `session` (AsyncSession): Асинхронная сессия базы данных `SQLAlchemy`.
- `page` (int, optional): Номер страницы для отображения. По умолчанию `1`.
- `page_size` (int, optional): Количество записей на странице. По умолчанию `10`.
- `filters` (BaseModel, optional): Объект `BaseModel`, содержащий фильтры для поиска. По умолчанию `None`.

**Возвращает**:

- `List[T]`: Список записей типа `T`, соответствующих заданной странице и размеру страницы.

**Вызывает исключения**:

- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример вызова функции
async def example():
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy.orm import declarative_base
    from typing import Optional, List
    from pydantic import BaseModel, Field
    from sqlalchemy import Column, Integer, String

    # Определите базовый класс для моделей SQLAlchemy
    Base = declarative_base()

    # Определите модель данных (пример)
    class MyModel(Base):
        __tablename__ = 'my_table'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        value = Column(Integer)

    # Создайте движок SQLAlchemy (замените URL на ваш реальный URL базы данных)
    engine = create_async_engine('sqlite+aiosqlite:///:memory:')

    # Асинхронная функция для создания таблиц
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    # Вызовите функцию для создания таблиц
    await create_tables()

    # Создайте сессию
    async with AsyncSession(engine) as session:
        # Определите модель данных с использованием pydantic BaseModel
        class MyModelFilters(BaseModel):
            name: Optional[str] = Field(None, description="Name to filter by")

        # Пример использования paginate
        filters = MyModelFilters(name="example_name")
        page = 1
        page_size = 5
        records = await BaseDAO[MyModel].paginate(session, page, page_size, filters)

        print(f"Found {len(records)} records on page {page}.")
        for record in records:
            print(f"Record: {record.name}, {record.value}")
```

### `find_by_ids`

```python
@classmethod
async def find_by_ids(cls, session: AsyncSession, ids: List[int]) -> List[Any]:
    """Найти несколько записей по списку ID"""
```

**Описание**:

Находит несколько записей по списку ID.

**Параметры**:

- `session` (AsyncSession): Асинхронная сессия базы данных `SQLAlchemy`.
- `ids` (List[int]): Список ID записей, которые нужно найти.

**Возвращает**:

- `List[Any]`: Список найденных записей.

**Вызывает исключения**:

- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример вызова функции
async def example():
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy.orm import declarative_base
    from typing import Optional, List
    from pydantic import BaseModel, Field
    from sqlalchemy import Column, Integer, String

    # Определите базовый класс для моделей SQLAlchemy
    Base = declarative_base()

    # Определите модель данных (пример)
    class MyModel(Base):
        __tablename__ = 'my_table'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        value = Column(Integer)

    # Создайте движок SQLAlchemy (замените URL на ваш реальный URL базы данных)
    engine = create_async_engine('sqlite+aiosqlite:///:memory:')

    # Асинхронная функция для создания таблиц
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    # Вызовите функцию для создания таблиц
    await create_tables()

    # Создайте сессию
    async with AsyncSession(engine) as session:
        # Пример использования find_by_ids
        ids = [1, 2, 3]
        records = await BaseDAO[MyModel].find_by_ids(session, ids)

        print(f"Found {len(records)} records by IDs.")
        for record in records:
            print(f"Record: {record.name}, {record.value}")
```

### `upsert`

```python
@classmethod
async def upsert(cls, session: AsyncSession, unique_fields: List[str], values: BaseModel):
    """Создать запись или обновить существующую"""
```

**Описание**:

Создает запись в базе данных или обновляет существующую, если запись с указанными уникальными полями уже существует.

**Параметры**:

- `session` (AsyncSession): Асинхронная сессия базы данных `SQLAlchemy`.
- `unique_fields` (List[str]): Список уникальных полей, которые используются для поиска существующей записи.
- `values` (BaseModel): Объект `BaseModel`, содержащий значения для создания или обновления записи.

**Возвращает**:

- `T`: Возвращает созданную или обновленную запись типа `T`.

**Вызывает исключения**:

- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример вызова функции
async def example():
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy.orm import declarative_base
    from typing import Optional, List
    from pydantic import BaseModel, Field
    from sqlalchemy import Column, Integer, String

    # Определите базовый класс для моделей SQLAlchemy
    Base = declarative_base()

    # Определите модель данных (пример)
    class MyModel(Base):
        __tablename__ = 'my_table'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        value = Column(Integer)

    # Создайте движок SQLAlchemy (замените URL на ваш реальный URL базы данных)
    engine = create_async_engine('sqlite+aiosqlite:///:memory:')

    # Асинхронная функция для создания таблиц
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    # Вызовите функцию для создания таблиц
    await create_tables()

    # Создайте сессию
    async with AsyncSession(engine) as session:
        # Определите модель данных с использованием pydantic BaseModel
        class MyModelCreate(BaseModel):
            name: str = Field(..., description="Name")
            value: int = Field(..., description="Value")

        # Пример использования upsert
        unique_fields = ["name"]
        values = MyModelCreate(name="unique_example", value=123)
        record = await BaseDAO[MyModel].upsert(session, unique_fields, values)

        print(f"Record upserted: {record.name}, {record.value}")
```

### `bulk_update`

```python
@classmethod
async def bulk_update(cls, session: AsyncSession, records: List[BaseModel]) -> int:
    """Массовое обновление записей"""
```

**Описание**:

Массово обновляет записи в базе данных.

**Параметры**:

- `session` (AsyncSession): Асинхронная сессия базы данных `SQLAlchemy`.
- `records` (List[BaseModel]): Список объектов `BaseModel`, содержащих значения для обновления. Каждый объект должен содержать поле `id` для идентификации записи.

**Возвращает**:

- `int`: Количество обновленных записей.

**Вызывает исключения**:

- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример вызова функции
async def example():
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy.orm import declarative_base
    from typing import Optional, List
    from pydantic import BaseModel, Field
    from sqlalchemy import Column, Integer, String

    # Определите базовый класс для моделей SQLAlchemy
    Base = declarative_base()

    # Определите модель данных (пример)
    class MyModel(Base):
        __tablename__ = 'my_table'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        value = Column(Integer)

    # Создайте движок SQLAlchemy (замените URL на ваш реальный URL базы данных)
    engine = create_async_engine('sqlite+aiosqlite:///:memory:')

    # Асинхронная функция для создания таблиц
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    # Вызовите функцию для создания таблиц
    await create_tables()

    # Создайте сессию
    async with AsyncSession(engine) as session:
        # Определите модель данных с использованием pydantic BaseModel
        class MyModelUpdate(BaseModel):
            id: int = Field(..., description="ID of the record to update")
            name: Optional[str] = Field(None, description="New name")
            value: Optional[int] = Field(None, description="New value")

        # Пример использования bulk_update
        records = [
            MyModelUpdate(id=1, name="updated_example_1", value=456),
            MyModelUpdate(id=2, name="updated_example_2", value=789)
        ]
        updated_count = await BaseDAO[MyModel].bulk_update(session, records)

        print(f"Bulk updated {updated_count} records.")