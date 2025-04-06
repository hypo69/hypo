# Модуль для создания клавиатур администратора для Telegram-бота цифрового рынка
==================================================================

Модуль содержит функции для создания различных inline-клавиатур для административной панели Telegram-бота цифрового рынка.
Эти клавиатуры используются для управления каталогом, товарами, просмотра статистики и выполнения других административных задач.

## Обзор

Модуль `kbs.py` предоставляет набор функций для создания inline-клавиатур, используемых в Telegram-боте для административных целей. Клавиатуры создаются с использованием `InlineKeyboardBuilder` из библиотеки `aiogram` и содержат различные кнопки для навигации и выполнения действий, связанных с управлением каталогом, товарами и статистикой.

## Подробнее

Этот модуль содержит функции, генерирующие различные варианты клавиатур администратора.
Функции используют библиотеку `aiogram` для создания `InlineKeyboardBuilder`, добавляют кнопки с текстом и callback_data, и возвращают готовые `InlineKeyboardMarkup`.
Каждая функция создает клавиатуру для определенной цели, например, для отображения списка категорий каталога, подтверждения отправки файла, отображения панели администратора и т.д.

## Функции

### `catalog_admin_kb`

```python
def catalog_admin_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """Создает inline-клавиатуру для отображения категорий каталога в панели администратора.

    Args:
        catalog_data (List[Category]): Список объектов `Category`, представляющих категории каталога.

    Returns:
        InlineKeyboardMarkup: Объект `InlineKeyboardMarkup`, представляющий клавиатуру с категориями и кнопкой "Отмена".

    Как работает функция:
    1. Инициализирует `InlineKeyboardBuilder`.
    2. Перебирает список категорий `catalog_data`.
    3. Для каждой категории добавляет кнопку с названием категории и callback_data, содержащим id категории.
    4. Добавляет кнопку "Отмена" с callback_data "admin_panel".
    5. Устанавливает порядок размещения кнопок в два столбца.
    6. Возвращает созданную клавиатуру.

    ASCII flowchart:
    A: Инициализация InlineKeyboardBuilder
    |
    B: Перебор категорий в catalog_data
    |
    C: Добавление кнопки для каждой категории
    |
    D: Добавление кнопки "Отмена"
    |
    E: Установка порядка размещения кнопок
    |
    F: Возврат InlineKeyboardMarkup

    A --> B --> C --> D --> E --> F

    Примеры:
    >>> from typing import List
    >>> from aiogram.types import InlineKeyboardMarkup
    >>> from bot.dao.models import Category
    >>> catalog_data: List[Category] = [Category(id=1, category_name="Электроника"), Category(id=2, category_name="Одежда")]
    >>> keyboard: InlineKeyboardMarkup = catalog_admin_kb(catalog_data)
    >>> print(keyboard)
    {'inline_keyboard': [[{'text': 'Электроника', 'callback_data': 'add_category_1'}, {'text': 'Одежда', 'callback_data': 'add_category_2'}], [{'text': 'Отмена', 'callback_data': 'admin_panel'}]]}
    """
    ...
```

### `admin_send_file_kb`

```python
def admin_send_file_kb() -> InlineKeyboardMarkup:
    """Создает inline-клавиатуру для выбора отправки файла или отказа от отправки в панели администратора.

    Returns:
        InlineKeyboardMarkup: Объект `InlineKeyboardMarkup`, представляющий клавиатуру с кнопками "Без файла" и "Отмена".

    Как работает функция:
    1. Инициализирует `InlineKeyboardBuilder`.
    2. Добавляет кнопку "Без файла" с callback_data "without_file".
    3. Добавляет кнопку "Отмена" с callback_data "admin_panel".
    4. Устанавливает порядок размещения кнопок в два столбца.
    5. Возвращает созданную клавиатуру.

    ASCII flowchart:
    A: Инициализация InlineKeyboardBuilder
    |
    B: Добавление кнопки "Без файла"
    |
    C: Добавление кнопки "Отмена"
    |
    D: Установка порядка размещения кнопок
    |
    E: Возврат InlineKeyboardMarkup

    A --> B --> C --> D --> E

    Примеры:
    >>> from aiogram.types import InlineKeyboardMarkup
    >>> keyboard: InlineKeyboardMarkup = admin_send_file_kb()
    >>> print(keyboard)
    {'inline_keyboard': [[{'text': 'Без файла', 'callback_data': 'without_file'}, {'text': 'Отмена', 'callback_data': 'admin_panel'}]]}
    """
    ...
```

### `admin_kb`

```python
def admin_kb() -> InlineKeyboardMarkup:
    """Создает inline-клавиатуру для панели администратора с кнопками "Статистика", "Управлять товарами" и "На главную".

    Returns:
        InlineKeyboardMarkup: Объект `InlineKeyboardMarkup`, представляющий клавиатуру панели администратора.

    Как работает функция:
    1. Инициализирует `InlineKeyboardBuilder`.
    2. Добавляет кнопку "📊 Статистика" с callback_data "statistic".
    3. Добавляет кнопку "🛍️ Управлять товарами" с callback_data "process_products".
    4. Добавляет кнопку "🏠 На главную" с callback_data "home".
    5. Устанавливает порядок размещения кнопок в два столбца.
    6. Возвращает созданную клавиатуру.

    ASCII flowchart:
    A: Инициализация InlineKeyboardBuilder
    |
    B: Добавление кнопки "📊 Статистика"
    |
    C: Добавление кнопки "🛍️ Управлять товарами"
    |
    D: Добавление кнопки "🏠 На главную"
    |
    E: Установка порядка размещения кнопок
    |
    F: Возврат InlineKeyboardMarkup

    A --> B --> C --> D --> E --> F

    Примеры:
    >>> from aiogram.types import InlineKeyboardMarkup
    >>> keyboard: InlineKeyboardMarkup = admin_kb()
    >>> print(keyboard)
    {'inline_keyboard': [[{'text': '📊 Статистика', 'callback_data': 'statistic'}, {'text': '🛍️ Управлять товарами', 'callback_data': 'process_products'}], [{'text': '🏠 На главную', 'callback_data': 'home'}]]}
    """
    ...
```

### `admin_kb_back`

```python
def admin_kb_back() -> InlineKeyboardMarkup:
    """Создает inline-клавиатуру с кнопками "Админ панель" и "На главную" для возврата к предыдущему меню.

    Returns:
        InlineKeyboardMarkup: Объект `InlineKeyboardMarkup`, представляющий клавиатуру для возврата в панель администратора.

    Как работает функция:
    1. Инициализирует `InlineKeyboardBuilder`.
    2. Добавляет кнопку "⚙️ Админ панель" с callback_data "admin_panel".
    3. Добавляет кнопку "🏠 На главную" с callback_data "home".
    4. Устанавливает порядок размещения кнопок в один столбец.
    5. Возвращает созданную клавиатуру.

    ASCII flowchart:
    A: Инициализация InlineKeyboardBuilder
    |
    B: Добавление кнопки "⚙️ Админ панель"
    |
    C: Добавление кнопки "🏠 На главную"
    |
    D: Установка порядка размещения кнопок
    |
    E: Возврат InlineKeyboardMarkup

    A --> B --> C --> D --> E

    Примеры:
    >>> from aiogram.types import InlineKeyboardMarkup
    >>> keyboard: InlineKeyboardMarkup = admin_kb_back()
    >>> print(keyboard)
    {'inline_keyboard': [[{'text': '⚙️ Админ панель', 'callback_data': 'admin_panel'}], [{'text': '🏠 На главную', 'callback_data': 'home'}]]}
    """
    ...
```

### `dell_product_kb`

```python
def dell_product_kb(product_id: int) -> InlineKeyboardMarkup:
    """Создает inline-клавиатуру для подтверждения удаления товара с кнопками "Удалить", "Админ панель" и "На главную".

    Args:
        product_id (int): ID товара, который необходимо удалить.

    Returns:
        InlineKeyboardMarkup: Объект `InlineKeyboardMarkup`, представляющий клавиатуру подтверждения удаления товара.

    Как работает функция:
    1. Инициализирует `InlineKeyboardBuilder`.
    2. Добавляет кнопку "🗑️ Удалить" с callback_data, содержащим id товара.
    3. Добавляет кнопку "⚙️ Админ панель" с callback_data "admin_panel".
    4. Добавляет кнопку "🏠 На главную" с callback_data "home".
    5. Устанавливает порядок размещения кнопок в три ряда: 2, 2 и 1 кнопка.
    6. Возвращает созданную клавиатуру.

    ASCII flowchart:
    A: Инициализация InlineKeyboardBuilder
    |
    B: Добавление кнопки "🗑️ Удалить"
    |
    C: Добавление кнопки "⚙️ Админ панель"
    |
    D: Добавление кнопки "🏠 На главную"
    |
    E: Установка порядка размещения кнопок
    |
    F: Возврат InlineKeyboardMarkup

    A --> B --> C --> D --> E --> F

    Примеры:
    >>> from aiogram.types import InlineKeyboardMarkup
    >>> product_id: int = 123
    >>> keyboard: InlineKeyboardMarkup = dell_product_kb(product_id)
    >>> print(keyboard)
    {'inline_keyboard': [[{'text': '🗑️ Удалить', 'callback_data': 'dell_123'}], [{'text': '⚙️ Админ панель', 'callback_data': 'admin_panel'}], [{'text': '🏠 На главную', 'callback_data': 'home'}]]}
    """
    ...
```

### `product_management_kb`

```python
def product_management_kb() -> InlineKeyboardMarkup:
    """Создает inline-клавиатуру для управления товарами с кнопками "Добавить товар", "Удалить товар", "Админ панель" и "На главную".

    Returns:
        InlineKeyboardMarkup: Объект `InlineKeyboardMarkup`, представляющий клавиатуру управления товарами.

    Как работает функция:
    1. Инициализирует `InlineKeyboardBuilder`.
    2. Добавляет кнопку "➕ Добавить товар" с callback_data "add_product".
    3. Добавляет кнопку "🗑️ Удалить товар" с callback_data "delete_product".
    4. Добавляет кнопку "⚙️ Админ панель" с callback_data "admin_panel".
    5. Добавляет кнопку "🏠 На главную" с callback_data "home".
    6. Устанавливает порядок размещения кнопок в три ряда: 2, 2 и 1 кнопка.
    7. Возвращает созданную клавиатуру.

    ASCII flowchart:
    A: Инициализация InlineKeyboardBuilder
    |
    B: Добавление кнопки "➕ Добавить товар"
    |
    C: Добавление кнопки "🗑️ Удалить товар"
    |
    D: Добавление кнопки "⚙️ Админ панель"
    |
    E: Добавление кнопки "🏠 На главную"
    |
    F: Установка порядка размещения кнопок
    |
    G: Возврат InlineKeyboardMarkup

    A --> B --> C --> D --> E --> F --> G

    Примеры:
    >>> from aiogram.types import InlineKeyboardMarkup
    >>> keyboard: InlineKeyboardMarkup = product_management_kb()
    >>> print(keyboard)
    {'inline_keyboard': [[{'text': '➕ Добавить товар', 'callback_data': 'add_product'}, {'text': '🗑️ Удалить товар', 'callback_data': 'delete_product'}], [{'text': '⚙️ Админ панель', 'callback_data': 'admin_panel'}], [{'text': '🏠 На главную', 'callback_data': 'home'}]]}
    """
    ...
```

### `cancel_kb_inline`

```python
def cancel_kb_inline() -> InlineKeyboardMarkup:
    """Создает inline-клавиатуру с кнопкой "Отмена".

    Returns:
        InlineKeyboardMarkup: Объект `InlineKeyboardMarkup`, представляющий клавиатуру с кнопкой отмены.

    Как работает функция:
    1. Инициализирует `InlineKeyboardBuilder`.
    2. Добавляет кнопку "Отмена" с callback_data "cancel".
    3. Возвращает созданную клавиатуру.

    ASCII flowchart:
    A: Инициализация InlineKeyboardBuilder
    |
    B: Добавление кнопки "Отмена"
    |
    C: Возврат InlineKeyboardMarkup

    A --> B --> C

    Примеры:
    >>> from aiogram.types import InlineKeyboardMarkup
    >>> keyboard: InlineKeyboardMarkup = cancel_kb_inline()
    >>> print(keyboard)
    {'inline_keyboard': [[{'text': 'Отмена', 'callback_data': 'cancel'}]]}
    """
    ...
```

### `admin_confirm_kb`

```python
def admin_confirm_kb() -> InlineKeyboardMarkup:
    """Создает inline-клавиатуру для подтверждения действия администратором с кнопками "Все верно" и "Отмена".

    Returns:
        InlineKeyboardMarkup: Объект `InlineKeyboardMarkup`, представляющий клавиатуру подтверждения действия.

    Как работает функция:
    1. Инициализирует `InlineKeyboardBuilder`.
    2. Добавляет кнопку "Все верно" с callback_data "confirm_add".
    3. Добавляет кнопку "Отмена" с callback_data "admin_panel".
    4. Устанавливает порядок размещения кнопок в один столбец.
    5. Возвращает созданную клавиатуру.

    ASCII flowchart:
    A: Инициализация InlineKeyboardBuilder
    |
    B: Добавление кнопки "Все верно"
    |
    C: Добавление кнопки "Отмена"
    |
    D: Установка порядка размещения кнопок
    |
    E: Возврат InlineKeyboardMarkup

    A --> B --> C --> D --> E

    Примеры:
    >>> from aiogram.types import InlineKeyboardMarkup
    >>> keyboard: InlineKeyboardMarkup = admin_confirm_kb()
    >>> print(keyboard)
    {'inline_keyboard': [[{'text': 'Все верно', 'callback_data': 'confirm_add'}, {'text': 'Отмена', 'callback_data': 'admin_panel'}]]}
    """
    ...