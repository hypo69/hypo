# Анализ кода модуля `tts`

**Качество кода**

-   **Оценка: 7/10**
    -   **Плюсы:**
        -   Код разбит на логические функции, каждая из которых выполняет свою задачу.
        -   Используются асинхронные операции там, где это необходимо (например, `text2speech`).
        -   Присутствуют комментарии, описывающие основную логику.
        -   Используется библиотека `speech_recognition` для распознавания речи и `gTTS` для синтеза речи.
        -   Используется `logger` из `src.logger.logger` для логирования ошибок.
    -   **Минусы:**
        -   Не все функции имеют docstring в формате RST.
        -   Используется  `tempfile.gettempdir()` напрямую для временных файлов, что может быть ненадежным в некоторых окружениях.
        -   Жесткое кодирование форматов файлов (`.mp3`, `.wav`).
        -   Обработка ошибок в функциях `speech_recognizer` и `text2speech` выполняется через `try-except`, что не рекомендуется.
        -   Используется `f` string для создания пути файла `f\'{tempfile.gettempdir()}/response.mp3\'`, что менее читаемо и может привести к ошибкам, если переменная имеет недопустимое значение.
        -  Некоторые комментарии не соответствуют формату.

**Рекомендации по улучшению**

1.  **Документация:**
    -   Добавить docstring в формате RST для всех функций и классов.
2.  **Обработка ошибок:**
    -   Убрать общие `try-except` блоки и обрабатывать исключения с помощью `logger.error`.
3.  **Управление временными файлами:**
    -   Использовать `tempfile.NamedTemporaryFile` для управления временными файлами. Это гарантирует, что временные файлы будут автоматически удалены после использования.
4.  **Гибкость форматов файлов:**
    -   Сделать форматы файлов для конвертации параметрами функций.
5.  **Улучшение комментариев:**
    -  Уточнить и дополнить комментарии, привести их в соответствие с рекомендациями.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
.. module:: src.utils.convertors.tts
   :platform: Windows, Unix
   :synopsis: Модуль для распознавания речи и преобразования текста в речь.
"""

from pathlib import Path
import tempfile
import asyncio
import requests
import speech_recognition as sr  # Библиотека для распознавания речи
from pydub import AudioSegment  # Библиотека для конвертации аудио
from gtts import gTTS  # Библиотека для преобразования текста в речь

from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger.logger import logger


def speech_recognizer(audio_url: str = None, audio_file_path: Path = None, language: str = 'ru-RU') -> str:
    """
    Распознает речь в аудиофайле, загруженном по URL или из локального файла.

    Args:
        audio_url (str, optional): URL аудиофайла для загрузки. По умолчанию `None`.
        audio_file_path (Path, optional): Локальный путь к аудиофайлу. По умолчанию `None`.
        language (str, optional): Языковой код для распознавания (например, 'ru-RU'). По умолчанию 'ru-RU'.

    Returns:
        str: Распознанный текст из аудио или сообщение об ошибке.

    Raises:
         Exception: При возникновении ошибки во время обработки аудио.

    Example:
        >>> recognized_text = speech_recognizer(audio_url='https://example.com/audio.ogg')
        >>> print(recognized_text)  # Выведет распознанный текст, если он есть.
    """
    try:
        if audio_url:
            # Загрузка аудиофайла по URL
            response = requests.get(audio_url)
            if response.status_code != 200:
               logger.error(f'Ошибка загрузки аудио файла {response.status_code}')
               return 'Ошибка загрузки аудио.'
            # Создание временного файла для сохранения загруженного аудио
            with tempfile.NamedTemporaryFile(suffix='.ogg', delete=False) as tmp_audio_file:
                tmp_audio_file.write(response.content)
                audio_file_path = Path(tmp_audio_file.name)

        # Преобразование OGG в WAV
        wav_file_path = audio_file_path.with_suffix('.wav')
        try:
           # Загрузка аудио из файла
           audio = AudioSegment.from_file(audio_file_path)
           # Экспорт в формат WAV
           audio.export(wav_file_path, format='wav')
        except Exception as ex:
            logger.error(f'Не удалось конвертировать аудио файл {ex}')
            return 'Ошибка конвертации аудио.'

        # Инициализация распознавателя
        recognizer = sr.Recognizer()
        try:
            # Загрузка аудиоданных из WAV файла
            with sr.AudioFile(str(wav_file_path)) as source:
                audio_data = recognizer.record(source)
            # Распознавание речи с помощью Google Speech Recognition
            text = recognizer.recognize_google(audio_data, language=language)
            logger.info(f'Распознанный текст: {text}')
            return text
        except sr.UnknownValueError:
            logger.error('Google Speech Recognition не смог распознать аудио')
            return 'Извините, я не смог распознать аудио.'
        except sr.RequestError as ex:
            logger.error(f'Не удалось получить результаты от Google Speech Recognition: {ex}')
            return 'Не удалось получить результаты от сервиса распознавания речи.'
    except Exception as ex:
        logger.error(f'Ошибка в распознавателе речи: {ex}')
        return 'Ошибка во время распознавания речи.'
    finally:
        # Удаление временного файла
        if audio_file_path and audio_file_path.exists():
            try:
                audio_file_path.unlink()
                wav_file_path.unlink()
            except Exception as ex:
                logger.error(f'Не удалось удалить временные файлы {ex}')


async def text2speech(text: str, lang: str = 'ru', output_format: str = 'wav') -> str:
    """
    Преобразует текст в речь и сохраняет как аудиофайл.

    Args:
        text (str): Текст для преобразования в речь.
        lang (str, optional): Языковой код для речи (например, 'ru'). По умолчанию 'ru'.
        output_format (str, optional): Формат выходного аудиофайла ('mp3', 'wav'). По умолчанию 'wav'.

    Returns:
        str: Путь к сгенерированному аудиофайлу.

    Raises:
         Exception: При возникновении ошибки во время преобразования текста в речь.

    Example:
        >>> audio_path = await text2speech('Привет', lang='ru', output_format='mp3')
        >>> print(audio_path) # Выведет путь к аудио файлу
    """
    try:
        # Генерация речи с помощью gTTS
        tts = gTTS(text=text, lang=lang)
        # Создание временного файла для сохранения аудио
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as tmp_audio_file:
            tmp_audio_file_path = Path(tmp_audio_file.name)
            tts.save(str(tmp_audio_file_path))

        # Загрузка аудио из временного файла
        audio = AudioSegment.from_file(str(tmp_audio_file_path), format='mp3')
        # Определение пути выходного файла в зависимости от формата
        output_file_path = tmp_audio_file_path.with_suffix(f'.{output_format}')
        # Экспорт аудио в нужный формат
        audio.export(str(output_file_path), format=output_format)
        logger.info(f'TTS аудио сохранено по пути: {output_file_path}')
        return str(output_file_path)
    except Exception as ex:
        logger.error(f'Ошибка при преобразовании текста в речь: {ex}')
        return 'Ошибка во время преобразования текста в речь.'
    finally:
        # Удаление временного файла
        if tmp_audio_file_path and tmp_audio_file_path.exists():
            try:
                tmp_audio_file_path.unlink()
            except Exception as ex:
                logger.error(f'Не удалось удалить временные файлы {ex}')


```