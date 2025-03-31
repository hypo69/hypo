# Модуль `models.py`

## Обзор

Модуль `models.py` содержит определения классов моделей базы данных, используемых в Telegram-боте для цифрового рынка. Он определяет структуру таблиц для пользователей, категорий, продуктов и покупок, а также устанавливает связи между ними. Модуль использует SQLAlchemy ORM для взаимодействия с базой данных.

## Подробней

Этот модуль определяет структуру данных, которая будет храниться в базе данных.  Он включает в себя классы, представляющие пользователей, категории продуктов, сами продукты и историю покупок. Связи между этими классами определены с помощью SQLAlchemy, что позволяет легко получать связанные данные (например, все покупки конкретного пользователя).  Модуль играет важную роль в организации данных и обеспечивает согласованность данных в приложении. <инструкция для модели gemini:Обеспечение целостности и согласованности данных.>

## Классы

### `User`

**Описание**: Класс `User` представляет таблицу пользователей в базе данных.

**Как работает класс**:
Класс `User` определяет структуру таблицы `users` в базе данных.  Он включает поля для хранения идентификатора пользователя в Telegram, имени пользователя, имени и фамилии, а также список покупок, связанных с этим пользователем.  Связь с классом `Purchase` осуществляется через отношение `relationship`, что позволяет легко получать все покупки, сделанные конкретным пользователем.

**Методы**:
- `__repr__`: Возвращает строковое представление объекта `User`, содержащее его id, telegram_id и имя пользователя.

**Параметры**:
- `telegram_id` (int): Уникальный идентификатор пользователя в Telegram.
- `username` (str | None): Имя пользователя в Telegram (может быть `None`).
- `first_name` (str | None): Имя пользователя (может быть `None`).
- `last_name` (str | None): Фамилия пользователя (может быть `None`).
- `purchases` (List['Purchase']): Список покупок, связанных с пользователем.

**Примеры**
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bot.dao.database import Base  # Предполагается, что Base определен в database.py

# Создание SQLite базы данных в памяти для примера
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Пример создания пользователя
new_user = User(telegram_id=123456789, username='test_user', first_name='Test', last_name='User')
session.add(new_user)
session.commit()

# Получение пользователя
retrieved_user = session.query(User).filter_by(telegram_id=123456789).first()
print(retrieved_user)  # Вывод: <User(id=1, telegram_id=123456789, username='test_user')>

session.close()
```

### `Category`

**Описание**: Класс `Category` представляет таблицу категорий продуктов в базе данных.

**Как работает класс**:
Класс `Category` определяет структуру таблицы `categories` в базе данных.  Он включает поле для хранения названия категории и список продуктов, связанных с этой категорией.  Связь с классом `Product` осуществляется через отношение `relationship`, что позволяет легко получать все продукты, принадлежащие к конкретной категории.
```python
class Category(Base):
    __tablename__ = 'categories'

    category_name: Mapped[str] = mapped_column(Text, nullable=False)
    products: Mapped[List["Product"]] = relationship(
        "Product",
        back_populates="category",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.category_name}')>"
```
**Методы**:
- `__repr__`: Возвращает строковое представление объекта `Category`, содержащее его id и название категории.

**Параметры**:
- `category_name` (str): Название категории.
- `products` (List["Product"]): Список продуктов, принадлежащих к категории.

**Примеры**
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bot.dao.database import Base  # Предполагается, что Base определен в database.py

# Создание SQLite базы данных в памяти для примера
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Пример создания категории
new_category = Category(category_name='Electronics')
session.add(new_category)
session.commit()

# Получение категории
retrieved_category = session.query(Category).filter_by(category_name='Electronics').first()
print(retrieved_category)  # Вывод: <Category(id=1, name='Electronics')>

session.close()
```

### `Product`

**Описание**: Класс `Product` представляет таблицу продуктов в базе данных.

**Как работает класс**:
Класс `Product` определяет структуру таблицы `products` в базе данных.  Он включает поля для хранения названия продукта, описания, цены, file_id, category_id, hidden_content, связи с категорией и списком покупок, связанных с продуктом.  Связь с классом `Category` осуществляется через отношение `relationship`, что позволяет легко получать категорию, к которой принадлежит продукт.  Связь с классом `Purchase` позволяет получить все покупки, содержащие данный продукт.

**Методы**:
- `__repr__`: Возвращает строковое представление объекта `Product`, содержащее его id, название и цену.

**Параметры**:
- `name` (str): Название продукта.
- `description` (str): Описание продукта.
- `price` (int): Цена продукта.
- `file_id` (str | None): Идентификатор файла, связанного с продуктом (может быть `None`).
- `category_id` (int): Идентификатор категории, к которой принадлежит продукт.
- `hidden_content` (str): Скрытое содержимое, связанное с продуктом.
- `category` (Category): Категория, к которой принадлежит продукт.
- `purchases` (List['Purchase']): Список покупок, связанных с продуктом.

**Примеры**
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bot.dao.database import Base  # Предполагается, что Base определен в database.py

# Предположим, что Category уже определена и есть объект category
# Пример создания category (если её нет)
new_category = Category(category_name='Electronics')
session.add(new_category)
session.commit()
category = session.query(Category).filter_by(category_name='Electronics').first()

# Пример создания продукта
new_product = Product(
    name='Laptop',
    description='High-performance laptop',
    price=1200,
    category_id=category.id,  # Используем id существующей категории
    hidden_content='Confidential data'
)
session.add(new_product)
session.commit()

# Получение продукта
retrieved_product = session.query(Product).filter_by(name='Laptop').first()
print(retrieved_product)  # Вывод: <Product(id=1, name='Laptop', price=1200)>

session.close()
```

### `Purchase`

**Описание**: Класс `Purchase` представляет таблицу покупок в базе данных.

**Как работает класс**:
Класс `Purchase` определяет структуру таблицы `purchases` в базе данных.  Он включает поля для хранения идентификаторов пользователя и продукта, цены, типа оплаты, идентификатора платежа, а также связи с пользователем и продуктом.  Связи с классами `User` и `Product` осуществляются через отношения `relationship`, что позволяет легко получать информацию о пользователе и продукте, связанных с покупкой.

**Методы**:
- `__repr__`: Возвращает строковое представление объекта `Purchase`, содержащее его id, user_id, product_id и дату создания.

**Параметры**:
- `user_id` (int): Идентификатор пользователя, совершившего покупку.
- `product_id` (int): Идентификатор приобретенного продукта.
- `price` (int): Цена покупки.
- `payment_type` (str): Тип оплаты.
- `payment_id` (str): Идентификатор платежа.
- `user` (User): Пользователь, совершивший покупку.
- `product` (Product): Приобретенный продукт.

**Примеры**
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bot.dao.database import Base  # Предполагается, что Base определен в database.py

# Предположим, что User и Product уже определены и есть объекты user и product
# Пример создания user и product (если их нет)
new_user = User(telegram_id=123456789, username='test_user', first_name='Test', last_name='User')
session.add(new_user)
new_category = Category(category_name='Electronics')
session.add(new_category)
session.commit()
category = session.query(Category).filter_by(category_name='Electronics').first()

new_product = Product(
    name='Laptop',
    description='High-performance laptop',
    price=1200,
    category_id=category.id,  # Используем id существующей категории
    hidden_content='Confidential data'
)
session.add(new_product)
session.commit()

user = session.query(User).filter_by(telegram_id=123456789).first()
product = session.query(Product).filter_by(name='Laptop').first()

# Пример создания покупки
new_purchase = Purchase(
    user_id=user.id,
    product_id=product.id,
    price=1200,
    payment_type='Credit Card',
    payment_id='1234567890'
)
session.add(new_purchase)
session.commit()

# Получение покупки
retrieved_purchase = session.query(Purchase).filter_by(payment_id='1234567890').first()
print(retrieved_purchase)  # Вывод: <Purchase(id=1, user_id=1, product_id=1, date=2024-10-26 00:00:00)>

session.close()
```