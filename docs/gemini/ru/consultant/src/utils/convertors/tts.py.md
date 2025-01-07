# Анализ кода модуля `tts`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован, каждая функция имеет четкое назначение.
    - Используются библиотеки для конвертации речи в текст и наоборот.
    - Присутствует обработка ошибок с использованием `try-except` блоков.
    - Код использует `logger` для записи ошибок, что соответствует требованиям.
    - Код документирован с использованием docstrings.
    - Присутствуют примеры использования в docstrings
- Минусы
    - Не все комментарии соответствуют формату reStructuredText (RST).
    - Отсутствует описание модуля в формате RST.
    - Использование `tempfile.gettempdir()` для сохранения временных файлов без явного контроля их удаления может привести к накоплению мусора.
    - Избыточное использование try-except, можно заменить на обработку ошибок через `logger.error`
    - Не все импорты используются.

**Рекомендации по улучшению**

1.  **Документация в формате RST**:
    - Добавить описание модуля в формате RST.
    - Переписать docstrings в формате RST.
    - Улучшить docstrings, включив подробное описание аргументов и возвращаемых значений.
2.  **Обработка ошибок**:
    - Упростить обработку ошибок, используя `logger.error` вместо `try-except` там, где это уместно.
3.  **Улучшение временных файлов**:
    - Использовать контекстный менеджер для создания временных файлов, чтобы гарантировать их удаление.
4.  **Импорты**:
    - Удалить неиспользуемые импорты, такие как `asyncio` и `j_dumps`.
5.  **Именование переменных**:
    - Переименовать переменную `ex` на `e` в блоках `except` для краткости.
6. **Комментарии**:
    - Заменить комментарии в коде на более подробные, соответствующие формату RST.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для преобразования речи в текст и текста в речь.
=================================================================

Этот модуль предоставляет функции для распознавания речи из аудиофайлов и преобразования текста в речь.
Он использует библиотеки `speech_recognition`, `pydub` и `gTTS`.

Пример использования
--------------------

Пример использования функций `speech_recognizer` и `text2speech`:

.. code-block:: python

    recognized_text = speech_recognizer(audio_url='https://example.com/audio.ogg')
    print(recognized_text)

    audio_path = await text2speech('Привет', lang='ru')
    print(audio_path)
"""


from pathlib import Path
import tempfile
import requests
import speech_recognition as sr  # Библиотека для распознавания речи
from pydub import AudioSegment  # Library for audio conversion
from gtts import gTTS  # Генерация текста в речь

from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger


def speech_recognizer(audio_url: str = None, audio_file_path: Path = None, language: str = 'ru-RU') -> str:
    """
    Распознает речь в аудиофайле, загруженном по URL или из локального файла.

    :param audio_url: URL аудиофайла для загрузки.
    :type audio_url: str, optional
    :param audio_file_path: Путь к локальному аудиофайлу.
    :type audio_file_path: Path, optional
    :param language: Языковой код для распознавания, например, 'ru-RU'.
    :type language: str, optional
    :return: Распознанный текст или сообщение об ошибке.
    :rtype: str

    :Example:

    .. code-block:: python

        recognized_text = speech_recognizer(audio_url='https://example.com/audio.ogg')
        print(recognized_text)
    """
    try:
        if audio_url:
            # Код исполняет загрузку аудиофайла по URL
            response = requests.get(audio_url)
            audio_file_path = Path(tempfile.gettempdir()) / 'recognized_audio.ogg'

            with open(audio_file_path, 'wb') as f:
                # Код записывает содержимое ответа в файл
                f.write(response.content)

        # Код исполняет преобразование OGG в WAV
        wav_file_path = audio_file_path.with_suffix('.wav')
        audio = AudioSegment.from_file(audio_file_path)  # Загрузка OGG файла
        audio.export(wav_file_path, format='wav')  # Экспорт в WAV

        # Код исполняет инициализацию распознавателя
        recognizer = sr.Recognizer()
        with sr.AudioFile(str(wav_file_path)) as source:
            audio_data = recognizer.record(source)
            try:
                # Код исполняет распознавание речи с помощью Google Speech Recognition
                text = recognizer.recognize_google(audio_data, language=language)
                logger.info(f'Recognized text: {text}')
                return text
            except sr.UnknownValueError:
                # Код логирует ошибку, если Google Speech Recognition не может распознать речь
                logger.error('Google Speech Recognition could not understand audio')
                return 'Sorry, I could not understand the audio.'
            except sr.RequestError as e:
                 # Код логирует ошибку запроса к сервису Google Speech Recognition
                logger.error('Could not request results from Google Speech Recognition service:', e)
                return 'Could not request results from the speech recognition service.'
    except Exception as e:
         # Код логирует ошибку во время распознавания речи
        logger.error('Error in speech recognizer:', e)
        return 'Error during speech recognition.'


async def text2speech(text: str, lang: str = 'ru') -> str:
    """
    Преобразует текст в речь и сохраняет как аудиофайл.

    :param text: Текст для преобразования в речь.
    :type text: str
    :param lang: Языковой код для синтеза речи, например, 'ru'.
    :type lang: str, optional
    :return: Путь к сгенерированному аудиофайлу.
    :rtype: str

    :Example:

    .. code-block:: python

        audio_path = await text2speech('Привет', lang='ru')
        print(audio_path)
    """
    try:
        # Код исполняет генерацию речи с помощью gTTS
        tts = gTTS(text=text, lang=lang)
        audio_file_path = f'{tempfile.gettempdir()}/response.mp3'
        tts.save(audio_file_path)  # Сохранение аудио файла

        # Код исполняет загрузку и экспорт аудио с помощью pydub
        audio = AudioSegment.from_file(audio_file_path, format='mp3')
        wav_file_path = audio_file_path.replace('.mp3', '.wav')
        audio.export(wav_file_path, format='wav')

        logger.info(f'TTS audio saved at: {wav_file_path}')
        return wav_file_path
    except Exception as e:
        # Код логирует ошибку во время преобразования текста в речь
        logger.error('Error in text2speech:', e)
        return 'Error during text-to-speech conversion.'
```