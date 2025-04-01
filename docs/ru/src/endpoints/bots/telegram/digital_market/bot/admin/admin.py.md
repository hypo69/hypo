# Модуль `admin`

## Обзор

Модуль `admin` предназначен для организации работы административной панели Telegram-бота. Он включает в себя обработку команд администратора, управление товарами (добавление, удаление, просмотр статистики) и другие административные функции.

## Подробней

Этот модуль предоставляет набор функций и обработчиков для управления административной частью Telegram-бота. Он использует библиотеку `aiogram` для обработки входящих запросов от администраторов и `SQLAlchemy` для взаимодействия с базой данных.

## Классы

### `AddProduct(StatesGroup)`

**Описание**:
Класс `AddProduct` представляет собой группу состояний (StatesGroup) для процесса добавления нового товара в базу данных. Каждое состояние соответствует определенному шагу в процессе добавления товара.

**Как работает класс**:
Класс `AddProduct` наследуется от `StatesGroup` из библиотеки `aiogram.fsm`. Он определяет состояния, необходимые для сбора информации о новом продукте от администратора. Каждое состояние представляет собой отдельный атрибут класса типа `State`.

**Состояния**:
- `name` (State): Ожидание ввода имени товара.
- `description` (State): Ожидание ввода описания товара.
- `price` (State): Ожидание ввода цены товара.
- `file_id` (State): Ожидание отправки файла товара (если есть).
- `category_id` (State): Ожидание выбора категории товара.
- `hidden_content` (State): Ожидание ввода скрытого контента товара.
- `confirm_add` (State): Ожидание подтверждения добавления товара.

## Функции

### `start_admin(call: CallbackQuery)`

```python
async def start_admin(call: CallbackQuery):
    """Обработчик callback-запроса для входа в админ-панель.

    Args:
        call (CallbackQuery): Объект callback-запроса от пользователя.

    Raises:
        Exception: Если происходит ошибка при открытии админ-панели.

    Как работает функция:
    1. Проверяет, имеет ли пользователь право доступа в админ-панель на основе `settings.ADMIN_IDS`.
    2. Отправляет подтверждение доступа.
    3. Редактирует сообщение, предоставляя пользователю выбор действий в админ-панели.
    4. Обрабатывает исключения, если не удается отредактировать или отправить сообщение.

    Внутри функции происходят следующие действия и преобразования:
    A: Проверка прав доступа пользователя.
    |
    -- B: Редактирование сообщения с предоставлением выбора действий.
    |
    C: Обработка ошибок при редактировании/отправке сообщения.

    Примеры:
    Пример вызова функции:
    >>> await start_admin(call)
    """
```

### `admin_statistic(call: CallbackQuery, session_without_commit: AsyncSession)`

```python
async def admin_statistic(call: CallbackQuery, session_without_commit: AsyncSession):
    """Обработчик callback-запроса для получения статистики.

    Args:
        call (CallbackQuery): Объект callback-запроса от пользователя.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к БД.

    Как работает функция:
    1. Отправляет подтверждение о запросе статистики.
    2. Извлекает статистику пользователей и статистику по заказам из базы данных.
    3. Формирует сообщение со статистикой.
    4. Редактирует сообщение, отправляя статистику пользователю.

    Внутри функции происходят следующие действия и преобразования:
    A: Получение статистики пользователей.
    |
    -- B: Получение статистики по заказам.
    |
    C: Формирование сообщения со статистикой.
    |
    D: Отправка сообщения со статистикой пользователю.

    Примеры:
    Пример вызова функции:
    >>> await admin_statistic(call, session_without_commit)
    """
```

### `admin_process_cancel(call: CallbackQuery, state: FSMContext)`

```python
async def admin_process_cancel(call: CallbackQuery, state: FSMContext):
    """Обработчик callback-запроса для отмены текущего сценария добавления товара.

    Args:
        call (CallbackQuery): Объект callback-запроса от пользователя.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.

    Как работает функция:
    1. Очищает текущее состояние пользователя.
    2. Отправляет подтверждение об отмене сценария.
    3. Удаляет предыдущее сообщение и отправляет новое сообщение об отмене.

    Внутри функции происходят следующие действия и преобразования:
    A: Очистка состояния пользователя.
    |
    -- B: Отправка сообщения об отмене.

    Примеры:
    Пример вызова функции:
    >>> await admin_process_cancel(call, state)
    """
```

### `admin_process_start_dell(call: CallbackQuery, session_without_commit: AsyncSession)`

```python
async def admin_process_start_dell(call: CallbackQuery, session_without_commit: AsyncSession):
    """Обработчик callback-запроса для начала процесса удаления товара.

    Args:
        call (CallbackQuery): Объект callback-запроса от пользователя.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к БД.

    Как работает функция:
    1. Отправляет подтверждение о начале режима удаления товаров.
    2. Извлекает все товары из базы данных.
    3. Формирует сообщение для каждого товара с кнопкой удаления.
    4. Отправляет сообщения с информацией о товарах и кнопками удаления.

    Внутри функции происходят следующие действия и преобразования:
    A: Получение всех товаров из базы данных.
    |
    -- B: Формирование сообщений с информацией о товарах и кнопками удаления.
    |
    C: Отправка сообщений пользователю.

    Примеры:
    Пример вызова функции:
    >>> await admin_process_start_dell(call, session_without_commit)
    """
```

### `admin_process_start_dell(call: CallbackQuery, session_with_commit: AsyncSession)`

```python
async def admin_process_start_dell(call: CallbackQuery, session_with_commit: AsyncSession):
    """Обработчик callback-запроса для удаления товара.

    Args:
        call (CallbackQuery): Объект callback-запроса от пользователя.
        session_with_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к БД.

    Как работает функция:
    1. Извлекает ID товара из callback-запроса.
    2. Удаляет товар из базы данных.
    3. Отправляет подтверждение об удалении товара.
    4. Удаляет сообщение с информацией о товаре.

    Внутри функции происходят следующие действия и преобразования:
    A: Извлечение ID товара из callback-запроса.
    |
    -- B: Удаление товара из базы данных.
    |
    C: Отправка подтверждения и удаление сообщения.

    Примеры:
    Пример вызова функции:
    >>> await admin_process_start_dell(call, session_with_commit)
    """
```

### `admin_process_products(call: CallbackQuery, session_without_commit: AsyncSession)`

```python
async def admin_process_products(call: CallbackQuery, session_without_commit: AsyncSession):
    """Обработчик callback-запроса для управления товарами.

    Args:
        call (CallbackQuery): Объект callback-запроса от пользователя.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к БД.

    Как работает функция:
    1. Отправляет подтверждение о начале режима управления товарами.
    2. Подсчитывает количество товаров в базе данных.
    3. Редактирует сообщение, предлагая пользователю выбор действий (добавить, удалить и т.д.).

    Внутри функции происходят следующие действия и преобразования:
    A: Подсчет количества товаров в базе данных.
    |
    -- B: Отправка сообщения с вариантами действий.

    Примеры:
    Пример вызова функции:
    >>> await admin_process_products(call, session_without_commit)
    """
```

### `admin_process_add_product(call: CallbackQuery, state: FSMContext)`

```python
async def admin_process_add_product(call: CallbackQuery, state: FSMContext):
    """Обработчик callback-запроса для начала процесса добавления товара.

    Args:
        call (CallbackQuery): Объект callback-запроса от пользователя.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.

    Как работает функция:
    1. Отправляет подтверждение о начале сценария добавления товара.
    2. Удаляет предыдущее сообщение.
    3. Запрашивает у пользователя имя товара.
    4. Устанавливает состояние `AddProduct.name`.

    Внутри функции происходят следующие действия и преобразования:
    A: Запрос имени товара у пользователя.
    |
    -- B: Установка состояния `AddProduct.name`.

    Примеры:
    Пример вызова функции:
    >>> await admin_process_add_product(call, state)
    """
```

### `admin_process_name(message: Message, state: FSMContext)`

```python
async def admin_process_name(message: Message, state: FSMContext):
    """Обработчик сообщения с именем товара.

    Args:
        message (Message): Объект сообщения от пользователя.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.

    Как работает функция:
    1. Обновляет состояние, сохраняя имя товара.
    2. Удаляет предыдущее сообщение пользователя.
    3. Запрашивает у пользователя описание товара.
    4. Устанавливает состояние `AddProduct.description`.

    Внутри функции происходят следующие действия и преобразования:
    A: Сохранение имени товара в состояние.
    |
    -- B: Запрос описания товара у пользователя.
    |
    C: Установка состояния `AddProduct.description`.

    Примеры:
    Пример вызова функции:
    >>> await admin_process_name(message, state)
    """
```

### `admin_process_description(message: Message, state: FSMContext, session_without_commit: AsyncSession)`

```python
async def admin_process_description(message: Message, state: FSMContext, session_without_commit: AsyncSession):
    """Обработчик сообщения с описанием товара.

    Args:
        message (Message): Объект сообщения от пользователя.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к БД.

    Как работает функция:
    1. Обновляет состояние, сохраняя описание товара.
    2. Удаляет предыдущее сообщение пользователя.
    3. Получает список категорий товаров из базы данных.
    4. Предлагает пользователю выбрать категорию товара.
    5. Устанавливает состояние `AddProduct.category_id`.

    Внутри функции происходят следующие действия и преобразования:
    A: Сохранение описания товара в состояние.
    |
    -- B: Получение списка категорий товаров из базы данных.
    |
    C: Предложение выбора категории товара пользователю.
    |
    D: Установка состояния `AddProduct.category_id`.

    Примеры:
    Пример вызова функции:
    >>> await admin_process_description(message, state, session_without_commit)
    """
```

### `admin_process_category(call: CallbackQuery, state: FSMContext)`

```python
async def admin_process_category(call: CallbackQuery, state: FSMContext):
    """Обработчик callback-запроса с выбранной категорией товара.

    Args:
        call (CallbackQuery): Объект callback-запроса от пользователя.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.

    Как работает функция:
    1. Извлекает ID категории из callback-запроса.
    2. Обновляет состояние, сохраняя ID категории товара.
    3. Отправляет подтверждение о выборе категории.
    4. Предлагает пользователю ввести цену товара.
    5. Устанавливает состояние `AddProduct.price`.

    Внутри функции происходят следующие действия и преобразования:
    A: Извлечение ID категории из callback-запроса.
    |
    -- B: Сохранение ID категории в состояние.
    |
    C: Предложение ввести цену товара пользователю.
    |
    D: Установка состояния `AddProduct.price`.

    Примеры:
    Пример вызова функции:
    >>> await admin_process_category(call, state)
    """
```

### `admin_process_price(message: Message, state: FSMContext)`

```python
async def admin_process_price(message: Message, state: FSMContext):
    """Обработчик сообщения с ценой товара.

    Args:
        message (Message): Объект сообщения от пользователя.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.

    Как работает функция:
    1. Пытается преобразовать введенный текст в число (цену).
    2. Обновляет состояние, сохраняя цену товара.
    3. Удаляет предыдущее сообщение пользователя.
    4. Предлагает пользователю отправить файл товара или выбрать вариант "БЕЗ ФАЙЛА".
    5. Устанавливает состояние `AddProduct.file_id`.
    6. Обрабатывает исключение `ValueError`, если введенный текст не является числом.

    Внутри функции происходят следующие действия и преобразования:
    A: Преобразование введенного текста в число (цену).
    |
    -- B: Сохранение цены товара в состояние.
    |
    C: Предложение отправить файл товара или выбрать вариант "БЕЗ ФАЙЛА".
    |
    D: Установка состояния `AddProduct.file_id`.
    |
    E: Обработка исключения `ValueError`.

    Примеры:
    Пример вызова функции:
    >>> await admin_process_price(message, state)
    """
```

### `admin_process_without_file(call: CallbackQuery, state: FSMContext)`

```python
async def admin_process_without_file(call: CallbackQuery, state: FSMContext):
    """Обработчик callback-запроса для варианта "БЕЗ ФАЙЛА".

    Args:
        call (CallbackQuery): Объект callback-запроса от пользователя.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.

    Как работает функция:
    1. Обновляет состояние, устанавливая `file_id` в `None`.
    2. Отправляет подтверждение о том, что файл не выбран.
    3. Предлагает пользователю отправить скрытый контент товара.
    4. Устанавливает состояние `AddProduct.hidden_content`.

    Внутри функции происходят следующие действия и преобразования:
    A: Установка `file_id` в `None`.
    |
    -- B: Предложение отправить скрытый контент товара.
    |
    C: Установка состояния `AddProduct.hidden_content`.

    Примеры:
    Пример вызова функции:
    >>> await admin_process_without_file(call, state)
    """
```

### `admin_process_without_file(message: Message, state: FSMContext)`

```python
async def admin_process_without_file(message: Message, state: FSMContext):
    """Обработчик сообщения с файлом товара.

    Args:
        message (Message): Объект сообщения от пользователя.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.

    Как работает функция:
    1. Обновляет состояние, сохраняя `file_id` отправленного файла.
    2. Удаляет предыдущее сообщение пользователя.
    3. Предлагает пользователю отправить скрытый контент товара.
    4. Устанавливает состояние `AddProduct.hidden_content`.

    Внутри функции происходят следующие действия и преобразования:
    A: Сохранение `file_id` отправленного файла в состояние.
    |
    -- B: Предложение отправить скрытый контент товара.
    |
    C: Установка состояния `AddProduct.hidden_content`.

    Примеры:
    Пример вызова функции:
    >>> await admin_process_without_file(message, state)
    """
```

### `admin_process_hidden_content(message: Message, state: FSMContext, session_without_commit: AsyncSession)`

```python
async def admin_process_hidden_content(message: Message, state: FSMContext, session_without_commit: AsyncSession):
    """Обработчик сообщения со скрытым контентом товара.

    Args:
        message (Message): Объект сообщения от пользователя.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к БД.

    Как работает функция:
    1. Обновляет состояние, сохраняя скрытый контент товара.
    2. Получает данные о товаре из состояния.
    3. Получает информацию о категории товара из базы данных.
    4. Формирует сообщение с информацией о товаре для подтверждения.
    5. Предлагает пользователю подтвердить добавление товара.
    6. Устанавливает состояние `AddProduct.confirm_add`.

    Внутри функции происходят следующие действия и преобразования:
    A: Сохранение скрытого контента товара в состояние.
    |
    -- B: Получение данных о товаре из состояния.
    |
    C: Получение информации о категории товара из базы данных.
    |
    D: Формирование сообщения с информацией о товаре для подтверждения.
    |
    E: Предложение подтвердить добавление товара.
    |
    F: Установка состояния `AddProduct.confirm_add`.

    Примеры:
    Пример вызова функции:
    >>> await admin_process_hidden_content(message, state, session_without_commit)
    """
```

### `admin_process_confirm_add(call: CallbackQuery, state: FSMContext, session_with_commit: AsyncSession)`

```python
async def admin_process_confirm_add(call: CallbackQuery, state: FSMContext, session_with_commit: AsyncSession):
    """Обработчик callback-запроса для подтверждения добавления товара.

    Args:
        call (CallbackQuery): Объект callback-запроса от пользователя.
        state (FSMContext): Объект FSMContext для управления состоянием пользователя.
        session_with_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к БД.

    Как работает функция:
    1. Отправляет подтверждение о начале сохранения файла.
    2. Получает данные о товаре из состояния.
    3. Удаляет сообщение с подтверждением.
    4. Добавляет товар в базу данных.
    5. Отправляет сообщение об успешном добавлении товара.

    Внутри функции происходят следующие действия и преобразования:
    A: Получение данных о товаре из состояния.
    |
    -- B: Добавление товара в базу данных.
    |
    C: Отправка сообщения об успешном добавлении товара.

    Примеры:
    Пример вызова функции:
    >>> await admin_process_confirm_add(call, state, session_with_commit)
    """