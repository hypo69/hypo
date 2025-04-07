# Модуль `src.endpoints.hypo69.code_assistant.onela_bot`

## Обзор

Модуль предназначен для организации диалога с моделью ассистента программиста через чат Telegram. Он включает в себя класс `OnelaBot`, который обрабатывает текстовые сообщения и документы, взаимодействуя с AI-моделями для генерации ответов.

## Подробней

Этот модуль позволяет пользователям взаимодействовать с AI-ассистентом программиста через Telegram, отправляя текстовые запросы и загружая документы для анализа. Он использует библиотеки `telegram`, `asyncio`, и модели `GoogleGenerativeAI` из `src.ai`, чтобы обрабатывать сообщения и генерировать ответы.

## Классы

### `OnelaBot`

**Описание**: Класс `OnelaBot` предназначен для взаимодействия с моделью ассистента программиста через Telegram.

**Наследует**:
- `TelegramBot`: Этот класс наследует функциональность базового Telegram-бота из модуля `src.endpoints.bots.telegram`.

**Атрибуты**:
- `model` (GoogleGenerativeAI): Экземпляр модели GoogleGenerativeAI, используемый для генерации ответов на запросы. Модель инициализируется с использованием ключа API и конфигурации генерации.

**Методы**:
- `__init__()`: Инициализирует объект `OnelaBot`, вызывая конструктор родительского класса `TelegramBot` с использованием учетных данных Telegram бота Onela.
- `handle_message(update: Update, context: CallbackContext) -> None`: Обрабатывает входящие текстовые сообщения, отправляет их в модель для получения ответа и отправляет ответ обратно пользователю.
- `handle_document(update: Update, context: CallbackContext) -> None`: Обрабатывает загруженные документы, сохраняет их локально, отправляет информацию о файле пользователю и обрабатывает содержимое документа.

## Функции

### `__init__`

```python
    def __init__(self) -> None:
        """
        Инициализация объекта OnelaBot.
        """
        super().__init__(gs.credentials.telegram.onela_bot)
```

**Назначение**: Инициализация экземпляра класса `OnelaBot`.

**Как работает функция**:
1. Вызывается конструктор родительского класса `TelegramBot` с передачей учетных данных Telegram бота Onela.

ASCII flowchart:
```
[Начало] --> [Вызов TelegramBot.__init__] --> [Конец]
```

### `handle_message`

```python
    async def handle_message(self, update: Update, context: CallbackContext) -> None:
        """
        Обработка текстовых сообщений.

        Args:
            update (Update): Данные обновления Telegram.
            context (CallbackContext): Контекст выполнения.
        """
        q: str = update.message.text
        user_id: int = update.effective_user.id
        try:
            # Получение ответа от модели
            answer: str = await self.model.chat(q)
            await update.message.reply_text(answer)
        except Exception as ex:
            logger.error('Ошибка обработки текстового сообщения: ', ex)
            ...
```

**Назначение**: Обработка текстовых сообщений, поступающих в Telegram-бот.

**Параметры**:
- `update` (Update): Объект, содержащий информацию об обновлении из Telegram.
- `context` (CallbackContext): Объект, содержащий контекст выполнения обработчика.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Логируется в случае возникновения ошибки при обработке сообщения.

**Как работает функция**:
1. Извлекает текст сообщения из объекта `update`.
2. Извлекает ID пользователя, отправившего сообщение.
3. Пытается получить ответ от модели, используя метод `self.model.chat(q)`.
4. Отправляет полученный ответ обратно пользователю с помощью `update.message.reply_text(answer)`.
5. В случае возникновения исключения, логирует ошибку.

ASCII flowchart:
```
[Начало] --> [Извлечение текста сообщения] --> [Извлечение ID пользователя] --> [Получение ответа от модели] --> [Отправка ответа пользователю]
    ^                                                                                                          |
    |__________________________________________________________________________________________________________|
    |
    [Ошибка: Логирование]
```

**Примеры**:

```python
# Пример обработки текстового сообщения
update = Update(...)  # Объект Update, содержащий сообщение
context = CallbackContext(...)
await bot.handle_message(update, context)
```

### `handle_document`

```python
    async def handle_document(self, update: Update, context: CallbackContext) -> None:
        """
        Обработка загруженных документов.

        Args:
            update (Update): Данные обновления Telegram.
            context (CallbackContext): Контекст выполнения.
        """
        try:
            file = await update.message.document.get_file()
            tmp_file_path: Path = await file.download_to_drive()  # Сохранение файла локально
            answer: str = await update.message.reply_text(file)
            update.message.reply_text(answer)
        except Exception as ex:
            logger.error('Ошибка обработки документа: ', ex)
            ...
```

**Назначение**: Обработка документов, загруженных в Telegram-бот.

**Параметры**:
- `update` (Update): Объект, содержащий информацию об обновлении из Telegram.
- `context` (CallbackContext): Объект, содержащий контекст выполнения обработчика.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Логируется в случае возникновения ошибки при обработке документа.

**Как работает функция**:
1. Пытается получить файл из объекта `update`.
2. Скачивает файл на диск, используя метод `file.download_to_drive()`.
3. Отправляет информацию о файле пользователю с помощью `update.message.reply_text(file)`.
4. В случае возникновения исключения, логирует ошибку.

ASCII flowchart:
```
[Начало] --> [Получение файла из update] --> [Скачивание файла на диск] --> [Отправка информации о файле пользователю]
    ^                                                                                                         |
    |__________________________________________________________________________________________________________|
    |
    [Ошибка: Логирование]
```

**Примеры**:

```python
# Пример обработки документа
update = Update(...)  # Объект Update, содержащий документ
context = CallbackContext(...)
await bot.handle_document(update, context)
```

### `__main__`

```python
if __name__ == '__main__':
    bot = OnelaBot()
    asyncio.run(bot.application.run_polling())
```

**Назначение**: Основная точка входа для запуска бота.

**Как работает функция**:
1. Создает экземпляр класса `OnelaBot`.
2. Запускает бота в режиме опроса (polling) с использованием `asyncio.run`.

ASCII flowchart:
```
[Начало] --> [Создание экземпляра OnelaBot] --> [Запуск бота в режиме polling] --> [Конец]