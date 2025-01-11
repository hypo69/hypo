# Анализ кода модуля `schemas.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и использует `pydantic` для валидации данных, что обеспечивает надежность и типобезопасность.
    -  Используются `BaseModel`, `ConfigDict`, `Field` из `pydantic`, что является хорошей практикой.
    - Присутствуют описания полей для `PaymentData`.
-  Минусы
    - Отсутствует документация модуля и документация для классов.
    - Нет импортов `logger` из `src.logger`, что может привести к проблемам с логированием.

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла.
2.  Добавить документацию в формате RST для каждого класса и полей, включая описание для чего он нужен, аргументы, примеры использования, и т.д.
3.  Включить импорт `logger` из `src.logger.logger` для логирования.

**Оптимизированный код**

```python
"""
Модуль содержит Pydantic схемы для валидации данных, связанных с пользователями, продуктами и платежами в Telegram боте.
========================================================================================================================

Этот модуль определяет модели данных, используемые для представления информации о пользователях Telegram,
идентификаторах продуктов и категориях, а также данных о платежах.
Модели построены на базе Pydantic, что обеспечивает автоматическую валидацию типов данных и возможность
легко сериализовывать/десериализовывать объекты.

Пример использования
--------------------

Пример использования моделей `UserModel` и `PaymentData`:

.. code-block:: python

    from pydantic import ValidationError
    from src.endpoints.bots.telegram.digital_market.bot.user.schemas import UserModel, PaymentData
    
    # Пример создания объекта UserModel
    try:
       user_data = {'telegram_id': 12345, 'username': 'test_user', 'first_name': 'Test', 'last_name': 'User'}
       user = UserModel(**user_data)
       print(user)
    except ValidationError as e:
       print(e)
    
    # Пример создания объекта PaymentData
    try:
        payment_data = {'user_id': 12345, 'payment_id': 'payment123', 'price': 100, 'product_id': 10, 'payment_type': 'card'}
        payment = PaymentData(**payment_data)
        print(payment)
    except ValidationError as e:
       print(e)
"""

from pydantic import BaseModel, ConfigDict, Field
# Импортируем logger из src.logger
from src.logger.logger import logger


class TelegramIDModel(BaseModel):
    """
    Базовая модель для идентификации пользователя по Telegram ID.
    
    Attributes:
        telegram_id (int): Уникальный идентификатор пользователя в Telegram.
    """
    telegram_id: int
    
    model_config = ConfigDict(from_attributes=True)


class UserModel(TelegramIDModel):
    """
    Модель данных пользователя Telegram.
    
    Наследует `telegram_id` из `TelegramIDModel`.
    
    Attributes:
        username (str | None): Имя пользователя в Telegram (может быть `None`).
        first_name (str | None): Имя пользователя (может быть `None`).
        last_name (str | None): Фамилия пользователя (может быть `None`).
    """
    username: str | None
    first_name: str | None
    last_name: str | None


class ProductIDModel(BaseModel):
    """
    Модель для идентификации продукта по ID.
    
    Attributes:
        id (int): Уникальный идентификатор продукта.
    """
    id: int


class ProductCategoryIDModel(BaseModel):
    """
    Модель для идентификации категории продукта по ID.
    
    Attributes:
        category_id (int): Уникальный идентификатор категории продукта.
    """
    category_id: int


class PaymentData(BaseModel):
    """
    Модель данных платежа.
    
    Attributes:
        user_id (int): ID пользователя Telegram.
        payment_id (str): Уникальный ID платежа.
        price (int): Сумма платежа в рублях.
        product_id (int): ID товара.
        payment_type (str): Тип оплаты.
    """
    user_id: int = Field(..., description='ID пользователя Telegram')
    payment_id: str = Field(..., max_length=255, description='Уникальный ID платежа')
    price: int = Field(..., description='Сумма платежа в рублях')
    product_id: int = Field(..., description='ID товара')
    payment_type: str = Field(..., description='Тип оплаты')
```