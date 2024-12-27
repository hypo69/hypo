# Анализ кода модуля `discord_bot_trainger.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на отдельные функции, что облегчает его понимание и поддержку.
    - Присутствует логирование действий с использованием библиотеки `logger`.
    - Используются асинхронные функции для работы с Discord API, что позволяет боту быть более отзывчивым.
    - Код обрабатывает различные типы входящих сообщений, включая текстовые команды, вложения и голосовые сообщения.
    - Присутствует обработка ошибок в различных блоках кода.
    - Код содержит базовый функционал для работы с Discord ботом, включая подключение к голосовым каналам, тренировку модели, тестирование, архивирование файлов, и коррекцию ответов.
-  Минусы
    -  Не все функции и методы имеют docstring.
    -  Импорт `from src.utils.jjson import j_loads_ns, j_loads_ns, j_dumps` содержит дублирование `j_loads_ns`.
    -  Не используется `j_loads` для загрузки json в функциях `test`, а применяется `json.JSONDecodeError`.
    -  Некоторые try-except блоки можно упростить, используя логирование ошибок через `logger.error`.
    -  Функция `recognizer` закомментирована, что может быть признаком незаконченной разработки или проблем с реализацией.
    -   Использование глобальных переменных `MODE`, `PREFIX`, `bot`, `model` не рекомендуется.
    -   В коде есть магические строки, такие как `"/tmp/{attachment.filename}"`, которые могут быть вынесены в константы.

**Рекомендации по улучшению**

1. **Документирование**:
   - Добавить docstring ко всем функциям, методам и классам, используя reStructuredText (RST) формат.
2. **Импорты**:
   - Исправить дублирование `j_loads_ns` в импорте, оставив только один.
3. **Обработка JSON**:
   - Заменить стандартный `json.loads` на `j_loads` для загрузки JSON в функции `test`.
4. **Логирование ошибок**:
   - Упростить блоки try-except, используя `logger.error` для записи ошибок и избегая избыточных блоков try-except.
5. **Глобальные переменные**:
   - Избегать использования глобальных переменных, таких как `MODE`, `PREFIX`, `bot`, `model`, передавая их как параметры или использовать классы.
6.  **Константы**:
    - Вынести магические строки в константы.
7.  **Функция `recognizer`**:
    - Раскомментировать и доработать функцию `recognizer`, или удалить её, если она не требуется.
8.  **Унификация именования**:
    - Привести имена функций и переменных к единому стилю (например, snake_case).

**Оптимизированный код**
```python
"""
Модуль для реализации Discord-бота с функциями обучения и взаимодействия с моделью.
================================================================================

Этот модуль содержит класс :class:`discord.ext.commands.Bot`, который используется для
взаимодействия с Discord API, и методы для обучения модели, обработки сообщений,
голосового взаимодействия, а также других функций.

Пример использования
--------------------

Пример запуска бота:

.. code-block:: python

    bot = commands.Bot(command_prefix='!', intents=intents)
    bot.run(bot_token)
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

import discord
from discord.ext import commands
from pathlib import Path
import tempfile
import asyncio
import requests
import speech_recognition as sr  # Библиотека для распознавания речи
from pydub import AudioSegment  # Библиотека для конвертации аудио
from gtts import gTTS  # Библиотека для текстового воспроизведения

from src import gs
from src.ai.openai.model.training import Model
from src.utils.jjson import j_loads, j_dumps
from src.logger.logger import logger

from .chatterbox import *

# Путь к ffmpeg
PATH_TO_FFMPEG = str(fr"{gs.path.bin}\\ffmpeg\\bin\\ffmpeg.exe")
AudioSegment.converter = PATH_TO_FFMPEG

# Префикс для команд бота
PREFIX = '!'
TEMP_FILE_DIR = "/tmp/"

# Создаем объект бота
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Создаем объект модели
model = Model()


@bot.event
async def on_ready():
    """
    Событие, вызываемое при успешном запуске бота.
    
    Выводит в лог информацию о том, что бот успешно запущен и готов к работе.
    """
    logger.info(f'Logged in as {bot.user}')


@bot.command(name='hi')
async def hi(ctx):
    """
    Команда для приветствия пользователя.
    
    :param ctx: Контекст команды, содержит информацию о том, откуда была вызвана команда.
    :type ctx: discord.ext.commands.Context
    :return: Возвращает True после отправки приветственного сообщения.
    :rtype: bool
    """
    logger.info(f'hi({ctx})')
    await ctx.send('HI!')
    return True


@bot.command(name='join')
async def join(ctx):
    """
    Команда для подключения бота к голосовому каналу пользователя.
    
    :param ctx: Контекст команды, содержит информацию о том, откуда была вызвана команда.
    :type ctx: discord.ext.commands.Context
    
    Если пользователь находится в голосовом канале, бот подключается к нему.
    В противном случае, отправляется сообщение о том, что пользователь не в голосовом канале.
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
    Команда для отключения бота от голосового канала.
    
    :param ctx: Контекст команды, содержит информацию о том, откуда была вызвана команда.
    :type ctx: discord.ext.commands.Context
    
    Если бот подключен к голосовому каналу, он отключается.
    В противном случае, отправляется сообщение о том, что бот не в голосовом канале.
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
    Команда для обучения модели с предоставленными данными.
    
    :param ctx: Контекст команды, содержит информацию о том, откуда была вызвана команда.
    :type ctx: discord.ext.commands.Context
    :param data: Путь к файлу или данные для обучения.
    :type data: str, optional
    :param data_dir: Путь к директории с данными для обучения.
    :type data_dir: str, optional
    :param positive: Флаг для обучения с позитивными или негативными данными.
    :type positive: bool, optional
    :param attachment: Файл, прикрепленный к сообщению.
    :type attachment: discord.Attachment, optional
    
    Если в сообщении есть вложение, бот сохраняет его во временную директорию и использует для обучения.
    Запускает обучение модели и отправляет ID задачи.
    """
    logger.info(f'train({ctx})')
    if attachment:
        file_path = f"{TEMP_FILE_DIR}{attachment.filename}"
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
    Команда для тестирования модели с предоставленными данными.
    
    :param ctx: Контекст команды, содержит информацию о том, откуда была вызвана команда.
    :type ctx: discord.ext.commands.Context
    :param test_data: Тестовые данные в формате JSON.
    :type test_data: str
    
    Преобразует JSON-строку в объект Python, выполняет тестирование модели, и отправляет результат.
    Если формат JSON не верный, отправляет сообщение об ошибке.
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
         logger.error(f'Invalid test data format. Please provide a valid JSON string. {ex}')
         await ctx.send('Invalid test data format. Please provide a valid JSON string.')


@bot.command(name='archive')
async def archive(ctx, directory: str):
    """
    Команда для архивирования файлов в указанной директории.
    
    :param ctx: Контекст команды, содержит информацию о том, откуда была вызвана команда.
    :type ctx: discord.ext.commands.Context
    :param directory: Путь к директории для архивирования.
    :type directory: str
    
    Выполняет архивирование файлов и отправляет сообщение о результате.
    В случае ошибки, отправляет сообщение об ошибке.
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
    Команда для выбора набора данных для обучения модели.
    
    :param ctx: Контекст команды, содержит информацию о том, откуда была вызвана команда.
    :type ctx: discord.ext.commands.Context
    :param path_to_dir_positive: Путь к директории с положительными данными для обучения.
    :type path_to_dir_positive: str
    :param positive: Флаг для выбора положительного набора данных.
    :type positive: bool, optional
    
    Выполняет выбор набора данных и отправляет сообщение о результате.
    В случае ошибки, отправляет сообщение об ошибке.
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
    Команда для вывода инструкции из внешнего файла.
    
    :param ctx: Контекст команды, содержит информацию о том, откуда была вызвана команда.
    :type ctx: discord.ext.commands.Context
    
    Загружает текст инструкции из файла и отправляет его пользователю.
    Если файл не найден, отправляет сообщение об ошибке.
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
    Команда для исправления предыдущего ответа бота.
    
    :param ctx: Контекст команды, содержит информацию о том, откуда была вызвана команда.
    :type ctx: discord.ext.commands.Context
    :param message_id: ID сообщения, которое нужно исправить.
    :type message_id: int
    :param correction: Исправленный текст.
    :type correction: str
    
    Находит сообщение по ID, логирует исправление и отправляет подтверждение.
    Если сообщение не найдено, отправляет сообщение об ошибке.
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
    Функция для сохранения исправлений в файл.
    
    :param original_text: Оригинальный текст сообщения.
    :type original_text: str
    :param correction: Исправленный текст.
    :type correction: str
    
    Сохраняет оригинальный и исправленный текст в файл для дальнейшего использования.
    """
    logger.info('store_correction()')
    correction_file = Path("corrections_log.txt")
    with correction_file.open("a") as file:
        file.write(f"Original: {original_text}\nCorrection: {correction}\n\n")


@bot.command(name='feedback')
async def feedback(ctx, *, feedback_text: str):
    """
    Команда для получения обратной связи от пользователя.
    
    :param ctx: Контекст команды, содержит информацию о том, откуда была вызвана команда.
    :type ctx: discord.ext.commands.Context
    :param feedback_text: Текст обратной связи.
    :type feedback_text: str
    
    Сохраняет текст обратной связи и отправляет подтверждение пользователю.
    """
    logger.info(f'feedback({ctx})')
    store_correction("Feedback", feedback_text)
    await ctx.send('Thank you for your feedback. We will use it to improve the model.')


@bot.command(name='getfile')
async def getfile(ctx, file_path: str):
    """
    Команда для отправки файла пользователю.
    
    :param ctx: Контекст команды, содержит информацию о том, откуда была вызвана команда.
    :type ctx: discord.ext.commands.Context
    :param file_path: Путь к файлу, который нужно отправить.
    :type file_path: str
    
    Если файл существует, бот отправляет его пользователю.
    В противном случае, отправляется сообщение об ошибке.
    """
    logger.info(f'getfile({ctx})')
    file_to_attach = Path(file_path)
    if file_to_attach.exists():
        await ctx.send("Here is the file you requested:", file=discord.File(file_to_attach))
    else:
        await ctx.send(f'File not found: {file_path}')


# def recognizer(audio_url: str, language: str = 'ru-RU') -> str:
#     """
#     Скачивает аудиофайл и распознает речь в нем.
    
#     :param audio_url: URL аудиофайла.
#     :type audio_url: str
#     :param language: Язык для распознавания речи.
#     :type language: str, optional
#     :return: Распознанный текст или сообщение об ошибке.
#     :rtype: str
#     """
#     # Скачивание аудио файла
#     response = requests.get(audio_url)
#     audio_file_path = Path(tempfile.gettempdir()) / "recognized_audio.ogg"

#     with open(audio_file_path, 'wb') as f:
#         f.write(response.content)

#     # Конвертация OGG в WAV
#     wav_file_path = audio_file_path.with_suffix('.wav')
#     audio = AudioSegment.from_ogg(audio_file_path)
#     audio.export(wav_file_path, format='wav')

#     # Инициализация распознавателя
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(str(wav_file_path)) as source:
#         audio_data = recognizer.record(source)
#         try:
#             # Распознавание речи с помощью Google Speech Recognition
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
    Конвертирует текст в речь и воспроизводит его в голосовом канале.
    
    :param text: Текст для воспроизведения.
    :type text: str
    :param channel: Голосовой канал для воспроизведения.
    :type channel: discord.VoiceChannel
    
    Использует Google Text-to-Speech для преобразования текста в аудио, подключается к голосовому каналу и воспроизводит аудио.
    После воспроизведения, отключается от голосового канала.
    """
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


@bot.event
async def on_message(message):
    """
    Обрабатывает входящие сообщения и реагирует на голосовые команды.
    
    :param message: Объект сообщения.
    :type message: discord.Message
    
    Если сообщение отправлено ботом, игнорируется.
    Если сообщение начинается с префикса, обрабатывается как команда.
    Если есть вложения, обрабатывается как аудио файл и распознается речь.
    В противном случае, отправляет текст в модель и выводит ответ в текстовый или голосовой канал.
    """
    #logger.info(f'on_message({message})')
    if message.author == bot.user:
        return  # Игнорируем сообщения от самого себя

    if message.content.startswith(PREFIX):
        await bot.process_commands(message)
        return  # Обрабатываем команды

    if message.attachments:
        # Проверяем, является ли вложение аудио файлом
        if message.attachments[0].content_type.startswith('audio/'):
            recognized_text = recognizer(message.attachments[0].url)
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