# Модуль для реализации троттлинга сообщений в Telegram боте

## Обзор

Этот модуль предоставляет middleware для aiogram, который позволяет ограничивать частоту отправки сообщений от пользователей в Telegram боте. Он использует `TTLCache` для хранения информации о том, когда пользователь в последний раз отправлял сообщение, и предотвращает обработку сообщений, отправленных слишком часто.

## Подробней

Данный код реализует механизм троттлинга (ограничения частоты) сообщений для Telegram-бота, использующего библиотеку `aiogram`. Он предотвращает перегрузку бота и спам со стороны пользователей, ограничивая количество сообщений, которые пользователь может отправлять в течение определенного периода времени.

Middleware `ThrottlingMiddleware` проверяет, находится ли идентификатор чата пользователя в кэше `TTLCache`. Если идентификатор чата уже есть в кэше, это означает, что пользователь недавно отправлял сообщение, и middleware не пропускает сообщение для дальнейшей обработки. Если идентификатора чата нет в кэше, middleware добавляет его в кэш и позволяет сообщению быть обработанным.

## Классы

### `ThrottlingMiddleware`

**Описание**: Middleware для ограничения частоты отправки сообщений от пользователей.

**Методы**:
- `__init__`: Инициализирует middleware с заданным временем ограничения.
- `__call__`: Вызывается для каждого входящего сообщения. Проверяет, не превысил ли пользователь лимит сообщений.

**Параметры**:
- `time_limit` (int): Время в секундах, в течение которого пользователь может отправлять только одно сообщение. По умолчанию 2 секунды.

**Примеры**
```python
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.handlers import MessageHandler
import asyncio
from typing import Any, Dict

# Импортируем наш middleware
from middlewares.throttling import ThrottlingMiddleware

# Вместо токена вставьте реальный токен вашего бота
BOT_TOKEN = "YOUR_BOT_TOKEN"

# Создаем экземпляры бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Регистрируем ThrottlingMiddleware
dp.message.middleware(ThrottlingMiddleware(time_limit=2))

# Обработчик команды /start
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> Any:
    await message.answer("Привет! Я бот с ограничением частоты сообщений.")

# Обработчик текстовых сообщений
@dp.message()
async def message_handler(message: Message, data: Dict[str, Any]) -> Any:
    await message.answer("Вы отправили сообщение!")

async def main() -> None:
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
```

## Функции

### `__init__`

```python
def __init__(self, time_limit: int = 2) -> None:
    """
    Args:
        time_limit (int, optional): Время в секундах, в течение которого пользователь может отправлять только одно сообщение. По умолчанию 2.

    Returns:
        None

    Raises:
        None

    """
```

**Описание**: Инициализирует middleware с заданным временем ограничения.

**Параметры**:
- `time_limit` (int): Время в секундах, в течение которого пользователь может отправлять только одно сообщение. По умолчанию 2 секунды.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
middleware = ThrottlingMiddleware(time_limit=3)
```

### `__call__`

```python
async def __call__(
    self,
    handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
    event: Message,
    data: Dict[str, Any]
) -> Any:
    """
    Args:
        handler (Callable[[Message, Dict[str, Any]], Awaitable[Any]]): Функция-обработчик сообщения.
        event (Message): Объект сообщения Telegram.
        data (Dict[str, Any]): Дополнительные данные.

    Returns:
        Any: Результат обработки сообщения.

    Raises:
        None

    """
```

**Описание**: Вызывается для каждого входящего сообщения. Проверяет, не превысил ли пользователь лимит сообщений.

**Параметры**:
- `handler` (Callable[[Message, Dict[str, Any]], Awaitable[Any]]): Функция-обработчик сообщения.
- `event` (Message): Объект сообщения Telegram.
- `data` (Dict[str, Any]): Дополнительные данные.

**Возвращает**:
- `Any`: Результат обработки сообщения.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
async def my_handler(message: Message, data: Dict[str, Any]) -> Any:
    # Обработка сообщения
    pass

middleware = ThrottlingMiddleware(time_limit=2)
# Вызов middleware
# await middleware(my_handler, message, data)
```