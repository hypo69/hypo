# Анализ кода модуля `tts`

**Качество кода**:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код выполняет заявленную функциональность по распознаванию речи и преобразованию текста в речь.
    - Используются асинхронные функции там, где это уместно (`text2speech`).
    - Код хорошо структурирован, функции имеют понятные имена и назначения.
    - Есть обработка ошибок в блоках `try-except`.
    - Присутствуют docstring для функций.
- **Минусы**:
    - Используются двойные кавычки для строк внутри кода, когда нужно использовать одинарные.
    - Некоторые docstring не соответствуют стандарту RST.
    - Отсутствуют комментарии в формате RST для параметров функций.
    - Используется стандартный `json.load`, вместо `j_loads` или `j_loads_ns`.
    - Логирование ошибок не соответствует шаблону: используются запятые вместо f-строк.
    - Не все исключения обрабатываются с использованием logger.

**Рекомендации по улучшению**:

-   Заменить все двойные кавычки на одинарные, кроме случаев вывода на экран или логирования.
-   Дополнить docstring в соответствии со стандартом RST.
-   Использовать `j_loads` или `j_loads_ns` вместо `json.load`.
-   Переписать логирование ошибок с использованием f-строк.
-   Добавить комментарии в формате RST для параметров функций.
-   Использовать `from src.logger.logger import logger` для импорта логгера.

**Оптимизированный код**:

```python
# -*- coding: utf-8 -*-
"""
Модуль для преобразования речи в текст и текста в речь.
=====================================================

Этот модуль предоставляет функциональность для распознавания речи из аудиофайлов и преобразования текста в аудиофайлы.
Он использует библиотеки speech_recognition, pydub, и gTTS для обработки аудио и преобразования.

Пример использования
--------------------
.. code-block:: python

    recognized_text = speech_recognizer(audio_url='https://example.com/audio.ogg')
    print(recognized_text)  # Вывод: "Привет"

    audio_path = await text2speech('Привет', lang='ru')
    print(audio_path) # Вывод: "/tmp/response.mp3"
"""
from pathlib import Path
import tempfile
import asyncio
import requests
import speech_recognition as sr  # Библиотека для распознавания речи
from pydub import AudioSegment  # Библиотека для обработки аудио
from gtts import gTTS  # Библиотека для генерации речи

from src.utils.jjson import j_loads, j_loads_ns, j_dumps # Импорт функций для работы с JSON
from src.logger.logger import logger # Импорт логгера

def speech_recognizer(audio_url: str = None, audio_file_path: Path = None, language: str = 'ru-RU') -> str:
    """
    Распознает речь в аудиофайле, полученном по URL или из локального файла.

    :param audio_url: URL аудиофайла для скачивания.
    :type audio_url: str, optional
    :param audio_file_path: Локальный путь к аудиофайлу.
    :type audio_file_path: Path, optional
    :param language: Языковой код для распознавания (например, 'ru-RU').
    :type language: str, optional
    :return: Распознанный текст или сообщение об ошибке.
    :rtype: str
    :raises Exception: В случае ошибки при распознавании речи.

    Пример:
        >>> recognized_text = speech_recognizer(audio_url='https://example.com/audio.ogg')
        >>> print(recognized_text)
        "Привет"
    """
    try:
        if audio_url:
            # Скачивание аудиофайла
            response = requests.get(audio_url)
            audio_file_path = Path(tempfile.gettempdir()) / 'recognized_audio.ogg'

            with open(audio_file_path, 'wb') as f:
                f.write(response.content)

        # Конвертация OGG в WAV
        wav_file_path = audio_file_path.with_suffix('.wav')
        audio = AudioSegment.from_file(audio_file_path) # Загрузка OGG файла
        audio.export(wav_file_path, format='wav') # Экспорт в WAV

        # Инициализация распознавателя
        recognizer = sr.Recognizer()
        with sr.AudioFile(str(wav_file_path)) as source:
            audio_data = recognizer.record(source)
            try:
                # Распознавание речи с помощью Google Speech Recognition
                text = recognizer.recognize_google(audio_data, language=language)
                logger.info(f'Recognized text: {text}') # Логирование распознанного текста
                return text
            except sr.UnknownValueError:
                logger.error('Google Speech Recognition could not understand audio') # Логирование ошибки распознавания
                return 'Sorry, I could not understand the audio.'
            except sr.RequestError as ex:
                logger.error(f'Could not request results from Google Speech Recognition service: {ex}') # Логирование ошибки запроса
                return 'Could not request results from the speech recognition service.'
    except Exception as ex:
        logger.error(f'Error in speech recognizer: {ex}') # Логирование общей ошибки
        return 'Error during speech recognition.'


async def text2speech(text: str, lang: str = 'ru') -> str:
    """
    Преобразует текст в речь и сохраняет в аудиофайл.

    :param text: Текст для преобразования в речь.
    :type text: str
    :param lang: Языковой код для речи (например, 'ru').
    :type lang: str, optional
    :return: Путь к сгенерированному аудиофайлу.
    :rtype: str
    :raises Exception: В случае ошибки при преобразовании текста в речь.

    Пример:
        >>> audio_path = await text2speech('Привет', lang='ru')
        >>> print(audio_path)
        "/tmp/response.mp3"
    """
    try:
        # Генерация речи с помощью gTTS
        tts = gTTS(text=text, lang=lang)
        audio_file_path = f'{tempfile.gettempdir()}/response.mp3'
        tts.save(audio_file_path) # Сохранение аудиофайла

        # Загрузка и экспорт аудио с помощью pydub
        audio = AudioSegment.from_file(audio_file_path, format='mp3')
        wav_file_path = audio_file_path.replace('.mp3', '.wav')
        audio.export(wav_file_path, format='wav')

        logger.info(f'TTS audio saved at: {wav_file_path}') # Логирование пути к сохраненному файлу
        return wav_file_path
    except Exception as ex:
        logger.error(f'Error in text2speech: {ex}') # Логирование общей ошибки
        return 'Error during text-to-speech conversion.'
```