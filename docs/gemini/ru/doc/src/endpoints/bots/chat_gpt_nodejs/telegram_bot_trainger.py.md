# Модуль telegram_bot_trainger.py

## Обзор

Модуль реализует Telegram-бота, использующего библиотеку python-telegram-bot. Бот поддерживает команды `/start` и `/help`, обрабатывает текстовые сообщения, голосовые сообщения и документы для обучения модели.

## Оглавление

1. [Импорты](#Импорты)
2. [Переменные](#Переменные)
3. [Функции](#Функции)
    - [`start`](#start)
    - [`help_command`](#help_command)
    - [`handle_document`](#handle_document)
    - [`handle_message`](#handle_message)
    - [`handle_voice`](#handle_voice)
    - [`main`](#main)
    
## Импорты

В данном модуле используются следующие библиотеки:
- `pathlib` - для работы с путями к файлам
- `tempfile` - для создания временных файлов
- `asyncio` - для асинхронного программирования
- `telegram` - для работы с Telegram API
- `telegram.ext` - для создания Telegram-ботов
- `header` - кастомный модуль
- `src.gs` - кастомный модуль
- `src.ai.openai.model.training` - кастомный модуль для обучения модели
- `src.utils.jjson` - кастомный модуль для работы с JSON
- `src.logger.logger` - кастомный модуль для логирования
- `speech_recognition` - для распознавания речи
- `requests` - для отправки HTTP запросов
- `pydub` - для обработки аудио файлов
- `gtts` - для конвертации текста в речь
- `src.utils.convertors.tts` - кастомный модуль для конвертации текста в речь

## Переменные

- `model`: Экземпляр класса `Model` для взаимодействия с моделью обучения.
- `TELEGRAM_TOKEN`: Токен для Telegram бота, полученный из `gs.credentials.telegram.bot_token`.

## Функции

### `start`

**Описание**:
Обрабатывает команду `/start`.

**Параметры**:
- `update` (Update): Объект обновления от Telegram.
- `context` (CallbackContext): Контекст обратного вызова.

**Возвращает**:
- `None`

**Пример использования**:
```python
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! I am your simple bot. Type /help to see available commands.')
```

### `help_command`

**Описание**:
Обрабатывает команду `/help`.

**Параметры**:
- `update` (Update): Объект обновления от Telegram.
- `context` (CallbackContext): Контекст обратного вызова.

**Возвращает**:
- `None`

**Пример использования**:
```python
async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Available commands:\\n/start - Start the bot\\n/help - Show this help message')
```

### `handle_document`

**Описание**:
Обрабатывает загруженные документы. Сохраняет документ во временный файл, читает его содержимое и отправляет его в модель для обучения.

**Параметры**:
- `update` (Update): Объект обновления от Telegram.
- `context` (CallbackContext): Контекст обратного вызова.

**Возвращает**:
- `None`

**Пример использования**:
```python
async def handle_document(update: Update, context: CallbackContext):
    file = await update.message.document.get_file()
    tmp_file_path = await file.download_to_drive()
    with open(tmp_file_path, 'r') as f:
        file_content = f.read()
    response = model.send_message(f"Обучение модели на следующем содержимом:{file_content}")
    await update.message.reply_text(response)
```

### `handle_message`

**Описание**:
Обрабатывает текстовые сообщения. Отправляет полученный текст в модель и возвращает ответ пользователю.

**Параметры**:
- `update` (Update): Объект обновления от Telegram.
- `context` (CallbackContext): Контекст обратного вызова.

**Возвращает**:
- `None`

**Пример использования**:
```python
async def handle_message(update: Update, context: CallbackContext) -> None:
    text_received = update.message.text
    response = model.send_message(text_received)
    await update.message.reply_text(response)
```

### `handle_voice`

**Описание**:
Обрабатывает голосовые сообщения. Распознает речь из голосового сообщения и отправляет её в модель для обработки, после чего возвращает ответ пользователю и воспроизводит его голосом.

**Параметры**:
- `update` (Update): Объект обновления от Telegram.
- `context` (CallbackContext): Контекст обратного вызова.

**Возвращает**:
- `None`

**Пример использования**:
```python
async def handle_voice(update: Update, context: CallbackContext) -> None:
    voice_file = await update.message.voice.get_file()
    message = recognizer(audio_url=voice_file.file_path)
    response = model.send_message(message)
    await update.message.reply_text(response)
    tts_file_path = await text_to_speech (response)
    await update.message.reply_audio(audio=open(tts_file_path, 'rb'))
```

### `main`

**Описание**:
Главная функция для запуска бота. Инициализирует приложение Telegram, добавляет обработчики команд и сообщений и запускает бота.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Пример использования**:
```python
def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.VOICE, handle_voice))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    application.run_polling()
```