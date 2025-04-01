# Модуль для реализации троттлинга сообщений в Telegram боте
## Обзор

Этот модуль предоставляет класс `ThrottlingMiddleware`, который используется для ограничения частоты отправки сообщений от одного и того же чата в Telegram боте. Это позволяет предотвратить спам и защитить бота от перегрузки.

## Подробней

`ThrottlingMiddleware` реализует middleware для aiogram, которое проверяет, как часто пользователи отправляют сообщения боту. Если пользователь отправляет сообщения слишком часто, middleware игнорирует эти сообщения.

## Классы

### `ThrottlingMiddleware`

**Описание**:
Middleware для ограничения частоты отправки сообщений от одного и того же чата.

**Как работает класс**:

Класс `ThrottlingMiddleware` использует `TTLCache` из библиотеки `cachetools` для хранения информации о том, когда пользователь последний раз отправлял сообщение. При получении нового сообщения middleware проверяет, находится ли идентификатор чата в кэше. Если да, то сообщение игнорируется. Если нет, то идентификатор чата добавляется в кэш, и сообщение обрабатывается.

**Методы**:

- `__init__(self, time_limit: int = 2) -> None`:
    *   Инициализирует `ThrottlingMiddleware` с заданным `time_limit`.
- `__call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], event: Message, data: Dict[str, Any]) -> Any`:
    *   Вызывается для каждого входящего сообщения. Проверяет, не превышен ли лимит сообщений для данного чата.

### `__init__`

```python
    def __init__(self, time_limit: int = 2) -> None:
        """
        Инициализирует `ThrottlingMiddleware`.

        Args:
            time_limit (int, optional): Время в секундах, в течение которого разрешено отправлять только одно сообщение. По умолчанию `2`.
        """
        ...
```

**Параметры**:
- `time_limit` (int, optional): Время в секундах, в течение которого разрешено отправлять только одно сообщение. По умолчанию `2`.

**Как работает функция**:

1.  Функция `__init__` инициализирует класс `ThrottlingMiddleware`.
2.  Внутри функции создается экземпляр `TTLCache` с максимальным размером 10000 и временем жизни (TTL), равным `time_limit`. Этот кэш используется для хранения информации о том, когда пользователь последний раз отправлял сообщение.

### `__call__`

```python
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        """
        Вызывается для каждого входящего сообщения. Проверяет, не превышен ли лимит сообщений для данного чата.

        Args:
            handler (Callable[[Message, Dict[str, Any]], Awaitable[Any]]): Обработчик сообщения.
            event (Message): Объект сообщения от Telegram.
            data (Dict[str, Any]): Дополнительные данные.

        Returns:
            Any: Результат обработки сообщения.
        """
        ...
```

**Параметры**:

- `handler` (Callable[[Message, Dict[str, Any]], Awaitable[Any]]): Обработчик сообщения.
- `event` (Message): Объект сообщения от Telegram.
- `data` (Dict[str, Any]): Дополнительные данные.

**Как работает функция**:

1.  Функция `__call__` вызывается для каждого входящего сообщения.
2.  Сначала проверяется, находится ли идентификатор чата (`event.chat.id`) в кэше `self.limit`.
3.  Если идентификатор чата уже есть в кэше, это означает, что пользователь недавно отправлял сообщение, и функция немедленно завершается, игнорируя сообщение.
4.  Если идентификатора чата нет в кэше, он добавляется в кэш, и сообщение передается обработчику `handler`.

**Примеры**:

```python
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
import asyncio
from typing import Any, Dict

# Импортируем ThrottlingMiddleware из текущего модуля
from middlewares.throttling import ThrottlingMiddleware

# Токен вашего бота
BOT_TOKEN = "YOUR_BOT_TOKEN"

# Создаем экземпляры бота и диспетчера
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Регистрируем ThrottlingMiddleware
dp.message.middleware(ThrottlingMiddleware(time_limit=2))

# Обработчик команды /start
@dp.message.handler(CommandStart())
async def start_handler(message: Message, data: Dict[str, Any]):
    await message.answer("Привет! Я бот с троттлингом.")

# Обработчик всех остальных сообщений
@dp.message.handler()
async def echo_handler(message: Message, data: Dict[str, Any]):
    await message.answer(f"Ты написал: {message.text}")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
```
```
В этом примере ThrottlingMiddleware ограничивает частоту отправки сообщений до одного сообщения в 2 секунды.