## Анализ кода модуля `discord_bot_trainger.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разбит на логические блоки.
    - Присутствует обработка исключений.
    - Используются логи, что упрощает отладку.
    - Код использует асинхронность, что важно для Discord ботов.
    - Присутствуют docstring для функций и методов, но их нужно доработать в соответствии с RST.
-  Минусы
    - Некоторые docstring не соответствуют формату RST.
    - Используется `json.JSONDecodeError` вместо `j_loads_ns` или `j_loads`.
    - Обработка ошибок может быть более единообразной, лучше использовать `logger.error` вместо `try-except`.
    - В коде присутствуют неиспользуемые закомментированные блоки.

**Рекомендации по улучшению**

1. **Документация:**
   - Необходимо переписать все docstring в формате reStructuredText (RST).
   - Добавить более подробные описания для каждой функции и метода.
2.  **Импорты:**
    - В коде уже присутсвуют все необходимые импорты.
3.  **Обработка данных:**
    - Заменить `json.JSONDecodeError` на `j_loads_ns` или `j_loads` из `src.utils.jjson`.
4.  **Логирование:**
    - Использовать `logger.error` для обработки исключений вместо стандартных `try-except` блоков там где это уместно.
5.  **Рефакторинг:**
    - Убрать неиспользуемый закомментированный код.
6.  **Общая структура**:
    - Добавить описание модуля в начале файла.

**Оптимизированный код**
```python
"""
Модуль для управления Discord ботом и его обучением.
====================================================

Этот модуль содержит функциональность для управления Discord ботом, включая
подключение к голосовым каналам, обучение моделей, тестирование, архивирование данных,
а также обработку текстовых и голосовых сообщений.

Пример использования
--------------------

.. code-block:: python

   from src.endpoints.bots.discord.discord_bot_trainger import bot
   bot.run(token)
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
import header
from src import gs
from src.ai.openai.model.training import Model
from src.utils.jjson import j_loads_ns, j_loads
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
    Вызывается при готовности бота.

    Логирует информацию о том, что бот успешно вошел в систему.
    """
    logger.info(f'Logged in as {bot.user}')

@bot.command(name='hi')
async def hi(ctx):
    """
    Отправляет приветственное сообщение.

    :param ctx: Контекст команды.
    :type ctx: discord.ext.commands.Context
    """
    logger.info(f'hi({ctx})')
    await ctx.send('HI!')
    return True

@bot.command(name='join')
async def join(ctx):
    """
    Подключает бота к голосовому каналу пользователя.

    :param ctx: Контекст команды.
    :type ctx: discord.ext.commands.Context
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

    :param ctx: Контекст команды.
    :type ctx: discord.ext.commands.Context
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
    :type ctx: discord.ext.commands.Context
    :param data: Путь к файлу с данными или сами данные.
    :type data: str, optional
    :param data_dir: Путь к директории с данными.
    :type data_dir: str, optional
    :param positive: Флаг положительных данных.
    :type positive: bool, optional
    :param attachment: Прикрепленный файл.
    :type attachment: discord.Attachment, optional
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

    :param ctx: Контекст команды.
    :type ctx: discord.ext.commands.Context
    :param test_data: Тестовые данные в формате JSON.
    :type test_data: str
    """
    logger.info(f'test({ctx})')
    try:
        # Код загружает тестовые данные из JSON
        test_data = j_loads(test_data)
        predictions = model.predict(test_data)
        if predictions:
            await ctx.send(f'Test complete. Predictions: {predictions}')
            model.handle_errors(predictions, test_data)
        else:
            await ctx.send('Failed to get predictions.')
    except Exception as ex: # Обработка ошибок декодирования JSON
        logger.error(f'Invalid test data format: {ex}')
        await ctx.send('Invalid test data format. Please provide a valid JSON string.')

@bot.command(name='archive')
async def archive(ctx, directory: str):
    """
    Архивирует файлы в указанной директории.

    :param ctx: Контекст команды.
    :type ctx: discord.ext.commands.Context
    :param directory: Путь к директории для архивации.
    :type directory: str
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

    :param ctx: Контекст команды.
    :type ctx: discord.ext.commands.Context
    :param path_to_dir_positive: Путь к директории с данными.
    :type path_to_dir_positive: str
    :param positive: Флаг положительных данных.
    :type positive: bool, optional
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
    Отображает инструкцию из внешнего файла.

    :param ctx: Контекст команды.
    :type ctx: discord.ext.commands.Context
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
    Корректирует предыдущий ответ, используя ID сообщения и исправление.

    :param ctx: Контекст команды.
    :type ctx: discord.ext.commands.Context
    :param message_id: ID сообщения для корректировки.
    :type message_id: int
    :param correction: Текст исправления.
    :type correction: str
    """
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
        logger.error(f'An error occurred: {ex}')
        await ctx.send(f'An error occurred: {ex}')

def store_correction(original_text: str, correction: str):
    """
    Сохраняет исправление для дальнейшего использования.

    :param original_text: Исходный текст.
    :type original_text: str
    :param correction: Текст исправления.
    :type correction: str
    """
    logger.info('store_correction()')
    correction_file = Path("corrections_log.txt")
    with correction_file.open("a") as file:
        file.write(f"Original: {original_text}\nCorrection: {correction}\n\n")

@bot.command(name='feedback')
async def feedback(ctx, *, feedback_text: str):
    """
    Сохраняет обратную связь о ответе модели.

    :param ctx: Контекст команды.
    :type ctx: discord.ext.commands.Context
    :param feedback_text: Текст обратной связи.
    :type feedback_text: str
    """
    logger.info(f'feedback({ctx})')
    store_correction("Feedback", feedback_text)
    await ctx.send('Thank you for your feedback. We will use it to improve the model.')

@bot.command(name='getfile')
async def getfile(ctx, file_path: str):
    """
    Отправляет запрошенный файл.

    :param ctx: Контекст команды.
    :type ctx: discord.ext.commands.Context
    :param file_path: Путь к файлу.
    :type file_path: str
    """
    logger.info(f'getfile({ctx})')
    file_to_attach = Path(file_path)
    if file_to_attach.exists():
        await ctx.send("Here is the file you requested:", file=discord.File(file_to_attach))
    else:
        await ctx.send(f'File not found: {file_path}')


async def text_to_speech_and_play(text, channel):
    """
    Преобразует текст в речь и воспроизводит в голосовом канале.

    :param text: Текст для воспроизведения.
    :type text: str
    :param channel: Голосовой канал.
    :type channel: discord.VoiceChannel
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
    Обрабатывает входящие сообщения и отвечает на голосовые команды.

    :param message: Объект сообщения.
    :type message: discord.Message
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
            # TODO: fix recognizer
            # recognized_text = recognizer(message.attachments[0].url)
            # #await message.channel.send(recognized_text)
            # response = model.send_message(recognized_text)
            response = 'Распознавание речи временно не работает'

    else:
        response = model.send_message(message.content)
    if message.author.voice:
        # Если пользователь находится в голосовом канале, подключаемся и воспроизводим ответ
        await text_to_speech_and_play(response, message.author.voice.channel)
    else:
        await message.channel.send(response)  # Отправляем ответ в текстовый канал

if __name__ == "__main__":
    bot.run(gs.credentials.discord.bot_token)