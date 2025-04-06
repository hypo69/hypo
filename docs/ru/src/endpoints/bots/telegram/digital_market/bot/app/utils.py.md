# Модуль для работы с Robokassa
=================================================

Модуль содержит функции для генерации платежных ссылок Robokassa, проверки подписи и обработки ответов от Robokassa.
Этот модуль используется для интеграции с платежной системой Robokassa в Telegram боте для цифрового рынка.

## Оглавление
- [Обзор](#обзор)
- [Функции](#функции)
    - [calculate_signature](#calculate_signature)
    - [generate_payment_link](#generate_payment_link)
    - [parse_response](#parse_response)
    - [check_signature_result](#check_signature_result)
    - [result_payment](#result_payment)
    - [check_success_payment](#check_success_payment)

## Обзор

Этот модуль предоставляет набор функций для работы с платежной системой Robokassa. Он включает в себя:

- Генерацию подписи для запросов к Robokassa.
- Формирование платежной ссылки для оплаты.
- Разбор ответа от Robokassa.
- Проверку подписи ответа Robokassa.
- Обработку результата оплаты.
- Проверку успешности оплаты.

Эти функции позволяют безопасно и надежно интегрировать платежную систему Robokassa в Telegram бот для цифрового рынка.

## Функции

### `calculate_signature`

```python
def calculate_signature(login, cost, inv_id, password, user_id, user_telegram_id, product_id, is_result=False):
    """
    Вычисляет подпись для запросов к Robokassa.

    Args:
        login: Логин магазина в Robokassa.
        cost: Сумма платежа.
        inv_id: Номер заказа.
        password: Пароль магазина в Robokassa.
        user_id: ID пользователя.
        user_telegram_id: Telegram ID пользователя.
        product_id: ID товара.
        is_result (bool): Флаг, указывающий, что подпись вычисляется для Result URL. По умолчанию `False`.

    Returns:
        str: Вычисленная подпись в формате MD5.
    """
    ...
```

**Назначение**: Вычисляет MD5-хеш подписи для формирования запросов и проверки ответов от Robokassa.

**Параметры**:
- `login`: Логин магазина в Robokassa (тип не указан).
- `cost`: Сумма платежа (тип не указан).
- `inv_id`: Номер заказа (тип не указан).
- `password`: Пароль магазина в Robokassa (тип не указан).
- `user_id`: ID пользователя (тип не указан).
- `user_telegram_id`: Telegram ID пользователя (тип не указан).
- `product_id`: ID товара (тип не указан).
- `is_result` (bool): Флаг, указывающий, что подпись вычисляется для Result URL. По умолчанию `False`.

**Возвращает**:
- `str`: Вычисленная подпись в формате MD5.

**Как работает функция**:

1.  Формирует базовую строку для вычисления подписи в зависимости от значения `is_result`. Если `is_result` равен `True`, то используется формат для Result URL, иначе - для initial и Success URL.
2.  Создает словарь `additional_params`, содержащий идентификаторы пользователя, Telegram ID пользователя и ID продукта.
3.  Сортирует элементы словаря `additional_params` по ключам и добавляет их к базовой строке в формате `:{key}={value}`.
4.  Вычисляет MD5-хеш от полученной строки в кодировке UTF-8 и возвращает его в шестнадцатеричном формате.

**Примеры**:
```python
login = "test_login"
cost = 100.00
inv_id = 123
password = "test_password"
user_id = 1
user_telegram_id = 123456789
product_id = 10

signature_initial = calculate_signature(login, cost, inv_id, password, user_id, user_telegram_id, product_id)
print(f"Подпись для initial URL: {signature_initial}")

signature_result = calculate_signature(login, cost, inv_id, password, user_id, user_telegram_id, product_id, is_result=True)
print(f"Подпись для result URL: {signature_result}")

```

### `generate_payment_link`

```python
def generate_payment_link(cost: float, number: int, description: str,
                          user_id: int, user_telegram_id: int, product_id: int,
                          is_test=1, robokassa_payment_url='https://auth.robokassa.ru/Merchant/Index.aspx') -> str:
    """
    Генерирует ссылку для оплаты через Robokassa с обязательными параметрами.

    Args:
        cost (float): Стоимость товара
        number (int): Номер заказа
        description (str): Описание заказа
        user_id (int): ID пользователя
        user_telegram_id (int): Telegram ID пользователя
        product_id (int): ID товара
        is_test (int): Флаг тестового режима (1 - тест, 0 - боевой режим)
        robokassa_payment_url (str): URL для оплаты Robokassa

    Returns:
        str: Ссылка на страницу оплаты
    """
    ...
```

**Назначение**: Генерирует ссылку для оплаты через Robokassa с заданными параметрами.

**Параметры**:
- `cost` (float): Стоимость товара.
- `number` (int): Номер заказа.
- `description` (str): Описание заказа.
- `user_id` (int): ID пользователя.
- `user_telegram_id` (int): Telegram ID пользователя.
- `product_id` (int): ID товара.
- `is_test` (int): Флаг тестового режима (1 - тест, 0 - боевой режим). По умолчанию `1`.
- `robokassa_payment_url` (str): URL для оплаты Robokassa. По умолчанию `'https://auth.robokassa.ru/Merchant/Index.aspx'`.

**Возвращает**:
- `str`: Ссылка на страницу оплаты.

**Как работает функция**:

1.  Вычисляет подпись с использованием функции `calculate_signature` и передает необходимые параметры, включая логин магазина, пароль и идентификаторы пользователя и продукта.
2.  Формирует словарь `data`, содержащий параметры для запроса к Robokassa, такие как логин магазина, сумма платежа, номер заказа, описание, подпись, флаг тестового режима и идентификаторы пользователя и продукта.
3.  Кодирует параметры из словаря `data` в строку запроса с помощью `parse.urlencode`.
4.  Формирует и возвращает полную ссылку для оплаты, объединяя базовый URL Robokassa и строку запроса.

**Примеры**:
```python
cost = 100.00
number = 123
description = "Описание заказа"
user_id = 1
user_telegram_id = 123456789
product_id = 10
is_test = 1
robokassa_payment_url = 'https://auth.robokassa.ru/Merchant/Index.aspx'

payment_link = generate_payment_link(cost, number, description, user_id, user_telegram_id, product_id, is_test, robokassa_payment_url)
print(f"Ссылка для оплаты: {payment_link}")
```

### `parse_response`

```python
def parse_response(request: str) -> dict:
    """
    Разбирает строку запроса на параметры.

    Args:
        request (str): Строка запроса

    Returns:
        dict: Словарь с параметрами
    """
    ...
```

**Назначение**: Разбирает строку запроса на параметры и возвращает их в виде словаря.

**Параметры**:
- `request` (str): Строка запроса.

**Возвращает**:
- `dict`: Словарь с параметрами.

**Как работает функция**:

1.  Использует `urllib.parse.urlparse` для разбора URL из строки запроса.
2.  Извлекает строку запроса (query) из разобранного URL.
3.  Использует `urllib.parse.parse_qsl` для разбора строки запроса в список кортежей (ключ, значение).
4.  Преобразует список кортежей в словарь и возвращает его.

**Примеры**:
```python
request = "https://example.com/payment?OutSum=100.00&InvId=123&SignatureValue=test_signature"
params = parse_response(request)
print(f"Параметры запроса: {params}")
```

### `check_signature_result`

```python
def check_signature_result(out_sum, inv_id, received_signature, password, user_id, user_telegram_id, product_id) -> bool:
    """
    Проверяет подпись результата оплаты.

    Args:
        out_sum: Сумма платежа.
        inv_id: Номер заказа.
        received_signature: Полученная подпись.
        password: Пароль магазина.
        user_id: ID пользователя.
        user_telegram_id: Telegram ID пользователя.
        product_id: ID товара.

    Returns:
        bool: True, если подпись верна, иначе False.
    """
    ...
```

**Назначение**: Проверяет подпись результата оплаты, сравнивая вычисленную подпись с полученной.

**Параметры**:
- `out_sum`: Сумма платежа (тип не указан).
- `inv_id`: Номер заказа (тип не указан).
- `received_signature`: Полученная подпись (тип не указан).
- `password`: Пароль магазина (тип не указан).
- `user_id`: ID пользователя (тип не указан).
- `user_telegram_id`: Telegram ID пользователя (тип не указан).
- `product_id`: ID товара (тип не указан).

**Возвращает**:
- `bool`: `True`, если подпись верна, иначе `False`.

**Как работает функция**:

1.  Вычисляет подпись с использованием функции `calculate_signature` и параметром `is_result=True`, что указывает на вычисление подписи для Result URL.
2.  Сравнивает вычисленную подпись с полученной подписью `received_signature`, приводя обе подписи к нижнему регистру для регистронезависимого сравнения.
3.  Возвращает `True`, если подписи совпадают, и `False` в противном случае.

**Примеры**:
```python
out_sum = "100.00"
inv_id = "123"
received_signature = "test_signature"
password = "test_password"
user_id = "1"
user_telegram_id = "123456789"
product_id = "10"

is_signature_valid = check_signature_result(out_sum, inv_id, received_signature, password, user_id, user_telegram_id, product_id)
print(f"Подпись верна: {is_signature_valid}")
```

### `result_payment`

```python
def result_payment(request: str) -> str:
    """
    Обрабатывает результат оплаты (ResultURL).

    Args:
        request (str): Строка запроса с параметрами оплаты

    Returns:
        str: 'OK' + номер заказа, если оплата прошла успешно, иначе 'bad sign'
    """
    ...
```

**Назначение**: Обрабатывает результат оплаты, полученный через ResultURL от Robokassa, и проверяет подпись.

**Параметры**:
- `request` (str): Строка запроса с параметрами оплаты.

**Возвращает**:
- `str`: `'OK' + номер заказа`, если оплата прошла успешно, иначе `'bad sign'`.

**Как работает функция**:

1.  Разбирает строку запроса `request` с использованием функции `parse_response` и получает словарь параметров.
2.  Извлекает параметры `OutSum`, `InvId`, `SignatureValue`, `Shp_user_id`, `Shp_user_telegram_id` и `Shp_product_id` из словаря параметров.
3.  Вызывает функцию `check_signature_result` для проверки подписи, передавая необходимые параметры, включая пароль магазина, полученный из настроек (`settings.MRH_PASS_2`).
4.  Если подпись верна, возвращает строку `'OK' + номер заказа` (InvId), иначе возвращает строку `"bad sign"`.

**Примеры**:
```python
request = "https://example.com/result?OutSum=100.00&InvId=123&SignatureValue=test_signature&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=10"
payment_result = result_payment(request)
print(f"Результат оплаты: {payment_result}")
```

### `check_success_payment`

```python
def check_success_payment(request: str) -> str:
    """
    Проверяет успешность оплаты (SuccessURL).

    Args:
        request (str): Строка запроса с параметрами оплаты

    Returns:
        str: Сообщение об успешной оплате или 'bad sign' при неверной подписи
    """
    ...
```

**Назначение**: Проверяет успешность оплаты, полученной через SuccessURL от Robokassa, и проверяет подпись.

**Параметры**:
- `request` (str): Строка запроса с параметрами оплаты.

**Возвращает**:
- `str`: Сообщение об успешной оплате (`"Thank you for using our service"`) или `'bad sign'` при неверной подписи.

**Как работает функция**:

1.  Разбирает строку запроса `request` с использованием функции `parse_response` и получает словарь параметров.
2.  Извлекает параметры `OutSum`, `InvId`, `SignatureValue`, `Shp_user_id`, `Shp_user_telegram_id` и `Shp_product_id` из словаря параметров.
3.  Вызывает функцию `check_signature_result` для проверки подписи, передавая необходимые параметры, включая пароль магазина, полученный из настроек (`settings.MRH_PASS_1`).
4.  Если подпись верна, возвращает строку `"Thank you for using our service"`, иначе возвращает строку `"bad sign"`.

**Примеры**:
```python
request = "https://example.com/success?OutSum=100.00&InvId=123&SignatureValue=test_signature&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=10"
payment_success = check_success_payment(request)
print(f"Результат проверки успешности оплаты: {payment_success}")