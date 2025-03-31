### Анализ кода модуля `catalog_router`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код разбит на логические блоки, что упрощает его понимание.
    - Используются асинхронные функции для неблокирующих операций.
    - Применяется `aiogram` для обработки сообщений и колбеков от Telegram.
- **Минусы**:
    - Некоторые блоки `try-except` излишни, лучше использовать логирование ошибок.
    - Не хватает документации в формате RST для функций и модуля.
    - Отсутствует импорт `logger` из `src.logger`.
    - Не везде используются одинарные кавычки в коде, как указано в инструкции.
    - Не все переменные имеют выравнивание.

**Рекомендации по улучшению**:

- Добавить документацию в формате RST для всех функций и модуля.
- Заменить `try-except` на обработку ошибок через `logger.error`.
- Импортировать `logger` из `src.logger`.
- Использовать одинарные кавычки везде, где это необходимо, согласно инструкции.
- Выровнять названия функций, переменных и импортов в соответствии со стандартами PEP8.
- Улучшить форматирование кода, чтобы соответствовать PEP8.
- В функции `send_stars_invoice` `provider_token` можно удалить, если он не используется, либо добавить комментарий, что токен не требуется.
- В функции `successful_payment` можно использовать более читаемый способ получения `price` и `currency`, например, через тернарный оператор или отдельную функцию.

**Оптимизированный код**:

```python
"""
Модуль для обработки каталога товаров в Telegram боте.
=====================================================

Модуль содержит обработчики callback-запросов и сообщений, связанных с каталогом товаров,
включая просмотр категорий, товаров и проведение оплаты.

Пример использования
--------------------

.. code-block:: python

    from aiogram import Dispatcher
    from src.endpoints.bots.telegram.digital_market.bot.user.catalog_router import catalog_router

    dp = Dispatcher()
    dp.include_router(catalog_router)
"""
from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from sqlalchemy.ext.asyncio import AsyncSession

from src.logger import logger  # импортируем logger
from bot.app.utils import generate_payment_link
from bot.config import bot, settings
from bot.dao.dao import UserDAO, CategoryDao, ProductDao, PurchaseDao
from bot.user.kbs import catalog_kb, product_kb, get_product_buy_youkassa, \
    get_product_buy_stars, get_product_buy_robocassa
from bot.user.schemas import TelegramIDModel, ProductCategoryIDModel, PaymentData
from bot.user.utils import successful_payment_logic

catalog_router = Router()


@catalog_router.callback_query(F.data == 'catalog')
async def page_catalog(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обрабатывает callback-запрос для отображения каталога категорий.

    :param call: Объект CallbackQuery.
    :type call: CallbackQuery
    :param session_without_commit: Асинхронная сессия SQLAlchemy без коммита.
    :type session_without_commit: AsyncSession
    """
    await call.answer('Загрузка каталога...')
    try:
        await call.message.delete()  # удаляем предыдущее сообщение
    except Exception as e:
        logger.error(f'Error deleting message: {e}')  # логируем ошибку удаления сообщения

    catalog_data = await CategoryDao.find_all(session=session_without_commit)

    await call.message.answer(
        text='Выберите категорию товаров:',
        reply_markup=catalog_kb(catalog_data)
    )


@catalog_router.callback_query(F.data.startswith('category_'))
async def page_catalog_products(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обрабатывает callback-запрос для отображения списка товаров в выбранной категории.

    :param call: Объект CallbackQuery.
    :type call: CallbackQuery
    :param session_without_commit: Асинхронная сессия SQLAlchemy без коммита.
    :type session_without_commit: AsyncSession
    """
    category_id = int(call.data.split('_')[-1])
    products_category = await ProductDao.find_all(
        session=session_without_commit,
        filters=ProductCategoryIDModel(category_id=category_id)
    )
    count_products = len(products_category)
    if count_products:
        await call.answer(f'В данной категории {count_products} товаров.')
        for product in products_category:
            product_text = (
                f'📦 <b>Название товара:</b> {product.name}\n\n'
                f'💰 <b>Цена:</b> {product.price} руб.\n\n'
                f'📝 <b>Описание:</b>\n<i>{product.description}</i>\n\n'
                f'━━━━━━━━━━━━━━━━━━'
            )
            await call.message.answer(
                product_text,
                reply_markup=product_kb(product.id, product.price, 1)
            )
    else:
        await call.answer('В данной категории нет товаров.')


@catalog_router.callback_query(F.data.startswith('buy_'))
async def process_about(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обрабатывает callback-запрос для покупки товара.

    :param call: Объект CallbackQuery.
    :type call: CallbackQuery
    :param session_without_commit: Асинхронная сессия SQLAlchemy без коммита.
    :type session_without_commit: AsyncSession
    """
    user_info = await UserDAO.find_one_or_none(
        session=session_without_commit,
        filters=TelegramIDModel(telegram_id=call.from_user.id)
    )
    _, payment_type, product_id, price = call.data.split('_')

    if payment_type == 'yukassa':
        await send_yukassa_invoice(call, user_info, product_id, price)
    elif payment_type == 'stars':
        await send_stars_invoice(call, user_info, product_id, 10)
    elif payment_type == 'robocassa':
        await send_robocassa_invoice(call, user_info, product_id, price, session_without_commit)

    await call.message.delete()


async def send_yukassa_invoice(call: CallbackQuery, user_info, product_id: int, price: str):
    """
    Отправляет инвойс для оплаты через ЮKassa.

    :param call: Объект CallbackQuery.
    :type call: CallbackQuery
    :param user_info: Информация о пользователе.
    :type user_info: User
    :param product_id: ID продукта.
    :type product_id: int
    :param price: Цена товара.
    :type price: str
    """
    await bot.send_invoice(
        chat_id=call.from_user.id,
        title=f'Оплата 👉 {price}₽',
        description=f'Пожалуйста, завершите оплату в размере {price}₽, чтобы открыть доступ к выбранному товару.',
        payload=f'yukassa_{user_info.id}_{product_id}',
        provider_token=settings.PROVIDER_TOKEN,
        currency='rub',
        prices=[LabeledPrice(
            label=f'Оплата {price}',
            amount=int(price) * 100
        )],
        reply_markup=get_product_buy_youkassa(price)
    )


async def send_robocassa_invoice(call: CallbackQuery, user_info, product_id: int, price: str, session: AsyncSession):
    """
    Отправляет сообщение с ссылкой для оплаты через Robocassa.

    :param call: Объект CallbackQuery.
    :type call: CallbackQuery
    :param user_info: Информация о пользователе.
    :type user_info: User
    :param product_id: ID продукта.
    :type product_id: int
    :param price: Цена товара.
    :type price: str
    :param session: Асинхронная сессия SQLAlchemy.
    :type session: AsyncSession
    """
    pay_id = await PurchaseDao.get_next_id(session=session)
    text = f'Пожалуйста, завершите оплату в размере {price}₽, чтобы открыть доступ к выбранному товару.'
    description = f'Оплата за товар: ID {user_info.id} ({price}₽)'
    payment_link = generate_payment_link(
        cost=float(price),
        number=pay_id,
        description=description,
        user_id=user_info.id,
        user_telegram_id=call.from_user.id,
        product_id=product_id
    )
    kb = get_product_buy_robocassa(price, payment_link)
    await call.message.answer(text, reply_markup=kb)


async def send_stars_invoice(call: CallbackQuery, user_info, product_id: int, stars_price: int):
    """
    Отправляет инвойс для оплаты звездами.

    :param call: Объект CallbackQuery.
    :type call: CallbackQuery
    :param user_info: Информация о пользователе.
    :type user_info: User
    :param product_id: ID продукта.
    :type product_id: int
    :param stars_price: Цена в звездах.
    :type stars_price: int
    """
    await bot.send_invoice(
        chat_id=call.from_user.id,
        title=f'Оплата 👉 {stars_price} ⭐',
        description=f'Пожалуйста, завершите оплату в размере {stars_price} звезд, '
                    f'чтобы открыть доступ к выбранному товару.',
        payload=f'stars_{user_info.id}_{product_id}',
        provider_token="",  # токен не требуется для звезд
        currency='XTR',
        prices=[LabeledPrice(
            label=f'Оплата {stars_price} ⭐',
            amount=int(stars_price)
        )],
        reply_markup=get_product_buy_stars(stars_price)
    )


@catalog_router.pre_checkout_query(lambda query: True)
async def pre_checkout_query(pre_checkout_q: PreCheckoutQuery):
    """
    Обрабатывает pre-checkout query.

    :param pre_checkout_q: Объект PreCheckoutQuery.
    :type pre_checkout_q: PreCheckoutQuery
    """
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


@catalog_router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message, session_with_commit: AsyncSession):
    """
    Обрабатывает успешный платеж.

    :param message: Объект Message с информацией об успешном платеже.
    :type message: Message
    :param session_with_commit: Асинхронная сессия SQLAlchemy с коммитом.
    :type session_with_commit: AsyncSession
    """
    payment_info = message.successful_payment
    payment_type, user_id, product_id = payment_info.invoice_payload.split('_')

    if payment_type == 'stars':
        price = payment_info.total_amount
        currency = '⭐'
    else:
        price = payment_info.total_amount / 100
        currency = '₽'
    payment_data = {
        'user_id': int(user_id),
        'payment_id': payment_info.telegram_payment_charge_id,
        'price': price,
        'product_id': int(product_id),
        'payment_type': payment_type
    }

    await successful_payment_logic(
        session=session_with_commit,
        payment_data=payment_data,
        currency=currency,
        user_tg_id=message.from_user.id,
        bot=bot
    )