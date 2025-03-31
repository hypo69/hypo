# Модуль `tts`

## Обзор

Модуль `tts` предоставляет функции для распознавания речи и преобразования текста в речь. Он использует библиотеки `speech_recognition` для распознавания речи из аудиофайлов и `gTTS` для генерации речи из текста.

## Подробней

Модуль предназначен для преобразования аудио в текст и текста в аудио. Модуль использует `speech_recognition` для обработки аудио и `gTTS` для генерации речи. Распознавание речи выполняется с использованием сервиса Google Speech Recognition.
Временные файлы сохраняются в системном каталоге временных файлов (`tempfile.gettempdir()`).

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
    ...
```

**Описание**: Распознает речь в аудиофайле, загруженном по URL или из локального файла.

**Как работает функция**:
1. Если предоставлен `audio_url`, функция загружает аудиофайл по указанному URL и сохраняет его во временный файл.
2. Преобразует аудиофайл из формата OGG в формат WAV.
3. Инициализирует распознаватель речи `sr.Recognizer()`.
4. Использует Google Speech Recognition для распознавания речи в аудиоданных.
5. Возвращает распознанный текст или сообщение об ошибке в случае неудачи.

**Параметры**:
- `audio_url` (str, optional): URL аудиофайла для загрузки. По умолчанию `None`.
- `audio_file_path` (Path, optional): Локальный путь к аудиофайлу. По умолчанию `None`.
- `language` (str): Языковой код для распознавания (например, 'ru-RU'). По умолчанию 'ru-RU'.

**Возвращает**:
- `str`: Распознанный текст из аудио или сообщение об ошибке.

**Вызывает исключения**:
- `sr.UnknownValueError`: Если Google Speech Recognition не может распознать аудио.
- `sr.RequestError`: Если не удается запросить результаты от сервиса Google Speech Recognition.
- `Exception`: Если возникает любая другая ошибка в процессе распознавания речи.

**Примеры**:

```python
recognized_text = speech_recognizer(audio_url='https://example.com/audio.ogg')
print(recognized_text)  # Вывод: "Привет"
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
    ...
```

**Описание**: Преобразует текст в речь и сохраняет его в аудиофайл.

**Как работает функция**:
1. Использует `gTTS` для генерации речи из предоставленного текста на указанном языке.
2. Сохраняет сгенерированный аудиофайл во временный файл в формате MP3.
3. Загружает аудиофайл и экспортирует его в формат WAV с использованием `pydub`.
4. Возвращает путь к сгенерированному аудиофайлу.

**Параметры**:
- `text` (str): Текст для преобразования в речь.
- `lang` (str, optional): Языковой код для речи (например, 'ru'). По умолчанию 'ru'.

**Возвращает**:
- `str`: Путь к сгенерированному аудиофайлу.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка в процессе преобразования текста в речь.

**Примеры**:

```python
audio_path = await text2speech('Привет', lang='ru')
print(audio_path)  # Вывод: "/tmp/response.mp3"