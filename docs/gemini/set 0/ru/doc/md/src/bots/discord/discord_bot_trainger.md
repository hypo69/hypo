# Модуль discord_bot_trainger.py

## Обзор

Данный модуль содержит код для бота Discord, предназначенного для взаимодействия с пользователем и обучения модели.  Бот умеет присоединяться к голосовым каналам, обрабатывать команды, распознавать речь из вложений, отправлять текстовые сообщения и аудиоответы.  Поддерживается обучение модели на предоставленных данных.

## Оглавление

- [Модуль discord_bot_trainger.py](#модуль-discord_bot_traingerpy)
- [Переменные](#переменные)
- [Функции](#функции)
- [Методы](#методы)
- [Обработчики событий](#обработчики-событий)


## Переменные

### `MODE`

**Описание**:  Устанавливает режим работы бота (например, 'dev', 'prod').

### `PREFIX`

**Описание**: Префикс команд для бота.

### `intents`

**Описание**: Объект `discord.Intents`, определяющий события, на которые будет реагировать бот.


### `bot`

**Описание**: Объект `commands.Bot`, представляющий бота Discord.

### `model`

**Описание**: Объект класса `Model`, содержащий модель, на которой обучается бот.

### `path_to_ffmpeg`

**Описание**: Путь к исполняемому файлу ffmpeg.

## Функции

### `store_correction(original_text: str, correction: str)`

**Описание**: Сохраняет исправления в файл `corrections_log.txt`.

**Параметры**:
- `original_text` (str): Исходный текст.
- `correction` (str): Исправление.

**Возвращает**:
- Не имеет возвращаемого значения.

### `text_to_speech_and_play(text, channel)`

**Описание**: Преобразует текст в аудио и воспроизводит его в голосовом канале.

**Параметры**:
- `text` (str): Текст для преобразования.
- `channel` (discord.channel): Голосовой канал.

**Возвращает**:
- Не имеет возвращаемого значения.

## Методы

(Методы классов, не относящихся к `discord.ext.commands`)  - находятся в подключаемых модулях (модуль `src`, `gs` и др.) и не документированы здесь, т.к. их реализация  не видна.

## Обработчики событий

### `on_ready()`

**Описание**: Вызывается, когда бот готов к работе.

**Параметры**:
- Не имеет параметров.

**Возвращает**:
- Не имеет возвращаемого значения.


### `on_message(message)`

**Описание**: Обрабатывает входящие сообщения.

**Параметры**:
- `message` (discord.Message): Входящее сообщение.

**Возвращает**:
- Не имеет возвращаемого значения.


## Команды

### `hi(ctx)`

**Описание**:  Принимает команду `!hi` и возвращает приветствие.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Объект контекста команды.

**Возвращает**:
- `True` в случае успешного выполнения.

### `join(ctx)`

**Описание**: Подключается к голосовому каналу пользователя.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Объект контекста команды.


**Возвращает**:
- Не имеет возвращаемого значения.


### `leave(ctx)`

**Описание**: Отключается от голосового канала.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Объект контекста команды.

**Возвращает**:
- Не имеет возвращаемого значения.


### `train(ctx, data=None, data_dir=None, positive=True, attachment=None)`

**Описание**: Обучает модель.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Объект контекста команды.
- `data` (str, optional): Путь к данным для обучения.
- `data_dir` (str, optional): Директория с данными для обучения.
- `positive` (bool, optional): Флаг для определения типа данных (положительные или отрицательные).
- `attachment` (discord.Attachment, optional): Прикреплённый файл.

**Возвращает**:
- Не имеет возвращаемого значения.

### `test(ctx, test_data: str)`

**Описание**: Проводит тестирование модели.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Объект контекста команды.
- `test_data` (str): Данные для тестирования (строка JSON).

**Возвращает**:
- Не имеет возвращаемого значения. Возможны исключения.


### `archive(ctx, directory: str)`

**Описание**: Архивирует файлы в указанной директории.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Объект контекста команды.
- `directory` (str): Путь к директории для архивирования.

**Возвращает**:
- Не имеет возвращаемого значения.


### `select_dataset(ctx, path_to_dir_positive: str, positive=True)`

**Описание**: Выбирает и архивирует набор данных для обучения.


**Параметры**:
- `ctx` (discord.ext.commands.Context): Объект контекста команды.
- `path_to_dir_positive` (str): Путь к директории с положительными примерами.
- `positive` (bool, optional): Флаг для определения типа данных.

**Возвращает**:
- Не имеет возвращаемого значения.


### `instruction(ctx)`

**Описание**: Выводит инструкции из внешнего файла.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Объект контекста команды.

**Возвращает**:
- Не имеет возвращаемого значения.


### `correct(ctx, message_id: int, *, correction: str)`

**Описание**: Исправляет предыдущий ответ.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Объект контекста команды.
- `message_id` (int): ID сообщения.
- `correction` (str): Исправление.

**Возвращает**:
- Не имеет возвращаемого значения.



### `feedback(ctx, *, feedback_text: str)`

**Описание**: Отправляет обратную связь.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Объект контекста команды.
- `feedback_text` (str): Текст обратной связи.

**Возвращает**:
- Не имеет возвращаемого значения.


### `getfile(ctx, file_path: str)`

**Описание**: Прикрепляет файл к сообщению.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Объект контекста команды.
- `file_path` (str): Путь к файлу.

**Возвращает**:
- Не имеет возвращаемого значения.