# Модуль ThrottlingMiddleware

## Обзор

Модуль `ThrottlingMiddleware` предоставляет класс `ThrottlingMiddleware`, который реализует механизм ограничения скорости обработки сообщений в Telegram-боте. Он использует `TTLCache` для хранения информации о том, когда последнее сообщение от определенного пользователя было обработано, и предотвращает слишком частую обработку сообщений от одного и того же пользователя.

## Подробней

Этот код используется для предотвращения злоупотреблений и защиты от флуда в Telegram-боте. Он позволяет ограничить количество сообщений, которые пользователь может отправлять боту за определенный период времени, тем самым повышая стабильность и отзывчивость бота.

## Классы

### `ThrottlingMiddleware`

**Описание**: Middleware для ограничения скорости обработки сообщений в Telegram-боте.

**Методы**:
- `__init__`: Инициализирует объект `ThrottlingMiddleware`.
- `__call__`: Вызывается для обработки каждого сообщения.

**Параметры**:
- `time_limit` (int): Время в секундах, в течение которого сообщения от одного и того же пользователя будут игнорироваться. По умолчанию 2 секунды.

**Примеры**
```python
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.handlers import MessageHandler
import asyncio
from typing import Any, Dict

# Создаем экземпляр бота
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = Bot(token=TOKEN)

# Создаем диспетчер
dp = Dispatcher()

# Подключаем middleware
dp.message.middleware(ThrottlingMiddleware(time_limit=2))

# Обработчик команды /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет! Я бот, который ограничивает количество сообщений.")

# Обработчик всех остальных сообщений
@dp.message()
async def echo_handler(message: Message):
    await message.answer(f"Ты написал: {message.text}")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
```

## Функции

### `__init__`

```python
def __init__(self, time_limit: int = 2) -> None:
    """
    Инициализирует объект `ThrottlingMiddleware`.

    Args:
        time_limit (int, optional): Время в секундах, в течение которого сообщения от одного и того же пользователя будут игнорироваться. По умолчанию 2 секунды.

    Returns:
        None

    Raises:
        None
    """
```

**Описание**: Инициализирует объект `ThrottlingMiddleware`, создавая `TTLCache` с заданным временем жизни.

**Параметры**:
- `time_limit` (int, optional): Время в секундах, в течение которого сообщения от одного и того же пользователя будут игнорироваться. По умолчанию 2 секунды.

### `__call__`

```python
async def __call__(
    self,
    handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
    event: Message,
    data: Dict[str, Any]
) -> Any:
    """
    Вызывается для обработки каждого сообщения.

    Args:
        handler (Callable[[Message, Dict[str, Any]], Awaitable[Any]]): Функция-обработчик сообщения.
        event (Message): Объект сообщения.
        data (Dict[str, Any]): Дополнительные данные.

    Returns:
        Any: Результат обработки сообщения.

    Raises:
        None
    """
```

**Описание**: Метод `__call__` вызывается для обработки каждого сообщения. Он проверяет, находится ли идентификатор чата пользователя в кэше `self.limit`. Если да, то сообщение игнорируется. Если нет, то идентификатор чата добавляется в кэш, и сообщение передается обработчику.

**Параметры**:
- `handler` (Callable[[Message, Dict[str, Any]], Awaitable[Any]]): Функция-обработчик сообщения.
- `event` (Message): Объект сообщения.
- `data` (Dict[str, Any]): Дополнительные данные.

**Возвращает**:
- `Any`: Результат обработки сообщения.

**Примеры**:

```python
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio
from typing import Any, Dict

# Создаем экземпляр бота
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = Bot(token=TOKEN)

# Создаем диспетчер
dp = Dispatcher()

# Создаем экземпляр middleware
throttling_middleware = ThrottlingMiddleware(time_limit=2)

# Регистрируем middleware
dp.message.middleware(throttling_middleware)

# Обработчик команды /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет! Я бот, который ограничивает количество сообщений.")

# Обработчик всех остальных сообщений
@dp.message()
async def echo_handler(message: Message):
    await message.answer(f"Ты написал: {message.text}")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
```