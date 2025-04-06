# Модуль утилит для администраторов Telegram-бота (digital_market)

## Обзор

Модуль содержит функцию `process_dell_text_msg`, которая используется для удаления последнего сообщения пользователя и текущего сообщения в чате с ботом. Этот функционал предназначен для административных задач, таких как очистка чата от лишних сообщений.

## Подробней

Данный модуль обеспечивает удобный способ для администраторов бота удалять сообщения, что позволяет поддерживать порядок в чате и улучшить взаимодействие с пользователем. Функция использует `FSMContext` для получения ID последнего сообщения и удаляет как последнее сообщение, так и текущее сообщение пользователя.

## Функции

### `process_dell_text_msg`

```python
async def process_dell_text_msg(message: Message, state: FSMContext):
    """ Функция удаляет последнее сообщение пользователя и текущее сообщение в чате с ботом.

    Args:
        message (Message): Объект сообщения от Telegram.
        state (FSMContext): Объект состояния FSM (Finite State Machine) от aiogram.

    Returns:
        None

    Raises:
        Exception: Если происходит ошибка при удалении сообщения.

    """
```

**Параметры**:

- `message` (Message): Объект сообщения от Telegram, содержащий информацию о сообщении, отправителе и чате.
- `state` (FSMContext): Объект состояния FSM (Finite State Machine) от aiogram, используемый для хранения и получения данных о состоянии пользователя.

**Возвращает**:

- `None`: Функция ничего не возвращает.

**Вызывает исключения**:

- `Exception`: Если происходит ошибка при удалении сообщения, информация об ошибке логируется.

**Как работает функция**:

1. **Получение данных из состояния**: Функция пытается получить `last_msg_id` из состояния пользователя (`FSMContext`).
2. **Удаление последнего сообщения**: Если `last_msg_id` существует, функция пытается удалить сообщение с этим ID из чата пользователя.
3. **Удаление текущего сообщения**: Независимо от успеха удаления последнего сообщения, функция пытается удалить текущее сообщение пользователя.
4. **Обработка ошибок**: Если при удалении сообщения происходит ошибка, информация об ошибке логируется с использованием `logger.error`.

**ASCII Flowchart**:

```
A[Получение данных из FSMContext (last_msg_id)]
|
B[Проверка наличия last_msg_id]
|
C[Удаление сообщения по last_msg_id]
|
D[Удаление текущего сообщения]
|
E[Обработка исключений]
```

**Примеры**:

Предположим, что у пользователя в состоянии `state` сохранен `last_msg_id = 123`, и пользователь отправил сообщение с `message.message_id = 456`.

```python
from aiogram.types import Message, User, Chat
from aiogram.fsm.context import FSMContext
from unittest.mock import AsyncMock, patch
import asyncio

async def test_process_dell_text_msg():
    # Создаем мок-объекты message и state
    message_mock = Message(
        message_id=456,
        from_user=User(id=12345, is_bot=False, first_name="Test", last_name="User", username="testuser"),
        chat=Chat(id=12345, type="private"),
        date=None  # type: ignore
    )
    state_mock = AsyncMock(spec=FSMContext)
    state_mock.get_data.return_value = {'last_msg_id': 123}

    # Мокируем bot.delete_message и message.delete
    with patch("bot.config.bot.delete_message", new_callable=AsyncMock) as delete_message_mock, \
            patch.object(message_mock, "delete", new_callable=AsyncMock) as message_delete_mock:

        # Вызываем функцию
        await process_dell_text_msg(message_mock, state_mock)

        # Проверяем, что delete_message был вызван с правильными аргументами
        delete_message_mock.assert_called_once_with(chat_id=12345, message_id=123)
        # Проверяем, что message.delete был вызван
        message_delete_mock.assert_called_once()

    # Проверяем случай, когда last_msg_id отсутствует
    state_mock.get_data.return_value = {}
    with patch("bot.config.bot.delete_message", new_callable=AsyncMock) as delete_message_mock, \
            patch.object(message_mock, "delete", new_callable=AsyncMock) as message_delete_mock:
        await process_dell_text_msg(message_mock, state_mock)
        assert delete_message_mock.call_count == 0
        message_delete_mock.assert_called_once()

# Для запуска теста асинхронной функции
asyncio.run(test_process_dell_text_msg())