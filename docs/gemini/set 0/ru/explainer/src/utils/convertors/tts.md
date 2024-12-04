# <input code>

```python
## \file hypotez/src/utils/convertors/tts.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils.convertors.tts 
	:platform: Windows, Unix
	:synopsis: speech recognition and text-to-speech conversion

"""
MODE = 'dev'

from pathlib import Path
import tempfile
import asyncio
import requests
import speech_recognition as sr  # Библиотека для распознавания речи
from pydub import AudioSegment  # Library for audio conversion
from gtts import gTTS  # Генерация текста в речь

from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger import logger


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

1. **Input Validation:** Check if `audio_url` or `audio_file_path` is provided.
2. **Download (if needed):** If `audio_url` is given, download the audio to a temporary file.
3. **Conversion to WAV:** Convert the downloaded or provided audio file from OGG to WAV using pydub.
4. **Speech Recognition:**  Use `speech_recognition` to recognize the speech from the WAV file.
5. **Error Handling:** Catch exceptions (`sr.UnknownValueError`, `sr.RequestError`, general `Exception`) and log/return appropriate error messages.
6. **Return:** Return the recognized text or an error message.

**text2speech:**

1. **Text-to-Speech Conversion:** Use `gTTS` to convert the input text to speech.
2. **Save as MP3:** Save the generated audio as a temporary MP3 file.
3. **Conversion to WAV:** Convert the MP3 file to WAV using pydub.
4. **Logging:** Log the path to the WAV file.
5. **Return:** Return the path to the WAV file.
6. **Error Handling:** Catch exceptions and log/return appropriate error messages.

# <mermaid>

```mermaid
graph TD
    A[speech_recognizer] --> B{audio_url or audio_file_path?};
    B -- Yes --> C[Download audio];
    B -- No --> C1[No download];
    C --> D[Convert to WAV];
    C1 --> D;
    D --> E[Speech Recognition];
    E --> F{Success?};
    F -- Yes --> G[Return text];
    F -- No --> H[Error handling, Return error];
    E -- Error --> H;
    
    I[text2speech] --> J[Convert text to speech (gTTS)];
    J --> K[Save as MP3];
    K --> L[Convert to WAV];
    L --> M[Return path];
    
    style C fill:#f9f,stroke:#333,stroke-width:2px
    style C1 fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333,stroke-width:2px
    style E fill:#ccf,stroke:#333,stroke-width:2px
    style F fill:#ccf,stroke:#333,stroke-width:2px
    style G fill:#ccf,stroke:#333,stroke-width:2px
    style H fill:#f9f,stroke:#333,stroke-width:2px

    subgraph Dependencies
        style G fill:#ccf,stroke:#333,stroke-width:2px
        style G fill:#ccf,stroke:#333,stroke-width:2px
        S[requests] --> C;
        T[tempfile] --> C;
        U[speech_recognition] --> E;
        V[pydub] --> D,L;
        W[gtts] --> J;
        X[logger] --> E,H;
        Y[pathlib] --> A,I
        Z[asyncio] --> I;
        
    end
```

# <explanation>

**Импорты:**

- `from pathlib import Path`: Импортирует класс `Path` для работы с путями к файлам. Это полезно для более безопасной и переносимой работы с файлами.
- `import tempfile`: Для создания временных файлов.
- `import asyncio`:  Возможно используется для асинхронных операций, но в данном коде не используется напрямую.
- `import requests`: Для загрузки аудио файлов из интернета.
- `import speech_recognition as sr`: Библиотека для распознавания речи, использующая Google Cloud Speech-to-Text.  Связь с `src`: Используется для конкретной функциональности в `hypotez`, но не напрямую зависит от `src`.
- `from pydub import AudioSegment`: Библиотека для работы с аудио файлами, например, для преобразования форматов.  Связь с `src`: Используется для конкретной функциональности в `hypotez`, но не напрямую зависит от `src`.
- `from gtts import gTTS`: Библиотека для синтеза речи. Связь с `src`: Используется для конкретной функциональности в `hypotez`, но не напрямую зависит от `src`.
- `from src.utils.jjson import j_loads, j_loads_ns, j_dumps`: Импортирует функции для работы с JSON.  Связь с `src`: Явно зависимость от модуля `jjson`, который, скорее всего, реализован в `src.utils`.
- `from src.logger import logger`:  Импортирует `logger` объект для логирования.  Связь с `src`:  Прямая зависимость от модуля `logger` в директории `src`.

**Классы:**

Нет определенных классов в данном коде.


**Функции:**

- `speech_recognizer(audio_url, audio_file_path, language)`: Функция для распознавания речи.
    - Принимает URL аудио файла или локальный путь к файлу.
    - Загружает аудио, если `audio_url` предоставлен.
    - Преобразует аудио в WAV формат.
    - Распознает речь с помощью `speech_recognition`.
    - Возвращает распознанный текст или сообщение об ошибке.
- `text2speech(text, lang)`: Функция для преобразования текста в речь.
    - Принимает текст и код языка.
    - Преобразует текст в речь с помощью `gTTS`.
    - Сохраняет аудио в временный файл MP3.
    - Преобразует MP3 в WAV.
    - Возвращает путь к сгенерированному WAV файлу или сообщение об ошибке.

**Переменные:**

- `MODE`: Строковая переменная, хранящая режим работы.
- `audio_url`, `audio_file_path`, `language`: Аргументы функций.
- `wav_file_path`, `audio_file_path`:  Временные пути к файлам.
- `recognizer`, `audio_data`, `text`:  Локальные переменные, используемые в `speech_recognizer`.
- `tts`, `audio_file_path`, `wav_file_path`:  Локальные переменные, используемые в `text2speech`.


**Возможные ошибки и улучшения:**

- **Обработка исключений:**  Обработка исключений хорошая, но можно добавить более подробные сообщения об ошибках в лог.
- **Кэширование:** Если часто используются одни и те же аудио файлы или тексты, можно добавить кэширование, чтобы не выполнять ненужные операции.
- **Оптимизация обработки аудио:** Если аудио файлы очень большие, можно оптимизировать загрузку и обработку аудио, используя многопоточность или асинхронные операции.
- **Выбор формата аудио:**  Использование WAV как промежуточного формата, а не mp3, улучшает качество и не создает потерь.
- **Языки:** В коде поддерживается только один язык для распознавания речи. Можно расширить поддержку других языков.


**Взаимосвязь с другими частями проекта:**

Функции `speech_recognizer` и `text2speech`  вероятно, используются в других частях проекта для обработки пользовательского ввода или вывода.  `logger` предоставляет возможность логирования, что помогает отслеживать ошибки и поведение системы. `jjson` вероятно используется для работы с данными в формате JSON в других частях приложения.