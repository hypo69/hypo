# Модуль `src.endpoints.kazarinov`

## Обзор

Модуль `src.endpoints.kazarinov` предоставляет функциональность для работы с ботом Kazarinov в Telegram. Он содержит класс `KazarinovTelegramBot`, который используется для взаимодействия с ботом.

## Содержание

1. [Классы](#классы)
    - [`KazarinovTelegramBot`](#kazarinovtelegrambot)

## Классы

### `KazarinovTelegramBot`

**Описание**: 
Класс `KazarinovTelegramBot` представляет собой реализацию телеграм бота Kazarinov.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `KazarinovTelegramBot`.
- `run`: Запускает бота.
- `on_start`: Обрабатывает команду `/start`.
- `on_message`: Обрабатывает текстовые сообщения от пользователя.
- `on_error`: Обрабатывает ошибки, возникающие при работе бота.
- `process_message`: Обрабатывает входящее сообщение.
- `send_message`: Отправляет сообщение пользователю.

**Параметры**:

- `bot_token` (str): Токен бота для Telegram API.
- `allowed_user_ids` (List[int]): Список ID пользователей, которым разрешено использовать бота.
- `ai_client` (Optional[ChatGptClient]): Экземпляр клиента для ChatGPT API, по умолчанию `None`.
- `allowed_groups` (Optional[List[int]]): Список ID групп, в которых бот может работать, по умолчанию `None`.

```python
from .kazarinov_bot import KazarinovTelegramBot
```