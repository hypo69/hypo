# Модуль discord_bot_trainger

## Обзор

Модуль `discord_bot_trainger.py` предназначен для создания Discord-бота, который может выполнять различные задачи, такие как приветствие пользователей, присоединение и выход из голосовых каналов, обучение модели машинного обучения, тестирование модели, архивирование файлов, выбор набора данных, отображение инструкций, исправление предыдущих ответов, получение обратной связи и отправка файлов.

## Подробней

Этот модуль содержит реализацию Discord-бота, использующего библиотеку `discord.py`. Он включает в себя обработку команд, взаимодействие с голосовыми каналами, обучение и тестирование моделей машинного обучения, а также другие полезные функции. Бот использует токен для подключения к Discord и может быть расширен для выполнения дополнительных задач.

## Классы

В данном модуле классы отсутствуют.

## Функции

### `on_ready`

```python
@bot.event
async def on_ready():
    """Called when the bot is ready."""
    logger.info(f'Logged in as {bot.user}')
```

**Назначение**: Вызывается, когда бот готов к работе.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:
1. Регистрирует информацию о том, что бот успешно вошел в систему, используя модуль `logger`.

**Примеры**:
```python
# Автоматически вызывается библиотекой discord.py при готовности бота
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

**Назначение**: Отправляет приветственное сообщение в текстовый канал.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды, предоставляющий информацию о том, откуда была вызвана команда.

**Возвращает**:
- `bool`: `True` после успешной отправки сообщения.

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:
1. Регистрирует вызов команды `hi` с использованием модуля `logger`.
2. Отправляет сообщение "HI!" в канал, из которого была вызвана команда.

**Примеры**:
```python
# Вызов команды в Discord: !hi
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

**Назначение**: Подключает бота к голосовому каналу, в котором находится автор сообщения.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды, предоставляющий информацию о том, откуда была вызвана команда.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:
1. Регистрирует вызов команды `join` с использованием модуля `logger`.
2. Проверяет, находится ли автор сообщения в голосовом канале.
3. Если автор находится в голосовом канале, бот подключается к этому каналу и отправляет сообщение об успешном подключении.
4. Если автор не находится в голосовом канале, бот отправляет сообщение об ошибке.

**Примеры**:
```python
# Вызов команды в Discord: !join
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

**Назначение**: Отключает бота от голосового канала.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды, предоставляющий информацию о том, откуда была вызвана команда.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:
1. Регистрирует вызов команды `leave` с использованием модуля `logger`.
2. Проверяет, подключен ли бот к голосовому каналу.
3. Если бот подключен к голосовому каналу, он отключается и отправляет сообщение об успешном отключении.
4. Если бот не подключен к голосовому каналу, он отправляет сообщение об ошибке.

**Примеры**:
```python
# Вызов команды в Discord: !leave
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

**Назначение**: Запускает обучение модели с использованием предоставленных данных.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды, предоставляющий информацию о том, откуда была вызвана команда.
- `data` (str, optional): Путь к файлу с данными для обучения. По умолчанию `None`.
- `data_dir` (str, optional): Путь к каталогу с данными для обучения. По умолчанию `None`.
- `positive` (bool, optional): Указывает, являются ли данные положительными примерами. По умолчанию `True`.
- `attachment` (discord.Attachment, optional): Прикрепленный файл с данными для обучения. По умолчанию `None`.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:
1. Регистрирует вызов команды `train` с использованием модуля `logger`.
2. Если предоставлен прикрепленный файл, он сохраняется во временном каталоге, и путь к нему используется в качестве данных для обучения.
3. Вызывает метод `train` объекта `model` для запуска обучения модели.
4. Если обучение успешно запущено, бот отправляет сообщение с идентификатором задания.
5. Если запуск обучения не удался, бот отправляет сообщение об ошибке.

**Примеры**:
```python
# Вызов команды в Discord: !train data="path/to/data.txt" data_dir="path/to/data_dir" positive=True
# Вызов команды с прикрепленным файлом: !train attachment=file.txt
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

**Назначение**: Тестирует модель с использованием предоставленных тестовых данных.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды, предоставляющий информацию о том, откуда была вызвана команда.
- `test_data` (str): Тестовые данные в формате JSON.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:
1. Регистрирует вызов команды `test` с использованием модуля `logger`.
2. Пытается загрузить тестовые данные из JSON-строки.
3. Вызывает метод `predict` объекта `model` для получения предсказаний модели.
4. Если предсказания получены, бот отправляет сообщение с результатами тестирования и обрабатывает ошибки.
5. Если предсказания не получены, бот отправляет сообщение об ошибке.
6. Если тестовые данные имеют неверный формат JSON, бот отправляет сообщение об ошибке.

**Примеры**:
```python
# Вызов команды в Discord: !test test_data='{"data": [1, 2, 3]}'
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

**Назначение**: Архивация файлов в указанной директории.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды, предоставляющий информацию о том, откуда была вызвана команда.
- `directory` (str): Путь к директории, файлы которой необходимо архивировать.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:
1. Регистрирует вызов команды `archive` с использованием модуля `logger`.
2. Вызывает метод `archive_files` объекта `model` для архивации файлов в указанной директории.
3. Если архивация прошла успешно, бот отправляет сообщение об успехе.
4. Если в процессе архивации произошла ошибка, бот отправляет сообщение об ошибке.

**Примеры**:
```python
# Вызов команды в Discord: !archive directory="path/to/directory"
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

**Назначение**: Выбор набора данных для обучения модели.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды, предоставляющий информацию о том, откуда была вызвана команда.
- `path_to_dir_positive` (str): Путь к директории с положительными примерами данных.
- `positive` (bool, optional): Указывает, являются ли данные положительными примерами. По умолчанию `True`.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:
1. Регистрирует вызов команды `select_dataset` с использованием модуля `logger`.
2. Вызывает метод `select_dataset_and_archive` объекта `model` для выбора и архивации набора данных.
3. Если выбор набора данных прошел успешно, бот отправляет сообщение об успехе.
4. Если выбор набора данных не удался, бот отправляет сообщение об ошибке.

**Примеры**:
```python
# Вызов команды в Discord: !select_dataset path_to_dir_positive="path/to/directory" positive=True
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

**Назначение**: Отображает сообщение с инструкциями из внешнего файла.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды, предоставляющий информацию о том, откуда была вызвана команда.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:
1. Регистрирует вызов команды `instruction` с использованием модуля `logger`.
2. Пытается прочитать содержимое файла инструкций.
3. Если файл существует, бот отправляет содержимое файла в канал.
4. Если файл не найден, бот отправляет сообщение об ошибке.
5. Если в процессе чтения файла произошла ошибка, бот отправляет сообщение об ошибке.

**Примеры**:
```python
# Вызов команды в Discord: !instruction
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

**Назначение**: Исправляет предыдущий ответ бота, основываясь на идентификаторе сообщения и предоставленном исправлении.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды, предоставляющий информацию о том, откуда была вызвана команда.
- `message_id` (int): Идентификатор сообщения, которое нужно исправить.
- `correction` (str): Текст исправления.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:
1. Регистрирует вызов команды `correct` с использованием модуля `logger`.
2. Пытается получить сообщение по указанному идентификатору.
3. Если сообщение найдено, бот регистрирует информацию об исправлении и сохраняет исправление.
4. Бот отправляет сообщение об успешном получении исправления.
5. Если сообщение не найдено, бот отправляет сообщение об ошибке.
6. Если в процессе выполнения произошла ошибка, бот отправляет сообщение об ошибке.

**Примеры**:
```python
# Вызов команды в Discord: !correct message_id=1234567890 correction="This is the correct message."
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

**Назначение**: Сохраняет исправление для дальнейшего использования или переобучения модели.

**Параметры**:
- `original_text` (str): Исходный текст сообщения.
- `correction` (str): Текст исправления.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:
1. Регистрирует вызов функции `store_correction` с использованием модуля `logger`.
2. Открывает файл "corrections_log.txt" в режиме добавления.
3. Записывает в файл исходный текст и исправление.

**Примеры**:
```python
# Вызов функции: store_correction("Original message", "Corrected message")
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

**Назначение**: Отправляет обратную связь о ответе модели.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды, предоставляющий информацию о том, откуда была вызвана команда.
- `feedback_text` (str): Текст обратной связи.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:
1. Регистрирует вызов команды `feedback` с использованием модуля `logger`.
2. Сохраняет текст обратной связи с помощью функции `store_correction`.
3. Отправляет сообщение благодарности за обратную связь.

**Примеры**:
```python
# Вызов команды в Discord: !feedback This response was not helpful.
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

**Назначение**: Прикрепляет файл из указанного пути к сообщению.

**Параметры**:
- `ctx` (discord.ext.commands.Context): Контекст команды, предоставляющий информацию о том, откуда была вызвана команда.
- `file_path` (str): Путь к файлу, который нужно прикрепить.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:
1. Регистрирует вызов команды `getfile` с использованием модуля `logger`.
2. Проверяет, существует ли файл по указанному пути.
3. Если файл существует, бот отправляет сообщение с прикрепленным файлом.
4. Если файл не найден, бот отправляет сообщение об ошибке.

**Примеры**:
```python
# Вызов команды в Discord: !getfile file_path="path/to/file.txt"
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

**Назначение**: Преобразует текст в речь и воспроизводит его в голосовом канале.

**Параметры**:
- `text` (str): Текст для преобразования в речь.
- `channel` (discord.VoiceChannel): Голосовой канал для воспроизведения речи.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:
1. Преобразует текст в речь с помощью библиотеки `gTTS`.
2. Сохраняет аудиофайл во временном каталоге.
3. Подключается к голосовому каналу, если бот еще не подключен.
4. Воспроизводит аудиофайл в голосовом канале.
5. Отключается от голосового канала после завершения воспроизведения.

**Примеры**:
```python
# Вызов функции: await text_to_speech_and_play("Hello, world!", channel)
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

**Назначение**: Обрабатывает входящие сообщения и отвечает на голосовые команды.

**Параметры**:
- `message` (discord.Message): Объект сообщения, содержащий информацию о сообщении.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:
1. Игнорирует сообщения от самого бота.
2. Если сообщение начинается с префикса команды, обрабатывает команду.
3. Если в сообщении есть вложения, проверяет, является ли вложение аудиофайлом.
4. Если вложение является аудиофайлом, преобразует аудио в текст и отправляет текст модели для получения ответа.
5. Если в сообщении нет вложений, отправляет содержимое сообщения модели для получения ответа.
6. Если автор сообщения находится в голосовом канале, воспроизводит ответ модели в голосовом канале.
7. Если автор сообщения не находится в голосовом канале, отправляет ответ модели в текстовый канал.

**Примеры**:
```python
# Автоматически вызывается библиотекой discord.py при получении нового сообщения
```

### Вспомогательная функция `recognizer`
В данном коде функция `recognizer` закомментирована и не используется.

## Как работает модуль

1. **Инициализация**:
   - Создается объект бота с определенным префиксом команды и разрешениями.
   - Создается объект модели для взаимодействия с моделью машинного обучения.
2. **Обработка событий**:
   - Функция `on_ready` вызывается, когда бот готов к работе.
   - Функция `on_message` вызывается при получении нового сообщения.
3. **Обработка команд**:
   - Команды обрабатываются с использованием декораторов `@bot.command`.
   - Каждая команда выполняет определенную задачу, такую как приветствие, подключение к голосовому каналу, обучение модели и т.д.
4. **Запуск бота**:
   - Бот запускается с использованием токена, хранящегося в файле конфигурации.

## Примеры

### Запуск бота

```python
if __name__ == "__main__":
    bot.run(gs.credentials.discord.bot_token)
```

## ASCII flowchart функции `on_message`

```
Начало
  │
  │
  ▼
Проверка: Автор - бот?
  │
  ├── Да: Конец
  │
  └── Нет
      │
      ▼
Проверка: Сообщение начинается с префикса?
  │
  ├── Да: Обработка команды -> Конец
  │
  └── Нет
      │
      ▼
Проверка: Есть вложения?
  │
  ├── Да
  │   │
  │   ▼
  │   Проверка: Аудио вложение?
  │   │
  │   ├── Да: Преобразование аудио в текст -> Отправка текста модели
  │   │   │
  │   └── Нет: Отправка сообщения об ошибке
  │   │
  └── Нет: Отправка текста сообщения модели
      │
      ▼
Получение ответа от модели
  │
  ▼
Проверка: Автор в голосовом канале?
  │
  ├── Да: Воспроизведение ответа в голосовом канале
  │
  └── Нет: Отправка ответа в текстовый канал
  │
  ▼
Конец