# Модуль для создания клавиатур для Telegram-бота цифрового рынка

## Обзор

Модуль `kbs.py` предназначен для создания различных клавиатур (инлайн и обычных) для Telegram-бота цифрового рынка. Он содержит функции для создания клавиатур главного меню, каталога, покупок, продукта и оплаты.

## Подробнее

Этот модуль предоставляет набор функций для генерации интерактивных клавиатур, которые используются в Telegram-боте для навигации, отображения каталога товаров, управления покупками и осуществления платежей через различные платежные системы. Он использует библиотеку `aiogram` для создания клавиатур и включает интеграцию с платежными системами ЮKassa и Robocassa, а также возможность оплаты внутренними "звездами". Расположение файла в структуре проекта указывает на его роль в формировании пользовательского интерфейса бота.

## Функции

### `main_user_kb`

```python
def main_user_kb(user_id: int) -> InlineKeyboardMarkup:
    """Создает главную клавиатуру пользователя с кнопками "Мои покупки", "Каталог", "О магазине", "Поддержать автора" и "Админ панель" (для администраторов).

    Args:
        user_id (int): ID пользователя.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.

    """
    kb = InlineKeyboardBuilder()
    kb.button(text="👤 Мои покупки", callback_data="my_profile")
    kb.button(text="🛍 Каталог", callback_data="catalog")
    kb.button(text="ℹ️ О магазине", callback_data="about")
    kb.button(text="🌟 Поддержать автора 🌟", url='https://t.me/tribute/app?startapp=deLN')
    if user_id in settings.ADMIN_IDS:
        kb.button(text="⚙️ Админ панель", callback_data="admin_panel")
    kb.adjust(1)
    return kb.as_markup()
```

**Как работает функция**:

1.  Создает экземпляр `InlineKeyboardBuilder` для построения инлайн-клавиатуры.
2.  Добавляет кнопки "👤 Мои покупки", "🛍 Каталог", "ℹ️ О магазине", "🌟 Поддержать автора 🌟" с соответствующими callback-data или URL.
3.  Проверяет, является ли `user_id` администратором, и добавляет кнопку "⚙️ Админ панель", если это так.
4.  Устанавливает количество кнопок в строке равным 1 с помощью `kb.adjust(1)`.
5.  Преобразует построенную клавиатуру в объект `InlineKeyboardMarkup` с помощью `kb.as_markup()` и возвращает его.

**Параметры**:

*   `user_id` (int): ID пользователя, для которого создается клавиатура. Используется для определения, показывать ли кнопку административной панели.

**Возвращает**:

*   `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками главного меню пользователя.

### `catalog_kb`

```python
def catalog_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """Создает клавиатуру каталога с кнопками для каждой категории и кнопкой "На главную".

    Args:
        catalog_data (List[Category]): Список объектов категорий.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.

    """
    kb = InlineKeyboardBuilder()
    for category in catalog_data:
        kb.button(text=category.category_name, callback_data=f"category_{category.id}")
    kb.button(text="🏠 На главную", callback_data="home")
    kb.adjust(2)
    return kb.as_markup()
```

**Как работает функция**:

1.  Создает экземпляр `InlineKeyboardBuilder` для построения инлайн-клавиатуры.
2.  Перебирает список категорий `catalog_data` и для каждой категории создает кнопку с названием категории и callback_data в формате `"category_{category.id}"`.
3.  Добавляет кнопку "🏠 На главную" с callback_data `"home"`.
4.  Устанавливает количество кнопок в строке равным 2 с помощью `kb.adjust(2)`.
5.  Преобразует построенную клавиатуру в объект `InlineKeyboardMarkup` с помощью `kb.as_markup()` и возвращает его.

**Параметры**:

*   `catalog_data` (List\[Category]): Список объектов `Category`, содержащих информацию о категориях товаров.

**Возвращает**:

*   `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками категорий и кнопкой "На главную".

### `purchases_kb`

```python
def purchases_kb() -> InlineKeyboardMarkup:
    """Создает клавиатуру для раздела покупок с кнопками "Смотреть покупки" и "На главную".

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.

    """
    kb = InlineKeyboardBuilder()
    kb.button(text="🗑 Смотреть покупки", callback_data="purchases")
    kb.button(text="🏠 На главную", callback_data="home")
    kb.adjust(1)
    return kb.as_markup()
```

**Как работает функция**:

1.  Создает экземпляр `InlineKeyboardBuilder` для построения инлайн-клавиатуры.
2.  Добавляет кнопку "🗑 Смотреть покупки" с callback_data `"purchases"`.
3.  Добавляет кнопку "🏠 На главную" с callback_data `"home"`.
4.  Устанавливает количество кнопок в строке равным 1 с помощью `kb.adjust(1)`.
5.  Преобразует построенную клавиатуру в объект `InlineKeyboardMarkup` с помощью `kb.as_markup()` и возвращает его.

**Возвращает**:

*   `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками "Смотреть покупки" и "На главную".

### `product_kb`

```python
def product_kb(product_id, price, stars_price) -> InlineKeyboardMarkup:
    """Создает клавиатуру продукта с кнопками для оплаты через ЮКасса, Robocassa, звездами, а также кнопки "Назад" и "На главную".

    Args:
        product_id (int): ID продукта.
        price (int): Цена продукта.
        stars_price (int): Цена продукта в звездах.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.

    """
    kb = InlineKeyboardBuilder()
    kb.button(text="💳 Оплатить ЮКасса", callback_data=f"buy_yukassa_{product_id}_{price}")
    kb.button(text="💳 Оплатить Robocassa", callback_data=f"buy_robocassa_{product_id}_{price}")
    kb.button(text="⭐ Оплатить звездами", callback_data=f"buy_stars_{product_id}_{stars_price}")
    kb.button(text="🛍 Назад", callback_data="catalog")
    kb.button(text="🏠 На главную", callback_data="home")
    kb.adjust(2)
    return kb.as_markup()
```

**Как работает функция**:

1.  Создает экземпляр `InlineKeyboardBuilder` для построения инлайн-клавиатуры.
2.  Добавляет кнопки для оплаты через ЮKassa, Robocassa и звездами, используя `product_id`, `price` и `stars_price` для формирования callback_data.
3.  Добавляет кнопки "🛍 Назад" и "🏠 На главную" с соответствующими callback_data.
4.  Устанавливает количество кнопок в строке равным 2 с помощью `kb.adjust(2)`.
5.  Преобразует построенную клавиатуру в объект `InlineKeyboardMarkup` с помощью `kb.as_markup()` и возвращает его.

**Параметры**:

*   `product_id` (int): ID продукта, для которого создается клавиатура.
*   `price` (int): Цена продукта в рублях.
*   `stars_price` (int): Цена продукта в "звездах".

**Возвращает**:

*   `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками оплаты и навигации.

### `get_product_buy_youkassa`

```python
def get_product_buy_youkassa(price) -> InlineKeyboardMarkup:
    """Создает клавиатуру для оплаты продукта через ЮКасса.

    Args:
        price (int): Цена продукта.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.

    """
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f'Оплатить {price}₽', pay=True)],
        [InlineKeyboardButton(text='Отменить', callback_data='home')]
    ])
```

**Как работает функция**:

1.  Создает `InlineKeyboardMarkup` напрямую, передавая список списков кнопок.
2.  Добавляет кнопку "Оплатить {price}₽" с установленным параметром `pay=True`, что указывает на кнопку оплаты.
3.  Добавляет кнопку "Отменить" с callback_data `"home"`.

**Параметры**:

*   `price` (int): Цена продукта в рублях.

**Возвращает**:

*   `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопкой оплаты через ЮКасса и кнопкой "Отменить".

### `get_product_buy_robocassa`

```python
def get_product_buy_robocassa(price: int, payment_link: str) -> InlineKeyboardMarkup:
    """Создает клавиатуру для оплаты продукта через Robocassa с использованием web_app.

    Args:
        price (int): Цена продукта.
        payment_link (str): Ссылка для оплаты через Robocassa.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.

    """
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text=f'Оплатить {price}₽',
            web_app=WebAppInfo(url=payment_link)
        )],
        [InlineKeyboardButton(text='Отменить', callback_data='home')]
    ])
```

**Как работает функция**:

1.  Создает `InlineKeyboardMarkup` напрямую, передавая список списков кнопок.
2.  Добавляет кнопку "Оплатить {price}₽", используя `WebAppInfo` для указания URL оплаты через Robocassa.
3.  Добавляет кнопку "Отменить" с callback_data `"home"`.

**Параметры**:

*   `price` (int): Цена продукта в рублях.
*   `payment_link` (str): URL для оплаты через Robocassa.

**Возвращает**:

*   `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопкой оплаты через Robocassa и кнопкой "Отменить".

### `get_product_buy_stars`

```python
def get_product_buy_stars(price) -> InlineKeyboardMarkup:
    """Создает клавиатуру для оплаты продукта звездами.

    Args:
        price (int): Цена продукта в звездах.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.

    """
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"Оплатить {price} ⭐", pay=True)],
        [InlineKeyboardButton(text='Отменить', callback_data='home')]
    ])
```

**Как работает функция**:

1.  Создает `InlineKeyboardMarkup` напрямую, передавая список списков кнопок.
2.  Добавляет кнопку "Оплатить {price} ⭐" с установленным параметром `pay=True`, что указывает на кнопку оплаты.
3.  Добавляет кнопку "Отменить" с callback_data `"home"`.

**Параметры**:

*   `price` (int): Цена продукта в "звездах".

**Возвращает**:

*   `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопкой оплаты звездами и кнопкой "Отменить".