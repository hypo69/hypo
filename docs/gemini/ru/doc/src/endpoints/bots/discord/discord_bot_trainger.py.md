# Модуль `discord_bot_trainger.py`

## Обзор

Модуль `discord_bot_trainger.py` представляет собой реализацию Discord-бота, который интегрируется с моделью машинного обучения для обработки текстовых и голосовых сообщений. Бот может подключаться к голосовым каналам, обучать модель, тестировать её, архивировать файлы и обрабатывать обратную связь.

## Оглавление

- [Обзор](#обзор)
- [Константы](#константы)
- [Импорты](#импорты)
- [Переменные](#переменные)
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

## Константы

- `MODE = 'dev'` - режим работы.
- `PREFIX = '!'` - префикс для команд бота.

## Импорты

Модуль использует следующие библиотеки:
- `discord`: для интеграции с Discord API.
- `discord.ext.commands`: для создания команд бота.
- `pathlib.Path`: для работы с путями к файлам.
- `tempfile`: для работы с временными файлами.
- `asyncio`: для асинхронного программирования.
- `header`: для общих настроек.
- `src.gs`: для доступа к глобальным настройкам.
- `src.ai.openai.model.training.Model`: класс модели для обучения.
- `src.utils.jjson`: для работы с JSON.
- `src.logger.logger`: для логирования.
- `speech_recognition`: для распознавания речи.
- `requests`: для скачивания файлов.
- `pydub`: для конвертации аудио.
- `gtts`: для текстового воспроизведения.
- `chatterbox`: для работы с текстовым чатом.

## Переменные

- `path_to_ffmpeg`: путь к исполняемому файлу ffmpeg.
- `intents`: объект `discord.Intents`, определяющий подписки бота на события Discord.
- `bot`: объект `commands.Bot`, представляющий бота Discord.
- `model`: объект `Model`, представляющий модель машинного обучения.

## События

### `on_ready`

**Описание**: Вызывается при готовности бота к работе.

```python
@bot.event
async def on_ready():
    """Called when the bot is ready."""
    logger.info(f'Logged in as {bot.user}')
```

### `on_message`

**Описание**: Обрабатывает входящие сообщения. Если сообщение является командой, она обрабатывается. Если это голосовое сообщение, оно распознается и отправляется модели. Если это текстовое сообщение, оно отправляется модели напрямую.

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

## Команды

### `hi`

**Описание**: Отправляет приветственное сообщение.

```python
@bot.command(name='hi')
async def hi(ctx):
    """Welcome message."""
    logger.info(f'hi({ctx})')
    await ctx.send('HI!')
    return True
```

### `join`

**Описание**: Подключает бота к голосовому каналу автора команды.

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

### `leave`

**Описание**: Отключает бота от текущего голосового канала.

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

### `train`

**Описание**: Запускает обучение модели с предоставленными данными.

**Параметры**:
- `ctx`: контекст команды.
- `data` (str, optional): путь к файлу данных или сам текст. По умолчанию `None`.
- `data_dir` (str, optional): путь к директории с данными. По умолчанию `None`.
- `positive` (bool, optional): флаг для положительных данных. По умолчанию `True`.
- `attachment` (discord.Attachment, optional): вложение с файлом данных. По умолчанию `None`.

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

### `test`

**Описание**: Тестирует модель с предоставленными тестовыми данными.

**Параметры**:
- `ctx`: контекст команды.
- `test_data` (str): тестовые данные в формате JSON.

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

### `archive`

**Описание**: Архивирует файлы в указанной директории.

**Параметры**:
- `ctx`: контекст команды.
- `directory` (str): путь к директории для архивирования.

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

### `select_dataset`

**Описание**: Выбирает и архивирует набор данных для обучения.

**Параметры**:
- `ctx`: контекст команды.
- `path_to_dir_positive` (str): путь к директории с положительными данными.
- `positive` (bool, optional): флаг для положительных данных. По умолчанию `True`.

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

### `instruction`

**Описание**: Отображает инструкцию из внешнего файла.

**Параметры**:
- `ctx`: контекст команды.

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

### `correct`

**Описание**: Принимает исправления к предыдущему ответу бота.

**Параметры**:
- `ctx`: контекст команды.
- `message_id` (int): ID сообщения, которое нужно исправить.
- `correction` (str): текст исправления.

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

### `feedback`

**Описание**: Принимает обратную связь от пользователя.

**Параметры**:
- `ctx`: контекст команды.
- `feedback_text` (str): текст обратной связи.

```python
@bot.command(name='feedback')
async def feedback(ctx, *, feedback_text: str):
    """Submit feedback about the model's response."""
    logger.info(f'feedback({ctx})')
    store_correction("Feedback", feedback_text)
    await ctx.send('Thank you for your feedback. We will use it to improve the model.')
```

### `getfile`

**Описание**: Отправляет файл из указанного пути в чат.

**Параметры**:
- `ctx`: контекст команды.
- `file_path` (str): путь к файлу.

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

## Функции

### `store_correction`

**Описание**: Сохраняет исправления в файл.

**Параметры**:
- `original_text` (str): оригинальный текст.
- `correction` (str): текст исправления.

```python
def store_correction(original_text: str, correction: str):
    """Store the correction for future reference or retraining."""
    logger.info('store_correction()')
    correction_file = Path("corrections_log.txt")
    with correction_file.open("a") as file:
        file.write(f"Original: {original_text}\nCorrection: {correction}\n\n")
```

### `text_to_speech_and_play`

**Описание**: Конвертирует текст в речь и воспроизводит его в голосовом канале.

**Параметры**:
- `text` (str): текст для воспроизведения.
- `channel` (discord.VoiceChannel): голосовой канал для воспроизведения.

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