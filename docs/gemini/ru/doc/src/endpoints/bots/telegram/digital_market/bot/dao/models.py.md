# Модуль `models.py`

## Обзор

Модуль `models.py` содержит определения классов моделей базы данных, используемых в Telegram-боте для цифрового рынка. Эти модели включают `User`, `Category`, `Product` и `Purchase`, представляющие пользователей, категории продуктов, продукты и записи о покупках соответственно. Модуль использует SQLAlchemy для определения структуры базы данных и связей между таблицами.

## Подробней

Этот модуль является ключевым компонентом для хранения и управления данными, связанными с пользователями, продуктами и покупками в цифровом магазине Telegram-бота. Он определяет структуру таблиц базы данных и обеспечивает объектно-реляционное отображение (ORM), что упрощает взаимодействие с базой данных из кода Python. Связи между моделями позволяют легко получать информацию, например, о покупках конкретного пользователя или о продуктах в определенной категории.

## Классы

### `User`

**Описание**: Класс `User` представляет пользователя Telegram-бота.

**Атрибуты**:
- `telegram_id` (int): Уникальный идентификатор пользователя в Telegram.
- `username` (str | None): Имя пользователя в Telegram (может отсутствовать).
- `first_name` (str | None): Имя пользователя (может отсутствовать).
- `last_name` (str | None): Фамилия пользователя (может отсутствовать).
- `purchases` (List['Purchase']): Список покупок, связанных с пользователем.

**Методы**:
- `__repr__`: Возвращает строковое представление объекта `User`.

**Примеры**:
```python
# Пример создания экземпляра класса User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(telegram_id=123456789, username='testuser', first_name='Test', last_name='User')
session.add(new_user)
session.commit()

print(new_user)
```

### `Category`

**Описание**: Класс `Category` представляет категорию продуктов.

**Атрибуты**:
- `category_name` (str): Название категории.
- `products` (List['Product']): Список продуктов, принадлежащих к категории.

**Методы**:
- `__repr__`: Возвращает строковое представление объекта `Category`.

**Примеры**:
```python
# Пример создания экземпляра класса Category
new_category = Category(category_name='Electronics')
session.add(new_category)
session.commit()

print(new_category)
```

### `Product`

**Описание**: Класс `Product` представляет продукт в магазине.

**Атрибуты**:
- `name` (str): Название продукта.
- `description` (str): Описание продукта.
- `price` (int): Цена продукта.
- `file_id` (str | None): Идентификатор файла, связанного с продуктом (может отсутствовать).
- `category_id` (int): Идентификатор категории, к которой принадлежит продукт.
- `hidden_content` (str): Скрытое содержимое продукта.
- `category` (Category): Категория, к которой принадлежит продукт.
- `purchases` (List['Purchase']): Список покупок, связанных с продуктом.

**Методы**:
- `__repr__`: Возвращает строковое представление объекта `Product`.

**Примеры**:
```python
# Пример создания экземпляра класса Product
new_product = Product(
    name='Example Product',
    description='This is an example product.',
    price=100,
    category_id=new_category.id,
    hidden_content='Secret content'
)
session.add(new_product)
session.commit()

print(new_product)
```

### `Purchase`

**Описание**: Класс `Purchase` представляет запись о покупке.

**Атрибуты**:
- `user_id` (int): Идентификатор пользователя, совершившего покупку.
- `product_id` (int): Идентификатор приобретенного продукта.
- `price` (int): Цена покупки.
- `payment_type` (str): Тип платежа.
- `payment_id` (str): Уникальный идентификатор платежа.
- `user` (User): Пользователь, совершивший покупку.
- `product` (Product): Приобретенный продукт.

**Методы**:
- `__repr__`: Возвращает строковое представление объекта `Purchase`.

**Примеры**:
```python
# Пример создания экземпляра класса Purchase
new_purchase = Purchase(
    user_id=new_user.id,
    product_id=new_product.id,
    price=100,
    payment_type='card',
    payment_id='unique_payment_id'
)
session.add(new_purchase)
session.commit()

print(new_purchase)
```