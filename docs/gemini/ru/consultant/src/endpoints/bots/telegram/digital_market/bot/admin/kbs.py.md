# Анализ кода модуля `kbs.py`

**Качество кода**
-  Соответствие требованиям по оформлению кода: 9/10
    -   Плюсы
        -   Код хорошо структурирован и читаем.
        -   Используются `InlineKeyboardBuilder` для создания клавиатур.
        -   Функции имеют понятные имена, отражающие их назначение.
        -   Присутствуют импорты необходимых модулей.
    -   Минусы
        -   Отсутствует docstring для модуля и функций.
        -   Используется snake_case для именования, но это не является критической проблемой
        -   Не везде используется `adjust` правильно, что может привести к нежелательному расположению кнопок
        -   Не используется logger

**Рекомендации по улучшению**
1.  Добавить docstring для модуля и каждой функции, описывающие их назначение, параметры и возвращаемые значения.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок.
3.  Уточнить использование `adjust` для более точного расположения кнопок.
4.  Обеспечить единообразие в именовании (использовать только snake_case).
5.  Добавить примеры использования в docstring.

**Оптимизированный код**

```python
"""
Модуль для создания inline клавиатур для административной панели Telegram бота.
===========================================================================

Этот модуль содержит функции для генерации различных inline клавиатур,
используемых в административной панели бота. Каждая функция возвращает
объект InlineKeyboardMarkup, готовый для отправки пользователю.

Пример использования
--------------------

.. code-block:: python

    from aiogram import Bot
    from aiogram.types import Message
    from src.endpoints.bots.telegram.digital_market.bot.admin.kbs import admin_kb

    bot = Bot(token="YOUR_TOKEN")

    async def send_admin_keyboard(message: Message):
        keyboard = admin_kb()
        await bot.send_message(message.chat.id, "Админ панель", reply_markup=keyboard)
"""
from typing import List
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.endpoints.bots.telegram.digital_market.bot.dao.models import Category
# Импорт логгера
from src.logger.logger import logger


def catalog_admin_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """
    Создает inline клавиатуру для управления категориями товаров в админ-панели.

    Args:
        catalog_data (List[Category]): Список объектов Category, для которых нужно создать кнопки.

    Returns:
        InlineKeyboardMarkup: Inline клавиатура с кнопками для каждой категории и кнопкой "Отмена".

    Example:
        >>> from src.endpoints.bots.telegram.digital_market.bot.dao.models import Category
        >>> categories = [Category(id=1, category_name='Электроника'), Category(id=2, category_name='Одежда')]
        >>> keyboard = catalog_admin_kb(categories)
        >>> assert isinstance(keyboard, InlineKeyboardMarkup)
    """
    kb = InlineKeyboardBuilder()
    # Добавляем кнопку для каждой категории
    for category in catalog_data:
        kb.button(text=category.category_name, callback_data=f'add_category_{category.id}')
    # Добавляем кнопку "Отмена"
    kb.button(text='Отмена', callback_data='admin_panel')
    kb.adjust(2) # Размещаем кнопки в 2 колонки
    return kb.as_markup()


def admin_send_file_kb() -> InlineKeyboardMarkup:
    """
    Создает inline клавиатуру для выбора отправки файла или отказа от него.

    Returns:
        InlineKeyboardMarkup: Inline клавиатура с кнопками "Без файла" и "Отмена".

    Example:
        >>> keyboard = admin_send_file_kb()
        >>> assert isinstance(keyboard, InlineKeyboardMarkup)
    """
    kb = InlineKeyboardBuilder()
    # Создаем кнопку "Без файла"
    kb.button(text='Без файла', callback_data='without_file')
    # Создаем кнопку "Отмена"
    kb.button(text='Отмена', callback_data='admin_panel')
    kb.adjust(2) # Размещаем кнопки в 2 колонки
    return kb.as_markup()


def admin_kb() -> InlineKeyboardMarkup:
    """
    Создает главную inline клавиатуру для административной панели.

    Returns:
        InlineKeyboardMarkup: Inline клавиатура с кнопками "Статистика", "Управлять товарами" и "На главную".

    Example:
        >>> keyboard = admin_kb()
        >>> assert isinstance(keyboard, InlineKeyboardMarkup)
    """
    kb = InlineKeyboardBuilder()
    # Создаем кнопку "📊 Статистика"
    kb.button(text='📊 Статистика', callback_data='statistic')
    # Создаем кнопку "🛍️ Управлять товарами"
    kb.button(text='🛍️ Управлять товарами', callback_data='process_products')
    # Создаем кнопку "🏠 На главную"
    kb.button(text='🏠 На главную', callback_data='home')
    kb.adjust(2)  # Размещаем кнопки в 2 колонки
    return kb.as_markup()


def admin_kb_back() -> InlineKeyboardMarkup:
    """
    Создает inline клавиатуру с кнопками "Админ панель" и "На главную".

    Returns:
        InlineKeyboardMarkup: Inline клавиатура с кнопками "Админ панель" и "На главную".

    Example:
        >>> keyboard = admin_kb_back()
        >>> assert isinstance(keyboard, InlineKeyboardMarkup)
    """
    kb = InlineKeyboardBuilder()
    # Создаем кнопку "⚙️ Админ панель"
    kb.button(text='⚙️ Админ панель', callback_data='admin_panel')
    # Создаем кнопку "🏠 На главную"
    kb.button(text='🏠 На главную', callback_data='home')
    kb.adjust(1) # Размещаем кнопки в 1 колонку
    return kb.as_markup()


def dell_product_kb(product_id: int) -> InlineKeyboardMarkup:
    """
    Создает inline клавиатуру для удаления товара.

    Args:
        product_id (int): ID товара, который нужно удалить.

    Returns:
        InlineKeyboardMarkup: Inline клавиатура с кнопками "Удалить", "Админ панель" и "На главную".

    Example:
        >>> keyboard = dell_product_kb(123)
        >>> assert isinstance(keyboard, InlineKeyboardMarkup)
    """
    kb = InlineKeyboardBuilder()
    # Создаем кнопку "🗑️ Удалить"
    kb.button(text='🗑️ Удалить', callback_data=f'dell_{product_id}')
    # Создаем кнопку "⚙️ Админ панель"
    kb.button(text='⚙️ Админ панель', callback_data='admin_panel')
    # Создаем кнопку "🏠 На главную"
    kb.button(text='🏠 На главную', callback_data='home')
    kb.adjust(2, 1)  # Размещаем кнопки в 2 ряда: 2 кнопки в первом и 1 во втором
    return kb.as_markup()


def product_management_kb() -> InlineKeyboardMarkup:
    """
    Создает inline клавиатуру для управления товарами.

    Returns:
        InlineKeyboardMarkup: Inline клавиатура с кнопками "Добавить товар", "Удалить товар", "Админ панель" и "На главную".

    Example:
        >>> keyboard = product_management_kb()
        >>> assert isinstance(keyboard, InlineKeyboardMarkup)
    """
    kb = InlineKeyboardBuilder()
    # Создаем кнопку "➕ Добавить товар"
    kb.button(text='➕ Добавить товар', callback_data='add_product')
    # Создаем кнопку "🗑️ Удалить товар"
    kb.button(text='🗑️ Удалить товар', callback_data='delete_product')
    # Создаем кнопку "⚙️ Админ панель"
    kb.button(text='⚙️ Админ панель', callback_data='admin_panel')
    # Создаем кнопку "🏠 На главную"
    kb.button(text='🏠 На главную', callback_data='home')
    kb.adjust(2, 2)  # Размещаем кнопки в 2 ряда: 2 кнопки в каждом
    return kb.as_markup()


def cancel_kb_inline() -> InlineKeyboardMarkup:
    """
    Создает inline клавиатуру с кнопкой "Отмена".

    Returns:
        InlineKeyboardMarkup: Inline клавиатура с кнопкой "Отмена".

    Example:
        >>> keyboard = cancel_kb_inline()
        >>> assert isinstance(keyboard, InlineKeyboardMarkup)
    """
    kb = InlineKeyboardBuilder()
    # Создаем кнопку "Отмена"
    kb.button(text='Отмена', callback_data='cancel')
    return kb.as_markup()


def admin_confirm_kb() -> InlineKeyboardMarkup:
    """
    Создает inline клавиатуру с кнопками "Все верно" и "Отмена".

    Returns:
        InlineKeyboardMarkup: Inline клавиатура с кнопками "Все верно" и "Отмена".

    Example:
        >>> keyboard = admin_confirm_kb()
        >>> assert isinstance(keyboard, InlineKeyboardMarkup)
    """
    kb = InlineKeyboardBuilder()
    # Создаем кнопку "Все верно"
    kb.button(text='Все верно', callback_data='confirm_add')
    # Создаем кнопку "Отмена"
    kb.button(text='Отмена', callback_data='admin_panel')
    kb.adjust(1) # Размещаем кнопки в 1 колонку
    return kb.as_markup()
```