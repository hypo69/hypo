# Модуль утилит для работы с Robokassa в Telegram боте

## Обзор

Модуль содержит функции для генерации платежных ссылок Robokassa, проверки подписи и обработки ответов от Robokassa. Он используется для интеграции платежной системы Robokassa в Telegram бот, позволяя пользователям оплачивать товары и услуги через бот.

## Подробнее

Этот модуль обеспечивает взаимодействие с Robokassa, включая формирование платежных ссылок, проверку корректности данных, приходящих от Robokassa, и обработку результатов оплаты. Все функции модуля работают с параметрами, необходимыми для безопасного и корректного проведения платежей. Модуль использует параметры из конфигурационного файла `bot.config.settings`.

## Функции

### `calculate_signature`

```python
def calculate_signature(login, cost, inv_id, password, user_id, user_telegram_id, product_id, is_result=False):
    """
    Вычисляет подпись для запросов к Robokassa.

    Args:
        login (str): Логин мерчанта в Robokassa.
        cost (float): Сумма платежа.
        inv_id (int): Номер заказа.
        password (str): Пароль мерчанта.
        user_id (int): ID пользователя.
        user_telegram_id (int): Telegram ID пользователя.
        product_id (int): ID продукта.
        is_result (bool): Флаг, указывающий, что подпись вычисляется для Result URL.

    Returns:
        str: MD5 хеш подписи в шестнадцатеричном формате.

    """
```

**Как работает функция**:

1.  Функция `calculate_signature` вычисляет MD5-хеш, используемый для проверки подлинности запросов, отправляемых или получаемых от Robokassa.

2.  Определяется базовая строка для подписи в зависимости от значения флага `is_result`. Если `is_result` равен `True`, используется формат для Result URL, иначе - для initial и Success URL.

3.  Создается словарь `additional_params`, содержащий дополнительные параметры, такие как `user_id`, `user_telegram_id` и `product_id`.

4.  Параметры из `additional_params` сортируются по ключам и добавляются к базовой строке.

5.  Базовая строка кодируется в UTF-8 и хешируется с помощью MD5.

6.  Возвращается MD5 хеш в шестнадцатеричном формате.

**ASCII flowchart**:

```
Начало
|
Определение базовой строки (зависит от is_result)
|
Создание additional_params
|
Сортировка и добавление параметров к базовой строке
|
Кодирование в UTF-8 и хеширование MD5
|
Возврат MD5 хеша
Конец
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
```

**Как работает функция**:

1.  Функция `generate_payment_link` генерирует URL для перенаправления пользователя на страницу оплаты Robokassa.

2.  Вызывается функция `calculate_signature` для формирования подписи запроса.

3.  Создается словарь `data` с параметрами запроса, включая логин мерчанта, сумму, номер заказа, описание и подпись.

4.  Параметры кодируются в URL-encoded строку.

5.  Возвращается полная URL, включающая базовый URL Robokassa и параметры запроса.

**ASCII flowchart**:

```
Начало
|
Вычисление подписи
|
Создание словаря data с параметрами
|
Кодирование параметров в URL-encoded строку
|
Формирование полной URL
|
Возврат URL
Конец
```

**Примеры**:

```python
payment_link = generate_payment_link(
    cost=100.0,
    number=123,
    description='Test Payment',
    user_id=1,
    user_telegram_id=123456789,
    product_id=1,
    is_test=1,
    robokassa_payment_url='https://auth.robokassa.ru/Merchant/Index.aspx'
)
print(payment_link)
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
```

**Как работает функция**:

1.  Функция `parse_response` разбирает строку запроса, полученную от Robokassa, и извлекает параметры.

2.  Используется `urlparse` для разбора URL и `parse_qsl` для извлечения параметров запроса в виде списка кортежей.

3.  Результат преобразуется в словарь и возвращается.

**ASCII flowchart**:

```
Начало
|
Разбор URL
|
Извлечение параметров запроса
|
Преобразование в словарь
|
Возврат словаря
Конец
```

**Примеры**:

```python
request = 'https://example.com/result?OutSum=100&InvId=123&SignatureValue=test'
params = parse_response(request)
print(params)
```

### `check_signature_result`

```python
def check_signature_result(out_sum, inv_id, received_signature, password, user_id, user_telegram_id, product_id) -> bool:
    """
    Проверяет подпись для ResultURL.

    Args:
        out_sum (float): Сумма платежа
        inv_id (int): Номер заказа
        received_signature (str): Полученная подпись
        password (str): Пароль мерчанта
        user_id (int): ID пользователя
        user_telegram_id (int): Telegram ID пользователя
        product_id (int): ID продукта

    Returns:
        bool: True, если подпись верна, иначе False
    """
```

**Как работает функция**:

1.  Функция `check_signature_result` проверяет подлинность подписи, полученной от Robokassa в Result URL.

2.  Вызывается функция `calculate_signature` с флагом `is_result=True` для вычисления ожидаемой подписи.

3.  Полученная подпись и вычисленная подпись приводятся к нижнему регистру и сравниваются.

4.  Возвращается `True`, если подписи совпадают, иначе `False`.

**ASCII flowchart**:

```
Начало
|
Вычисление ожидаемой подписи (is_result=True)
|
Приведение подписей к нижнему регистру
|
Сравнение подписей
|
Возврат результата сравнения
Конец
```

**Примеры**:

```python
is_valid = check_signature_result(
    out_sum=100.0,
    inv_id=123,
    received_signature='test',
    password='password',
    user_id=1,
    user_telegram_id=123456789,
    product_id=1
)
print(is_valid)
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
```

**Как работает функция**:

1.  Функция `result_payment` обрабатывает Result URL, который Robokassa отправляет после завершения оплаты.

2.  Вызывается функция `parse_response` для извлечения параметров из запроса.

3.  Извлекаются параметры `out_sum`, `inv_id`, `signature`, `user_id`, `user_telegram_id` и `product_id`.

4.  Вызывается функция `check_signature_result` для проверки подлинности подписи.

5.  Если подпись верна, возвращается строка `'OK{inv_id}'`, иначе возвращается строка `"bad sign"`.

**ASCII flowchart**:

```
Начало
|
Разбор запроса
|
Извлечение параметров
|
Проверка подписи
|
Возврат результата (OK{inv_id} или "bad sign")
Конец
```

**Примеры**:

```python
result = result_payment('https://example.com/result?OutSum=100&InvId=123&SignatureValue=test&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=1')
print(result)
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
```

**Как работает функция**:

1.  Функция `check_success_payment` обрабатывает Success URL, на который Robokassa перенаправляет пользователя после успешной оплаты.

2.  Вызывается функция `parse_response` для извлечения параметров из запроса.

3.  Извлекаются параметры `out_sum`, `inv_id`, `signature`, `user_id`, `user_telegram_id` и `product_id`.

4.  Вызывается функция `check_signature_result` для проверки подлинности подписи.

5.  Если подпись верна, возвращается строка `"Thank you for using our service"`, иначе возвращается строка `"bad sign"`.

**ASCII flowchart**:

```
Начало
|
Разбор запроса
|
Извлечение параметров
|
Проверка подписи
|
Возврат результата ("Thank you for using our service" или "bad sign")
Конец
```

**Примеры**:

```python
success_message = check_success_payment('https://example.com/success?OutSum=100&InvId=123&SignatureValue=test&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=1')
print(success_message)