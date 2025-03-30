# Модуль администрирования бота (admin.py)

## Обзор

Модуль `admin.py` предназначен для реализации функциональности административной панели Telegram-бота. Он содержит обработчики для различных административных действий, таких как просмотр статистики, управление товарами (добавление, удаление) и другие операции, доступные только администраторам бота.

## Подробней

Этот модуль обеспечивает интерфейс для администраторов бота, позволяя им управлять контентом и функциональностью бота через Telegram. Он включает в себя обработку колбэков и текстовых сообщений, связанных с административными командами, а также использует FSM (машину состояний) для управления сложными процессами, такими как добавление нового товара. Расположение файла в структуре проекта указывает на то, что это один из основных компонентов, отвечающих за административные функции.

## Классы

### `AddProduct`

**Описание**:
Класс `AddProduct` представляет собой группу состояний (StatesGroup), используемую для управления процессом добавления нового товара в базу данных. Каждое состояние соответствует определенному шагу в процессе добавления товара, такому как ввод имени, описания, цены и т.д.

**Атрибуты**:
- `name` (State): Состояние для ввода имени товара.
- `description` (State): Состояние для ввода описания товара.
- `price` (State): Состояние для ввода цены товара.
- `file_id` (State): Состояние для выбора или загрузки файла товара.
- `category_id` (State): Состояние для выбора категории товара.
- `hidden_content` (State): Состояние для ввода скрытого контента товара.
- `confirm_add` (State): Состояние для подтверждения добавления товара.

**Примеры**:

```python
class AddProduct(StatesGroup):
    name = State()
    description = State()
    price = State()
    file_id = State()
    category_id = State()
    hidden_content = State()
    confirm_add = State()
```

## Функции

### `start_admin`

```python
async def start_admin(call: CallbackQuery):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, представляющий входящий колбэк.

    Returns:
        None

    Raises:
        Exception: Если возникает ошибка при открытии админ-панели.

    Example:
        Пример вызова:
        (Предположим, что у нас есть объект `call` типа `CallbackQuery`)
        >>> await start_admin(call)
    """
```

**Описание**:
Обработчик колбэка `admin_panel`. Проверяет, имеет ли пользователь доступ к админ-панели на основе `settings.ADMIN_IDS`. Если доступ разрешен, отправляет сообщение с клавиатурой администратора.

**Параметры**:
- `call` (CallbackQuery): Объект колбэка, содержащий информацию о вызове.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Обрабатывает исключения, которые могут возникнуть при редактировании или отправке сообщений.

**Примеры**:
Пример вызова функции:
```python
# Пример вызова функции start_admin с объектом call типа CallbackQuery
await start_admin(call)
```

### `admin_statistic`

```python
async def admin_statistic(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, представляющий входящий колбэк.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

    Returns:
        None

    Raises:
        Нет

    Example:
        Пример вызова:
        (Предположим, что у нас есть объекты `call` типа `CallbackQuery` и `session_without_commit` типа `AsyncSession`)
        >>> await admin_statistic(call, session_without_commit)
    """
```

**Описание**:
Обработчик колбэка `statistic`. Собирает и отображает статистику пользователей и заказов. Использует `UserDAO` и `PurchaseDao` для получения данных из базы данных.

**Параметры**:
- `call` (CallbackQuery): Объект колбэка, содержащий информацию о вызове.
- `session_without_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

**Возвращает**:
- `None`

**Примеры**:
Пример вызова функции:
```python
# Пример вызова функции admin_statistic с объектами call типа CallbackQuery и session_without_commit типа AsyncSession
await admin_statistic(call, session_without_commit)
```

### `admin_process_cancel`

```python
async def admin_process_cancel(call: CallbackQuery, state: FSMContext):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, представляющий входящий колбэк.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.

    Returns:
        None

    Raises:
        Нет

    Example:
        Пример вызова:
        (Предположим, что у нас есть объекты `call` типа `CallbackQuery` и `state` типа `FSMContext`)
        >>> await admin_process_cancel(call, state)
    """
```

**Описание**:
Обработчик колбэка `cancel`. Очищает состояние FSM и отменяет процесс добавления товара.

**Параметры**:
- `call` (CallbackQuery): Объект колбэка, содержащий информацию о вызове.
- `state` (FSMContext): Объект FSMContext для управления состоянием пользователя.

**Возвращает**:
- `None`

**Примеры**:
Пример вызова функции:
```python
# Пример вызова функции admin_process_cancel с объектами call типа CallbackQuery и state типа FSMContext
await admin_process_cancel(call, state)
```

### `admin_process_start_dell`

```python
async def admin_process_start_dell(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, представляющий входящий колбэк.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

    Returns:
        None

    Raises:
        Нет

    Example:
        Пример вызова:
        (Предположим, что у нас есть объекты `call` типа `CallbackQuery` и `session_without_commit` типа `AsyncSession`)
        >>> await admin_process_start_dell(call, session_without_commit)
    """
```

**Описание**:
Обработчик колбэка `delete_product`. Запускает процесс удаления товара, отображая список всех товаров с возможностью выбора для удаления.

**Параметры**:
- `call` (CallbackQuery): Объект колбэка, содержащий информацию о вызове.
- `session_without_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

**Возвращает**:
- `None`

**Примеры**:
Пример вызова функции:
```python
# Пример вызова функции admin_process_start_dell с объектами call типа CallbackQuery и session_without_commit типа AsyncSession
await admin_process_start_dell(call, session_without_commit)
```

### `admin_process_start_dell`

```python
async def admin_process_start_dell(call: CallbackQuery, session_with_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, представляющий входящий колбэк.
        session_with_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных с коммитом.

    Returns:
        None

    Raises:
        Нет

    Example:
        Пример вызова:
        (Предположим, что у нас есть объекты `call` типа `CallbackQuery` и `session_with_commit` типа `AsyncSession`)
        >>> await admin_process_start_dell(call, session_with_commit)
    """
```

**Описание**:
Обработчик колбэков, начинающихся с `dell_`. Удаляет выбранный товар из базы данных.

**Параметры**:
- `call` (CallbackQuery): Объект колбэка, содержащий информацию о вызове.
- `session_with_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных с коммитом.

**Возвращает**:
- `None`

**Примеры**:
Пример вызова функции:
```python
# Пример вызова функции admin_process_start_dell с объектами call типа CallbackQuery и session_with_commit типа AsyncSession
await admin_process_start_dell(call, session_with_commit)
```

### `admin_process_products`

```python
async def admin_process_products(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, представляющий входящий колбэк.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

    Returns:
        None

    Raises:
        Нет

    Example:
        Пример вызова:
        (Предположим, что у нас есть объекты `call` типа `CallbackQuery` и `session_without_commit` типа `AsyncSession`)
        >>> await admin_process_products(call, session_without_commit)
    """
```

**Описание**:
Обработчик колбэка `process_products`. Отображает количество товаров в базе данных и предлагает выбор действий (добавить, удалить и т.д.).

**Параметры**:
- `call` (CallbackQuery): Объект колбэка, содержащий информацию о вызове.
- `session_without_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

**Возвращает**:
- `None`

**Примеры**:
Пример вызова функции:
```python
# Пример вызова функции admin_process_products с объектами call типа CallbackQuery и session_without_commit типа AsyncSession
await admin_process_products(call, session_without_commit)
```

### `admin_process_add_product`

```python
async def admin_process_add_product(call: CallbackQuery, state: FSMContext):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, представляющий входящий колбэк.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.

    Returns:
        None

    Raises:
        Нет

    Example:
        Пример вызова:
        (Предположим, что у нас есть объекты `call` типа `CallbackQuery` и `state` типа `FSMContext`)
        >>> await admin_process_add_product(call, state)
    """
```

**Описание**:
Обработчик колбэка `add_product`. Запускает сценарий добавления нового товара, устанавливая начальное состояние `AddProduct.name`.

**Параметры**:
- `call` (CallbackQuery): Объект колбэка, содержащий информацию о вызове.
- `state` (FSMContext): Объект FSMContext для управления состоянием пользователя.

**Возвращает**:
- `None`

**Примеры**:
Пример вызова функции:
```python
# Пример вызова функции admin_process_add_product с объектами call типа CallbackQuery и state типа FSMContext
await admin_process_add_product(call, state)
```

### `admin_process_name`

```python
async def admin_process_name(message: Message, state: FSMContext):
    """
    Args:
        message (Message): Объект Message, представляющий входящее сообщение.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.

    Returns:
        None

    Raises:
        Нет

    Example:
        Пример вызова:
        (Предположим, что у нас есть объекты `message` типа `Message` и `state` типа `FSMContext`)
        >>> await admin_process_name(message, state)
    """
```

**Описание**:
Обработчик текстового сообщения в состоянии `AddProduct.name`. Сохраняет имя товара и переходит к следующему состоянию `AddProduct.description`.

**Параметры**:
- `message` (Message): Объект сообщения, содержащий текст с именем товара.
- `state` (FSMContext): Объект FSMContext для управления состоянием пользователя.

**Возвращает**:
- `None`

**Примеры**:
Пример вызова функции:
```python
# Пример вызова функции admin_process_name с объектами message типа Message и state типа FSMContext
await admin_process_name(message, state)
```

### `admin_process_description`

```python
async def admin_process_description(message: Message, state: FSMContext, session_without_commit: AsyncSession):
    """
    Args:
        message (Message): Объект Message, представляющий входящее сообщение.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

    Returns:
        None

    Raises:
        Нет

    Example:
        Пример вызова:
        (Предположим, что у нас есть объекты `message` типа `Message`, `state` типа `FSMContext` и `session_without_commit` типа `AsyncSession`)
        >>> await admin_process_description(message, state, session_without_commit)
    """
```

**Описание**:
Обработчик текстового сообщения в состоянии `AddProduct.description`. Сохраняет описание товара и переходит к следующему состоянию `AddProduct.category_id`.

**Параметры**:
- `message` (Message): Объект сообщения, содержащий текст с описанием товара.
- `state` (FSMContext): Объект FSMContext для управления состоянием пользователя.
- `session_without_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

**Возвращает**:
- `None`

**Примеры**:
Пример вызова функции:
```python
# Пример вызова функции admin_process_description с объектами message типа Message, state типа FSMContext и session_without_commit типа AsyncSession
await admin_process_description(message, state, session_without_commit)
```

### `admin_process_category`

```python
async def admin_process_category(call: CallbackQuery, state: FSMContext):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, представляющий входящий колбэк.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.

    Returns:
        None

    Raises:
        Нет

    Example:
        Пример вызова:
        (Предположим, что у нас есть объекты `call` типа `CallbackQuery` и `state` типа `FSMContext`)
        >>> await admin_process_category(call, state)
    """
```

**Описание**:
Обработчик колбэков, начинающихся с `add_category_`. Сохраняет идентификатор выбранной категории товара и переходит к следующему состоянию `AddProduct.price`.

**Параметры**:
- `call` (CallbackQuery): Объект колбэка, содержащий информацию о вызове.
- `state` (FSMContext): Объект FSMContext для управления состоянием пользователя.

**Возвращает**:
- `None`

**Примеры**:
Пример вызова функции:
```python
# Пример вызова функции admin_process_category с объектами call типа CallbackQuery и state типа FSMContext
await admin_process_category(call, state)
```

### `admin_process_price`

```python
async def admin_process_price(message: Message, state: FSMContext):
    """
    Args:
        message (Message): Объект Message, представляющий входящее сообщение.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.

    Returns:
        None

    Raises:
        ValueError: Если введенное значение цены не является числом.

    Example:
        Пример вызова:
        (Предположим, что у нас есть объекты `message` типа `Message` и `state` типа `FSMContext`)
        >>> await admin_process_price(message, state)
    """
```

**Описание**:
Обработчик текстового сообщения в состоянии `AddProduct.price`. Сохраняет цену товара и переходит к следующему состоянию `AddProduct.file_id`.

**Параметры**:
- `message` (Message): Объект сообщения, содержащий текст с ценой товара.
- `state` (FSMContext): Объект FSMContext для управления состоянием пользователя.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если введенное значение цены не является числом.

**Примеры**:
Пример вызова функции:
```python
# Пример вызова функции admin_process_price с объектами message типа Message и state типа FSMContext
await admin_process_price(message, state)
```

### `admin_process_without_file`

```python
async def admin_process_without_file(call: CallbackQuery, state: FSMContext):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, представляющий входящий колбэк.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.

    Returns:
        None

    Raises:
        Нет

    Example:
        Пример вызова:
        (Предположим, что у нас есть объекты `call` типа `CallbackQuery` и `state` типа `FSMContext`)
        >>> await admin_process_without_file(call, state)
    """
```

**Описание**:
Обработчик колбэка `without_file`. Устанавливает `file_id` в `None`, если файл не выбран, и переходит к следующему состоянию `AddProduct.hidden_content`.

**Параметры**:
- `call` (CallbackQuery): Объект колбэка, содержащий информацию о вызове.
- `state` (FSMContext): Объект FSMContext для управления состоянием пользователя.

**Возвращает**:
- `None`

**Примеры**:
Пример вызова функции:
```python
# Пример вызова функции admin_process_without_file с объектами call типа CallbackQuery и state типа FSMContext
await admin_process_without_file(call, state)
```

### `admin_process_without_file`

```python
async def admin_process_without_file(message: Message, state: FSMContext):
    """
    Args:
        message (Message): Объект Message, представляющий входящее сообщение.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.

    Returns:
        None

    Raises:
        Нет

    Example:
        Пример вызова:
        (Предположим, что у нас есть объекты `message` типа `Message` и `state` типа `FSMContext`)
        >>> await admin_process_without_file(message, state)
    """
```

**Описание**:
Обработчик документа в состоянии `AddProduct.file_id`. Сохраняет `file_id` и переходит к следующему состоянию `AddProduct.hidden_content`.

**Параметры**:
- `message` (Message): Объект сообщения, содержащий документ (файл).
- `state` (FSMContext): Объект FSMContext для управления состоянием пользователя.

**Возвращает**:
- `None`

**Примеры**:
Пример вызова функции:
```python
# Пример вызова функции admin_process_without_file с объектами message типа Message и state типа FSMContext
await admin_process_without_file(message, state)
```

### `admin_process_hidden_content`

```python
async def admin_process_hidden_content(message: Message, state: FSMContext, session_without_commit: AsyncSession):
    """
    Args:
        message (Message): Объект Message, представляющий входящее сообщение.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

    Returns:
        None

    Raises:
        Нет

    Example:
        Пример вызова:
        (Предположим, что у нас есть объекты `message` типа `Message`, `state` типа `FSMContext` и `session_without_commit` типа `AsyncSession`)
        >>> await admin_process_hidden_content(message, state, session_without_commit)
    """
```

**Описание**:
Обработчик текстового сообщения в состоянии `AddProduct.hidden_content`. Сохраняет скрытый контент товара, формирует сообщение с информацией о товаре и предлагает подтвердить добавление.

**Параметры**:
- `message` (Message): Объект сообщения, содержащий текст со скрытым контентом товара.
- `state` (FSMContext): Объект FSMContext для управления состоянием пользователя.
- `session_without_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

**Возвращает**:
- `None`

**Примеры**:
Пример вызова функции:
```python
# Пример вызова функции admin_process_hidden_content с объектами message типа Message, state типа FSMContext и session_without_commit типа AsyncSession
await admin_process_hidden_content(message, state, session_without_commit)
```

### `admin_process_confirm_add`

```python
async def admin_process_confirm_add(call: CallbackQuery, state: FSMContext, session_with_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, представляющий входящий колбэк.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.
        session_with_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных с коммитом.

    Returns:
        None

    Raises:
        Нет

    Example:
        Пример вызова:
        (Предположим, что у нас есть объекты `call` типа `CallbackQuery`, `state` типа `FSMContext` и `session_with_commit` типа `AsyncSession`)
        >>> await admin_process_confirm_add(call, state, session_with_commit)
    """
```

**Описание**:
Обработчик колбэка `confirm_add`. Подтверждает добавление товара, сохраняет данные в базе данных и завершает сценарий добавления товара.

**Параметры**:
- `call` (CallbackQuery): Объект колбэка, содержащий информацию о вызове.
- `state` (FSMContext): Объект FSMContext для управления состоянием пользователя.
- `session_with_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных с коммитом.

**Возвращает**:
- `None`

**Примеры**:
Пример вызова функции:
```python
# Пример вызова функции admin_process_confirm_add с объектами call типа CallbackQuery, state типа FSMContext и session_with_commit типа AsyncSession
await admin_process_confirm_add(call, state, session_with_commit)