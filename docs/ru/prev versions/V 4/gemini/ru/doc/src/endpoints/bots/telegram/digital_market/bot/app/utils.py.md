# Модуль utils.py для Robokassa

## Обзор

Модуль `utils.py` предназначен для генерации платежных ссылок Robokassa и обработки ответов от Robokassa. Он включает функции для расчета подписи, создания ссылок для оплаты, разбора ответов и проверки подписи для ResultURL и SuccessURL. Модуль обеспечивает интеграцию с платежной системой Robokassa для обработки платежей в боте Telegram.

## Подробней

Этот модуль содержит функции, необходимые для взаимодействия с Robokassa API. Он генерирует ссылки для оплаты, проверяет подписи и обрабатывает ответы от Robokassa, что позволяет безопасно и надежно проводить платежи. Используется для автоматизации процесса оплаты в боте Telegram, предоставляя пользователям удобный способ оплаты за товары или услуги.

## Функции

### `calculate_signature`

```python
def calculate_signature(login, cost, inv_id, password, user_id, user_telegram_id, product_id, is_result=False):
    """ This if example function
    Args:
        login:
        cost:
        inv_id:
        password:
        user_id:
        user_telegram_id:
        product_id:
        is_result (bool):

    Returns:

     Raises:
          Ошибка выполнение

     Example:
          Примеры вызовов

    """
```

**Описание**: Вычисляет подпись для запросов к Robokassa.

**Параметры**:
- `login`: Логин магазина в Robokassa.
- `cost`: Сумма платежа.
- `inv_id`: Номер заказа.
- `password`: Пароль магазина в Robokassa.
- `user_id`: ID пользователя.
- `user_telegram_id`: Telegram ID пользователя.
- `product_id`: ID продукта.
- `is_result` (bool): Флаг, указывающий, является ли URL результатом (Result URL).

**Возвращает**:
- `str`: Подпись, вычисленная на основе входных параметров.

**Примеры**:

```python
login = "test_login"
cost = 100.0
inv_id = 123
password = "test_password"
user_id = 1
user_telegram_id = 123456789
product_id = 10

signature = calculate_signature(login, cost, inv_id, password, user_id, user_telegram_id, product_id)
print(signature)
```

### `generate_payment_link`

```python
def generate_payment_link(cost: float, number: int, description: str,
                          user_id: int, user_telegram_id: int, product_id: int,
                          is_test=1, robokassa_payment_url='https://auth.robokassa.ru/Merchant/Index.aspx') -> str:
    """ This if example function
    Args:
        cost (float): Стоимость товара
        number (int): Номер заказа
        description (str): Описание заказа
        user_id (int): ID пользователя
        user_telegram_id (int): Telegram ID пользователя
        product_id (int): ID товара
        is_test:
        robokassa_payment_url:

    Returns:

     Raises:
          Ошибка выполнение

     Example:
          Примеры вызовов

    """
```

**Описание**: Генерирует ссылку для оплаты через Robokassa.

**Параметры**:
- `cost` (float): Стоимость товара.
- `number` (int): Номер заказа.
- `description` (str): Описание заказа.
- `user_id` (int): ID пользователя.
- `user_telegram_id` (int): Telegram ID пользователя.
- `product_id` (int): ID товара.
- `is_test`: Флаг тестового режима (1 - тест, 0 - боевой режим).
- `robokassa_payment_url`: URL для оплаты Robokassa.

**Возвращает**:
- `str`: Ссылка на страницу оплаты.

**Примеры**:

```python
cost = 100.0
number = 123
description = "Test order"
user_id = 1
user_telegram_id = 123456789
product_id = 10

payment_link = generate_payment_link(cost, number, description, user_id, user_telegram_id, product_id)
print(payment_link)
```

### `parse_response`

```python
def parse_response(request: str) -> dict:
    """ This if example function
    Args:
        request (str): Строка запроса

    Returns:

     Raises:
          Ошибка выполнение

     Example:
          Примеры вызовов

    """
```

**Описание**: Разбирает строку запроса на параметры.

**Параметры**:
- `request` (str): Строка запроса.

**Возвращает**:
- `dict`: Словарь с параметрами.

**Примеры**:

```python
request = "https://example.com?param1=value1&param2=value2"
params = parse_response(request)
print(params)
```

### `check_signature_result`

```python
def check_signature_result(out_sum, inv_id, received_signature, password, user_id, user_telegram_id, product_id) -> bool:
    """ This if example function
    Args:
        out_sum:
        inv_id:
        received_signature:
        password:
        user_id:
        user_telegram_id:
        product_id:

    Returns:

     Raises:
          Ошибка выполнение

     Example:
          Примеры вызовов

    """
```

**Описание**: Проверяет подпись для ResultURL.

**Параметры**:
- `out_sum`: Сумма платежа.
- `inv_id`: Номер заказа.
- `received_signature`: Полученная подпись.
- `password`: Пароль магазина в Robokassa.
- `user_id`: ID пользователя.
- `user_telegram_id`: Telegram ID пользователя.
- `product_id`: ID продукта.

**Возвращает**:
- `bool`: `True`, если подпись верна, иначе `False`.

**Примеры**:

```python
out_sum = 100.0
inv_id = 123
received_signature = "test_signature"
password = "test_password"
user_id = 1
user_telegram_id = 123456789
product_id = 10

is_valid = check_signature_result(out_sum, inv_id, received_signature, password, user_id, user_telegram_id, product_id)
print(is_valid)
```

### `result_payment`

```python
def result_payment(request: str) -> str:
    """ This if example function
    Args:
        request (str): Строка запроса с параметрами оплаты

    Returns:

     Raises:
          Ошибка выполнение

     Example:
          Примеры вызовов

    """
```

**Описание**: Обрабатывает результат оплаты (ResultURL).

**Параметры**:
- `request` (str): Строка запроса с параметрами оплаты.

**Возвращает**:
- `str`: `'OK' + номер заказа`, если оплата прошла успешно, иначе `'bad sign'`.

**Примеры**:

```python
request = "https://example.com?OutSum=100.0&InvId=123&SignatureValue=test_signature&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=10"
result = result_payment(request)
print(result)
```

### `check_success_payment`

```python
def check_success_payment(request: str) -> str:
    """ This if example function
    Args:
        request (str): Строка запроса с параметрами оплаты

    Returns:

     Raises:
          Ошибка выполнение

     Example:
          Примеры вызовов

    """
```

**Описание**: Проверяет успешность оплаты (SuccessURL).

**Параметры**:
- `request` (str): Строка запроса с параметрами оплаты.

**Возвращает**:
- `str`: Сообщение об успешной оплате или `'bad sign'` при неверной подписи.

**Примеры**:

```python
request = "https://example.com?OutSum=100.0&InvId=123&SignatureValue=test_signature&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=10"
result = check_success_payment(request)
print(result)