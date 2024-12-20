# Модуль revai

## Обзор

Модуль `revai` предоставляет инструменты для работы с API сервиса Rev.com, специализирующегося на обработке аудиофайлов (переговоры, совещания, звонки).  Он позволяет интегрировать функционал Rev.com в приложения, обеспечивая доступ к API для транскрипции, анализа и других связанных задач.

## Использование

Для использования модуля необходимо установить библиотеку `revai`.  Подробная информация о установке и настройке доступна в документации.

## API (Подробности)

```python
# Пример использования функции для загрузки аудиофайла
def upload_audio(file_path: str, file_type: str, callback: callable = None) -> dict | None:
    """
    Загружает аудиофайл на сервер Rev.com.

    Args:
        file_path (str): Путь к аудиофайлу.
        file_type (str): Тип аудиофайла (например, 'mp3', 'wav').
        callback (callable, optional): Функция обратного вызова для получения статуса загрузки. По умолчанию None.

    Returns:
        dict | None: Словарь с информацией о загруженном файле или None при ошибке.

    Raises:
        FileNotFoundError: Если файл не найден по указанному пути.
        ConnectionError: При проблемах с подключением к серверу Rev.com.
    """
```

## Функции

### `upload_audio`

**Описание**: Загружает аудиофайл на сервер Rev.com.

**Параметры**:
- `file_path` (str): Путь к аудиофайлу.
- `file_type` (str): Тип аудиофайла (например, 'mp3', 'wav').
- `callback` (callable, optional): Функция обратного вызова для получения статуса загрузки. По умолчанию `None`.


**Возвращает**:
- `dict | None`: Словарь с информацией о загруженном файле или `None` при ошибке.


**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден по указанному пути.
- `ConnectionError`: При проблемах с подключением к серверу Rev.com.


```python
# Пример использования функции для транскрипции аудиофайла
def transcribe_audio(audio_id: str) -> str | None:
    """
    Выполняет транскрипцию аудиофайла, загруженного ранее.

    Args:
        audio_id (str): Идентификатор загруженного аудиофайла.

    Returns:
        str | None: Текст транскрипции или None при ошибке.

    Raises:
        ValueError: Если аудиофайл не найден.
        APIError: Если возникла ошибка на стороне API.
    """
```

### `transcribe_audio`

**Описание**: Выполняет транскрипцию аудиофайла, загруженного ранее.

**Параметры**:
- `audio_id` (str): Идентификатор загруженного аудиофайла.

**Возвращает**:
- `str | None`: Текст транскрипции или `None` при ошибке.

**Вызывает исключения**:
- `ValueError`: Если аудиофайл не найден.
- `APIError`: Если возникла ошибка на стороне API.


## Классы

(Список классов и их методов, если они есть, добавит здесь)


## Дополнительная информация

- [Документация Rev.com](https://www.rev.com/api/docs)
- [Примеры кода Rev.com](https://docs.rev.ai/resources/code-samples/python/)