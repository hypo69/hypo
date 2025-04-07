# Модуль `utils.py` для работы с Robokassa

## Обзор

Модуль содержит набор утилитных функций для работы с платежной системой Robokassa. Он включает в себя функции для генерации платежных ссылок, проверки подписи, обработки результатов оплаты и проверки успешности оплаты.
Модуль предназначен для использования в Telegram-боте для цифрового рынка.

## Подробней

Этот модуль предоставляет инструменты для интеграции с Robokassa, обеспечивая безопасное взаимодействие для проведения платежей. Он включает в себя функции для генерации ссылок для оплаты, проверки подлинности ответов от Robokassa и обработки результатов транзакций. Модуль использует параметры конфигурации из `bot.config.settings` для обеспечения безопасности и правильной работы.

## Функции

### `calculate_signature`

```python
def calculate_signature(login, cost, inv_id, password, user_id, user_telegram_id, product_id, is_result=False):
    """
    Вычисляет подпись для запроса к Robokassa.

    Args:
        login (str): Логин магазина в Robokassa.
        cost (float): Сумма платежа.
        inv_id (int): Номер заказа.
        password (str): Пароль магазина в Robokassa.
        user_id (int): ID пользователя.
        user_telegram_id (int): Telegram ID пользователя.
        product_id (int): ID товара.
        is_result (bool, optional): Флаг, указывающий, что подпись вычисляется для Result URL. По умолчанию `False`.

    Returns:
        str: Вычисленная подпись в виде MD5-хэша.

    Как работает функция:
    1. Определяется базовая строка для вычисления подписи в зависимости от флага `is_result`.
    2. Добавляются дополнительные параметры в алфавитном порядке.
    3. Вычисляется MD5-хэш от полученной строки.

    ASCII flowchart:
    Определение_базовой_строки -- Добавление_дополнительных_параметров -- Вычисление_MD5_хэша

    Примеры:
        >>> calculate_signature('login', 100.0, 123, 'password', 1, 123456789, 1)
        'e5941bb769a77a84ebc956b9c3b88e9a'

        >>> calculate_signature('login', 100.0, 123, 'password', 1, 123456789, 1, is_result=True)
        '776693cc4a08c826f9f02a356cb16967'
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
        is_test (int, optional): Флаг тестового режима (1 - тест, 0 - боевой режим). По умолчанию `1`.
        robokassa_payment_url (str, optional): URL для оплаты Robokassa. По умолчанию 'https://auth.robokassa.ru/Merchant/Index.aspx'.

    Returns:
        str: Ссылка на страницу оплаты.

    Как работает функция:
    1. Вычисляется подпись для запроса с использованием функции `calculate_signature`.
    2. Формируются параметры запроса в виде словаря.
    3. Кодируются параметры запроса в URL-строку.
    4. Возвращается полная URL-ссылка для оплаты.

    ASCII flowchart:
    Вычисление_подписи -- Формирование_параметров -- Кодирование_в_URL -- Возврат_URL

    Примеры:
        >>> generate_payment_link(100.0, 123, 'Test order', 1, 123456789, 1)
        'https://auth.robokassa.ru/Merchant/Index.aspx?MerchantLogin=your_login&OutSum=100.0&InvId=123&Description=Test+order&SignatureValue=0e134b0f66a31549478548214df7160a&IsTest=1&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=1'
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
    1. Извлекается строка запроса из URL.
    2. Разбирается строка запроса на параметры и их значения.
    3. Возвращается словарь, содержащий параметры запроса.

    ASCII flowchart:
    Извлечение_строки_запроса -- Разбор_параметров -- Возврат_словаря

    Примеры:
        >>> parse_response('https://example.com/api?param1=value1&param2=value2')
        {'param1': 'value1', 'param2': 'value2'}
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
        product_id (int): ID товара.

    Returns:
        bool: `True`, если подпись верна, иначе `False`.

    Как работает функция:
    1. Вычисляет подпись с использованием функции `calculate_signature` и флага `is_result=True`.
    2. Сравнивает вычисленную подпись с полученной подписью (без учета регистра).
    3. Возвращает результат сравнения.

    ASCII flowchart:
    Вычисление_подписи -- Сравнение_подписей -- Возврат_результата

    Примеры:
        >>> check_signature_result(100.0, 123, '776693cc4a08c826f9f02a356cb16967', 'password', 1, 123456789, 1)
        True

        >>> check_signature_result(100.0, 123, 'invalid_signature', 'password', 1, 123456789, 1)
        False
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
    1. Разбирает параметры запроса с использованием функции `parse_response`.
    2. Извлекает необходимые параметры из словаря.
    3. Проверяет подпись с использованием функции `check_signature_result`.
    4. Возвращает 'OK' + номер заказа, если подпись верна, иначе 'bad sign'.

    ASCII flowchart:
    Разбор_параметров -- Извлечение_параметров -- Проверка_подписи -- Возврат_результата

    Примеры:
        >>> result_payment('https://example.com/result?OutSum=100.0&InvId=123&SignatureValue=776693cc4a08c826f9f02a356cb16967&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=1')
        'OK123'

        >>> result_payment('https://example.com/result?OutSum=100.0&InvId=123&SignatureValue=invalid_signature&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=1')
        'bad sign'
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
    1. Разбирает параметры запроса с использованием функции `parse_response`.
    2. Извлекает необходимые параметры из словаря.
    3. Проверяет подпись с использованием функции `check_signature_result` с использованием `settings.MRH_PASS_1`.
    4. Возвращает сообщение об успешной оплате, если подпись верна, иначе 'bad sign'.

    ASCII flowchart:
    Разбор_параметров -- Извлечение_параметров -- Проверка_подписи -- Возврат_результата

    Примеры:
        >>> check_success_payment('https://example.com/success?OutSum=100.0&InvId=123&SignatureValue=0e134b0f66a31549478548214df7160a&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=1')
        'Thank you for using our service'

        >>> check_success_payment('https://example.com/success?OutSum=100.0&InvId=123&SignatureValue=invalid_signature&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=1')
        'bad sign'
    """
    ...