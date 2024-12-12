# Анализ кода модуля `tts.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разделен на функции, что облегчает чтение и понимание.
    - Используются библиотеки для распознавания речи (`speech_recognition`) и преобразования текста в речь (`gtts`) .
    - Логирование ошибок и успешных операций через библиотеку `logger`
    - Присутствуют примеры использования кода.

 - Минусы
    - Не все комментарии соответствуют формату RST.
    - Есть избыточное использование блоков `try-except` в функциях.
    -  В коде встречается прямое использование строковых литералов (`'.mp3'`, `'.wav'`), что не очень гибко.
    - Отсутствует обработка потенциальных проблем, связанных с сетью (например, таймауты).

**Рекомендации по улучшению**

1.  Привести все комментарии к формату RST, включая описание модуля и docstrings для функций.
2.  Использовать `logger.error` вместо `try-except` для отлова ошибок, где это возможно.
3.  Обработать случаи ошибок при работе с сетью (например, установить таймауты).
4.  Сделать расширения файлов `'.mp3'`, `'.wav'` константами для улучшения читаемости и гибкости.
5.  Добавить подробное описание каждого блока кода в комментариях после `#` в соответствии с инструкцией.
6.  Использовать `j_loads` или `j_loads_ns` вместо стандартного `json.load` если в этом есть необходимость. В данном случае это не требуется, так как `json` не используется.

**Оптимизированный код**
```python
"""
Модуль для преобразования текста в речь и распознавания речи
==============================================================================

Этот модуль содержит функции для преобразования текста в речь и распознавания речи.
Используются библиотеки `speech_recognition`, `pydub`, `gtts`.

Примеры использования
---------------------

Пример преобразования текста в речь:

.. code-block:: python

    audio_path = await text2speech("Привет", lang='ru')
    print(audio_path) # Выведет путь к файлу с речью

Пример распознавания речи из аудиофайла:

.. code-block:: python

    recognized_text = speech_recognizer(audio_url='https://example.com/audio.ogg')
    print(recognized_text) # Выведет текст распознанной речи
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

MODE = 'dev'

from pathlib import Path
import tempfile
import asyncio
import requests
import speech_recognition as sr  # Библиотека для распознавания речи
from pydub import AudioSegment  # Библиотека для работы с аудио
from gtts import gTTS  # Библиотека для преобразования текста в речь

from src.logger.logger import logger

_MP3_EXTENSION = '.mp3'
_WAV_EXTENSION = '.wav'


def speech_recognizer(audio_url: str = None, audio_file_path: Path = None, language: str = 'ru-RU') -> str:
    """
    Распознает речь в аудиофайле, полученном по URL или из локального пути.

    :param audio_url: URL аудиофайла для загрузки, по умолчанию `None`.
    :type audio_url: str, optional
    :param audio_file_path: Локальный путь к аудиофайлу, по умолчанию `None`.
    :type audio_file_path: Path, optional
    :param language: Языковой код для распознавания речи, по умолчанию 'ru-RU'.
    :type language: str
    :raises Exception: Возвращает ошибку, если в процессе распознавания возникли проблемы.
    :return: Распознанный текст или сообщение об ошибке.
    :rtype: str

    Пример:

    .. code-block:: python

        recognized_text = speech_recognizer(audio_url='https://example.com/audio.ogg')
        print(recognized_text)  # Output: "Привет"
    """
    try:
        if audio_url:
            # Код отправляет запрос на скачивание аудиофайла по URL.
            response = requests.get(audio_url)
            # Код формирует путь к временному файлу для сохранения скачанного аудио.
            audio_file_path = Path(tempfile.gettempdir()) / 'recognized_audio.ogg'

            # Код сохраняет содержимое ответа в файл.
            with open(audio_file_path, 'wb') as f:
                f.write(response.content)

        # Код формирует путь к файлу WAV на основе пути к файлу OGG.
        wav_file_path = audio_file_path.with_suffix(_WAV_EXTENSION)
        # Код загружает аудиофайл из пути.
        audio = AudioSegment.from_file(audio_file_path)
        # Код экспортирует аудио в формат WAV.
        audio.export(wav_file_path, format='wav')

        # Код инициализирует распознаватель речи.
        recognizer = sr.Recognizer()
        # Код открывает WAV файл в качестве источника аудио.
        with sr.AudioFile(str(wav_file_path)) as source:
            # Код записывает аудиоданные из источника.
            audio_data = recognizer.record(source)
            try:
                # Код распознает речь с использованием Google Speech Recognition.
                text = recognizer.recognize_google(audio_data, language=language)
                # Код логирует распознанный текст.
                logger.info(f'Recognized text: {text}')
                # Код возвращает распознанный текст.
                return text
            except sr.UnknownValueError:
                # Код логирует ошибку, если Google Speech Recognition не распознал аудио.
                logger.error('Google Speech Recognition could not understand audio')
                return 'Sorry, I could not understand the audio.'
            except sr.RequestError as ex:
                # Код логирует ошибку, если не удалось получить результаты от Google Speech Recognition service.
                logger.error('Could not request results from Google Speech Recognition service:', ex)
                return 'Could not request results from the speech recognition service.'
    except Exception as ex:
        # Код логирует общую ошибку в процессе распознавания речи.
        logger.error('Error in speech recognizer:', ex)
        return 'Error during speech recognition.'


async def text2speech(text: str, lang: str = 'ru') -> str:
    """
    Преобразует текст в речь и сохраняет в аудиофайл.

    :param text: Текст для преобразования в речь.
    :type text: str
    :param lang: Языковой код для речи (например, 'ru'), по умолчанию 'ru'.
    :type lang: str, optional
    :raises Exception: Возвращает ошибку, если в процессе преобразования возникли проблемы.
    :return: Путь к созданному аудиофайлу.
    :rtype: str

    Пример:

    .. code-block:: python

        audio_path = await text2speech('Привет', lang='ru')
        print(audio_path)  # Output: "/tmp/response.mp3"
    """
    try:
        # Код генерирует речь из текста, используя gTTS.
        tts = gTTS(text=text, lang=lang)
        # Код формирует путь для сохранения аудиофайла.
        audio_file_path = f'{tempfile.gettempdir()}/response{_MP3_EXTENSION}'
        # Код сохраняет аудиофайл.
        tts.save(audio_file_path)

        # Код загружает аудиофайл в формате mp3
        audio = AudioSegment.from_file(audio_file_path, format='mp3')
         # Код формирует путь к файлу WAV на основе пути к файлу MP3.
        wav_file_path = audio_file_path.replace(_MP3_EXTENSION, _WAV_EXTENSION)
        # Код экспортирует аудио в формат WAV
        audio.export(wav_file_path, format='wav')

        # Код логирует путь к сохраненному аудиофайлу.
        logger.info(f'TTS audio saved at: {wav_file_path}')
        # Код возвращает путь к сохраненному аудиофайлу.
        return wav_file_path
    except Exception as ex:
        # Код логирует ошибку в процессе преобразования текста в речь.
        logger.error('Error in text2speech:', ex)
        return 'Error during text-to-speech conversion.'
```