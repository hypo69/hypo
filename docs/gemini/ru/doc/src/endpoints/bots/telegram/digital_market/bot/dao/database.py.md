# Модуль database.py

## Обзор

Модуль `database.py` предназначен для настройки и управления базой данных, используемой в Telegram-боте для цифрового рынка. Он включает в себя создание движка базы данных, сессии и базового класса для моделей, обеспечивая асинхронное взаимодействие с базой данных.

## Подробней

Этот модуль определяет подключение к базе данных, используя SQLAlchemy и Asyncio для асинхронных операций. Он создает движок базы данных на основе URL, указанного в конфигурации, и предоставляет фабрику сессий для работы с базой данных. Также модуль содержит базовый класс `Base`, который используется для определения структуры таблиц в базе данных. Все модели наследуются от этого класса, что позволяет им автоматически получать поля `id`, `created_at` и `updated_at`, а также метод `to_dict` для преобразования объектов в словари.

## Классы

### `Base`

**Описание**: Базовый класс для всех моделей базы данных.

**Методы**:
- `to_dict`: Преобразует объект модели в словарь.

**Параметры**:
- `id` (int): Уникальный идентификатор записи.
- `created_at` (datetime): Дата и время создания записи.
- `updated_at` (datetime): Дата и время последнего обновления записи.

**Примеры**
```python
from datetime import datetime
from sqlalchemy import func, TIMESTAMP, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True  # Базовый класс будет абстрактным, чтобы не создавать отдельную таблицу для него

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )

    @classmethod
    @property
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'

    def to_dict(self) -> dict:
        # Метод для преобразования объекта в словарь
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
```

## Функции

### `__tablename__`

```python
@classmethod
@property
def __tablename__(cls) -> str:
    return cls.__name__.lower() + 's'
```

**Описание**: Возвращает имя таблицы в нижнем регистре с добавлением суффикса 's'.

**Параметры**:
- `cls`: Класс модели.

**Возвращает**:
- `str`: Имя таблицы.

**Примеры**:
```python
class User(Base):
    __tablename__ = 'users'
```

### `to_dict`

```python
def to_dict(self) -> dict:
    # Метод для преобразования объекта в словарь
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}
```

**Описание**: Преобразует объект модели в словарь, где ключами являются имена столбцов, а значениями - соответствующие значения атрибутов.

**Параметры**:
- `self`: Объект модели.

**Возвращает**:
- `dict`: Словарь, представляющий объект модели.

**Примеры**:
```python
user = User(name='John', email='john@example.com')
user_dict = user.to_dict()
print(user_dict)
```
```output
{'id': None, 'name': 'John', 'email': 'john@example.com', 'created_at': None, 'updated_at': None}