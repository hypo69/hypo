# Модуль утилит для работы с Robokassa

## Обзор

Модуль `utils.py` содержит набор функций для взаимодействия с платежной системой Robokassa. Он включает функции для генерации платежных ссылок, проверки подписи, обработки результатов оплаты и проверки успешности платежей. Модуль использует параметры из файла конфигурации `bot.config.settings`.

## Подробнее

Этот модуль играет важную роль в процессе интеграции с Robokassa, обеспечивая безопасное и надежное взаимодействие для проведения платежей. Функции модуля позволяют генерировать ссылки для оплаты, проверять подлинность ответов от Robokassa и обрабатывать результаты платежей.

## Функции

### `calculate_signature`

```python
def calculate_signature(login, cost, inv_id, password, user_id, user_telegram_id, product_id, is_result=False):
    """
    Вычисляет подпись для запросов к Robokassa.

    Args:
        login (str): Логин магазина в Robokassa.
        cost (float): Сумма платежа.
        inv_id (int): Номер заказа.
        password (str): Пароль магазина в Robokassa.
        user_id (int): ID пользователя.
        user_telegram_id (int): Telegram ID пользователя.
        product_id (int): ID продукта.
        is_result (bool, optional): Флаг, указывающий, является ли запрос результатом оплаты. По умолчанию `False`.

    Returns:
        str: MD5-хеш, представляющий подпись.

    Как работает функция:
    1. Определяется базовая строка для подписи в зависимости от флага `is_result`. Если `is_result` равен `True`, используется формат для URL результата, иначе — для начального URL и URL успеха.
    2. Создается словарь `additional_params` с дополнительными параметрами, такими как `user_id`, `user_telegram_id` и `product_id`.
    3. Параметры из `additional_params` сортируются по ключам и добавляются к базовой строке в формате `:{key}={value}`.
    4. Вычисляется MD5-хеш от полученной строки в кодировке UTF-8.
    5. Возвращается полученный хеш в виде строки.
    """
    ...
```

### `generate_payment_link`

```python
def generate_payment_link(cost: float, number: int, description: str,
                          user_id: int, user_telegram_id: int, product_id: int,
                          is_test=1, robokassa_payment_url='https://auth.robokassa.ru/Merchant/Index.aspx') -> str:
    """
    Генерирует ссылку для оплаты через Robokassa с обязательными параметрами.

    Args:
        cost (float): Стоимость товара.
        number (int): Номер заказа.
        description (str): Описание заказа.
        user_id (int): ID пользователя.
        user_telegram_id (int): Telegram ID пользователя.
        product_id (int): ID товара.
        is_test (int, optional): Флаг тестового режима (1 - тест, 0 - боевой режим). По умолчанию 1.
        robokassa_payment_url (str, optional): URL для оплаты Robokassa. По умолчанию 'https://auth.robokassa.ru/Merchant/Index.aspx'.

    Returns:
        str: Ссылка на страницу оплаты.

    Как работает функция:
    1. Вызывает функцию `calculate_signature` для генерации подписи на основе переданных параметров и настроек магазина.
    2. Создает словарь `data` с параметрами, необходимыми для формирования платежной ссылки, включая логин магазина, сумму, номер заказа, описание, подпись и дополнительные параметры пользователя и продукта.
    3. Формирует URL, объединяя базовый URL Robokassa и параметры из словаря `data`, закодированные с помощью `parse.urlencode`.
    4. Возвращает полученную ссылку для оплаты.
    """
    ...
```

### `parse_response`

```python
def parse_response(request: str) -> dict:
    """
    Разбирает строку запроса на параметры.

    Args:
        request (str): Строка запроса.

    Returns:
        dict: Словарь с параметрами.

    Как работает функция:
    1. Использует `urllib.parse.urlparse` для разбора URL из строки запроса.
    2. Извлекает строку запроса (query) из разобранного URL.
    3. Использует `urllib.parse.parse_qsl` для разбора строки запроса в список пар ключ-значение.
    4. Преобразует список пар ключ-значение в словарь и возвращает его.
    """
    ...
```

### `check_signature_result`

```python
def check_signature_result(out_sum, inv_id, received_signature, password, user_id, user_telegram_id, product_id) -> bool:
    """
    Проверяет подпись результата оплаты.

    Args:
        out_sum (float): Сумма платежа.
        inv_id (int): Номер заказа.
        received_signature (str): Полученная подпись.
        password (str): Пароль магазина в Robokassa.
        user_id (int): ID пользователя.
        user_telegram_id (int): Telegram ID пользователя.
        product_id (int): ID продукта.

    Returns:
        bool: `True`, если подпись верна, иначе `False`.

    Как работает функция:
    1. Вызывает функцию `calculate_signature` для генерации подписи на основе переданных параметров и пароля магазина. Важно, что флаг `is_result` установлен в `True`.
    2. Сравнивает сгенерированную подпись с полученной подписью, приводя обе строки к нижнему регистру для регистронезависимого сравнения.
    3. Возвращает `True`, если подписи совпадают, и `False` в противном случае.
    """
    ...
```

### `result_payment`

```python
def result_payment(request: str) -> str:
    """
    Обрабатывает результат оплаты (ResultURL).

    Args:
        request (str): Строка запроса с параметрами оплаты.

    Returns:
        str: 'OK' + номер заказа, если оплата прошла успешно, иначе 'bad sign'.

    Как работает функция:
    1. Извлекает параметры из строки запроса с помощью функции `parse_response`.
    2. Получает значения `out_sum`, `inv_id`, `signature`, `user_id`, `user_telegram_id` и `product_id` из извлеченных параметров.
    3. Вызывает функцию `check_signature_result` для проверки подписи результата оплаты. Используется второй пароль магазина (`settings.MRH_PASS_2`).
    4. Если подпись верна, возвращает строку 'OK' + номер заказа (`inv_id`).
    5. Если подпись неверна, возвращает строку "bad sign".
    """
    ...
```

### `check_success_payment`

```python
def check_success_payment(request: str) -> str:
    """
    Проверяет успешность оплаты (SuccessURL).

    Args:
        request (str): Строка запроса с параметрами оплаты.

    Returns:
        str: Сообщение об успешной оплате или 'bad sign' при неверной подписи.

    Как работает функция:
    1. Извлекает параметры из строки запроса с помощью функции `parse_response`.
    2. Получает значения `out_sum`, `inv_id`, `signature`, `user_id`, `user_telegram_id` и `product_id` из извлеченных параметров.
    3. Вызывает функцию `check_signature_result` для проверки подписи. Используется первый пароль магазина (`settings.MRH_PASS_1`).
    4. Если подпись верна, возвращает сообщение "Thank you for using our service".
    5. Если подпись неверна, возвращает строку "bad sign".
    """
    ...