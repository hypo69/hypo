# Документация модуля kbs.py

## Обзор

Модуль `kbs.py` предназначен для создания различных инлайн и reply клавиатур для Telegram-бота. Он содержит функции для генерации клавиатур главного меню, каталога, списка покупок и кнопок оплаты товара. Клавиатуры создаются с использованием `InlineKeyboardBuilder` и `ReplyKeyboardBuilder` из библиотеки `aiogram`.

## Подробней

Этот модуль играет важную роль в обеспечении удобного пользовательского интерфейса бота. Он предоставляет набор функций для создания интерактивных клавиатур, которые позволяют пользователям легко перемещаться по различным разделам бота, просматривать каталог товаров, управлять своими покупками и совершать оплату. Модуль использует данные о категориях товаров и настройках бота для динамического формирования клавиатур.

## Функции

### `main_user_kb`

```python
def main_user_kb(user_id: int) -> InlineKeyboardMarkup:
    """
    Args:
        user_id (int): ID пользователя.

    Returns:
        InlineKeyboardMarkup: Инлайн клавиатура с основными кнопками для пользователя.
    """
```

**Описание**: Создает инлайн-клавиатуру для основного меню пользователя. Клавиатура содержит кнопки "👤 Мои покупки", "🛍 Каталог", "ℹ️ О магазине", "🌟 Поддержать автора 🌟" и, если пользователь является администратором, кнопку "⚙️ Админ панель".

**Параметры**:
- `user_id` (int): ID пользователя, для которого создается клавиатура. Используется для проверки, является ли пользователь администратором.

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками основного меню.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

user_id = 12345
main_keyboard: InlineKeyboardMarkup = main_user_kb(user_id=user_id)
```

### `catalog_kb`

```python
def catalog_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """
    Args:
        catalog_data (List[Category]): Список категорий товаров.

    Returns:
        InlineKeyboardMarkup: Инлайн клавиатура с категориями товаров и кнопкой "🏠 На главную".
    """
```

**Описание**: Создает инлайн-клавиатуру для отображения каталога товаров. Клавиатура содержит кнопки для каждой категории товаров и кнопку "🏠 На главную".

**Параметры**:
- `catalog_data` (List[Category]): Список объектов `Category`, представляющих категории товаров.

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура с категориями товаров.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from bot.dao.models import Category

catalog_data: list[Category] = [Category(id=1, category_name='Электроника'), Category(id=2, category_name='Одежда')]
catalog_keyboard: InlineKeyboardMarkup = catalog_kb(catalog_data=catalog_data)
```

### `purchases_kb`

```python
def purchases_kb() -> InlineKeyboardMarkup:
    """
    Returns:
        InlineKeyboardMarkup: Инлайн клавиатура с кнопками "🗑 Смотреть покупки" и "🏠 На главную".
    """
```

**Описание**: Создает инлайн-клавиатуру для раздела покупок пользователя. Клавиатура содержит кнопки "🗑 Смотреть покупки" и "🏠 На главную".

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура для раздела покупок.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

purchases_keyboard: InlineKeyboardMarkup = purchases_kb()
```

### `product_kb`

```python
def product_kb(product_id, price, stars_price) -> InlineKeyboardMarkup:
    """
    Args:
        product_id: ID продукта.
        price: Цена продукта в рублях.
        stars_price: Цена продукта в звездах.

    Returns:
        InlineKeyboardMarkup: Инлайн клавиатура с вариантами оплаты продукта.
    """
```

**Описание**: Создает инлайн-клавиатуру для страницы продукта. Клавиатура содержит кнопки для оплаты через ЮKassa, Robocassa и звездами, а также кнопки "🛍 Назад" и "🏠 На главную".

**Параметры**:
- `product_id`: ID продукта.
- `price`: Цена продукта в рублях.
- `stars_price`: Цена продукта в звездах.

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура для страницы продукта.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

product_id: int = 123
price: int = 100
stars_price: int = 50
product_keyboard: InlineKeyboardMarkup = product_kb(product_id=product_id, price=price, stars_price=stars_price)
```

### `get_product_buy_youkassa`

```python
def get_product_buy_youkassa(price) -> InlineKeyboardMarkup:
    """
    Args:
        price: Цена продукта в рублях.

    Returns:
        InlineKeyboardMarkup: Инлайн клавиатура для оплаты продукта через ЮKassa.
    """
```

**Описание**: Создает инлайн-клавиатуру для оплаты продукта через ЮKassa. Клавиатура содержит кнопку для оплаты указанной суммы и кнопку "Отменить".

**Параметры**:
- `price`: Цена продукта в рублях.

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура для оплаты через ЮKassa.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

price: int = 100
youkassa_keyboard: InlineKeyboardMarkup = get_product_buy_youkassa(price=price)
```

### `get_product_buy_robocassa`

```python
def get_product_buy_robocassa(price: int, payment_link: str) -> InlineKeyboardMarkup:
    """
    Args:
        price (int): Цена продукта в рублях.
        payment_link (str): Ссылка для оплаты через Robocassa.

    Returns:
        InlineKeyboardMarkup: Инлайн клавиатура для оплаты продукта через Robocassa.
    """
```

**Описание**: Создает инлайн-клавиатуру для оплаты продукта через Robocassa. Клавиатура содержит кнопку для оплаты с использованием предоставленной ссылки и кнопку "Отменить".

**Параметры**:
- `price` (int): Цена продукта в рублях.
- `payment_link` (str): Ссылка для оплаты через Robocassa.

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура для оплаты через Robocassa.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

price: int = 100
payment_link: str = 'https://example.com/robocassa_payment'
robocassa_keyboard: InlineKeyboardMarkup = get_product_buy_robocassa(price=price, payment_link=payment_link)
```

### `get_product_buy_stars`

```python
def get_product_buy_stars(price) -> InlineKeyboardMarkup:
    """
    Args:
        price: Цена продукта в звездах.

    Returns:
        InlineKeyboardMarkup: Инлайн клавиатура для оплаты продукта звездами.
    """
```

**Описание**: Создает инлайн-клавиатуру для оплаты продукта звездами. Клавиатура содержит кнопку для оплаты указанным количеством звезд и кнопку "Отменить".

**Параметры**:
- `price`: Цена продукта в звездах.

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура для оплаты звездами.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

price: int = 50
stars_keyboard: InlineKeyboardMarkup = get_product_buy_stars(price=price)
```