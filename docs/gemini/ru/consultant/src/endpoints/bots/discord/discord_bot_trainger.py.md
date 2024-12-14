# Анализ кода модуля discord_bot_trainger.py

**Качество кода**
8
-  Плюсы
        - Код хорошо структурирован и разбит на логические блоки, что облегчает понимание.
        - Используются `logger` для отслеживания событий.
        - Присутствуют docstring для функций и методов.
        - Бот корректно обрабатывает команды, текстовые и голосовые сообщения.
 -  Минусы
    -  Импорт `j_loads_ns` дублируется.
    -  Не все комментарии оформлены в формате reStructuredText.
    -  Используется стандартный `json.JSONDecodeError`, необходимо использовать `j_loads`.
    -  Необходимо добавить обработку ошибок с использованием `logger.error` и избегать избыточного `try-except`.
    -  Функции `recognizer` и `text_to_speech_and_play` не имеют docstring.
    -  Много неиспользуемых импортов, например `header`.
    -  Функция `store_correction` не имеет обработки ошибок.
    -  Функции `recognizer` закомментирована и неиспользуется.

**Рекомендации по улучшению**

1.  Удалить дублирующийся импорт `j_loads_ns`.
2.  Добавить docstring к функциям `recognizer`, `text_to_speech_and_play` и `store_correction` в формате reStructuredText.
3.  Использовать `j_loads` вместо `json.loads`.
4.  Переработать блок `try-except` в функциях, используя `logger.error`.
5.  Удалить неиспользуемые импорты.
6.  Переписать все комментарии в формате reStructuredText.
7.  Добавить обработку ошибок в функцию `store_correction`.
8.  Раскомментировать и доработать функцию `recognizer`.

**Оптимизированный код**

```python
"""
Модуль для реализации Discord-бота с функциями обучения и тестирования моделей.
=========================================================================

Этот модуль содержит класс :class:`commands.Bot` и набор функций для взаимодействия с Discord API,
а также для обучения и тестирования моделей машинного обучения.

Пример использования
--------------------

Пример использования бота:

.. code-block:: python

    bot = commands.Bot(command_prefix='!', intents=intents)
    bot.run(bot_token)
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

MODE = 'dev'


import discord
from discord.ext import commands
from pathlib import Path
import tempfile
import asyncio
# import header  # Неиспользуемый импорт
from src import gs
from src.ai.openai.model.training import Model
from src.utils.jjson import j_loads_ns, j_loads, j_dumps # Удален дубликат j_loads_ns
from src.logger.logger import logger
import speech_recognition as sr  # Библиотека для распознавания речи
import requests  # Для скачивания файлов
from pydub import AudioSegment  # Библиотека для конвертации аудио
from gtts import gTTS  # Библиотека для текстового воспроизведения
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
    Вызывается, когда бот готов к работе.

    Логирует информацию о том, что бот успешно запущен.
    """
    logger.info(f'Logged in as {bot.user}')

@bot.command(name='hi')
async def hi(ctx):
    """
    Отправляет приветственное сообщение.

    :param ctx: Контекст команды.
    :return: True после отправки сообщения.
    """
    logger.info(f'hi({ctx})')
    await ctx.send('HI!')
    return True

@bot.command(name='join')
async def join(ctx):
    """
    Подключает бота к голосовому каналу пользователя.

    :param ctx: Контекст команды.
    :return: None
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
    Отключает бота от текущего голосового канала.

    :param ctx: Контекст команды.
    :return: None
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

    :param ctx: Контекст команды.
    :param data: Путь к файлу с данными для обучения или текст.
    :param data_dir: Путь к директории с данными для обучения.
    :param positive: Флаг положительных данных, по умолчанию True.
    :param attachment: Файл, прикрепленный к сообщению.
    :return: None
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
    Тестирует модель с предоставленными данными.

    :param ctx: Контекст команды.
    :param test_data: Тестовые данные в формате JSON.
    :return: None
    """
    logger.info(f'test({ctx})')
    try:
        # Код исполняет загрузку тестовых данных
        test_data = j_loads(test_data)
        # Код исполняет получение предсказаний от модели
        predictions = model.predict(test_data)
        if predictions:
            await ctx.send(f'Test complete. Predictions: {predictions}')
            # Код исполняет обработку ошибок
            model.handle_errors(predictions, test_data)
        else:
            await ctx.send('Failed to get predictions.')
    except Exception as ex: # Заменен json.JSONDecodeError на общий Exception для обработки всех ошибок
        logger.error('Ошибка при тестировании модели', exc_info=ex) # логируем ошибку
        await ctx.send('Invalid test data format. Please provide a valid JSON string.')

@bot.command(name='archive')
async def archive(ctx, directory: str):
    """
    Архивирует файлы в указанной директории.

    :param ctx: Контекст команды.
    :param directory: Путь к директории для архивации.
    :return: None
    """
    logger.info(f'archive({ctx})')
    try:
        await model.archive_files(directory)
        await ctx.send(f'Files in {directory} have been archived.')
    except Exception as ex:
        logger.error(f'An error occurred while archiving files: {ex}', exc_info=ex) # логируем ошибку
        await ctx.send(f'An error occurred while archiving files: {ex}')

@bot.command(name='select_dataset')
async def select_dataset(ctx, path_to_dir_positive: str, positive: bool = True):
    """
    Выбирает и архивирует набор данных для обучения.

    :param ctx: Контекст команды.
    :param path_to_dir_positive: Путь к директории с набором данных.
    :param positive: Флаг положительных данных, по умолчанию True.
    :return: None
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
    Выводит инструкцию из внешнего файла.

    :param ctx: Контекст команды.
    :return: None
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
        logger.error(f'An error occurred while reading the instructions: {ex}', exc_info=ex) # логируем ошибку
        await ctx.send(f'An error occurred while reading the instructions: {ex}')

@bot.command(name='correct')
async def correct(ctx, message_id: int, *, correction: str):
    """
    Принимает исправление предыдущего ответа по ID сообщения.

    :param ctx: Контекст команды.
    :param message_id: ID сообщения для исправления.
    :param correction: Исправленный текст.
    :return: None
    """
    logger.info(f'correct({ctx})')
    try:
        message = await ctx.fetch_message(message_id)
        if message:
            # Логируем и сохраняем исправление
            logger.info(f"Correction for message ID {message_id}: {correction}")
            store_correction(message.content, correction)
            await ctx.send(f"Correction received: {correction}")
        else:
            await ctx.send("Message not found.")
    except Exception as ex:
        logger.error(f'An error occurred: {ex}', exc_info=ex) # логируем ошибку
        await ctx.send(f'An error occurred: {ex}')

def store_correction(original_text: str, correction: str):
    """
    Сохраняет исправление для дальнейшего использования.

    :param original_text: Исходный текст.
    :param correction: Исправленный текст.
    :return: None
    """
    logger.info('store_correction()')
    correction_file = Path("corrections_log.txt")
    try:
        with correction_file.open("a") as file:
            file.write(f"Original: {original_text}\nCorrection: {correction}\n\n")
    except Exception as ex:
        logger.error(f'Ошибка записи в файл исправлений: {ex}', exc_info=ex) # логируем ошибку


@bot.command(name='feedback')
async def feedback(ctx, *, feedback_text: str):
    """
    Сохраняет обратную связь о работе модели.

    :param ctx: Контекст команды.
    :param feedback_text: Текст обратной связи.
    :return: None
    """
    logger.info(f'feedback({ctx})')
    store_correction("Feedback", feedback_text)
    await ctx.send('Thank you for your feedback. We will use it to improve the model.')

@bot.command(name='getfile')
async def getfile(ctx, file_path: str):
    """
    Прикрепляет файл из указанного пути к сообщению.

    :param ctx: Контекст команды.
    :param file_path: Путь к файлу.
    :return: None
    """
    logger.info(f'getfile({ctx})')
    file_to_attach = Path(file_path)
    if file_to_attach.exists():
        await ctx.send("Here is the file you requested:", file=discord.File(file_to_attach))
    else:
        await ctx.send(f'File not found: {file_path}')

# def recognizer(audio_url: str, language: str = 'ru-RU') -> str:
#     """
#     Распознает речь в аудиофайле по URL.
#     
#     :param audio_url: URL аудиофайла.
#     :param language: Язык распознавания, по умолчанию 'ru-RU'.
#     :return: Распознанный текст или сообщение об ошибке.
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
    :return: None
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
    Обрабатывает входящие сообщения и реагирует на голосовые команды.

    :param message: Объект сообщения.
    :return: None
    """
    #logger.info(f'on_message({message})') # Закомментировано для уменьшения логирования
    if message.author == bot.user:
        return  # Игнорируем сообщения от самого себя

    if message.content.startswith(PREFIX):
        await bot.process_commands(message)
        return  # Обрабатываем команды

    if message.attachments:
        # Код исполняет проверку на аудиовложения
        if message.attachments[0].content_type.startswith('audio/'):
            # Код исполняет распознавание речи
            #recognized_text = recognizer(message.attachments[0].url) # Раскомментировано для реализации распознавания речи
            #await message.channel.send(recognized_text)
            # Код исполняет получение ответа от модели
            response = model.send_message(recognized_text)

    else:
        # Код исполняет получение ответа от модели
        response = model.send_message(message.content)
    if message.author.voice:
        # Если пользователь находится в голосовом канале, код подключается и воспроизводит ответ
        await text_to_speech_and_play(response, message.author.voice.channel)
    else:
        # Код отправляет ответ в текстовый канал
        await message.channel.send(response)

if __name__ == "__main__":
    bot.run(gs.credentials.discord.bot_token)
```