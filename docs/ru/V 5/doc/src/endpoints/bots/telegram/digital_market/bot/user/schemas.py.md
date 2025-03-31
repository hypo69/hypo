# Модуль schemas.py

## Обзор

Модуль `schemas.py` содержит Pydantic-модели для представления данных, связанных с пользователями Telegram, продуктами и платежами. Эти модели используются для валидации и сериализации данных, передаваемых между различными компонентами приложения, такими как бот Telegram и база данных.

## Подробней

Этот модуль определяет схемы данных, используемые в Telegram-боте для цифрового рынка. Он включает модели для идентификации пользователей Telegram, информации о пользователях, идентификации продуктов и категорий продуктов, а также данных о платежах. Эти схемы обеспечивают строгую типизацию и валидацию данных, что помогает предотвратить ошибки и обеспечивает надежность приложения.

## Классы

### `TelegramIDModel`

**Описание**: Базовая модель для идентификации пользователя Telegram по его ID.

**Как работает класс**:
Класс `TelegramIDModel` наследуется от `pydantic.BaseModel` и содержит поле `telegram_id` типа `int`.  Поле `model_config` используется для настройки модели, в данном случае указывается, что атрибуты могут быть взяты из экземпляров других классов (`from_attributes=True`).

**Методы**: Нет

**Параметры**:
- `telegram_id` (int): Уникальный идентификатор пользователя в Telegram.

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
Класс `UserModel` наследуется от `TelegramIDModel` и добавляет поля `username`, `first_name` и `last_name` для хранения информации о пользователе. Все поля, кроме `telegram_id`, являются опциональными (`Optional[str]`).

**Методы**: Нет

**Параметры**:
- `telegram_id` (int): Уникальный идентификатор пользователя в Telegram (унаследован от `TelegramIDModel`).
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
Класс `ProductIDModel` наследуется от `pydantic.BaseModel` и содержит поле `id` типа `int`.

**Методы**: Нет

**Параметры**:
- `id` (int): Уникальный идентификатор продукта.

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
Класс `ProductCategoryIDModel` наследуется от `pydantic.BaseModel` и содержит поле `category_id` типа `int`.

**Методы**: Нет

**Параметры**:
- `category_id` (int): Уникальный идентификатор категории продукта.

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
Класс `PaymentData` наследуется от `pydantic.BaseModel` и содержит поля для хранения информации о платеже, включая ID пользователя, ID платежа, сумму платежа, ID продукта и тип оплаты. Поле `user_id` содержит ID пользователя в Telegram, `payment_id` - уникальный ID платежа (максимальная длина 255 символов), `price` - сумма платежа в рублях, `product_id` - ID товара, `payment_type` - тип оплаты.

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
payment_data = PaymentData(user_id=123456789, payment_id='payment123', price=1000, product_id=789, payment_type='card')
print(payment_data.price)  # Вывод: 1000
```