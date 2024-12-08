# Модуль hypotez/src/utils/convertors/tts.py

## Обзор

Данный модуль предоставляет функции для распознавания речи (speech recognition) и преобразования текста в речь (text-to-speech). Он использует библиотеки `speech_recognition`, `pydub`, и `gtts`. Модуль умеет загружать аудио из URL, распознавать речь и сохранять результат в WAV формате, а также синтезировать речь по тексту.

## Функции

### `speech_recognizer`

**Описание**: Функция загружает аудио файл по URL или с указанного пути, конвертирует его в WAV формат и распознает речь с помощью Google Speech Recognition.

**Параметры**:
- `audio_url` (str, необязательно): URL аудио файла. По умолчанию `None`.
- `audio_file_path` (Path, необязательно): Путь к локальному аудио файлу. По умолчанию `None`.
- `language` (str): Код языка для распознавания (например, 'ru-RU'). По умолчанию 'ru-RU'.

**Возвращает**:
- `str`: Распознанный текст или сообщение об ошибке.

**Вызывает исключения**:
- `requests.exceptions.RequestException`: Возникает при ошибке запроса к URL.
- `sr.UnknownValueError`: Возникает, если Google Speech Recognition не смог распознать аудио.
- `sr.RequestError`: Возникает при ошибке запроса к сервису Google Speech Recognition.
- `Exception`: Общая ошибка во время работы функции.

### `text2speech`

**Описание**: Функция преобразует текст в речь, сохраняет результат в аудио файл в формате WAV и возвращает путь к сохранённому файлу.

**Параметры**:
- `text` (str): Текст для преобразования в речь.
- `lang` (str, необязательно): Код языка (например, 'ru'). По умолчанию 'ru'.

**Возвращает**:
- `str`: Путь к сохранённому аудио файлу.

**Вызывает исключения**:
- `Exception`: Общая ошибка во время работы функции.


## Использование

Примеры использования функций модуля приведены в их документации.

```
```
```
```
```


```
```
```
```
```
```
```
```
```
```
```

```


```


```

```
```
```

```

```
```

```
```
```

```
```
```
```
```

```
```
```
```
```
```
```
```
```
```
```
```
```

```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```

```
```