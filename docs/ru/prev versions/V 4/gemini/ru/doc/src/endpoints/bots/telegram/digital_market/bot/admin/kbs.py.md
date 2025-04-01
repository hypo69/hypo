# Модуль для создания клавиатур администратора для Telegram бота

## Обзор

Модуль `kbs.py` предназначен для создания различных встроенных клавиатур (InlineKeyboardMarkup) для административной панели Telegram-бота.
Он предоставляет функции для создания клавиатур для управления каталогом, отправки файлов, общей админ-панели, управления продуктами и подтверждения действий.
Использует библиотеку `aiogram` для создания клавиатур.

## Подробней

Этот модуль содержит функции, которые генерируют объекты `InlineKeyboardMarkup`, используемые для различных действий в административной панели Telegram-бота. Каждая функция создает свой набор кнопок с соответствующими callback_data, что позволяет боту обрабатывать действия пользователя при нажатии на кнопку.

## Функции

### `catalog_admin_kb`

```python
def catalog_admin_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """
    Args:
        catalog_data (List[Category]): Список объектов категорий для отображения в клавиатуре.

    Returns:
        InlineKeyboardMarkup: Объект встроенной клавиатуры с кнопками категорий и кнопкой "Отмена".
    """
```

**Описание**: Создает встроенную клавиатуру для администратора с кнопками, представляющими категории товаров. Каждая кнопка имеет callback_data, содержащий ID категории.

**Параметры**:
- `catalog_data` (List[Category]): Список объектов `Category`, для которых нужно создать кнопки.

**Возвращает**:
- `InlineKeyboardMarkup`: Клавиатура с кнопками категорий и кнопкой "Отмена".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from bot.dao.models import Category
from typing import List
# Пример использования функции catalog_admin_kb
catalog_data: List[Category] = [
    Category(id=1, category_name="Электроника"),
    Category(id=2, category_name="Одежда")
]
keyboard: InlineKeyboardMarkup = catalog_admin_kb(catalog_data)
```

### `admin_send_file_kb`

```python
def admin_send_file_kb() -> InlineKeyboardMarkup:
    """
    Returns:
        InlineKeyboardMarkup: Объект встроенной клавиатуры с кнопками "Без файла" и "Отмена".
    """
```

**Описание**: Создает встроенную клавиатуру для администратора с кнопками "Без файла" и "Отмена".

**Возвращает**:
- `InlineKeyboardMarkup`: Клавиатура с кнопками "Без файла" и "Отмена".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Пример использования функции admin_send_file_kb
keyboard: InlineKeyboardMarkup = admin_send_file_kb()
```

### `admin_kb`

```python
def admin_kb() -> InlineKeyboardMarkup:
    """
    Returns:
        InlineKeyboardMarkup: Объект встроенной клавиатуры с кнопками "📊 Статистика", "🛍️ Управлять товарами" и "🏠 На главную".
    """
```

**Описание**: Создает основную встроенную клавиатуру администратора с кнопками "📊 Статистика", "🛍️ Управлять товарами" и "🏠 На главную".

**Возвращает**:
- `InlineKeyboardMarkup`: Клавиатура с кнопками "📊 Статистика", "🛍️ Управлять товарами" и "🏠 На главную".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Пример использования функции admin_kb
keyboard: InlineKeyboardMarkup = admin_kb()
```

### `admin_kb_back`

```python
def admin_kb_back() -> InlineKeyboardMarkup:
    """
    Returns:
        InlineKeyboardMarkup: Объект встроенной клавиатуры с кнопками "⚙️ Админ панель" и "🏠 На главную".
    """
```

**Описание**: Создает встроенную клавиатуру с кнопками "⚙️ Админ панель" и "🏠 На главную" для возврата в предыдущее меню.

**Возвращает**:
- `InlineKeyboardMarkup`: Клавиатура с кнопками "⚙️ Админ панель" и "🏠 На главную".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Пример использования функции admin_kb_back
keyboard: InlineKeyboardMarkup = admin_kb_back()
```

### `dell_product_kb`

```python
def dell_product_kb(product_id: int) -> InlineKeyboardMarkup:
    """
    Args:
        product_id (int): ID продукта, который нужно удалить.

    Returns:
        InlineKeyboardMarkup: Объект встроенной клавиатуры с кнопками "🗑️ Удалить", "⚙️ Админ панель" и "🏠 На главную".
    """
```

**Описание**: Создает встроенную клавиатуру для подтверждения удаления товара с кнопками "🗑️ Удалить", "⚙️ Админ панель" и "🏠 На главную".

**Параметры**:
- `product_id` (int): ID продукта, который нужно удалить.

**Возвращает**:
- `InlineKeyboardMarkup`: Клавиатура с кнопками "🗑️ Удалить", "⚙️ Админ панель" и "🏠 На главную".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Пример использования функции dell_product_kb
product_id: int = 123
keyboard: InlineKeyboardMarkup = dell_product_kb(product_id)
```

### `product_management_kb`

```python
def product_management_kb() -> InlineKeyboardMarkup:
    """
    Returns:
        InlineKeyboardMarkup: Объект встроенной клавиатуры с кнопками "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель" и "🏠 На главную".
    """
```

**Описание**: Создает встроенную клавиатуру для управления товарами с кнопками "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель" и "🏠 На главную".

**Возвращает**:
- `InlineKeyboardMarkup`: Клавиатура с кнопками "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель" и "🏠 На главную".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Пример использования функции product_management_kb
keyboard: InlineKeyboardMarkup = product_management_kb()
```

### `cancel_kb_inline`

```python
def cancel_kb_inline() -> InlineKeyboardMarkup:
    """
    Returns:
        InlineKeyboardMarkup: Объект встроенной клавиатуры с кнопкой "Отмена".
    """
```

**Описание**: Создает встроенную клавиатуру с кнопкой "Отмена".

**Возвращает**:
- `InlineKeyboardMarkup`: Клавиатура с кнопкой "Отмена".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Пример использования функции cancel_kb_inline
keyboard: InlineKeyboardMarkup = cancel_kb_inline()
```

### `admin_confirm_kb`

```python
def admin_confirm_kb() -> InlineKeyboardMarkup:
    """
    Returns:
        InlineKeyboardMarkup: Объект встроенной клавиатуры с кнопками "Все верно" и "Отмена".
    """
```

**Описание**: Создает встроенную клавиатуру для подтверждения действия администратором с кнопками "Все верно" и "Отмена".

**Возвращает**:
- `InlineKeyboardMarkup`: Клавиатура с кнопками "Все верно" и "Отмена".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Пример использования функции admin_confirm_kb
keyboard: InlineKeyboardMarkup = admin_confirm_kb()