# Анализ кода модуля `utils`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код достаточно логичен и структурирован.
    - Используются асинхронные операции, что хорошо для Telegram-бота.
    - Присутствуют комментарии, которые в целом описывают логику.
- **Минусы**:
    -  Используются двойные кавычки в тексте.
    -  Используется `logger` из `loguru`, а не из `src.logger`.
    -  Текст для сообщений с большим количеством форматирования сложен для чтения.
    -  Отсутствует RST-документация для функции.
    -  Используется `try-except` для обработки ошибок отправки сообщений.

**Рекомендации по улучшению:**

1. **Импорт логгера**: Измените импорт логгера на `from src.logger import logger`.
2.  **Форматирование строк**: Переформатируйте текст для сообщений, чтобы он был более читаемым, и используйте одинарные кавычки для строк, кроме тех, что используются в функциях логирования и вывода.
3.  **RST-документация**: Добавьте RST-документацию для функции `successful_payment_logic`.
4.  **Обработка ошибок**: Замените блок `try-except` на `logger.error` для обработки ошибок отправки сообщений.
5.  **Использование f-строк**: Используйте f-строки для форматирования текста.
6. **Комментарии**: Уточните комментарии, чтобы они были более информативными и описывали действия, а не просто констатировали их наличие.

**Оптимизированный код:**

```python
from aiogram import Bot
from sqlalchemy.ext.asyncio import AsyncSession
from src.logger import logger  # Исправлен импорт логгера
from bot.config import settings
from bot.dao.dao import PurchaseDao, ProductDao
from bot.user.kbs import main_user_kb
from bot.user.schemas import PaymentData


async def successful_payment_logic(
    session: AsyncSession, payment_data: dict, currency: str, user_tg_id: int, bot: Bot
) -> None:
    """
    Обрабатывает успешную оплату, добавляет запись о покупке в БД,
    отправляет уведомления администраторам и пользователю.

    :param session: Сессия SQLAlchemy для работы с БД.
    :type session: AsyncSession
    :param payment_data: Данные об оплате.
    :type payment_data: dict
    :param currency: Валюта оплаты.
    :type currency: str
    :param user_tg_id: Telegram ID пользователя.
    :type user_tg_id: int
    :param bot: Экземпляр Telegram бота.
    :type bot: Bot
    :raises Exception: В случае ошибки при отправке уведомлений администраторам.

    Пример использования:
        >>> from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
        >>> from aiogram import Bot
        >>> from unittest.mock import AsyncMock
        >>> async def test_successful_payment_logic():
        ...     engine = create_async_engine("sqlite+aiosqlite:///:memory:")
        ...     async with engine.begin() as conn:
        ...         await conn.run_sync(Base.metadata.create_all)
        ...     async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
        ...     async with async_session() as session:
        ...         bot_mock = AsyncMock(spec=Bot)
        ...         payment_data = {
        ...             "product_id": "1",
        ...             "price": "100",
        ...             "payment_type": "stars",
        ...             "payment_id": "123",
        ...             "user_id": "456",
        ...         }
        ...         await successful_payment_logic(
        ...             session=session,
        ...             payment_data=payment_data,
        ...             currency="USD",
        ...             user_tg_id=123,
        ...             bot=bot_mock
        ...         )
        ...         assert bot_mock.send_message.call_count > 0
        ...         assert bot_mock.send_document.call_count == 0
    """
    product_id = int(payment_data.get('product_id'))
    price = payment_data.get('price')
    payment_type = payment_data.get('payment_type')
    payment_id = payment_data.get('payment_id')
    user_id = payment_data.get('user_id')

    await PurchaseDao.add(session=session, values=PaymentData(**payment_data)) # Добавляем запись о покупке в БД
    product_data = await ProductDao.find_one_or_none_by_id(session=session, data_id=product_id) # Получаем данные о товаре

    for admin_id in settings.ADMIN_IDS: # Отправляем уведомления администраторам
        try:
             await bot.send_message(
                chat_id=admin_id,
                text=(
                    f'💲 Пользователь c ID {user_id} купил товар <b>{product_data.name}</b> (ID: {product_id}) '
                    f'за <b>{price} {currency}</b>.'
                )
             )
        except Exception as e:
           logger.error(f'Ошибка при отправке уведомления администраторам: {e}')# Обработка ошибок отправки сообщений через логгер


    file_text = '📦 <b>Товар включает файл:</b>' if product_data.file_id else '📄 <b>Товар не включает файлы:</b>' # Определяем текст для сообщения в зависимости от наличия файла

    product_text = ( # Формируем текст сообщения для пользователя
        '🎉 <b>Спасибо за покупку!</b>\\n\\n'
        '🛒 <b>Информация о вашем товаре:</b>\\n'
        '━━━━━━━━━━━━━━━━━━\\n'
        f'🔹 <b>Название:</b> <b>{product_data.name}</b>\\n'
        f'🔹 <b>Описание:</b>\\n<i>{product_data.description}</i>\\n'
        f'🔹 <b>Цена:</b> <b>{price} {currency}</b>\\n'
        f'🔹 <b>Закрытое описание:</b>\\n<i>{product_data.hidden_content}</i>\\n'
        '━━━━━━━━━━━━━━━━━━\\n'
        f'{file_text}\\n\\n'
        'ℹ️ <b>Информацию о всех ваших покупках вы можете найти в личном профиле.</b>'
    )


    if product_data.file_id: # Отправляем документ, если он есть
        await bot.send_document(
            document=product_data.file_id,
            chat_id=user_tg_id,
            caption=product_text,
            reply_markup=main_user_kb(user_tg_id)
        )
    else:
        await bot.send_message(chat_id=user_tg_id, text=product_text, reply_markup=main_user_kb(user_tg_id)) # Отправляем сообщение, если файла нет

    if payment_type == 'stars': # Если оплата звездами, возвращаем звезды пользователю
        await bot.refund_star_payment(user_id=user_tg_id, telegram_payment_charge_id=payment_id)
```