# Модуль для создания клавиатур для Telegram-бота цифрового магазина
## Обзор

Модуль `kbs.py` предназначен для создания и управления различными типами клавиатур, используемых в Telegram-боте цифрового магазина. Он содержит функции для создания основных, каталожных клавиатур, клавиатур для покупок и оплаты продуктов.

## Подробней

Этот модуль предоставляет набор функций для генерации интерактивных клавиатур, которые позволяют пользователям взаимодействовать с ботом. Клавиатуры создаются с использованием `InlineKeyboardMarkup` и `ReplyKeyboardMarkup` из библиотеки `aiogram`. Модуль также включает функции для создания ссылок на оплату и настройки внешнего вида клавиатур. Он является важной частью интерфейса пользователя бота, обеспечивая удобную навигацию и доступ к основным функциям, таким как просмотр каталога, совершение покупок и управление профилем.

## Функции

### `main_user_kb`

```python
def main_user_kb(user_id: int) -> InlineKeyboardMarkup:
    """Создает главную клавиатуру пользователя с кнопками "Мои покупки", "Каталог", "О магазине", "Поддержать автора" и "Админ панель" (если пользователь является администратором).

    Args:
        user_id (int): ID пользователя для проверки, является ли он администратором.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup, представляющий главную клавиатуру пользователя.

    Как работает функция:
    1. Создает объект `InlineKeyboardBuilder`.
    2. Добавляет кнопки "👤 Мои покупки", "🛍 Каталог", "ℹ️ О магазине" и "🌟 Поддержать автора 🌟" с соответствующими callback_data или url.
    3. Если `user_id` есть в списке `settings.ADMIN_IDS`, добавляет кнопку "⚙️ Админ панель".
    4. Устанавливает количество кнопок в ряду равным 1.
    5. Преобразует объект `InlineKeyboardBuilder` в объект `InlineKeyboardMarkup` и возвращает его.
    """
    ...
```

### `catalog_kb`

```python
def catalog_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """Создает клавиатуру каталога с кнопками для каждой категории и кнопкой "На главную".

    Args:
        catalog_data (List[Category]): Список объектов `Category`, представляющих категории товаров.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup, представляющий клавиатуру каталога.

    Как работает функция:
    1. Создает объект `InlineKeyboardBuilder`.
    2. Итерируется по списку `catalog_data` и добавляет кнопку для каждой категории, используя `category.category_name` в качестве текста кнопки и `f"category_{category.id}"` в качестве callback_data.
    3. Добавляет кнопку "🏠 На главную" с callback_data "home".
    4. Устанавливает количество кнопок в ряду равным 2.
    5. Преобразует объект `InlineKeyboardBuilder` в объект `InlineKeyboardMarkup` и возвращает его.
    """
    ...
```

### `purchases_kb`

```python
def purchases_kb() -> InlineKeyboardMarkup:
    """Создает клавиатуру для управления покупками с кнопками "Смотреть покупки" и "На главную".

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup, представляющий клавиатуру покупок.

    Как работает функция:
    1. Создает объект `InlineKeyboardBuilder`.
    2. Добавляет кнопку "🗑 Смотреть покупки" с callback_data "purchases".
    3. Добавляет кнопку "🏠 На главную" с callback_data "home".
    4. Устанавливает количество кнопок в ряду равным 1.
    5. Преобразует объект `InlineKeyboardBuilder` в объект `InlineKeyboardMarkup` и возвращает его.
    """
    ...
```

### `product_kb`

```python
def product_kb(product_id, price, stars_price) -> InlineKeyboardMarkup:
    """Создает клавиатуру продукта с кнопками для оплаты через ЮКасса, Robocassa и звездами, а также кнопками "Назад" и "На главную".

    Args:
        product_id: ID продукта.
        price: Цена продукта.
        stars_price: Цена продукта в звездах.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup, представляющий клавиатуру продукта.

    Как работает функция:
    1. Создает объект `InlineKeyboardBuilder`.
    2. Добавляет кнопки "💳 Оплатить ЮКасса", "💳 Оплатить Robocassa" и "⭐ Оплатить звездами" с соответствующими callback_data, включающими ID продукта и цену.
    3. Добавляет кнопки "🛍 Назад" с callback_data "catalog" и "🏠 На главную" с callback_data "home".
    4. Устанавливает количество кнопок в ряду равным 2.
    5. Преобразует объект `InlineKeyboardBuilder` в объект `InlineKeyboardMarkup` и возвращает его.
    """
    ...
```

### `get_product_buy_youkassa`

```python
def get_product_buy_youkassa(price) -> InlineKeyboardMarkup:
    """Создает клавиатуру для оплаты продукта через ЮКасса с кнопкой "Оплатить" и кнопкой "Отменить".

    Args:
        price: Цена продукта.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup, представляющий клавиатуру оплаты через ЮКасса.

    Как работает функция:
    1. Создает объект `InlineKeyboardMarkup` с двумя рядами кнопок.
    2. Первый ряд содержит кнопку "Оплатить {price}₽" с атрибутом `pay=True`, указывающим на необходимость оплаты.
    3. Второй ряд содержит кнопку "Отменить" с callback_data "home".
    4. Возвращает объект `InlineKeyboardMarkup`.
    """
    ...
```

### `get_product_buy_robocassa`

```python
def get_product_buy_robocassa(price: int, payment_link: str) -> InlineKeyboardMarkup:
    """Создает клавиатуру для оплаты продукта через Robocassa с кнопкой "Оплатить" и кнопкой "Отменить".

    Args:
        price (int): Цена продукта.
        payment_link (str): Ссылка на оплату в Robocassa.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup, представляющий клавиатуру оплаты через Robocassa.

    Как работает функция:
    1. Создает объект `InlineKeyboardMarkup` с двумя рядами кнопок.
    2. Первый ряд содержит кнопку "Оплатить {price}₽" с атрибутом `web_app`, содержащим объект `WebAppInfo` со ссылкой на оплату.
    3. Второй ряд содержит кнопку "Отменить" с callback_data "home".
    4. Возвращает объект `InlineKeyboardMarkup`.
    """
    ...
```

### `get_product_buy_stars`

```python
def get_product_buy_stars(price) -> InlineKeyboardMarkup:
    """Создает клавиатуру для оплаты продукта звездами с кнопкой "Оплатить" и кнопкой "Отменить".

    Args:
        price: Цена продукта в звездах.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup, представляющий клавиатуру оплаты звездами.

    Как работает функция:
    1. Создает объект `InlineKeyboardMarkup` с двумя рядами кнопок.
    2. Первый ряд содержит кнопку "Оплатить {price} ⭐" с атрибутом `pay=True`, указывающим на необходимость оплаты.
    3. Второй ряд содержит кнопку "Отменить" с callback_data "home".
    4. Возвращает объект `InlineKeyboardMarkup`.
    """
    ...