# Модуль `kazarinov_bot`

## Обзор

Модуль `kazarinov_bot.py` представляет собой Telegram-бота для проекта Kazarinov. Бот взаимодействует с парсером Mexiron и моделью Google Generative AI, поддерживает обработку текстовых сообщений, документов и URL.

## Содержание

- [Классы](#классы)
    - [`KazarinovTelegramBot`](#kazarinovtelegrambot)
- [Функции](#функции)

## Классы

### `KazarinovTelegramBot`

**Описание**: Класс `KazarinovTelegramBot` реализует Telegram-бота с пользовательским поведением для проекта Kazarinov. Наследуется от `TelegramBot` и `BotHandler`.

**Параметры**:\
- `token` (str): Токен Telegram-бота.\
- `config` (SimpleNamespace): Конфигурация бота, загружаемая из `kazarinov.json`.\
- `model` (GoogleGenerativeAI): Модель Google Generative AI для диалога с пользователем.

**Методы**:

- `__init__(self, mode: Optional[str] = None, webdriver_name: Optional[str] = 'firefox')`
    
    **Описание**: Инициализирует экземпляр `KazarinovTelegramBot`.

    **Параметры**:
    - `mode` (Optional[str], optional): Режим работы ('test' или 'production'). По умолчанию `None`, используется значение из конфигурации.
    - `webdriver_name` (Optional[str], optional): Имя веб-драйвера для `BotHandler`. По умолчанию `'firefox'`.

- `handle_message(self, update: Update, context: CallbackContext) -> None`
    
    **Описание**: Обрабатывает текстовые сообщения, направляя URL на соответствующую обработку,  остальные сообщения обрабатываются моделью.

    **Параметры**:
    - `update` (Update): Объект `Update` от Telegram.
    - `context` (CallbackContext): Объект `CallbackContext` от Telegram.

## Функции
   
   Нет функций