# Голосовой помощник ChatGPT - Telegram

## Обзор

Этот модуль предоставляет функциональность для взаимодействия с голосовым помощником ChatGPT через Telegram.  Он обеспечивает обработку сообщений, отправку ответов и управление диалогами.


## Функции

### `send_message`

**Описание**: Отправляет сообщение в Telegram-чат.

**Параметры**:
- `chat_id` (int): Идентификатор чата в Telegram.
- `text` (str): Текст сообщения.

**Возвращает**:
- `bool`: `True`, если сообщение отправлено успешно, `False` - в противном случае.

**Исключения**:
- `TelegramError`: Возникает при проблемах с отправкой сообщения в Telegram.


### `get_message`

**Описание**: Получает сообщение из Telegram-чата.

**Параметры**:
- `chat_id` (int): Идентификатор чата в Telegram.

**Возвращает**:
- `str`: Текст полученного сообщения.
- `None`: Если сообщение не получено.

**Исключения**:
- `TelegramError`: Возникает при проблемах с получением сообщения из Telegram.