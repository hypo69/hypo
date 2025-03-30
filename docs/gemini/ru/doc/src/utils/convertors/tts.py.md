# Модуль `tts`

## Обзор

Модуль `tts` предоставляет функциональность для распознавания речи и преобразования текста в речь. Он включает функции для загрузки аудиофайлов, распознавания речи в них и генерации речи из текста. Модуль использует библиотеки `speech_recognition`, `pydub` и `gTTS` для выполнения этих задач.

## Подробней

Этот модуль предоставляет функции для преобразования речи в текст и наоборот, что позволяет интегрировать голосовые интерфейсы в различные приложения. Функция `speech_recognizer` позволяет распознавать речь из аудиофайлов, а функция `text2speech` преобразует текст в аудиофайлы. Модуль использует временные файлы для хранения промежуточных результатов, обеспечивая эффективную обработку данных.

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

**Описание**: Распознает речь в аудиофайле, который может быть загружен по URL или указан локальным путем. Функция сначала загружает (при необходимости) и конвертирует аудиофайл в формат WAV, а затем использует Google Speech Recognition для преобразования речи в текст.

**Параметры**:
- `audio_url` (str, optional): URL аудиофайла для загрузки. По умолчанию `None`.
- `audio_file_path` (Path, optional): Локальный путь к аудиофайлу. По умолчанию `None`.
- `language` (str, optional): Языковой код для распознавания речи (например, `'ru-RU'`). По умолчанию `'ru-RU'`.

**Возвращает**:
- `str`: Распознанный текст из аудио или сообщение об ошибке.

**Вызывает исключения**:
- `sr.UnknownValueError`: Возникает, если Google Speech Recognition не может распознать аудио.
- `sr.RequestError`: Возникает, если не удается получить результаты от сервиса Google Speech Recognition.
- `Exception`: Возникает при любой другой ошибке в процессе распознавания речи.

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
```

**Описание**: Преобразует текст в речь и сохраняет его в виде аудиофайла. Функция использует `gTTS` для генерации речи из текста и сохраняет аудиофайл во временном каталоге.

**Параметры**:
- `text` (str): Текст для преобразования в речь.
- `lang` (str, optional): Языковой код для речи (например, `'ru'`). По умолчанию `'ru'`.

**Возвращает**:
- `str`: Путь к сгенерированному аудиофайлу.

**Вызывает исключения**:
- `Exception`: Возникает при любой ошибке в процессе преобразования текста в речь.

**Примеры**:

```python
audio_path = await text2speech('Привет', lang='ru')
print(audio_path)  # Вывод: "/tmp/response.mp3"