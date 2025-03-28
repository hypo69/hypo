# Модуль `src.utils.convertors.tts`

## Обзор

Модуль `src.utils.convertors.tts` предназначен для выполнения операций распознавания речи и преобразования текста в речь.

## Содержание

1. [Функции](#Функции)
    - [`speech_recognizer`](#speech_recognizer)
    - [`text2speech`](#text2speech)

## Функции

### `speech_recognizer`

**Описание**: Загружает аудиофайл и распознает речь в нем.

**Параметры**:
- `audio_url` (str, optional): URL аудиофайла для загрузки. По умолчанию `None`.
- `audio_file_path` (Path, optional): Локальный путь к аудиофайлу. По умолчанию `None`.
- `language` (str): Языковой код для распознавания (например, 'ru-RU'). По умолчанию 'ru-RU'.

**Возвращает**:
- `str`: Распознанный текст из аудио или сообщение об ошибке.

**Вызывает исключения**:
- `sr.UnknownValueError`: Возникает, когда Google Speech Recognition не может распознать аудио.
- `sr.RequestError`: Возникает, когда не удается получить результаты от сервиса Google Speech Recognition.
- `Exception`: Возникает при любой другой ошибке в процессе распознавания речи.

### `text2speech`

**Описание**: Преобразует текст в речь и сохраняет его как аудиофайл.

**Параметры**:
- `text` (str): Текст для преобразования в речь.
- `lang` (str, optional): Языковой код для речи (например, 'ru'). По умолчанию 'ru'.

**Возвращает**:
- `str`: Путь к сгенерированному аудиофайлу.

**Вызывает исключения**:
- `Exception`: Возникает при любой ошибке в процессе преобразования текста в речь.