# Модуль `catalog_router.py`

## Обзор

Модуль `catalog_router.py` предназначен для обработки запросов, связанных с каталогом товаров в Telegram-боте. Он содержит набор обработчиков callback-запросов и сообщений, которые позволяют пользователям просматривать категории товаров, информацию о товарах и совершать покупки через различные платежные системы.

## Подробней

Этот модуль играет ключевую роль в навигации пользователей по каталогу товаров, отображении информации о товарах и организации процесса оплаты. Он интегрирован с базой данных для получения информации о категориях и товарах, а также взаимодействует с платежными системами, такими как ЮKassa, Robocassa и Stars.

## Функции

### `page_catalog`

```python
async def page_catalog(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, представляющий запрос обратного вызова от пользователя.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для работы с базой данных без автоматической фиксации изменений.

    Returns:
        None

    Raises:
        Exception: Если не удается удалить предыдущее сообщение (например, если оно отсутствует).
    """
```

**Описание**: Обработчик callback-запроса `catalog`. Отвечает за отображение каталога товаров, запрашивая список категорий из базы данных и отправляя пользователю сообщение с кнопками для выбора категории.

**Параметры**:
- `call` (CallbackQuery): Объект CallbackQuery, содержащий информацию о callback-запросе.
- `session_without_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.

**Пример**:

```python
# Пример вызова функции (не отображается в реальном коде, вызывается через CallbackQuery)
# await page_catalog(call, session_without_commit)
```

### `page_catalog_products`

```python
async def page_catalog_products(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, представляющий запрос обратного вызова от пользователя.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для работы с базой данных без автоматической фиксации изменений.

    Returns:
        None
    """
```

**Описание**: Обработчик callback-запросов, начинающихся с `category_`. Отображает список товаров, принадлежащих к выбранной категории.

**Параметры**:
- `call` (CallbackQuery): Объект CallbackQuery, содержащий информацию о callback-запросе.
- `session_without_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.

**Пример**:

```python
# Пример вызова функции (не отображается в реальном коде, вызывается через CallbackQuery)
# await page_catalog_products(call, session_without_commit)
```

### `process_about`

```python
async def process_about(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект CallbackQuery, представляющий запрос обратного вызова от пользователя.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для работы с базой данных без автоматической фиксации изменений.

    Returns:
        None
    """
```

**Описание**: Обработчик callback-запросов, начинающихся с `buy_`.  Инициирует процесс покупки товара в зависимости от выбранного типа оплаты.

**Параметры**:
- `call` (CallbackQuery): Объект CallbackQuery, содержащий информацию о callback-запросе.
- `session_without_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.

**Пример**:

```python
# Пример вызова функции (не отображается в реальном коде, вызывается через CallbackQuery)
# await process_about(call, session_without_commit)
```

### `send_yukassa_invoice`

```python
async def send_yukassa_invoice(call, user_info, product_id, price):
    """
    Args:
        call: Объект CallbackQuery, представляющий запрос обратного вызова от пользователя.
        user_info: Информация о пользователе.
        product_id: Идентификатор продукта.
        price: Цена продукта.

    Returns:
        None
    """
```

**Описание**: Отправляет пользователю инвойс для оплаты через ЮKassa.

**Параметры**:
- `call`: Объект CallbackQuery, содержащий информацию о callback-запросе.
- `user_info`: Информация о пользователе.
- `product_id`: Идентификатор продукта.
- `price`: Цена продукта.

**Пример**:

```python
# Пример вызова функции
# await send_yukassa_invoice(call, user_info, product_id, price)
```

### `send_robocassa_invoice`

```python
async def send_robocassa_invoice(call, user_info, product_id, price, session: AsyncSession):
    """
    Args:
        call: Объект CallbackQuery, представляющий запрос обратного вызова от пользователя.
        user_info: Информация о пользователе.
        product_id: Идентификатор продукта.
        price: Цена продукта.
        session (AsyncSession): Асинхровая сессия SQLAlchemy для работы с базой данных без автоматической фиксации изменений.

    Returns:
        None
    """
```

**Описание**: Отправляет пользователю ссылку для оплаты через Robocassa.

**Параметры**:
- `call`: Объект CallbackQuery, содержащий информацию о callback-запросе.
- `user_info`: Информация о пользователе.
- `product_id`: Идентификатор продукта.
- `price`: Цена продукта.
- `session` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.

**Пример**:

```python
# Пример вызова функции
# await send_robocassa_invoice(call, user_info, product_id, price, session)
```

### `send_stars_invoice`

```python
async def send_stars_invoice(call, user_info, product_id, stars_price):
    """
    Args:
        call: Объект CallbackQuery, представляющий запрос обратного вызова от пользователя.
        user_info: Информация о пользователе.
        product_id: Идентификатор продукта.
        stars_price: Цена продукта в звездах.

    Returns:
        None
    """
```

**Описание**: Отправляет пользователю инвойс для оплаты звездами.

**Параметры**:
- `call`: Объект CallbackQuery, представляющий запрос обратного вызова от пользователя.
- `user_info`: Информация о пользователе.
- `product_id`: Идентификатор продукта.
- `stars_price`: Цена продукта в звездах.

**Пример**:

```python
# Пример вызова функции
# await send_stars_invoice(call, user_info, product_id, stars_price)
```

### `pre_checkout_query`

```python
async def pre_checkout_query(pre_checkout_q: PreCheckoutQuery):
    """
    Args:
        pre_checkout_q (PreCheckoutQuery): Объект PreCheckoutQuery, содержащий информацию о предварительном запросе перед оплатой.

    Returns:
        None
    """
```

**Описание**: Обработчик предварительного запроса перед оплатой.

**Параметры**:
- `pre_checkout_q` (PreCheckoutQuery): Объект PreCheckoutQuery, содержащий информацию о предварительном запросе перед оплатой.

**Пример**:

```python
# Пример вызова функции (не отображается в реальном коде, вызывается через PreCheckoutQuery)
# await pre_checkout_query(pre_checkout_q)
```

### `successful_payment`

```python
async def successful_payment(message: Message, session_with_commit: AsyncSession):
    """
    Args:
        message (Message): Объект Message, содержащий информацию об успешной оплате.
        session_with_commit (AsyncSession): Асинхровая сессия SQLAlchemy для работы с базой данных с автоматической фиксацией изменений.

    Returns:
        None
    """
```

**Описание**: Обработчик события успешной оплаты. Выполняет логику после успешной оплаты, такую как предоставление доступа к купленному товару.

**Параметры**:
- `message` (Message): Объект Message, содержащий информацию об успешной оплате.
- `session_with_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных.

**Пример**:

```python
# Пример вызова функции (не отображается в реальном коде, вызывается при успешной оплате)
# await successful_payment(message, session_with_commit)