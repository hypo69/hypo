# Модуль `discord_bot_trainger.py`

## Обзор

Модуль `discord_bot_trainger.py` реализует Discord-бота для обучения и тестирования языковой модели. Бот позволяет пользователям отправлять команды для управления обучением, тестированием, архивированием данных и взаимодействия с моделью.

## Содержание

- [Обзор](#обзор)
- [Константы](#константы)
- [Импорты](#импорты)
- [Глобальные переменные](#глобальные-переменные)
- [События](#события)
  - [`on_ready`](#on_ready)
  - [`on_message`](#on_message)
- [Команды](#команды)
  - [`hi`](#hi)
  - [`join`](#join)
  - [`leave`](#leave)
  - [`train`](#train)
  - [`test`](#test)
  - [`archive`](#archive)
  - [`select_dataset`](#select_dataset)
  - [`instruction`](#instruction)
  - [`correct`](#correct)
  - [`feedback`](#feedback)
  - [`getfile`](#getfile)
- [Функции](#функции)
    - [`store_correction`](#store_correction)
    - [`text_to_speech_and_play`](#text_to_speech_and_play)
- [Запуск бота](#запуск-бота)

## Константы

### `MODE`
```python
MODE = 'dev'
```
Режим работы бота, в данном случае установлен в 'dev'.

### `PREFIX`
```python
PREFIX = '!'
```
Префикс для вызова команд бота.

## Импорты

```python
import discord
from discord.ext import commands
from pathlib import Path
import tempfile
import asyncio
import header
from src import gs
from src.ai.openai.model.training import Model
from src.utils.jjson import j_loads_ns, j_loads_ns, j_dumps
from src.logger.logger import logger
import speech_recognition as sr
import requests
from pydub import AudioSegment
from gtts import gTTS
from .chatterbox import *
```
Импортированы необходимые библиотеки для работы с Discord API, файловой системой, асинхронностью, JSON, логированием, распознаванием и синтезом речи, а также пользовательский модуль `chatterbox`.

## Глобальные переменные

### `bot`
```python
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)
```
Объект бота Discord.

### `model`
```python
model = Model()
```
Объект модели для обучения и предсказаний.

## События

### `on_ready`

```python
@bot.event
async def on_ready():
    """Called when the bot is ready."""
    logger.info(f'Logged in as {bot.user}')
```

**Описание**: Вызывается, когда бот готов к работе. Логирует информацию о том, под каким пользователем запущен бот.

### `on_message`

```python
@bot.event
async def on_message(message):
    """Handle incoming messages and respond to voice commands."""
    #logger.info(f'on_message({message})')
    if message.author == bot.user:
        return  # Игнорируем сообщения от самого себя

    if message.content.startswith(PREFIX):
        await bot.process_commands(message)
        return  # Обрабатываем команды

    if message.attachments:
        # Check if it's an audio attachment
        if message.attachments[0].content_type.startswith('audio/'):
            recognized_text = recognizer(message.attachments[0].url)
            #await message.channel.send(recognized_text)
            response = model.send_message(recognized_text)

    else:
        response = model.send_message(message.content)
    if message.author.voice:
        # Если пользователь находится в голосовом канале, подключаемся и воспроизводим ответ
        await text_to_speech_and_play(response, message.author.voice.channel)
    else:
        await message.channel.send(response)  # Отправляем ответ в текстовый канал
```
**Описание**: Обрабатывает входящие сообщения. Игнорирует сообщения от самого бота, обрабатывает команды, распознает речь из аудио-вложений или обрабатывает текстовые сообщения и отправляет ответ, либо воспроизводит его голосом, если пользователь находится в голосовом канале.

## Команды

### `hi`

```python
@bot.command(name='hi')
async def hi(ctx):
    """Welcome message."""
    logger.info(f'hi({ctx})')
    await ctx.send('HI!')
    return True
```

**Описание**: Отправляет приветственное сообщение "HI!".

**Параметры**:
- `ctx`: Контекст команды.

**Возвращает**:
- `True`: В случае успешного выполнения.

### `join`

```python
@bot.command(name='join')
async def join(ctx):
    """Connect the bot to the voice channel."""
    logger.info(f'join({ctx})')
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f'Joined {channel}')
    else:
        await ctx.send('You are not in a voice channel.')
```

**Описание**: Подключает бота к голосовому каналу, в котором находится автор команды.

**Параметры**:
- `ctx`: Контекст команды.

### `leave`

```python
@bot.command(name='leave')
async def leave(ctx):
    """Disconnect the bot from the voice channel."""
    logger.info(f'leave({ctx})')
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send('Disconnected from the voice channel.')
    else:
        await ctx.send('I am not in a voice channel.')
```

**Описание**: Отключает бота от текущего голосового канала.

**Параметры**:
- `ctx`: Контекст команды.

### `train`

```python
@bot.command(name='train')
async def train(ctx, data: str = None, data_dir: str = None, positive: bool = True, attachment: discord.Attachment = None):
    """Train the model with the provided data."""
    logger.info(f'train({ctx})')
    if attachment:
        file_path = f"/tmp/{attachment.filename}"
        await attachment.save(file_path)
        data = file_path

    job_id = model.train(data, data_dir, positive)
    if job_id:
        await ctx.send(f'Model training started. Job ID: {job_id}')
        model.save_job_id(job_id, "Training task started")
    else:
        await ctx.send('Failed to start training.')
```

**Описание**: Запускает процесс обучения модели с предоставленными данными.

**Параметры**:
- `ctx`: Контекст команды.
- `data` (str, optional): Путь к файлу с данными или сами данные.
- `data_dir` (str, optional): Путь к директории с данными.
- `positive` (bool, optional): Флаг, указывающий, являются ли данные позитивными. По умолчанию `True`.
- `attachment` (discord.Attachment, optional): Вложение с данными.
**Возвращает**:
    - `None`
    
### `test`

```python
@bot.command(name='test')
async def test(ctx, test_data: str):
    """Test the model with the provided test data."""
    logger.info(f'test({ctx})')
    try:
        test_data = j_loads(test_data)
        predictions = model.predict(test_data)
        if predictions:
            await ctx.send(f'Test complete. Predictions: {predictions}')
            model.handle_errors(predictions, test_data)
        else:
            await ctx.send('Failed to get predictions.')
    except json.JSONDecodeError:
        await ctx.send('Invalid test data format. Please provide a valid JSON string.')
```

**Описание**: Тестирует модель с предоставленными тестовыми данными.

**Параметры**:
- `ctx`: Контекст команды.
- `test_data` (str): Тестовые данные в формате JSON.

**Вызывает исключения**:
- `json.JSONDecodeError`: Если `test_data` не является валидной JSON строкой.

### `archive`

```python
@bot.command(name='archive')
async def archive(ctx, directory: str):
    """Archive files in the specified directory."""
    logger.info(f'archive({ctx})')
    try:
        await model.archive_files(directory)
        await ctx.send(f'Files in {directory} have been archived.')
    except Exception as ex:
        await ctx.send(f'An error occurred while archiving files: {ex}')
```

**Описание**: Архивация файлов в указанной директории.

**Параметры**:
- `ctx`: Контекст команды.
- `directory` (str): Путь к директории для архивации.

**Вызывает исключения**:
- `Exception`: Если возникла ошибка во время архивирования файлов.

### `select_dataset`

```python
@bot.command(name='select_dataset')
async def select_dataset(ctx, path_to_dir_positive: str, positive: bool = True):
    """Select a dataset for training the model."""
    logger.info(f'select_dataset({ctx})')
    dataset = await model.select_dataset_and_archive(path_to_dir_positive, positive)
    if dataset:
        await ctx.send(f'Dataset selected and archived. Dataset: {dataset}')
    else:
        await ctx.send('Failed to select dataset.')
```

**Описание**: Выбирает набор данных для обучения модели.

**Параметры**:
- `ctx`: Контекст команды.
- `path_to_dir_positive` (str): Путь к директории с данными.
- `positive` (bool, optional): Флаг, указывающий, являются ли данные позитивными. По умолчанию `True`.

### `instruction`

```python
@bot.command(name='instruction')
async def instruction(ctx):
    """Display the instruction message from an external file."""
    logger.info(f'instruction({ctx})')
    try:
        instructions_path = Path("_docs/bot_instruction.md")
        if instructions_path.exists():
            with instructions_path.open("r") as file:
                instructions = file.read()
            await ctx.send(instructions)
        else:
            await ctx.send('Instructions file not found.')
    except Exception as ex:
        await ctx.send(f'An error occurred while reading the instructions: {ex}')
```

**Описание**: Отображает инструкцию из внешнего файла `_docs/bot_instruction.md`.

**Параметры**:
- `ctx`: Контекст команды.

**Вызывает исключения**:
- `Exception`: Если возникла ошибка при чтении файла с инструкцией.

### `correct`

```python
@bot.command(name='correct')
async def correct(ctx, message_id: int, *, correction: str):
    """Correct a previous response by providing the message ID and the correction."""
    logger.info(f'correct({ctx})')
    try:
        message = await ctx.fetch_message(message_id)
        if message:
            # Log or store the correction
            logger.info(f"Correction for message ID {message_id}: {correction}")
            store_correction(message.content, correction)
            await ctx.send(f"Correction received: {correction}")
        else:
            await ctx.send("Message not found.")
    except Exception as ex:
        await ctx.send(f'An error occurred: {ex}')
```

**Описание**: Принимает исправление для предыдущего ответа по его ID.

**Параметры**:
- `ctx`: Контекст команды.
- `message_id` (int): ID сообщения для исправления.
- `correction` (str): Текст исправления.

**Вызывает исключения**:
- `Exception`: Если возникла ошибка при обработке.

### `feedback`

```python
@bot.command(name='feedback')
async def feedback(ctx, *, feedback_text: str):
    """Submit feedback about the model's response."""
    logger.info(f'feedback({ctx})')
    store_correction("Feedback", feedback_text)
    await ctx.send('Thank you for your feedback. We will use it to improve the model.')
```

**Описание**: Отправляет отзыв о модели.

**Параметры**:
- `ctx`: Контекст команды.
- `feedback_text` (str): Текст отзыва.

### `getfile`

```python
@bot.command(name='getfile')
async def getfile(ctx, file_path: str):
    """Attach a file from the given path."""
    logger.info(f'getfile({ctx})')
    file_to_attach = Path(file_path)
    if file_to_attach.exists():
        await ctx.send("Here is the file you requested:", file=discord.File(file_to_attach))
    else:
        await ctx.send(f'File not found: {file_path}')
```

**Описание**: Прикрепляет файл из указанного пути к сообщению.

**Параметры**:
- `ctx`: Контекст команды.
- `file_path` (str): Путь к файлу.

## Функции

### `store_correction`

```python
def store_correction(original_text: str, correction: str):
    """Store the correction for future reference or retraining."""
    logger.info('store_correction()')
    correction_file = Path("corrections_log.txt")
    with correction_file.open("a") as file:
        file.write(f"Original: {original_text}\nCorrection: {correction}\n\n")
```

**Описание**: Сохраняет оригинальный текст и его исправление в файл `corrections_log.txt`.

**Параметры**:
- `original_text` (str): Оригинальный текст.
- `correction` (str): Исправленный текст.

### `text_to_speech_and_play`

```python
async def text_to_speech_and_play(text, channel):
    """Convert text to speech and play it in a voice channel."""
    tts = gTTS(text=text, lang='ru')  # Замените 'ru' на нужный язык
    audio_file_path = f"{tempfile.gettempdir()}/response.mp3"  # Путь к временно созданному файлу
    tts.save(audio_file_path)  # Сохраняем аудиофайл

    voice_channel = channel.guild.voice_client
    if not voice_channel:
        voice_channel = await channel.connect()  # Подключаемся к голосовому каналу

    voice_channel.play(discord.FFmpegPCMAudio(audio_file_path), after=lambda ex: logger.info(f'Finished playing: {ex}'))

    while voice_channel.is_playing():  # Ждем пока играет звук
        await asyncio.sleep(1)

    await voice_channel.disconnect()  # Отключаемся
```

**Описание**: Преобразует текст в речь и воспроизводит его в голосовом канале.

**Параметры**:
- `text` (str): Текст для преобразования в речь.
- `channel`: Голосовой канал, в котором нужно воспроизвести речь.
**Вызывает исключения**:
    - `Exception`: Если возникла ошибка во время воспросизведения.

## Запуск бота

```python
if __name__ == "__main__":
    bot.run(gs.credentials.discord.bot_token)
```

**Описание**: Запускает бота с использованием токена из настроек.