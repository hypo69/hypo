# Модуль `tts`

## Обзор

Модуль `tts` предоставляет функциональность для распознавания речи и преобразования текста в речь. Он включает функции для загрузки аудиофайлов, распознавания речи в них и синтеза речи из текста.

## Подробней

Модуль предназначен для использования в приложениях, где требуется автоматическое распознавание речи или озвучивание текста. Модуль использует сторонние библиотеки, такие как `speech_recognition`, `pydub` и `gTTS`, для выполнения этих задач.

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

**Назначение**: Функция `speech_recognizer` принимает URL-адрес или локальный путь к аудиофайлу, распознает речь в этом файле и возвращает распознанный текст.

**Параметры**:

- `audio_url` (str, optional): URL-адрес аудиофайла для загрузки. По умолчанию `None`.
- `audio_file_path` (Path, optional): Локальный путь к аудиофайлу. По умолчанию `None`.
- `language` (str): Языковой код для распознавания (например, 'ru-RU'). По умолчанию 'ru-RU'.

**Возвращает**:

- `str`: Распознанный текст из аудио или сообщение об ошибке.

**Вызывает исключения**:

- `sr.UnknownValueError`: Если Google Speech Recognition не может распознать аудио.
- `sr.RequestError`: Если не удается получить результаты от сервиса Google Speech Recognition.
- `Exception`: Если возникает ошибка при обработке аудио или распознавании речи.

**Как работает функция**:

1. **Проверка наличия URL-адреса аудиофайла (audio_url)**: Если предоставлен URL-адрес, функция загружает аудиофайл по указанному адресу.
2. **Загрузка аудиофайла**: Если `audio_url` предоставлен, функция выполняет GET-запрос к указанному URL-адресу и сохраняет содержимое ответа во временный файл с расширением `.ogg`.
3. **Определение пути к аудиофайлу**: Если `audio_url` не предоставлен, функция использует предоставленный локальный путь к аудиофайлу `audio_file_path`.
4. **Конвертация OGG в WAV**: Преобразует аудиофайл из формата OGG в формат WAV с использованием библиотеки `pydub`. Это необходимо, поскольку `speech_recognition` лучше работает с WAV.
5. **Инициализация распознавателя речи**: Создает экземпляр класса `sr.Recognizer` из библиотеки `speech_recognition`.
6. **Чтение аудиоданных**: Открывает WAV-файл и считывает аудиоданные с использованием `sr.AudioFile` и `recognizer.record`.
7. **Распознавание речи**: Использует Google Speech Recognition для распознавания речи в аудиоданных.
8. **Обработка результатов распознавания**:
   - Если распознавание прошло успешно, возвращает распознанный текст.
   - Если Google Speech Recognition не смог распознать аудио, логирует ошибку и возвращает сообщение об ошибке.
   - Если не удалось запросить результаты от сервиса Google Speech Recognition, логирует ошибку и возвращает сообщение об ошибке.
9. **Обработка исключений**: Если в процессе выполнения возникают какие-либо исключения, логирует ошибку и возвращает сообщение об ошибке.

**ASCII flowchart**:

```
A [Проверка audio_url]
|
B [Загрузка аудиофайла по URL]
|
C [Определение audio_file_path]
|
D [Конвертация OGG в WAV]
|
E [Инициализация распознавателя]
|
F [Чтение аудиоданных]
|
G [Распознавание речи]
|
H [Обработка результатов]
|
I [Возврат текста или ошибки]
```

**Примеры**:

```python
recognized_text = speech_recognizer(audio_url='https://example.com/audio.ogg')
print(recognized_text)  # Вывод: "Привет"

recognized_text = speech_recognizer(audio_file_path=Path('/path/to/audio.ogg'))
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
    ...
```

**Назначение**: Функция `text2speech` преобразует текст в речь и сохраняет его в виде аудиофайла.

**Параметры**:

- `text` (str): Текст, который нужно преобразовать в речь.
- `lang` (str, optional): Языковой код для речи (например, 'ru'). По умолчанию 'ru'.

**Возвращает**:

- `str`: Путь к сгенерированному аудиофайлу.

**Вызывает исключения**:

- `Exception`: Если возникает ошибка во время преобразования текста в речь.

**Как работает функция**:

1. **Генерация речи**: Использует `gTTS` для генерации речи из предоставленного текста на указанном языке.
2. **Сохранение аудиофайла**: Сохраняет сгенерированный аудиофайл во временный каталог в формате MP3.
3. **Загрузка и экспорт аудио**: Загружает сохраненный MP3-файл с использованием `pydub` и экспортирует его в формат WAV.
4. **Логирование**: Записывает путь к сохраненному аудиофайлу в журнал.
5. **Обработка исключений**: Если в процессе выполнения возникают какие-либо исключения, логирует ошибку и возвращает сообщение об ошибке.

**ASCII flowchart**:

```
A [Генерация речи с помощью gTTS]
|
B [Сохранение аудиофайла в формате MP3]
|
C [Загрузка MP3-файла с помощью pydub]
|
D [Экспорт аудио в формат WAV]
|
E [Логирование пути к аудиофайлу]
|
F [Возврат пути к аудиофайлу или сообщение об ошибке]
```

**Примеры**:

```python
audio_path = await text2speech('Привет', lang='ru')
print(audio_path)  # Вывод: "/tmp/response.mp3"

audio_path = await text2speech('Hello', lang='en')
print(audio_path)