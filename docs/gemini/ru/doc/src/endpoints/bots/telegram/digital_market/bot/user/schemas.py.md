# Документация модуля `schemas.py`

## Обзор

Модуль `schemas.py` содержит Pydantic-модели для валидации и типизации данных, связанных с пользователями Telegram, продуктами и платежами в цифровом рынке. Эти модели используются для определения структуры данных при взаимодействии с API.

## Содержание

1. [Классы](#классы)
    - [`TelegramIDModel`](#telegramidmodel)
    - [`UserModel`](#usermodel)
    - [`ProductIDModel`](#productidmodel)
    - [`ProductCategoryIDModel`](#productcategoryidmodel)
    - [`PaymentData`](#paymentdata)

## Классы

### `TelegramIDModel`

**Описание**: Базовая модель для хранения идентификатора пользователя Telegram.

**Поля**:
- `telegram_id` (int): Идентификатор пользователя Telegram.

### `UserModel`

**Описание**: Модель для хранения информации о пользователе Telegram, наследуется от `TelegramIDModel`.

**Поля**:
- `telegram_id` (int): Идентификатор пользователя Telegram (унаследован от `TelegramIDModel`).
- `username` (Optional[str]): Имя пользователя Telegram (может быть `None`).
- `first_name` (Optional[str]): Имя пользователя Telegram (может быть `None`).
- `last_name` (Optional[str]): Фамилия пользователя Telegram (может быть `None`).

### `ProductIDModel`

**Описание**: Модель для хранения идентификатора продукта.

**Поля**:
- `id` (int): Идентификатор продукта.

### `ProductCategoryIDModel`

**Описание**: Модель для хранения идентификатора категории продукта.

**Поля**:
- `category_id` (int): Идентификатор категории продукта.

### `PaymentData`

**Описание**: Модель для хранения данных о платеже.

**Поля**:
- `user_id` (int): ID пользователя Telegram.
- `payment_id` (str): Уникальный ID платежа. Максимальная длина 255 символов.
- `price` (int): Сумма платежа в рублях.
- `product_id` (int): ID товара.
- `payment_type` (str): Тип оплаты.