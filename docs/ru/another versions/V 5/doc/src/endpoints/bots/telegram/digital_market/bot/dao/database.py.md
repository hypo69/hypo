# Модуль database.py

## Обзор

Модуль `database.py` содержит настройки и базовые классы для работы с базой данных, используя SQLAlchemy. Он определяет подключение к базе данных, базовый класс для моделей и вспомогательные методы.

## Подробней

Этот модуль является основой для взаимодействия с базой данных в проекте. Он включает в себя конфигурацию подключения, создание движка и сессии, а также базовый класс для определения таблиц базы данных. Класс `Base` содержит общие поля, такие как `id`, `created_at` и `updated_at`, которые будут наследоваться другими моделями.

## Классы

### `Base`

**Описание**: Базовый класс для моделей SQLAlchemy, представляющий абстрактную декларативную базу.

**Как работает класс**: Класс `Base` наследуется от `AsyncAttrs` и `DeclarativeBase` из SQLAlchemy. Он определяет общие поля, такие как `id` (первичный ключ с автоинкрементом), `created_at` (время создания записи) и `updated_at` (время последнего обновления записи). Также содержит метод `to_dict` для преобразования объекта модели в словарь.

**Методы**:
- `to_dict`: Преобразует объект модели в словарь, где ключами являются имена столбцов, а значениями - соответствующие значения атрибутов.
- `__tablename__`: Возвращает имя таблицы, основанное на имени класса, преобразованном в нижний регистр и добавлением суффикса 's'.

**Параметры**:
- `id` (int): Уникальный идентификатор записи.
- `created_at` (datetime): Дата и время создания записи.
- `updated_at` (datetime): Дата и время последнего обновления записи.

**Примеры**:
```python
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = 'users'

    name: Mapped[str] = mapped_column(String(50))

# Пример создания объекта User
# user = User(name='John Doe')
# user_dict = user.to_dict()  # Преобразование объекта в словарь
```

## Функции

### `create_async_engine`

```python
engine = create_async_engine(url=database_url)
```

**Описание**: Создает асинхронный движок SQLAlchemy для подключения к базе данных.

**Как работает функция**: Функция `create_async_engine` создает экземпляр движка, используя URL базы данных, полученный из переменной `database_url`. Этот движок используется для установления соединения с базой данных и выполнения запросов.

**Параметры**:
- `url` (str): URL для подключения к базе данных.

**Возвращает**:
- `AsyncEngine`: Асинхронный движок SQLAlchemy.

**Примеры**:
```python
from sqlalchemy.ext.asyncio import create_async_engine

# engine = create_async_engine(url='postgresql+asyncpg://user:password@host:port/database')
```

### `async_sessionmaker`

```python
async_session_maker = async_sessionmaker(engine, class_=AsyncSession)
```

**Описание**: Создает фабрику асинхронных сессий SQLAlchemy.

**Как работает функция**: Функция `async_sessionmaker` создает фабрику, которая используется для создания новых сессий базы данных. Сессия используется для выполнения операций с базой данных, таких как запросы и сохранения изменений.

**Параметры**:
- `engine` (AsyncEngine): Асинхронный движок SQLAlchemy.
- `class_` (AsyncSession): Класс асинхронной сессии.

**Возвращает**:
- `async_sessionmaker`: Фабрика асинхронных сессий.

**Примеры**:
```python
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

# async_session_maker = async_sessionmaker(engine, class_=AsyncSession)

# Пример использования сессии:
# async with async_session_maker() as session:
#     result = await session.execute(select(User))
#     users = result.scalars().all()