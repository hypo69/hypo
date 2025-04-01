# Модуль `bot_aiogram.py`

## Обзор

Модуль `bot_aiogram.py` предоставляет реализацию Telegram-бота с использованием библиотеки `aiogram` и интеграцией с сервером FastAPI через RPC. Он включает в себя классы для управления ботом, регистрации обработчиков и настройки вебхуков.

## Подробней

Основная цель этого модуля - создать Telegram-бота, способного взаимодействовать с пользователями через Telegram API. Для этого используется библиотека `aiogram`, которая предоставляет удобные инструменты для обработки входящих сообщений, команд и других событий.

В проекте `hypotez` этот модуль отвечает за прием и обработку сообщений от пользователей Telegram, а также за взаимодействие с другими компонентами системы через RPC.

## Классы

### `TelegramBot`

**Описание**: Класс `TelegramBot` представляет собой основной класс для управления Telegram-ботом. Он инициализирует бота, регистрирует обработчики команд и сообщений, а также настраивает вебхуки для получения обновлений от Telegram.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `TelegramBot`.
- `run`: Запускает бота, инициализирует RPC и вебхуки.
- `_register_default_handlers`: Регистрирует обработчики по умолчанию.
- `_handle_message`: Обрабатывает текстовые сообщения.
- `initialize_bot_webhook`: Инициализирует вебхук бота.
- `_register_route_via_rpc`: Регистрирует маршрут Telegram вебхука через RPC.
- `stop`: Останавливает бота и удаляет вебхук.

**Параметры**:
- `token` (str): Токен Telegram-бота.
- `route` (str, optional): Вебхук маршрут для FastAPI. По умолчанию `telegram_webhook`.

#### `__init__`

```python
def __init__(self, token: str, route: str = 'telegram_webhook'):
    """
    Args:
        token (str): Telegram bot token.
        route (str): Webhook route for FastAPI. Defaults to '/telegram_webhook'.
    """
    ...
```

**Описание**: Инициализирует экземпляр класса `TelegramBot`.

**Параметры**:
- `token` (str): Токен Telegram-бота.
- `route` (str, optional): Вебхук маршрут для FastAPI. По умолчанию `'telegram_webhook'`.

#### `run`

```python
def run(self):
    """
    Args:
        self (TelegramBot): Экземпляр класса `TelegramBot`.
    
    Returns:
        None
    """
    ...
```

**Описание**: Запускает бота, инициализирует RPC и вебхуки.

**Параметры**:
- `self` (TelegramBot): Экземпляр класса `TelegramBot`.

**Возвращает**:
- `None`

#### `_register_default_handlers`

```python
def _register_default_handlers(self):
    """
    Args:
        self (TelegramBot): Экземпляр класса `TelegramBot`.
    
    Returns:
        None
    """
    ...
```

**Описание**: Регистрирует обработчики по умолчанию.

**Параметры**:
- `self` (TelegramBot): Экземпляр класса `TelegramBot`.

**Возвращает**:
- `None`

#### `_handle_message`

```python
async def _handle_message(self, message: types.Message):
    """
    Args:
        message (types.Message): Объект сообщения от Telegram.
    
    Returns:
        None
    """
    ...
```

**Описание**: Обрабатывает текстовые сообщения.

**Параметры**:
- `message` (types.Message): Объект сообщения от Telegram.

**Возвращает**:
- `None`

#### `initialize_bot_webhook`

```python
def initialize_bot_webhook(self, route: str):
    """
    Args:
        route (str): Маршрут вебхука.
    
    Returns:
        str | bool: URL вебхука или False в случае ошибки.
    """
    ...
```

**Описание**: Инициализирует вебхук бота.

**Параметры**:
- `route` (str): Маршрут вебхука.

**Возвращает**:
- `str | bool`: URL вебхука или `False` в случае ошибки.

#### `_register_route_via_rpc`

```python
def _register_route_via_rpc(self, rpc_client: ServerProxy):
    """
    Args:
        rpc_client (ServerProxy): RPC клиент для регистрации маршрута.
    
    Returns:
        None
    """
    ...
```

**Описание**: Регистрирует маршрут Telegram вебхука через RPC.

**Параметры**:
- `rpc_client` (ServerProxy): RPC клиент для регистрации маршрута.

**Возвращает**:
- `None`

#### `stop`

```python
def stop(self):
     """
     Args:
         self (TelegramBot): Экземпляр класса `TelegramBot`.
     
     Returns:
         None
     """
     ...
```

**Описание**: Останавливает бота и удаляет вебхук.

**Параметры**:
- `self` (TelegramBot): Экземпляр класса `TelegramBot`.

**Возвращает**:
- `None`

**Примеры**
```python
from dotenv import load_dotenv
import os
from src.endpoints.bots.telegram.bot_aiogram import TelegramBot

load_dotenv()
bot = TelegramBot(os.getenv('TELEGRAM_TOKEN'))
bot.run()
```

## Функции

### `__main__`

```python
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    bot = TelegramBot(os.getenv('TELEGRAM_TOKEN'))
    bot.run()
```

**Описание**: Точка входа в программу. Загружает переменные окружения из файла `.env`, создает экземпляр класса `TelegramBot` и запускает его.

**Параметры**:
- `None`

**Возвращает**:
- `None`