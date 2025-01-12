# Модуль `utils.py`

## Обзор

Модуль `utils.py` содержит набор функций для работы с платежной системой Robokassa. Он включает в себя функции для генерации платежных ссылок, проверки подписей, а также обработки уведомлений об успешной или неуспешной оплате.

## Оглавление

1.  [Функции](#функции)
    -   [`calculate_signature`](#calculate_signature)
    -   [`generate_payment_link`](#generate_payment_link)
    -   [`parse_response`](#parse_response)
    -   [`check_signature_result`](#check_signature_result)
    -   [`result_payment`](#result_payment)
    -   [`check_success_payment`](#check_success_payment)

## Функции

### `calculate_signature`

**Описание**:
Вычисляет MD5-хеш подписи для запросов к Robokassa.

**Параметры**:
- `login` (str): Логин мерчанта в Robokassa.
- `cost` (float): Сумма платежа.
- `inv_id` (int): Номер заказа.
- `password` (str): Пароль мерчанта в Robokassa.
- `user_id` (int): ID пользователя.
- `user_telegram_id` (int): Telegram ID пользователя.
- `product_id` (int): ID продукта.
- `is_result` (bool, optional): Флаг, указывающий, что подпись вычисляется для Result URL. По умолчанию `False`.

**Возвращает**:
- `str`: MD5-хеш подписи в шестнадцатеричном формате.

### `generate_payment_link`

**Описание**:
Генерирует ссылку для оплаты через Robokassa с обязательными параметрами.

**Параметры**:
- `cost` (float): Стоимость товара.
- `number` (int): Номер заказа.
- `description` (str): Описание заказа.
- `user_id` (int): ID пользователя.
- `user_telegram_id` (int): Telegram ID пользователя.
- `product_id` (int): ID товара.
- `is_test` (int, optional): Флаг тестового режима (1 - тест, 0 - боевой режим). По умолчанию `1`.
- `robokassa_payment_url` (str, optional): URL для оплаты Robokassa. По умолчанию `https://auth.robokassa.ru/Merchant/Index.aspx`.

**Возвращает**:
- `str`: Ссылка на страницу оплаты Robokassa.

### `parse_response`

**Описание**:
Разбирает строку запроса на параметры.

**Параметры**:
- `request` (str): Строка запроса.

**Возвращает**:
- `dict`: Словарь с параметрами запроса.

### `check_signature_result`

**Описание**:
Проверяет соответствие полученной подписи вычисленной подписи для Result URL.

**Параметры**:
- `out_sum` (str): Сумма платежа.
- `inv_id` (str): Номер заказа.
- `received_signature` (str): Полученная подпись.
- `password` (str): Пароль мерчанта в Robokassa.
- `user_id` (str): ID пользователя.
- `user_telegram_id` (str): Telegram ID пользователя.
- `product_id` (str): ID продукта.

**Возвращает**:
- `bool`: `True`, если подписи совпадают, иначе `False`.

### `result_payment`

**Описание**:
Обрабатывает результат оплаты (ResultURL).

**Параметры**:
- `request` (str): Строка запроса с параметрами оплаты.

**Возвращает**:
- `str`: `'OK' + номер заказа`, если оплата прошла успешно, иначе `'bad sign'`.

### `check_success_payment`

**Описание**:
Проверяет успешность оплаты (SuccessURL).

**Параметры**:
- `request` (str): Строка запроса с параметрами оплаты.

**Возвращает**:
- `str`: Сообщение об успешной оплате (`"Thank you for using our service"`) или `'bad sign'` при неверной подписи.