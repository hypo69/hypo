# Модуль `hypotez/src/utils/convertors/tts.py`

## Обзор

Модуль `tts.py` предоставляет функции для распознавания речи (speech recognition) и преобразования текста в речь (text-to-speech). Он использует библиотеки `speech_recognition`, `pydub`, и `gtts`.  Модуль предоставляет методы для загрузки аудио файлов, распознавания речи с использованием Google Cloud Speech API и генерации аудио файлов из текста.  Он также управляет преобразованием аудио форматов (например, из OGG в WAV) и обработкой ошибок.


## Функции

### `speech_recognizer`

**Описание**: Функция распознает речь из аудио файла или URL.  Загружает аудио, преобразует его в формат WAV, и использует Google Speech Recognition для распознавания речи.

**Параметры**:

- `audio_url` (str, необязательно): URL аудио файла.
- `audio_file_path` (Path, необязательно): Путь к локальному аудио файлу.
- `language` (str): Код языка для распознавания (например, 'ru-RU'). По умолчанию 'ru-RU'.

**Возвращает**:

- str: Распознанный текст или сообщение об ошибке.

**Обрабатывает исключения**:

- `sr.UnknownValueError`: Возникает, если Google Speech Recognition не смог понять аудио.
- `sr.RequestError`: Возникает, если не удалось получить результаты от сервиса Google Speech Recognition.
- `Exception`: Возникает при других ошибках во время выполнения функции.

### `text2speech`

**Описание**: Функция преобразует текст в речь и сохраняет результат в аудио файл.

**Параметры**:

- `text` (str): Текст, который нужно преобразовать.
- `lang` (str, необязательно): Код языка (например, 'ru'). По умолчанию 'ru'.

**Возвращает**:

- str: Путь к сгенерированному аудио файлу.

**Обрабатывает исключения**:

- `Exception`: Возникает при других ошибках во время выполнения функции.


## Использование

Для использования модуля, импортируйте необходимые функции и вызовите их с соответствующими параметрами.

```python
from hypotez.src.utils.convertors import tts

# Распознавание речи из URL
recognized_text = tts.speech_recognizer(audio_url='https://example.com/audio.ogg')
print(recognized_text)

# Генерация речи из текста
audio_path = asyncio.run(tts.text2speech('Привет, мир!'))
print(audio_path)
```

**Примечание**: Для работы с `speech_recognizer` вам потребуется установить библиотеку `speech_recognition`. Для `text2speech`  необходимы `pydub` и `gtts`.  Также убедитесь, что у вас установлен `requests`.

```bash
pip install speech-recognition pydub gtts requests
```

##  Зависимости


- `speech_recognition`
- `pydub`
- `gtts`
- `requests`
- `asyncio`
- `pathlib`