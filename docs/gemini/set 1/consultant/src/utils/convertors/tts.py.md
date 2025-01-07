# Анализ кода модуля `tts.py`

**Качество кода**

-  Соответствие требованиям по оформлению кода: 8
 -  Плюсы
    - Код хорошо структурирован и разбит на функции `speech_recognizer` и `text2speech`, что повышает его читаемость и повторное использование.
    - Используются асинхронные операции там, где это уместно (`text2speech`).
    - Присутствуют логирующие сообщения, что помогает в отладке и мониторинге работы кода.
 -  Минусы
    - Не все комментарии соответствуют стандарту RST.
    - Используется стандартный `json.load`, вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Некоторые блоки try-except не обрабатывают исключения должным образом (просто возвращают строку с ошибкой), не логируя ошибку.
    - Отсутствует документация для модуля в формате reStructuredText.
    - Использование f-строк в некоторых местах предпочтительнее, чем конкатенация строк.
    - Отсутствуют импорты из `src.logger.logger`.
    - Не все комментарии достаточно информативны.
    - Некоторые переменные не соответствуют стандарту snake_case.
    - Не используется `j_dumps` из `src.utils.jjson`.

**Рекомендации по улучшению**

1.  Добавить документацию модуля в формате RST.
2.  Заменить `json.load` на `j_loads` или `j_loads_ns`.
3.  Обработать ошибки в `try-except` блоках с помощью `logger.error`, и передать исключение в лог.
4.  Добавить недостающие импорты, в частности `from src.logger.logger import logger`.
5.  Привести имена переменных и функций в snake_case.
6.  Все комментарии переписать в формате RST.
7.  Улучшить комментарии в коде, сделав их более информативными.
8.  Избегать избыточного использования `try-except`.
9.  Использовать f-строки для форматирования строк.
10. Добавить проверки на существование и корректность данных перед их использованием.
11. Проверить и использовать `j_dumps`.

**Оптимизированный код**

```python
"""
Модуль для конвертации текста в речь и распознавания речи.
=========================================================================================

Этот модуль содержит функции для преобразования текста в аудио и наоборот,
используя сторонние библиотеки, такие как speech_recognition, pydub и gTTS.

Пример использования
--------------------

Пример использования функций `speech_recognizer` и `text2speech`:

.. code-block:: python

    from pathlib import Path
    import asyncio
    from src.utils.convertors.tts import speech_recognizer, text2speech

    async def main():
        recognized_text = speech_recognizer(audio_url='https://example.com/audio.ogg')
        print(f'Распознанный текст: {recognized_text}')

        audio_path = await text2speech('Привет', lang='ru')
        print(f'Путь к аудио: {audio_path}')

    if __name__ == "__main__":
        asyncio.run(main())

"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

from pathlib import Path
import tempfile
import asyncio
import requests
import speech_recognition as sr
from pydub import AudioSegment
from gtts import gTTS

#from src.utils.jjson import j_loads, j_loads_ns, j_dumps  # убрал пока не используется
from src.logger.logger import logger





def speech_recognizer(audio_url: str = None, audio_file_path: Path = None, language: str = 'ru-RU') -> str:
    """
    Распознаёт речь в аудиофайле.

    :param audio_url: URL аудиофайла для загрузки. По умолчанию `None`.
    :type audio_url: str, optional
    :param audio_file_path: Локальный путь к аудиофайлу. По умолчанию `None`.
    :type audio_file_path: Path, optional
    :param language: Языковой код для распознавания (например, 'ru-RU'). По умолчанию 'ru-RU'.
    :type language: str
    :raises Exception: Если возникает ошибка при распознавании речи.
    :return: Распознанный текст из аудио или сообщение об ошибке.
    :rtype: str

    :Example:

        .. code-block:: python

            recognized_text = speech_recognizer(audio_url='https://example.com/audio.ogg')
            print(recognized_text)  # Output: "Привет"
    """
    try:
        if audio_url:
            # Код загружает аудиофайл по URL.
            response = requests.get(audio_url)
            audio_file_path = Path(tempfile.gettempdir()) / 'recognized_audio.ogg'

            with open(audio_file_path, 'wb') as f:
                f.write(response.content)

        # Код конвертирует OGG в WAV.
        wav_file_path = audio_file_path.with_suffix('.wav')
        audio = AudioSegment.from_file(audio_file_path)  # загрузка OGG
        audio.export(wav_file_path, format='wav')  # экспорт в WAV

        # Инициализирует распознаватель.
        recognizer = sr.Recognizer()
        with sr.AudioFile(str(wav_file_path)) as source:
            audio_data = recognizer.record(source)
            try:
                # Код распознаёт речь с использованием Google Speech Recognition.
                text = recognizer.recognize_google(audio_data, language=language)
                logger.info(f'Распознанный текст: {text}')
                return text
            except sr.UnknownValueError as ex:
                 # Логирует ошибку, если Google Speech Recognition не смог распознать аудио.
                logger.error('Google Speech Recognition не смог распознать аудио', exc_info=ex)
                return 'Sorry, I could not understand the audio.'
            except sr.RequestError as ex:
                # Логирует ошибку, если не удалось запросить результаты из Google Speech Recognition.
                logger.error('Не удалось получить результаты из Google Speech Recognition:', exc_info=ex)
                return 'Could not request results from the speech recognition service.'
    except Exception as ex:
        # Логирует общую ошибку распознавания речи.
        logger.error('Ошибка при распознавании речи', exc_info=ex)
        return 'Error during speech recognition.'


async def text2speech(text: str, lang: str = 'ru') -> str:
    """
    Преобразует текст в речь и сохраняет в аудиофайл.

    :param text: Текст для преобразования в речь.
    :type text: str
    :param lang: Языковой код для синтеза речи (например, 'ru'). По умолчанию 'ru'.
    :type lang: str, optional
    :raises Exception: Если возникает ошибка при преобразовании текста в речь.
    :return: Путь к сгенерированному аудиофайлу.
    :rtype: str

    :Example:

        .. code-block:: python

            audio_path = await text2speech('Привет', lang='ru')
            print(audio_path)  # Output: "/tmp/response.mp3"
    """
    try:
        # Код генерирует речь с использованием gTTS.
        tts = gTTS(text=text, lang=lang)
        audio_file_path = f'{tempfile.gettempdir()}/response.mp3'
        tts.save(audio_file_path)  # Сохраняет аудиофайл.

        # Код загружает и экспортирует аудио с использованием pydub.
        audio = AudioSegment.from_file(audio_file_path, format='mp3')
        wav_file_path = audio_file_path.replace('.mp3', '.wav')
        audio.export(wav_file_path, format='wav')

        logger.info(f'TTS аудио сохранено по пути: {wav_file_path}')
        return wav_file_path
    except Exception as ex:
         # Логирует ошибку преобразования текста в речь.
        logger.error('Ошибка при преобразовании текста в речь', exc_info=ex)
        return 'Error during text-to-speech conversion.'
```