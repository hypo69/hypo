# Модуль `catalog_router`

## Обзор

Модуль `catalog_router` предназначен для обработки запросов, связанных с каталогом товаров в Telegram-боте. Он включает в себя обработку запросов на отображение каталога, выбор категорий товаров и организацию процесса покупки.

## Подробней

Данный модуль является частью логики Telegram-бота, отвечающей за взаимодействие с пользователем в процессе выбора и покупки товаров. Он использует библиотеку `aiogram` для обработки входящих запросов и `sqlalchemy` для взаимодействия с базой данных. Логика модуля включает в себя отображение каталога товаров, обработку выбора категории, отображение товаров в выбранной категории и организацию процесса оплаты через различные платежные системы, такие как ЮKassa, Robocassa и Stars.

## Классы

В данном модуле классы отсутствуют.

## Функции

### `page_catalog`

```python
async def page_catalog(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обрабатывает запрос на отображение каталога товаров.

    Args:
        call (CallbackQuery): Объект обратного вызова от Telegram.
        session_without_commit (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных без коммита.

    Returns:
        None

    Raises:
        Exception: Обрабатывает исключения при удалении предыдущего сообщения.

    Как работает функция:
    1. Отвечает на обратный вызов сообщением "Загрузка каталога...".
    2. Пытается удалить предыдущее сообщение пользователя.
    3. Получает данные каталога из базы данных с использованием `CategoryDao.find_all`.
    4. Отправляет пользователю сообщение с категориями товаров, используя клавиатуру `catalog_kb`.
    """
```

**Описание**: Обрабатывает запрос на отображение каталога товаров.

**Параметры**:
- `call` (CallbackQuery): Объект обратного вызова от Telegram.
- `session_without_commit` (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных без коммита.

**Возвращает**: None

**Вызывает исключения**: Exception: Обрабатывает исключения при удалении предыдущего сообщения.

**Примеры**:
```python
# Пример вызова (в контексте aiogram handler)
# @catalog_router.callback_query(F.data == "catalog")
# async def handler(call: CallbackQuery, session_without_commit: AsyncSession):
#     await page_catalog(call, session_without_commit)
```

### `page_catalog_products`

```python
async def page_catalog_products(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обрабатывает запрос на отображение товаров в выбранной категории.

    Args:
        call (CallbackQuery): Объект обратного вызова от Telegram.
        session_without_commit (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных без коммита.

    Returns:
        None

    Как работает функция:
    1. Извлекает идентификатор категории из данных обратного вызова.
    2. Получает список товаров в выбранной категории из базы данных с использованием `ProductDao.find_all`.
    3. Если товары найдены, отправляет пользователю сообщение с информацией о каждом товаре, используя клавиатуру `product_kb`.
    4. Если товары не найдены, отправляет пользователю сообщение об отсутствии товаров в данной категории.
    """
```

**Описание**: Обрабатывает запрос на отображение товаров в выбранной категории.

**Параметры**:
- `call` (CallbackQuery): Объект обратного вызова от Telegram.
- `session_without_commit` (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных без коммита.

**Возвращает**: None

**Примеры**:
```python
# Пример вызова (в контексте aiogram handler)
# @catalog_router.callback_query(F.data.startswith("category_"))
# async def handler(call: CallbackQuery, session_without_commit: AsyncSession):
#     await page_catalog_products(call, session_without_commit)
```

### `process_about`

```python
async def process_about(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обрабатывает запрос на покупку товара.

    Args:
        call (CallbackQuery): Объект обратного вызова от Telegram.
        session_without_commit (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных без коммита.

    Returns:
        None

    Как работает функция:
    1. Получает информацию о пользователе из базы данных с использованием `UserDAO.find_one_or_none`.
    2. Извлекает тип платежа, идентификатор товара и цену из данных обратного вызова.
    3. В зависимости от типа платежа вызывает соответствующую функцию для организации оплаты (ЮKassa, Stars или Robocassa).
    4. Удаляет предыдущее сообщение пользователя.
    """
```

**Описание**: Обрабатывает запрос на покупку товара.

**Параметры**:
- `call` (CallbackQuery): Объект обратного вызова от Telegram.
- `session_without_commit` (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных без коммита.

**Возвращает**: None

**Примеры**:
```python
# Пример вызова (в контексте aiogram handler)
# @catalog_router.callback_query(F.data.startswith('buy_'))
# async def handler(call: CallbackQuery, session_without_commit: AsyncSession):
#     await process_about(call, session_without_commit)
```

### `send_yukassa_invoice`

```python
async def send_yukassa_invoice(call, user_info, product_id, price):
    """
    Отправляет пользователю инвойс для оплаты через ЮKassa.

    Args:
        call (CallbackQuery): Объект обратного вызова от Telegram.
        user_info: Информация о пользователе.
        product_id: Идентификатор товара.
        price: Цена товара.

    Returns:
        None

    Как работает функция:
    1. Отправляет инвойс пользователю с использованием `bot.send_invoice`.
    2. Указывает параметры платежа, такие как название, описание, payload, токен провайдера, валюта и цена.
    3. Добавляет клавиатуру с кнопкой для оплаты через ЮKassa.
    """
```

**Описание**: Отправляет пользователю инвойс для оплаты через ЮKassa.

**Параметры**:
- `call` (CallbackQuery): Объект обратного вызова от Telegram.
- `user_info`: Информация о пользователе.
- `product_id`: Идентификатор товара.
- `price`: Цена товара.

**Возвращает**: None

**Примеры**:
```python
# Пример вызова
# await send_yukassa_invoice(call, user_info, product_id, price)
```

### `send_robocassa_invoice`

```python
async def send_robocassa_invoice(call, user_info, product_id, price, session: AsyncSession):
    """
    Отправляет пользователю ссылку для оплаты через Robocassa.

    Args:
        call (CallbackQuery): Объект обратного вызова от Telegram.
        user_info: Информация о пользователе.
        product_id: Идентификатор товара.
        price: Цена товара.
        session (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных.

    Returns:
        None

    Как работает функция:
    1. Получает следующий идентификатор для покупки из базы данных с использованием `PurchaseDao.get_next_id`.
    2. Генерирует ссылку для оплаты с использованием `generate_payment_link`.
    3. Отправляет пользователю сообщение с ссылкой на оплату, используя клавиатуру `get_product_buy_robocassa`.
    """
```

**Описание**: Отправляет пользователю ссылку для оплаты через Robocassa.

**Параметры**:
- `call` (CallbackQuery): Объект обратного вызова от Telegram.
- `user_info`: Информация о пользователе.
- `product_id`: Идентификатор товара.
- `price`: Цена товара.
- `session (AsyncSession)`: Асинхронная сессия SQLAlchemy для работы с базой данных.

**Возвращает**: None

**Примеры**:
```python
# Пример вызова
# await send_robocassa_invoice(call, user_info, product_id, price, session)
```

### `send_stars_invoice`

```python
async def send_stars_invoice(call, user_info, product_id, stars_price):
    """
    Отправляет пользователю инвойс для оплаты звездами.

    Args:
        call (CallbackQuery): Объект обратного вызова от Telegram.
        user_info: Информация о пользователе.
        product_id: Идентификатор товара.
        stars_price: Цена товара в звездах.

    Returns:
        None

    Как работает функция:
    1. Отправляет инвойс пользователю с использованием `bot.send_invoice`.
    2. Указывает параметры платежа, такие как название, описание, payload, валюта и цена в звездах.
    3. Добавляет клавиатуру с кнопкой для оплаты звездами.
    """
```

**Описание**: Отправляет пользователю инвойс для оплаты звездами.

**Параметры**:
- `call` (CallbackQuery): Объект обратного вызова от Telegram.
- `user_info`: Информация о пользователе.
- `product_id`: Идентификатор товара.
- `stars_price`: Цена товара в звездах.

**Возвращает**: None

**Примеры**:
```python
# Пример вызова
# await send_stars_invoice(call, user_info, product_id, stars_price)
```

### `pre_checkout_query`

```python
async def pre_checkout_query(pre_checkout_q: PreCheckoutQuery):
    """
    Обрабатывает предварительный запрос на подтверждение оплаты.

    Args:
        pre_checkout_q (PreCheckoutQuery): Объект предварительного запроса на оплату от Telegram.

    Returns:
        None

    Как работает функция:
    1. Подтверждает запрос на оплату, отправляя `ok=True` с использованием `bot.answer_pre_checkout_query`.
    """
```

**Описание**: Обрабатывает предварительный запрос на подтверждение оплаты.

**Параметры**:
- `pre_checkout_q` (PreCheckoutQuery): Объект предварительного запроса на оплату от Telegram.

**Возвращает**: None

**Примеры**:
```python
# Пример вызова (в контексте aiogram handler)
# @catalog_router.pre_checkout_query(lambda query: True)
# async def handler(pre_checkout_q: PreCheckoutQuery):
#     await pre_checkout_query(pre_checkout_q)
```

### `successful_payment`

```python
async def successful_payment(message: Message, session_with_commit: AsyncSession):
    """
    Обрабатывает успешное завершение оплаты.

    Args:
        message (Message): Объект сообщения от Telegram.
        session_with_commit (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных с коммитом.

    Returns:
        None

    Как работает функция:
    1. Извлекает информацию о платеже из сообщения.
    2. Определяет тип платежа и цену.
    3. Формирует словарь с данными о платеже.
    4. Вызывает функцию `successful_payment_logic` для обработки логики успешной оплаты.
    """
```

**Описание**: Обрабатывает успешное завершение оплаты.

**Параметры**:
- `message` (Message): Объект сообщения от Telegram.
- `session_with_commit` (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных с коммитом.

**Возвращает**: None

**Примеры**:
```python
# Пример вызова (в контексте aiogram handler)
# @catalog_router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
# async def handler(message: Message, session_with_commit: AsyncSession):
#     await successful_payment(message, session_with_commit)