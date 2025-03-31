# Модуль для работы с каталогом товаров в Telegram боте

## Обзор

Модуль `catalog_router.py` предназначен для организации работы с каталогом товаров в Telegram боте. Он включает в себя обработку запросов пользователей на просмотр каталога, выбор категорий товаров, отображение информации о товарах и проведение оплаты через различные платежные системы (ЮKassa, Robocassa, Stars). Модуль использует библиотеку `aiogram` для работы с Telegram API, `sqlalchemy` для взаимодействия с базой данных и другие вспомогательные модули для генерации платежных ссылок и формирования клавиатур.

## Подробней

Этот модуль является ключевым компонентом Telegram-бота, отвечающим за взаимодействие с пользователем в процессе выбора и покупки товаров. Он обрабатывает запросы на просмотр каталога, отображает товары в выбранной категории, предоставляет информацию о товаре и предлагает различные способы оплаты. Модуль интегрирован с платежными системами ЮKassa, Robocassa и Stars, обеспечивая удобный и безопасный процесс оплаты для пользователей.

## Классы

В данном модуле классы отсутствуют.

## Функции

### `page_catalog`

```python
async def page_catalog(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Отображает каталог товаров.

    Args:
        call (CallbackQuery): Объект обратного вызова от Telegram.
        session_without_commit (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных (без коммита изменений).

    Returns:
        None

    Raises:
        Exception: В случае ошибки при удалении предыдущего сообщения пользователя.

    Example:
        Пример использования:
        (Предполагается, что `call` и `session_without_commit` уже инициализированы)
        >>> await page_catalog(call, session_without_commit)
    """
```

**Как работает функция**:
1. Отвечает на обратный вызов сообщением "Загрузка каталога...".
2. Пытается удалить предыдущее сообщение пользователя, чтобы избежать нагромождения сообщений в чате.
3. Извлекает данные каталога (категории товаров) из базы данных с использованием `CategoryDao.find_all`.
4. Отправляет пользователю сообщение со списком категорий товаров, используя клавиатуру, сформированную функцией `catalog_kb`.

### `page_catalog_products`

```python
async def page_catalog_products(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Отображает товары выбранной категории.

    Args:
        call (CallbackQuery): Объект обратного вызова от Telegram.
        session_without_commit (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных (без коммита изменений).

    Returns:
        None

    Raises:
        None

    Example:
        Пример использования:
        (Предполагается, что `call` и `session_without_commit` уже инициализированы)
        >>> await page_catalog_products(call, session_without_commit)
    """
```

**Как работает функция**:

1. Извлекает `category_id` из данных обратного вызова (`call.data`).
2. Получает список товаров, принадлежащих указанной категории, из базы данных с использованием `ProductDao.find_all` и фильтра `ProductCategoryIDModel`.
3. Проверяет количество товаров в категории.
4. Если товары есть, отправляет пользователю сообщение с информацией о каждом товаре, включая название, цену, описание и клавиатуру для покупки (`product_kb`).
5. Если товаров нет, отправляет пользователю сообщение "В данной категории нет товаров.".

### `process_about`

```python
async def process_about(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обрабатывает выбор способа оплаты товара.

    Args:
        call (CallbackQuery): Объект обратного вызова от Telegram.
        session_without_commit (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных (без коммита изменений).

    Returns:
        None

    Raises:
        None

    Example:
        Пример использования:
        (Предполагается, что `call` и `session_without_commit` уже инициализированы)
        >>> await process_about(call, session_without_commit)
    """
```

**Как работает функция**:

1. Извлекает информацию о пользователе из базы данных с использованием `UserDAO.find_one_or_none`.
2. Извлекает тип оплаты (`payment_type`), ID продукта (`product_id`) и цену (`price`) из данных обратного вызова (`call.data`).
3. В зависимости от типа оплаты вызывает соответствующую функцию для отправки инвойса (счета) на оплату:
   - `send_yukassa_invoice` для ЮKassa.
   - `send_stars_invoice` для Stars.
   - `send_robocassa_invoice` для Robocassa.
4. Удаляет предыдущее сообщение пользователя.

### `send_yukassa_invoice`

```python
async def send_yukassa_invoice(call, user_info, product_id, price):
    """
    Отправляет инвойс для оплаты через ЮKassa.

    Args:
        call (CallbackQuery): Объект обратного вызова от Telegram.
        user_info: Информация о пользователе.
        product_id: ID товара.
        price: Цена товара.

    Returns:
        None

    Raises:
        None

    Example:
        Пример использования:
        (Предполагается, что `call`, `user_info`, `product_id` и `price` уже инициализированы)
        >>> await send_yukassa_invoice(call, user_info, product_id, price)
    """
```

**Как работает функция**:

1. Отправляет инвойс (счет) пользователю через Telegram API с использованием `bot.send_invoice`.
2. Формирует заголовок и описание инвойса на основе цены товара.
3. Устанавливает `payload` для инвойса, содержащий информацию о типе оплаты, ID пользователя и ID продукта.
4. Устанавливает `provider_token` для ЮKassa.
5. Устанавливает валюту инвойса в рубли (`rub`).
6. Формирует список цен (`prices`) с указанием стоимости товара.
7. Устанавливает клавиатуру для покупки товара через ЮKassa (`get_product_buy_youkassa`).

### `send_robocassa_invoice`

```python
async def send_robocassa_invoice(call, user_info, product_id, price, session: AsyncSession):
    """
    Отправляет ссылку для оплаты через Robocassa.

    Args:
        call (CallbackQuery): Объект обратного вызова от Telegram.
        user_info: Информация о пользователе.
        product_id: ID товара.
        price: Цена товара.
        session (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных.

    Returns:
        None

    Raises:
        None

    Example:
        Пример использования:
        (Предполагается, что `call`, `user_info`, `product_id`, `price` и `session` уже инициализированы)
        >>> await send_robocassa_invoice(call, user_info, product_id, price, session)
    """
```

**Как работает функция**:

1. Получает следующий доступный ID для покупки из базы данных с использованием `PurchaseDao.get_next_id`.
2. Формирует текст и описание для платежа на основе цены товара и ID пользователя.
3. Генерирует платежную ссылку с использованием функции `generate_payment_link`, передавая необходимые параметры (стоимость, ID платежа, описание, ID пользователя, ID пользователя Telegram, ID продукта).
4. Формирует клавиатуру для покупки товара через Robocassa (`get_product_buy_robocassa`), передавая цену товара и платежную ссылку.
5. Отправляет пользователю сообщение с текстом и клавиатурой для оплаты.

### `send_stars_invoice`

```python
async def send_stars_invoice(call, user_info, product_id, stars_price):
    """
    Отправляет инвойс для оплаты через Stars.

    Args:
        call (CallbackQuery): Объект обратного вызова от Telegram.
        user_info: Информация о пользователе.
        product_id: ID товара.
        stars_price: Цена товара в звездах.

    Returns:
        None

    Raises:
        None

    Example:
        Пример использования:
        (Предполагается, что `call`, `user_info`, `product_id` и `stars_price` уже инициализированы)
        >>> await send_stars_invoice(call, user_info, product_id, stars_price)
    """
```

**Как работает функция**:

1. Отправляет инвойс (счет) пользователю через Telegram API с использованием `bot.send_invoice`.
2. Формирует заголовок и описание инвойса на основе цены товара в звездах.
3. Устанавливает `payload` для инвойса, содержащий информацию о типе оплаты, ID пользователя и ID продукта.
4. Валюта `XTR`.
5. Формирует список цен (`prices`) с указанием стоимости товара в звездах.
6. Устанавливает клавиатуру для покупки товара через Stars (`get_product_buy_stars`).

### `pre_checkout_query`

```python
async def pre_checkout_query(pre_checkout_q: PreCheckoutQuery):
    """
    Обрабатывает предварительный запрос перед оплатой.

    Args:
        pre_checkout_q (PreCheckoutQuery): Объект предварительного запроса от Telegram.

    Returns:
        None

    Raises:
        None

    Example:
        Пример использования:
        (Предполагается, что `pre_checkout_q` уже инициализирован)
        >>> await pre_checkout_query(pre_checkout_q)
    """
```

**Как работает функция**:

1. Отвечает на предварительный запрос перед оплатой, подтверждая возможность проведения оплаты (`ok=True`).

### `successful_payment`

```python
async def successful_payment(message: Message, session_with_commit: AsyncSession):
    """
    Обрабатывает успешную оплату.

    Args:
        message (Message): Объект сообщения от Telegram.
        session_with_commit (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных (с возможностью коммита изменений).

    Returns:
        None

    Raises:
        None

    Example:
        Пример использования:
        (Предполагается, что `message` и `session_with_commit` уже инициализированы)
        >>> await successful_payment(message, session_with_commit)
    """
```

**Как работает функция**:

1. Извлекает информацию об оплате из объекта сообщения (`message.successful_payment`).
2. Извлекает тип оплаты (`payment_type`), ID пользователя (`user_id`) и ID продукта (`product_id`) из `invoice_payload`.
3. Определяет цену и валюту в зависимости от типа оплаты.
4. Формирует словарь `payment_data` с информацией об оплате.
5. Вызывает функцию `successful_payment_logic` для обработки логики успешной оплаты, передавая необходимые параметры (сессию, данные об оплате, валюту, ID пользователя Telegram, бота).