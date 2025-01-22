### Анализ кода модуля `app`

**Качество кода**:
   - **Соответствие стандартам**: 7/10
   - **Плюсы**:
     - Код достаточно структурирован и выполняет свои функции.
     - Используется асинхронный подход, что хорошо для обработки веб-запросов.
     - Есть логирование основных операций.
     - Присутствует базовая документация в виде docstrings.
   - **Минусы**:
     - Используется стандартный `logger` вместо `src.logger.logger`.
     -  Не все функции имеют docstring в формате RST.
     - Не все переменные именованы в едином стиле.
     - Есть `print` вместо `logger.info`.
     - Отсутствует обработка ошибок в `robokassa_fail`, кроме вывода в консоль.
     - Использование `f` строк для HTML, что усложняет поддержку и чтение.
     - Разброс в использовании `int()` при преобразовании к целому числу.

**Рекомендации по улучшению**:
   - Необходимо импортировать `logger` из `src.logger.logger`.
   - Добавить RST-документацию для всех функций и классов.
   - Переписать `home_page` с использованием шаблонизатора Jinja2 для более читаемого HTML.
   - Убрать print, заменив его на logger.
   - Добавить обработку ошибок в `robokassa_fail` через `logger.error`.
   - Использовать `j_loads` для обработки JSON.
   - Выровнять именование переменных.
   - Убрать дублирование кода `int()` - использовать сразу после get.
   - Добавить общие `try-except` блоки для более корректной обработки исключений.
   - Использовать константы для magic strings.

**Оптимизированный код**:
```python
"""
Модуль для обработки HTTP-запросов и webhook'ов.
==================================================

Модуль обрабатывает webhook'и от Telegram, запросы от Robokassa,
а также предоставляет главную страницу сервиса.

Пример использования
----------------------
.. code-block:: python

    from aiohttp import web
    from bot.app.app import handle_webhook, home_page, robokassa_result, robokassa_fail

    app = web.Application()
    app.add_routes([
        web.post('/webhook', handle_webhook),
        web.get('/', home_page),
        web.post('/robokassa/result', robokassa_result),
        web.get('/robokassa/fail', robokassa_fail),
    ])
"""
import datetime

from aiohttp import web
from aiogram.types import Update

from src.logger.logger import logger  # Исправленный импорт logger
from bot.app.utils import check_signature_result
from bot.config import bot, dp, settings
from bot.dao.database import async_session_maker
from bot.user.utils import successful_payment_logic

_OK_RESULT = "OK"  # Константа для успешного ответа
_BAD_SIGN_RESULT = "bad sign"  # Константа для неудачного ответа
_PAYMENT_FAILED_TEXT = "Платеж не удался" # Константа для текста ошибки
_ROBOKASSA_PAYMENT_TYPE = "robocassa" # Константа для типа платежа

async def handle_webhook(request: web.Request) -> web.Response:
    """
    Асинхронно обрабатывает входящий webhook от Telegram.

    :param request: HTTP-запрос с данными webhook.
    :type request: web.Request
    :return: HTTP-ответ с кодом 200 в случае успеха, 500 в случае ошибки.
    :rtype: web.Response
    :raises Exception: В случае ошибки при обработке webhook'а.

    Пример:
        >>> from aiohttp import web
        >>> from unittest.mock import AsyncMock, MagicMock
        >>> request_mock = AsyncMock(web.Request)
        >>> request_mock.json = AsyncMock(return_value={})
        >>> dp_mock = MagicMock()
        >>> bot_mock = MagicMock()
        >>> dp_mock.feed_update = AsyncMock()
        >>> dp = dp_mock
        >>> bot = bot_mock
        >>> response = await handle_webhook(request_mock)
        >>> response.status
        200
    """
    try:
        update = Update(**await request.json())
        await dp.feed_update(bot, update)
        return web.Response(status=200)
    except Exception as e:
        logger.error(f"Ошибка при обработке вебхука: {e}") # Используем logger.error
        return web.Response(status=500)


async def home_page(request: web.Request) -> web.Response:
    """
    Асинхронно возвращает HTML-страницу с информацией о сервисе.

    :param request: HTTP-запрос.
    :type request: web.Request
    :return: HTTP-ответ с HTML-страницей.
    :rtype: web.Response

    Пример:
         >>> from aiohttp import web
         >>> request_mock = web.Request(None, None, None, None, None, None)
         >>> response = await home_page(request_mock)
         >>> response.content_type
         'text/html'
    """
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html_content = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>aiohttp Демонстрация</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: 0 auto; }}
            h1 {{ color: #333; }}
            .info {{ background-color: #f4f4f4; padding: 15px; border-radius: 5px; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <h1>Привет, меня зовут Яковенко Алексей</h1>
        <p>Тут вы видите то, что aiohttp способен вполне себе рендерить и HTML странички.</p>
        <div class="info">
            <p>Через aiohttp в данном проекте обрабатываются:</p>
            <ul>
                <li>Хуки от телеграмм бота</li>
                <li>Хуки для обработки ответов от робокассы</li>
            </ul>
        </div>
        <p>Текущее время сервера: {current_time}</p>
    </body>
    </html>
    """
    return web.Response(text=html_content, content_type='text/html')


async def robokassa_result(request: web.Request) -> web.Response:
    """
    Асинхронно обрабатывает запрос от Robokassa на ResultURL.

    :param request: HTTP-запрос от Robokassa.
    :type request: web.Request
    :return: HTTP-ответ с результатом проверки подписи.
    :rtype: web.Response
    :raises Exception: В случае ошибки при обработке запроса.

    Пример:
        >>> from aiohttp import web
        >>> from unittest.mock import AsyncMock, MagicMock
        >>> request_mock = AsyncMock(web.Request)
        >>> request_mock.post = AsyncMock(return_value={'SignatureValue': 'test', 'OutSum': '100', 'InvId': '1', 'Shp_user_id': '1', 'Shp_user_telegram_id': '1', 'Shp_product_id': '1'})
        >>> check_signature_result_mock = MagicMock(return_value=True)
        >>> settings_mock = MagicMock()
        >>> settings_mock.MRH_PASS_2 = 'password'
        >>> bot_mock = MagicMock()
        >>> async_session_mock = MagicMock()
        >>> async_session_mock.return_value.__aenter__.return_value = async_session_mock
        >>> async_session_mock.commit = AsyncMock()
        >>> successful_payment_logic_mock = AsyncMock()
        >>> check_signature_result = check_signature_result_mock
        >>> settings = settings_mock
        >>> bot = bot_mock
        >>> async_session_maker = async_session_mock
        >>> successful_payment_logic = successful_payment_logic_mock
        >>> response = await robokassa_result(request_mock)
        >>> response.text
        'OK1'
    """
    logger.success("Получен ответ от Робокассы!")
    try:
        data = await request.post()

        signature = data.get('SignatureValue')
        out_sum = data.get('OutSum')
        inv_id = data.get('InvId')
        user_id = data.get('Shp_user_id')
        user_telegram_id = data.get('Shp_user_telegram_id')
        product_id = data.get('Shp_product_id')

        if check_signature_result(
            out_sum=out_sum,
            inv_id=inv_id,
            received_signature=signature,
            password=settings.MRH_PASS_2,
            user_id=user_id,
            user_telegram_id=user_telegram_id,
            product_id=product_id
        ):
            result = f"{_OK_RESULT}{inv_id}" # используем константу
            logger.info(f"Успешная проверка подписи для InvId: {inv_id}")

            payment_data = {
                'user_id': int(user_id),
                'payment_id': signature,
                'price': int(out_sum),
                'product_id': int(product_id),
                'payment_type': _ROBOKASSA_PAYMENT_TYPE # используем константу
            }

            async with async_session_maker() as session:
                await successful_payment_logic(
                    session=session,
                    payment_data=payment_data,
                    currency="₽",
                    user_tg_id=int(user_telegram_id),
                    bot=bot
                )
                await session.commit()
        else:
            result = _BAD_SIGN_RESULT  # используем константу
            logger.warning(f"Неверная подпись для InvId: {inv_id}")

        logger.info(f"Ответ: {result}")
        return web.Response(text=result)
    except Exception as e:
          logger.error(f"Ошибка при обработке ответа от робокассы: {e}")
          return web.Response(text=_BAD_SIGN_RESULT)


async def robokassa_fail(request: web.Request) -> web.Response:
    """
    Асинхронно обрабатывает запрос от Robokassa на FailURL.

    :param request: HTTP-запрос от Robokassa.
    :type request: web.Request
    :return: HTTP-ответ с сообщением об ошибке.
    :rtype: web.Response

    Пример:
        >>> from aiohttp import web
        >>> request_mock = web.Request(None, None, None, None, None, None, query_string='InvId=123&OutSum=100')
        >>> response = await robokassa_fail(request_mock)
        >>> response.text
        'Платеж не удался'
    """
    try:
      inv_id = request.query.get('InvId')
      out_sum = request.query.get('OutSum')
      logger.info(f"Неудачный платеж: сумма {out_sum}, ID {inv_id}") # заменили print на logger
      return web.Response(text=_PAYMENT_FAILED_TEXT, content_type='text/html') # используем константу
    except Exception as e:
        logger.error(f"Ошибка при обработке неудачного платежа: {e}")
        return web.Response(text=_PAYMENT_FAILED_TEXT, content_type='text/html')