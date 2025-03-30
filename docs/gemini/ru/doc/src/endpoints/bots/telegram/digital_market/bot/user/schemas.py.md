# Документация модуля schemas.py

## Обзор

Модуль `schemas.py` содержит определения Pydantic моделей для представления данных, связанных с пользователями Telegram, продуктами и платежами. Эти модели используются для валидации и сериализации данных, передаваемых между различными частями приложения, в частности, между ботом Telegram и другими сервисами.

## Подробней

Этот модуль определяет схемы данных, используемые для представления информации о пользователях Telegram, идентификаторах продуктов и категорий, а также данных о платежах. Схемы определены с использованием Pydantic, что обеспечивает валидацию типов данных и упрощает процесс сериализации и десериализации данных. В частности, эти схемы используются для обработки данных, поступающих от пользователей через Telegram-бота, а также для обмена данными с другими частями системы, такими как базы данных или другие микросервисы.

## Классы

### `TelegramIDModel`

**Описание**: Базовая модель для представления идентификатора пользователя Telegram.

**Параметры**:
- `telegram_id` (int): Идентификатор пользователя Telegram.

**Примеры**:

```python
from pydantic import BaseModel, ConfigDict

class TelegramIDModel(BaseModel):
    telegram_id: int
    model_config = ConfigDict(from_attributes=True)

# Пример создания экземпляра класса
telegram_id_model = TelegramIDModel(telegram_id=123456789)
print(telegram_id_model.telegram_id)
```

### `UserModel`

**Описание**: Модель для представления информации о пользователе Telegram, включая имя пользователя, имя и фамилию.

**Параметры**:
- `telegram_id` (int): Идентификатор пользователя Telegram.
- `username` (str | None): Имя пользователя Telegram (может отсутствовать).
- `first_name` (str | None): Имя пользователя (может отсутствовать).
- `last_name` (str | None): Фамилия пользователя (может отсутствовать).

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
print(user_model.username)
```

### `ProductIDModel`

**Описание**: Модель для представления идентификатора продукта.

**Параметры**:
- `id` (int): Идентификатор продукта.

**Примеры**:

```python
from pydantic import BaseModel

class ProductIDModel(BaseModel):
    id: int

# Пример создания экземпляра класса
product_id_model = ProductIDModel(id=123)
print(product_id_model.id)
```

### `ProductCategoryIDModel`

**Описание**: Модель для представления идентификатора категории продукта.

**Параметры**:
- `category_id` (int): Идентификатор категории продукта.

**Примеры**:

```python
from pydantic import BaseModel

class ProductCategoryIDModel(BaseModel):
    category_id: int

# Пример создания экземпляра класса
product_category_id_model = ProductCategoryIDModel(category_id=456)
print(product_category_id_model.category_id)
```

### `PaymentData`

**Описание**: Модель для представления данных о платеже, включая ID пользователя, ID платежа, сумму, ID товара и тип оплаты.

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
payment_data = PaymentData(user_id=123456789, payment_id='payment123', price=100, product_id=123, payment_type='card')
print(payment_data.price)
```