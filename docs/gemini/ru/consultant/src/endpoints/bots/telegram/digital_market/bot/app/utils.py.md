### Анализ кода модуля `utils`

**Качество кода**:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код выполняет основные функции по генерации и проверке платежных ссылок Robokassa.
    - Присутствует базовая документация для функций.
    - Используются безопасные методы для работы с URL.
- **Минусы**:
    - Не везде используется одинарный формат кавычек в коде.
    - Код местами не соответствует PEP8, например, форматирование строк и именование переменных.
    -  Отсутствует логирование ошибок.
    -  Не используется `j_loads` или `j_loads_ns`.
    - Комментарии не соответствуют стандарту **RST**.

**Рекомендации по улучшению**:
- Необходимо заменить двойные кавычки на одинарные, где это требуется, и наоборот, для соответствия стандарту.
- Форматировать код согласно PEP8.
- Добавить подробную документацию в формате RST для всех функций.
- Добавить логирование ошибок с использованием `logger.error`.
- Уточнить комментарии, сделав их более информативными.
- Использовать `j_loads` или `j_loads_ns` при работе с JSON, если это потребуется в будущем.

**Оптимизированный код**:
```python
import hashlib
from urllib import parse
from urllib.parse import urlparse

from src.logger import logger  # Используем logger из src.logger
from bot.config import settings


def calculate_signature(
    login: str,
    cost: float,
    inv_id: int,
    password: str,
    user_id: int,
    user_telegram_id: int,
    product_id: int,
    is_result: bool = False,
) -> str:
    """
    Вычисляет подпись для запросов к Robokassa.

    :param login: Логин мерчанта в Robokassa.
    :type login: str
    :param cost: Сумма платежа.
    :type cost: float
    :param inv_id: Номер счета.
    :type inv_id: int
    :param password: Пароль мерчанта.
    :type password: str
    :param user_id: ID пользователя.
    :type user_id: int
    :param user_telegram_id: Telegram ID пользователя.
    :type user_telegram_id: int
    :param product_id: ID продукта.
    :type product_id: int
    :param is_result: Флаг, указывающий, является ли URL результатом оплаты.
    :type is_result: bool
    :return: MD5 хэш подписи.
    :rtype: str

    Подпись формируется путем конкатенации параметров и последующего хеширования MD5.
    Для Result URL используется другой набор параметров.

    Пример:
        >>> calculate_signature(
        ...     login='test_login',
        ...     cost=100.00,
        ...     inv_id=12345,
        ...     password='test_password',
        ...     user_id=1,
        ...     user_telegram_id=123,
        ...     product_id=10,
        ...     is_result=False
        ... )
        'e9c95a4210f2658a41880e4a35e0a62b'
    """
    if is_result:
        base_string = f'{cost}:{inv_id}:{password}'  # Для Result URL
    else:
        base_string = f'{login}:{cost}:{inv_id}:{password}'  # Для initital URL и Success URL

    additional_params = {
        'Shp_user_id': user_id,
        'Shp_user_telegram_id': user_telegram_id,
        'Shp_product_id': product_id,
    }
    for key, value in sorted(additional_params.items()):
        base_string += f':{key}={value}'

    return hashlib.md5(base_string.encode('utf-8')).hexdigest()


def generate_payment_link(
    cost: float,
    number: int,
    description: str,
    user_id: int,
    user_telegram_id: int,
    product_id: int,
    is_test: int = 1,
    robokassa_payment_url: str = 'https://auth.robokassa.ru/Merchant/Index.aspx',
) -> str:
    """
    Генерирует ссылку для оплаты через Robokassa.

    :param cost: Стоимость товара.
    :type cost: float
    :param number: Номер заказа.
    :type number: int
    :param description: Описание заказа.
    :type description: str
    :param user_id: ID пользователя.
    :type user_id: int
    :param user_telegram_id: Telegram ID пользователя.
    :type user_telegram_id: int
    :param product_id: ID товара.
    :type product_id: int
    :param is_test: Флаг тестового режима (1 - тест, 0 - боевой режим).
    :type is_test: int, optional
    :param robokassa_payment_url: URL для оплаты Robokassa.
    :type robokassa_payment_url: str, optional
    :return: Ссылка на страницу оплаты.
    :rtype: str

    Создает URL с необходимыми параметрами для оплаты через Robokassa,
    включая подпись безопасности.
    """
    signature = calculate_signature(
        settings.MRH_LOGIN,
        cost,
        number,
        settings.MRH_PASS_1,
        user_id,
        user_telegram_id,
        product_id,
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
        'Shp_product_id': product_id,
    }

    return f'{robokassa_payment_url}?{parse.urlencode(data)}'


def parse_response(request: str) -> dict:
    """
    Разбирает строку запроса на параметры.

    :param request: Строка запроса.
    :type request: str
    :return: Словарь с параметрами.
    :rtype: dict

    Преобразует строку запроса в словарь параметров, используя `urlparse` и `parse_qsl`.

    Пример:
        >>> parse_response("https://example.com/payment?param1=value1&param2=value2")
        {'param1': 'value1', 'param2': 'value2'}
    """
    try:
        return dict(parse.parse_qsl(urlparse(request).query))
    except Exception as e:
        logger.error(f'Error parsing response: {e}')
        return {}


def check_signature_result(
    out_sum: float,
    inv_id: int,
    received_signature: str,
    password: str,
    user_id: int,
    user_telegram_id: int,
    product_id: int,
) -> bool:
    """
    Проверяет подпись для Result URL.

    :param out_sum: Сумма платежа.
    :type out_sum: float
    :param inv_id: Номер счета.
    :type inv_id: int
    :param received_signature: Полученная подпись.
    :type received_signature: str
    :param password: Пароль мерчанта.
    :type password: str
    :param user_id: ID пользователя.
    :type user_id: int
    :param user_telegram_id: Telegram ID пользователя.
    :type user_telegram_id: int
    :param product_id: ID продукта.
    :type product_id: int
    :return: True, если подпись совпадает, иначе False.
    :rtype: bool

    Сравнивает сгенерированную подпись с полученной для проверки целостности данных.
    """
    signature = calculate_signature(
        settings.MRH_LOGIN,
        out_sum,
        inv_id,
        password,
        user_id,
        user_telegram_id,
        product_id,
        is_result=True,  # Важный флаг для Result URL
    )
    return signature.lower() == received_signature.lower()


def result_payment(request: str) -> str:
    """
    Обрабатывает результат оплаты (ResultURL).

    :param request: Строка запроса с параметрами оплаты.
    :type request: str
    :return: 'OK' + номер заказа, если оплата прошла успешно, иначе 'bad sign'.
    :rtype: str

    Извлекает параметры из запроса и проверяет подпись.
    Возвращает 'OK' + номер заказа при успешной проверке, иначе 'bad sign'.
    """
    params = parse_response(request)
    if not params:  # Проверка на пустой словарь
        return 'bad sign'
    out_sum = params.get('OutSum')
    inv_id = params.get('InvId')
    signature = params.get('SignatureValue')
    user_id = params.get('Shp_user_id')
    user_telegram_id = params.get('Shp_user_telegram_id')
    product_id = params.get('Shp_product_id')

    if check_signature_result(
        out_sum, inv_id, signature, settings.MRH_PASS_2, user_id, user_telegram_id, product_id
    ):
        return f'OK{inv_id}'
    return 'bad sign'


def check_success_payment(request: str) -> str:
    """
    Проверяет успешность оплаты (SuccessURL).

    :param request: Строка запроса с параметрами оплаты.
    :type request: str
    :return: Сообщение об успешной оплате или 'bad sign' при неверной подписи.
    :rtype: str

    Извлекает параметры из запроса и проверяет подпись.
    Возвращает сообщение об успешной оплате при верной подписи, иначе 'bad sign'.
    """
    params = parse_response(request)
    if not params:  # Проверка на пустой словарь
        return 'bad sign'
    out_sum = params.get('OutSum')
    inv_id = params.get('InvId')
    signature = params.get('SignatureValue')
    user_id = params.get('Shp_user_id')
    user_telegram_id = params.get('Shp_user_telegram_id')
    product_id = params.get('Shp_product_id')

    if check_signature_result(
        out_sum, inv_id, signature, settings.MRH_PASS_1, user_id, user_telegram_id, product_id
    ):
        return 'Thank you for using our service'
    return 'bad sign'