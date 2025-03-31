# Модуль `src.utils.convertors.tts`

## Обзор

Модуль `src.utils.convertors.tts` предоставляет функциональность для распознавания речи и преобразования текста в речь. Он включает функции для загрузки аудиофайлов, распознавания речи в них и генерации речи на основе заданного текста.

## Подробней

Этот модуль предназначен для использования в задачах, где требуется автоматическая обработка аудио и генерация речи. Он может быть полезен для создания голосовых интерфейсов, систем автоматического ответа и других приложений, взаимодействующих с пользователем через голос.

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

**Как работает функция**:
Функция `speech_recognizer` принимает URL или локальный путь к аудиофайлу, загружает его (если указан URL), преобразует в формат WAV и распознает речь с использованием Google Speech Recognition.

**Параметры**:
- `audio_url` (str, optional): URL аудиофайла для загрузки. По умолчанию `None`.
- `audio_file_path` (Path, optional): Локальный путь к аудиофайлу. По умолчанию `None`.
- `language` (str, optional): Языковой код для распознавания речи (например, 'ru-RU'). По умолчанию 'ru-RU'.

**Возвращает**:
- `str`: Распознанный текст из аудиофайла или сообщение об ошибке.

**Вызывает исключения**:
- `sr.UnknownValueError`: Если Google Speech Recognition не может распознать аудио.
- `sr.RequestError`: Если не удается получить результаты от сервиса Google Speech Recognition.
- `Exception`: При возникновении любой другой ошибки в процессе распознавания речи.

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

**Как работает функция**:

Функция `text2speech` преобразует заданный текст в речь, используя gTTS (Google Text-to-Speech), и сохраняет его как аудиофайл в формате WAV.

**Параметры**:
- `text` (str): Текст для преобразования в речь.
- `lang` (str, optional): Языковой код для речи (например, 'ru'). По умолчанию 'ru'.

**Возвращает**:
- `str`: Путь к сгенерированному аудиофайлу в формате WAV.

**Вызывает исключения**:
- `Exception`: При возникновении ошибки в процессе преобразования текста в речь.

**Примеры**:

```python
audio_path = await text2speech('Привет', lang='ru')
print(audio_path)  # Вывод: "/tmp/response.mp3"