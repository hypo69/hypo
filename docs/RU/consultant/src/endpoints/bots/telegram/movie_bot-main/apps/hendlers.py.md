# Анализ кода модуля hendlers.py

**Качество кода**
8
- Плюсы
    - Код структурирован и логически разделен на обработчики команд и состояний.
    - Используются `FSMContext` для управления состояниями диалога.
    - Применение `aiogram` для создания telegram-бота.
    - Присутствуют docstring к функциям.
- Минусы
    - Отсутствуют импорты из `src.logger`
    - Нет обработки ошибок.
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`
    - Неполная документация.

**Рекомендации по улучшению**

1.  **Импорты:**
    - Добавить импорт `from src.logger.logger import logger` для логирования ошибок.
2.  **Обработка ошибок:**
    -  Добавить обработку исключений в функции `name_handler` с использованием `logger.error`.
3.  **Документация:**
    - Добавить полное описание модуля в начале файла.
    - Добавить более подробные docstring для каждой функции.
4.  **Форматирование:**
    - Использовать f-строки для форматирования строк (пример: `f"Название: {data['name']}"`).
    - Улучшить читаемость кода, добавив пустые строки между логическими блоками.
5.  **Переменные:**
    - Убрать  `type_movies` как глобальную переменную, перенести в `class Params`
    - Типизировать переменные.

**Оптимизированный код**

```python
"""
Модуль обработки сообщений и состояний для Telegram-бота поиска фильмов.
======================================================================

Этот модуль содержит обработчики для различных команд и состояний бота,
использующие FSM (конечные автоматы) для управления диалогом с пользователем.
Включает функции для обработки начальной команды, выбора типа фильма (фильм или сериал),
а также для получения названия фильма и отображения результатов поиска.

Пример использования
--------------------

Для запуска бота необходимо настроить и запустить aiogram bot,
после чего будут доступны обработчики сообщений, определенные в этом модуле.

.. code-block:: python

    from aiogram import Bot, Dispatcher
    from hendlers import router
    # Инициализация бота и диспетчера
    bot = Bot(token="YOUR_TOKEN")
    dp = Dispatcher()
    dp.include_router(router)

    async def main():
        try:
            await dp.start_polling(bot)
        finally:
            await bot.session.close()

    if __name__ == "__main__":
        import asyncio
        asyncio.run(main())
"""
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

import apps.keyboard as kb
from apps.search import search_query
from src.logger.logger import logger # Импортируем logger

router = Router()


class Params(StatesGroup):
    """
    Состояния для конечного автомата, отслеживающие тип фильма и его название.
    """
    type_movie = State()
    name = State()
    type_movies = {'film': 'Фильм', 'series': 'Сериал'}


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Обрабатывает команду /start и отправляет приветственное сообщение.

    Args:
        message (Message): Объект сообщения от пользователя.
    """
    await message.answer(f"Добро пожаловать, "
                         f"<b>{message.from_user.full_name}</b> 😎",
                         parse_mode="html")
    await message.answer('Найти интересующий фильм', reply_markup=kb.find_movie)


@router.callback_query(F.data == 'new_movies')
async def movie_handler(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Обрабатывает нажатие кнопки "Найти фильм" и устанавливает состояние `type_movie`.

    Args:
        callback (CallbackQuery): Объект обратного вызова от пользователя.
        state (FSMContext): Контекст FSM для управления состоянием диалога.
    """
    await state.set_state(Params.type_movie)
    await callback.message.edit_text('Укажите фильм или сериал вы ищите',
                                     reply_markup=kb.choice)


@router.callback_query(F.data == 'series')
async def series_handler(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Обрабатывает выбор типа "сериал" и устанавливает состояние `name`.

    Args:
        callback (CallbackQuery): Объект обратного вызова от пользователя.
        state (FSMContext): Контекст FSM для управления состоянием диалога.
    """
    await callback.message.delete()
    await state.update_data(type_movie='series')
    await state.set_state(Params.name)
    await callback.message.answer('Введите название')


@router.callback_query(F.data == 'film')
async def film_handler(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Обрабатывает выбор типа "фильм" и устанавливает состояние `name`.

    Args:
        callback (CallbackQuery): Объект обратного вызова от пользователя.
        state (FSMContext): Контекст FSM для управления состоянием диалога.
    """
    await callback.message.delete()
    await state.update_data(type_movie='film')
    await state.set_state(Params.name)
    await callback.message.answer('Введите название')


@router.message(Params.name)
async def name_handler(message: Message, state: FSMContext) -> None:
    """
    Обрабатывает ввод названия фильма, выполняет поиск и отправляет результат.

    Args:
        message (Message): Объект сообщения от пользователя.
        state (FSMContext): Контекст FSM для управления состоянием диалога.
    """
    try:
        await state.update_data(name=message.text)
        data = await state.get_data()
        movie = search_query(data['name'], data['type_movie'])
        await message.answer(f"Название: <b>{data['name']}</b>\n"
                             f"Тип: <b>{Params.type_movies[data['type_movie']]}</b>",
                             parse_mode="html")

        if movie:
            await message.answer("По вашему запросу найдено ✨✨✨:")
            await message.answer(f"<b>{movie['title']}</b>\n"
                                 f"{movie['description']}\n"
                                 f"{movie['link']}", parse_mode="html")
        else:
            await message.answer(f"Ваш {Params.type_movies[data['type_movie']]} "
                                 f"не найден 😢")
        await message.answer('Найти новый фильм', reply_markup=kb.find_movie)
        await state.clear()
    except Exception as ex:
        logger.error(f'Произошла ошибка при обработке названия фильма {ex=}', exc_info=True)
        await message.answer("Произошла ошибка, попробуйте позже")
        await state.clear()
```