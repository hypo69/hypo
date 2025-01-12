# Модуль `kbs.py`

## Обзор

Модуль `kbs.py` содержит функции для создания различных инлайн-клавиатур (InlineKeyboardMarkup) для административной панели Telegram-бота. Эти клавиатуры используются для навигации, управления товарами, добавления категорий и других административных действий.

## Оглавление

1. [Функции](#Функции)
    - [`catalog_admin_kb`](#catalog_admin_kb)
    - [`admin_send_file_kb`](#admin_send_file_kb)
    - [`admin_kb`](#admin_kb)
    - [`admin_kb_back`](#admin_kb_back)
    - [`dell_product_kb`](#dell_product_kb)
    - [`product_management_kb`](#product_management_kb)
    - [`cancel_kb_inline`](#cancel_kb_inline)
    - [`admin_confirm_kb`](#admin_confirm_kb)

## Функции

### `catalog_admin_kb`

**Описание**:
Создает инлайн-клавиатуру для выбора категории из списка доступных категорий для администратора.

**Параметры**:
- `catalog_data` (List[Category]): Список объектов `Category`, для которых будут созданы кнопки.

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками категорий и кнопкой "Отмена".

```python
def catalog_admin_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """
    Args:
        catalog_data (List[Category]): Список объектов `Category`, для которых будут созданы кнопки.

    Returns:
        InlineKeyboardMarkup: Инлайн-клавиатура с кнопками категорий и кнопкой "Отмена".
    """
```

### `admin_send_file_kb`

**Описание**:
Создает инлайн-клавиатуру с кнопками "Без файла" и "Отмена" для административной панели.

**Параметры**:
- Нет

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками "Без файла" и "Отмена".

```python
def admin_send_file_kb() -> InlineKeyboardMarkup:
    """
    Args:
        None

    Returns:
        InlineKeyboardMarkup: Инлайн-клавиатура с кнопками "Без файла" и "Отмена".
    """
```

### `admin_kb`

**Описание**:
Создает основную инлайн-клавиатуру для административной панели с кнопками "Статистика", "Управлять товарами" и "На главную".

**Параметры**:
- Нет

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура для административной панели.

```python
def admin_kb() -> InlineKeyboardMarkup:
    """
    Args:
        None

    Returns:
        InlineKeyboardMarkup: Инлайн-клавиатура для административной панели.
    """
```

### `admin_kb_back`

**Описание**:
Создает инлайн-клавиатуру с кнопками "Админ панель" и "На главную" для возврата к предыдущим меню.

**Параметры**:
- Нет

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура для возврата в админ-панель или на главную.

```python
def admin_kb_back() -> InlineKeyboardMarkup:
    """
    Args:
        None

    Returns:
        InlineKeyboardMarkup: Инлайн-клавиатура для возврата в админ-панель или на главную.
    """
```

### `dell_product_kb`

**Описание**:
Создает инлайн-клавиатуру для подтверждения удаления товара, содержит кнопки "Удалить", "Админ панель" и "На главную".

**Параметры**:
- `product_id` (int): ID товара для удаления.

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура для подтверждения удаления товара.

```python
def dell_product_kb(product_id: int) -> InlineKeyboardMarkup:
    """
    Args:
        product_id (int): ID товара для удаления.

    Returns:
        InlineKeyboardMarkup: Инлайн-клавиатура для подтверждения удаления товара.
    """
```

### `product_management_kb`

**Описание**:
Создает инлайн-клавиатуру для управления товарами, содержит кнопки "Добавить товар", "Удалить товар", "Админ панель" и "На главную".

**Параметры**:
- Нет

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура для управления товарами.

```python
def product_management_kb() -> InlineKeyboardMarkup:
    """
    Args:
        None

    Returns:
        InlineKeyboardMarkup: Инлайн-клавиатура для управления товарами.
    """
```

### `cancel_kb_inline`

**Описание**:
Создает инлайн-клавиатуру с кнопкой "Отмена" для отмены текущего действия.

**Параметры**:
- Нет

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопкой "Отмена".

```python
def cancel_kb_inline() -> InlineKeyboardMarkup:
    """
    Args:
        None

    Returns:
        InlineKeyboardMarkup: Инлайн-клавиатура с кнопкой "Отмена".
    """
```

### `admin_confirm_kb`

**Описание**:
Создает инлайн-клавиатуру для подтверждения добавления товара, содержит кнопки "Все верно" и "Отмена".

**Параметры**:
- Нет

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура для подтверждения добавления товара.

```python
def admin_confirm_kb() -> InlineKeyboardMarkup:
    """
    Args:
        None

    Returns:
        InlineKeyboardMarkup: Инлайн-клавиатура для подтверждения добавления товара.
    """
```