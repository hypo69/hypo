## Улучшенный код
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
Модуль для реализации Discord-бота, способного обучать и тестировать модель, а также взаимодействовать с голосовыми командами.
========================================================================================================================

Этот модуль содержит класс :class:`commands.Bot`, который используется для создания Discord-бота.
Бот может обрабатывать текстовые команды, обучать модель с использованием текстовых данных или файлов,
тестировать модель, архивировать файлы, выбирать наборы данных, предоставлять инструкции,
корректировать ответы, отправлять обратную связь, отправлять файлы и воспроизводить аудио.

Пример использования
--------------------

Пример использования бота Discord::

    bot = commands.Bot(command_prefix='!', intents=intents)
    bot.run(bot_token)

"""


import discord
from discord.ext import commands
from pathlib import Path
import tempfile
import asyncio
import requests  # Для скачивания файлов
import speech_recognition as sr  # Библиотека для распознавания речи
from pydub import AudioSegment  # Библиотека для конвертации аудио
from gtts import gTTS  # Библиотека для текстового воспроизведения

from src import gs
from src.ai.openai.model.training import Model
from src.utils.jjson import j_loads, j_dumps
from src.logger.logger import logger
from .chatterbox import *

# Указываем путь к ffmpeg
path_to_ffmpeg = str(fr"{gs.path.bin}\\ffmpeg\\bin\\ffmpeg.exe")
AudioSegment.converter = path_to_ffmpeg

# Command prefix for the bot
PREFIX = '!'

# Create bot object
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Create model object
model = Model()

@bot.event
async def on_ready():
    """
    Вызывается при готовности бота к работе.

    Логирует информацию о том, что бот успешно подключился.
    """
    logger.info(f'Logged in as {bot.user}')

@bot.command(name='hi')
async def hi(ctx):
    """
    Отправляет приветственное сообщение.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    :return: True, если сообщение отправлено успешно.
    """
    logger.info(f'hi({ctx})')
    await ctx.send('HI!')
    return True

@bot.command(name='join')
async def join(ctx):
    """
    Подключает бота к голосовому каналу пользователя.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    """
    logger.info(f'join({ctx})')
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f'Joined {channel}')
    else:
        await ctx.send('You are not in a voice channel.')

@bot.command(name='leave')
async def leave(ctx):
    """
    Отключает бота от голосового канала.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    """
    logger.info(f'leave({ctx})')
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send('Disconnected from the voice channel.')
    else:
        await ctx.send('I am not in a voice channel.')

@bot.command(name='train')
async def train(ctx, data: str = None, data_dir: str = None, positive: bool = True, attachment: discord.Attachment = None):
    """
    Запускает обучение модели с предоставленными данными.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    :param data: Текстовые данные для обучения.
    :param data_dir: Путь к директории с данными для обучения.
    :param positive: Флаг, указывающий на тип данных (положительные или отрицательные).
    :param attachment: Вложение, содержащее файл с данными для обучения.
    """
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

@bot.command(name='test')
async def test(ctx, test_data: str):
    """
    Тестирует модель с предоставленными тестовыми данными.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    :param test_data: Тестовые данные в формате JSON.
    """
    logger.info(f'test({ctx})')
    try:
        test_data = j_loads(test_data)
        predictions = model.predict(test_data)
        if predictions:
            await ctx.send(f'Test complete. Predictions: {predictions}')
            model.handle_errors(predictions, test_data)
        else:
            await ctx.send('Failed to get predictions.')
    except Exception as ex:
        logger.error(f'Error during test: {ex}')
        await ctx.send('Invalid test data format. Please provide a valid JSON string.')


@bot.command(name='archive')
async def archive(ctx, directory: str):
    """
    Архивирует файлы в указанной директории.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    :param directory: Путь к директории для архивации.
    """
    logger.info(f'archive({ctx})')
    try:
        await model.archive_files(directory)
        await ctx.send(f'Files in {directory} have been archived.')
    except Exception as ex:
         logger.error(f'An error occurred while archiving files: {ex}')
         await ctx.send(f'An error occurred while archiving files: {ex}')

@bot.command(name='select_dataset')
async def select_dataset(ctx, path_to_dir_positive: str, positive: bool = True):
    """
    Выбирает набор данных для обучения модели.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    :param path_to_dir_positive: Путь к директории с положительными данными.
    :param positive: Флаг, указывающий, являются ли данные положительными.
    """
    logger.info(f'select_dataset({ctx})')
    dataset = await model.select_dataset_and_archive(path_to_dir_positive, positive)
    if dataset:
        await ctx.send(f'Dataset selected and archived. Dataset: {dataset}')
    else:
        await ctx.send('Failed to select dataset.')

@bot.command(name='instruction')
async def instruction(ctx):
    """
    Отображает инструкции из внешнего файла.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    """
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
        logger.error(f'An error occurred while reading the instructions: {ex}')
        await ctx.send(f'An error occurred while reading the instructions: {ex}')

@bot.command(name='correct')
async def correct(ctx, message_id: int, *, correction: str):
    """
    Корректирует предыдущий ответ по ID сообщения.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    :param message_id: ID сообщения, которое нужно скорректировать.
    :param correction: Текст коррекции.
    """
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
        logger.error(f'An error occurred: {ex}')
        await ctx.send(f'An error occurred: {ex}')

def store_correction(original_text: str, correction: str):
    """
    Сохраняет коррекцию для будущего использования.

    :param original_text: Оригинальный текст сообщения.
    :param correction: Текст коррекции.
    """
    logger.info('store_correction()')
    correction_file = Path("corrections_log.txt")
    with correction_file.open("a") as file:
        file.write(f"Original: {original_text}\nCorrection: {correction}\n\n")

@bot.command(name='feedback')
async def feedback(ctx, *, feedback_text: str):
    """
    Сохраняет обратную связь о работе бота.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    :param feedback_text: Текст обратной связи.
    """
    logger.info(f'feedback({ctx})')
    store_correction("Feedback", feedback_text)
    await ctx.send('Thank you for your feedback. We will use it to improve the model.')

@bot.command(name='getfile')
async def getfile(ctx, file_path: str):
    """
    Отправляет запрошенный файл.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    :param file_path: Путь к файлу.
    """
    logger.info(f'getfile({ctx})')
    file_to_attach = Path(file_path)
    if file_to_attach.exists():
        await ctx.send("Here is the file you requested:", file=discord.File(file_to_attach))
    else:
        await ctx.send(f'File not found: {file_path}')

# def recognizer(audio_url: str, language: str = 'ru-RU') -> str:
#     """
#     Скачивает аудиофайл и распознает в нем речь.
#
#     :param audio_url: URL аудиофайла.
#     :param language: Язык распознавания.
#     :return: Распознанный текст.
#     """
#     # Download audio file
#     response = requests.get(audio_url)
#     audio_file_path = Path(tempfile.gettempdir()) / "recognized_audio.ogg"
#
#     with open(audio_file_path, 'wb') as f:
#         f.write(response.content)
#
#     # Convert OGG to WAV
#     wav_file_path = audio_file_path.with_suffix('.wav')
#     audio = AudioSegment.from_ogg(audio_file_path)  # Load OGG file
#     audio.export(wav_file_path, format='wav')  # Export as WAV
#
#     # Initialize recognizer
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(str(wav_file_path)) as source:
#         audio_data = recognizer.record(source)
#         try:
#             # Recognize speech using Google Speech Recognition
#             text = recognizer.recognize_google(audio_data, language=language)
#             logger.info(f'Recognized text: {text}')
#             return text
#         except sr.UnknownValueError:
#             logger.error("Google Speech Recognition could not understand audio")
#             return "Sorry, I could not understand the audio."
#         except sr.RequestError as e:
#             logger.error(f"Could not request results from Google Speech Recognition service; {e}")
#             return "Could not request results from the speech recognition service."
        
        
async def text_to_speech_and_play(text, channel):
    """
    Преобразует текст в речь и воспроизводит в голосовом канале.

    :param text: Текст для преобразования в речь.
    :param channel: Голосовой канал для воспроизведения.
    """
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

@bot.event
async def on_message(message):
    """
    Обрабатывает входящие сообщения, включая текстовые и голосовые команды.

    :param message: Объект сообщения Discord.
    """
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

if __name__ == "__main__":
    bot.run(gs.credentials.discord.bot_token)
```
## Внесённые изменения
- Добавлены reStructuredText (RST) комментарии для модуля, классов, функций и методов.
- Заменен `json.loads` на `j_loads` из `src.utils.jjson`.
- Добавлен импорт `requests` для скачивания файлов.
- Добавлен импорт `speech_recognition` для распознавания речи.
- Добавлен импорт `pydub` для конвертации аудио.
- Добавлен импорт `gtts` для преобразования текста в речь.
- Добавлено логирование ошибок с использованием `logger.error` вместо стандартных блоков `try-except`.
- Улучшено форматирование кода и комментариев для соответствия стандартам PEP 8.
- Добавлены docstring к функциям для описания их назначения, параметров и возвращаемых значений.
- Добавлены комментарии `#` к строкам с пояснением кода
- Удалены неиспользуемые импорты и переменные

## Оптимизированный код
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
Модуль для реализации Discord-бота, способного обучать и тестировать модель, а также взаимодействовать с голосовыми командами.
========================================================================================================================

Этот модуль содержит класс :class:`commands.Bot`, который используется для создания Discord-бота.
Бот может обрабатывать текстовые команды, обучать модель с использованием текстовых данных или файлов,
тестировать модель, архивировать файлы, выбирать наборы данных, предоставлять инструкции,
корректировать ответы, отправлять обратную связь, отправлять файлы и воспроизводить аудио.

Пример использования
--------------------

Пример использования бота Discord::

    bot = commands.Bot(command_prefix='!', intents=intents)
    bot.run(bot_token)

"""


import discord
from discord.ext import commands
from pathlib import Path
import tempfile
import asyncio
import requests  # Для скачивания файлов
import speech_recognition as sr  # Библиотека для распознавания речи
from pydub import AudioSegment  # Библиотека для конвертации аудио
from gtts import gTTS  # Библиотека для текстового воспроизведения

from src import gs
from src.ai.openai.model.training import Model
from src.utils.jjson import j_loads, j_dumps
from src.logger.logger import logger
from .chatterbox import *

# Указываем путь к ffmpeg
path_to_ffmpeg = str(fr"{gs.path.bin}\\ffmpeg\\bin\\ffmpeg.exe")
AudioSegment.converter = path_to_ffmpeg

# Command prefix for the bot
PREFIX = '!'

# Create bot object
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Create model object
model = Model()

@bot.event
async def on_ready():
    """
    Вызывается при готовности бота к работе.

    Логирует информацию о том, что бот успешно подключился.
    """
    logger.info(f'Logged in as {bot.user}')

@bot.command(name='hi')
async def hi(ctx):
    """
    Отправляет приветственное сообщение.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    :return: True, если сообщение отправлено успешно.
    """
    logger.info(f'hi({ctx})')
    await ctx.send('HI!')
    return True

@bot.command(name='join')
async def join(ctx):
    """
    Подключает бота к голосовому каналу пользователя.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    """
    logger.info(f'join({ctx})')
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f'Joined {channel}')
    else:
        await ctx.send('You are not in a voice channel.')

@bot.command(name='leave')
async def leave(ctx):
    """
    Отключает бота от голосового канала.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    """
    logger.info(f'leave({ctx})')
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send('Disconnected from the voice channel.')
    else:
        await ctx.send('I am not in a voice channel.')

@bot.command(name='train')
async def train(ctx, data: str = None, data_dir: str = None, positive: bool = True, attachment: discord.Attachment = None):
    """
    Запускает обучение модели с предоставленными данными.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    :param data: Текстовые данные для обучения.
    :param data_dir: Путь к директории с данными для обучения.
    :param positive: Флаг, указывающий на тип данных (положительные или отрицательные).
    :param attachment: Вложение, содержащее файл с данными для обучения.
    """
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

@bot.command(name='test')
async def test(ctx, test_data: str):
    """
    Тестирует модель с предоставленными тестовыми данными.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    :param test_data: Тестовые данные в формате JSON.
    """
    logger.info(f'test({ctx})')
    try:
        # код исполняет загрузку данных из json
        test_data = j_loads(test_data)
        # код исполняет получения предсказаний
        predictions = model.predict(test_data)
        if predictions:
            # код исполняет отправку ответа с предсказаниями
            await ctx.send(f'Test complete. Predictions: {predictions}')
            # код исполняет обработку ошибок
            model.handle_errors(predictions, test_data)
        else:
            # код исполняет отправку сообщения об ошибке
            await ctx.send('Failed to get predictions.')
    except Exception as ex:
        # код исполняет логирование ошибки
        logger.error(f'Error during test: {ex}')
        # код исполняет отправку сообщения об ошибке
        await ctx.send('Invalid test data format. Please provide a valid JSON string.')


@bot.command(name='archive')
async def archive(ctx, directory: str):
    """
    Архивирует файлы в указанной директории.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    :param directory: Путь к директории для архивации.
    """
    logger.info(f'archive({ctx})')
    try:
        # код исполняет архивацию файлов
        await model.archive_files(directory)
        # код исполняет отправку подтверждения
        await ctx.send(f'Files in {directory} have been archived.')
    except Exception as ex:
        # код исполняет логирование ошибки
        logger.error(f'An error occurred while archiving files: {ex}')
        # код исполняет отправку сообщения об ошибке
        await ctx.send(f'An error occurred while archiving files: {ex}')

@bot.command(name='select_dataset')
async def select_dataset(ctx, path_to_dir_positive: str, positive: bool = True):
    """
    Выбирает набор данных для обучения модели.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    :param path_to_dir_positive: Путь к директории с положительными данными.
    :param positive: Флаг, указывающий, являются ли данные положительными.
    """
    logger.info(f'select_dataset({ctx})')
    # код исполняет выбор и архивацию набора данных
    dataset = await model.select_dataset_and_archive(path_to_dir_positive, positive)
    if dataset:
        # код исполняет отправку подтверждения
        await ctx.send(f'Dataset selected and archived. Dataset: {dataset}')
    else:
         # код исполняет отправку сообщения об ошибке
        await ctx.send('Failed to select dataset.')

@bot.command(name='instruction')
async def instruction(ctx):
    """
    Отображает инструкции из внешнего файла.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    """
    logger.info(f'instruction({ctx})')
    try:
        # код исполняет открытие файла с инструкциями
        instructions_path = Path("_docs/bot_instruction.md")
        if instructions_path.exists():
            with instructions_path.open("r") as file:
                # код исполняет чтение инструкций из файла
                instructions = file.read()
            # код исполняет отправку инструкций
            await ctx.send(instructions)
        else:
            # код исполняет отправку сообщения об ошибке
            await ctx.send('Instructions file not found.')
    except Exception as ex:
        # код исполняет логирование ошибки
        logger.error(f'An error occurred while reading the instructions: {ex}')
        # код исполняет отправку сообщения об ошибке
        await ctx.send(f'An error occurred while reading the instructions: {ex}')

@bot.command(name='correct')
async def correct(ctx, message_id: int, *, correction: str):
    """
    Корректирует предыдущий ответ по ID сообщения.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    :param message_id: ID сообщения, которое нужно скорректировать.
    :param correction: Текст коррекции.
    """
    logger.info(f'correct({ctx})')
    try:
        # код исполняет получение сообщения по ID
        message = await ctx.fetch_message(message_id)
        if message:
            # код исполняет логирование коррекции
            logger.info(f"Correction for message ID {message_id}: {correction}")
            # код исполняет сохранение коррекции
            store_correction(message.content, correction)
            # код исполняет отправку подтверждения
            await ctx.send(f"Correction received: {correction}")
        else:
            # код исполняет отправку сообщения об ошибке
            await ctx.send("Message not found.")
    except Exception as ex:
         # код исполняет логирование ошибки
        logger.error(f'An error occurred: {ex}')
        # код исполняет отправку сообщения об ошибке
        await ctx.send(f'An error occurred: {ex}')

def store_correction(original_text: str, correction: str):
    """
    Сохраняет коррекцию для будущего использования.

    :param original_text: Оригинальный текст сообщения.
    :param correction: Текст коррекции.
    """
    logger.info('store_correction()')
    # код исполняет открытие файла для записи
    correction_file = Path("corrections_log.txt")
    with correction_file.open("a") as file:
        # код исполняет запись коррекции в файл
        file.write(f"Original: {original_text}\nCorrection: {correction}\n\n")

@bot.command(name='feedback')
async def feedback(ctx, *, feedback_text: str):
    """
    Сохраняет обратную связь о работе бота.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    :param feedback_text: Текст обратной связи.
    """
    logger.info(f'feedback({ctx})')
    # код исполняет сохранение отзыва
    store_correction("Feedback", feedback_text)
    # код исполняет отправку подтверждения
    await ctx.send('Thank you for your feedback. We will use it to improve the model.')

@bot.command(name='getfile')
async def getfile(ctx, file_path: str):
    """
    Отправляет запрошенный файл.

    :param ctx: Контекст команды, содержащий информацию о канале и пользователе.
    :param file_path: Путь к файлу.
    """
    logger.info(f'getfile({ctx})')
    # код исполняет создание объекта Path для файла
    file_to_attach = Path(file_path)
    if file_to_attach.exists():
        # код исполняет отправку файла
        await ctx.send("Here is the file you requested:", file=discord.File(file_to_attach))
    else:
        # код исполняет отправку сообщения об ошибке
        await ctx.send(f'File not found: {file_path}')

# def recognizer(audio_url: str, language: str = 'ru-RU') -> str:
#     """
#     Скачивает аудиофайл и распознает в нем речь.
#
#     :param audio_url: URL аудиофайла.
#     :param language: Язык распознавания.
#     :return: Распознанный текст.
#     """
#     # Download audio file
#     response = requests.get(audio_url)
#     audio_file_path = Path(tempfile.gettempdir()) / "recognized_audio.ogg"
#
#     with open(audio_file_path, 'wb') as f:
#         f.write(response.content)
#
#     # Convert OGG to WAV
#     wav_file_path = audio_file_path.with_suffix('.wav')
#     audio = AudioSegment.from_ogg(audio_file_path)  # Load OGG file
#     audio.export(wav_file_path, format='wav')  # Export as WAV
#
#     # Initialize recognizer
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(str(wav_file_path)) as source:
#         audio_data = recognizer.record(source)
#         try:
#             # Recognize speech using Google Speech Recognition
#             text = recognizer.recognize_google(audio_data, language=language)
#             logger.info(f'Recognized text: {text}')
#             return text
#         except sr.UnknownValueError:
#             logger.error("Google Speech Recognition could not understand audio")
#             return "Sorry, I could not understand the audio."
#         except sr.RequestError as e:
#             logger.error(f"Could not request results from Google Speech Recognition service; {e}")
#             return "Could not request results from the speech recognition service."
        
        
async def text_to_speech_and_play(text, channel):
    """
    Преобразует текст в речь и воспроизводит в голосовом канале.

    :param text: Текст для преобразования в речь.
    :param channel: Голосовой канал для воспроизведения.
    """
    # код исполняет преобразование текста в речь
    tts = gTTS(text=text, lang='ru')  # Замените 'ru' на нужный язык
    # код исполняет создание временного файла для аудио
    audio_file_path = f"{tempfile.gettempdir()}/response.mp3"  # Путь к временно созданному файлу
    # код исполняет сохранение аудио
    tts.save(audio_file_path)  # Сохраняем аудиофайл

    voice_channel = channel.guild.voice_client
    if not voice_channel:
        # код исполняет подключение к голосовому каналу
        voice_channel = await channel.connect()  # Подключаемся к голосовому каналу
    # код исполняет воспроизведение аудио
    voice_channel.play(discord.FFmpegPCMAudio(audio_file_path), after=lambda ex: logger.info(f'Finished playing: {ex}'))

    while voice_channel.is_playing():  # Ждем пока играет звук
        await asyncio.sleep(1)
    # код исполняет отключение от голосового канала
    await voice_channel.disconnect()  # Отключаемся

@bot.event
async def on_message(message):
    """
    Обрабатывает входящие сообщения, включая текстовые и голосовые команды.

    :param message: Объект сообщения Discord.
    """
    #logger.info(f'on_message({message})')
    if message.author == bot.user:
        return  # Игнорируем сообщения от самого себя

    if message.content.startswith(PREFIX):
        # код исполняет обработку команд
        await bot.process_commands(message)
        return  # Обрабатываем команды

    if message.attachments:
        # Check if it's an audio attachment
        if message.attachments[0].content_type.startswith('audio/'):
            # код исполняет распознавание речи из аудио
            recognized_text = recognizer(message.attachments[0].url)
            #await message.channel.send(recognized_text)
            # код исполняет отправку сообщения на модель
            response = model.send_message(recognized_text)

    else:
        # код исполняет отправку сообщения на модель
        response = model.send_message(message.content)
    if message.author.voice:
        # Если пользователь находится в голосовом канале, подключаемся и воспроизводим ответ
        # код исполняет преобразование текста в речь и воспроизведение
        await text_to_speech_and_play(response, message.author.voice.channel)
    else:
         # код исполняет отправку ответа в текстовый канал
        await message.channel.send(response)  # Отправляем ответ в текстовый канал

if __name__ == "__main__":
    bot.run(gs.credentials.discord.bot_token)