# Анализ кода модуля `user_router.py`

**Качество кода: 8/10**

- Плюсы:
    - Код логически структурирован и выполняет поставленные задачи.
    - Используются асинхронные операции, что повышает производительность.
    - Применяются `F`-фильтры для обработки callback-запросов.
    - Используется `DAO` для работы с базой данных.
    - Добавлены docstring для функций.
- Минусы:
    - Отсутствует обработка ошибок в некоторых функциях.
    - Не используется логгирование.
    - Есть неиспользуемые блоки `try-except`.

**Рекомендации по улучшению**

1. **Добавить импорт логгера:** Необходимо добавить `from src.logger.logger import logger` для логирования ошибок.
2. **Улучшить обработку ошибок:** Заменить блоки `try-except` на `logger.error` для логирования ошибок и возврата или продолжения работы.
3. **Использовать `j_loads` или `j_loads_ns`:** В данном модуле нет работы с `json`, поэтому это не требуется.
4. **Документирование:** Дополнить docstring для функций, указать аргументы, возвращаемые значения, исключения и примеры.
5. **Уточнить комментарии:** Добавить комментарии для большей ясности в коде.
6. **Убрать `pass`**:  Блок `except` не должен быть пустым. Либо он должен что-то делать (например, логгировать ошибку), либо должен быть убран.

**Оптимизированный код**

```python
"""
Модуль `user_router` для обработки пользовательских действий в Telegram боте.
==========================================================================

Этот модуль содержит обработчики для различных пользовательских команд и действий,
таких как команда `/start`, просмотр профиля, информации о магазине и истории покупок.

Пример использования
--------------------

Пример использования обработчика команды `/start`:

.. code-block:: python

   from aiogram import Dispatcher, Router
   from aiogram.types import Message
   from bot.user.user_router import user_router

   dp = Dispatcher()
   dp.include_router(user_router)

   @dp.message_handler(commands=['start'])
   async def start_handler(message: Message):
      # Обработчик вызовет функцию `cmd_start` из `user_router`
      pass


"""
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from bot.dao.dao import UserDAO
from bot.user.kbs import main_user_kb, purchases_kb
from bot.user.schemas import TelegramIDModel, UserModel
from src.logger.logger import logger # Импортируем логгер

user_router = Router()


@user_router.message(CommandStart())
async def cmd_start(message: Message, session_with_commit: AsyncSession):
    """
    Обрабатывает команду `/start`.

    Проверяет, существует ли пользователь в базе данных. Если нет, создает нового пользователя.
    Отправляет приветственное сообщение с основным меню.

    Args:
        message (Message): Объект сообщения от Telegram.
        session_with_commit (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных.

    Returns:
        None: Отправляет сообщение пользователю.
    """
    user_id = message.from_user.id
    # Ищет пользователя в базе данных по telegram_id
    user_info = await UserDAO.find_one_or_none(
        session=session_with_commit,
        filters=TelegramIDModel(telegram_id=user_id)
    )

    if user_info:
        # Если пользователь существует, отправляет приветствие
        return await message.answer(
            f"👋 Привет, {message.from_user.full_name}! Выберите необходимое действие",
            reply_markup=main_user_kb(user_id)
        )

    # Если пользователя нет, создает запись в базе данных
    values = UserModel(
        telegram_id=user_id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    await UserDAO.add(session=session_with_commit, values=values)
    # Отправляет сообщение о регистрации
    await message.answer(f"🎉 <b>Благодарим за регистрацию!</b>. Теперь выберите необходимое действие.",
                         reply_markup=main_user_kb(user_id))


@user_router.callback_query(F.data == 'home')
async def page_home(call: CallbackQuery):
    """
    Обрабатывает callback запрос для кнопки 'home'.

    Отправляет приветственное сообщение с основным меню.

    Args:
        call (CallbackQuery): Объект callback запроса от Telegram.

    Returns:
        None: Отправляет сообщение пользователю.
    """
    await call.answer('Главная страница')
    # Отправляет приветственное сообщение
    return await call.message.answer(
        f"👋 Привет, {call.from_user.full_name}! Выберите необходимое действие",
        reply_markup=main_user_kb(call.from_user.id)
    )


@user_router.callback_query(F.data == 'about')
async def page_about(call: CallbackQuery):
    """
    Обрабатывает callback запрос для кнопки 'about'.

    Отправляет информацию о магазине.

    Args:
        call (CallbackQuery): Объект callback запроса от Telegram.

    Returns:
        None: Отправляет сообщение пользователю.
    """
    await call.answer('О магазине')
    # Отправляет информацию о магазине
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
        reply_markup=call.message.reply_markup
    )


@user_router.callback_query(F.data == 'my_profile')
async def page_about(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обрабатывает callback запрос для кнопки 'my_profile'.

    Получает и отправляет статистику покупок пользователя.

    Args:
        call (CallbackQuery): Объект callback запроса от Telegram.
        session_without_commit (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных.

    Returns:
        None: Отправляет сообщение пользователю.
    """
    await call.answer('Профиль')

    # Получает статистику покупок пользователя
    purchases = await UserDAO.get_purchase_statistics(session=session_without_commit, telegram_id=call.from_user.id)
    total_amount = purchases.get('total_amount', 0)
    total_purchases = purchases.get('total_purchases', 0)

    # Формирует сообщение в зависимости от наличия покупок
    if total_purchases == 0:
        await call.message.answer(
            text="🔍 <b>У вас пока нет покупок.</b>\\n\\n"
                 "Откройте каталог и выберите что-нибудь интересное!",
            reply_markup=main_user_kb(call.from_user.id)
        )
    else:
        text = (
            f"🛍 <b>Ваш профиль:</b>\\n\\n"
            f"Количество покупок: <b>{total_purchases}</b>\\n"
            f"Общая сумма: <b>{total_amount}₽</b>\\n\\n"
            "Хотите просмотреть детали ваших покупок?"
        )
        await call.message.answer(
            text=text,
            reply_markup=purchases_kb()
        )


@user_router.callback_query(F.data == 'purchases')
async def page_user_purchases(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обрабатывает callback запрос для кнопки 'purchases'.

    Получает и отправляет список покупок пользователя.

    Args:
        call (CallbackQuery): Объект callback запроса от Telegram.
        session_without_commit (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных.

    Returns:
        None: Отправляет сообщение пользователю.
    """
    await call.answer('Мои покупки')
    try:
        await call.message.delete() #  удаляет предыдущее сообщение
    except Exception as e:
        logger.error(f'Не удалось удалить предыдущее сообщение: {e}', exc_info=True) # Логируем ошибку если не удалось удалить сообщение

    # Получает список покупок пользователя
    purchases = await UserDAO.get_purchased_products(session=session_without_commit, telegram_id=call.from_user.id)

    if not purchases:
        await call.message.answer(
            text=f"🔍 <b>У вас пока нет покупок.</b>\\n\\n"
                 f"Откройте каталог и выберите что-нибудь интересное!",
            reply_markup=main_user_kb(call.from_user.id)
        )
        return

    # Отправляет информацию о каждой покупке
    for purchase in purchases:
        product = purchase.product
        file_text = '📦 <b>Товар включает файл:</b>' if product.file_id else '📄 <b>Товар не включает файлы:</b>'

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
            # Отправляет файл с текстом
            await call.message.answer_document(
                document=product.file_id,
                caption=product_text,
            )
        else:
            # Отправляет только текст
            await call.message.answer(
                text=product_text,
            )

    await call.message.answer(
        text="🙏 Спасибо за доверие!",
        reply_markup=main_user_kb(call.from_user.id)
    )
```