# Модуль `src.endpoints.hypo69.code_assistant.onela_bot`

## Обзор

Модуль `src.endpoints.hypo69.code_assistant.onela_bot` предназначен для взаимодействия с моделью ассистента программиста через чат в Telegram. Он предоставляет класс `OnelaBot`, который наследуется от `TelegramBot` и обрабатывает текстовые сообщения и документы, отправленные боту.

## Подробнее

Этот модуль позволяет пользователям взаимодействовать с AI-моделью (в данном случае, Google Gemini) через Telegram для получения помощи в задачах, связанных с программированием. Он включает функциональность для обработки как текстовых сообщений, так и загруженных документов. Модуль использует библиотеку `telegram.ext` для обработки обновлений от Telegram и модуль `src.logger.logger` для логирования ошибок.

## Классы

### `OnelaBot`

**Описание**: Класс `OnelaBot` обеспечивает взаимодействие с моделью ассистента программиста.

**Наследует**:
- `TelegramBot`: Наследует функциональность для работы с Telegram ботом.

**Атрибуты**:
- `model` (GoogleGenerativeAI): AI модель Google Gemini для обработки запросов.

**Методы**:
- `__init__`: Инициализирует объект `OnelaBot`.
- `handle_message`: Обрабатывает входящие текстовые сообщения.
- `handle_document`: Обрабатывает входящие документы.

### `__init__`

```python
    def __init__(self) -> None:
        """
        Инициализация объекта OnelaBot.
        """
        super().__init__(gs.credentials.telegram.onela_bot)
```

**Назначение**: Инициализирует объект `OnelaBot`, вызывая конструктор родительского класса `TelegramBot` с использованием учетных данных Telegram бота.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Как работает функция**:

1. Вызывается конструктор родительского класса `TelegramBot` с передачей учетных данных Telegram бота, хранящихся в `gs.credentials.telegram.onela_bot`.

**Примеры**:

```python
bot = OnelaBot()
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

**Назначение**: Обрабатывает входящие текстовые сообщения, отправляя их в AI-модель для получения ответа и отправляя этот ответ обратно пользователю.

**Параметры**:
- `update` (Update): Объект, содержащий информацию об обновлении от Telegram.
- `context` (CallbackContext): Объект, содержащий контекст выполнения обработчика.

**Возвращает**:
- None

**Вызывает исключения**:
- Exception: В случае ошибки при обработке сообщения или взаимодействии с AI-моделью, информация об ошибке записывается в лог.

**Как работает функция**:

```
Пользователь -> [Получение текста сообщения] -> Модель Gemini
       |                                           |
       ↓                                           ↓
    Текст запроса                                 Ответ модели
       |                                           |
       ↓                                           ↓
   [Отправка запроса в модель]             [Отправка ответа пользователю]
       |                                           |
       ↓                                           ↓
      Бот <- Ответ модели

```

1. Извлекает текст сообщения из объекта `update`.
2. Извлекает ID пользователя из объекта `update`.
3. Отправляет текст сообщения в AI-модель (`self.model.chat(q)`) для получения ответа.
4. Отправляет полученный ответ обратно пользователю с помощью `update.message.reply_text(answer)`.
5. В случае возникновения исключения, логирует ошибку с использованием `logger.error`.

**Примеры**:

```python
# Пример обработки текстового сообщения
async def test_handle_message(update: Update, context: CallbackContext):
    await OnelaBot().handle_message(update, context)
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

**Назначение**: Обрабатывает загруженные документы, сохраняя их локально и отправляя информацию о файле обратно пользователю.

**Параметры**:
- `update` (Update): Объект, содержащий информацию об обновлении от Telegram.
- `context` (CallbackContext): Объект, содержащий контекст выполнения обработчика.

**Возвращает**:
- None

**Вызывает исключения**:
- Exception: В случае ошибки при обработке документа, информация об ошибке записывается в лог.

**Как работает функция**:

```
Пользователь -> [Загрузка документа] -> Telegram
       |                                   |
       ↓                                   ↓
   Документ                             [Получение информации о файле]
       |                                   |
       ↓                                   ↓
[Сохранение файла локально]               [Отправка информации о файле пользователю]
       |                                   |
       ↓                                   ↓
      Бот <- Информация о файле
```

1. Получает информацию о файле из объекта `update`.
2. Скачивает файл на диск, используя `file.download_to_drive()`.
3. Отправляет информацию о файле обратно пользователю с помощью `update.message.reply_text(file)`.
4. В случае возникновения исключения, логирует ошибку с использованием `logger.error`.

**Примеры**:

```python
# Пример обработки документа
async def test_handle_document(update: Update, context: CallbackContext):
    await OnelaBot().handle_document(update, context)
```

## Функции

### `main`

```python
if __name__ == '__main__':
    bot = OnelaBot()
    asyncio.run(bot.application.run_polling())
```

**Назначение**: Главная точка входа для запуска бота.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Как работает функция**:

1. Создает экземпляр класса `OnelaBot`.
2. Запускает бота в режиме опроса (polling) с использованием `asyncio.run` и `bot.application.run_polling()`.

**Примеры**:

Запуск бота:

```bash
python onela_bot.py