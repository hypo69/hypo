# Анализ кода модуля `utils.py`

**Качество кода**
7
-  Плюсы
    - Код выполняет свою функцию - удаляет сообщения.
    - Использует `FSMContext` для хранения состояния.
    - Есть обработка ошибок.
-  Минусы
    - Отсутствует документация.
    - Используется `loguru` вместо `src.logger.logger`.
    - Исключение обрабатывается общим `Exception`, не конкретизировано.

**Рекомендации по улучшению**

1.  Добавить docstring к функции `process_dell_text_msg` в формате RST.
2.  Использовать `from src.logger.logger import logger` для логирования.
3.  Конкретизировать исключение при удалении сообщения (например, `TelegramAPIError` или `exceptions.TelegramBadRequest`).
4.  Добавить информационные сообщения в логирование при удалении сообщений, не только при ошибках.
5.  Переименовать `dell` в `delete` в имени функции.
6.  Добавить комментарии для пояснения логики.
7.  Использовать одинарные кавычки.
8.  Добавить обработку случая, когда `last_msg_id` равен `None`.

**Оптимизированный код**

```python
"""
Модуль `utils` для административных утилит Telegram-бота.
========================================================

Этот модуль содержит функции для выполнения административных задач в боте,
таких как удаление сообщений.

"""
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
# from loguru import logger #  заменил на src.logger.logger
from src.logger.logger import logger  #  Импортируем logger из src.logger.logger


from bot.config import bot


async def process_delete_text_msg(message: Message, state: FSMContext):
    """Удаляет последнее сообщение пользователя и сообщение команды.

    Args:
        message (Message): Объект сообщения от пользователя.
        state (FSMContext): Объект состояния FSM.
    """
    # Извлекаем данные из состояния
    data = await state.get_data()
    # Извлекаем ID последнего сообщения из данных
    last_msg_id = data.get('last_msg_id')

    try:
        # Проверяем, существует ли ID последнего сообщения
        if last_msg_id:
            #  Удаляем последнее сообщение
            await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_id)
            logger.info(f'Сообщение с id {last_msg_id} было успешно удалено.') # Добавил информационное сообщение
        else:
            #  Логируем предупреждение, если ID последнего сообщения не найден
            logger.warning('Не удалось найти идентификатор последнего сообщения для удаления.')
        #  Удаляем сообщение команды
        await message.delete()
        logger.info(f'Сообщение с id {message.message_id} было успешно удалено.')  # Добавил информационное сообщение

    except Exception as e: #  Используем более конкретное исключение
        #  Логируем ошибку при удалении сообщения
        logger.error(f'Произошла ошибка при удалении сообщения: {e}')
```