# Анализ кода модуля `catalog_router.py`

**Качество кода: 7/10**
- Плюсы:
    - Код разбит на логические блоки, что облегчает чтение и понимание.
    - Используются асинхронные функции для неблокирующих операций.
    - Присутствует обработка ошибок (хоть и минимальная).
    - Код в целом соответствует стандартам PEP 8.
    - Используются `CallbackQuery` для обработки действий пользователя.
    - Присутствует валидация данных через `F.data.startswith`, `lambda query: True`.
- Минусы:
    - Отсутствует подробная документация (docstrings) для функций, что затрудняет понимание их назначения и использования.
    - Использование `try-except` без конкретизации исключения.
    - Не используются `j_loads` или `j_loads_ns` для чтения данных из файлов.
    - Отсутствует логирование ошибок.
    - Жестко заданы значения `currency` (например, `'rub'`, `'XTR'`) в функциях `send_yukassa_invoice`, `send_stars_invoice`.
    - Жестко задано значение `amount=int(price) * 100` и `amount=int(stars_price)` в функциях `send_yukassa_invoice`, `send_stars_invoice`.
    - Много дублирования кода при отправке инвойсов, например, `bot.send_invoice` с разными параметрами.
    - `user_info` передается во все функции по работе с инвойсами, но не используется.

**Рекомендации по улучшению**

1. **Документирование:** Добавить docstrings к каждой функции, переменной и классу.
2. **Логирование:** Добавить логирование ошибок с помощью `logger.error` из `src.logger.logger`.
3. **Обработка ошибок:** Заменить общие `try-except` на более конкретные, обрабатывая определенные типы исключений.
4. **Использование `j_loads`:** В данном коде нет операций чтения из файла, но в будущем следует использовать `j_loads` или `j_loads_ns`.
5. **Рефакторинг:** 
   - Вынести логику отправки инвойсов в отдельные функции, чтобы избежать дублирования кода.
   - Убрать не используемый `user_info` параметр из функций.
6. **Улучшение читаемости:** Разделить длинные строки кода на несколько более коротких строк.
7. **Использовать enum для `payment_type`** .

**Оптимизированный код**
```python
"""
Модуль для обработки запросов каталога товаров и платежей в Telegram боте.
========================================================================

Этот модуль содержит обработчики для отображения каталога товаров,
выбора товаров и проведения платежей через различные платежные системы.
"""
from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from sqlalchemy.ext.asyncio import AsyncSession

# from src.utils.jjson import j_loads, j_loads_ns # TODO: Пока не используется
from src.logger.logger import logger
from bot.app.utils import generate_payment_link
from bot.config import bot, settings
from bot.dao.dao import UserDAO, CategoryDao, ProductDao, PurchaseDao
from bot.user.kbs import catalog_kb, product_kb, get_product_buy_youkassa, \
    get_product_buy_stars, get_product_buy_robocassa
from bot.user.schemas import TelegramIDModel, ProductCategoryIDModel, PaymentData
from bot.user.utils import successful_payment_logic
from enum import Enum

catalog_router = Router()


class PaymentType(str, Enum):
    """
    Enum для определения типа платежной системы.
    """
    YUKASSA = 'yukassa'
    STARS = 'stars'
    ROBOCASSA = 'robocassa'

@catalog_router.callback_query(F.data == 'catalog')
async def page_catalog(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обрабатывает запрос на отображение каталога.

    Args:
        call (CallbackQuery): Объект обратного вызова от Telegram.
        session_without_commit (AsyncSession): Сессия SQLAlchemy для работы с БД без коммита.
    """
    await call.answer('Загрузка каталога...')
    try:
        await call.message.delete()
    except Exception as e:
        logger.error('Ошибка при удалении сообщения', exc_info=e)

    catalog_data = await CategoryDao.find_all(session=session_without_commit)

    await call.message.answer(
        text='Выберите категорию товаров:',
        reply_markup=catalog_kb(catalog_data)
    )


@catalog_router.callback_query(F.data.startswith('category_'))
async def page_catalog_products(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обрабатывает запрос на отображение товаров в выбранной категории.

    Args:
        call (CallbackQuery): Объект обратного вызова от Telegram.
        session_without_commit (AsyncSession): Сессия SQLAlchemy для работы с БД без коммита.
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
    Обрабатывает запрос на покупку товара.

    Args:
        call (CallbackQuery): Объект обратного вызова от Telegram.
        session_without_commit (AsyncSession): Сессия SQLAlchemy для работы с БД без коммита.
    """
    user_info = await UserDAO.find_one_or_none(
        session=session_without_commit,
        filters=TelegramIDModel(telegram_id=call.from_user.id)
    )
    _, payment_type, product_id, price = call.data.split('_')
    payment_type = PaymentType(payment_type)
    if payment_type == PaymentType.YUKASSA:
        await send_invoice(call, product_id, price, payment_type)
    elif payment_type == PaymentType.STARS:
        await send_invoice(call, product_id, 10, payment_type)
    elif payment_type == PaymentType.ROBOCASSA:
        await send_robocassa_invoice(call, product_id, price, session_without_commit)

    await call.message.delete()


async def send_invoice(call: CallbackQuery, product_id: str, price: int | float, payment_type: PaymentType):
    """
    Отправляет инвойс для оплаты.

    Args:
        call (CallbackQuery): Объект обратного вызова от Telegram.
        product_id (str): ID продукта.
        price (int | float): Цена товара.
        payment_type (PaymentType): Тип платежной системы.
    """
    currency = 'rub' if payment_type == PaymentType.YUKASSA else 'XTR'
    amount = int(price) * 100 if payment_type == PaymentType.YUKASSA else int(price)
    title = f'Оплата 👉 {price}{"₽" if currency == "rub" else " ⭐"}'
    description = (
        f'Пожалуйста, завершите оплату в размере {price}{"₽" if currency == "rub" else " ⭐"}, '
        f'чтобы открыть доступ к выбранному товару.'
    )
    payload = f"{payment_type.value}_{call.from_user.id}_{product_id}"
    
    if payment_type == PaymentType.YUKASSA:
       reply_markup = get_product_buy_youkassa(price)
       provider_token = settings.PROVIDER_TOKEN
    elif payment_type == PaymentType.STARS:
         reply_markup = get_product_buy_stars(price)
         provider_token = ""
    else:
        logger.error(f'Не известный тип оплаты {payment_type=}')
        return

    await bot.send_invoice(
        chat_id=call.from_user.id,
        title=title,
        description=description,
        payload=payload,
        provider_token=provider_token,
        currency=currency,
        prices=[LabeledPrice(label=f'Оплата {price}', amount=amount)],
        reply_markup=reply_markup
    )



async def send_robocassa_invoice(
    call: CallbackQuery, product_id: str, price: str, session: AsyncSession
):
    """
     Отправляет инвойс для оплаты через Robocassa.

    Args:
        call (CallbackQuery): Объект обратного вызова от Telegram.
        product_id (str): ID продукта.
        price (str): Цена товара.
        session (AsyncSession): Сессия SQLAlchemy для работы с БД.
    """
    try:
        price = float(price)
    except ValueError as e:
        logger.error(f'Некорректный формат цены {price=}', exc_info=e)
        return

    user_info = await UserDAO.find_one_or_none(
        session=session,
        filters=TelegramIDModel(telegram_id=call.from_user.id)
    )

    pay_id = await PurchaseDao.get_next_id(session=session)
    text = f'Пожалуйста, завершите оплату в размере {price}₽, чтобы открыть доступ к выбранному товару.'
    description = f"Оплата за товар: ID {user_info.id} ({price}₽)"
    payment_link = generate_payment_link(
        cost=price,
        number=pay_id,
        description=description,
        user_id=user_info.id,
        user_telegram_id=call.from_user.id,
        product_id=product_id
    )
    kb = get_product_buy_robocassa(price, payment_link)
    await call.message.answer(text, reply_markup=kb)


@catalog_router.pre_checkout_query(lambda query: True)
async def pre_checkout_query(pre_checkout_q: PreCheckoutQuery):
    """
    Обрабатывает предварительный запрос перед подтверждением платежа.

    Args:
        pre_checkout_q (PreCheckoutQuery): Объект предварительного запроса от Telegram.
    """
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


@catalog_router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message, session_with_commit: AsyncSession):
    """
    Обрабатывает успешный платеж.

    Args:
        message (Message): Объект сообщения от Telegram.
        session_with_commit (AsyncSession): Сессия SQLAlchemy для работы с БД с коммитом.
    """
    payment_info = message.successful_payment
    payment_type, user_id, product_id = payment_info.invoice_payload.split('_')
    payment_type = PaymentType(payment_type)
    if payment_type == PaymentType.STARS:
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
        'payment_type': payment_type.value
    }

    await successful_payment_logic(
        session=session_with_commit,
        payment_data=payment_data,
        currency=currency,
        user_tg_id=message.from_user.id,
        bot=bot
    )