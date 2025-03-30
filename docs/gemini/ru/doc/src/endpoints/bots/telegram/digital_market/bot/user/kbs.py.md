# Модуль kbs

## Обзор

Модуль `kbs.py` предназначен для формирования клавиатур (keyboard) для Telegram-бота, используемого в цифровом магазине.
Он включает в себя функции для создания различных типов клавиатур, таких как главная клавиатура пользователя, клавиатура каталога,
клавиатура для просмотра покупок и клавиатуры для выбора способов оплаты продукта.
Каждая функция создает `InlineKeyboardMarkup` с кнопками, настроенными с использованием `InlineKeyboardBuilder`
из библиотеки `aiogram`.

## Подробней

Основное назначение модуля - предоставить набор функций, которые упрощают создание интерактивных клавиатур для
пользовательского интерфейса Telegram-бота. Эти клавиатуры позволяют пользователям навигировать по магазину,
просматривать каталог, управлять своими покупками и выбирать предпочтительные способы оплаты.
Модуль активно использует колбэки (callback data) для обработки действий пользователя и динамического обновления интерфейса бота.

## Функции

### `main_user_kb`

```python
def main_user_kb(user_id: int) -> InlineKeyboardMarkup:
    """
    Args:
        user_id (int): ID пользователя.

    Returns:
        InlineKeyboardMarkup: Клавиатура с основными функциями пользователя.
    """
```

**Описание**: Создает главную клавиатуру пользователя с кнопками для перехода в профиль, каталог, информации о магазине и поддержки автора.

**Параметры**:
- `user_id` (int): ID пользователя, который используется для определения, является ли пользователь администратором.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup`, представляющий главную клавиатуру пользователя.

**Примеры**:
```python
from aiogram.types import InlineKeyboardMarkup
user_id = 12345  # Пример ID пользователя
main_keyboard = main_user_kb(user_id)
# main_keyboard - объект InlineKeyboardMarkup с кнопками "Мои покупки", "Каталог", "О магазине" и "Поддержать автора"
```

### `catalog_kb`

```python
def catalog_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """
    Args:
        catalog_data (List[Category]): Список категорий для отображения в каталоге.

    Returns:
        InlineKeyboardMarkup: Клавиатура с категориями каталога.
    """
```

**Описание**: Создает клавиатуру каталога на основе списка категорий.

**Параметры**:
- `catalog_data` (List[Category]): Список объектов `Category`, представляющих категории товаров.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup`, представляющий клавиатуру каталога.

**Примеры**:
```python
from aiogram.types import InlineKeyboardMarkup
from bot.dao.models import Category
catalog_data = [
    Category(id=1, category_name="Электроника"),
    Category(id=2, category_name="Одежда")
]
catalog_keyboard = catalog_kb(catalog_data)
# catalog_keyboard - объект InlineKeyboardMarkup с кнопками "Электроника", "Одежда" и "На главную"
```

### `purchases_kb`

```python
def purchases_kb() -> InlineKeyboardMarkup:
    """
    Returns:
        InlineKeyboardMarkup: Клавиатура для управления покупками пользователя.
    """
```

**Описание**: Создает клавиатуру для управления покупками пользователя.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками для просмотра покупок и возврата на главную.

**Примеры**:
```python
from aiogram.types import InlineKeyboardMarkup
purchases_keyboard = purchases_kb()
# purchases_keyboard - объект InlineKeyboardMarkup с кнопками "Смотреть покупки" и "На главную"
```

### `product_kb`

```python
def product_kb(product_id, price, stars_price) -> InlineKeyboardMarkup:
    """
    Args:
        product_id: id продукта
        price: цена продукта
        stars_price: цена продукта в звездах

    Returns:
        InlineKeyboardMarkup: Клавиатура для выбора способа оплаты продукта.
    """
```

**Описание**: Создает клавиатуру для выбора способа оплаты продукта.

**Параметры**:
- `product_id`: ID продукта.
- `price`: Цена продукта.
- `stars_price`: Цена продукта в звездах.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками для выбора способов оплаты (ЮКасса, Robocassa, звезды) и возврата в каталог или на главную.

**Примеры**:
```python
from aiogram.types import InlineKeyboardMarkup
product_keyboard = product_kb(product_id=123, price=100, stars_price=50)
# product_keyboard - объект InlineKeyboardMarkup с кнопками "Оплатить ЮКасса", "Оплатить Robocassa", "Оплатить звездами", "Назад" и "На главную"
```

### `get_product_buy_youkassa`

```python
def get_product_buy_youkassa(price) -> InlineKeyboardMarkup:
    """
    Args:
        price: Цена продукта

    Returns:
        InlineKeyboardMarkup: Клавиатура для оплаты продукта через ЮКасса.
    """
```

**Описание**: Создает клавиатуру для оплаты продукта через ЮКасса.

**Параметры**:
- `price`: Цена продукта.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками для оплаты через ЮКасса и отмены.

**Примеры**:
```python
from aiogram.types import InlineKeyboardMarkup
youkassa_keyboard = get_product_buy_youkassa(price=100)
# youkassa_keyboard - объект InlineKeyboardMarkup с кнопками "Оплатить 100₽" и "Отменить"
```

### `get_product_buy_robocassa`

```python
def get_product_buy_robocassa(price: int, payment_link: str) -> InlineKeyboardMarkup:
    """
    Args:
        price (int): Цена продукта
        payment_link (str): Ссылка на оплату через Robocassa

    Returns:
        InlineKeyboardMarkup: Клавиатура для оплаты продукта через Robocassa.
    """
```

**Описание**: Создает клавиатуру для оплаты продукта через Robocassa.

**Параметры**:
- `price` (int): Цена продукта.
- `payment_link` (str): Ссылка на оплату через Robocassa.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками для оплаты через Robocassa и отмены.

**Примеры**:
```python
from aiogram.types import InlineKeyboardMarkup
robocassa_keyboard = get_product_buy_robocassa(price=100, payment_link="https://example.com/robocassa_payment")
# robocassa_keyboard - объект InlineKeyboardMarkup с кнопками "Оплатить 100₽" и "Отменить"
```

### `get_product_buy_stars`

```python
def get_product_buy_stars(price) -> InlineKeyboardMarkup:
    """
    Args:
        price: Цена продукта в звездах

    Returns:
        InlineKeyboardMarkup: Клавиатура для оплаты продукта звездами.
    """
```

**Описание**: Создает клавиатуру для оплаты продукта звездами.

**Параметры**:
- `price`: Цена продукта в звездах.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками для оплаты звездами и отмены.

**Примеры**:
```python
from aiogram.types import InlineKeyboardMarkup
stars_keyboard = get_product_buy_stars(price=50)
# stars_keyboard - объект InlineKeyboardMarkup с кнопками "Оплатить 50 ⭐" и "Отменить"