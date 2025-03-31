# Документация модуля `schemas.py`

## Обзор

Модуль содержит Pydantic-схемы для валидации и представления данных, связанных с пользователями, продуктами и платежами в Telegram-боте цифрового магазина. Он определяет структуры данных для идентификации пользователей, продуктов, категорий продуктов и информации об оплате.

## Подробней

Этот модуль предоставляет схемы Pydantic для работы с данными пользователей, продуктов и платежей в Telegram-боте цифрового магазина. `TelegramIDModel` используется для идентификации пользователей по их Telegram ID. `UserModel` расширяет `TelegramIDModel`, добавляя информацию об имени пользователя. `ProductIDModel` и `ProductCategoryIDModel` используются для идентификации продуктов и категорий продуктов соответственно. `PaymentData` описывает структуру данных для информации об оплате, включая ID пользователя, ID платежа, сумму платежа, ID продукта и тип оплаты.

## Классы

### `TelegramIDModel`

**Описание**: Базовая модель для представления Telegram ID пользователя.

**Параметры**:
- `telegram_id` (int): ID пользователя в Telegram.

**Примеры**
```python
from pydantic import BaseModel, ConfigDict

class TelegramIDModel(BaseModel):
    telegram_id: int

    model_config = ConfigDict(from_attributes=True)

# Пример создания экземпляра класса
telegram_id_model = TelegramIDModel(telegram_id=123456789)
print(telegram_id_model)
```

### `UserModel`

**Описание**: Модель для представления информации о пользователе Telegram, включая Telegram ID, имя пользователя, имя и фамилию.

**Параметры**:
- `telegram_id` (int): ID пользователя в Telegram.
- `username` (str | None): Имя пользователя в Telegram (опционально).
- `first_name` (str | None): Имя пользователя (опционально).
- `last_name` (str | None): Фамилия пользователя (опционально).

**Примеры**
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
print(user_model)
```

### `ProductIDModel`

**Описание**: Модель для представления ID продукта.

**Параметры**:
- `id` (int): ID продукта.

**Примеры**
```python
from pydantic import BaseModel

class ProductIDModel(BaseModel):
    id: int

# Пример создания экземпляра класса
product_id_model = ProductIDModel(id=123)
print(product_id_model)
```

### `ProductCategoryIDModel`

**Описание**: Модель для представления ID категории продукта.

**Параметры**:
- `category_id` (int): ID категории продукта.

**Примеры**
```python
from pydantic import BaseModel

class ProductCategoryIDModel(BaseModel):
    category_id: int

# Пример создания экземпляра класса
product_category_id_model = ProductCategoryIDModel(category_id=456)
print(product_category_id_model)
```

### `PaymentData`

**Описание**: Модель для представления данных об оплате.

**Параметры**:
- `user_id` (int): ID пользователя Telegram.
- `payment_id` (str): Уникальный ID платежа.
- `price` (int): Сумма платежа в рублях.
- `product_id` (int): ID товара.
- `payment_type` (str): Тип оплаты.

**Примеры**
```python
from pydantic import BaseModel, Field

class PaymentData(BaseModel):
    user_id: int = Field(..., description="ID пользователя Telegram")
    payment_id: str = Field(..., max_length=255, description="Уникальный ID платежа")
    price: int = Field(..., description="Сумма платежа в рублях")
    product_id: int = Field(..., description="ID товара")
    payment_type: str = Field(..., description="Тип оплаты")

# Пример создания экземпляра класса
payment_data = PaymentData(user_id=123456789, payment_id='payment123', price=100, product_id=789, payment_type='credit_card')
print(payment_data)
```