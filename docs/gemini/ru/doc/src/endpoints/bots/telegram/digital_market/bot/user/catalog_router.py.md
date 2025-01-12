# Модуль `catalog_router`

## Обзор

Модуль `catalog_router.py` реализует функциональность для обработки запросов, связанных с каталогом товаров в Telegram-боте. Он включает в себя обработку callback-запросов для навигации по категориям и отображения товаров, а также обработку запросов на оплату товаров через различные платежные системы (ЮKassa, Stars, Robokassa).

## Содержание

- [Функции](#Функции)
    - [`page_catalog`](#page_catalog)
    - [`page_catalog_products`](#page_catalog_products)
    - [`process_about`](#process_about)
    - [`send_yukassa_invoice`](#send_yukassa_invoice)
    - [`send_robocassa_invoice`](#send_robocassa_invoice)
    - [`send_stars_invoice`](#send_stars_invoice)
    - [`pre_checkout_query`](#pre_checkout_query)
    - [`successful_payment`](#successful_payment)

## Функции

### `page_catalog`

**Описание**:
Обрабатывает callback-запрос для отображения каталога категорий товаров.

**Параметры**:
- `call` (CallbackQuery): Объект callback-запроса.
- `session_without_commit` (AsyncSession): Асинхронная сессия базы данных.

**Возвращает**:
- `None`: Функция не возвращает значения.

**Вызывает исключения**:
- `Exception`: Обрабатывает любые исключения при удалении сообщения.

### `page_catalog_products`

**Описание**:
Обрабатывает callback-запрос для отображения товаров выбранной категории.

**Параметры**:
- `call` (CallbackQuery): Объект callback-запроса.
- `session_without_commit` (AsyncSession): Асинхронная сессия базы данных.

**Возвращает**:
- `None`: Функция не возвращает значения.

### `process_about`

**Описание**:
Обрабатывает callback-запрос для выбора способа оплаты товара.

**Параметры**:
- `call` (CallbackQuery): Объект callback-запроса.
- `session_without_commit` (AsyncSession): Асинхронная сессия базы данных.

**Возвращает**:
- `None`: Функция не возвращает значения.

### `send_yukassa_invoice`

**Описание**:
Отправляет пользователю инвойс для оплаты через ЮKassa.

**Параметры**:
- `call` (CallbackQuery): Объект callback-запроса.
- `user_info` (User): Объект с информацией о пользователе.
- `product_id` (int): Идентификатор товара.
- `price` (str): Цена товара.

**Возвращает**:
- `None`: Функция не возвращает значения.

### `send_robocassa_invoice`

**Описание**:
Отправляет пользователю ссылку на оплату через Robokassa.

**Параметры**:
- `call` (CallbackQuery): Объект callback-запроса.
- `user_info` (User): Объект с информацией о пользователе.
- `product_id` (int): Идентификатор товара.
- `price` (str): Цена товара.
- `session` (AsyncSession): Асинхронная сессия базы данных.

**Возвращает**:
- `None`: Функция не возвращает значения.

### `send_stars_invoice`

**Описание**:
Отправляет пользователю инвойс для оплаты звездами.

**Параметры**:
- `call` (CallbackQuery): Объект callback-запроса.
- `user_info` (User): Объект с информацией о пользователе.
- `product_id` (int): Идентификатор товара.
- `stars_price` (int): Цена в звездах.

**Возвращает**:
- `None`: Функция не возвращает значения.

### `pre_checkout_query`

**Описание**:
Обрабатывает pre-checkout query перед подтверждением оплаты.

**Параметры**:
- `pre_checkout_q` (PreCheckoutQuery): Объект pre-checkout query.

**Возвращает**:
- `None`: Функция не возвращает значения.

### `successful_payment`

**Описание**:
Обрабатывает успешное завершение оплаты.

**Параметры**:
- `message` (Message): Объект сообщения.
- `session_with_commit` (AsyncSession): Асинхронная сессия базы данных с возможностью коммита.

**Возвращает**:
- `None`: Функция не возвращает значения.