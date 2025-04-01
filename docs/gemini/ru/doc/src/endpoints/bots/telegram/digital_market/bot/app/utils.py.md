# Модуль utils.py для работы с Robokassa

## Обзор

Модуль `utils.py` предоставляет набор функций для генерации платежных ссылок Robokassa, проверки подписи и обработки ответов от Robokassa. Этот модуль используется для интеграции с платежной системой Robokassa в боте Telegram для цифрового рынка.

## Подробней

Модуль содержит функции для расчета подписи, генерации платежных ссылок, разбора ответов от Robokassa и проверки успешности платежей. Эти функции обеспечивают безопасное взаимодействие с Robokassa и позволяют боту Telegram принимать платежи от пользователей.

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
        is_result (bool, optional): Флаг, указывающий, что подпись вычисляется для Result URL. По умолчанию `False`.

    Returns:
        str: Вычисленная подпись в виде MD5 хеша.
    """
```

**Как работает функция**:

1.  Формирует строку для вычисления подписи в зависимости от типа URL (Result URL или initial/Success URL).
2.  Добавляет дополнительные параметры (user\_id, user\_telegram\_id, product\_id) к строке, сортируя их по ключам.
3.  Вычисляет MD5 хеш от полученной строки.

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
    """
```

**Как работает функция**:

1.  Вычисляет подпись с использованием функции `calculate_signature`.
2.  Формирует словарь с параметрами запроса к Robokassa, включая логин магазина, сумму, номер заказа, описание, подпись, флаг тестового режима и дополнительные параметры.
3.  Кодирует параметры в строку запроса и добавляет её к базовому URL Robokassa.

**Примеры**:

```python
cost = 100.0
number = 123
description = 'Test order'
user_id = 1
user_telegram_id = 123456789
product_id = 1
payment_link = generate_payment_link(cost, number, description, user_id, user_telegram_id, product_id)
print(payment_link)
# Output: https://auth.robokassa.ru/Merchant/Index.aspx?MerchantLogin=<merchant_login>&OutSum=100.0&InvId=123&Description=Test+order&SignatureValue=<signature>&IsTest=1&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=1
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
    """
```

**Как работает функция**:

1.  Использует `urlparse` для разбора URL из строки запроса.
2.  Использует `parse_qsl` для разбора строки запроса в словарь.

**Примеры**:

```python
request = 'https://example.com/path?param1=value1&param2=value2'
params = parse_response(request)
print(params)
# Output: {'param1': 'value1', 'param2': 'value2'}
```

### `check_signature_result`

```python
def check_signature_result(out_sum, inv_id, received_signature, password, user_id, user_telegram_id, product_id) -> bool:
    """
    Проверяет подпись для Result URL.

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
    """
```

**Как работает функция**:

1.  Вычисляет подпись с использованием функции `calculate_signature` и флага `is_result=True`.
2.  Сравнивает вычисленную подпись с полученной подписью, приводя обе к нижнему регистру.

### `result_payment`

```python
def result_payment(request: str) -> str:
    """
    Обрабатывает результат оплаты (ResultURL).

    Args:
        request (str): Строка запроса с параметрами оплаты.

    Returns:
        str: 'OK' + номер заказа, если оплата прошла успешно, иначе 'bad sign'.
    """
```

**Как работает функция**:

1.  Разбирает строку запроса с использованием функции `parse_response`.
2.  Извлекает параметры (out\_sum, inv\_id, signature, user\_id, user\_telegram\_id, product\_id) из словаря параметров.
3.  Проверяет подпись с использованием функции `check_signature_result` и второго пароля магазина (settings.MRH\_PASS\_2).
4.  Возвращает 'OK' + номер заказа, если подпись верна, иначе возвращает 'bad sign'.

**Примеры**:

```python
request = 'https://example.com/result?OutSum=100.0&InvId=123&SignatureValue=<signature>&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=1'
result = result_payment(request)
print(result)
# Output: OK123 или bad sign
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
    """
```

**Как работает функция**:

1.  Разбирает строку запроса с использованием функции `parse_response`.
2.  Извлекает параметры (out\_sum, inv\_id, signature, user\_id, user\_telegram\_id, product\_id) из словаря параметров.
3.  Проверяет подпись с использованием функции `check_signature_result` и первого пароля магазина (settings.MRH\_PASS\_1).
4.  Возвращает сообщение об успешной оплате, если подпись верна, иначе возвращает 'bad sign'.

**Примеры**:

```python
request = 'https://example.com/success?OutSum=100.0&InvId=123&SignatureValue=<signature>&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=1'
result = check_success_payment(request)
print(result)
# Output: Thank you for using our service или bad sign