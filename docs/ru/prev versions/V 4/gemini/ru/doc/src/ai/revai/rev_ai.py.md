# Модуль rev_ai

## Обзор

Модуль предоставляет класс `RevAI` для взаимодействия с API сервиса rev.ai с целью обработки аудиофайлов. Он позволяет выполнять транскрипцию и анализ аудио-данных. Модуль содержит функциональность для инициализации подключения к API rev.ai, обработки аудиофайлов и возврата результатов обработки.

## Подробней

Модуль предназначен для интеграции с сервисом rev.ai, который предоставляет услуги транскрипции аудио. Класс `RevAI` инкапсулирует логику взаимодействия с API rev.ai, включая аутентификацию и отправку запросов на обработку аудиофайлов. Этот модуль может быть использован в приложениях, требующих автоматическую транскрипцию аудио, например, в системах обработки вызовов или анализе медиа-контента.

## Классы

### `RevAI`

**Описание**: Класс для работы с API rev.ai.

**Методы**:
- `__init__`: Инициализирует объект `RevAI` с указанным API ключом.
- `process_audio_file`: Обрабатывает аудио файл, используя API rev.ai.

**Параметры**:
- `api_key` (str): API ключ для доступа к сервису rev.ai.
- `audio_file_path` (str): Путь к аудио файлу.

**Примеры**
```python
from src.ai.revai import RevAI

revai_instance = RevAI(api_key='YOUR_API_KEY')  # Замените 'YOUR_API_KEY'
result = revai_instance.process_audio_file('path/to/audio.wav')
if result:
    print(result)
```

## Функции

### `__init__`

```python
def __init__(self, api_key: str):
    """
    Args:
        api_key (str): API ключ для доступа к сервису rev.ai.
    """
```

**Описание**: Инициализирует объект `RevAI` с указанным API ключом.

**Параметры**:
- `api_key` (str): API ключ для доступа к сервису rev.ai.

**Примеры**:
```python
revai_instance = RevAI(api_key='YOUR_API_KEY')
```

### `process_audio_file`

```python
def process_audio_file(self, audio_file_path: str) -> dict:
    """
    Args:
        audio_file_path (str): Путь к аудио файлу.

    Returns:
        dict: Результат обработки аудио файла в формате словаря.
    """
```

**Описание**: Обрабатывает аудио файл, используя API rev.ai.

**Параметры**:
- `audio_file_path` (str): Путь к аудио файлу.

**Возвращает**:
- `dict`: Результат обработки аудио файла в формате словаря.

**Вызывает исключения**:
- `requests.exceptions.RequestException`: Возникает при ошибке отправки запроса к API.
- `Exception`: Возникает при общей ошибке обработки файла.

**Примеры**:
```python
result = revai_instance.process_audio_file('path/to/audio.wav')
if result:
    print(result)