# Модуль schemas.py

## Обзор

Модуль содержит Pydantic-схемы для валидации и типизации данных, связанных с пользователями Telegram, продуктами и платежами в контексте цифрового рынка.

## Подробней

Этот модуль определяет структуры данных, используемые для представления информации о пользователях Telegram, идентификаторах продуктов и категорий, а также данных, связанных с платежами. Он использует библиотеку Pydantic для обеспечения валидации данных и автоматической генерации схем.

## Классы

### `TelegramIDModel`

**Описание**: Базовая модель для представления идентификатора пользователя Telegram.

**Как работает класс**:
Класс `TelegramIDModel` служит базовой моделью для хранения идентификатора пользователя Telegram. Он включает поле `telegram_id`, которое должно быть целым числом. Класс использует `ConfigDict` для настройки поведения Pydantic, в частности, для поддержки создания экземпляров модели из атрибутов объектов.

**Методы**: Нет.

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

**Описание**: Модель для представления информации о пользователе Telegram, расширяющая `TelegramIDModel`.

**Как работает класс**:
Класс `UserModel` наследуется от `TelegramIDModel` и добавляет поля для хранения имени пользователя (`username`), имени (`first_name`) и фамилии (`last_name`) пользователя Telegram. Все дополнительные поля являются опциональными, что позволяет представлять пользователей с неполной информацией.

**Методы**: Нет.

**Параметры**:
- `telegram_id` (int): Идентификатор пользователя в Telegram.
- `username` (str | None): Имя пользователя в Telegram (опционально).
- `first_name` (str | None): Имя пользователя (опционально).
- `last_name` (str | None): Фамилия пользователя (опционально).

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
user_model = UserModel(telegram_id=123456789, username='johndoe', first_name='John', last_name='Doe')
print(user_model.username)  # Вывод: johndoe
```

### `ProductIDModel`

**Описание**: Модель для представления идентификатора продукта.

**Как работает класс**:
Класс `ProductIDModel` предназначен для хранения идентификатора продукта. Он содержит поле `id`, которое должно быть целым числом.

**Методы**: Нет.

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
Класс `ProductCategoryIDModel` предназначен для хранения идентификатора категории продукта. Он содержит поле `category_id`, которое должно быть целым числом.

**Методы**: Нет.

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
Класс `PaymentData` предназначен для хранения информации о платеже, включая идентификатор пользователя Telegram, уникальный идентификатор платежа, сумму платежа, идентификатор товара и тип оплаты. Класс использует библиотеку Pydantic для валидации данных и обеспечения соответствия типов.

**Методы**: Нет.

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
payment_data = PaymentData(user_id=123456789, payment_id='payment123', price=1000, product_id=123, payment_type='card')
print(payment_data.price)  # Вывод: 1000