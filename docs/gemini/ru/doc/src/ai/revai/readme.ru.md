# Модуль revai

## Обзор

Этот модуль предоставляет интерфейс для работы с API сервиса Rev.com, специализирующегося на обработке аудиозаписей переговоров, совещаний и звонков.  Модуль позволяет проводить различные операции, например, транскрипцию, распознавание речи и т.д.

## Использование

Для использования модуля необходимо установить библиотеку `rev-api`.  Подробная информация об установке и использовании приведена в документации API Rev.com.

## Основные классы и функции

### Класс `RevaiClient`

**Описание**: Основной класс для взаимодействия с API Rev.com.  Обеспечивает создание и управление сессиями, а также выполнение различных запросов.

**Методы:**

- `__init__(api_key: str)`: Инициализирует клиент с предоставленным API ключом.
- `create_transcription_job(audio_file_path: str, language: str = "en-US") -> dict | None`: Создает задачу транскрипции аудиофайла.
- `get_transcription_status(job_id: str) -> dict | None`: Получает статус выполнения задачи транскрипции по заданному идентификатору.
- `get_transcription_result(job_id: str) -> dict | None`: Получает результат транскрипции по заданному идентификатору.
- `upload_audio_file(audio_file_path: str) -> str | None`: Загружает аудиофайл на сервер Rev.com и возвращает URL.  Возможны ошибки при загрузке, в зависимости от проблем с файлом, сервером или сетью.

**Параметры**:

- `api_key` (str): API ключ Rev.com.

**Возвращает**:

-  `dict | None`: Результат операции, в зависимости от типа запроса. Может возвращать словарь с информацией о транскрипции или статусе, или None, если произошла ошибка.

**Вызывает исключения**:

- `RevApiException`: Общие исключения, связанные с ошибками API.
- `FileNotFoundError`: Исключение, если файл не найден.
- `requests.exceptions.RequestException`:  Исключения, связанные с HTTP запросами (например, проблемы с соединением или сервером).



## Примеры использования (фрагменты кода)

```python
from revai import RevaiClient
import os

# ... (код для получения api_key) ...

client = RevaiClient(api_key)

# Пример загрузки аудио и запуска транскрипции
try:
    audio_file_path = 'path/to/audio.wav'  # путь к аудиофайлу
    url = client.upload_audio_file(audio_file_path)
    if url:
        job_id = client.create_transcription_job(url, language="ru-RU")
        status = client.get_transcription_status(job_id)
        result = client.get_transcription_result(job_id)
        print(result)
    else:
        print("Ошибка загрузки файла")
excep  FileExistsError as e:
        print(f"Ошибка {e}")
except RevApiException as ex:
    print(f"Ошибка API: {ex}")
except Exception as ex:
  print(f"Произошла непредвиденная ошибка: {ex}")
```


## Дополнительные замечания

Для корректной работы необходимо установить необходимые библиотеки, например, `requests`.  Обратите внимание на правильность указания API ключа.  Для удобства добавлены подробные примеры работы с клиентом.


```