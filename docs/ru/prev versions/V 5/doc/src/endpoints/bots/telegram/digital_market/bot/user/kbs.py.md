# Модуль для создания клавиатур для Telegram бота цифрового магазина

## Обзор

Модуль `kbs.py` предназначен для создания различных клавиатур (клавиатурных интерфейсов) для Telegram-бота цифрового магазина. Он включает в себя функции для создания основных пользовательских клавиатур, каталога, покупок, а также клавиатур для оплаты продуктов с использованием различных платежных систем. Модуль использует библиотеку `aiogram` для создания клавиатур и кнопок.

## Подробней

Этот модуль играет ключевую роль в формировании пользовательского интерфейса бота. Он предоставляет функции для создания интерактивных клавиатур, которые позволяют пользователям перемещаться по каталогу, просматривать свои покупки, получать информацию о магазине и совершать оплату товаров. Каждая функция создает определенный тип клавиатуры с соответствующими кнопками и коллбэками. Расположение файла: `hypotez/src/endpoints/bots/telegram/digital_market/bot/user/kbs.py` указывает, что этот модуль является частью Telegram-бота цифрового магазина и отвечает за пользовательский интерфейс.

## Функции

### `main_user_kb`

```python
def main_user_kb(user_id: int) -> InlineKeyboardMarkup:
    """
    Args:
        user_id (int): ID пользователя.

    Returns:
        InlineKeyboardMarkup: Объект инлайн клавиатуры.

    """
```

**Описание**: Создает основную пользовательскую клавиатуру с кнопками "👤 Мои покупки", "🛍 Каталог", "ℹ️ О магазине", "🌟 Поддержать автора 🌟" и "⚙️ Админ панель" (если пользователь является админом).

**Как работает функция**: Функция создает объект `InlineKeyboardBuilder`, добавляет кнопки с соответствующими текстами и коллбэками. Если `user_id` находится в списке `settings.ADMIN_IDS`, добавляется кнопка "⚙️ Админ панель". Клавиатура адаптируется для отображения в одну колонку.

**Параметры**:

-   `user_id` (int): ID пользователя, используется для определения, является ли пользователь администратором.

**Возвращает**:

-   `InlineKeyboardMarkup`: Объект инлайн клавиатуры, готовый для отправки пользователю.

**Примеры**:

```python
from aiogram import Bot
from aiogram.types import Message

bot = Bot(token="YOUR_BOT_TOKEN")

async def send_main_keyboard(message: Message):
    user_id = message.from_user.id
    keyboard = main_user_kb(user_id)
    await bot.send_message(message.chat.id, "Главное меню", reply_markup=keyboard)
```

### `catalog_kb`

```python
def catalog_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """
    Args:
        catalog_data (List[Category]): Список объектов категорий.

    Returns:
        InlineKeyboardMarkup: Объект инлайн клавиатуры.

    """
```

**Описание**: Создает клавиатуру каталога на основе списка категорий.

**Как работает функция**: Функция создает объект `InlineKeyboardBuilder`, добавляет кнопки для каждой категории из `catalog_data` с коллбэками вида `category_{category.id}`. Также добавляется кнопка "🏠 На главную". Клавиатура адаптируется для отображения в две колонки.

**Параметры**:

-   `catalog_data` (List\[Category]): Список объектов категорий, где каждый объект содержит информацию о категории, такую как `category_name` и `id`.

**Возвращает**:

-   `InlineKeyboardMarkup`: Объект инлайн клавиатуры с категориями и кнопкой "🏠 На главную".

**Примеры**:

```python
from aiogram import Bot
from aiogram.types import Message
from bot.dao.models import Category

bot = Bot(token="YOUR_BOT_TOKEN")

async def send_catalog_keyboard(message: Message):
    catalog_data = [
        Category(id=1, category_name="Электроника"),
        Category(id=2, category_name="Одежда"),
    ]
    keyboard = catalog_kb(catalog_data)
    await bot.send_message(message.chat.id, "Каталог товаров", reply_markup=keyboard)
```

### `purchases_kb`

```python
def purchases_kb() -> InlineKeyboardMarkup:
    """
    Returns:
        InlineKeyboardMarkup: Объект инлайн клавиатуры.

    """
```

**Описание**: Создает клавиатуру для управления покупками пользователя.

**Как работает функция**: Функция создает объект `InlineKeyboardBuilder` и добавляет кнопки "🗑 Смотреть покупки" и "🏠 На главную". Клавиатура адаптируется для отображения в одну колонку.

**Возвращает**:

-   `InlineKeyboardMarkup`: Объект инлайн клавиатуры с кнопками для просмотра покупок и возврата на главную.

**Примеры**:

```python
from aiogram import Bot
from aiogram.types import Message

bot = Bot(token="YOUR_BOT_TOKEN")

async def send_purchases_keyboard(message: Message):
    keyboard = purchases_kb()
    await bot.send_message(message.chat.id, "Мои покупки", reply_markup=keyboard)
```

### `product_kb`

```python
def product_kb(product_id, price, stars_price) -> InlineKeyboardMarkup:
    """
    Args:
        product_id:
        price:
        stars_price:

    Returns:
        InlineKeyboardMarkup: Объект инлайн клавиатуры.

    """
```

**Описание**: Создает клавиатуру для отображения опций покупки продукта.

**Как работает функция**: Функция создает объект `InlineKeyboardBuilder` и добавляет кнопки для оплаты продукта через ЮКассу, Robocassa и звездами, а также кнопки "🛍 Назад" и "🏠 На главную". Клавиатура адаптируется для отображения в две колонки.

**Параметры**:

-   `product_id`: ID продукта.
-   `price`: Цена продукта в рублях.
-   `stars_price`: Цена продукта в звездах.

**Возвращает**:

-   `InlineKeyboardMarkup`: Объект инлайн клавиатуры с опциями покупки продукта.

**Примеры**:

```python
from aiogram import Bot
from aiogram.types import Message

bot = Bot(token="YOUR_BOT_TOKEN")

async def send_product_keyboard(message: Message, product_id: int, price: int, stars_price: int):
    keyboard = product_kb(product_id, price, stars_price)
    await bot.send_message(message.chat.id, "Выберите способ оплаты", reply_markup=keyboard)
```

### `get_product_buy_youkassa`

```python
def get_product_buy_youkassa(price) -> InlineKeyboardMarkup:
    """
    Args:
        price:

    Returns:
        InlineKeyboardMarkup: Объект инлайн клавиатуры.

    """
```

**Описание**: Создает клавиатуру для подтверждения покупки через ЮКассу.

**Как работает функция**: Функция создает объект `InlineKeyboardMarkup` с кнопкой для оплаты указанной цены и кнопкой "Отменить".

**Параметры**:

-   `price`: Цена продукта.

**Возвращает**:

-   `InlineKeyboardMarkup`: Объект инлайн клавиатуры с кнопкой оплаты через ЮКассу.

**Примеры**:

```python
from aiogram import Bot
from aiogram.types import Message

bot = Bot(token="YOUR_BOT_TOKEN")

async def send_youkassa_keyboard(message: Message, price: int):
    keyboard = get_product_buy_youkassa(price)
    await bot.send_message(message.chat.id, f"Оплатить {price}₽ через ЮКассу?", reply_markup=keyboard)
```

### `get_product_buy_robocassa`

```python
def get_product_buy_robocassa(price: int, payment_link: str) -> InlineKeyboardMarkup:
    """
    Args:
        price (int):
        payment_link (str):

    Returns:
        InlineKeyboardMarkup: Объект инлайн клавиатуры.

    """
```

**Описание**: Создает клавиатуру для подтверждения покупки через Robocassa.

**Как работает функция**: Функция создает объект `InlineKeyboardMarkup` с кнопкой для оплаты указанной цены через Robocassa (с использованием `WebAppInfo`) и кнопкой "Отменить".

**Параметры**:

-   `price` (int): Цена продукта.
-   `payment_link` (str): Ссылка для оплаты через Robocassa.

**Возвращает**:

-   `InlineKeyboardMarkup`: Объект инлайн клавиатуры с кнопкой оплаты через Robocassa.

**Примеры**:

```python
from aiogram import Bot
from aiogram.types import Message

bot = Bot(token="YOUR_BOT_TOKEN")

async def send_robocassa_keyboard(message: Message, price: int, payment_link: str):
    keyboard = get_product_buy_robocassa(price, payment_link)
    await bot.send_message(message.chat.id, f"Оплатить {price}₽ через Robocassa?", reply_markup=keyboard)
```

### `get_product_buy_stars`

```python
def get_product_buy_stars(price) -> InlineKeyboardMarkup:
    """
    Args:
        price:

    Returns:
        InlineKeyboardMarkup: Объект инлайн клавиатуры.

    """
```

**Описание**: Создает клавиатуру для подтверждения покупки за звезды.

**Как работает функция**: Функция создает объект `InlineKeyboardMarkup` с кнопкой для оплаты указанной цены звездами и кнопкой "Отменить".

**Параметры**:

-   `price`: Цена продукта в звездах.

**Возвращает**:

-   `InlineKeyboardMarkup`: Объект инлайн клавиатуры с кнопкой оплаты звездами.

**Примеры**:

```python
from aiogram import Bot
from aiogram.types import Message

bot = Bot(token="YOUR_BOT_TOKEN")

async def send_stars_keyboard(message: Message, price: int):
    keyboard = get_product_buy_stars(price)
    await bot.send_message(message.chat.id, f"Оплатить {price} ⭐?", reply_markup=keyboard)
```