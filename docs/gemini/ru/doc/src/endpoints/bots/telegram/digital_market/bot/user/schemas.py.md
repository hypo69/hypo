# Модуль Schemas для работы с данными пользователей и продуктов в Telegram боте

## Обзор

Модуль `schemas.py` определяет набор моделей данных, используемых для представления информации о пользователях Telegram, продуктах и платежах в контексте цифрового рынка. Он содержит классы, основанные на `pydantic.BaseModel`, которые обеспечивают валидацию данных и упрощают работу с данными, полученными от Telegram API и других источников.

## Подробней

Этот модуль предоставляет структуры данных для представления пользователей, продуктов, категорий продуктов и платежей. Он используется для валидации и обработки данных, передаваемых между различными компонентами приложения, такими как Telegram бот и база данных. Использование `pydantic.BaseModel` обеспечивает типовую безопасность и упрощает процесс разработки.

## Классы

### `TelegramIDModel`

**Описание**: Базовая модель для представления идентификатора Telegram пользователя.

**Как работает класс**:
Класс `TelegramIDModel` является базовой моделью, от которой наследуются другие модели, содержащие идентификатор Telegram пользователя. Он определяет поле `telegram_id` типа `int` и включает конфигурацию `ConfigDict(from_attributes=True)`, которая позволяет создавать экземпляры модели из атрибутов объектов.

**Методы**: Нет

**Параметры**:
- `telegram_id` (int): Идентификатор пользователя в Telegram.

**Примеры**:
```python
from pydantic import BaseModel, ConfigDict

class TelegramIDModel(BaseModel):
    telegram_id: int

    model_config = ConfigDict(from_attributes=True)

# Пример создания экземпляра класса
telegram_id_model = TelegramIDModel(telegram_id=123456789)
print(telegram_id_model.telegram_id)  # Вывод: 123456789
```

### `UserModel`

**Описание**: Модель для представления информации о пользователе Telegram.

**Как работает класс**:
Класс `UserModel` наследуется от `TelegramIDModel` и добавляет поля для хранения имени пользователя, имени и фамилии. Он используется для представления полной информации о пользователе Telegram.

**Методы**: Нет

**Параметры**:
- `telegram_id` (int): Идентификатор пользователя в Telegram.
- `username` (str | None): Имя пользователя в Telegram (может быть `None`).
- `first_name` (str | None): Имя пользователя (может быть `None`).
- `last_name` (str | None): Фамилия пользователя (может быть `None`).

**Примеры**:
```python
from pydantic import BaseModel, ConfigDict

class TelegramIDModel(BaseModel):
    telegram_id: int

    model_config = ConfigDict(from_attributes=True)

class UserModel(TelegramIDModel):
    username: str | None
    first_name: str | None
    last_name: str | None

# Пример создания экземпляра класса
user_model = UserModel(telegram_id=123456789, username='testuser', first_name='Test', last_name='User')
print(user_model.username)  # Вывод: testuser
```

### `ProductIDModel`

**Описание**: Модель для представления идентификатора продукта.

**Как работает класс**:
Класс `ProductIDModel` определяет поле `id` типа `int` для хранения идентификатора продукта. Он используется для однозначной идентификации продукта в системе.

**Методы**: Нет

**Параметры**:
- `id` (int): Идентификатор продукта.

**Примеры**:
```python
from pydantic import BaseModel

class ProductIDModel(BaseModel):
    id: int

# Пример создания экземпляра класса
product_id_model = ProductIDModel(id=123)
print(product_id_model.id)  # Вывод: 123
```

### `ProductCategoryIDModel`

**Описание**: Модель для представления идентификатора категории продукта.

**Как работает класс**:
Класс `ProductCategoryIDModel` определяет поле `category_id` типа `int` для хранения идентификатора категории продукта. Он используется для классификации продуктов по категориям.

**Методы**: Нет

**Параметры**:
- `category_id` (int): Идентификатор категории продукта.

**Примеры**:
```python
from pydantic import BaseModel

class ProductCategoryIDModel(BaseModel):
    category_id: int

# Пример создания экземпляра класса
product_category_id_model = ProductCategoryIDModel(category_id=456)
print(product_category_id_model.category_id)  # Вывод: 456
```

### `PaymentData`

**Описание**: Модель для представления данных о платеже.

**Как работает класс**:
Класс `PaymentData` определяет поля для хранения информации о платеже, такой как идентификатор пользователя, идентификатор платежа, сумма, идентификатор продукта и тип оплаты. Он использует `pydantic.Field` для добавления описаний к полям и указания максимальной длины для поля `payment_id`.

**Методы**: Нет

**Параметры**:
- `user_id` (int): ID пользователя Telegram.
- `payment_id` (str): Уникальный ID платежа (максимальная длина 255 символов).
- `price` (int): Сумма платежа в рублях.
- `product_id` (int): ID товара.
- `payment_type` (str): Тип оплаты.

**Примеры**:
```python
from pydantic import BaseModel, Field

class PaymentData(BaseModel):
    user_id: int = Field(..., description="ID пользователя Telegram")
    payment_id: str = Field(..., max_length=255, description="Уникальный ID платежа")
    price: int = Field(..., description="Сумма платежа в рублях")
    product_id: int = Field(..., description="ID товара")
    payment_type: str = Field(..., description="Тип оплаты")

# Пример создания экземпляра класса
payment_data = PaymentData(user_id=123456789, payment_id='payment123', price=100, product_id=123, payment_type='credit_card')
print(payment_data.price)  # Вывод: 100
```