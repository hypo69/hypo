# Модуль `base.py`

## Обзор

Модуль `base.py` содержит базовый класс `BaseDAO`, который предоставляет набор общих методов для взаимодействия с базой данных. Этот класс предназначен для наследования другими DAO (Data Access Object) классами, специфичными для каждой таблицы в базе данных. Он включает методы для поиска, добавления, обновления, удаления и подсчета записей, а также для выполнения операций пагинации и upsert.

## Подробней

Модуль предоставляет абстрактный базовый класс `BaseDAO`, который параметризуется типом `T`, представляющим модель SQLAlchemy, связанную с таблицей в базе данных. `BaseDAO` предоставляет стандартные операции CRUD (Create, Read, Update, Delete) и другие полезные методы, такие как пагинация и массовое обновление, которые могут быть использованы для взаимодействия с базой данных. Использование `BaseDAO` позволяет избежать дублирования кода и обеспечивает единообразный интерфейс для работы с различными таблицами базы данных.

## Классы

### `BaseDAO`

**Описание**:
Базовый класс, предоставляющий общие методы для доступа к данным в базе данных. Этот класс является универсальным и предназначен для наследования другими DAO-классами, специфичными для каждой модели базы данных.

**Как работает класс**:
Класс `BaseDAO` параметризуется типом `T`, который должен быть наследником класса `Base` из SQLAlchemy. Это позволяет классу `BaseDAO` работать с различными моделями базы данных, предоставляя общие методы для выполнения операций CRUD и других операций, таких как пагинация и массовое обновление.

**Методы**:
- `find_one_or_none_by_id`: Находит одну запись по ID.
- `find_one_or_none`: Находит одну запись по фильтрам.
- `find_all`: Находит все записи по фильтрам.
- `add`: Добавляет одну запись.
- `add_many`: Добавляет несколько записей.
- `update`: Обновляет записи по фильтрам.
- `delete`: Удаляет записи по фильтру.
- `count`: Подсчитывает количество записей.
- `paginate`: Выполняет пагинацию записей.
- `find_by_ids`: Находит несколько записей по списку ID.
- `upsert`: Создает запись или обновляет существующую.
- `bulk_update`: Массовое обновление записей.

### `find_one_or_none_by_id`

```python
@classmethod
async def find_one_or_none_by_id(cls, data_id: int, session: AsyncSession):
    """Найти запись по ID"""
```

**Как работает функция**:
1. Функция `find_one_or_none_by_id` выполняет поиск записи в базе данных по заданному `data_id`.
2. Формируется запрос `select` к базе данных, используя `cls.model` для определения таблицы и `filter_by` для указания условия поиска по `id`.
3. Выполняется запрос с использованием `session.execute`, и результат извлекается с помощью `scalar_one_or_none`, что возвращает либо найденную запись, либо `None`.
4. Логируется информация о результате поиска с использованием `logger.info`.
5. В случае ошибки `SQLAlchemyError` логируется сообщение об ошибке с использованием `logger.error` и вызывается исключение.

**Параметры**:
- `data_id` (int): ID записи для поиска.
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.

**Возвращает**:
- `T | None`: Найденная запись или `None`, если запись не найдена.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример использования функции find_one_or_none_by_id
async with async_session() as session:
    record = await BaseDAO.find_one_or_none_by_id(data_id=123, session=session)
    if record:
        print(f"Найденная запись: {record}")
    else:
        print("Запись не найдена")
```

### `find_one_or_none`

```python
@classmethod
async def find_one_or_none(cls, session: AsyncSession, filters: BaseModel):
    """Найти одну запись по фильтрам"""
```

**Как работает функция**:
1. Функция `find_one_or_none` выполняет поиск одной записи в базе данных по заданным фильтрам.
2. Извлекает параметры фильтрации из объекта `filters` с помощью `filters.model_dump(exclude_unset=True)`, чтобы получить словарь с параметрами.
3. Формируется запрос `select` к базе данных, используя `cls.model` для определения таблицы и `filter_by` для указания условий поиска.
4. Выполняется запрос с использованием `session.execute`, и результат извлекается с помощью `scalar_one_or_none`, что возвращает либо найденную запись, либо `None`.
5. Логируется информация о результате поиска с использованием `logger.info`.
6. В случае ошибки `SQLAlchemyError` логируется сообщение об ошибке с использованием `logger.error` и вызывается исключение.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `filters` (BaseModel): Объект Pydantic BaseModel, содержащий параметры фильтрации.

**Возвращает**:
- `T | None`: Найденная запись или `None`, если запись не найдена.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример использования функции find_one_or_none
from pydantic import BaseModel

class UserFilter(BaseModel):
    name: str
    age: int

async with async_session() as session:
    filters = UserFilter(name="John", age=30)
    record = await BaseDAO.find_one_or_none(session=session, filters=filters)
    if record:
        print(f"Найденная запись: {record}")
    else:
        print("Запись не найдена")
```

### `find_all`

```python
@classmethod
async def find_all(cls, session: AsyncSession, filters: BaseModel | None = None):
    """Найти все записи по фильтрам"""
```

**Как работает функция**:
1. Функция `find_all` выполняет поиск всех записей в базе данных, соответствующих заданным фильтрам.
2. Извлекает параметры фильтрации из объекта `filters` с помощью `filters.model_dump(exclude_unset=True)`, если `filters` не `None`, чтобы получить словарь с параметрами.
3. Формируется запрос `select` к базе данных, используя `cls.model` для определения таблицы и `filter_by` для указания условий поиска.
4. Выполняется запрос с использованием `session.execute`, и результат извлекается с помощью `scalars().all()`, что возвращает список всех найденных записей.
5. Логируется информация о количестве найденных записей с использованием `logger.info`.
6. В случае ошибки `SQLAlchemyError` логируется сообщение об ошибке с использованием `logger.error` и вызывается исключение.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `filters` (BaseModel | None): Объект Pydantic BaseModel, содержащий параметры фильтрации. Может быть `None`, если фильтры не требуются.

**Возвращает**:
- `List[T]`: Список найденных записей.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример использования функции find_all
from pydantic import BaseModel
from typing import Optional

class UserFilter(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None

async with async_session() as session:
    filters = UserFilter(name="John")
    records = await BaseDAO.find_all(session=session, filters=filters)
    if records:
        for record in records:
            print(f"Найденная запись: {record}")
    else:
        print("Записи не найдены")
```

### `add`

```python
@classmethod
async def add(cls, session: AsyncSession, values: BaseModel):
    """Добавить одну запись"""
```

**Как работает функция**:
1. Функция `add` добавляет одну запись в базу данных.
2. Извлекает значения полей из объекта `values` с помощью `values.model_dump(exclude_unset=True)`, чтобы получить словарь с данными.
3. Создается новый экземпляр модели `cls.model` с использованием полученных значений.
4. Новый экземпляр добавляется в сессию с помощью `session.add`.
5. Вызывается `session.flush` для немедленного сохранения изменений в базе данных.
6. Логируется информация об успешном добавлении записи с использованием `logger.info`.
7. В случае ошибки `SQLAlchemyError` выполняется откат транзакции с помощью `session.rollback()`, логируется сообщение об ошибке с использованием `logger.error` и вызывается исключение.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `values` (BaseModel): Объект Pydantic BaseModel, содержащий значения для добавления новой записи.

**Возвращает**:
- `T`: Новый экземпляр добавленной записи.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример использования функции add
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    age: int

async with async_session() as session:
    values = UserCreate(name="John", age=30)
    new_record = await BaseDAO.add(session=session, values=values)
    print(f"Добавленная запись: {new_record}")
```

### `add_many`

```python
@classmethod
async def add_many(cls, session: AsyncSession, instances: List[BaseModel]):
    """Добавить несколько записей"""
```

**Как работает функция**:
1. Функция `add_many` добавляет несколько записей в базу данных.
2. Извлекает значения полей из каждого объекта в списке `instances` с помощью `item.model_dump(exclude_unset=True)`, чтобы получить список словарей с данными.
3. Создаются новые экземпляры модели `cls.model` для каждого словаря в списке.
4. Новые экземпляры добавляются в сессию с помощью `session.add_all`.
5. Вызывается `session.flush` для немедленного сохранения изменений в базе данных.
6. Логируется информация об успешном добавлении записей с использованием `logger.info`.
7. В случае ошибки `SQLAlchemyError` выполняется откат транзакции с помощью `session.rollback()`, логируется сообщение об ошибке с использованием `logger.error` и вызывается исключение.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `instances` (List[BaseModel]): Список объектов Pydantic BaseModel, содержащих значения для добавления новых записей.

**Возвращает**:
- `List[T]`: Список новых экземпляров добавленных записей.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример использования функции add_many
from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    name: str
    age: int

async with async_session() as session:
    instances = [
        UserCreate(name="John", age=30),
        UserCreate(name="Jane", age=25)
    ]
    new_records = await BaseDAO.add_many(session=session, instances=instances)
    for record in new_records:
        print(f"Добавленная запись: {record}")
```

### `update`

```python
@classmethod
async def update(cls, session: AsyncSession, filters: BaseModel, values: BaseModel):
    """Обновить записи по фильтрам"""
```

**Как работает функция**:
1. Функция `update` обновляет записи в базе данных, соответствующие заданным фильтрам, новыми значениями.
2. Извлекает параметры фильтрации из объекта `filters` и значения для обновления из объекта `values` с помощью `model_dump(exclude_unset=True)`, чтобы получить словари с данными.
3. Формируется запрос `sqlalchemy_update` к базе данных, используя `cls.model` для определения таблицы, `where` для указания условий фильтрации и `values` для указания новых значений.
4. Выполняется запрос с использованием `session.execute`.
5. Вызывается `session.flush` для немедленного сохранения изменений в базе данных.
6. Логируется информация об успешном обновлении записей с использованием `logger.info`.
7. В случае ошибки `SQLAlchemyError` выполняется откат транзакции с помощью `session.rollback()`, логируется сообщение об ошибке с использованием `logger.error` и вызывается исключение.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `filters` (BaseModel): Объект Pydantic BaseModel, содержащий параметры фильтрации для выбора записей, которые необходимо обновить.
- `values` (BaseModel): Объект Pydantic BaseModel, содержащий новые значения для обновления выбранных записей.

**Возвращает**:
- `int`: Количество обновленных записей.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример использования функции update
from pydantic import BaseModel
from typing import Optional

class UserFilter(BaseModel):
    name: str

class UserUpdate(BaseModel):
    age: int

async with async_session() as session:
    filters = UserFilter(name="John")
    values = UserUpdate(age=31)
    updated_count = await BaseDAO.update(session=session, filters=filters, values=values)
    print(f"Обновлено {updated_count} записей")
```

### `delete`

```python
@classmethod
async def delete(cls, session: AsyncSession, filters: BaseModel):
    """Удалить записи по фильтру"""
```

**Как работает функция**:
1. Функция `delete` удаляет записи из базы данных, соответствующие заданным фильтрам.
2. Извлекает параметры фильтрации из объекта `filters` с помощью `filters.model_dump(exclude_unset=True)`, чтобы получить словарь с данными.
3. Проверяется, что предоставлен хотя бы один фильтр. Если фильтры отсутствуют, логируется сообщение об ошибке с использованием `logger.error` и вызывается исключение `ValueError`.
4. Формируется запрос `sqlalchemy_delete` к базе данных, используя `cls.model` для определения таблицы и `filter_by` для указания условий фильтрации.
5. Выполняется запрос с использованием `session.execute`.
6. Вызывается `session.flush` для немедленного сохранения изменений в базе данных.
7. Логируется информация об успешном удалении записей с использованием `logger.info`.
8. В случае ошибки `SQLAlchemyError` выполняется откат транзакции с помощью `session.rollback()`, логируется сообщение об ошибке с использованием `logger.error` и вызывается исключение.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `filters` (BaseModel): Объект Pydantic BaseModel, содержащий параметры фильтрации для выбора записей, которые необходимо удалить.

**Возвращает**:
- `int`: Количество удаленных записей.

**Вызывает исключения**:
- `ValueError`: Если не предоставлен ни один фильтр для удаления.
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример использования функции delete
from pydantic import BaseModel

class UserFilter(BaseModel):
    name: str

async with async_session() as session:
    filters = UserFilter(name="John")
    deleted_count = await BaseDAO.delete(session=session, filters=filters)
    print(f"Удалено {deleted_count} записей")
```

### `count`

```python
@classmethod
async def count(cls, session: AsyncSession, filters: BaseModel | None = None):
    """Подсчитать количество записей"""
```

**Как работает функция**:
1. Функция `count` подсчитывает количество записей в базе данных, соответствующих заданным фильтрам.
2. Извлекает параметры фильтрации из объекта `filters` с помощью `filters.model_dump(exclude_unset=True)`, если `filters` не `None`, чтобы получить словарь с параметрами.
3. Формируется запрос `select(func.count(cls.model.id))` к базе данных, используя `cls.model` для определения таблицы и `filter_by` для указания условий фильтрации.
4. Выполняется запрос с использованием `session.execute`, и результат извлекается с помощью `scalar()`, что возвращает количество найденных записей.
5. Логируется информация о количестве найденных записей с использованием `logger.info`.
6. В случае ошибки `SQLAlchemyError` логируется сообщение об ошибке с использованием `logger.error` и вызывается исключение.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `filters` (BaseModel | None): Объект Pydantic BaseModel, содержащий параметры фильтрации для выбора записей, которые необходимо подсчитать. Может быть `None`, если фильтры не требуются.

**Возвращает**:
- `int`: Количество записей, соответствующих заданным фильтрам.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример использования функции count
from pydantic import BaseModel
from typing import Optional

class UserFilter(BaseModel):
    name: Optional[str] = None

async with async_session() as session:
    filters = UserFilter(name="John")
    count = await BaseDAO.count(session=session, filters=filters)
    print(f"Найдено {count} записей")
```

### `paginate`

```python
@classmethod
async def paginate(cls, session: AsyncSession, page: int = 1, page_size: int = 10, filters: BaseModel = None):
    """Пагинация записей"""
```

**Как работает функция**:
1. Функция `paginate` выполняет пагинацию записей в базе данных, соответствующих заданным фильтрам.
2. Извлекает параметры фильтрации из объекта `filters` с помощью `filters.model_dump(exclude_unset=True)`, если `filters` не `None`, чтобы получить словарь с параметрами.
3. Формируется запрос `select` к базе данных, используя `cls.model` для определения таблицы и `filter_by` для указания условий фильтрации.
4. К запросу добавляются параметры `offset` и `limit` для выполнения пагинации.
5. Выполняется запрос с использованием `session.execute`, и результат извлекается с помощью `scalars().all()`, что возвращает список записей для текущей страницы.
6. Логируется информация о количестве найденных записей на странице с использованием `logger.info`.
7. В случае ошибки `SQLAlchemyError` логируется сообщение об ошибке с использованием `logger.error` и вызывается исключение.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `page` (int): Номер страницы для извлечения. По умолчанию 1.
- `page_size` (int): Количество записей на странице. По умолчанию 10.
- `filters` (BaseModel | None): Объект Pydantic BaseModel, содержащий параметры фильтрации для выбора записей, которые необходимо пагинировать. Может быть `None`, если фильтры не требуются.

**Возвращает**:
- `List[T]`: Список записей для текущей страницы.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример использования функции paginate
from pydantic import BaseModel
from typing import Optional

class UserFilter(BaseModel):
    name: Optional[str] = None

async with async_session() as session:
    filters = UserFilter(name="John")
    page = 2
    page_size = 10
    records = await BaseDAO.paginate(session=session, page=page, page_size=page_size, filters=filters)
    if records:
        for record in records:
            print(f"Найдена запись: {record}")
    else:
        print("Записи не найдены")
```

### `find_by_ids`

```python
@classmethod
async def find_by_ids(cls, session: AsyncSession, ids: List[int]) -> List[Any]:
    """Найти несколько записей по списку ID"""
```

**Как работает функция**:
1. Функция `find_by_ids` выполняет поиск нескольких записей в базе данных по списку ID.
2. Формируется запрос `select` к базе данных, используя `cls.model` для определения таблицы и `filter(cls.model.id.in_(ids))` для указания условия поиска по списку ID.
3. Выполняется запрос с использованием `session.execute`, и результат извлекается с помощью `scalars().all()`, что возвращает список найденных записей.
4. Логируется информация о количестве найденных записей с использованием `logger.info`.
5. В случае ошибки `SQLAlchemyError` логируется сообщение об ошибке с использованием `logger.error` и вызывается исключение.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `ids` (List[int]): Список ID записей для поиска.

**Возвращает**:
- `List[Any]`: Список найденных записей.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример использования функции find_by_ids
async with async_session() as session:
    ids = [1, 2, 3]
    records = await BaseDAO.find_by_ids(session=session, ids=ids)
    if records:
        for record in records:
            print(f"Найденная запись: {record}")
    else:
        print("Записи не найдены")
```

### `upsert`

```python
@classmethod
async def upsert(cls, session: AsyncSession, unique_fields: List[str], values: BaseModel):
    """Создать запись или обновить существующую"""
```

**Как работает функция**:
1. Функция `upsert` создает новую запись в базе данных или обновляет существующую, если запись с указанными уникальными полями уже существует.
2. Извлекает значения полей из объекта `values` с помощью `values.model_dump(exclude_unset=True)`, чтобы получить словарь с данными.
3. Формируется словарь `filter_dict` с уникальными полями и их значениями.
4. Выполняется поиск существующей записи с использованием `cls.find_one_or_none` и `BaseModel.construct(**filter_dict)`.
5. Если запись существует, она обновляется новыми значениями из `values_dict`.
6. Если запись не существует, создается новый экземпляр модели `cls.model` с использованием `values_dict`, и добавляется в сессию.
7. Вызывается `session.flush` для немедленного сохранения изменений в базе данных.
8. Логируется информация о создании или обновлении записи с использованием `logger.info`.
9. В случае ошибки `SQLAlchemyError` выполняется откат транзакции с помощью `session.rollback()`, логируется сообщение об ошибке с использованием `logger.error` и вызывается исключение.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `unique_fields` (List[str]): Список уникальных полей, используемых для поиска существующей записи.
- `values` (BaseModel): Объект Pydantic BaseModel, содержащий значения для создания или обновления записи.

**Возвращает**:
- `T`: Обновленный или созданный экземпляр записи.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример использования функции upsert
from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    name: str
    age: int

async with async_session() as session:
    unique_fields = ["name"]
    values = UserCreate(name="John", age=30)
    record = await BaseDAO.upsert(session=session, unique_fields=unique_fields, values=values)
    print(f"Созданная или обновленная запись: {record}")
```

### `bulk_update`

```python
@classmethod
async def bulk_update(cls, session: AsyncSession, records: List[BaseModel]) -> int:
    """Массовое обновление записей"""
```

**Как работает функция**:
1. Функция `bulk_update` выполняет массовое обновление записей в базе данных.
2. Итерируется по списку записей `records`.
3. Для каждой записи извлекаются значения полей с помощью `record.model_dump(exclude_unset=True)`, чтобы получить словарь с данными.
4. Проверяется наличие ключа `id` в словаре с данными. Если `id` отсутствует, запись пропускается.
5. Формируется словарь `update_data` с данными для обновления, исключая поле `id`.
6. Формируется запрос `sqlalchemy_update` к базе данных, используя `cls.model` для определения таблицы, `filter_by(id=record_dict['id'])` для указания условия поиска по ID и `values(**update_data)` для указания новых значений.
7. Выполняется запрос с использованием `session.execute`.
8. Подсчитывается общее количество обновленных записей.
9. Вызывается `session.flush` для немедленного сохранения изменений в базе данных.
10. Логируется информация об успешном обновлении записей с использованием `logger.info`.
11. В случае ошибки `SQLAlchemyError` выполняется откат транзакции с помощью `session.rollback()`, логируется сообщение об ошибке с использованием `logger.error` и вызывается исключение.

**Параметры**:
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.
- `records` (List[BaseModel]): Список объектов Pydantic BaseModel, содержащих значения для обновления записей.

**Возвращает**:
- `int`: Общее количество обновленных записей.

**Вызывает исключения**:
- `SQLAlchemyError`: Если возникает ошибка при выполнении запроса к базе данных.

**Примеры**:

```python
# Пример использования функции bulk_update
from pydantic import BaseModel
from typing import List, Optional

class UserUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    age: Optional[int] = None

async with async_session() as session:
    records = [
        UserUpdate(id=1, age=31),
        UserUpdate(id=2, name="Jane")
    ]
    updated_count = await BaseDAO.bulk_update(session=session, records=records)
    print(f"Обновлено {updated_count} записей")