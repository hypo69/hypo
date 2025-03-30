### Анализ кода модуля `user_router`

**Качество кода:**
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код хорошо структурирован, с разделением на обработку разных callback query.
    - Используется `AsyncSession` для работы с базой данных.
    - Применяются f-строки для форматирования текста.
- **Минусы**:
    - Не все текстовые сообщения вынесены в константы или переменные.
    - Присутствует блок `try-except` без обработки ошибки (просто `pass`).
    - Используется `call.message.reply_markup` без необходимости, так как это не изменяет поведение.
    - Комментарии в коде отсутствуют.

**Рекомендации по улучшению:**
- Добавить docstring к каждой функции для улучшения читаемости и документирования.
- Заменить `try-except` на логирование ошибки через `logger.error`.
- Упростить использование `call.message.reply_markup`, где это возможно.
- Использовать константы для текстовых сообщений, особенно если они используются несколько раз.
- Добавить комментарии для пояснения логики в ключевых местах.

**Оптимизированный код:**
```python
"""
Модуль для обработки пользовательских запросов в Telegram боте.
=============================================================

Модуль содержит роутер (:class:`user_router`) для обработки команд и callback-запросов,
связанных с пользователями. Включает обработку команды start, отображение главной страницы,
информацию о магазине, профиль пользователя и список его покупок.

Пример использования
----------------------
.. code-block:: python

    from aiogram import Dispatcher
    from src.endpoints.bots.telegram.digital_market.bot.user.user_router import user_router
    dp = Dispatcher()
    dp.include_router(user_router)
"""
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from src.logger import logger  # Исправлен импорт logger
from bot.dao.dao import UserDAO
from bot.user.kbs import main_user_kb, purchases_kb
from bot.user.schemas import TelegramIDModel, UserModel

user_router = Router()

HOME_TEXT = '👋 Привет, {full_name}! Выберите необходимое действие'
REGISTRATION_TEXT = '🎉 <b>Благодарим за регистрацию!</b>. Теперь выберите необходимое действие.'
MAIN_PAGE_TEXT = "Главная страница"
PROFILE_TEXT = "Профиль"
NO_PURCHASES_TEXT = "🔍 <b>У вас пока нет покупок.</b>\\n\\nОткройте каталог и выберите что-нибудь интересное!"
PURCHASE_HISTORY_TEXT = "🛍 <b>Ваш профиль:</b>\\n\\nКоличество покупок: <b>{total_purchases}</b>\\nОбщая сумма: <b>{total_amount}₽</b>\\n\\nХотите просмотреть детали ваших покупок?"
MY_PURCHASES_TEXT = "Мои покупки"
THANKS_FOR_TRUST_TEXT = "🙏 Спасибо за доверие!"


@user_router.message(CommandStart())
async def cmd_start(message: Message, session_with_commit: AsyncSession):
    """
    Обрабатывает команду /start.

    Ищет пользователя в базе данных. Если пользователь существует, отправляет приветственное сообщение.
    Если пользователя нет, регистрирует его и отправляет приветственное сообщение.

    :param message: Объект Message от aiogram.
    :type message: Message
    :param session_with_commit: Сессия для работы с базой данных.
    :type session_with_commit: AsyncSession
    :return: None
    :rtype: None
    """
    user_id = message.from_user.id
    user_info = await UserDAO.find_one_or_none(
        session=session_with_commit,
        filters=TelegramIDModel(telegram_id=user_id)
    )
    # Проверяем, существует ли пользователь
    if user_info:
        # Отправляем приветственное сообщение, если пользователь найден
        await message.answer(
            HOME_TEXT.format(full_name=message.from_user.full_name),
            reply_markup=main_user_kb(user_id)
        )
        return
    # Создаем модель пользователя, если пользователь не найден
    values = UserModel(
        telegram_id=user_id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    # Добавляем пользователя в базу данных
    await UserDAO.add(session=session_with_commit, values=values)
    # Отправляем сообщение о регистрации
    await message.answer(REGISTRATION_TEXT, reply_markup=main_user_kb(user_id))


@user_router.callback_query(F.data == "home")
async def page_home(call: CallbackQuery):
    """
    Обрабатывает callback-запрос для отображения главной страницы.

    Отправляет приветственное сообщение с главным меню.

    :param call: CallbackQuery от aiogram.
    :type call: CallbackQuery
    :return: None
    :rtype: None
    """
    await call.answer(MAIN_PAGE_TEXT)
    await call.message.answer(
        HOME_TEXT.format(full_name=call.from_user.full_name),
        reply_markup=main_user_kb(call.from_user.id)
    )


@user_router.callback_query(F.data == "about")
async def page_about(call: CallbackQuery):
    """
    Обрабатывает callback-запрос для отображения информации о магазине.

    Отправляет текстовое сообщение с информацией о магазине.

    :param call: CallbackQuery от aiogram.
    :type call: CallbackQuery
    :return: None
    :rtype: None
    """
    await call.answer("О магазине")
    await call.message.answer(
        text=(
            "🎓 Добро пожаловать в наш учебный магазин!\\n\\n"
            "🚀 Этот бот создан как демонстрационный проект для статьи на Хабре.\\n\\n"
            "👨\u200d💻 Автор: Яковенко Алексей\\n\\n"
            "🛍️ Здесь вы можете изучить принципы работы телеграм-магазина, "
            "ознакомиться с функциональностью и механизмами взаимодействия с пользователем.\\n\\n"
            "📚 Этот проект - это отличный способ погрузиться в мир разработки ботов "
            "и электронной коммерции в Telegram.\\n\\n"
            "💡 Исследуйте, учитесь и вдохновляйтесь!\\n\\n"
            "Данные для тестовой оплаты:\\n\\n"
            "Карта: 1111 1111 1111 1026\\n"
            "Годен до: 12/26\\n"
            "CVC-код: 000\\n"
        ),
        reply_markup=call.message.reply_markup # Сохраняем текущую разметку
    )


@user_router.callback_query(F.data == "my_profile")
async def page_profile(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обрабатывает callback-запрос для отображения профиля пользователя.

    Получает статистику покупок пользователя и отправляет соответствующее сообщение.

    :param call: CallbackQuery от aiogram.
    :type call: CallbackQuery
    :param session_without_commit: Сессия для работы с базой данных.
    :type session_without_commit: AsyncSession
    :return: None
    :rtype: None
    """
    await call.answer(PROFILE_TEXT)
    # Получаем статистику покупок пользователя
    purchases = await UserDAO.get_purchase_statistics(session=session_without_commit, telegram_id=call.from_user.id)
    total_amount = purchases.get('total_amount', 0)
    total_purchases = purchases.get('total_purchases', 0)
    # Проверяем, есть ли у пользователя покупки
    if total_purchases == 0:
        # Отправляем сообщение, если покупок нет
        await call.message.answer(
            text=NO_PURCHASES_TEXT,
            reply_markup=main_user_kb(call.from_user.id)
        )
    else:
        # Формируем сообщение о профиле, если есть покупки
        text = PURCHASE_HISTORY_TEXT.format(total_purchases=total_purchases, total_amount=total_amount)
        await call.message.answer(
            text=text,
            reply_markup=purchases_kb()
        )


@user_router.callback_query(F.data == "purchases")
async def page_user_purchases(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обрабатывает callback-запрос для отображения списка покупок пользователя.

    Получает список покупок и выводит информацию о каждой покупке.

    :param call: CallbackQuery от aiogram.
    :type call: CallbackQuery
    :param session_without_commit: Сессия для работы с базой данных.
    :type session_without_commit: AsyncSession
    :return: None
    :rtype: None
    """
    await call.answer(MY_PURCHASES_TEXT)
    try:
        await call.message.delete()  # Удаляем предыдущее сообщение
    except Exception as e:
        logger.error(f"Error deleting message: {e}") # Логируем ошибку, если не удалось удалить сообщение
    # Получаем список покупок пользователя
    purchases = await UserDAO.get_purchased_products(session=session_without_commit, telegram_id=call.from_user.id)

    if not purchases:
        # Отправляем сообщение, если нет покупок
        await call.message.answer(
            text=NO_PURCHASES_TEXT,
            reply_markup=main_user_kb(call.from_user.id)
        )
        return

    # Для каждой покупки отправляем информацию
    for purchase in purchases:
        product = purchase.product
        file_text = "📦 <b>Товар включает файл:</b>" if product.file_id else "📄 <b>Товар не включает файлы:</b>"

        product_text = (
            f"🛒 <b>Информация о вашем товаре:</b>\\n"
            f"━━━━━━━━━━━━━━━━━━\\n"
            f"🔹 <b>Название:</b> <i>{product.name}</i>\\n"
            f"🔹 <b>Описание:</b>\\n<i>{product.description}</i>\\n"
            f"🔹 <b>Цена:</b> <b>{product.price} ₽</b>\\n"
            f"🔹 <b>Закрытое описание:</b>\\n<i>{product.hidden_content}</i>\\n"
            f"━━━━━━━━━━━━━━━━━━\\n"
            f"{file_text}\\n"
        )

        if product.file_id:
            # Отправляем файл с текстом
            await call.message.answer_document(
                document=product.file_id,
                caption=product_text,
            )
        else:
            # Отправляем только текст
            await call.message.answer(
                text=product_text,
            )

    # Отправляем заключительное сообщение
    await call.message.answer(
        text=THANKS_FOR_TRUST_TEXT,
        reply_markup=main_user_kb(call.from_user.id)
    )