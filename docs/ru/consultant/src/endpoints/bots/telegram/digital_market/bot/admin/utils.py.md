# Анализ кода модуля `utils`

**Качество кода**:
   - **Соответствие стандартам**: 6
   - **Плюсы**:
     - Используется `async` для асинхронных операций.
     - Применяется `FSMContext` для управления состоянием.
     - Логирование ошибок с помощью `logger`.
   - **Минусы**:
     - Не стандартизирован импорт `logger`.
     - Используются двойные кавычки для логирования.
     - Отсутствует документация в формате RST.
     - Нет обработки случая, когда `last_msg_id` не является числом.
     - Излишнее использование `try-except`

**Рекомендации по улучшению**:
   - Импортировать `logger` из `src.logger`.
   - Использовать одинарные кавычки в коде и двойные только для вывода.
   - Добавить RST-документацию для функции.
   - Добавить проверку типа для `last_msg_id` перед использованием.
   - Заменить `try-except` на проверку и логирование ошибки через `logger.error`.
   - Добавить обработку ошибки, если сообщение не удаляется, а также ошибку, если не найден `last_msg_id`

**Оптимизированный код**:

```python
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from src.logger import logger # corrected import

from bot.config import bot


async def process_dell_text_msg(message: Message, state: FSMContext) -> None:
    """
    Асинхронно обрабатывает удаление текстовых сообщений.

    Извлекает `last_msg_id` из состояния и удаляет соответствующее сообщение, а также исходное сообщение.
    В случае ошибки логирует произошедшее.

    :param message: Объект сообщения от Telegram.
    :type message: Message
    :param state: Объект состояния FSMContext.
    :type state: FSMContext
    :raises Exception: В случае ошибки при удалении сообщения.

    Пример:
        >>> from aiogram.types import Message
        >>> from aiogram.fsm.context import FSMContext
        >>> async def mock_delete_message(chat_id, message_id):
        ...     print(f"Удалено сообщение {message_id} из чата {chat_id}")
        >>> async def mock_get_data():
        ...     return {'last_msg_id': 12345}
        >>> mock_message = Message(message_id=1, chat=type('Chat', (object,), {'id': 123})(), from_user=type('User', (object,), {'id': 123})())
        >>> mock_state = FSMContext(bot=None, chat=mock_message.chat, user=mock_message.from_user)
        >>> mock_state.get_data = mock_get_data
        >>> bot.delete_message = mock_delete_message
        >>> await process_dell_text_msg(mock_message, mock_state)
        Удалено сообщение 12345 из чата 123
    """
    data = await state.get_data()
    last_msg_id = data.get('last_msg_id')

    if not last_msg_id: # check if last_msg_id exists
        logger.warning("Не удалось найти идентификатор последнего сообщения для удаления.")
    elif not isinstance(last_msg_id, int): # check if last_msg_id is int
        logger.error(f"Идентификатор последнего сообщения имеет неверный тип: {type(last_msg_id)}")
    else:
        try:
            await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_id) # deleting last message
        except Exception as e:
            logger.error(f"Ошибка при удалении последнего сообщения: {e}") # logging error if deleting last message failed

    try:
        await message.delete() # deleting original message
    except Exception as e:
        logger.error(f"Ошибка при удалении исходного сообщения: {e}") # logging error if deleting original message failed
```