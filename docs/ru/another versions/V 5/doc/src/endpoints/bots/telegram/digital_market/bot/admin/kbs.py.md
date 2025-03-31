# Модуль для создания административных клавиатур для Telegram-бота

## Обзор

Этот модуль содержит функции для создания различных встроенных клавиатур (InlineKeyboardMarkup), используемых в Telegram-боте для административных целей. Клавиатуры используются для навигации по каталогу, управления товарами, просмотра статистики и других административных действий.

## Подробней

Модуль предоставляет набор функций, каждая из которых создает определенную клавиатуру с заданным набором кнопок и callback-data. Callback-data используются для обработки нажатий на кнопки и выполнения соответствующих действий. Модуль использует `InlineKeyboardBuilder` из библиотеки `aiogram` для удобного создания клавиатур.
Рассмотрим подробнее каждую функцию.

## Функции

### `catalog_admin_kb`

```python
def catalog_admin_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для администратора с категориями каталога.

    Args:
        catalog_data (List[Category]): Список объектов Category, представляющих категории каталога.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками категорий и кнопкой "Отмена".
    """
```

**Как работает функция**:
Функция `catalog_admin_kb` принимает список объектов `Category` и создает клавиатуру с кнопками, представляющими каждую категорию. Callback-data для каждой кнопки формируется как `"add_category_{category.id}"`, где `category.id` - идентификатор категории. Также добавляется кнопка "Отмена" с callback-data `"admin_panel"`. Кнопки располагаются в два столбца.

**Параметры**:
- `catalog_data` (List[Category]): Список объектов `Category`, для которых нужно создать кнопки.

**Возвращает**:
- `InlineKeyboardMarkup`: Клавиатура с кнопками категорий и кнопкой "Отмена".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from bot.dao.models import Category
# Пример использования функции
catalog_data = [Category(id=1, category_name="Электроника"), Category(id=2, category_name="Одежда")]
keyboard = catalog_admin_kb(catalog_data)
# Далее можно отправить эту клавиатуру пользователю через Telegram API
```

### `admin_send_file_kb`

```python
def admin_send_file_kb() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для администратора с кнопками "Без файла" и "Отмена".

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками "Без файла" и "Отмена".
    """
```

**Как работает функция**:

Функция `admin_send_file_kb` создает клавиатуру с двумя кнопками: "Без файла" и "Отмена". Callback-data для кнопки "Без файла" - `"without_file"`, а для кнопки "Отмена" - `"admin_panel"`. Кнопки располагаются в два столбца.

**Возвращает**:
- `InlineKeyboardMarkup`: Клавиатура с кнопками "Без файла" и "Отмена".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Пример использования функции
keyboard = admin_send_file_kb()
# Далее можно отправить эту клавиатуру пользователю через Telegram API
```

### `admin_kb`

```python
def admin_kb() -> InlineKeyboardMarkup:
    """
    Создает главную клавиатуру для администратора с кнопками "📊 Статистика", "🛍️ Управлять товарами" и "🏠 На главную".

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками "📊 Статистика", "🛍️ Управлять товарами" и "🏠 На главную".
    """
```

**Как работает функция**:

Функция `admin_kb` создает главную клавиатуру для администратора с кнопками: "📊 Статистика", "🛍️ Управлять товарами" и "🏠 На главную". Callback-data для каждой кнопки: `"statistic"`, `"process_products"` и `"home"` соответственно. Кнопки располагаются в два столбца.

**Возвращает**:
- `InlineKeyboardMarkup`: Главная клавиатура для администратора.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Пример использования функции
keyboard = admin_kb()
# Далее можно отправить эту клавиатуру пользователю через Telegram API
```

### `admin_kb_back`

```python
def admin_kb_back() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для возврата в админ-панель и на главную страницу.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками "⚙️ Админ панель" и "🏠 На главную".
    """
```

**Как работает функция**:

Функция `admin_kb_back` создает клавиатуру с двумя кнопками: "⚙️ Админ панель" и "🏠 На главную". Callback-data для каждой кнопки: `"admin_panel"` и `"home"` соответственно. Кнопки располагаются в один столбец.

**Возвращает**:
- `InlineKeyboardMarkup`: Клавиатура для возврата в админ-панель и на главную страницу.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Пример использования функции
keyboard = admin_kb_back()
# Далее можно отправить эту клавиатуру пользователю через Telegram API
```

### `dell_product_kb`

```python
def dell_product_kb(product_id: int) -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для удаления товара с кнопками "🗑️ Удалить", "⚙️ Админ панель" и "🏠 На главную".

    Args:
        product_id (int): Идентификатор товара, который нужно удалить.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками "🗑️ Удалить", "⚙️ Админ панель" и "🏠 На главную".
    """
```

**Как работает функция**:

Функция `dell_product_kb` создает клавиатуру для удаления товара. Она принимает `product_id` и создает кнопку "🗑️ Удалить" с callback-data `"dell_{product_id}"`. Также добавляются кнопки "⚙️ Админ панель" и "🏠 На главную" с соответствующими callback-data. Кнопки располагаются в три ряда: 2, 2 и 1 кнопка.

**Параметры**:
- `product_id` (int): Идентификатор товара, который нужно удалить.

**Возвращает**:
- `InlineKeyboardMarkup`: Клавиатура для удаления товара.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Пример использования функции
product_id = 123
keyboard = dell_product_kb(product_id)
# Далее можно отправить эту клавиатуру пользователю через Telegram API
```

### `product_management_kb`

```python
def product_management_kb() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для управления товарами с кнопками "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель" и "🏠 На главную".

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель" и "🏠 На главную".
    """
```

**Как работает функция**:

Функция `product_management_kb` создает клавиатуру для управления товарами с кнопками: "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель" и "🏠 На главную". Callback-data для каждой кнопки: `"add_product"`, `"delete_product"`, `"admin_panel"` и `"home"` соответственно. Кнопки располагаются в три ряда: 2, 2 и 1 кнопка.

**Возвращает**:
- `InlineKeyboardMarkup`: Клавиатура для управления товарами.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Пример использования функции
keyboard = product_management_kb()
# Далее можно отправить эту клавиатуру пользователю через Telegram API
```

### `cancel_kb_inline`

```python
def cancel_kb_inline() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру с кнопкой "Отмена".

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопкой "Отмена".
    """
```

**Как работает функция**:

Функция `cancel_kb_inline` создает простую клавиатуру с одной кнопкой "Отмена" и callback-data `"cancel"`.

**Возвращает**:
- `InlineKeyboardMarkup`: Клавиатура с кнопкой "Отмена".

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Пример использования функции
keyboard = cancel_kb_inline()
# Далее можно отправить эту клавиатуру пользователю через Telegram API
```

### `admin_confirm_kb`

```python
def admin_confirm_kb() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для подтверждения действия администратором с кнопками "Все верно" и "Отмена".

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками "Все верно" и "Отмена".
    """
```

**Как работает функция**:

Функция `admin_confirm_kb` создает клавиатуру с двумя кнопками: "Все верно" и "Отмена". Callback-data для кнопки "Все верно" - `"confirm_add"`, а для кнопки "Отмена" - `"admin_panel"`. Кнопки располагаются в один столбец.

**Возвращает**:
- `InlineKeyboardMarkup`: Клавиатура для подтверждения действия администратором.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Пример использования функции
keyboard = admin_confirm_kb()
# Далее можно отправить эту клавиатуру пользователю через Telegram API
```