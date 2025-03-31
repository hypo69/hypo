# Модуль `minibot`

## Обзор

Модуль `minibot` представляет собой реализацию простого Telegram-бота, предназначенного для обработки запросов, связанных с сайтом emil-design.com. Он включает в себя обработку текстовых команд, URL-адресов, голосовых сообщений и документов. Бот использует Google Gemini AI для генерации ответов на текстовые запросы.

## Подробнее

Модуль состоит из нескольких основных частей:

1.  **Обработчик бота (`BotHandler`)**: Класс, который обрабатывает различные типы сообщений и команд, поступающих от пользователя. Он включает в себя методы для обработки URL-адресов, текстовых сообщений и команды `--next`.
2.  **Конфигурация (`Config`)**: Класс, содержащий настройки бота, такие как токен, идентификатор канала и пути к файлам.
3.  **Запуск бота (`bot.py`)**: Основной блок, который инициализирует бота, регистрирует обработчики команд и запускает прослушивание входящих сообщений.

Этот бот может быть использован для предоставления информации о продуктах или услугах emil-design.com, обработки заказов или предоставления поддержки пользователям.

## Классы

### `BotHandler`

**Описание**: Обработчик команд, полученных ботом.

**Методы**:

*   `__init__`: Инициализация обработчика событий телеграм-бота.
*   `handle_message`: Обработка текстовых сообщений.
*   `_send_user_flowchart`: Отправка схемы user\_flowchart.
*   `_handle_url`: Обработка URL, присланного пользователем.
*   `_handle_next_command`: Обработка команды '--next' и её аналогов.
*   `help_command`: Обработка команды /help.
*   `send_pdf`: Обработка команды /sendpdf для отправки PDF.
*   `handle_voice`: Обработка голосовых сообщений.
*   `_transcribe_voice`: Транскрибирование голосового сообщения (заглушка).
*   `handle_document`: Обработка полученных документов.

**Параметры**:

*   `base_dir` (Path): Базовая директория для поиска ресурсов.

**Примеры**

```python
handler = BotHandler()
```

### `Config`

**Описание**: Класс, содержащий настройки бота.

**Параметры**:

*   `BOT_TOKEN` (str): Токен Telegram-бота.
*   `CHANNEL_ID` (str): Идентификатор канала Telegram.
*   `PHOTO_DIR` (Path): Путь к директории с фотографиями.
*   `COMMAND_INFO` (str): Информация о боте.
*   `UNKNOWN_COMMAND_MESSAGE` (str): Сообщение для неизвестной команды.
*   `START_MESSAGE` (str): Приветственное сообщение при запуске бота.
*   `HELP_MESSAGE` (str): Справочное сообщение с доступными командами.

**Примеры**

```python
config = Config()
```

## Функции

### `command_start`

```python
def command_start(message):
    """
    Args:
        message: Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        Exception: Если произошла ошибка при отправке сообщения.

    Example:
        Примеры вызовов
    """
    ...
```

**Описание**: Обработка команды `/start`.

**Параметры**:

*   `message`: Объект сообщения от Telegram.

**Возвращает**:

*   `None`

### `command_help`

```python
def command_help(message):
    """
    Args:
        message: Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        Exception: Если произошла ошибка при обработке команды.

    Example:
        Примеры вызовов
    """
    ...
```

**Описание**: Обработка команды `/help`.

**Параметры**:

*   `message`: Объект сообщения от Telegram.

**Возвращает**:

*   `None`

### `command_info`

```python
def command_info(message):
    """
    Args:
        message: Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        Exception: Если произошла ошибка при обработке команды.

    Example:
        Примеры вызовов
    """
    ...
```

**Описание**: Обработка команды `/info`.

**Параметры**:

*   `message`: Объект сообщения от Telegram.

**Возвращает**:

*   `None`

### `command_time`

```python
def command_time(message):
    """
    Args:
        message: Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        Exception: Если произошла ошибка при обработке команды.

    Example:
        Примеры вызовов
    """
    ...
```

**Описание**: Обработка команды `/time`.

**Параметры**:

*   `message`: Объект сообщения от Telegram.

**Возвращает**:

*   `None`

### `command_photo`

```python
def command_photo(message):
    """
    Args:
        message: Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        FileNotFoundError: Если директория с фото не найдена.
        Exception: Если произошла ошибка при отправке фото.

    Example:
        Примеры вызовов
    """
    ...
```

**Описание**: Обработка команды `/photo`.

**Параметры**:

*   `message`: Объект сообщения от Telegram.

**Возвращает**:

*   `None`

### `handle_voice_message`

```python
def handle_voice_message(message):
    """
    Args:
        message: Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        Exception: Если произошла ошибка при обработке голосового сообщения.

    Example:
        Примеры вызовов
    """
    ...
```

**Описание**: Обработка голосовых сообщений.

**Параметры**:

*   `message`: Объект сообщения от Telegram.

**Возвращает**:

*   `None`

### `handle_document_message`

```python
def handle_document_message(message):
    """
    Args:
        message: Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        Exception: Если произошла ошибка при обработке документа.

    Example:
        Примеры вызовов
    """
    ...
```

**Описание**: Обработка документов, отправленных боту.

**Параметры**:

*   `message`: Объект сообщения от Telegram.

**Возвращает**:

*   `None`

### `handle_text_message`

```python
def handle_text_message(message):
    """
    Args:
        message: Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        Exception: Если произошла ошибка при обработке текстового сообщения.

    Example:
        Примеры вызовов
    """
    ...
```

**Описание**: Обработка текстовых сообщений, не начинающихся с `/`.

**Параметры**:

*   `message`: Объект сообщения от Telegram.

**Возвращает**:

*   `None`

### `handle_unknown_command`

```python
def handle_unknown_command(message):
    """
    Args:
        message: Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        Exception: Если произошла ошибка при обработке неизвестной команды.

    Example:
        Примеры вызовов
    """
    ...
```

**Описание**: Обработка неизвестных команд, начинающихся с `/`.

**Параметры**:

*   `message`: Объект сообщения от Telegram.

**Возвращает**:

*   `None`