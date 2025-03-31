# Модуль моделей базы данных для Telegram-бота Digital Market

## Обзор

Этот модуль содержит определения моделей базы данных, используемых для хранения информации о пользователях, категориях, продуктах и покупках в Telegram-боте Digital Market. Он использует SQLAlchemy для определения структуры базы данных и ORM для взаимодействия с ней.

## Подробней

Этот модуль определяет структуру базы данных, необходимую для функционирования Telegram-бота Digital Market. Он включает в себя модели для пользователей, категорий продуктов, самих продуктов и истории покупок. Связи между моделями устанавливаются с использованием `relationship` из SQLAlchemy, обеспечивая целостность данных и удобство навигации между связанными записями. Модуль использует SQLAlchemy для определения структуры базы данных и ORM для взаимодействия с ней.

## Классы

### `User`

**Описание**: Класс, представляющий пользователя Telegram-бота.

**Как работает класс**:
Класс `User` представляет собой модель пользователя в базе данных. Он содержит информацию о пользователе, такую как его telegram ID, имя пользователя, имя и фамилия. Также он содержит связь с таблицей `Purchase` для отслеживания покупок пользователя.

**Методы**:
- `__repr__`: Возвращает строковое представление объекта `User`.

**Параметры**:
- `telegram_id` (int): Уникальный идентификатор пользователя в Telegram.
- `username` (str | None): Имя пользователя в Telegram (может отсутствовать).
- `first_name` (str | None): Имя пользователя (может отсутствовать).
- `last_name` (str | None): Фамилия пользователя (может отсутствовать).
- `purchases` (List['Purchase']): Список покупок, связанных с пользователем.

**Примеры**
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Определите строку подключения к базе данных (замените на свою)
DATABASE_URL = "sqlite:///:memory:"

# Создайте движок SQLAlchemy
engine = create_engine(DATABASE_URL)

# Создайте таблицы в базе данных (если их еще нет)
Base.metadata.create_all(engine)

# Создайте класс Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Пример использования класса User
def create_user(telegram_id: int, username: str, first_name: str, last_name: str) -> User:
    """
    Создает нового пользователя в базе данных.

    Args:
        telegram_id (int): Уникальный идентификатор пользователя в Telegram.
        username (str): Имя пользователя в Telegram.
        first_name (str): Имя пользователя.
        last_name (str): Фамилия пользователя.

    Returns:
        User: Объект созданного пользователя.
    """
    db = SessionLocal()
    try:
        new_user = User(telegram_id=telegram_id, username=username, first_name=first_name, last_name=last_name)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as ex:
        db.rollback()
        raise ex
    finally:
        db.close()

# Пример создания пользователя
new_user = create_user(123456789, "testuser", "Test", "User")
print(new_user)
```

### `Category`

**Описание**: Класс, представляющий категорию продукта.

**Как работает класс**:
Класс `Category` представляет собой модель категории продукта в базе данных. Он содержит название категории и связь с таблицей `Product` для получения списка продуктов, принадлежащих к данной категории.

**Методы**:
- `__repr__`: Возвращает строковое представление объекта `Category`.

**Параметры**:
- `category_name` (str): Название категории.
- `products` (List["Product"]): Список продуктов, связанных с категорией.

**Примеры**
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Определите строку подключения к базе данных (замените на свою)
DATABASE_URL = "sqlite:///:memory:"

# Создайте движок SQLAlchemy
engine = create_engine(DATABASE_URL)

# Создайте таблицы в базе данных (если их еще нет)
Base.metadata.create_all(engine)

# Создайте класс Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_category(category_name: str) -> Category:
    """
    Создает новую категорию в базе данных.

    Args:
        category_name (str): Название категории.

    Returns:
        Category: Объект созданной категории.
    """
    db = SessionLocal()
    try:
        new_category = Category(category_name=category_name)
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return new_category
    except Exception as ex:
        db.rollback()
        raise ex
    finally:
        db.close()

# Пример создания категории
new_category = create_category("Электроника")
print(new_category)
```

### `Product`

**Описание**: Класс, представляющий продукт.

**Как работает класс**:
Класс `Product` представляет собой модель продукта в базе данных. Он содержит информацию о продукте, такую как название, описание, цена, file_id (идентификатор файла, связанного с продуктом), category_id (идентификатор категории, к которой принадлежит продукт) и hidden_content (скрытое содержимое, доступное после покупки). Также он содержит связи с таблицами `Category` и `Purchase`.

**Методы**:
- `__repr__`: Возвращает строковое представление объекта `Product`.

**Параметры**:
- `name` (str): Название продукта.
- `description` (str): Описание продукта.
- `price` (int): Цена продукта.
- `file_id` (str | None): Идентификатор файла, связанного с продуктом (может отсутствовать).
- `category_id` (int): Идентификатор категории, к которой принадлежит продукт.
- `hidden_content` (str): Скрытое содержимое, доступное после покупки.
- `category` (Category): Объект категории, к которой принадлежит продукт.
- `purchases` (List['Purchase']): Список покупок, связанных с продуктом.

**Примеры**
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Определите строку подключения к базе данных (замените на свою)
DATABASE_URL = "sqlite:///:memory:"

# Создайте движок SQLAlchemy
engine = create_engine(DATABASE_URL)

# Создайте таблицы в базе данных (если их еще нет)
Base.metadata.create_all(engine)

# Создайте класс Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_product(name: str, description: str, price: int, file_id: str, category_id: int, hidden_content: str) -> Product:
    """
    Создает новый продукт в базе данных.

    Args:
        name (str): Название продукта.
        description (str): Описание продукта.
        price (int): Цена продукта.
        file_id (str): Идентификатор файла, связанного с продуктом.
        category_id (int): Идентификатор категории, к которой принадлежит продукт.
        hidden_content (str): Скрытое содержимое, доступное после покупки.

    Returns:
        Product: Объект созданного продукта.
    """
    db = SessionLocal()
    try:
        new_product = Product(name=name, description=description, price=price, file_id=file_id, category_id=category_id, hidden_content=hidden_content)
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
    except Exception as ex:
        db.rollback()
        raise ex
    finally:
        db.close()

# Пример создания продукта
new_product = create_product("Наушники", "Беспроводные наушники", 1500, "file123", 1, "Секретный код: 1234")
print(new_product)
```

### `Purchase`

**Описание**: Класс, представляющий покупку.

**Как работает класс**:
Класс `Purchase` представляет собой модель покупки в базе данных. Он содержит информацию о покупке, такую как user_id (идентификатор пользователя, совершившего покупку), product_id (идентификатор приобретенного продукта), цена, тип оплаты, идентификатор платежа, а также связи с таблицами `User` и `Product`.

**Методы**:
- `__repr__`: Возвращает строковое представление объекта `Purchase`.

**Параметры**:
- `user_id` (int): Идентификатор пользователя, совершившего покупку.
- `product_id` (int): Идентификатор приобретенного продукта.
- `price` (int): Цена покупки.
- `payment_type` (str): Тип оплаты.
- `payment_id` (str): Уникальный идентификатор платежа.
- `user` (User): Объект пользователя, совершившего покупку.
- `product` (Product): Объект приобретенного продукта.

**Примеры**
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Определите строку подключения к базе данных (замените на свою)
DATABASE_URL = "sqlite:///:memory:"

# Создайте движок SQLAlchemy
engine = create_engine(DATABASE_URL)

# Создайте таблицы в базе данных (если их еще нет)
Base.metadata.create_all(engine)

# Создайте класс Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_purchase(user_id: int, product_id: int, price: int, payment_type: str, payment_id: str) -> Purchase:
    """
    Создает новую покупку в базе данных.

    Args:
        user_id (int): Идентификатор пользователя, совершившего покупку.
        product_id (int): Идентификатор приобретенного продукта.
        price (int): Цена покупки.
        payment_type (str): Тип оплаты.
        payment_id (str): Уникальный идентификатор платежа.

    Returns:
        Purchase: Объект созданной покупки.
    """
    db = SessionLocal()
    try:
        new_purchase = Purchase(user_id=user_id, product_id=product_id, price=price, payment_type=payment_type, payment_id=payment_id)
        db.add(new_purchase)
        db.commit()
        db.refresh(new_purchase)
        return new_purchase
    except Exception as ex:
        db.rollback()
        raise ex
    finally:
        db.close()

# Пример создания покупки
new_purchase = create_purchase(1, 1, 1500, "card", "payment123")
print(new_purchase)
```