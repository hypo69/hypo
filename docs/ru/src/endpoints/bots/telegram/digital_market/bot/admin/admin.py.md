# Модуль `admin`

## Обзор

Модуль `admin` предназначен для обработки административных функций в Telegram-боте цифрового рынка. Он включает в себя обработку команд администратора, таких как просмотр статистики, управление продуктами (добавление, удаление) и отмена операций.

## Подробней

Этот модуль содержит набор обработчиков (`handlers`) для различных административных действий, выполняемых через Telegram-бота. Он использует конечные автоматы (FSM) для управления состоянием при добавлении новых продуктов, а также взаимодействует с базой данных через DAO для выполнения операций с пользователями, продуктами и категориями.

## Классы

### `AddProduct(StatesGroup)`

**Описание**:
Класс состояний, используемый для управления процессом добавления нового продукта через FSM (Finite State Machine).

**Как работает класс**:
Этот класс определяет набор состояний, через которые проходит процесс добавления продукта. Каждое состояние соответствует определенному этапу ввода информации о продукте (например, имя, описание, цена). FSM используется для последовательного сбора данных от администратора и сохранения их в контексте состояния.

**Состояния**:
- `name`: Ожидание ввода имени продукта.
- `description`: Ожидание ввода описания продукта.
- `price`: Ожидание ввода цены продукта.
- `file_id`: Ожидание отправки файла продукта (если есть).
- `category_id`: Ожидание выбора категории продукта.
- `hidden_content`: Ожидание ввода скрытого контента продукта.
- `confirm_add`: Ожидание подтверждения добавления продукта.

## Функции

### `start_admin(call: CallbackQuery)`

```python
async def start_admin(call: CallbackQuery):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, содержащий информацию о взаимодействии пользователя с кнопкой административной панели.

    Raises:
        Exception: Обрабатывает исключения, возникающие при попытке редактирования или отправки сообщения.

    """
```

**Описание**:
Обработчик для запуска административной панели.

**Как работает функция**:
Функция обрабатывает нажатие на кнопку "admin_panel" и предоставляет администратору доступ к панели управления. Она пытается отредактировать существующее сообщение, чтобы отобразить административную клавиатуру. В случае ошибки редактирования, функция пытается удалить старое сообщение и отправить новое. Если и это не удается, отправляется сообщение об ошибке.

### `admin_statistic(call: CallbackQuery, session_without_commit: AsyncSession)`

```python
async def admin_statistic(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, содержащий информацию о взаимодействии пользователя с кнопкой запроса статистики.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без автоматической фиксации изменений.

    """
```

**Описание**:
Обработчик для получения и отображения административной статистики.

**Как работает функция**:
Функция обрабатывает нажатие на кнопку "statistic" и отображает статистику пользователей и заказов. Она использует `UserDAO` и `PurchaseDao` для получения данных из базы данных и форматирует их в удобочитаемое сообщение.

### `admin_process_cancel(call: CallbackQuery, state: FSMContext)`

```python
async def admin_process_cancel(call: CallbackQuery, state: FSMContext):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, содержащий информацию о взаимодействии пользователя с кнопкой отмены.
        state (FSMContext): Объект FSMContext, содержащий состояние конечного автомата для текущего пользователя.

    """
```

**Описание**:
Обработчик для отмены процесса добавления товара.

**Как работает функция**:
Функция обрабатывает нажатие на кнопку "cancel" и отменяет текущий процесс добавления товара, очищая состояние FSM и отправляя сообщение об отмене.

### `admin_process_start_dell(call: CallbackQuery, session_without_commit: AsyncSession)`

```python
async def admin_process_start_dell(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, содержащий информацию о взаимодействии пользователя с кнопкой удаления товара.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без автоматической фиксации изменений.

    """
```

**Описание**:
Обработчик для начала процесса удаления товара.

**Как работает функция**:
Функция обрабатывает нажатие на кнопку "delete_product" и отображает список всех товаров в базе данных с возможностью их удаления. Она использует `ProductDao` для получения списка товаров и формирует сообщения для каждого товара с кнопкой удаления.

### `admin_process_start_dell(call: CallbackQuery, session_with_commit: AsyncSession)`

```python
async def admin_process_start_dell(call: CallbackQuery, session_with_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, содержащий информацию о взаимодействии пользователя с кнопкой удаления товара.
        session_with_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных с автоматической фиксацией изменений.

    """
```

**Описание**:
Обработчик для фактического удаления товара из базы данных.

**Как работает функция**:
Функция обрабатывает нажатие на кнопку удаления товара и удаляет соответствующий товар из базы данных. Она использует `ProductDao` для удаления товара по его ID и отправляет уведомление об успешном удалении.

### `admin_process_products(call: CallbackQuery, session_without_commit: AsyncSession)`

```python
async def admin_process_products(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, содержащий информацию о взаимодействии пользователя с кнопкой управления товарами.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без автоматической фиксации изменений.

    """
```

**Описание**:
Обработчик для отображения панели управления продуктами.

**Как работает функция**:
Функция обрабатывает нажатие на кнопку "process_products" и отображает панель управления продуктами с возможностью добавления или удаления товаров.

### `admin_process_add_product(call: CallbackQuery, state: FSMContext)`

```python
async def admin_process_add_product(call: CallbackQuery, state: FSMContext):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, содержащий информацию о взаимодействии пользователя с кнопкой добавления товара.
        state (FSMContext): Объект FSMContext, содержащий состояние конечного автомата для текущего пользователя.

    """
```

**Описание**:
Обработчик для начала процесса добавления нового товара.

**Как работает функция**:
Функция обрабатывает нажатие на кнопку "add_product" и запускает процесс добавления нового товара, начиная с запроса имени товара. Она использует FSM для управления состоянием процесса.

### `admin_process_name(message: Message, state: FSMContext)`

```python
async def admin_process_name(message: Message, state: FSMContext):
    """
    Args:
        message (Message): Объект Message, содержащий текст сообщения от пользователя с именем товара.
        state (FSMContext): Объект FSMContext, содержащий состояние конечного автомата для текущего пользователя.

    """
```

**Описание**:
Обработчик для получения имени товара.

**Как работает функция**:
Функция обрабатывает ввод имени товара от администратора, сохраняет его в контексте FSM и запрашивает описание товара.

### `admin_process_description(message: Message, state: FSMContext, session_without_commit: AsyncSession)`

```python
async def admin_process_description(message: Message, state: FSMContext, session_without_commit: AsyncSession):
    """
    Args:
        message (Message): Объект Message, содержащий текст сообщения от пользователя с описанием товара.
        state (FSMContext): Объект FSMContext, содержащий состояние конечного автомата для текущего пользователя.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без автоматической фиксации изменений.

    """
```

**Описание**:
Обработчик для получения описания товара.

**Как работает функция**:
Функция обрабатывает ввод описания товара от администратора, сохраняет его в контексте FSM и запрашивает выбор категории товара.

### `admin_process_category(call: CallbackQuery, state: FSMContext)`

```python
async def admin_process_category(call: CallbackQuery, state: FSMContext):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, содержащий информацию о взаимодействии пользователя с кнопкой выбора категории товара.
        state (FSMContext): Объект FSMContext, содержащий состояние конечного автомата для текущего пользователя.

    """
```

**Описание**:
Обработчик для получения категории товара.

**Как работает функция**:
Функция обрабатывает выбор категории товара от администратора, сохраняет его в контексте FSM и запрашивает цену товара.

### `admin_process_price(message: Message, state: FSMContext)`

```python
async def admin_process_price(message: Message, state: FSMContext):
    """
    Args:
        message (Message): Объект Message, содержащий текст сообщения от пользователя с ценой товара.
        state (FSMContext): Объект FSMContext, содержащий состояние конечного автомата для текущего пользователя.

    """
```

**Описание**:
Обработчик для получения цены товара.

**Как работает функция**:
Функция обрабатывает ввод цены товара от администратора, проверяет, что цена является числом, сохраняет ее в контексте FSM и запрашивает файл товара (если есть).

### `admin_process_without_file(call: CallbackQuery, state: FSMContext)`

```python
async def admin_process_without_file(call: CallbackQuery, state: FSMContext):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, содержащий информацию о взаимодействии пользователя с кнопкой "без файла".
        state (FSMContext): Объект FSMContext, содержащий состояние конечного автомата для текущего пользователя.

    """
```

**Описание**:
Обработчик для случая, когда файл товара не требуется.

**Как работает функция**:
Функция обрабатывает нажатие на кнопку "without_file", сохраняет информацию об отсутствии файла в контексте FSM и запрашивает скрытый контент товара.

### `admin_process_without_file(message: Message, state: FSMContext)`

```python
async def admin_process_without_file(message: Message, state: FSMContext):
    """
    Args:
        message (Message): Объект Message, содержащий документ (файл) от пользователя.
        state (FSMContext): Объект FSMContext, содержащий состояние конечного автомата для текущего пользователя.

    """
```

**Описание**:
Обработчик для получения файла товара.

**Как работает функция**:
Функция обрабатывает отправку файла товара от администратора, сохраняет file_id в контексте FSM и запрашивает скрытый контент товара.

### `admin_process_hidden_content(message: Message, state: FSMContext, session_without_commit: AsyncSession)`

```python
async def admin_process_hidden_content(message: Message, state: FSMContext, session_without_commit: AsyncSession):
    """
    Args:
        message (Message): Объект Message, содержащий текст сообщения от пользователя со скрытым контентом товара.
        state (FSMContext): Объект FSMContext, содержащий состояние конечного автомата для текущего пользователя.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без автоматической фиксации изменений.

    """
```

**Описание**:
Обработчик для получения скрытого контента товара.

**Как работает функция**:
Функция обрабатывает ввод скрытого контента товара от администратора, сохраняет его в контексте FSM и отображает сводку всей информации о товаре для подтверждения.

### `admin_process_confirm_add(call: CallbackQuery, state: FSMContext, session_with_commit: AsyncSession)`

```python
async def admin_process_confirm_add(call: CallbackQuery, state: FSMContext, session_with_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, содержащий информацию о взаимодействии пользователя с кнопкой подтверждения добавления товара.
        state (FSMContext): Объект FSMContext, содержащий состояние конечного автомата для текущего пользователя.
        session_with_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных с автоматической фиксацией изменений.

    """
```

**Описание**:
Обработчик для подтверждения добавления товара.

**Как работает функция**:
Функция обрабатывает нажатие на кнопку "confirm_add", сохраняет информацию о товаре в базе данных и отправляет уведомление об успешном добавлении.