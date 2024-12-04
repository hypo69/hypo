# Голосовой помощник chatgpt - telegram

## Обзор

Данный модуль представляет собой интеграцию чат-бота ChatGPT с Telegram.  Он позволяет пользователям Telegram общаться с чат-ботом ChatGPT, используя текстовые сообщения.

## Структура модуля

Модуль организован в соответствии с функциональностью чат-бота.

## Функции

### `start_bot`

**Описание**: Функция запускает чат-бота.

**Параметры**:
- `API_TOKEN` (str): Токен доступа к Telegram боту.
- `CHAT_ID` (str): ID чата в Telegram, с которым будет взаимодействовать бот.

**Возвращает**:
- `None`: Функция не возвращает значение.

**Вызывает исключения**:
- `ValueError`: Если передан некорректный API токен или ID чата.


### `handle_message`

**Описание**: Обрабатывает входящие сообщения от пользователей Telegram.

**Параметры**:
- `update` (object): Объект, содержащий данные о входящем сообщении.

**Возвращает**:
- `None`: Функция не возвращает значение.

**Вызывает исключения**:
- `TypeError`: Если передан некорректный тип данных.
- `Exception`: Общее исключение для других возможных ошибок.

## Классы

### `ChatGPTBot`

**Описание**:  Класс, представляющий чат-бота ChatGPT для Telegram.

**Методы**:
- `__init__(self, api_token, chat_id)`: Инициализирует бота с заданным API токеном и ID чата.
- `start(self)`: Запускает бота.
- `handle_update(self, update)`: Обрабатывает обновление Telegram.
- `send_message(self, message)`: Отправляет сообщение в Telegram.


## Использование

Для использования модуля необходимо:

1. Установить необходимые библиотеки.
2. Задать API токен и ID чата.
3. Вызвать функцию `start_bot`.

## Примеры

```python
# Пример использования
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from .bot import ChatGPTBot  #  Предполагается, что бот находится в файле bot.py

# Вставьте сюда ваш API токен и ID чата
API_TOKEN = "YOUR_API_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"


def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update.message.reply_text("Привет! Напиши мне что-нибудь.")


def main() -> None:
   
    bot = ChatGPTBot(API_TOKEN, CHAT_ID)
    bot.start()

if __name__ == "__main__":
    main()

```


```