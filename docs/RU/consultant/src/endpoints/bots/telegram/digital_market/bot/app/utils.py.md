# Анализ кода модуля `utils`

**Качество кода**
   7
 -  Плюсы
        - Код выполняет поставленные задачи по генерации ссылок для оплаты через Robokassa и проверке подписей.
        - Функции достаточно хорошо документированы с использованием docstrings.
        - Используется `hashlib` для создания подписей, что является хорошей практикой.
 -  Минусы
    -  Не используется `from src.logger.logger import logger` для логирования ошибок.
    -  Используются двойные кавычки в строках кода, где должны быть одинарные.
    -  Не все функции имеют подробное описание с примерами в docstring.
    -  В некоторых функциях можно было бы добавить обработку исключений.

**Рекомендации по улучшению**

1.  Импортировать `logger` из `src.logger.logger` для логирования ошибок.
2.  Заменить все двойные кавычки на одинарные в коде, кроме операций вывода и строк документации.
3.  Добавить более подробные docstrings для функций, включая примеры использования.
4.  Улучшить обработку ошибок, добавив логирование и, возможно, обработку исключений в некоторых местах, где это необходимо.
5.  Использовать `j_loads` или `j_loads_ns` если работа с json файлами.

**Оптимизированный код**

```python
"""
Модуль для работы с платежной системой Robokassa.
=========================================================================================

Этот модуль содержит функции для генерации платежных ссылок,
проверки подписей и обработки ответов от Robokassa.

Пример использования
--------------------

Пример генерации ссылки:

.. code-block:: python

    payment_link = generate_payment_link(
        cost=100.00,
        number=12345,
        description='Тестовый заказ',
        user_id=1,
        user_telegram_id=123456789,
        product_id=1,
        is_test=1
    )
    print(payment_link)

"""
import hashlib
from urllib import parse
from urllib.parse import urlparse
from bot.config import settings
from src.logger.logger import logger  # Импорт logger


def calculate_signature(login, cost, inv_id, password, user_id, user_telegram_id, product_id, is_result=False):
    """
    Вычисляет подпись для запроса к Robokassa.

    Args:
        login (str): Логин мерчанта.
        cost (float): Сумма платежа.
        inv_id (int): Номер заказа.
        password (str): Пароль мерчанта.
        user_id (int): ID пользователя.
        user_telegram_id (int): Telegram ID пользователя.
        product_id (int): ID товара.
        is_result (bool, optional): Флаг для Result URL. Defaults to False.

    Returns:
        str: MD5-хеш подписи.

    """
    if is_result:
        base_string = f'{cost}:{inv_id}:{password}'  # Для Result URL
    else:
        base_string = f'{login}:{cost}:{inv_id}:{password}'  # Для initital URL и Success URL

    additional_params = {
        'Shp_user_id': user_id,
        'Shp_user_telegram_id': user_telegram_id,
        'Shp_product_id': product_id
    }
    for key, value in sorted(additional_params.items()):
        base_string += f':{key}={value}'

    return hashlib.md5(base_string.encode('utf-8')).hexdigest()


def generate_payment_link(cost: float, number: int, description: str,
                          user_id: int, user_telegram_id: int, product_id: int,
                          is_test=1, robokassa_payment_url='https://auth.robokassa.ru/Merchant/Index.aspx') -> str:
    """
    Генерирует ссылку для оплаты через Robokassa.

    Args:
        cost (float): Стоимость товара.
        number (int): Номер заказа.
        description (str): Описание заказа.
        user_id (int): ID пользователя.
        user_telegram_id (int): Telegram ID пользователя.
        product_id (int): ID товара.
        is_test (int, optional): Флаг тестового режима (1 - тест, 0 - боевой режим). Defaults to 1.
        robokassa_payment_url (str, optional): URL для оплаты Robokassa. Defaults to 'https://auth.robokassa.ru/Merchant/Index.aspx'.

    Returns:
        str: Ссылка на страницу оплаты.

    Example:
        >>> link = generate_payment_link(
        ...     cost=100.00,
        ...     number=12345,
        ...     description='Test order',
        ...     user_id=1,
        ...     user_telegram_id=123456789,
        ...     product_id=1
        ... )
        >>> print(link)
        'https://auth.robokassa.ru/Merchant/Index.aspx?MerchantLogin=your_login&OutSum=100.0&InvId=12345&Description=Test+order&SignatureValue=...&IsTest=1&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=1'
    """
    signature = calculate_signature(
        settings.MRH_LOGIN,
        cost,
        number,
        settings.MRH_PASS_1,
        user_id,
        user_telegram_id,
        product_id
    )

    data = {
        'MerchantLogin': settings.MRH_LOGIN,
        'OutSum': cost,
        'InvId': number,
        'Description': description,
        'SignatureValue': signature,
        'IsTest': is_test,
        'Shp_user_id': user_id,
        'Shp_user_telegram_id': user_telegram_id,
        'Shp_product_id': product_id
    }

    return f'{robokassa_payment_url}?{parse.urlencode(data)}'


def parse_response(request: str) -> dict:
    """
    Разбирает строку запроса на параметры.

    Args:
        request (str): Строка запроса.

    Returns:
        dict: Словарь с параметрами.

    Example:
        >>> request = 'https://example.com?param1=value1&param2=value2'
        >>> params = parse_response(request)
        >>> print(params)
        {'param1': 'value1', 'param2': 'value2'}
    """
    return dict(parse.parse_qsl(urlparse(request).query))


def check_signature_result(out_sum, inv_id, received_signature, password, user_id, user_telegram_id, product_id) -> bool:
    """
    Проверяет подпись для Result URL.

    Args:
        out_sum (float): Сумма платежа.
        inv_id (int): Номер заказа.
        received_signature (str): Полученная подпись.
        password (str): Пароль мерчанта.
        user_id (int): ID пользователя.
        user_telegram_id (int): Telegram ID пользователя.
        product_id (int): ID товара.

    Returns:
        bool: True, если подпись верна, False в противном случае.
    """
    signature = calculate_signature(
        settings.MRH_LOGIN,
        out_sum,
        inv_id,
        password,
        user_id,
        user_telegram_id,
        product_id,
        is_result=True  # Флаг для Result URL
    )
    return signature.lower() == received_signature.lower()


def result_payment(request: str) -> str:
    """
    Обрабатывает результат оплаты (ResultURL).

    Args:
        request (str): Строка запроса с параметрами оплаты.

    Returns:
        str: 'OK' + номер заказа, если оплата прошла успешно, иначе 'bad sign'.

    Example:
        >>> request = 'https://example.com?OutSum=100&InvId=12345&SignatureValue=...&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=1'
        >>> result = result_payment(request)
        >>> print(result)
        'OK12345'
    """
    try: # Добавлена обработка исключений для parse_response
        params = parse_response(request)
        out_sum = params['OutSum']
        inv_id = params['InvId']
        signature = params['SignatureValue']
        user_id = params['Shp_user_id']
        user_telegram_id = params['Shp_user_telegram_id']
        product_id = params['Shp_product_id']
    except Exception as e:
        logger.error(f'Ошибка при разборе параметров запроса {request}: {e}')
        return 'bad sign'

    if check_signature_result(out_sum, inv_id, signature, settings.MRH_PASS_2, user_id, user_telegram_id, product_id):
        return f'OK{inv_id}'
    return 'bad sign'


def check_success_payment(request: str) -> str:
    """
    Проверяет успешность оплаты (SuccessURL).

    Args:
        request (str): Строка запроса с параметрами оплаты.

    Returns:
        str: Сообщение об успешной оплате или 'bad sign' при неверной подписи.

    Example:
        >>> request = 'https://example.com?OutSum=100&InvId=12345&SignatureValue=...&Shp_user_id=1&Shp_user_telegram_id=123456789&Shp_product_id=1'
        >>> result = check_success_payment(request)
        >>> print(result)
        'Thank you for using our service'
    """
    try: # Добавлена обработка исключений для parse_response
        params = parse_response(request)
        out_sum = params['OutSum']
        inv_id = params['InvId']
        signature = params['SignatureValue']
        user_id = params['Shp_user_id']
        user_telegram_id = params['Shp_user_telegram_id']
        product_id = params['Shp_product_id']
    except Exception as e:
        logger.error(f'Ошибка при разборе параметров запроса {request}: {e}')
        return 'bad sign'

    if check_signature_result(out_sum, inv_id, signature, settings.MRH_PASS_1, user_id, user_telegram_id, product_id):
        return 'Thank you for using our service'
    return 'bad sign'
```