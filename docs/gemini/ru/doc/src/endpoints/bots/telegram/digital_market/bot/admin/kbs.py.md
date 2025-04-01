# Модуль для создания клавиатур администратора Telegram-бота
## Обзор

Модуль `kbs.py` предназначен для формирования различных инлайн-клавиатур (InlineKeyboardMarkup) для административной панели Telegram-бота. Эти клавиатуры используются для управления каталогом, товарами, просмотра статистики и выполнения других административных действий. Все функции в модуле создают клавиатуры на основе библиотеки `aiogram`.

## Подробней
Модуль предоставляет набор функций для создания инлайн-клавиатур, которые позволяют администраторам взаимодействовать с ботом через удобные интерфейсы. Каждая функция отвечает за создание определенного типа клавиатуры с соответствующим набором кнопок и callback-data. Callback-data используются для обработки нажатий на кнопки и выполнения связанных с ними действий.

## Функции

### `catalog_admin_kb`

```python
def catalog_admin_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру для администратора с категориями каталога.

    Args:
        catalog_data (List[Category]): Список объектов Category, содержащих информацию о категориях.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры с кнопками категорий и кнопкой "Отмена".
    
    Пример:
        >>> from bot.dao.models import Category
        >>> catalog_data = [Category(id=1, category_name="Электроника"), Category(id=2, category_name="Одежда")]
        >>> keyboard = catalog_admin_kb(catalog_data)
    """
    ...
```

**Назначение**:
Функция `catalog_admin_kb` создает инлайн-клавиатуру для отображения категорий каталога в административной панели. Она принимает список объектов `Category` и создает кнопки для каждой категории, позволяя администратору выбирать категории для дальнейших действий (например, добавления товаров в категорию).

**Параметры**:
- `catalog_data` (List[Category]): Список объектов `Category`, где каждый объект содержит информацию об идентификаторе и имени категории.

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками для каждой категории и кнопкой "Отмена".

**Как работает функция**:

1.  Инициализирует объект `InlineKeyboardBuilder`.
2.  Для каждой категории в `catalog_data` создает кнопку с именем категории и callback-data, содержащим идентификатор категории.
3.  Добавляет кнопку "Отмена" с callback-data "admin_panel".
4.  Настраивает размещение кнопок в два столбца.
5.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**ASCII Flowchart**:

```
A[Получение списка категорий catalog_data]
|
B[Создание InlineKeyboardBuilder]
|
C[Для каждой категории создание кнопки с именем и id]
|
D[Добавление кнопки "Отмена"]
|
E[Настройка размещения кнопок в 2 столбца]
|
F[Преобразование в InlineKeyboardMarkup]
|
G[Возврат InlineKeyboardMarkup]
```

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from bot.dao.models import Category

# Пример данных о категориях
catalog_data = [
    Category(id=1, category_name="Электроника"),
    Category(id=2, category_name="Одежда")
]

# Создание клавиатуры
keyboard = catalog_admin_kb(catalog_data)
assert isinstance(keyboard, InlineKeyboardMarkup)

```

### `admin_send_file_kb`

```python
def admin_send_file_kb() -> InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру для администратора с вариантами отправки файла.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры с кнопками "Без файла" и "Отмена".
    
        Пример:
            >>> keyboard = admin_send_file_kb()
    """
    ...
```

**Назначение**:
Функция `admin_send_file_kb` создает инлайн-клавиатуру для администратора с кнопками "Без файла" и "Отмена". Это позволяет администратору выбирать, отправлять ли файл при выполнении определенных действий (например, при добавлении товара).

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками "Без файла" и "Отмена".

**Как работает функция**:

1.  Инициализирует объект `InlineKeyboardBuilder`.
2.  Создает кнопку "Без файла" с callback-data "without_file".
3.  Создает кнопку "Отмена" с callback-data "admin_panel".
4.  Настраивает размещение кнопок в два столбца.
5.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**ASCII Flowchart**:

```
A[Создание InlineKeyboardBuilder]
|
B[Создание кнопки "Без файла"]
|
C[Создание кнопки "Отмена"]
|
D[Настройка размещения кнопок в 2 столбца]
|
E[Преобразование в InlineKeyboardMarkup]
|
F[Возврат InlineKeyboardMarkup]
```

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard = admin_send_file_kb()
assert isinstance(keyboard, InlineKeyboardMarkup)
```

### `admin_kb`

```python
def admin_kb() -> InlineKeyboardMarkup:
    """
    Создает основную инлайн-клавиатуру административной панели.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры с кнопками "📊 Статистика", "🛍️ Управлять товарами" и "🏠 На главную".
        
        Пример:
            >>> keyboard = admin_kb()
    """
    ...
```

**Назначение**:
Функция `admin_kb` создает основную инлайн-клавиатуру для административной панели. Она включает кнопки для просмотра статистики, управления товарами и возврата на главную страницу.

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками "📊 Статистика", "🛍️ Управлять товарами" и "🏠 На главную".

**Как работает функция**:

1.  Инициализирует объект `InlineKeyboardBuilder`.
2.  Создает кнопку "📊 Статистика" с callback-data "statistic".
3.  Создает кнопку "🛍️ Управлять товарами" с callback-data "process_products".
4.  Создает кнопку "🏠 На главную" с callback-data "home".
5.  Настраивает размещение кнопок в два столбца.
6.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**ASCII Flowchart**:

```
A[Создание InlineKeyboardBuilder]
|
B[Создание кнопки "📊 Статистика"]
|
C[Создание кнопки "🛍️ Управлять товарами"]
|
D[Создание кнопки "🏠 На главную"]
|
E[Настройка размещения кнопок в 2 столбца]
|
F[Преобразование в InlineKeyboardMarkup]
|
G[Возврат InlineKeyboardMarkup]
```

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard = admin_kb()
assert isinstance(keyboard, InlineKeyboardMarkup)
```

### `admin_kb_back`

```python
def admin_kb_back() -> InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру с кнопками возврата в админ-панель и на главную.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры с кнопками "⚙️ Админ панель" и "🏠 На главную".
        
        Пример:
            >>> keyboard = admin_kb_back()
    """
    ...
```

**Назначение**:
Функция `admin_kb_back` создает инлайн-клавиатуру с кнопками для возврата в административную панель и на главную страницу.

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками "⚙️ Админ панель" и "🏠 На главную".

**Как работает функция**:

1.  Инициализирует объект `InlineKeyboardBuilder`.
2.  Создает кнопку "⚙️ Админ панель" с callback-data "admin_panel".
3.  Создает кнопку "🏠 На главную" с callback-data "home".
4.  Настраивает размещение кнопок в один столбец.
5.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**ASCII Flowchart**:

```
A[Создание InlineKeyboardBuilder]
|
B[Создание кнопки "⚙️ Админ панель"]
|
C[Создание кнопки "🏠 На главную"]
|
D[Настройка размещения кнопок в 1 столбец]
|
E[Преобразование в InlineKeyboardMarkup]
|
F[Возврат InlineKeyboardMarkup]
```

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard = admin_kb_back()
assert isinstance(keyboard, InlineKeyboardMarkup)
```

### `dell_product_kb`

```python
def dell_product_kb(product_id: int) -> InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру для подтверждения удаления товара.

    Args:
        product_id (int): Идентификатор товара, который нужно удалить.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры с кнопками "🗑️ Удалить", "⚙️ Админ панель" и "🏠 На главную".
        
        Пример:
            >>> keyboard = dell_product_kb(123)
    """
    ...
```

**Назначение**:
Функция `dell_product_kb` создает инлайн-клавиатуру для подтверждения удаления товара. Она включает кнопку для удаления товара и кнопки для возврата в административную панель или на главную страницу.

**Параметры**:
- `product_id` (int): Идентификатор товара, который нужно удалить.

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками "🗑️ Удалить", "⚙️ Админ панель" и "🏠 На главную".

**Как работает функция**:

1.  Инициализирует объект `InlineKeyboardBuilder`.
2.  Создает кнопку "🗑️ Удалить" с callback-data, содержащим идентификатор товара.
3.  Создает кнопку "⚙️ Админ панель" с callback-data "admin_panel".
4.  Создает кнопку "🏠 На главную" с callback-data "home".
5.  Настраивает размещение кнопок в три ряда: 2, 2 и 1 кнопка.
6.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**ASCII Flowchart**:

```
A[Получение ID продукта product_id]
|
B[Создание InlineKeyboardBuilder]
|
C[Создание кнопки "🗑️ Удалить" с ID продукта]
|
D[Создание кнопки "⚙️ Админ панель"]
|
E[Создание кнопки "🏠 На главную"]
|
F[Настройка размещения кнопок]
|
G[Преобразование в InlineKeyboardMarkup]
|
H[Возврат InlineKeyboardMarkup]
```

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры для удаления товара с ID 123
keyboard = dell_product_kb(123)
assert isinstance(keyboard, InlineKeyboardMarkup)
```

### `product_management_kb`

```python
def product_management_kb() -> InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру для управления товарами.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры с кнопками "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель" и "🏠 На главную".
        
        Пример:
            >>> keyboard = product_management_kb()
    """
    ...
```

**Назначение**:
Функция `product_management_kb` создает инлайн-клавиатуру для управления товарами. Она включает кнопки для добавления, удаления товаров, возврата в административную панель и на главную страницу.

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель" и "🏠 На главную".

**Как работает функция**:

1.  Инициализирует объект `InlineKeyboardBuilder`.
2.  Создает кнопку "➕ Добавить товар" с callback-data "add_product".
3.  Создает кнопку "🗑️ Удалить товар" с callback-data "delete_product".
4.  Создает кнопку "⚙️ Админ панель" с callback-data "admin_panel".
5.  Создает кнопку "🏠 На главную" с callback-data "home".
6.  Настраивает размещение кнопок в три ряда: 2, 2 и 1 кнопка.
7.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**ASCII Flowchart**:

```
A[Создание InlineKeyboardBuilder]
|
B[Создание кнопки "➕ Добавить товар"]
|
C[Создание кнопки "🗑️ Удалить товар"]
|
D[Создание кнопки "⚙️ Админ панель"]
|
E[Создание кнопки "🏠 На главную"]
|
F[Настройка размещения кнопок]
|
G[Преобразование в InlineKeyboardMarkup]
|
H[Возврат InlineKeyboardMarkup]
```

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры для управления товарами
keyboard = product_management_kb()
assert isinstance(keyboard, InlineKeyboardMarkup)
```

### `cancel_kb_inline`

```python
def cancel_kb_inline() -> InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру с кнопкой "Отмена".

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры с кнопкой "Отмена".
        
        Пример:
            >>> keyboard = cancel_kb_inline()
    """
    ...
```

**Назначение**:
Функция `cancel_kb_inline` создает инлайн-клавиатуру с кнопкой "Отмена". Эта клавиатура используется для отмены текущего действия.

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопкой "Отмена".

**Как работает функция**:

1.  Инициализирует объект `InlineKeyboardBuilder`.
2.  Создает кнопку "Отмена" с callback-data "cancel".
3.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**ASCII Flowchart**:

```
A[Создание InlineKeyboardBuilder]
|
B[Создание кнопки "Отмена"]
|
C[Преобразование в InlineKeyboardMarkup]
|
D[Возврат InlineKeyboardMarkup]
```

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры с кнопкой "Отмена"
keyboard = cancel_kb_inline()
assert isinstance(keyboard, InlineKeyboardMarkup)
```

### `admin_confirm_kb`

```python
def admin_confirm_kb() -> InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру для подтверждения действий администратором.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры с кнопками "Все верно" и "Отмена".

        Пример:
            >>> keyboard = admin_confirm_kb()
    """
    ...
```

**Назначение**:
Функция `admin_confirm_kb` создает инлайн-клавиатуру для подтверждения действий администратором. Она включает кнопки "Все верно" и "Отмена".

**Возвращает**:
- `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками "Все верно" и "Отмена".

**Как работает функция**:

1.  Инициализирует объект `InlineKeyboardBuilder`.
2.  Создает кнопку "Все верно" с callback-data "confirm_add".
3.  Создает кнопку "Отмена" с callback-data "admin_panel".
4.  Настраивает размещение кнопок в один столбец.
5.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**ASCII Flowchart**:

```
A[Создание InlineKeyboardBuilder]
|
B[Создание кнопки "Все верно"]
|
C[Создание кнопки "Отмена"]
|
D[Настройка размещения кнопок в 1 столбец]
|
E[Преобразование в InlineKeyboardMarkup]
|
F[Возврат InlineKeyboardMarkup]
```

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры подтверждения
keyboard = admin_confirm_kb()
assert isinstance(keyboard, InlineKeyboardMarkup)