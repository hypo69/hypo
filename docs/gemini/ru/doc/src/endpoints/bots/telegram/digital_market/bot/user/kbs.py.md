# Модуль для создания клавиатур для Telegram-бота цифрового рынка
=================================================================

Модуль содержит функции для создания различных типов клавиатур, используемых в Telegram-боте цифрового рынка.
Клавиатуры включают главную клавиатуру пользователя, клавиатуру каталога, клавиатуру покупок и клавиатуру продукта.

## Обзор

Этот модуль предоставляет набор функций для генерации интерактивных клавиатур, которые помогают пользователям взаимодействовать с ботом.
Он использует библиотеку `aiogram` для создания inline-клавиатур и кнопок, а также включает функциональность для обработки платежей через различные системы, такие как ЮKassa и Robocassa.

## Подробнее

Модуль `kbs.py` предназначен для создания пользовательских клавиатур в Telegram-боте, которые упрощают навигацию и взаимодействие с различными функциями, такими как просмотр каталога, совершение покупок и управление профилем.
Используя этот модуль, разработчики могут легко настраивать клавиатуры для различных сценариев использования бота.

## Функции

### `main_user_kb`

```python
def main_user_kb(user_id: int) -> InlineKeyboardMarkup:
    """Создает главную клавиатуру пользователя.

    Args:
        user_id (int): ID пользователя.

    Returns:
        InlineKeyboardMarkup: Главная клавиатура пользователя.

    Example:
        >>> main_user_kb(12345)
        <InlineKeyboardMarkup object>
    """
```

**Назначение**: Создает главную клавиатуру пользователя с кнопками для доступа к основным функциям бота.

**Параметры**:
- `user_id` (int): ID пользователя, используемый для определения, показывать ли кнопку администратора.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект inline-клавиатуры, содержащий кнопки "👤 Мои покупки", "🛍 Каталог", "ℹ️ О магазине", "🌟 Поддержать автора 🌟" и, если пользователь является администратором, "⚙️ Админ панель".

**Как работает функция**:

1. Инициализируется построитель inline-клавиатуры (`InlineKeyboardBuilder`).
2. Добавляются кнопки: "👤 Мои покупки", "🛍 Каталог", "ℹ️ О магазине", "🌟 Поддержать автора 🌟".
3. Проверяется, является ли `user_id` ID администратора (содержится ли он в `settings.ADMIN_IDS`).
4. Если пользователь является администратором, добавляется кнопка "⚙️ Админ панель".
5. Устанавливается количество кнопок в строке (`adjust(1)`).
6. Клавиатура преобразуется в объект `InlineKeyboardMarkup` и возвращается.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from bot.config import settings  # Предполагается, что settings определен
settings.ADMIN_IDS = [12345]
user_id = 12345
result = main_user_kb(user_id)
assert isinstance(result, InlineKeyboardMarkup)
```

### `catalog_kb`

```python
def catalog_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """Создает клавиатуру каталога.

    Args:
        catalog_data (List[Category]): Список категорий каталога.

    Returns:
        InlineKeyboardMarkup: Клавиатура каталога.

    Example:
        >>> catalog_kb([Category(id=1, category_name='Электроника')])
        <InlineKeyboardMarkup object>
    """
```

**Назначение**: Создает клавиатуру каталога на основе предоставленных данных о категориях.

**Параметры**:
- `catalog_data` (List[Category]): Список объектов `Category`, каждый из которых представляет категорию в каталоге.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект inline-клавиатуры, содержащий кнопки для каждой категории и кнопку "🏠 На главную".

**Как работает функция**:

1. Инициализируется построитель inline-клавиатуры (`InlineKeyboardBuilder`).
2. Перебирается список `catalog_data`.
3. Для каждой категории создается кнопка с текстом, равным имени категории (`category.category_name`), и callback_data, содержащим ID категории (`category.id`).
4. Добавляется кнопка "🏠 На главную".
5. Устанавливается количество кнопок в строке (`adjust(2)`).
6. Клавиатура преобразуется в объект `InlineKeyboardMarkup` и возвращается.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from bot.dao.models import Category  # Предполагается, что Category определен

catalog_data = [
    Category(id=1, category_name='Электроника'),
    Category(id=2, category_name='Одежда')
]
result = catalog_kb(catalog_data)
assert isinstance(result, InlineKeyboardMarkup)
```

### `purchases_kb`

```python
def purchases_kb() -> InlineKeyboardMarkup:
    """Создает клавиатуру покупок.

    Returns:
        InlineKeyboardMarkup: Клавиатура покупок.

    Example:
        >>> purchases_kb()
        <InlineKeyboardMarkup object>
    """
```

**Назначение**: Создает клавиатуру для управления покупками пользователя.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект inline-клавиатуры с кнопками "🗑 Смотреть покупки" и "🏠 На главную".

**Как работает функция**:

1. Инициализируется построитель inline-клавиатуры (`InlineKeyboardBuilder`).
2. Добавляются кнопки "🗑 Смотреть покупки" и "🏠 На главную".
3. Устанавливается количество кнопок в строке (`adjust(1)`).
4. Клавиатура преобразуется в объект `InlineKeyboardMarkup` и возвращается.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

result = purchases_kb()
assert isinstance(result, InlineKeyboardMarkup)
```

### `product_kb`

```python
def product_kb(product_id, price, stars_price) -> InlineKeyboardMarkup:
    """Создает клавиатуру продукта.

    Args:
        product_id (int): ID продукта.
        price (int): Цена продукта в рублях.
        stars_price (int): Цена продукта в звездах.

    Returns:
        InlineKeyboardMarkup: Клавиатура продукта.

    Example:
        >>> product_kb(1, 100, 50)
        <InlineKeyboardMarkup object>
    """
```

**Назначение**: Создает клавиатуру для отображения опций покупки продукта.

**Параметры**:
- `product_id` (int): ID продукта.
- `price` (int): Цена продукта в рублях.
- `stars_price` (int): Цена продукта в звездах.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект inline-клавиатуры с кнопками для оплаты через ЮKassa, Robocassa, звездами, кнопкой "🛍 Назад" и кнопкой "🏠 На главную".

**Как работает функция**:

1. Инициализируется построитель inline-клавиатуры (`InlineKeyboardBuilder`).
2. Добавляются кнопки для оплаты через ЮKassa, Robocassa и звездами, каждая из которых содержит информацию о продукте и цене в callback_data.
3. Добавляются кнопки "🛍 Назад" и "🏠 На главную".
4. Устанавливается количество кнопок в строке (`adjust(2)`).
5. Клавиатура преобразуется в объект `InlineKeyboardMarkup` и возвращается.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

product_id = 1
price = 100
stars_price = 50
result = product_kb(product_id, price, stars_price)
assert isinstance(result, InlineKeyboardMarkup)
```

### `get_product_buy_youkassa`

```python
def get_product_buy_youkassa(price) -> InlineKeyboardMarkup:
    """Создает клавиатуру для покупки продукта через ЮKassa.

    Args:
        price (int): Цена продукта.

    Returns:
        InlineKeyboardMarkup: Клавиатура для покупки через ЮKassa.

    Example:
        >>> get_product_buy_youkassa(100)
        <InlineKeyboardMarkup object>
    """
```

**Назначение**: Создает клавиатуру для подтверждения оплаты продукта через ЮKassa.

**Параметры**:
- `price` (int): Цена продукта.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект inline-клавиатуры, содержащий кнопку для оплаты через ЮKassa и кнопку "Отменить".

**Как работает функция**:

1. Создается объект `InlineKeyboardMarkup`.
2. Добавляется кнопка с текстом, содержащим цену продукта и символом рубля, с атрибутом `pay=True`, что указывает на возможность оплаты.
3. Добавляется кнопка "Отменить" с callback_data "home".
4. Клавиатура возвращается.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

price = 100
result = get_product_buy_youkassa(price)
assert isinstance(result, InlineKeyboardMarkup)
```

### `get_product_buy_robocassa`

```python
def get_product_buy_robocassa(price: int, payment_link: str) -> InlineKeyboardMarkup:
    """Создает клавиатуру для покупки продукта через Robocassa.

    Args:
        price (int): Цена продукта.
        payment_link (str): Ссылка на оплату в Robocassa.

    Returns:
        InlineKeyboardMarkup: Клавиатура для покупки через Robocassa.

    Example:
        >>> get_product_buy_robocassa(100, 'https://example.com/robocassa_payment')
        <InlineKeyboardMarkup object>
    """
```

**Назначение**: Создает клавиатуру для перенаправления пользователя на страницу оплаты Robocassa.

**Параметры**:
- `price` (int): Цена продукта.
- `payment_link` (str): Ссылка для оплаты через Robocassa.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект inline-клавиатуры, содержащий кнопку для перехода на страницу оплаты Robocassa и кнопку "Отменить".

**Как работает функция**:

1. Создается объект `InlineKeyboardMarkup`.
2. Добавляется кнопка с текстом, содержащим цену продукта и символом рубля, и `web_app=WebAppInfo(url=payment_link)`, что позволяет открыть страницу оплаты в Robocassa.
3. Добавляется кнопка "Отменить" с callback_data "home".
4. Клавиатура возвращается.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup, WebAppInfo

price = 100
payment_link = 'https://example.com/robocassa_payment'
result = get_product_buy_robocassa(price, payment_link)
assert isinstance(result, InlineKeyboardMarkup)
```

### `get_product_buy_stars`

```python
def get_product_buy_stars(price) -> InlineKeyboardMarkup:
    """Создает клавиатуру для покупки продукта за звезды.

    Args:
        price (int): Цена продукта в звездах.

    Returns:
        InlineKeyboardMarkup: Клавиатура для покупки за звезды.

    Example:
        >>> get_product_buy_stars(50)
        <InlineKeyboardMarkup object>
    """
```

**Назначение**: Создает клавиатуру для подтверждения оплаты продукта звездами.

**Параметры**:
- `price` (int): Цена продукта в звездах.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект inline-клавиатуры, содержащий кнопку для оплаты звездами и кнопку "Отменить".

**Как работает функция**:

1. Создается объект `InlineKeyboardMarkup`.
2. Добавляется кнопка с текстом, содержащим цену продукта в звездах и символом звезды, с атрибутом `pay=True`, что указывает на возможность оплаты.
3. Добавляется кнопка "Отменить" с callback_data "home".
4. Клавиатура возвращается.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

price = 50
result = get_product_buy_stars(price)
assert isinstance(result, InlineKeyboardMarkup)
```