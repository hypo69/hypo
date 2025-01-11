### Анализ кода модуля `admin`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    -   Используется асинхронность для работы с ботом.
    -   Применяются FSM для управления состоянием.
    -   Код разбит на отдельные функции, что улучшает читаемость.
    -   Есть обработка ошибок и логирование.
- **Минусы**:
    -   Используются двойные кавычки в некоторых местах, где должны быть одинарные.
    -   Не везде есть подробные комментарии.
    -   Много `try-except` блоков в одном месте, которые можно заменить на более элегантную обработку ошибок.
    -   Некоторые участки кода можно сделать более лаконичными и читаемыми.

**Рекомендации по улучшению**:
-   Использовать одинарные кавычки для всех строк, кроме `print`, `input` и `logger.error`.
-   Добавить RST-документацию для всех функций и классов.
-   Использовать `logger.error` вместо общих `except Exception`.
-   Избегать повторения кода.
-   Улучшить именование переменных для большей ясности.
-   Убрать лишние комментарии, заменив их более точными описаниями действий.
-   Привести все импорты в порядок.
-   Удалить лишние `try-except` блоки, где это возможно, и добавить `logger.error` в оставшиеся.

**Оптимизированный код**:

```python
"""
Модуль для управления административной частью бота.
==================================================

Этот модуль содержит набор функций для управления пользователями, товарами и статистикой бота.
Он использует FSM (конечные автоматы) для обработки состояний и предоставляет интерфейс для администраторов.

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

from bot.config import settings, bot
from bot.dao.dao import UserDAO, ProductDao, CategoryDao, PurchaseDao
from bot.admin.kbs import (
    admin_kb,
    admin_kb_back,
    product_management_kb,
    cancel_kb_inline,
    catalog_admin_kb,
    admin_send_file_kb,
    admin_confirm_kb,
    dell_product_kb
)
from bot.admin.schemas import ProductModel, ProductIDModel
from bot.admin.utils import process_dell_text_msg
from src.logger import logger # Используем импорт logger из src.logger

admin_router = Router()


class AddProduct(StatesGroup):
    """
    Класс для представления состояний добавления товара.

    :ivar name: Состояние для ввода имени товара.
    :vartype name: State
    :ivar description: Состояние для ввода описания товара.
    :vartype description: State
    :ivar price: Состояние для ввода цены товара.
    :vartype price: State
    :ivar file_id: Состояние для ввода ID файла товара.
    :vartype file_id: State
    :ivar category_id: Состояние для ввода ID категории товара.
    :vartype category_id: State
    :ivar hidden_content: Состояние для ввода скрытого контента товара.
    :vartype hidden_content: State
    :ivar confirm_add: Состояние для подтверждения добавления товара.
    :vartype confirm_add: State
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
    Обработчик для начала работы с админ-панелью.

    :param call: Объект CallbackQuery.
    :type call: CallbackQuery
    :raises Exception: В случае ошибки при открытии админ-панели.

    :return: None
    :rtype: None
    """
    await call.answer('Доступ в админ-панель разрешен!')
    try:
        await call.message.edit_text(
            text='Вам разрешен доступ в админ-панель. Выберите необходимое действие.',
            reply_markup=admin_kb()
        )
    except Exception as e:
        logger.error(f"Error editing message: {e}")  # логируем ошибку редактирования
        try:
            await call.message.delete()
            await call.message.answer(
                text='Вам разрешен доступ в админ-панель. Выберите необходимое действие.',
                reply_markup=admin_kb()
            )
        except Exception as e:
            logger.error(f"Error sending message: {e}") # логируем ошибку отправки сообщения
            await call.message.answer(
                text='Произошла ошибка при открытии админ-панели. Пожалуйста, попробуйте еще раз.',
                reply_markup=admin_kb()
            )


@admin_router.callback_query(F.data == 'statistic', F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_statistic(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обработчик для получения статистики.

    :param call: Объект CallbackQuery.
    :type call: CallbackQuery
    :param session_without_commit: Объект AsyncSession для работы с БД.
    :type session_without_commit: AsyncSession

    :return: None
    :rtype: None
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


@admin_router.callback_query(F.data == 'cancel', F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_process_cancel(call: CallbackQuery, state: FSMContext):
    """
     Обработчик для отмены текущего сценария добавления товара.

    :param call: Объект CallbackQuery.
    :type call: CallbackQuery
    :param state: Объект FSMContext для управления состояниями.
    :type state: FSMContext

    :return: None
    :rtype: None
    """
    await state.clear()
    await call.answer('Отмена сценария добавления товара')
    await call.message.delete()
    await call.message.answer(
        text='Отмена добавления товара.',
        reply_markup=admin_kb_back()
    )


@admin_router.callback_query(F.data == 'delete_product', F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_process_start_dell(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обработчик для начала процесса удаления товара.

    :param call: Объект CallbackQuery.
    :type call: CallbackQuery
    :param session_without_commit: Объект AsyncSession для работы с БД.
    :type session_without_commit: AsyncSession

    :return: None
    :rtype: None
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
     Обработчик для удаления товара по его ID.

    :param call: Объект CallbackQuery.
    :type call: CallbackQuery
    :param session_with_commit: Объект AsyncSession для работы с БД.
    :type session_with_commit: AsyncSession

    :return: None
    :rtype: None
    """
    product_id = int(call.data.split('_')[-1])
    await ProductDao.delete(session=session_with_commit, filters=ProductIDModel(id=product_id))
    await call.answer(f'Товар с ID {product_id} удален!', show_alert=True)
    await asyncio.sleep(1.5)
    await call.message.delete()


@admin_router.callback_query(F.data == 'process_products', F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_process_products(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обработчик для отображения меню управления товарами.

    :param call: Объект CallbackQuery.
    :type call: CallbackQuery
    :param session_without_commit: Объект AsyncSession для работы с БД.
    :type session_without_commit: AsyncSession

    :return: None
    :rtype: None
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
    Обработчик для начала процесса добавления товара.

    :param call: Объект CallbackQuery.
    :type call: CallbackQuery
    :param state: Объект FSMContext для управления состояниями.
    :type state: FSMContext

    :return: None
    :rtype: None
    """
    await call.answer('Запущен сценарий добавления товара.')
    await call.message.delete()
    msg = await call.message.answer(text='Для начала укажите имя товара: ', reply_markup=cancel_kb_inline())
    await state.update_data(last_msg_id=msg.message_id)
    await state.set_state(AddProduct.name)


@admin_router.message(F.text, F.from_user.id.in_(settings.ADMIN_IDS), AddProduct.name)
async def admin_process_name(message: Message, state: FSMContext):
    """
    Обработчик для получения имени товара.

    :param message: Объект Message.
    :type message: Message
    :param state: Объект FSMContext для управления состояниями.
    :type state: FSMContext

    :return: None
    :rtype: None
    """
    await state.update_data(name=message.text)
    await process_dell_text_msg(message, state)
    msg = await message.answer(text='Теперь дайте короткое описание товару: ', reply_markup=cancel_kb_inline())
    await state.update_data(last_msg_id=msg.message_id)
    await state.set_state(AddProduct.description)


@admin_router.message(F.text, F.from_user.id.in_(settings.ADMIN_IDS), AddProduct.description)
async def admin_process_description(message: Message, state: FSMContext, session_without_commit: AsyncSession):
    """
    Обработчик для получения описания товара.

    :param message: Объект Message.
    :type message: Message
    :param state: Объект FSMContext для управления состояниями.
    :type state: FSMContext
    :param session_without_commit: Объект AsyncSession для работы с БД.
    :type session_without_commit: AsyncSession

    :return: None
    :rtype: None
    """
    await state.update_data(description=message.html_text)
    await process_dell_text_msg(message, state)
    catalog_data = await CategoryDao.find_all(session=session_without_commit)
    msg = await message.answer(text='Теперь выберите категорию товара: ', reply_markup=catalog_admin_kb(catalog_data))
    await state.update_data(last_msg_id=msg.message_id)
    await state.set_state(AddProduct.category_id)


@admin_router.callback_query(F.data.startswith('add_category_'),
                             F.from_user.id.in_(settings.ADMIN_IDS),
                             AddProduct.category_id)
async def admin_process_category(call: CallbackQuery, state: FSMContext):
    """
    Обработчик для получения категории товара.

    :param call: Объект CallbackQuery.
    :type call: CallbackQuery
    :param state: Объект FSMContext для управления состояниями.
    :type state: FSMContext

    :return: None
    :rtype: None
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
    Обработчик для получения цены товара.

    :param message: Объект Message.
    :type message: Message
    :param state: Объект FSMContext для управления состояниями.
    :type state: FSMContext

    :return: None
    :rtype: None
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


@admin_router.callback_query(F.data == 'without_file', F.from_user.id.in_(settings.ADMIN_IDS), AddProduct.file_id)
async def admin_process_without_file(call: CallbackQuery, state: FSMContext):
    """
     Обработчик для случая, когда файл не требуется.

    :param call: Объект CallbackQuery.
    :type call: CallbackQuery
    :param state: Объект FSMContext для управления состояниями.
    :type state: FSMContext

    :return: None
    :rtype: None
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
    Обработчик для получения файла товара.

    :param message: Объект Message.
    :type message: Message
    :param state: Объект FSMContext для управления состояниями.
    :type state: FSMContext

    :return: None
    :rtype: None
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
    Обработчик для получения скрытого контента товара.

    :param message: Объект Message.
    :type message: Message
    :param state: Объект FSMContext для управления состояниями.
    :type state: FSMContext
    :param session_without_commit: Объект AsyncSession для работы с БД.
    :type session_without_commit: AsyncSession

    :return: None
    :rtype: None
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


@admin_router.callback_query(F.data == 'confirm_add', F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_process_confirm_add(call: CallbackQuery, state: FSMContext, session_with_commit: AsyncSession):
    """
     Обработчик для подтверждения добавления товара.

    :param call: Объект CallbackQuery.
    :type call: CallbackQuery
    :param state: Объект FSMContext для управления состояниями.
    :type state: FSMContext
    :param session_with_commit: Объект AsyncSession для работы с БД.
    :type session_with_commit: AsyncSession

    :return: None
    :rtype: None
    """
    await call.answer('Приступаю к сохранению файла!')
    product_data = await state.get_data()
    await bot.delete_message(chat_id=call.from_user.id, message_id=product_data['last_msg_id'])
    del product_data['last_msg_id']
    await ProductDao.add(session=session_with_commit, values=ProductModel(**product_data))
    await call.message.answer(text='Товар успешно добавлен в базу данных!', reply_markup=admin_kb())