# Модуль discord_bot_trainger

## Обзор

Модуль `discord_bot_trainger.py` предназначен для создания и управления Discord-ботом, который может взаимодействовать с пользователями через текстовые команды и голосовой чат. Бот интегрирован с системой обучения моделей, позволяя тренировать и тестировать модели непосредственно через Discord.

## Подробней

Этот модуль реализует Discord-бота, способного выполнять следующие функции:

- Подключение и отключение от голосовых каналов.
- Обучение моделей на основе предоставленных данных.
- Тестирование моделей с использованием JSON-данных.
- Архивирование файлов в указанных директориях.
- Выбор и архивирование наборов данных.
- Отображение инструкций из внешнего файла.
- Коррекция предыдущих ответов бота.
- Сбор обратной связи от пользователей.
- Предоставление файлов по запросу.
- Распознавание речи в аудиосообщениях (закомментировано).
- Преобразование текста в речь и воспроизведение в голосовом канале.

Бот использует библиотеку `discord.py` для интеграции с Discord, а также другие библиотеки, такие как `pydub`, `gtts`, и `speech_recognition` для обработки аудио и речи.

## Классы

### `commands.Bot`

**Описание**: Объект бота Discord, который обрабатывает команды и события.

**Методы**:
- `on_ready`: Вызывается, когда бот готов к работе.
- `command`: Декоратор для регистрации команд бота.

**Параметры**:
- `command_prefix` (str): Префикс, используемый для вызова команд бота.
- `intents` (discord.Intents): Настройки разрешений для бота.

**Примеры**
```python
# Создание экземпляра бота
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    """Called when the bot is ready."""
    logger.info(f'Logged in as {bot.user}')
```

### `Model`

**Описание**: Класс для обучения и тестирования моделей.

**Методы**:
- `train`: Запускает процесс обучения модели.
- `predict`: Получает предсказания от модели.
- `archive_files`: Архивирует файлы в указанной директории.
- `select_dataset_and_archive`: Выбирает и архивирует набор данных.
- `handle_errors`: Обрабатывает ошибки в предсказаниях.
- `save_job_id`: Сохраняет ID задачи обучения.
- `send_message`: Отправляет сообщение и получает ответ от модели.

**Параметры**:
- Нет параметров при инициализации.

**Примеры**
```python
# Создание экземпляра модели
model = Model()

# Запуск обучения модели
job_id = model.train(data, data_dir, positive)
```

## Функции

### `on_ready`

```python
@bot.event
async def on_ready():
    """Called when the bot is ready."""
    logger.info(f'Logged in as {bot.user}')
```

**Описание**: Вызывается, когда бот успешно подключился к Discord и готов к работе.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет исключений.

**Примеры**:
```python
@bot.event
async def on_ready():
    """Called when the bot is ready."""
    logger.info(f'Logged in as {bot.user}')
```

### `hi`

```python
@bot.command(name='hi')
async def hi(ctx):
    """Welcome message."""
    logger.info(f'hi({ctx})')
    await ctx.send('HI!')
    return True
```

**Описание**: Отправляет приветственное сообщение в текстовый канал.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды, содержащий информацию об отправителе и канале.

**Возвращает**:
- `bool`: `True` после успешной отправки сообщения.

**Вызывает исключения**:
- Нет исключений.

**Примеры**:
```python
@bot.command(name='hi')
async def hi(ctx):
    """Welcome message."""
    logger.info(f'hi({ctx})')
    await ctx.send('HI!')
    return True
```

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

**Описание**: Подключает бота к голосовому каналу, в котором находится пользователь, вызвавший команду.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет исключений.

**Примеры**:
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
- `ctx` (discord.ext.commands.Context): Контекст команды.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет исключений.

**Примеры**:
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

**Описание**: Запускает процесс обучения модели с использованием предоставленных данных.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды.
- `data` (str, optional): Путь к файлу с данными для обучения. По умолчанию `None`.
- `data_dir` (str, optional): Путь к директории с данными для обучения. По умолчанию `None`.
- `positive` (bool, optional): Указывает, являются ли данные положительными или отрицательными. По умолчанию `True`.
- `attachment` (discord.Attachment, optional): Приложенный файл с данными для обучения. По умолчанию `None`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет исключений.

**Примеры**:
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

**Описание**: Тестирует модель с использованием предоставленных JSON-данных.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды.
- `test_data` (str): JSON-строка с данными для тестирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `json.JSONDecodeError`: Если предоставлена невалидная JSON-строка.

**Примеры**:
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
- `ctx` (discord.ext.commands.Context): Контекст команды.
- `directory` (str): Путь к директории для архивации.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при архивации файлов.

**Примеры**:
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
- `ctx` (discord.ext.commands.Context): Контекст команды.
- `path_to_dir_positive` (str): Путь к директории с положительными данными.
- `positive` (bool, optional): Указывает, являются ли данные положительными или отрицательными. По умолчанию `True`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет исключений.

**Примеры**:
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

**Описание**: Отображает инструкции из внешнего файла.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при чтении файла инструкций.

**Примеры**:
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

**Описание**: Позволяет исправить предыдущий ответ бота, указав ID сообщения и текст исправления.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды.
- `message_id` (int): ID сообщения, которое нужно исправить.
- `correction` (str): Текст исправления.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при получении сообщения.

**Примеры**:
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

### `store_correction`

```python
def store_correction(original_text: str, correction: str):
    """Store the correction for future reference or retraining."""
    logger.info('store_correction()')
    correction_file = Path("corrections_log.txt")
    with correction_file.open("a") as file:
        file.write(f"Original: {original_text}\nCorrection: {correction}\n\n")
```

**Описание**: Сохраняет исправление для дальнейшего использования или переобучения модели.

**Параметры**:
- `original_text` (str): Оригинальный текст сообщения.
- `correction` (str): Текст исправления.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет исключений.

**Примеры**:
```python
def store_correction(original_text: str, correction: str):
    """Store the correction for future reference or retraining."""
    logger.info('store_correction()')
    correction_file = Path("corrections_log.txt")
    with correction_file.open("a") as file:
        file.write(f"Original: {original_text}\nCorrection: {correction}\n\n")
```

### `feedback`

```python
@bot.command(name='feedback')
async def feedback(ctx, *, feedback_text: str):
    """Submit feedback about the model's response."""
    logger.info(f'feedback({ctx})')
    store_correction("Feedback", feedback_text)
    await ctx.send('Thank you for your feedback. We will use it to improve the model.')
```

**Описание**: Позволяет отправить обратную связь о работе модели.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды.
- `feedback_text` (str): Текст обратной связи.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет исключений.

**Примеры**:
```python
@bot.command(name='feedback')
async def feedback(ctx, *, feedback_text: str):
    """Submit feedback about the model's response."""
    logger.info(f'feedback({ctx})')
    store_correction("Feedback", feedback_text)
    await ctx.send('Thank you for your feedback. We will use it to improve the model.')
```

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

**Описание**: Отправляет файл из указанного пути в Discord.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды.
- `file_path` (str): Путь к файлу.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет исключений.

**Примеры**:
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

**Описание**: Преобразует текст в речь и воспроизводит его в указанном голосовом канале.

**Параметры**:
- `text` (str): Текст для преобразования в речь.
- `channel` (discord.VoiceChannel): Голосовой канал для воспроизведения речи.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет исключений.

**Примеры**:
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

**Описание**: Обрабатывает входящие сообщения и отвечает на голосовые команды.

**Параметры**:
- `message` (discord.Message): Объект сообщения, содержащий информацию об отправителе и содержимом сообщения.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет исключений.

**Примеры**:
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