# Модуль `discord_bot_trainger`

## Обзор

Модуль `discord_bot_trainger.py` представляет собой Discord-бота, который позволяет обучать и тестировать модели машинного обучения, а также взаимодействовать с пользователями через текстовые и голосовые каналы. Бот использует библиотеку `discord.py` для взаимодействия с Discord API, а также другие библиотеки для обработки аудио и текста.

## Содержание

1. [Обзор](#обзор)
2. [Импорты](#импорты)
3. [Константы](#константы)
4. [Глобальные переменные](#глобальные-переменные)
5. [События](#события)
   - [`on_ready`](#on_ready)
   - [`on_message`](#on_message)
6. [Команды](#команды)
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
7. [Функции](#функции)
    - [`store_correction`](#store_correction)
    - [`text_to_speech_and_play`](#text_to_speech_and_play)
8. [Запуск бота](#запуск-бота)

## Импорты

Модуль импортирует следующие библиотеки:

- `discord`: для взаимодействия с Discord API.
- `discord.ext.commands`: для создания команд бота.
- `pathlib`: для работы с путями к файлам.
- `tempfile`: для создания временных файлов.
- `asyncio`: для асинхронного программирования.
- `header`: собственный модуль (не документирован).
- `src.gs`: собственный модуль для доступа к глобальным настройкам (не документирован).
- `src.ai.openai.model.training.Model`: собственный модуль для обучения моделей (не документирован).
- `src.utils.jjson`: собственный модуль для работы с JSON (не документирован).
- `src.logger.logger`: собственный модуль для логирования (не документирован).
- `speech_recognition`: для распознавания речи.
- `requests`: для скачивания файлов.
- `pydub`: для конвертации аудио.
- `gtts`: для преобразования текста в речь.
- `src.endpoints.bots.discord.chatterbox`: собственный модуль для взаимодействия с чатботом (не документирован).

## Константы

- `path_to_ffmpeg`: Путь к исполняемому файлу `ffmpeg.exe`.
- `PREFIX`: Префикс для команд бота (`!`).

## Глобальные переменные

- `intents`: Настройки интентов для бота.
- `bot`: Объект бота `commands.Bot`.
- `model`: Объект модели обучения `Model`.

## События

### `on_ready`

```python
@bot.event
async def on_ready():
    """Called when the bot is ready."""
    logger.info(f'Logged in as {bot.user}')
```
**Описание**: Вызывается, когда бот успешно подключился к Discord и готов к работе.

### `on_message`

```python
@bot.event
async def on_message(message):
    """Handle incoming messages and respond to voice commands."""
    if message.author == bot.user:
        return
    if message.content.startswith(PREFIX):
        await bot.process_commands(message)
        return
    if message.attachments:
        if message.attachments[0].content_type.startswith('audio/'):
            recognized_text = recognizer(message.attachments[0].url)
            response = model.send_message(recognized_text)
    else:
        response = model.send_message(message.content)
    if message.author.voice:
        await text_to_speech_and_play(response, message.author.voice.channel)
    else:
        await message.channel.send(response)
```

**Описание**: Обрабатывает входящие сообщения. Если сообщение начинается с префикса, то обрабатывается как команда. Если сообщение является аудиофайлом, то оно распознается и обрабатывается моделью. В остальных случаях текст сообщения отправляется на обработку модели. Ответ отправляется в текстовый канал или проигрывается в голосовом канале пользователя.

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

**Описание**: Подключает бота к голосовому каналу пользователя.

**Параметры**:
- `ctx` (`discord.ext.commands.Context`): Контекст команды.

**Возвращает**:
- `None`

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
- `ctx` (`discord.ext.commands.Context`): Контекст команды.

**Возвращает**:
- `None`

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
**Описание**: Запускает обучение модели с предоставленными данными. Данные могут быть переданы как строка, путь к директории или как вложение.

**Параметры**:
- `ctx` (`discord.ext.commands.Context`): Контекст команды.
- `data` (`str`, optional): Данные для обучения. По умолчанию `None`.
- `data_dir` (`str`, optional): Путь к директории с данными. По умолчанию `None`.
- `positive` (`bool`, optional): Указывает на положительную или отрицательную выборку. По умолчанию `True`.
- `attachment` (`discord.Attachment`, optional): Вложение с данными для обучения. По умолчанию `None`.

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

**Описание**: Запускает тестирование модели с предоставленными данными в формате JSON.

**Параметры**:
- `ctx` (`discord.ext.commands.Context`): Контекст команды.
- `test_data` (`str`): Тестовые данные в формате JSON.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `json.JSONDecodeError`: Если формат `test_data` не является корректным JSON.

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
**Описание**: Архивирует файлы в указанной директории.

**Параметры**:
- `ctx` (`discord.ext.commands.Context`): Контекст команды.
- `directory` (`str`): Путь к директории для архивации.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при архивировании.

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
**Описание**: Выбирает и архивирует набор данных для обучения модели.

**Параметры**:
- `ctx` (`discord.ext.commands.Context`): Контекст команды.
- `path_to_dir_positive` (`str`): Путь к директории с набором данных.
- `positive` (`bool`, optional): Указывает на положительную или отрицательную выборку. По умолчанию `True`.

**Возвращает**:
- `None`

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

**Описание**: Выводит инструкцию из файла `_docs/bot_instruction.md`.

**Параметры**:
- `ctx` (`discord.ext.commands.Context`): Контекст команды.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при чтении файла.

### `correct`

```python
@bot.command(name='correct')
async def correct(ctx, message_id: int, *, correction: str):
    """Correct a previous response by providing the message ID and the correction."""
    logger.info(f'correct({ctx})')
    try:
        message = await ctx.fetch_message(message_id)
        if message:
            logger.info(f"Correction for message ID {message_id}: {correction}")
            store_correction(message.content, correction)
            await ctx.send(f"Correction received: {correction}")
        else:
            await ctx.send("Message not found.")
    except Exception as ex:
        await ctx.send(f'An error occurred: {ex}')
```

**Описание**: Принимает исправление для предыдущего ответа по ID сообщения. Сохраняет исправление в лог.

**Параметры**:
- `ctx` (`discord.ext.commands.Context`): Контекст команды.
- `message_id` (`int`): ID сообщения для исправления.
- `correction` (`str`): Текст исправления.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при поиске сообщения или его обработке.

### `feedback`
```python
@bot.command(name='feedback')
async def feedback(ctx, *, feedback_text: str):
    """Submit feedback about the model's response."""
    logger.info(f'feedback({ctx})')
    store_correction("Feedback", feedback_text)
    await ctx.send('Thank you for your feedback. We will use it to improve the model.')
```
**Описание**: Принимает текст обратной связи и сохраняет его.

**Параметры**:
- `ctx` (`discord.ext.commands.Context`): Контекст команды.
- `feedback_text` (`str`): Текст обратной связи.

**Возвращает**:
- `None`

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
**Описание**: Отправляет файл из указанного пути.

**Параметры**:
- `ctx` (`discord.ext.commands.Context`): Контекст команды.
- `file_path` (`str`): Путь к файлу.

**Возвращает**:
- `None`

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
**Описание**: Записывает исходный текст и его исправление в файл `corrections_log.txt`.

**Параметры**:
- `original_text` (`str`): Исходный текст.
- `correction` (`str`): Исправленный текст.

**Возвращает**:
- `None`

### `text_to_speech_and_play`

```python
async def text_to_speech_and_play(text, channel):
    """Convert text to speech and play it in a voice channel."""
    tts = gTTS(text=text, lang='ru')
    audio_file_path = f"{tempfile.gettempdir()}/response.mp3"
    tts.save(audio_file_path)

    voice_channel = channel.guild.voice_client
    if not voice_channel:
        voice_channel = await channel.connect()

    voice_channel.play(discord.FFmpegPCMAudio(audio_file_path), after=lambda ex: logger.info(f'Finished playing: {ex}'))

    while voice_channel.is_playing():
        await asyncio.sleep(1)

    await voice_channel.disconnect()
```

**Описание**: Преобразует текст в речь и воспроизводит его в указанном голосовом канале.

**Параметры**:
- `text` (`str`): Текст для преобразования в речь.
- `channel` (`discord.VoiceChannel`): Голосовой канал для воспроизведения.

**Возвращает**:
- `None`

## Запуск бота

```python
if __name__ == "__main__":
    bot.run(gs.credentials.discord.bot_token)
```
**Описание**: Запускает бота с токеном из глобальных настроек.