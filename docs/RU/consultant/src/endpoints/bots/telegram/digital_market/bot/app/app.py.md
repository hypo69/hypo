# Анализ кода модуля app

**Качество кода**
8
- Плюсы
    - Код разбит на логические блоки, каждый из которых выполняет свою функцию.
    - Используется асинхронность для обработки веб-запросов, что хорошо для производительности.
    - Присутствует логирование для отслеживания хода выполнения программы и ошибок.
    - Используется `async_session_maker` для работы с базой данных.
    - Функция `home_page` возвращает HTML-страницу.

- Минусы
    - Отсутствует описание модуля в начале файла.
    - Нет документации в формате RST для функций.
    - В функции `robokassa_fail` используется `print` вместо `logger`, что не соответствует стандартам.
    - Не все переменные и функции имеют согласованные имена с другими файлами.
    - Код не соответствует всем требованиям по форматированию и стилю.

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла.
2.  Добавить документацию в формате RST для всех функций.
3.  Использовать `logger.error` для записи ошибок вместо `print`.
4.  Привести имена переменных и функций в соответствие с ранее обработанными файлами.
5.  Использовать одинарные кавычки в коде, двойные только в операциях вывода.
6.  Улучшить обработку ошибок, избегая лишних `try-except` блоков.
7.  Добавить комментарии для более подробного объяснения логики работы кода.

**Оптимизированный код**

```python
"""
Модуль для запуска и обработки веб-хуков Telegram и Robokassa.
==============================================================

Этот модуль содержит функции для обработки вебхуков от Telegram и Robokassa,
а также для отображения главной страницы сервиса.

Пример использования
--------------------

Пример использования функции `handle_webhook`:

.. code-block:: python

   async def handle_webhook(request: web.Request):
       ...

Пример использования функции `home_page`:

.. code-block:: python

   async def home_page(request: web.Request) -> web.Response:
       ...
"""
import datetime
from pathlib import Path
from typing import Any

from aiohttp import web
from aiogram.types import Update

# from loguru import logger #  заменено на импорт из src.logger
from src.logger.logger import logger
from src.utils.jjson import j_loads  # добавил j_loads
from bot.app.utils import check_signature_result
from bot.config import bot, dp, settings
from bot.dao.database import async_session_maker
from bot.user.utils import successful_payment_logic


async def handle_webhook(request: web.Request) -> web.Response:
    """
    Обрабатывает входящий вебхук от Telegram.

    Args:
        request (web.Request): HTTP-запрос.

    Returns:
        web.Response: Ответ сервера.
    """
    try:
        #  Код извлекает JSON из запроса и создаёт объект Update
        update = Update(**await request.json())
        #  Код передаёт обновление в диспетчер для обработки
        await dp.feed_update(bot, update)
        return web.Response(status=200)
    except Exception as e:
        # Логирует ошибку при обработке вебхука
        logger.error(f'Ошибка при обработке вебхука: {e}')
        return web.Response(status=500)


async def home_page(request: web.Request) -> web.Response:
    """
    Обработчик для отображения главной страницы с информацией о сервисе.

    Args:
         request (web.Request): HTTP-запрос.
    Returns:
        web.Response: HTML-ответ с информацией о сервисе.
    """
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

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
    Обрабатывает запрос от Робокассы на ResultURL.

    Args:
        request (web.Request): HTTP-запрос.

    Returns:
        web.Response: Текстовый ответ с результатами проверки.
    """
    logger.success('Получен ответ от Робокассы!')
    #  Код извлекает данные из POST-запроса
    data = await request.post()

    #  Код извлекает параметры из запроса
    signature = data.get('SignatureValue')
    out_sum = data.get('OutSum')
    inv_id = data.get('InvId')
    user_id = data.get('Shp_user_id')
    user_telegram_id = data.get('Shp_user_telegram_id')
    product_id = data.get('Shp_product_id')

    #  Код проверяет подпись
    if check_signature_result(
        out_sum=out_sum,
        inv_id=inv_id,
        received_signature=signature,
        password=settings.MRH_PASS_2,
        user_id=user_id,
        user_telegram_id=user_telegram_id,
        product_id=product_id,
    ):
        result = f'OK{inv_id}'
        logger.info(f'Успешная проверка подписи для InvId: {inv_id}')
        #  Код подготавливает данные о платеже
        payment_data = {
            'user_id': int(user_id),
            'payment_id': signature,
            'price': int(out_sum),
            'product_id': int(product_id),
            'payment_type': 'robocassa',
        }
        #  Код вызывает логику успешного платежа и коммитит транзакцию
        async with async_session_maker() as session:
            await successful_payment_logic(
                session=session,
                payment_data=payment_data,
                currency='₽',
                user_tg_id=int(user_telegram_id),
                bot=bot,
            )
            await session.commit()
    else:
        result = 'bad sign'
        #  Логирует предупреждение о неверной подписи
        logger.warning(f'Неверная подпись для InvId: {inv_id}')

    logger.info(f'Ответ: {result}')
    return web.Response(text=result)


async def robokassa_fail(request: web.Request) -> web.Response:
    """
    Обрабатывает запрос от Робокассы на FailURL.

    Args:
        request (web.Request): HTTP-запрос.

    Returns:
        web.Response: Текстовый ответ о неудачном платеже.
    """
    #  Код извлекает параметры из GET-запроса
    inv_id = request.query.get('InvId')
    out_sum = request.query.get('OutSum')
    #  Логирует информацию о неудачном платеже
    logger.error(f'Неудачный платеж: сумма {out_sum}, ID {inv_id}')
    return web.Response(text='Платеж не удался', content_type='text/html')