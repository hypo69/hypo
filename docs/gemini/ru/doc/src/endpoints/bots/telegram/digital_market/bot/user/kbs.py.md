# Модуль для создания клавиатур для Telegram-бота цифрового магазина
====================================================================

Модуль содержит функции для создания различных типов клавиатур (InlineKeyboardMarkup и ReplyKeyboardMarkup), используемых в Telegram-боте для цифрового магазина.
Эти клавиатуры предоставляют пользователям интерфейс для навигации по магазину, просмотра каталога, совершения покупок и управления профилем.

Пример использования
----------------------

```python
from aiogram.types import InlineKeyboardMarkup
from bot.dao.models import Category
from typing import List

# Пример создания главной клавиатуры пользователя
user_id = 12345
main_keyboard: InlineKeyboardMarkup = main_user_kb(user_id)

# Пример создания клавиатуры каталога
catalog_data: List[Category] = [...]  # Заполните данными категорий
catalog_keyboard: InlineKeyboardMarkup = catalog_kb(catalog_data)
```

## Обзор

Модуль `kbs.py` предназначен для формирования интерактивных клавиатур, используемых в Telegram-боте цифрового магазина.
Он включает в себя функции для создания главной клавиатуры пользователя, клавиатуры каталога, клавиатуры покупок и клавиатуры продукта.
Клавиатуры создаются с использованием библиотеки `aiogram` и содержат кнопки для навигации, совершения покупок и выполнения других действий.

## Подробней

Этот модуль предоставляет набор функций для генерации клавиатур для Telegram-бота, облегчая взаимодействие пользователей с ботом.
Он использует библиотеку `aiogram` для создания и управления клавиатурами, а также интегрируется с базой данных для отображения информации о категориях и продуктах.

## Функции

### `main_user_kb`

```python
def main_user_kb(user_id: int) -> InlineKeyboardMarkup:
    """Создает главную клавиатуру пользователя.

    Args:
        user_id (int): ID пользователя.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками "Мои покупки", "Каталог", "О магазине", "Поддержать автора" и "Админ панель" (если пользователь является администратором).
    """
```

**Назначение**: Создает главную клавиатуру для пользователя в Telegram-боте. Эта клавиатура предоставляет пользователю основные опции, такие как просмотр профиля, переход в каталог, получение информации о магазине и поддержка автора. Если пользователь является администратором, также отображается кнопка для доступа к панели администратора.

**Параметры**:
- `user_id` (int): ID пользователя, для которого создается клавиатура. Используется для определения, является ли пользователь администратором.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с настроенными кнопками.

**Как работает функция**:

1.  Создает экземпляр `InlineKeyboardBuilder`.
2.  Добавляет кнопки "👤 Мои покупки", "🛍 Каталог", "ℹ️ О магазине" и "🌟 Поддержать автора" с соответствующими callback_data или URL.
3.  Проверяет, является ли `user_id` администратором (содержится ли в `settings.ADMIN_IDS`). Если да, добавляет кнопку "⚙️ Админ панель".
4.  Устанавливает количество кнопок в строке (adjust(1)).
5.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

user_id = 12345
main_keyboard: InlineKeyboardMarkup = main_user_kb(user_id)
```

### `catalog_kb`

```python
def catalog_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """Создает клавиатуру каталога.

    Args:
        catalog_data (List[Category]): Список объектов Category.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками категорий и кнопкой "🏠 На главную".
    """
```

**Назначение**: Создает клавиатуру каталога на основе списка категорий. Каждая категория отображается в виде кнопки, при нажатии на которую пользователь переходит к списку товаров в этой категории. Также добавляется кнопка для возврата на главную страницу.

**Параметры**:
- `catalog_data` (List[Category]): Список объектов `Category`, представляющих категории товаров.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками категорий и кнопкой "🏠 На главную".

**Как работает функция**:

1.  Создает экземпляр `InlineKeyboardBuilder`.
2.  Итерируется по списку `catalog_data` и для каждой категории создает кнопку с именем категории и callback_data, содержащим ID категории.
3.  Добавляет кнопку "🏠 На главную" с callback_data "home".
4.  Устанавливает количество кнопок в строке (adjust(2)).
5.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from bot.dao.models import Category
from typing import List

catalog_data: List[Category] = [...]  # Заполните данными категорий
catalog_keyboard: InlineKeyboardMarkup = catalog_kb(catalog_data)
```

### `purchases_kb`

```python
def purchases_kb() -> InlineKeyboardMarkup:
    """Создает клавиатуру для управления покупками.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками "🗑 Смотреть покупки" и "🏠 На главную".
    """
```

**Назначение**: Создает клавиатуру для управления покупками пользователя. Предоставляет кнопки для просмотра списка покупок и возврата на главную страницу.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками "🗑 Смотреть покупки" и "🏠 На главную".

**Как работает функция**:

1.  Создает экземпляр `InlineKeyboardBuilder`.
2.  Добавляет кнопку "🗑 Смотреть покупки" с callback_data "purchases".
3.  Добавляет кнопку "🏠 На главную" с callback_data "home".
4.  Устанавливает количество кнопок в строке (adjust(1)).
5.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

purchases_keyboard: InlineKeyboardMarkup = purchases_kb()
```

### `product_kb`

```python
def product_kb(product_id, price, stars_price) -> InlineKeyboardMarkup:
    """Создает клавиатуру продукта.

    Args:
        product_id: ID продукта.
        price: Цена продукта в рублях.
        stars_price: Цена продукта в звездах.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками оплаты через ЮКасса, Robocassa и звездами, а также кнопками "🛍 Назад" и "🏠 На главную".
    """
```

**Назначение**: Создает клавиатуру продукта с опциями оплаты через различные платежные системы (ЮКасса, Robocassa, звезды) и кнопками для возврата в каталог и на главную страницу.

**Параметры**:
- `product_id`: ID продукта.
- `price`: Цена продукта в рублях.
- `stars_price`: Цена продукта в звездах.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками оплаты через ЮКасса, Robocassa и звездами, а также кнопками "🛍 Назад" и "🏠 На главную".

**Как работает функция**:

1.  Создает экземпляр `InlineKeyboardBuilder`.
2.  Добавляет кнопки оплаты через ЮКасса, Robocassa и звездами с соответствующими callback_data, включающими ID продукта и цену.
3.  Добавляет кнопки "🛍 Назад" с callback_data "catalog" и "🏠 На главную" с callback_data "home".
4.  Устанавливает количество кнопок в строке (adjust(2)).
5.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

product_id = 123
price = 100
stars_price = 50
product_keyboard: InlineKeyboardMarkup = product_kb(product_id, price, stars_price)
```

### `get_product_buy_youkassa`

```python
def get_product_buy_youkassa(price) -> InlineKeyboardMarkup:
    """Создает клавиатуру для покупки продукта через ЮКасса.

    Args:
        price: Цена продукта.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопкой оплаты через ЮКасса и кнопкой "Отменить".
    """
```

**Назначение**: Создает клавиатуру для оплаты продукта через ЮКасса. Предоставляет кнопку для совершения платежа и кнопку для отмены операции и возврата на главную страницу.

**Параметры**:
- `price`: Цена продукта.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопкой оплаты через ЮКасса и кнопкой "Отменить".

**Как работает функция**:

1.  Создает экземпляр `InlineKeyboardMarkup`.
2.  Добавляет кнопку оплаты с текстом, включающим цену, и атрибутом `pay=True`, что указывает на необходимость оплаты.
3.  Добавляет кнопку "Отменить" с callback_data "home".
4.  Возвращает созданную клавиатуру.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

price = 100
youkassa_keyboard: InlineKeyboardMarkup = get_product_buy_youkassa(price)
```

### `get_product_buy_robocassa`

```python
def get_product_buy_robocassa(price: int, payment_link: str) -> InlineKeyboardMarkup:
    """Создает клавиатуру для покупки продукта через Robocassa.

    Args:
        price (int): Цена продукта.
        payment_link (str): Ссылка на оплату в Robocassa.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопкой оплаты через Robocassa и кнопкой "Отменить".
    """
```

**Назначение**: Создает клавиатуру для оплаты продукта через Robocassa. Предоставляет кнопку для перехода по ссылке на оплату в Robocassa и кнопку для отмены операции и возврата на главную страницу.

**Параметры**:
- `price` (int): Цена продукта.
- `payment_link` (str): Ссылка на оплату в Robocassa.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопкой оплаты через Robocassa и кнопкой "Отменить".

**Как работает функция**:

1.  Создает экземпляр `InlineKeyboardMarkup`.
2.  Добавляет кнопку оплаты с текстом, включающим цену, и атрибутом `web_app`, содержащим ссылку на оплату в Robocassa.
3.  Добавляет кнопку "Отменить" с callback_data "home".
4.  Возвращает созданную клавиатуру.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

price = 100
payment_link = "https://example.com/robocassa_payment"
robocassa_keyboard: InlineKeyboardMarkup = get_product_buy_robocassa(price, payment_link)
```

### `get_product_buy_stars`

```python
def get_product_buy_stars(price) -> InlineKeyboardMarkup:
    """Создает клавиатуру для покупки продукта за звезды.

    Args:
        price: Цена продукта в звездах.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопкой оплаты звездами и кнопкой "Отменить".
    """
```

**Назначение**: Создает клавиатуру для оплаты продукта с использованием "звезд". Предоставляет кнопку для совершения оплаты звездами и кнопку для отмены операции и возврата на главную страницу.

**Параметры**:
- `price`: Цена продукта в звездах.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопкой оплаты звездами и кнопкой "Отменить".

**Как работает функция**:

1.  Создает экземпляр `InlineKeyboardMarkup`.
2.  Добавляет кнопку оплаты с текстом, включающим цену в звездах, и атрибутом `pay=True`, что указывает на необходимость оплаты.
3.  Добавляет кнопку "Отменить" с callback_data "home".
4.  Возвращает созданную клавиатуру.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

price = 50
stars_keyboard: InlineKeyboardMarkup = get_product_buy_stars(price)