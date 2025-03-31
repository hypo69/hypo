# Модуль для создания административных клавиатур для Telegram бота

## Обзор

Модуль содержит функции для создания различных встроенных клавиатур (InlineKeyboardMarkup) для административной панели Telegram-бота. Клавиатуры используются для управления каталогом, товарами, просмотра статистики и выполнения других административных действий.

## Подробнее

Этот модуль предоставляет набор функций для создания интерактивных клавиатур, которые отображаются непосредственно в сообщениях Telegram. Каждая функция создает определенный тип клавиатуры с кнопками, связанными с callback-data, что позволяет боту реагировать на нажатия кнопок.

## Функции

### `catalog_admin_kb`

```python
def catalog_admin_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """Создает встроенную клавиатуру для администратора для управления каталогом.

    Args:
        catalog_data (List[Category]): Список объектов Category, для которых создаются кнопки.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками категорий и кнопкой "Отмена".

    Как работает функция:
    1. Инициализируется построитель клавиатуры `InlineKeyboardBuilder`.
    2. Для каждой категории в `catalog_data` создается кнопка с названием категории и callback_data, содержащим ID категории.
    3. Добавляется кнопка "Отмена" с callback_data "admin_panel".
    4. Кнопки размещаются в два столбца.
    5. Возвращается созданная клавиатура в виде объекта `InlineKeyboardMarkup`.
    """
    ...
```
**Параметры:**
- `catalog_data` (List[Category]): Список объектов Category, для каждой из которых будет создана кнопка в клавиатуре.

**Возвращает:**
- `InlineKeyboardMarkup`: Сгенерированная клавиатура для управления каталогом.

### `admin_send_file_kb`

```python
def admin_send_file_kb() -> InlineKeyboardMarkup:
    """Создает встроенную клавиатуру для администратора для отправки файла.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками "Без файла" и "Отмена".

    Как работает функция:
    1. Инициализируется построитель клавиатуры `InlineKeyboardBuilder`.
    2. Создается кнопка "Без файла" с callback_data "without_file".
    3. Создается кнопка "Отмена" с callback_data "admin_panel".
    4. Кнопки размещаются в два столбца.
    5. Возвращается созданная клавиатура в виде объекта `InlineKeyboardMarkup`.
    """
    ...
```

**Возвращает:**
- `InlineKeyboardMarkup`: Сгенерированная клавиатура для выбора отправки файла или отмены.

### `admin_kb`

```python
def admin_kb() -> InlineKeyboardMarkup:
    """Создает основную встроенную клавиатуру для административной панели.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками "📊 Статистика", "🛍️ Управлять товарами" и "🏠 На главную".

    Как работает функция:
    1. Инициализируется построитель клавиатуры `InlineKeyboardBuilder`.
    2. Создается кнопка "📊 Статистика" с callback_data "statistic".
    3. Создается кнопка "🛍️ Управлять товарами" с callback_data "process_products".
    4. Создается кнопка "🏠 На главную" с callback_data "home".
    5. Кнопки размещаются в два столбца.
    6. Возвращается созданная клавиатура в виде объекта `InlineKeyboardMarkup`.
    """
    ...
```

**Возвращает:**
- `InlineKeyboardMarkup`: Основная клавиатура административной панели.

### `admin_kb_back`

```python
def admin_kb_back() -> InlineKeyboardMarkup:
    """Создает встроенную клавиатуру с кнопками возврата в админ-панель и на главную.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками "⚙️ Админ панель" и "🏠 На главную".

    Как работает функция:
    1. Инициализируется построитель клавиатуры `InlineKeyboardBuilder`.
    2. Создается кнопка "⚙️ Админ панель" с callback_data "admin_panel".
    3. Создается кнопка "🏠 На главную" с callback_data "home".
    4. Кнопки размещаются в один столбец.
    5. Возвращается созданная клавиатура в виде объекта `InlineKeyboardMarkup`.
    """
    ...
```

**Возвращает:**
- `InlineKeyboardMarkup`: Клавиатура с кнопками возврата.

### `dell_product_kb`

```python
def dell_product_kb(product_id: int) -> InlineKeyboardMarkup:
    """Создает встроенную клавиатуру для подтверждения удаления товара.

    Args:
        product_id (int): ID товара, который нужно удалить.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками "🗑️ Удалить", "⚙️ Админ панель" и "🏠 На главную".

    Как работает функция:
    1. Инициализируется построитель клавиатуры `InlineKeyboardBuilder`.
    2. Создается кнопка "🗑️ Удалить" с callback_data, содержащим ID товара для удаления.
    3. Создается кнопка "⚙️ Админ панель" с callback_data "admin_panel".
    4. Создается кнопка "🏠 На главную" с callback_data "home".
    5. Кнопки размещаются в три ряда: 2, 2 и 1 кнопка.
    6. Возвращается созданная клавиатура в виде объекта `InlineKeyboardMarkup`.
    """
    ...
```

**Параметры:**
- `product_id` (int): Идентификатор товара, который необходимо удалить.

**Возвращает:**
- `InlineKeyboardMarkup`: Клавиатура для подтверждения удаления товара.

### `product_management_kb`

```python
def product_management_kb() -> InlineKeyboardMarkup:
    """Создает встроенную клавиатуру для управления товарами.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель" и "🏠 На главную".

    Как работает функция:
    1. Инициализируется построитель клавиатуры `InlineKeyboardBuilder`.
    2. Создается кнопка "➕ Добавить товар" с callback_data "add_product".
    3. Создается кнопка "🗑️ Удалить товар" с callback_data "delete_product".
    4. Создается кнопка "⚙️ Админ панель" с callback_data "admin_panel".
    5. Создается кнопка "🏠 На главную" с callback_data "home".
    6. Кнопки размещаются в три ряда: 2, 2 и 1 кнопка.
    7. Возвращается созданная клавиатура в виде объекта `InlineKeyboardMarkup`.
    """
    ...
```

**Возвращает:**
- `InlineKeyboardMarkup`: Клавиатура для управления товарами.

### `cancel_kb_inline`

```python
def cancel_kb_inline() -> InlineKeyboardMarkup:
    """Создает встроенную клавиатуру с кнопкой отмены.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопкой "Отмена".

    Как работает функция:
    1. Инициализируется построитель клавиатуры `InlineKeyboardBuilder`.
    2. Создается кнопка "Отмена" с callback_data "cancel".
    3. Возвращается созданная клавиатура в виде объекта `InlineKeyboardMarkup`.
    """
    ...
```

**Возвращает:**
- `InlineKeyboardMarkup`: Клавиатура с кнопкой отмены.

### `admin_confirm_kb`

```python
def admin_confirm_kb() -> InlineKeyboardMarkup:
    """Создает встроенную клавиатуру для подтверждения действия администратором.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками "Все верно" и "Отмена".

    Как работает функция:
    1. Инициализируется построитель клавиатуры `InlineKeyboardBuilder`.
    2. Создается кнопка "Все верно" с callback_data "confirm_add".
    3. Создается кнопка "Отмена" с callback_data "admin_panel".
    4. Кнопки размещаются в один столбец.
    5. Возвращается созданная клавиатура в виде объекта `InlineKeyboardMarkup`.
    """
    ...
```

**Возвращает:**
- `InlineKeyboardMarkup`: Клавиатура для подтверждения действия.