# `discord_bot_trainger.py`

## סקירה כללית

קובץ זה מגדיר בוט דיסקורד שנועד לתקשר עם מודל AI, כולל אימון המודל, בדיקתו וטיפול בפקודות קוליות. הבוט יכול להצטרף לערוצי קול, לזהות דיבור ולהגיב בהתאם.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [משתנים](#משתנים)
- [אירועים](#אירועים)
    - [`on_ready`](#on_ready)
    - [`on_message`](#on_message)
- [פקודות](#פקודות)
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
- [פונקציות](#פונקציות)
    - [`store_correction`](#store_correction)
    - [`text_to_speech_and_play`](#text_to_speech_and_play)
- [הרצה](#הרצה)

## משתנים

- `MODE`: מציין את מצב הפעולה של הבוט (`'dev'` לפיתוח).
- `path_to_ffmpeg`: הנתיב לקובץ ההפעלה `ffmpeg`.
- `PREFIX`: קידומת הפקודה לבוט ( `!`).
- `intents`: הרשאות הבוט.
- `bot`: מופע של בוט דיסקורד.
- `model`: מופע של מודל AI.

## אירועים

### `on_ready`

**תיאור**: מופעל כאשר הבוט מוכן.

```python
async def on_ready():
    """Called when the bot is ready."""
    logger.info(f'Logged in as {bot.user}')
```

### `on_message`

**תיאור**: מטפל בהודעות נכנסות ומגיב לפקודות קוליות.

```python
async def on_message(message):
    """Handle incoming messages and respond to voice commands."""
    #logger.info(f'on_message({message})\')
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

## פקודות

### `hi`

**תיאור**: שולח הודעת "HI!".

**Parameters**:
   - `ctx` (commands.Context): הקשר של הפקודה.

```python
@bot.command(name='hi')
async def hi(ctx):
    """Welcome message."""
    logger.info(f'hi({ctx})')
    await ctx.send('HI!')
    return True
```

### `join`

**תיאור**: מחבר את הבוט לערוץ הקולי של השולח.

**Parameters**:
   - `ctx` (commands.Context): הקשר של הפקודה.

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

**תיאור**: מנתק את הבוט מערוץ הקולי.

**Parameters**:
   - `ctx` (commands.Context): הקשר של הפקודה.

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

**תיאור**: מאמן את המודל עם הנתונים המסופקים.

**Parameters**:
   - `ctx` (commands.Context): הקשר של הפקודה.
   - `data` (Optional[str], optional): נתוני האימון. ברירת מחדל: `None`.
   - `data_dir` (Optional[str], optional): ספריית נתוני האימון. ברירת מחדל: `None`.
   - `positive` (bool, optional): האם הנתונים חיוביים. ברירת מחדל: `True`.
    - `attachment` (Optional[discord.Attachment], optional): קובץ מצורף. ברירת מחדל: `None`.

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

**תיאור**: בודק את המודל עם נתוני בדיקה מסופקים.

**Parameters**:
   - `ctx` (commands.Context): הקשר של הפקודה.
   - `test_data` (str): נתוני הבדיקה בפורמט JSON.

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

**תיאור**: מארכב קבצים בספרייה שצוינה.

**Parameters**:
   - `ctx` (commands.Context): הקשר של הפקודה.
   - `directory` (str): הספרייה לארכוב.

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

**תיאור**: בוחר מערך נתונים לאימון המודל.

**Parameters**:
   - `ctx` (commands.Context): הקשר של הפקודה.
   - `path_to_dir_positive` (str): הנתיב לספריית הנתונים החיוביים.
   - `positive` (bool, optional): האם הנתונים חיוביים. ברירת מחדל: `True`.

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

**תיאור**: מציג הודעת הדרכה מקובץ חיצוני.

**Parameters**:
   - `ctx` (commands.Context): הקשר של הפקודה.

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

**תיאור**: מתקן תגובה קודמת על ידי ציון מזהה ההודעה והתיקון.

**Parameters**:
   - `ctx` (commands.Context): הקשר של הפקודה.
   - `message_id` (int): מזהה ההודעה לתיקון.
   - `correction` (str): התיקון.

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

**תיאור**: שולח משוב על תגובת המודל.

**Parameters**:
   - `ctx` (commands.Context): הקשר של הפקודה.
   - `feedback_text` (str): טקסט המשוב.

```python
@bot.command(name='feedback')
async def feedback(ctx, *, feedback_text: str):
    """Submit feedback about the model's response."""
    logger.info(f'feedback({ctx})')
    store_correction("Feedback", feedback_text)
    await ctx.send('Thank you for your feedback. We will use it to improve the model.')
```

### `getfile`

**תיאור**: מצרף קובץ מהנתיב שסופק.

**Parameters**:
   - `ctx` (commands.Context): הקשר של הפקודה.
   - `file_path` (str): נתיב הקובץ.

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

## פונקציות

### `store_correction`

**תיאור**: שומר את התיקון לשימוש עתידי.

**Parameters**:
   - `original_text` (str): הטקסט המקורי.
   - `correction` (str): התיקון.

```python
def store_correction(original_text: str, correction: str):
    """Store the correction for future reference or retraining."""
    logger.info('store_correction()')
    correction_file = Path("corrections_log.txt")
    with correction_file.open("a") as file:
        file.write(f"Original: {original_text}\\nCorrection: {correction}\\n\\n")
```

### `text_to_speech_and_play`

**תיאור**: ממיר טקסט לדיבור ומשמיע אותו בערוץ קולי.

**Parameters**:
   - `text` (str): הטקסט להמרה.
   - `channel` (discord.VoiceChannel): ערוץ הקול להשמעה.

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

## הרצה

הרצת הבוט נעשית על ידי הפעלת הפונקציה `bot.run` עם אסימון הבוט מדיסקורד.

```python
if __name__ == "__main__":
    bot.run(gs.credentials.discord.bot_token)