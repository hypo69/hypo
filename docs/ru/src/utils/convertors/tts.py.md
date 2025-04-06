# Модуль для преобразования речи в текст и текста в речь
=========================================================

Модуль содержит функции для распознавания речи из аудиофайлов и преобразования текста в речь.

## Обзор

Модуль `tts.py` предоставляет функциональность для работы с речью, включая преобразование текста в речь (text-to-speech, TTS) и распознавание речи (speech-to-text, STT). Он использует библиотеки `speech_recognition` для распознавания речи, `gTTS` для преобразования текста в речь и `pydub` для работы с аудиофайлами. Модуль предназначен для использования в проектах, где требуется автоматическая обработка аудио и речи.

## Подробнее

Модуль содержит две основные функции: `speech_recognizer` и `text2speech`. Функция `speech_recognizer` принимает URL или локальный путь к аудиофайлу, распознает речь и возвращает текст. Функция `text2speech` преобразует заданный текст в речь и сохраняет его в аудиофайл.

## Функции

### `speech_recognizer`

```python
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
```

**Назначение**: Распознавание речи из аудиофайла, доступного по URL или локальному пути.

**Параметры**:

-   `audio_url` (str, optional): URL аудиофайла для скачивания. По умолчанию `None`.
-   `audio_file_path` (Path, optional): Локальный путь к аудиофайлу. По умолчанию `None`.
-   `language` (str): Язык распознавания речи (например, 'ru-RU'). По умолчанию 'ru-RU'.

**Возвращает**:

-   `str`: Распознанный текст из аудио или сообщение об ошибке.

**Вызывает исключения**:

-   `Exception`: Возникает при ошибках во время скачивания, конвертации или распознавания аудио.

**Как работает функция**:

1.  **Проверка наличия URL аудиофайла**:
    Если предоставлен URL, функция скачивает аудиофайл и сохраняет его во временную директорию.
2.  **Конвертация OGG в WAV**:
    Конвертирует аудиофайл из формата OGG в WAV с использованием библиотеки `pydub`.
3.  **Инициализация распознавателя**:
    Инициализирует объект `Recognizer` из библиотеки `speech_recognition`.
4.  **Распознавание речи**:
    Использует Google Speech Recognition для распознавания речи в аудиоданных.
5.  **Обработка результатов**:
    Возвращает распознанный текст или сообщение об ошибке, если распознавание не удалось.

```
A: Проверка наличия audio_url
|
-- B: Скачивание аудиофайла (если audio_url)
|
C: Конвертация OGG в WAV
|
D: Инициализация распознавателя речи
|
E: Распознавание речи с использованием Google Speech Recognition
|
F: Возврат распознанного текста или сообщения об ошибке
```

**Примеры**:

```python
# Пример 1: Распознавание речи из аудиофайла по URL
recognized_text = speech_recognizer(audio_url='https://example.com/audio.ogg')
print(recognized_text)

# Пример 2: Распознавание речи из локального аудиофайла
from pathlib import Path
audio_file_path = Path('/path/to/audio.ogg')
recognized_text = speech_recognizer(audio_file_path=audio_file_path)
print(recognized_text)

# Пример 3: Распознавание речи на английском языке
recognized_text = speech_recognizer(audio_url='https://example.com/audio.ogg', language='en-US')
print(recognized_text)
```

### `text2speech`

```python
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
```

**Назначение**: Преобразование текста в речь и сохранение его в аудиофайл.

**Параметры**:

-   `text` (str): Текст для преобразования в речь.
-   `lang` (str, optional): Язык речи (например, 'ru'). По умолчанию 'ru'.

**Возвращает**:

-   `str`: Путь к сгенерированному аудиофайлу.

**Вызывает исключения**:

-   `Exception`: Возникает при ошибках во время генерации или сохранения аудио.

**Как работает функция**:

1.  **Генерация речи**:
    Использует `gTTS` для генерации речи из заданного текста на указанном языке.
2.  **Сохранение аудиофайла**:
    Сохраняет сгенерированный аудиофайл во временную директорию в формате MP3.
3.  **Конвертация MP3 в WAV**:
    Конвертирует аудиофайл из формата MP3 в WAV с использованием библиотеки `pydub`.
4.  **Возврат пути к аудиофайлу**:
    Возвращает путь к сгенерированному аудиофайлу в формате WAV.

```
A: Генерация речи из текста с использованием gTTS
|
-- B: Сохранение аудиофайла в формате MP3
|
C: Конвертация MP3 в WAV
|
D: Возврат пути к аудиофайлу в формате WAV
```

**Примеры**:

```python
# Пример 1: Преобразование текста в речь на русском языке
import asyncio
async def main():
    audio_path = await text2speech('Привет', lang='ru')
    print(audio_path)

asyncio.run(main())

# Пример 2: Преобразование текста в речь на английском языке
import asyncio
async def main():
    audio_path = await text2speech('Hello', lang='en')
    print(audio_path)
asyncio.run(main())

# Пример 3: Преобразование длинного текста в речь
import asyncio
async def main():
    text = 'Это длинный текст для преобразования в речь. Он будет сохранен в аудиофайл.'
    audio_path = await text2speech(text, lang='ru')
    print(audio_path)
asyncio.run(main())