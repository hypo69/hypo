# Модуль `base.py`

## Обзор

Модуль `base.py` содержит абстрактный базовый класс `BaseDAO`, предназначенный для осуществления взаимодействия с базой данных. Он предоставляет набор асинхронных методов для выполнения основных операций CRUD (Create, Read, Update, Delete) и других полезных операций, таких как пагинация и подсчет записей. Класс использует `SQLAlchemy` для работы с базой данных и `pydantic` для валидации данных.

## Подробнее

`BaseDAO` предназначен для наследования другими DAO (Data Access Object) классами, специфичными для каждой таблицы базы данных. Он предоставляет общую логику для работы с базой данных, такую как поиск, добавление, обновление и удаление записей. Это позволяет избежать дублирования кода и обеспечивает единообразный интерфейс для работы с различными таблицами.

## Классы

### `BaseDAO`

**Описание**:
Абстрактный базовый класс для Data Access Objects. Предоставляет общие методы для взаимодействия с базой данных, такие как создание, чтение, обновление и удаление записей.

**Принцип работы**:
Класс параметризуется типовым параметром `T`, который должен быть наследником класса `Base` из `SQLAlchemy`. Это гарантирует, что все DAO работают с моделями, представляющими таблицы базы данных. Класс предоставляет асинхронные методы для выполнения различных операций с базой данных, используя `SQLAlchemy` для построения и выполнения запросов.

**Атрибуты**:
- `model` (type[T]): Тип модели SQLAlchemy, с которой работает DAO.

**Методы**:
- `find_one_or_none_by_id(data_id: int, session: AsyncSession)`: Находит запись по ID.
- `find_one_or_none(session: AsyncSession, filters: BaseModel)`: Находит одну запись по фильтрам.
- `find_all(session: AsyncSession, filters: BaseModel | None = None)`: Находит все записи по фильтрам.
- `add(session: AsyncSession, values: BaseModel)`: Добавляет одну запись.
- `add_many(session: AsyncSession, instances: List[BaseModel])`: Добавляет несколько записей.
- `update(session: AsyncSession, filters: BaseModel, values: BaseModel)`: Обновляет записи по фильтрам.
- `delete(session: AsyncSession, filters: BaseModel)`: Удаляет записи по фильтру.
- `count(session: AsyncSession, filters: BaseModel | None = None)`: Подсчитывает количество записей.
- `paginate(session: AsyncSession, page: int = 1, page_size: int = 10, filters: BaseModel = None)`: Пагинация записей.
- `find_by_ids(session: AsyncSession, ids: List[int])`: Найти несколько записей по списку ID
- `upsert(session: AsyncSession, unique_fields: List[str], values: BaseModel)`: Создать запись или обновить существующую
- `bulk_update(session: AsyncSession, records: List[BaseModel]) -> int`: Массовое обновление записей

## Функции

### `find_one_or_none_by_id`

```python
@classmethod
async def find_one_or_none_by_id(cls, data_id: int, session: AsyncSession):
    """Найти запись по ID"""
```

**Назначение**:
Находит запись в базе данных по указанному ID.

**Параметры**:
- `data_id` (int): ID записи для поиска.
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.

**Возвращает**:
- `T | None`: Объект модели, если запись найдена, иначе `None`.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Как работает функция**:

1. Логирует информацию о поиске записи с указанным ID.
2. Формирует запрос `SQLAlchemy` для поиска записи в таблице, соответствующей модели `cls.model`, с указанным `id`.
3. Выполняет запрос асинхронно с использованием `session.execute()`.
4. Извлекает результат запроса с использованием `result.scalar_one_or_none()`.
5. Логирует информацию о том, была ли найдена запись.
6. Возвращает найденную запись или `None`, если запись не найдена.
7. В случае возникновения ошибки `SQLAlchemyError`, логирует информацию об ошибке и пробрасывает исключение.

```
A[Логирование начала поиска]
|
B[Формирование запроса SQLAlchemy]
|
C[Выполнение запроса в БД]
|
D[Получение результата]
|
E[Логирование результата]
|
F[Возврат результата]
```

**Примеры**:

```python
# Пример использования
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

class MyModel(Base):
    __tablename__ = 'my_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class MyDAO(BaseDAO[MyModel]):
    model = MyModel

async def test_find_one_or_none_by_id(async_session: AsyncSession):
    async with async_session() as session:
        # Предположим, что запись с id=1 существует
        record = await MyDAO.find_one_or_none_by_id(1, session)
        if record:
            print(f"Найдена запись с id=1: {record.name}")
        else:
            print("Запись с id=1 не найдена")

```

### `find_one_or_none`

```python
    @classmethod
    async def find_one_or_none(cls, session: AsyncSession, filters: BaseModel):
        """Найти одну запись по фильтрам"""
```

**Назначение**:
Находит одну запись в базе данных, соответствующую заданным фильтрам.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия `SQLAlchemy` для выполнения запросов к базе данных.
- `filters` (BaseModel): Объект `BaseModel`, содержащий фильтры для поиска записи.

**Возвращает**:
- `T | None`: Объект модели, если запись найдена, иначе `None`.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Как работает функция**:

1. Преобразует объект `filters` в словарь, исключая неустановленные значения.
2. Логирует информацию о поиске одной записи с указанными фильтрами.
3. Формирует запрос `SQLAlchemy` для поиска записи в таблице, соответствующей модели `cls.model`, с использованием фильтров из словаря.
4. Выполняет запрос асинхронно с использованием `session.execute()`.
5. Извлекает результат запроса с использованием `result.scalar_one_or_none()`.
6. Логирует информацию о том, была ли найдена запись.
7. Возвращает найденную запись или `None`, если запись не найдена.
8. В случае возникновения ошибки `SQLAlchemyError`, логирует информацию об ошибке и пробрасывает исключение.

```
A[Преобразование фильтров в словарь]
|
B[Логирование начала поиска]
|
C[Формирование запроса SQLAlchemy]
|
D[Выполнение запроса в БД]
|
E[Получение результата]
|
F[Логирование результата]
|
G[Возврат результата]
```

**Примеры**:

```python
# Пример использования
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

class MyModel(Base):
    __tablename__ = 'my_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class MyFilter(BaseModel):
    name: str

class MyDAO(BaseDAO[MyModel]):
    model = MyModel

async def test_find_one_or_none(async_session: AsyncSession):
    async with async_session() as session:
        filters = MyFilter(name="Example")
        record = await MyDAO.find_one_or_none(session, filters)
        if record:
            print(f"Найдена запись с name='Example': {record.id}")
        else:
            print("Запись с name='Example' не найдена")
```

### `find_all`

```python
    @classmethod
    async def find_all(cls, session: AsyncSession, filters: BaseModel | None = None):
        """Найти все записи по фильтрам"""
```

**Назначение**:
Находит все записи в базе данных, соответствующие заданным фильтрам.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `filters` (BaseModel | None): Объект BaseModel, содержащий фильтры для поиска записей. Если `None`, возвращаются все записи.

**Возвращает**:
- `List[T]`: Список объектов модели, соответствующих фильтрам.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Как работает функция**:

1. Преобразует объект `filters` в словарь, исключая неустановленные значения, если `filters` не `None`.
2. Логирует информацию о поиске всех записей с указанными фильтрами.
3. Формирует запрос SQLAlchemy для поиска записей в таблице, соответствующей модели `cls.model`, с использованием фильтров из словаря.
4. Выполняет запрос асинхронно с использованием `session.execute()`.
5. Извлекает все результаты запроса с использованием `result.scalars().all()`.
6. Логирует информацию о количестве найденных записей.
7. Возвращает список найденных записей.
8. В случае возникновения ошибки `SQLAlchemyError`, логирует информацию об ошибке и пробрасывает исключение.

```
A[Преобразование фильтров в словарь]
|
B[Логирование начала поиска]
|
C[Формирование запроса SQLAlchemy]
|
D[Выполнение запроса в БД]
|
E[Получение результатов]
|
F[Логирование результатов]
|
G[Возврат результатов]
```

**Примеры**:

```python
# Пример использования
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

class MyModel(Base):
    __tablename__ = 'my_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class MyFilter(BaseModel):
    name: str

class MyDAO(BaseDAO[MyModel]):
    model = MyModel

async def test_find_all(async_session: AsyncSession):
    async with async_session() as session:
        filters = MyFilter(name="Example")
        records = await MyDAO.find_all(session, filters)
        print(f"Найдено {len(records)} записей с name='Example'")
```

### `add`

```python
    @classmethod
    async def add(cls, session: AsyncSession, values: BaseModel):
        """Добавить одну запись"""
```

**Назначение**:
Добавляет одну запись в базу данных.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `values` (BaseModel): Объект BaseModel, содержащий значения для добавления новой записи.

**Возвращает**:
- `T`: Объект созданной модели.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Как работает функция**:

1. Преобразует объект `values` в словарь, исключая неустановленные значения.
2. Логирует информацию о добавлении записи с указанными параметрами.
3. Создает новый экземпляр модели `cls.model` с использованием значений из словаря.
4. Добавляет новый экземпляр в сессию SQLAlchemy.
5. Пытается выполнить операцию добавления в базе данных с использованием `session.flush()`.
6. Логирует информацию об успешном добавлении записи.
7. В случае возникновения ошибки `SQLAlchemyError`, выполняет откат транзакции с использованием `session.rollback()`, логирует информацию об ошибке и пробрасывает исключение.
8. Возвращает созданный экземпляр модели.

```
A[Преобразование значений в словарь]
|
B[Логирование начала добавления]
|
C[Создание нового экземпляра модели]
|
D[Добавление экземпляра в сессию]
|
E[Выполнение операции добавления в БД]
|
F[Логирование успеха]
|
G[Возврат экземпляра модели]
```

**Примеры**:

```python
# Пример использования
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

class MyModel(Base):
    __tablename__ = 'my_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class MyCreate(BaseModel):
    name: str

class MyDAO(BaseDAO[MyModel]):
    model = MyModel

async def test_add(async_session: AsyncSession):
    async with async_session() as session:
        values = MyCreate(name="New Example")
        new_record = await MyDAO.add(session, values)
        print(f"Добавлена запись с id={new_record.id} и name='{new_record.name}'")
```

### `add_many`

```python
    @classmethod
    async def add_many(cls, session: AsyncSession, instances: List[BaseModel]):
        """Добавить несколько записей"""
```

**Назначение**:
Добавляет несколько записей в базу данных.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `instances` (List[BaseModel]): Список объектов BaseModel, содержащих значения для добавления новых записей.

**Возвращает**:
- `List[T]`: Список объектов созданных моделей.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Как работает функция**:

1. Преобразует каждый объект из списка `instances` в словарь, исключая неустановленные значения.
2. Логирует информацию о добавлении нескольких записей.
3. Создает список новых экземпляров модели `cls.model` с использованием значений из словарей.
4. Добавляет все новые экземпляры в сессию SQLAlchemy.
5. Пытается выполнить операцию добавления в базе данных с использованием `session.flush()`.
6. Логирует информацию об успешном добавлении записей.
7. В случае возникновения ошибки `SQLAlchemyError`, выполняет откат транзакции с использованием `session.rollback()`, логирует информацию об ошибке и пробрасывает исключение.
8. Возвращает список созданных экземпляров моделей.

```
A[Преобразование значений в список словарей]
|
B[Логирование начала добавления]
|
C[Создание списка новых экземпляров модели]
|
D[Добавление экземпляров в сессию]
|
E[Выполнение операции добавления в БД]
|
F[Логирование успеха]
|
G[Возврат списка экземпляров модели]
```

**Примеры**:

```python
# Пример использования
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from typing import List

class MyModel(Base):
    __tablename__ = 'my_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class MyCreate(BaseModel):
    name: str

class MyDAO(BaseDAO[MyModel]):
    model = MyModel

async def test_add_many(async_session: AsyncSession):
    async with async_session() as session:
        values = [
            MyCreate(name="Example 1"),
            MyCreate(name="Example 2")
        ]
        new_records = await MyDAO.add_many(session, values)
        print(f"Добавлено {len(new_records)} записей")
```

### `update`

```python
    @classmethod
    async def update(cls, session: AsyncSession, filters: BaseModel, values: BaseModel):
        """Обновить записи по фильтрам"""
```

**Назначение**:
Обновляет записи в базе данных, соответствующие заданным фильтрам, новыми значениями.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `filters` (BaseModel): Объект BaseModel, содержащий фильтры для поиска записей, которые нужно обновить.
- `values` (BaseModel): Объект BaseModel, содержащий новые значения для обновления записей.

**Возвращает**:
- `int`: Количество обновленных записей.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Как работает функция**:

1. Преобразует объекты `filters` и `values` в словари, исключая неустановленные значения.
2. Логирует информацию об обновлении записей с указанными фильтрами и значениями.
3. Формирует запрос `SQLAlchemy` для обновления записей в таблице, соответствующей модели `cls.model`, с использованием фильтров из словаря `filter_dict` и новых значений из словаря `values_dict`.
4. Выполняет запрос асинхронно с использованием `session.execute()`.
5. Выполняет операцию обновления в базе данных с использованием `session.flush()`.
6. Логирует информацию о количестве обновленных записей.
7. Возвращает количество обновленных записей.
8. В случае возникновения ошибки `SQLAlchemyError`, выполняет откат транзакции с использованием `session.rollback()`, логирует информацию об ошибке и пробрасывает исключение.

```
A[Преобразование фильтров и значений в словари]
|
B[Логирование начала обновления]
|
C[Формирование запроса SQLAlchemy]
|
D[Выполнение запроса в БД]
|
E[Выполнение операции обновления в БД]
|
F[Логирование количества обновленных записей]
|
G[Возврат количества обновленных записей]
```

**Примеры**:

```python
# Пример использования
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MyModel(Base):
    __tablename__ = 'my_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class MyFilter(BaseModel):
    id: int

class MyUpdate(BaseModel):
    name: str

class MyDAO(BaseDAO[MyModel]):
    model = MyModel

async def test_update(async_session: AsyncSession):
    async with async_session() as session:
        #  Предположим, что запись с id=1 существует
        filters = MyFilter(id=1)
        values = MyUpdate(name="Updated Example")
        updated_count = await MyDAO.update(session, filters, values)
        print(f"Обновлено {updated_count} записей")
```

### `delete`

```python
    @classmethod
    async def delete(cls, session: AsyncSession, filters: BaseModel):
        """Удалить записи по фильтру"""
```

**Назначение**:
Удаляет записи из базы данных, соответствующие заданным фильтрам.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `filters` (BaseModel): Объект BaseModel, содержащий фильтры для поиска записей, которые нужно удалить.

**Возвращает**:
- `int`: Количество удаленных записей.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.
- `ValueError`: Если не указан ни один фильтр для удаления.

**Как работает функция**:

1. Преобразует объект `filters` в словарь, исключая неустановленные значения.
2. Логирует информацию об удалении записей с указанными фильтрами.
3. Проверяет, что указан хотя бы один фильтр для удаления. Если фильтры не указаны, выбрасывает исключение `ValueError`.
4. Формирует запрос SQLAlchemy для удаления записей из таблицы, соответствующей модели `cls.model`, с использованием фильтров из словаря.
5. Выполняет запрос асинхронно с использованием `session.execute()`.
6. Выполняет операцию удаления в базе данных с использованием `session.flush()`.
7. Логирует информацию о количестве удаленных записей.
8. Возвращает количество удаленных записей.
9. В случае возникновения ошибки `SQLAlchemyError`, выполняет откат транзакции с использованием `session.rollback()`, логирует информацию об ошибке и пробрасывает исключение.

```
A[Преобразование фильтров в словарь]
|
B[Логирование начала удаления]
|
C[Проверка наличия фильтров]
|
D[Формирование запроса SQLAlchemy]
|
E[Выполнение запроса в БД]
|
F[Выполнение операции удаления в БД]
|
G[Логирование количества удаленных записей]
|
H[Возврат количества удаленных записей]
```

**Примеры**:

```python
# Пример использования
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MyModel(Base):
    __tablename__ = 'my_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class MyFilter(BaseModel):
    id: int

class MyDAO(BaseDAO[MyModel]):
    model = MyModel

async def test_delete(async_session: AsyncSession):
    async with async_session() as session:
        # Предположим, что запись с id=1 существует
        filters = MyFilter(id=1)
        deleted_count = await MyDAO.delete(session, filters)
        print(f"Удалено {deleted_count} записей")
```

### `count`

```python
    @classmethod
    async def count(cls, session: AsyncSession, filters: BaseModel | None = None):
        """Подсчитать количество записей"""
```

**Назначение**:
Подсчитывает количество записей в базе данных, соответствующих заданным фильтрам.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `filters` (BaseModel | None): Объект BaseModel, содержащий фильтры для поиска записей. Если `None`, подсчитываются все записи.

**Возвращает**:
- `int`: Количество записей, соответствующих фильтрам.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Как работает функция**:

1. Преобразует объект `filters` в словарь, исключая неустановленные значения, если `filters` не `None`.
2. Логирует информацию о подсчете количества записей с указанными фильтрами.
3. Формирует запрос SQLAlchemy для подсчета количества записей в таблице, соответствующей модели `cls.model`, с использованием фильтров из словаря.
4. Выполняет запрос асинхронно с использованием `session.execute()`.
5. Извлекает результат запроса с использованием `result.scalar()`.
6. Логирует информацию о количестве найденных записей.
7. Возвращает количество найденных записей.
8. В случае возникновения ошибки `SQLAlchemyError`, логирует информацию об ошибке и пробрасывает исключение.

```
A[Преобразование фильтров в словарь]
|
B[Логирование начала подсчета]
|
C[Формирование запроса SQLAlchemy]
|
D[Выполнение запроса в БД]
|
E[Получение результата]
|
F[Логирование результата]
|
G[Возврат результата]
```

**Примеры**:

```python
# Пример использования
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MyModel(Base):
    __tablename__ = 'my_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class MyFilter(BaseModel):
    name: str

class MyDAO(BaseDAO[MyModel]):
    model = MyModel

async def test_count(async_session: AsyncSession):
    async with async_session() as session:
        filters = MyFilter(name="Example")
        count = await MyDAO.count(session, filters)
        print(f"Найдено {count} записей с name='Example'")
```

### `paginate`

```python
    @classmethod
    async def paginate(cls, session: AsyncSession, page: int = 1, page_size: int = 10, filters: BaseModel = None):
        """Пагинация записей"""
```

**Назначение**:
Возвращает записи из базы данных для заданной страницы с учетом размера страницы и фильтров.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `page` (int): Номер страницы для извлечения (по умолчанию: 1).
- `page_size` (int): Количество записей на странице (по умолчанию: 10).
- `filters` (BaseModel | None): Объект BaseModel, содержащий фильтры для поиска записей. Если `None`, возвращаются все записи.

**Возвращает**:
- `List[T]`: Список объектов модели, соответствующих фильтрам и находящихся на заданной странице.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Как работает функция**:

1. Преобразует объект `filters` в словарь, исключая неустановленные значения, если `filters` не `None`.
2. Логирует информацию о пагинации записей с указанными фильтрами, страницей и размером страницы.
3. Формирует запрос SQLAlchemy для поиска записей в таблице, соответствующей модели `cls.model`, с использованием фильтров из словаря, смещения и лимита для пагинации.
4. Выполняет запрос асинхронно с использованием `session.execute()`.
5. Извлекает все результаты запроса с использованием `result.scalars().all()`.
6. Логирует информацию о количестве найденных записей на странице.
7. Возвращает список найденных записей.
8. В случае возникновения ошибки `SQLAlchemyError`, логирует информацию об ошибке и пробрасывает исключение.

```
A[Преобразование фильтров в словарь]
|
B[Логирование начала пагинации]
|
C[Формирование запроса SQLAlchemy]
|
D[Выполнение запроса в БД]
|
E[Получение результатов]
|
F[Логирование результатов]
|
G[Возврат результатов]
```

**Примеры**:

```python
# Пример использования
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MyModel(Base):
    __tablename__ = 'my_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class MyFilter(BaseModel):
    name: str

class MyDAO(BaseDAO[MyModel]):
    model = MyModel

async def test_paginate(async_session: AsyncSession):
    async with async_session() as session:
        filters = MyFilter(name="Example")
        page = 2
        page_size = 10
        records = await MyDAO.paginate(session, page, page_size, filters)
        print(f"Найдено {len(records)} записей на странице {page}")
```

### `find_by_ids`

```python
    @classmethod
    async def find_by_ids(cls, session: AsyncSession, ids: List[int]) -> List[Any]:
        """Найти несколько записей по списку ID"""
```

**Назначение**:
Находит несколько записей в базе данных по списку их идентификаторов.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `ids` (List[int]): Список идентификаторов записей, которые нужно найти.

**Возвращает**:
- `List[Any]`: Список найденных записей.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Как работает функция**:

1. Логирует информацию о поиске записей по списку ID.
2. Формирует запрос SQLAlchemy для поиска записей в таблице, соответствующей модели `cls.model`, с использованием фильтра по списку ID.
3. Выполняет запрос асинхронно с использованием `session.execute()`.
4. Извлекает все результаты запроса с использованием `result.scalars().all()`.
5. Логирует информацию о количестве найденных записей.
6. Возвращает список найденных записей.
7. В случае возникновения ошибки `SQLAlchemyError`, логирует информацию об ошибке и пробрасывает исключение.

```
A[Логирование начала поиска]
|
B[Формирование запроса SQLAlchemy]
|
C[Выполнение запроса в БД]
|
D[Получение результатов]
|
E[Логирование результатов]
|
F[Возврат результатов]
```

**Примеры**:

```python
# Пример использования
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from typing import List

Base = declarative_base()

class MyModel(Base):
    __tablename__ = 'my_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class MyDAO(BaseDAO[MyModel]):
    model = MyModel

async def test_find_by_ids(async_session: AsyncSession):
    async with async_session() as session:
        ids = [1, 2, 3]
        records = await MyDAO.find_by_ids(session, ids)
        print(f"Найдено {len(records)} записей по списку ID")
```

### `upsert`

```python
    @classmethod
    async def upsert(cls, session: AsyncSession, unique_fields: List[str], values: BaseModel):
        """Создать запись или обновить существующую"""
```

**Назначение**:
Создает новую запись в базе данных или обновляет существующую, если запись с указанными уникальными полями уже существует.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `unique_fields` (List[str]): Список уникальных полей, используемых для поиска существующей записи.
- `values` (BaseModel): Объект BaseModel, содержащий значения для создания или обновления записи.

**Возвращает**:
- `T`: Объект созданной или обновленной модели.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Как работает функция**:

1. Преобразует объект `values` в словарь, исключая неустановленные значения.
2. Формирует словарь `filter_dict` на основе `unique_fields` и значений из `values_dict`.
3. Логирует информацию о выполнении операции upsert.
4. Пытается найти существующую запись с использованием метода `find_one_or_none` и фильтра `filter_dict`.
5. Если запись найдена, обновляет ее атрибуты значениями из `values_dict` и выполняет операцию обновления в базе данных.
6. Если запись не найдена, создает новый экземпляр модели `cls.model` с использованием значений из словаря и выполняет операцию добавления в базе данных.
7. Логирует информацию об успешном создании или обновлении записи.
8. Возвращает созданный или обновленный экземпляр модели.
9. В случае возникновения ошибки `SQLAlchemyError`, выполняет откат транзакции с использованием `session.rollback()`, логирует информацию об ошибке и пробрасывает исключение.

```
A[Преобразование значений в словарь]
|
B[Формирование словаря фильтров]
|
C[Логирование начала операции upsert]
|
D[Поиск существующей записи]
|
E[Обновление существующей записи (если найдена)]
|
F[Создание новой записи (если не найдена)]
|
G[Логирование успеха]
|
H[Возврат экземпляра модели]
```

**Примеры**:

```python
# Пример использования
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from typing import List

Base = declarative_base()

class MyModel(Base):
    __tablename__ = 'my_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

class MyCreate(BaseModel):
    name: str
    email: str

class MyDAO(BaseDAO[MyModel]):
    model = MyModel

async def test_upsert(async_session: AsyncSession):
    async with async_session() as session:
        values = MyCreate(name="Example", email="example@example.com")
        unique_fields = ["email"]
        record = await MyDAO.upsert(session, unique_fields, values)
        print(f"Создана или обновлена запись с id={record.id} и email='{record.email}'")
```

### `bulk_update`

```python
    @classmethod
    async def bulk_update(cls, session: AsyncSession, records: List[BaseModel]) -> int:
        """Массовое обновление записей"""
```

**Назначение**:
Выполняет массовое обновление записей в базе данных.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `records` (List[BaseModel]): Список объектов BaseModel, содержащих значения для обновления записей. Каждый объект должен иметь атрибут `