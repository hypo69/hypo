## Анализ кода модуля discord_bot_trainger

**Качество кода**
1.  Соответствие требованиям по оформлению кода: 8/10
    *   Плюсы:
        *   Код хорошо структурирован и разбит на логические блоки.
        *   Используются `logger` для логирования, что облегчает отслеживание ошибок.
        *   Присутствует обработка исключений.
        *   Используются f-строки для форматирования строк.
    *   Минусы:
        *   Не везде используется `j_loads_ns` или `j_loads` для работы с JSON.
        *   Комментарии не всегда соответствуют формату RST.
        *   Избыточное использование try-except.
        *   Не все функции имеют docstring.
        *   Не используются `async with` для асинхронной работы с файлами.

**Рекомендации по улучшению**
*   Заменить все `json.load` на `j_loads_ns` или `j_loads` из `src.utils.jjson`.
*   Добавить docstring в формате RST для всех функций и методов.
*   Использовать `from src.logger.logger import logger` для импорта логгера.
*   Убрать избыточные блоки `try-except` и использовать `logger.error` для обработки ошибок.
*   Использовать `async with` для асинхронной работы с файлами.
*   Привести в соответствие имена переменных с ранее обработанными файлами.
*   Добавить описание модуля в начале файла.
*   Изменить формат комментариев с `#` для соответствия `RST`.

**Оптимизированный код**
```python
"""
Модуль для управления Discord ботом и взаимодействия с моделью обучения.
======================================================================

Этот модуль содержит класс, который используется для управления Discord ботом,
тренировки модели, обработки голосовых сообщений и текстового ввода.

Пример использования
--------------------

Пример запуска бота:

.. code-block:: python

    if __name__ == "__main__":
        bot.run(gs.credentials.discord.bot_token)
"""

# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
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
from src.utils.jjson import j_loads_ns, j_dumps, j_loads
from src.logger.logger import logger
from .chatterbox import * # TODO: разобраться зачем используется *
#from header import * #TODO: разобраться что это за модуль.
# Указываем путь к ffmpeg
path_to_ffmpeg = str(fr'{gs.path.bin}\\ffmpeg\\bin\\ffmpeg.exe')
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

    Логирует информацию о том, что бот успешно подключился.
    """
    logger.info(f'Logged in as {bot.user}')


@bot.command(name='hi')
async def hi(ctx):
    """
    Отправляет приветственное сообщение.

    Args:
        ctx (commands.Context): Контекст команды.
    """
    logger.info(f'hi({ctx})')
    await ctx.send('HI!')
    return True


@bot.command(name='join')
async def join(ctx):
    """
    Подключает бота к голосовому каналу пользователя.

    Args:
        ctx (commands.Context): Контекст команды.
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

    Args:
        ctx (commands.Context): Контекст команды.
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

    Args:
        ctx (commands.Context): Контекст команды.
        data (str, optional): Путь к файлу с данными или текст.
        data_dir (str, optional): Путь к директории с данными.
        positive (bool, optional): Флаг положительных данных. Defaults to True.
        attachment (discord.Attachment, optional): Прикрепленный файл.
    """
    logger.info(f'train({ctx})')
    if attachment:
        file_path = f'/tmp/{attachment.filename}'
        await attachment.save(file_path)
        data = file_path

    job_id = model.train(data, data_dir, positive)
    if job_id:
        await ctx.send(f'Model training started. Job ID: {job_id}')
        model.save_job_id(job_id, 'Training task started')
    else:
        await ctx.send('Failed to start training.')


@bot.command(name='test')
async def test(ctx, test_data: str):
    """
    Тестирует модель с предоставленными тестовыми данными.

    Args:
        ctx (commands.Context): Контекст команды.
        test_data (str): Тестовые данные в формате JSON.
    """
    logger.info(f'test({ctx})')
    try:
        # Код преобразует строку JSON в Python объект
        test_data = j_loads(test_data)
        predictions = model.predict(test_data)
        if predictions:
            await ctx.send(f'Test complete. Predictions: {predictions}')
            model.handle_errors(predictions, test_data)
        else:
            await ctx.send('Failed to get predictions.')
    except Exception as ex:
        logger.error(f'Invalid test data format. Please provide a valid JSON string: {ex}')
        await ctx.send('Invalid test data format. Please provide a valid JSON string.')


@bot.command(name='archive')
async def archive(ctx, directory: str):
    """
    Архивирует файлы в указанной директории.

    Args:
        ctx (commands.Context): Контекст команды.
        directory (str): Путь к директории для архивации.
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

    Args:
        ctx (commands.Context): Контекст команды.
        path_to_dir_positive (str): Путь к директории с положительными данными.
        positive (bool, optional): Флаг положительных данных. Defaults to True.
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

    Args:
        ctx (commands.Context): Контекст команды.
    """
    logger.info(f'instruction({ctx})')
    instructions_path = Path('_docs/bot_instruction.md')
    if instructions_path.exists():
        try:
            async with instructions_path.open('r') as file:
                instructions = await file.read()
            await ctx.send(instructions)
        except Exception as ex:
            logger.error(f'An error occurred while reading the instructions: {ex}')
            await ctx.send(f'An error occurred while reading the instructions: {ex}')
    else:
        await ctx.send('Instructions file not found.')


@bot.command(name='correct')
async def correct(ctx, message_id: int, *, correction: str):
    """
    Корректирует предыдущее сообщение по ID.

    Args:
        ctx (commands.Context): Контекст команды.
        message_id (int): ID сообщения для корректировки.
        correction (str): Текст исправления.
    """
    logger.info(f'correct({ctx})')
    try:
        message = await ctx.fetch_message(message_id)
        if message:
            #  Логирование или сохранение исправления
            logger.info(f'Correction for message ID {message_id}: {correction}')
            store_correction(message.content, correction)
            await ctx.send(f'Correction received: {correction}')
        else:
            await ctx.send('Message not found.')
    except Exception as ex:
        logger.error(f'An error occurred: {ex}')
        await ctx.send(f'An error occurred: {ex}')


def store_correction(original_text: str, correction: str):
    """
    Сохраняет исправление для последующего использования.

    Args:
        original_text (str): Оригинальный текст сообщения.
        correction (str): Исправленный текст.
    """
    logger.info('store_correction()')
    correction_file = Path('corrections_log.txt')
    try:
        with correction_file.open('a') as file:
             file.write(f'Original: {original_text}\nCorrection: {correction}\n\n')
    except Exception as ex:
        logger.error(f'Error writing correction to log file: {ex}')


@bot.command(name='feedback')
async def feedback(ctx, *, feedback_text: str):
    """
    Отправляет обратную связь о работе модели.

    Args:
        ctx (commands.Context): Контекст команды.
        feedback_text (str): Текст обратной связи.
    """
    logger.info(f'feedback({ctx})')
    store_correction('Feedback', feedback_text)
    await ctx.send('Thank you for your feedback. We will use it to improve the model.')


@bot.command(name='getfile')
async def getfile(ctx, file_path: str):
    """
    Отправляет файл из указанного пути.

    Args:
        ctx (commands.Context): Контекст команды.
        file_path (str): Путь к файлу.
    """
    logger.info(f'getfile({ctx})')
    file_to_attach = Path(file_path)
    if file_to_attach.exists():
        await ctx.send('Here is the file you requested:', file=discord.File(file_to_attach))
    else:
        await ctx.send(f'File not found: {file_path}')


# def recognizer(audio_url: str, language: str = 'ru-RU') -> str:
#     """Скачивает аудиофайл и распознает речь в нем."""
#     # Download audio file
#     response = requests.get(audio_url)
#     audio_file_path = Path(tempfile.gettempdir()) / 'recognized_audio.ogg'
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
#             logger.error('Google Speech Recognition could not understand audio')
#             return 'Sorry, I could not understand the audio.'
#         except sr.RequestError as e:
#             logger.error(f'Could not request results from Google Speech Recognition service; {e}')
#             return 'Could not request results from the speech recognition service.'

async def text_to_speech_and_play(text, channel):
    """
    Преобразует текст в речь и воспроизводит его в голосовом канале.

    Args:
        text (str): Текст для преобразования в речь.
        channel (discord.VoiceChannel): Голосовой канал для воспроизведения.
    """
    tts = gTTS(text=text, lang='ru')  # Замените 'ru' на нужный язык
    audio_file_path = f'{tempfile.gettempdir()}/response.mp3'  # Путь к временно созданному файлу
    try:
        tts.save(audio_file_path)  # Сохраняем аудиофайл
        voice_channel = channel.guild.voice_client
        if not voice_channel:
            voice_channel = await channel.connect()  # Подключаемся к голосовому каналу

        voice_channel.play(discord.FFmpegPCMAudio(audio_file_path), after=lambda ex: logger.info(f'Finished playing: {ex}'))

        while voice_channel.is_playing():  # Ждем пока играет звук
            await asyncio.sleep(1)

        await voice_channel.disconnect()  # Отключаемся
    except Exception as ex:
        logger.error(f'Error during text-to-speech or playback: {ex}')


@bot.event
async def on_message(message):
    """
    Обрабатывает входящие сообщения и реагирует на голосовые команды.

    Args:
        message (discord.Message): Входящее сообщение.
    """
    #logger.info(f'on_message({message})') #TODO: Подумать какой уровень логирования использовать
    if message.author == bot.user:
        return  # Игнорируем сообщения от самого себя

    if message.content.startswith(PREFIX):
        await bot.process_commands(message)
        return  # Обрабатываем команды

    if message.attachments:
        # Проверка на аудио вложения
        if message.attachments[0].content_type.startswith('audio/'):
             #TODO: добавить распознавание речи, возможно, с использованием API Yandex или Google
            recognized_text = 'распознавание речи не реализовано' #recognizer(message.attachments[0].url)
            response = model.send_message(recognized_text)
    else:
        response = model.send_message(message.content)
    
    if message.author.voice:
            # Если пользователь находится в голосовом канале, подключаемся и воспроизводим ответ
            await text_to_speech_and_play(response, message.author.voice.channel)
    else:
        await message.channel.send(response)  # Отправляем ответ в текстовый канал


if __name__ == '__main__':
    bot.run(gs.credentials.discord.bot_token)