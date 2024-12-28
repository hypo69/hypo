```MD
# <input code>

```python
## \file hypotez/src/utils/convertors/tts.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.utils.convertors.tts 
	:platform: Windows, Unix
	:synopsis: speech recognition and text-to-speech conversion

"""


from pathlib import Path
import tempfile
import asyncio
import requests
import speech_recognition as sr  # Библиотека для распознавания речи
from pydub import AudioSegment  # Library for audio conversion
from gtts import gTTS  # Генерация текста в речь

from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger.logger import logger

def speech_recognizer(audio_url: str = None, audio_file_path: Path = None, language: str = 'ru-RU') -> str:
    """ Download an audio file and recognize speech in it.

    Args:
        audio_url (str, optional): URL of the audio file to be downloaded. Defaults to `None`.
        audio_file_path (Path, optional): Local path to an audio file. Defaults to `None`.
        language (str): Language code for recognition (e.g., 'ru-RU'). Defaults to 'ru-RU'.

    Returns:
        str: Recognized text from the audio or an error message.

    Example:
        .. code::

            recognized_text = speech_recognizer(audio_url='https://example.com/audio.ogg')
            print(recognized_text)  # Output: "Привет"
    """
    try:
        if audio_url:
            # Download the audio file
            response = requests.get(audio_url)
            audio_file_path = Path(tempfile.gettempdir()) / 'recognized_audio.ogg'

            with open(audio_file_path, 'wb') as f:
                f.write(response.content)

        # Convert OGG to WAV
        wav_file_path = audio_file_path.with_suffix('.wav')
        audio = AudioSegment.from_file(audio_file_path)  # Load the OGG file
        audio.export(wav_file_path, format='wav')  # Export as WAV

        # Initialize the recognizer
        recognizer = sr.Recognizer()
        with sr.AudioFile(str(wav_file_path)) as source:
            audio_data = recognizer.record(source)
            try:
                # Recognize speech using Google Speech Recognition
                text = recognizer.recognize_google(audio_data, language=language)
                logger.info(f'Recognized text: {text}')
                return text
            except sr.UnknownValueError:
                logger.error('Google Speech Recognition could not understand audio')
                return 'Sorry, I could not understand the audio.'
            except sr.RequestError as ex:
                logger.error('Could not request results from Google Speech Recognition service:', ex)
                return 'Could not request results from the speech recognition service.'
    except Exception as ex:
        logger.error('Error in speech recognizer:', ex)
        return 'Error during speech recognition.'


async def text2speech(text: str, lang: str = 'ru') -> str:
    """ Convert text to speech and save it as an audio file.

    Args:
        text (str): The text to be converted into speech.
        lang (str, optional): Language code for the speech (e.g., 'ru'). Defaults to 'ru'.

    Returns:
        str: Path to the generated audio file.

    Example:
        .. code::

            audio_path = await text2speech('Привет', lang='ru')
            print(audio_path)  # Output: "/tmp/response.mp3"
    """
    try:
        # Generate speech using gTTS
        tts = gTTS(text=text, lang=lang)
        audio_file_path = f'{tempfile.gettempdir()}/response.mp3'
        tts.save(audio_file_path)  # Save the audio file

        # Load and export audio using pydub
        audio = AudioSegment.from_file(audio_file_path, format='mp3')
        wav_file_path = audio_file_path.replace('.mp3', '.wav')
        audio.export(wav_file_path, format='wav')

        logger.info(f'TTS audio saved at: {wav_file_path}')
        return wav_file_path
    except Exception as ex:
        logger.error('Error in text2speech:', ex)
        return 'Error during text-to-speech conversion.'
```

# <algorithm>

**speech_recognizer:**

1. **Проверка входных данных:** Проверяет, предоставлен ли URL аудиофайла `audio_url` или путь к файлу `audio_file_path`.

   * **Пример:** Если `audio_url` – "https://example.com/audio.ogg", то скачивается файл. Если `audio_file_path` – "/tmp/audio.ogg", то используется указанный файл.

2. **Загрузка аудио (если необходимо):** Если `audio_url` указан, загружается аудиофайл с помощью `requests`. Сохраняется в временную папку.

   * **Пример:** Файл "recognized_audio.ogg" сохраняется в `/tmp/`.

3. **Конвертация в WAV:** Файл аудио (скачанный или входной) преобразуется в формат WAV с помощью `pydub`.

   * **Пример:** "recognized_audio.ogg" преобразуется в "recognized_audio.wav".

4. **Распознавание речи:** Используется библиотека `speech_recognition` для распознавания аудио в формате WAV.

   * **Пример:** Процесс распознавания языка `ru-RU` на основе файла `recognized_audio.wav`.

5. **Обработка ошибок:** Обрабатываются возможные исключения, такие как `UnknownValueError` (непонимание аудио) и `RequestError` (проблемы с сервером распознавания). Выводятся сообщения об ошибках в `logger`.

   * **Пример:** Если возникает ошибка, возвращается сообщение об ошибке.

6. **Возврат результата:** Возвращает распознанный текст.

**text2speech:**

1. **Генерация речи:** Создает объект `gTTS` для генерации аудио с помощью предоставленного текста и языка.

   * **Пример:** `tts = gTTS(text="Привет", lang="ru")`

2. **Сохранение аудио:** Сохраняет сгенерированное аудио в временную папку в формате MP3.

   * **Пример:** Сохранение в файл "/tmp/response.mp3".

3. **Конвертация в WAV:** Преобразует аудиофайл из MP3 в WAV с помощью `pydub`.

   * **Пример:** Преобразование файла "/tmp/response.mp3" в "/tmp/response.wav"

4. **Возврат пути:** Возвращает путь к сохраненному WAV файлу.


# <mermaid>

```mermaid
graph LR
    A[Входной текст/URL] --> B(speech_recognizer);
    B --> C{Загрузить аудио (URL)};
    C -- Да --> D[Скачивание];
    C -- Нет --> E[Использовать файл];
    D --> F[Сохранение в `/tmp`];
    E --> F;
    F --> G[Конвертация в WAV];
    G --> H[Распознавание речи (Google Speech Recognition)];
    H --> I[Обработка результата];
    I -- Успешно --> J[Возврат текста];
    I -- Ошибка --> K[Возврат сообщения об ошибке];
    B --> L{Ошибка};
    L --> M[Возврат сообщения об ошибке];

    subgraph text2speech
        N[Входной текст] --> O(text2speech);
        O --> P[Генерация речи (gTTS)];
        P --> Q[Сохранение в MP3];
        Q --> R[Конвертация в WAV];
        R --> S[Возврат пути к WAV];
        O --> T{Ошибка};
        T --> U[Возврат сообщения об ошибке];
    end
```

**Объяснение диаграммы:**

Диаграмма отображает взаимосвязь между функциями `speech_recognizer` и `text2speech`. Входные данные (`text` или `audio_url`) поступают в соответствующие функции. Зависимости от библиотек (`speech_recognition`, `pydub`, `requests`, `gtts`, `logger`, `jjson`) подразумеваются и не показываются, так как являются внешними для анализируемого модуля.

# <explanation>

**Импорты:**

- `pathlib`: для работы с путями к файлам.
- `tempfile`: для создания временных файлов.
- `asyncio`: для асинхронных операций (в данном случае используется в `text2speech`, но не используется напрямую в `speech_recognizer`).
- `requests`: для загрузки аудиофайлов из интернета.
- `speech_recognition`: для распознавания речи.
- `pydub`: для обработки аудиофайлов (конвертация форматов).
- `gtts`: для генерации текста в речь.
- `src.utils.jjson`: для работы с JSON (предполагается, что определены функции для работы с JSON).
- `src.logger.logger`: для логирования информации.

**Классы:**

Нет классов, только функции.

**Функции:**

- `speech_recognizer`: принимает `audio_url` (URL аудио), `audio_file_path` (локальный путь к файлу) и `language` (язык распознавания). Загружает аудио, конвертирует в WAV, распознает речь и возвращает результат или сообщение об ошибке.
  - Аргументы: `audio_url`, `audio_file_path`, `language`.
  - Возвращаемое значение: `str` (распознанный текст или сообщение об ошибке).
- `text2speech`: принимает `text` (текст для преобразования) и `lang` (язык). Создает аудиофайл из текста, конвертирует его в WAV и возвращает путь к сгенерированному файлу.
  - Аргументы: `text`, `lang`.
  - Возвращаемое значение: `str` (путь к сохраненному аудиофайлу в формате WAV).

**Переменные:**

- `MODE`: строка, вероятно, используется для управления режимом работы программы (например, режим разработки или производства).
- `audio_url`, `audio_file_path`: переменные, хранят URL или путь к аудиофайлу.
- `language`: хранит язык распознавания.
- `wav_file_path`: переменная для хранения пути к WAV файлу.
- `audio_data`: переменная для хранения данных аудиофайла.
- `text`: переменная для хранения распознанного текста.


**Возможные ошибки и улучшения:**

- **Обработка ошибок:** Обработка ошибок в `speech_recognizer` и `text2speech` в целом неплоха, но можно добавить более подробные сообщения об ошибках, включая код ошибки, чтобы облегчить отладку.
- **Управление временными файлами:** Использование `tempfile` правильно, но стоит подумать о способе удаления временных файлов (если они не нужны после завершения работы скрипта).
- **Выбор формата аудио:**  В примере используется .ogg и .mp3. Стоит рассмотреть возможность обработки других форматов, например .wav.
- **Более гибкий выбор языка:** Можно сделать выбор языка более гибким, например, используя словарь языковых кодов вместо `ru-RU`, `ru`.


**Взаимосвязи с другими частями проекта:**

Функции `speech_recognizer` и `text2speech` используют `logger` из `src.logger.logger` для вывода сообщений об ошибках и информации.  Функции также используют `jjson` для работы с JSON, но это пока не отображается на диаграмме.  Использование `jjson` предполагает, что в проекте есть обработка данных в формате JSON, но детали взаимодействия не ясны из представленного кода.