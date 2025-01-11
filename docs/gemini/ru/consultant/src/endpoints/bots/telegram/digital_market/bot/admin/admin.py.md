## Анализ кода модуля `admin.py`

**Качество кода**
8
- Плюсы
    - Код разбит на логические блоки, используется `Router` для обработки различных типов запросов.
    - Присутствует использование `FSMContext` для управления состоянием пользователя при добавлении продукта.
    - Код использует асинхронные операции, что хорошо для производительности.
    - Используются `DAO` для работы с базой данных, что способствует разделению ответственности.
    - Присутствует обработка ошибок, хотя и не везде оптимальна.
- Минусы
    - Не везде используется `logger` для логирования ошибок.
    - Есть дублирование кода, например, при обработке `Exception` в функции `start_admin`.
    - Использование `try-except` можно упростить.
    - Не хватает документации к функциям и классам.
    - Присутствуют магические строки в тексте сообщений, лучше использовать константы.
    - Отсутствует обработка ошибок при удалении сообщений.
    - Не все переменные и функции имеют описательные имена.
    - Используется стандартный `json.load` (нет в коде, но в описании)

**Рекомендации по улучшению**

1.  **Импорты**: Добавить `from src.logger.logger import logger` для логирования.
2.  **Документация**: Добавить docstring к классам и функциям, используя формат RST.
3.  **Логирование**: Заменить `print` на `logger.error` для отслеживания ошибок.
4.  **Обработка ошибок**: Упростить блоки `try-except`, используя логирование и более конкретные исключения.
5.  **Дублирование кода**: Избегать дублирования кода, вынося повторяющиеся действия в отдельные функции.
6.  **Магические строки**: Заменить магические строки на константы.
7.  **Удаление сообщений**: Добавить обработку ошибок при удалении сообщений.
8.  **Именование**: Привести имена функций, переменных и импортов в соответствие с ранее обработанными файлами.

**Оптимизированный код**

```python
"""
Модуль для управления административными функциями Telegram-бота.
==============================================================

Этот модуль обрабатывает запросы администраторов, позволяя им управлять
пользователями, продуктами и категориями, а также просматривать статистику.

Основные возможности:
    - Просмотр статистики.
    - Добавление, удаление и управление продуктами.
    - Управление категориями продуктов.

Пример использования
--------------------

.. code-block:: python

    from aiogram import Dispatcher
    from bot.admin.admin import admin_router

    dp = Dispatcher()
    dp.include_router(admin_router)
"""
import asyncio
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message
from sqlalchemy.ext.asyncio import AsyncSession

# from bot.config import settings, bot #  Удалено: импорт bot не нужен
from src.config import settings, bot #  Исправлено: импорт bot из src.config
from src.dao.dao import UserDAO, ProductDao, CategoryDao, PurchaseDao #  Исправлено: импорт DAO из src.dao
from src.admin.kbs import admin_kb, admin_kb_back, product_management_kb, cancel_kb_inline, catalog_admin_kb, \
    admin_send_file_kb, admin_confirm_kb, dell_product_kb #  Исправлено: импорт kb из src.admin.kbs
from src.admin.schemas import ProductModel, ProductIDModel #  Исправлено: импорт схем из src.admin.schemas
from src.admin.utils import process_dell_text_msg #  Исправлено: импорт утилит из src.admin.utils
from src.logger.logger import logger # Добавлено: импорт logger

admin_router = Router()


class AddProduct(StatesGroup):
    """
    Состояния для процесса добавления нового продукта.

    :var name: Состояние для ввода имени продукта.
    :var description: Состояние для ввода описания продукта.
    :var price: Состояние для ввода цены продукта.
    :var file_id: Состояние для загрузки файла продукта.
    :var category_id: Состояние для выбора категории продукта.
    :var hidden_content: Состояние для ввода скрытого контента продукта.
    :var confirm_add: Состояние для подтверждения добавления продукта.
    """
    name = State()
    description = State()
    price = State()
    file_id = State()
    category_id = State()
    hidden_content = State()
    confirm_add = State()


@admin_router.callback_query(F.data == 'admin_panel', F.from_user.id.in_(settings.ADMIN_IDS))
async def start_admin(call: CallbackQuery):
    """
    Обрабатывает запрос на вход в админ-панель.

    При успешном входе отправляет сообщение с клавиатурой админ-панели.
    В случае ошибки выводит сообщение о невозможности входа.
    """
    await call.answer('Доступ в админ-панель разрешен!')
    try:
        await call.message.edit_text(
            text='Вам разрешен доступ в админ-панель. Выберите необходимое действие.',
            reply_markup=admin_kb()
        )
    except Exception as e: #  Изменено: обработка ошибки через logger
        logger.error('Ошибка при открытии админ-панели', exc_info=e)
        try:
            await call.message.delete()
            await call.message.answer(
                text='Вам разрешен доступ в админ-панель. Выберите необходимое действие.',
                reply_markup=admin_kb()
            )
        except Exception as e: #  Изменено: обработка ошибки через logger
            logger.error('Ошибка при удалении и повторном выводе сообщения админ-панели', exc_info=e)
            await call.message.answer(
                text='Произошла ошибка при открытии админ-панели. Пожалуйста, попробуйте еще раз.',
                reply_markup=admin_kb()
            )


@admin_router.callback_query(F.data == 'statistic', F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_statistic(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Отправляет статистику пользователей и заказов администратору.

    :param call: CallbackQuery объект
    :param session_without_commit: Асинхронная сессия SQLAlchemy
    """
    await call.answer('Запрос на получение статистики...')
    await call.answer('📊 Собираем статистику...')

    stats = await UserDAO.get_statistics(session=session_without_commit)
    payment_stats = await PurchaseDao.get_payment_stats(session=session_without_commit)
    stats_message = (
        '📈 Статистика пользователей:\\n\\n'
        f'👥 Всего пользователей: {stats["total_users"]}\\n'
        f'🆕 Новых за сегодня: {stats["new_today"]}\\n'
        f'📅 Новых за неделю: {stats["new_week"]}\\n'
        f'📆 Новых за месяц: {stats["new_month"]}\\n\\n'
        f'💰 Общая статистика по заказам:\\n\\n{payment_stats}'
    )
    await call.message.edit_text(
        text=stats_message,
        reply_markup=admin_kb()
    )


@admin_router.callback_query(F.data == "cancel", F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_process_cancel(call: CallbackQuery, state: FSMContext):
    """
    Отменяет текущий сценарий добавления товара.

    :param call: CallbackQuery объект
    :param state: FSMContext объект
    """
    await state.clear()
    await call.answer('Отмена сценария добавления товара')
    try:
         await call.message.delete()
    except Exception as e: #  Изменено: обработка ошибки через logger
        logger.error('Ошибка при удалении сообщения отмены добавления товара', exc_info=e)
    await call.message.answer(
        text='Отмена добавления товара.',
        reply_markup=admin_kb_back()
    )


@admin_router.callback_query(F.data == 'delete_product', F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_process_start_dell(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Начинает процесс удаления товара.
    Отправляет список всех товаров с кнопками для удаления.

    :param call: CallbackQuery объект
    :param session_without_commit: Асинхронная сессия SQLAlchemy
    """
    await call.answer('Режим удаления товаров')
    all_products = await ProductDao.find_all(session=session_without_commit)

    await call.message.edit_text(
        text=f'На данный момент в базе данных {len(all_products)} товаров. Для удаления нажмите на кнопку ниже'
    )
    for product_data in all_products:
        file_id = product_data.file_id
        file_text = '📦 Товар с файлом' if file_id else '📄 Товар без файла'

        product_text = (f'🛒 Описание товара:\\n\\n'
                        f'🔹 <b>Название товара:</b> <b>{product_data.name}</b>\\n'
                        f'🔹 <b>Описание:</b>\\n\\n<b>{product_data.description}</b>\\n\\n'
                        f'🔹 <b>Цена:</b> <b>{product_data.price} ₽</b>\\n'
                        f'🔹 <b>Описание (закрытое):</b>\\n\\n<b>{product_data.hidden_content}</b>\\n\\n'
                        f'<b>{file_text}</b>')
        if file_id:
            await call.message.answer_document(document=file_id, caption=product_text,
                                               reply_markup=dell_product_kb(product_data.id))
        else:
            await call.message.answer(text=product_text, reply_markup=dell_product_kb(product_data.id))


@admin_router.callback_query(F.data.startswith('dell_'), F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_process_delete_product(call: CallbackQuery, session_with_commit: AsyncSession):
    """
    Удаляет выбранный товар.

    :param call: CallbackQuery объект
    :param session_with_commit: Асинхронная сессия SQLAlchemy
    """
    product_id = int(call.data.split('_')[-1])
    await ProductDao.delete(session=session_with_commit, filters=ProductIDModel(id=product_id))
    await call.answer(f'Товар с ID {product_id} удален!', show_alert=True)
    await asyncio.sleep(1.5)
    try:
        await call.message.delete()
    except Exception as e: #  Изменено: обработка ошибки через logger
        logger.error('Ошибка при удалении сообщения об удалении товара', exc_info=e)


@admin_router.callback_query(F.data == 'process_products', F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_process_products(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обрабатывает запрос на управление товарами.
    Отправляет сообщение с клавиатурой для управления товарами.

    :param call: CallbackQuery объект
    :param session_without_commit: Асинхронная сессия SQLAlchemy
    """
    await call.answer('Режим управления товарами')
    all_products_count = await ProductDao.count(session=session_without_commit)
    await call.message.edit_text(
        text=f'На данный момент в базе данных {all_products_count} товаров. Что будем делать?',
        reply_markup=product_management_kb()
    )


@admin_router.callback_query(F.data == 'add_product', F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_process_add_product(call: CallbackQuery, state: FSMContext):
    """
    Начинает процесс добавления нового товара.
    Устанавливает начальное состояние FSM.

    :param call: CallbackQuery объект
    :param state: FSMContext объект
    """
    await call.answer('Запущен сценарий добавления товара.')
    try:
        await call.message.delete()
    except Exception as e: #  Изменено: обработка ошибки через logger
        logger.error('Ошибка при удалении сообщения о начале добавления товара', exc_info=e)
    msg = await call.message.answer(text='Для начала укажите имя товара: ', reply_markup=cancel_kb_inline())
    await state.update_data(last_msg_id=msg.message_id)
    await state.set_state(AddProduct.name)


@admin_router.message(F.text, F.from_user.id.in_(settings.ADMIN_IDS), AddProduct.name)
async def admin_process_name(message: Message, state: FSMContext):
    """
    Обрабатывает введенное имя товара.
    Переходит к следующему шагу - вводу описания.

    :param message: Message объект
    :param state: FSMContext объект
    """
    await state.update_data(name=message.text)
    await process_dell_text_msg(message, state)
    msg = await message.answer(text='Теперь дайте короткое описание товару: ', reply_markup=cancel_kb_inline())
    await state.update_data(last_msg_id=msg.message_id)
    await state.set_state(AddProduct.description)


@admin_router.message(F.text, F.from_user.id.in_(settings.ADMIN_IDS), AddProduct.description)
async def admin_process_description(message: Message, state: FSMContext, session_without_commit: AsyncSession):
    """
    Обрабатывает введенное описание товара.
    Переходит к следующему шагу - выбору категории товара.

    :param message: Message объект
    :param state: FSMContext объект
    :param session_without_commit: Асинхронная сессия SQLAlchemy
    """
    await state.update_data(description=message.html_text)
    await process_dell_text_msg(message, state)
    catalog_data = await CategoryDao.find_all(session=session_without_commit)
    msg = await message.answer(text='Теперь выберите категорию товара: ', reply_markup=catalog_admin_kb(catalog_data))
    await state.update_data(last_msg_id=msg.message_id)
    await state.set_state(AddProduct.category_id)


@admin_router.callback_query(F.data.startswith("add_category_"),
                             F.from_user.id.in_(settings.ADMIN_IDS),
                             AddProduct.category_id)
async def admin_process_category(call: CallbackQuery, state: FSMContext):
    """
    Обрабатывает выбор категории товара.
    Переходит к следующему шагу - вводу цены товара.

    :param call: CallbackQuery объект
    :param state: FSMContext объект
    """
    category_id = int(call.data.split('_')[-1])
    await state.update_data(category_id=category_id)
    await call.answer('Категория товара успешно выбрана.')
    msg = await call.message.edit_text(text='Введите цену товара: ', reply_markup=cancel_kb_inline())
    await state.update_data(last_msg_id=msg.message_id)
    await state.set_state(AddProduct.price)


@admin_router.message(F.text, F.from_user.id.in_(settings.ADMIN_IDS), AddProduct.price)
async def admin_process_price(message: Message, state: FSMContext):
    """
    Обрабатывает введенную цену товара.
    Переходит к следующему шагу - загрузке файла товара.

    :param message: Message объект
    :param state: FSMContext объект
    """
    try:
        price = int(message.text)
        await state.update_data(price=price)
        await process_dell_text_msg(message, state)
        msg = await message.answer(
            text='Отправьте файл (документ), если требуется или нажмите на \'БЕЗ ФАЙЛА\', если файл не требуется',
            reply_markup=admin_send_file_kb()
        )
        await state.update_data(last_msg_id=msg.message_id)
        await state.set_state(AddProduct.file_id)
    except ValueError:
        await message.answer(text='Ошибка! Необходимо ввести числовое значение для цены.')
        return


@admin_router.callback_query(F.data == "without_file", F.from_user.id.in_(settings.ADMIN_IDS), AddProduct.file_id)
async def admin_process_without_file(call: CallbackQuery, state: FSMContext):
    """
    Обрабатывает выбор товара без файла.
    Переходит к следующему шагу - вводу скрытого контента товара.

    :param call: CallbackQuery объект
    :param state: FSMContext объект
    """
    await state.update_data(file_id=None)
    await call.answer('Файл не выбран.')
    msg = await call.message.edit_text(
        text='Теперь отправьте контент, который отобразится после покупки товара внутри карточки',
        reply_markup=cancel_kb_inline())
    await state.update_data(last_msg_id=msg.message_id)
    await state.set_state(AddProduct.hidden_content)


@admin_router.message(F.document, F.from_user.id.in_(settings.ADMIN_IDS), AddProduct.file_id)
async def admin_process_file(message: Message, state: FSMContext):
    """
    Обрабатывает загрузку файла товара.
    Переходит к следующему шагу - вводу скрытого контента товара.

    :param message: Message объект
    :param state: FSMContext объект
    """
    await state.update_data(file_id=message.document.file_id)
    await process_dell_text_msg(message, state)
    msg = await message.answer(
        text='Теперь отправьте контент, который отобразится после покупки товара внутри карточки',
        reply_markup=cancel_kb_inline())
    await state.update_data(last_msg_id=msg.message_id)
    await state.set_state(AddProduct.hidden_content)


@admin_router.message(F.text, F.from_user.id.in_(settings.ADMIN_IDS), AddProduct.hidden_content)
async def admin_process_hidden_content(message: Message, state: FSMContext, session_without_commit: AsyncSession):
    """
    Обрабатывает ввод скрытого контента товара.
    Отправляет превью товара и предлагает подтвердить добавление.

    :param message: Message объект
    :param state: FSMContext объект
    :param session_without_commit: Асинхронная сессия SQLAlchemy
    """
    await state.update_data(hidden_content=message.html_text)

    product_data = await state.get_data()
    category_info = await CategoryDao.find_one_or_none_by_id(session=session_without_commit,
                                                             data_id=product_data.get('category_id'))

    file_id = product_data.get('file_id')
    file_text = '📦 Товар с файлом' if file_id else '📄 Товар без файла'

    product_text = (f'🛒 Проверьте, все ли корректно:\\n\\n'
                    f'🔹 <b>Название товара:</b> <b>{product_data["name"]}</b>\\n'
                    f'🔹 <b>Описание:</b>\\n\\n<b>{product_data["description"]}</b>\\n\\n'
                    f'🔹 <b>Цена:</b> <b>{product_data["price"]} ₽</b>\\n'
                    f'🔹 <b>Описание (закрытое):</b>\\n\\n<b>{product_data["hidden_content"]}</b>\\n\\n'
                    f'🔹 <b>Категория:</b> <b>{category_info.category_name} (ID: {category_info.id})</b>\\n\\n'
                    f'<b>{file_text}</b>')
    await process_dell_text_msg(message, state)

    if file_id:
        msg = await message.answer_document(document=file_id, caption=product_text, reply_markup=admin_confirm_kb())
    else:
        msg = await message.answer(text=product_text, reply_markup=admin_confirm_kb())
    await state.update_data(last_msg_id=msg.message_id)
    await state.set_state(AddProduct.confirm_add)


@admin_router.callback_query(F.data == "confirm_add", F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_process_confirm_add(call: CallbackQuery, state: FSMContext, session_with_commit: AsyncSession):
    """
    Обрабатывает подтверждение добавления товара.
    Сохраняет товар в базу данных и завершает процесс.

    :param call: CallbackQuery объект
    :param state: FSMContext объект
    :param session_with_commit: Асинхронная сессия SQLAlchemy
    """
    await call.answer('Приступаю к сохранению файла!')
    product_data = await state.get_data()
    try:
       await bot.delete_message(chat_id=call.from_user.id, message_id=product_data["last_msg_id"])
    except Exception as e: #  Изменено: обработка ошибки через logger
        logger.error('Ошибка при удалении сообщения о подтверждении добавления товара', exc_info=e)
    del product_data["last_msg_id"]
    await ProductDao.add(session=session_with_commit, values=ProductModel(**product_data))
    await call.message.answer(text='Товар успешно добавлен в базу данных!', reply_markup=admin_kb())