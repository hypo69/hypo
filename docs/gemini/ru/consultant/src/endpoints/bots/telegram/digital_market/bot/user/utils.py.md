# Анализ кода модуля `utils.py`

**Качество кода**
8
- Плюсы
    - Код логически структурирован и выполняет задачу обработки успешной оплаты.
    - Используются асинхронные операции, что хорошо для производительности.
    - Присутствует логирование ошибок.
    - Код достаточно читаемый.
- Минусы
    -  Не хватает документации функций и параметров.
    -  Используется `logger` из `loguru`, когда в проекте принят `src.logger.logger`.
    -  Обработка исключений `try-except` может быть упрощена с использованием `logger.error`.
    -   Используются двойные кавычки в f-строках (не в соответствии с инструкцией).
    -   Не все переменные названы в соответствии с принятыми в проекте стандартами.

**Рекомендации по улучшению**

1.  Добавить docstring к функции `successful_payment_logic` с описанием аргументов и возвращаемого значения.
2.  Заменить импорт `from loguru import logger` на `from src.logger.logger import logger`.
3.  Изменить способ обработки ошибок, используя `logger.error` напрямую в блоке `except`.
4.  Использовать одинарные кавычки в f-строках, где это возможно, в соответствии с инструкцией.
5.  Переименовать `user_tg_id` в `user_id_tg` для соответствия принятому стилю наименования в проекте.
6.  Добавить комментарии для пояснения сложных участков кода.

**Оптимизированный код**

```python
"""
Модуль содержит утилиты для обработки успешных платежей в Telegram боте.
========================================================================
"""
from aiogram import Bot
# from loguru import logger # Заменен на src.logger
from sqlalchemy.ext.asyncio import AsyncSession
from src.bot.config import settings
from src.bot.dao.dao import PurchaseDao, ProductDao
from src.bot.user.kbs import main_user_kb
from src.bot.user.schemas import PaymentData
from src.logger.logger import logger


async def successful_payment_logic(session: AsyncSession, payment_data: dict, currency: str, user_id_tg: int, bot: Bot) -> None:
    """
    Обрабатывает логику успешной оплаты, включая добавление записи о покупке, отправку уведомлений администраторам и пользователю.

    Args:
        session (AsyncSession): Сессия базы данных SQLAlchemy.
        payment_data (dict): Словарь с данными о платеже.
        currency (str): Валюта платежа.
        user_id_tg (int): ID пользователя в Telegram.
        bot (Bot): Объект бота aiogram.

    Returns:
        None
    """
    product_id = int(payment_data.get('product_id'))
    price = payment_data.get('price')
    payment_type = payment_data.get('payment_type')
    payment_id = payment_data.get('payment_id')
    user_id = payment_data.get('user_id')

    # Код добавляет данные о платеже в базу данных
    await PurchaseDao.add(session=session, values=PaymentData(**payment_data))

    # Код получает данные о продукте из базы данных
    product_data = await ProductDao.find_one_or_none_by_id(session=session,
                                                           data_id=product_id)

    # Код отправляет уведомления администраторам о покупке
    for admin_id in settings.ADMIN_IDS:
        try:
            await bot.send_message(
                chat_id=admin_id,
                text=(
                    f'💲 Пользователь c ID {user_id} купил товар <b>{product_data.name}</b> (ID: {product_id}) '
                    f'за <b>{price} {currency}</b>.'
                )
            )
        except Exception as e:
            # Логирование ошибки при отправке уведомления администраторам
            logger.error(f'Ошибка при отправке уведомления администраторам: {e}')

    # Код формирует текст сообщения для пользователя
    file_text = '📦 <b>Товар включает файл:</b>' if product_data.file_id else '📄 <b>Товар не включает файлы:</b>'
    product_text = (
        f'🎉 <b>Спасибо за покупку!</b>\\n\\n'
        f'🛒 <b>Информация о вашем товаре:</b>\\n'
        f'━━━━━━━━━━━━━━━━━━\\n'
        f'🔹 <b>Название:</b> <b>{product_data.name}</b>\\n'
        f'🔹 <b>Описание:</b>\\n<i>{product_data.description}</i>\\n'
        f'🔹 <b>Цена:</b> <b>{price} {currency}</b>\\n'
        f'🔹 <b>Закрытое описание:</b>\\n<i>{product_data.hidden_content}</i>\\n'
        f'━━━━━━━━━━━━━━━━━━\\n'
        f'{file_text}\\n\\n'
        f'ℹ️ <b>Информацию о всех ваших покупках вы можете найти в личном профиле.</b>'
    )

    # Код отправляет сообщение или документ пользователю в зависимости от наличия файла
    if product_data.file_id:
        await bot.send_document(document=product_data.file_id,
                                chat_id=user_id_tg,
                                caption=product_text, reply_markup=main_user_kb(user_id_tg))
    else:
        await bot.send_message(chat_id=user_id_tg, text=product_text, reply_markup=main_user_kb(user_id_tg))

    # Код автоматически возвращает звезды за покупку, если тип оплаты "stars"
    if payment_type == 'stars':
        await bot.refund_star_payment(user_id=user_id_tg, telegram_payment_charge_id=payment_id)
```