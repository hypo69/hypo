# Модуль утилит для интеграции с Robokassa

## Обзор

Модуль `utils.py` содержит набор функций для интеграции с платежной системой Robokassa. Он включает в себя функции для генерации платежных ссылок, проверки подписи, обработки ответов от Robokassa и проверки успешности платежей. Модуль предназначен для использования в Telegram-боте для автоматизации процессов оплаты.

## Подробней

Этот модуль обеспечивает взаимодействие с Robokassa, позволяя генерировать ссылки для оплаты, проверять корректность полученных данных и обрабатывать результаты платежей. Он использует параметры из файла конфигурации `bot.config.settings` для обеспечения безопасности и правильной работы. Функции модуля позволяют автоматизировать процесс приема платежей через Robokassa в контексте Telegram-бота.

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
        product_id: ID продукта.
        is_result (bool, optional): Флаг, указывающий, что подпись вычисляется для Result URL. По умолчанию False.

    Returns:
        str: MD5-хеш, представляющий собой подпись.
    """
```

**Как работает функция**:
Функция вычисляет MD5-хеш, используемый для проверки подлинности запросов к Robokassa. Она принимает параметры, такие как логин, стоимость, номер заказа и пароль, а также дополнительные параметры, такие как ID пользователя, Telegram ID пользователя и ID продукта. В зависимости от флага `is_result`, функция формирует строку для хеширования, используя разные наборы параметров.

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
Функция генерирует URL для перенаправления пользователя на страницу оплаты Robokassa. Она принимает параметры, такие как стоимость, номер заказа, описание и ID пользователя, Telegram ID пользователя и ID продукта. Функция вызывает `calculate_signature` для создания подписи и добавляет все параметры в URL.

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
Функция разбирает строку запроса, полученную от Robokassa, и извлекает параметры, сохраняя их в словарь. Она использует `urllib.parse.parse_qsl` для разбора параметров запроса.

### `check_signature_result`

```python
def check_signature_result(out_sum, inv_id, received_signature, password, user_id, user_telegram_id, product_id) -> bool:
    """
    Проверяет подпись результата оплаты.

    Args:
        out_sum: Сумма платежа.
        inv_id: Номер заказа.
        received_signature: Полученная подпись.
        password: Пароль магазина в Robokassa.
        user_id: ID пользователя.
        user_telegram_id: Telegram ID пользователя.
        product_id: ID продукта.

    Returns:
        bool: True, если подпись верна, иначе False.
    """
```

**Как работает функция**:
Функция проверяет подлинность полученного ответа от Robokassa путем сравнения вычисленной подписи с полученной. Она использует функцию `calculate_signature` для вычисления подписи на основе параметров ответа и сравнивает ее с полученной подписью.

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
Функция обрабатывает уведомление от Robokassa о результате оплаты. Она извлекает параметры из запроса, проверяет подпись и возвращает 'OK' с номером заказа, если подпись верна, иначе возвращает 'bad sign'.

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
Функция проверяет успешность оплаты на основе данных, полученных от Robokassa. Она извлекает параметры из запроса, проверяет подпись и возвращает сообщение об успешной оплате, если подпись верна, иначе возвращает 'bad sign'.