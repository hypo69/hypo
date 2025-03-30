# Модуль утилит для работы с Robokassa

## Обзор

Модуль `utils.py` содержит набор функций для работы с платежной системой Robokassa. Он включает в себя генерацию платежных ссылок, проверку подписи, обработку ответов от Robokassa и проверку успешности платежей. Модуль предназначен для интеграции с ботом Telegram и обеспечивает безопасное проведение платежей.

## Подробней

Модуль `utils.py` предоставляет функциональность для создания и проверки платежей через Robokassa. Он содержит функции для генерации подписи, создания платежной ссылки, разбора ответа от Robokassa и проверки успешности платежа. Эти функции используются для безопасного взаимодействия с Robokassa и обработки платежей в боте Telegram.

## Функции

### `calculate_signature`

```python
def calculate_signature(login, cost, inv_id, password, user_id, user_telegram_id, product_id, is_result=False):
    """ This if example function
        Args:
            login: логин мерчанта.
            cost: Стоимость товара.
            inv_id: Номер заказа.
            password: Пароль мерчанта.
            user_id: ID пользователя.
            user_telegram_id: Telegram ID пользователя.
            product_id: ID товара.
            is_result (bool): Флаг, указывающий, является ли URL результатом (Result URL). По умолчанию `False`.
        Returns:
            str: Возвращает MD5-хеш, используемый для подписи запроса.

        Raises:
             None

        Example:
            Примеры вызовов
    """
```

**Описание**: Вычисляет подпись для запросов к Robokassa. Подпись генерируется на основе параметров запроса и пароля мерчанта.

**Параметры**:
- `login`: Логин мерчанта.
- `cost`: Стоимость товара.
- `inv_id`: Номер заказа.
- `password`: Пароль мерчанта.
- `user_id`: ID пользователя.
- `user_telegram_id`: Telegram ID пользователя.
- `product_id`: ID товара.
- `is_result` (bool): Флаг, указывающий, является ли URL результатом (Result URL). По умолчанию `False`.

**Возвращает**:
- `str`: MD5-хеш, используемый для подписи запроса.

**Примеры**:
```python
calculate_signature('login', 100.0, 123, 'password', 1, 123456789, 1)
```

### `generate_payment_link`

```python
def generate_payment_link(cost: float, number: int, description: str,
                          user_id: int, user_telegram_id: int, product_id: int,
                          is_test=1, robokassa_payment_url='https://auth.robokassa.ru/Merchant/Index.aspx') -> str:
    """ This if example function
        Args:
            cost (float): Стоимость товара.
            number (int): Номер заказа.
            description (str): Описание заказа.
            user_id (int): ID пользователя.
            user_telegram_id (int): Telegram ID пользователя.
            product_id (int): ID товара.
            is_test (int): Флаг тестового режима (1 - тест, 0 - боевой режим). По умолчанию 1.
            robokassa_payment_url: URL для оплаты Robokassa. По умолчанию 'https://auth.robokassa.ru/Merchant/Index.aspx'.
        Returns:
            str: Ссылка на страницу оплаты.

        Raises:
             None

        Example:
            Примеры вызовов
    """
```

**Описание**: Генерирует ссылку для оплаты через Robokassa с обязательными параметрами.

**Параметры**:
- `cost` (float): Стоимость товара.
- `number` (int): Номер заказа.
- `description` (str): Описание заказа.
- `user_id` (int): ID пользователя.
- `user_telegram_id` (int): Telegram ID пользователя.
- `product_id` (int): ID товара.
- `is_test` (int): Флаг тестового режима (1 - тест, 0 - боевой режим). По умолчанию `1`.
- `robokassa_payment_url`: URL для оплаты Robokassa. По умолчанию `'https://auth.robokassa.ru/Merchant/Index.aspx'`.

**Возвращает**:
- `str`: Ссылка на страницу оплаты.

**Примеры**:
```python
generate_payment_link(100.0, 123, 'Test description', 1, 123456789, 1)
```

### `parse_response`

```python
def parse_response(request: str) -> dict:
    """ This if example function
        Args:
            request (str): Строка запроса.
        Returns:
            dict: Словарь с параметрами.

        Raises:
             None

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
parse_response('https://example.com?param1=value1&param2=value2')
```

### `check_signature_result`

```python
def check_signature_result(out_sum, inv_id, received_signature, password, user_id, user_telegram_id, product_id) -> bool:
    """ This if example function
        Args:
            out_sum: Сумма платежа.
            inv_id: Номер заказа.
            received_signature: Полученная подпись.
            password: Пароль мерчанта.
            user_id: ID пользователя.
            user_telegram_id: Telegram ID пользователя.
            product_id: ID товара.
        Returns:
            bool: `True`, если подпись верна, иначе `False`.

        Raises:
             None

        Example:
            Примеры вызовов
    """
```

**Описание**: Проверяет подпись результата оплаты.

**Параметры**:
- `out_sum`: Сумма платежа.
- `inv_id`: Номер заказа.
- `received_signature`: Полученная подпись.
- `password`: Пароль мерчанта.
- `user_id`: ID пользователя.
- `user_telegram_id`: Telegram ID пользователя.
- `product_id`: ID товара.

**Возвращает**:
- `bool`: `True`, если подпись верна, иначе `False`.

**Примеры**:
```python
check_signature_result(100.0, 123, 'signature', 'password', 1, 123456789, 1)
```

### `result_payment`

```python
def result_payment(request: str) -> str:
    """ This if example function
        Args:
            request (str): Строка запроса с параметрами оплаты.
        Returns:
            str: 'OK' + номер заказа, если оплата прошла успешно, иначе 'bad sign'.

        Raises:
             None

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
result_payment('https://example.com?OutSum=100.0&InvId=123&SignatureValue=signature&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=1')
```

### `check_success_payment`

```python
def check_success_payment(request: str) -> str:
    """ This if example function
        Args:
            request (str): Строка запроса с параметрами оплаты.
        Returns:
            str: Сообщение об успешной оплате или 'bad sign' при неверной подписи.

        Raises:
             None

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
check_success_payment('https://example.com?OutSum=100.0&InvId=123&SignatureValue=signature&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=1')