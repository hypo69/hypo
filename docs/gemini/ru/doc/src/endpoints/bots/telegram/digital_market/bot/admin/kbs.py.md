# Модуль для создания клавиатур администратора для Telegram-бота

## Обзор

Этот модуль содержит функции для создания различных встроенных клавиатур (InlineKeyboardMarkup) для административной панели Telegram-бота. Каждая функция создает клавиатуру с определенным набором кнопок, предназначенных для выполнения различных административных действий, таких как управление каталогом, отправка файлов, просмотр статистики, управление товарами и т.д.

## Подробней

Этот модуль предназначен для упрощения разработки административной панели Telegram-бота. Он предоставляет готовые функции для создания стандартных клавиатур, которые используются для навигации по панели администратора и выполнения различных действий. Использование этих функций позволяет избежать дублирования кода и упрощает поддержку и расширение функциональности бота.

## Функции

### `catalog_admin_kb`

```python
def catalog_admin_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """
    Args:
        catalog_data (List[Category]): Список объектов `Category`, для которых нужно создать кнопки.

    Returns:
        InlineKeyboardMarkup: Объект `InlineKeyboardMarkup` с кнопками для каждой категории и кнопкой "Отмена".
    """
```

**Описание**: Создает встроенную клавиатуру для администратора с кнопками для каждой категории в каталоге.

**Параметры**:
- `catalog_data` (List[Category]): Список объектов `Category`, для которых нужно создать кнопки.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками для каждой категории и кнопкой "Отмена".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from bot.dao.models import Category
from typing import List

# Пример данных о категориях
catalog_data:List[Category] = [
    Category(id=1, category_name="Электроника"),
    Category(id=2, category_name="Одежда")
]

# Создание клавиатуры
keyboard:InlineKeyboardMarkup = catalog_admin_kb(catalog_data)
```

### `admin_send_file_kb`

```python
def admin_send_file_kb() -> InlineKeyboardMarkup:
    """
    Returns:
        InlineKeyboardMarkup: Объект `InlineKeyboardMarkup` с кнопками "Без файла" и "Отмена".
    """
```

**Описание**: Создает встроенную клавиатуру с кнопками "Без файла" и "Отмена".

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками "Без файла" и "Отмена".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard:InlineKeyboardMarkup = admin_send_file_kb()
```

### `admin_kb`

```python
def admin_kb() -> InlineKeyboardMarkup:
    """
    Returns:
        InlineKeyboardMarkup: Объект `InlineKeyboardMarkup` с кнопками "📊 Статистика", "🛍️ Управлять товарами" и "🏠 На главную".
    """
```

**Описание**: Создает основную встроенную клавиатуру администратора с кнопками "📊 Статистика", "🛍️ Управлять товарами" и "🏠 На главную".

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками "📊 Статистика", "🛍️ Управлять товарами" и "🏠 На главную".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard:InlineKeyboardMarkup = admin_kb()
```

### `admin_kb_back`

```python
def admin_kb_back() -> InlineKeyboardMarkup:
    """
    Returns:
        InlineKeyboardMarkup: Объект `InlineKeyboardMarkup` с кнопками "⚙️ Админ панель" и "🏠 На главную".
    """
```

**Описание**: Создает встроенную клавиатуру с кнопками "⚙️ Админ панель" и "🏠 На главную".

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками "⚙️ Админ панель" и "🏠 На главную".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard:InlineKeyboardMarkup = admin_kb_back()
```

### `dell_product_kb`

```python
def dell_product_kb(product_id: int) -> InlineKeyboardMarkup:
    """
    Args:
        product_id (int): ID продукта, который нужно удалить.

    Returns:
        InlineKeyboardMarkup: Объект `InlineKeyboardMarkup` с кнопками "🗑️ Удалить", "⚙️ Админ панель" и "🏠 На главную".
    """
```

**Описание**: Создает встроенную клавиатуру для подтверждения удаления продукта с кнопками "🗑️ Удалить", "⚙️ Админ панель" и "🏠 На главную".

**Параметры**:
- `product_id` (int): ID продукта, который нужно удалить.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками "🗑️ Удалить", "⚙️ Админ панель" и "🏠 На главную".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard:InlineKeyboardMarkup = dell_product_kb(product_id=123)
```

### `product_management_kb`

```python
def product_management_kb() -> InlineKeyboardMarkup:
    """
    Returns:
        InlineKeyboardMarkup: Объект `InlineKeyboardMarkup` с кнопками "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель" и "🏠 На главную".
    """
```

**Описание**: Создает встроенную клавиатуру для управления товарами с кнопками "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель" и "🏠 На главную".

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель" и "🏠 На главную".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard:InlineKeyboardMarkup = product_management_kb()
```

### `cancel_kb_inline`

```python
def cancel_kb_inline() -> InlineKeyboardMarkup:
    """
    Returns:
        InlineKeyboardMarkup: Объект `InlineKeyboardMarkup` с кнопкой "Отмена".
    """
```

**Описание**: Создает встроенную клавиатуру с кнопкой "Отмена".

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопкой "Отмена".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard:InlineKeyboardMarkup = cancel_kb_inline()
```

### `admin_confirm_kb`

```python
def admin_confirm_kb() -> InlineKeyboardMarkup:
    """
    Returns:
        InlineKeyboardMarkup: Объект `InlineKeyboardMarkup` с кнопками "Все верно" и "Отмена".
    """
```

**Описание**: Создает встроенную клавиатуру для подтверждения действия администратора с кнопками "Все верно" и "Отмена".

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками "Все верно" и "Отмена".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard:InlineKeyboardMarkup = admin_confirm_kb()