# Анализ кода модуля kbs.py

**Качество кода: 8/10**

- Плюсы:
    - Код хорошо структурирован и легко читается.
    - Используются `InlineKeyboardBuilder` и `ReplyKeyboardBuilder` для создания клавиатур, что является хорошей практикой.
    - Функции имеют понятные названия и назначения.
    - Код разбит на логические блоки.
- Минусы:
    - Отсутствует docstring для модуля и функций.
    - Не используется `from src.logger.logger import logger` для логирования ошибок.
    - Жестко заданные URL (например, для "Поддержать автора") и callback_data, стоит рассмотреть вынесение их в константы.
    - Не везде используется f-строки, где это уместно.
    - Для некоторых клавиатур нет описания, для чего они нужны.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля и каждой функции, чтобы улучшить документирование кода.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок.
3.  Вынести все callback_data в константы, для улучшения читаемости и упрощения изменения.
4.  Заменить конкатенацию строк на f-строки для большей читаемости.
5.  Добавить описания к клавиатурам (например, в docstring), для чего они нужны и как используются.
6.  Рассмотреть использование `settings` для хранения URL для "Поддержать автора".
7.  Добавить проверку на существование `payment_link` перед использованием в `get_product_buy_robocassa`.
8.  Изменить `InlineKeyboardMarkup(inline_keyboard=[...])` на `InlineKeyboardBuilder()`

**Оптимизированный код**

```python
"""
Модуль для создания клавиатур для Telegram-бота.
=========================================================================================

Этот модуль содержит функции для генерации различных типов клавиатур
(инлайн и обычных) для Telegram-бота, включая кнопки для основного меню,
каталога, покупок и оплаты товаров.

Пример использования
--------------------

Пример создания главной клавиатуры пользователя:

.. code-block:: python

    from bot.dao.models import Category
    user_id = 12345
    main_kb = main_user_kb(user_id)

    catalog_data = [Category(id=1, category_name='Category 1'), Category(id=2, category_name='Category 2')]
    catalog_kb_markup = catalog_kb(catalog_data)

"""
from typing import List
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

# from bot.app.utils import generate_payment_link # TODO: Проверить необходимость импорта
from bot.config import settings
from bot.dao.models import Category
from src.logger.logger import logger # Использование logger


MAIN_MENU_MY_PROFILE = "my_profile"
MAIN_MENU_CATALOG = "catalog"
MAIN_MENU_ABOUT = "about"
MAIN_MENU_ADMIN_PANEL = "admin_panel"
MAIN_MENU_HOME = "home"
MAIN_MENU_SUPPORT_AUTHOR_URL = 'https://t.me/tribute/app?startapp=deLN'

CATALOG_BACK_TO_HOME = "home"

PURCHASES_SHOW_PURCHASES = "purchases"
PURCHASES_BACK_TO_HOME = "home"

PRODUCT_BUY_YUKASSA = "buy_yukassa"
PRODUCT_BUY_ROBOCASSA = "buy_robocassa"
PRODUCT_BUY_STARS = "buy_stars"
PRODUCT_BACK_TO_CATALOG = "catalog"
PRODUCT_BACK_TO_HOME = "home"

def main_user_kb(user_id: int) -> InlineKeyboardMarkup:
    """
    Создает главную клавиатуру пользователя.

    Args:
        user_id (int): Идентификатор пользователя.

    Returns:
        InlineKeyboardMarkup: Главная клавиатура.
    """
    kb = InlineKeyboardBuilder()
    kb.button(text="👤 Мои покупки", callback_data=MAIN_MENU_MY_PROFILE)
    kb.button(text="🛍 Каталог", callback_data=MAIN_MENU_CATALOG)
    kb.button(text="ℹ️ О магазине", callback_data=MAIN_MENU_ABOUT)
    kb.button(text="🌟 Поддержать автора 🌟", url=MAIN_MENU_SUPPORT_AUTHOR_URL)
    if user_id in settings.ADMIN_IDS:
        kb.button(text="⚙️ Админ панель", callback_data=MAIN_MENU_ADMIN_PANEL)
    kb.adjust(1)
    return kb.as_markup()


def catalog_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для каталога категорий.

    Args:
        catalog_data (List[Category]): Список объектов Category.

    Returns:
        InlineKeyboardMarkup: Клавиатура каталога.
    """
    kb = InlineKeyboardBuilder()
    for category in catalog_data:
        kb.button(text=category.category_name, callback_data=f"category_{category.id}")
    kb.button(text="🏠 На главную", callback_data=CATALOG_BACK_TO_HOME)
    kb.adjust(2)
    return kb.as_markup()


def purchases_kb() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для просмотра покупок.

    Returns:
        InlineKeyboardMarkup: Клавиатура покупок.
    """
    kb = InlineKeyboardBuilder()
    kb.button(text="🗑 Смотреть покупки", callback_data=PURCHASES_SHOW_PURCHASES)
    kb.button(text="🏠 На главную", callback_data=PURCHASES_BACK_TO_HOME)
    kb.adjust(1)
    return kb.as_markup()


def product_kb(product_id: int, price: int, stars_price: int) -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для товара с вариантами оплаты.

    Args:
        product_id (int): Идентификатор товара.
        price (int): Цена товара в рублях.
        stars_price (int): Цена товара в звездах.

    Returns:
        InlineKeyboardMarkup: Клавиатура товара.
    """
    kb = InlineKeyboardBuilder()
    kb.button(text="💳 Оплатить ЮКасса", callback_data=f"{PRODUCT_BUY_YUKASSA}_{product_id}_{price}")
    kb.button(text="💳 Оплатить Robocassa", callback_data=f"{PRODUCT_BUY_ROBOCASSA}_{product_id}_{price}")
    kb.button(text="⭐ Оплатить звездами", callback_data=f"{PRODUCT_BUY_STARS}_{product_id}_{stars_price}")
    kb.button(text="🛍 Назад", callback_data=PRODUCT_BACK_TO_CATALOG)
    kb.button(text="🏠 На главную", callback_data=PRODUCT_BACK_TO_HOME)
    kb.adjust(2)
    return kb.as_markup()


def get_product_buy_youkassa(price: int) -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для оплаты через ЮKassa.

    Args:
        price (int): Цена товара.

    Returns:
        InlineKeyboardMarkup: Клавиатура оплаты через ЮKassa.
    """
    kb = InlineKeyboardBuilder()
    kb.button(text=f'Оплатить {price}₽', pay=True)
    kb.row(InlineKeyboardButton(text='Отменить', callback_data=MAIN_MENU_HOME))
    return kb.as_markup()


def get_product_buy_robocassa(price: int, payment_link: str) -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для оплаты через Robocassa.

    Args:
        price (int): Цена товара.
        payment_link (str): Ссылка на оплату.

    Returns:
         InlineKeyboardMarkup: Клавиатура оплаты через Robocassa.
    """
    if not payment_link:
        logger.error(f'Отсутствует payment_link {payment_link=}')
        return InlineKeyboardMarkup(inline_keyboard=[])
    kb = InlineKeyboardBuilder()
    kb.button(text=f'Оплатить {price}₽', web_app=WebAppInfo(url=payment_link))
    kb.row(InlineKeyboardButton(text='Отменить', callback_data=MAIN_MENU_HOME))
    return kb.as_markup()


def get_product_buy_stars(price: int) -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для оплаты звездами.

    Args:
        price (int): Цена товара в звездах.

    Returns:
        InlineKeyboardMarkup: Клавиатура оплаты звездами.
    """
    kb = InlineKeyboardBuilder()
    kb.button(text=f'Оплатить {price} ⭐', pay=True)
    kb.row(InlineKeyboardButton(text='Отменить', callback_data=MAIN_MENU_HOME))
    return kb.as_markup()
```