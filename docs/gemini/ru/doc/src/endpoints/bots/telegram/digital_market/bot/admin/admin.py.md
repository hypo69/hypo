# `admin.py`

## Обзор

Этот модуль реализует функциональность административной панели для Telegram-бота, позволяя администраторам управлять продуктами, просматривать статистику и выполнять другие административные действия.

## Оглавление

1. [Классы](#Классы)
   - [`AddProduct`](#AddProduct)
2. [Функции](#Функции)
   - [`start_admin`](#start_admin)
   - [`admin_statistic`](#admin_statistic)
   - [`admin_process_cancel`](#admin_process_cancel)
   - [`admin_process_start_dell`](#admin_process_start_dell)
   - [`admin_process_products`](#admin_process_products)
   - [`admin_process_add_product`](#admin_process_add_product)
   - [`admin_process_name`](#admin_process_name)
   - [`admin_process_description`](#admin_process_description)
   - [`admin_process_category`](#admin_process_category)
    - [`admin_process_price`](#admin_process_price)
   - [`admin_process_without_file`](#admin_process_without_file)
   - [`admin_process_hidden_content`](#admin_process_hidden_content)
   -  [`admin_process_confirm_add`](#admin_process_confirm_add)

## Классы

### `AddProduct`
**Описание**:
    Класс, представляющий состояния для добавления нового продукта.
**Состояния**:
    - `name`: Состояние для ввода имени продукта.
    - `description`: Состояние для ввода описания продукта.
    - `price`: Состояние для ввода цены продукта.
    - `file_id`: Состояние для загрузки файла продукта.
    - `category_id`: Состояние для выбора категории продукта.
    - `hidden_content`: Состояние для ввода скрытого контента продукта.
    - `confirm_add`: Состояние для подтверждения добавления продукта.
## Функции

### `start_admin`
**Описание**:
    Обрабатывает команду открытия админ-панели.
**Параметры**:
    - `call` (CallbackQuery): Объект обратного вызова.
**Возвращает**:
    - `None`: Функция ничего не возвращает.

**Вызывает исключения**:
    - `Exception`: Возникает при ошибках отправки или редактирования сообщения.

### `admin_statistic`
**Описание**:
    Получает и отправляет статистику по пользователям и заказам.
**Параметры**:
    - `call` (CallbackQuery): Объект обратного вызова.
    - `session_without_commit` (AsyncSession): Сессия базы данных без коммита.
**Возвращает**:
    - `None`: Функция ничего не возвращает.

### `admin_process_cancel`
**Описание**:
    Обрабатывает команду отмены текущего действия (например, добавления товара).
**Параметры**:
    - `call` (CallbackQuery): Объект обратного вызова.
    - `state` (FSMContext): Объект состояния FSM.
**Возвращает**:
    - `None`: Функция ничего не возвращает.

### `admin_process_start_dell`
**Описание**:
    Обрабатывает команду начала удаления товаров.
**Параметры**:
    - `call` (CallbackQuery): Объект обратного вызова.
    - `session_without_commit` (AsyncSession): Сессия базы данных без коммита.
**Возвращает**:
    - `None`: Функция ничего не возвращает.

### `admin_process_start_dell`
**Описание**:
    Обрабатывает удаление товара.
**Параметры**:
    - `call` (CallbackQuery): Объект обратного вызова.
    - `session_with_commit` (AsyncSession): Сессия базы данных с коммитом.
**Возвращает**:
    - `None`: Функция ничего не возвращает.

### `admin_process_products`
**Описание**:
    Обрабатывает команду управления товарами.
**Параметры**:
    - `call` (CallbackQuery): Объект обратного вызова.
    - `session_without_commit` (AsyncSession): Сессия базы данных без коммита.
**Возвращает**:
    - `None`: Функция ничего не возвращает.

### `admin_process_add_product`
**Описание**:
    Начинает сценарий добавления нового продукта.
**Параметры**:
    - `call` (CallbackQuery): Объект обратного вызова.
    - `state` (FSMContext): Объект состояния FSM.
**Возвращает**:
    - `None`: Функция ничего не возвращает.

### `admin_process_name`
**Описание**:
    Обрабатывает ввод имени продукта.
**Параметры**:
    - `message` (Message): Объект сообщения.
    - `state` (FSMContext): Объект состояния FSM.
**Возвращает**:
    - `None`: Функция ничего не возвращает.

### `admin_process_description`
**Описание**:
    Обрабатывает ввод описания продукта.
**Параметры**:
    - `message` (Message): Объект сообщения.
    - `state` (FSMContext): Объект состояния FSM.
    - `session_without_commit` (AsyncSession): Сессия базы данных без коммита.
**Возвращает**:
    - `None`: Функция ничего не возвращает.

### `admin_process_category`
**Описание**:
    Обрабатывает выбор категории продукта.
**Параметры**:
    - `call` (CallbackQuery): Объект обратного вызова.
    - `state` (FSMContext): Объект состояния FSM.
**Возвращает**:
    - `None`: Функция ничего не возвращает.

### `admin_process_price`
**Описание**:
    Обрабатывает ввод цены продукта.
**Параметры**:
    - `message` (Message): Объект сообщения.
    - `state` (FSMContext): Объект состояния FSM.
**Возвращает**:
    - `None`: Функция ничего не возвращает.
**Вызывает исключения**:
    - `ValueError`: Вызывается, если введенное значение цены не является числом.

### `admin_process_without_file`
**Описание**:
    Обрабатывает ситуацию, когда файл для продукта не загружается.
**Параметры**:
    - `call` (CallbackQuery): Объект обратного вызова.
    - `state` (FSMContext): Объект состояния FSM.
**Возвращает**:
    - `None`: Функция ничего не возвращает.
### `admin_process_without_file`
**Описание**:
    Обрабатывает ситуацию, когда файл для продукта загружается.
**Параметры**:
    - `message` (Message): Объект сообщения.
    - `state` (FSMContext): Объект состояния FSM.
**Возвращает**:
    - `None`: Функция ничего не возвращает.

### `admin_process_hidden_content`
**Описание**:
    Обрабатывает ввод скрытого контента продукта и выводит подтверждение.
**Параметры**:
    - `message` (Message): Объект сообщения.
    - `state` (FSMContext): Объект состояния FSM.
    - `session_without_commit` (AsyncSession): Сессия базы данных без коммита.
**Возвращает**:
    - `None`: Функция ничего не возвращает.

### `admin_process_confirm_add`
**Описание**:
    Обрабатывает подтверждение добавления продукта.
**Параметры**:
    - `call` (CallbackQuery): Объект обратного вызова.
    - `state` (FSMContext): Объект состояния FSM.
    - `session_with_commit` (AsyncSession): Сессия базы данных с коммитом.
**Возвращает**:
    - `None`: Функция ничего не возвращает.