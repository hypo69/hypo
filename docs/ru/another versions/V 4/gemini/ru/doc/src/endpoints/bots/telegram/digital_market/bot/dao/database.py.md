# Модуль database.py

## Обзор

Модуль `database.py` предназначен для настройки и управления базой данных, используя SQLAlchemy. Он содержит базовый класс `Base` для моделей, настройки движка и сессии, а также методы для преобразования объектов в словари.

## Подробней

Этот модуль обеспечивает абстракцию для работы с базой данных, определяя базовый класс `Base`, от которого наследуются все остальные модели. Это позволяет унифицировать структуру таблиц и упростить взаимодействие с базой данных. Класс `Base` включает поля `id`, `created_at` и `updated_at`, которые автоматически добавляются ко всем таблицам. Также предоставляется метод `to_dict` для преобразования объектов моделей в словари.

## Классы

### `Base`

**Описание**: Базовый класс для всех моделей базы данных, наследуется от `AsyncAttrs` и `DeclarativeBase`.

**Методы**:
- `to_dict`: Преобразует объект модели в словарь.

**Параметры**:
- `id` (Mapped[int]): Первичный ключ, целое число с автоинкрементом.
- `created_at` (Mapped[datetime]): Дата и время создания записи, устанавливается автоматически при создании.
- `updated_at` (Mapped[datetime]): Дата и время последнего обновления записи, обновляется автоматически при каждом изменении.

**Примеры**

```python
# Пример определения класса, наследующего Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class MyModel(Base):
    name: Mapped[str] = mapped_column(String(50))

# Пример создания экземпляра модели
my_model = MyModel(name='Test')

# Пример преобразования объекта в словарь
model_dict = my_model.to_dict()
print(model_dict)
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

**Возвращает**:
- `str`: Имя таблицы.

**Примеры**:
```python
# Пример использования __tablename__
class User(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50))

print(User.__tablename__)  # Вывод: users