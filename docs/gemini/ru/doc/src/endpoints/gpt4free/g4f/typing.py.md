# Модуль для определения типов данных в g4f

## Обзор

Модуль `typing.py` определяет различные типы данных, используемые в проекте `g4f`. Он включает в себя импорты стандартных модулей `sys`, `os` и модуля `typing`, а также определяет новые типы, псевдонимы и структуры данных для обеспечения строгой типизации и улучшения читаемости кода. Модуль также обрабатывает условный импорт `PIL.Image`, чтобы избежать ошибок, если библиотека Pillow не установлена.

## Подробней

Этот файл играет важную роль в обеспечении типизации в проекте `g4f`, что помогает предотвратить ошибки и улучшает поддержку IDE. Он определяет типы для хешей, результатов генерации, сообщений, куки и изображений, а также включает поддержку `TypedDict` для версий Python ниже 3.8.  Псевдонимы типов, такие как `CreateResult` и `AsyncResult`, упрощают аннотацию функций и делают код более понятным.

## Типы

### `SHA256`

```python
SHA256 = NewType('sha_256_hash', str)
```

**Назначение**: Тип для представления SHA256 хешей.

**Как работает**: Создает новый тип `SHA256` на основе `str` для более явного указания, что переменная содержит SHA256 хеш.

### `CreateResult`

```python
CreateResult = Iterator[Union[str, ResponseType]]
```

**Назначение**: Тип для представления результатов создания в виде итератора строк или `ResponseType`.

**Как работает**: Определяет `CreateResult` как итератор, который может возвращать строки или объекты типа `ResponseType`.

### `AsyncResult`

```python
AsyncResult = AsyncIterator[Union[str, ResponseType]]
```

**Назначение**: Тип для представления асинхронных результатов в виде асинхронного итератора строк или `ResponseType`.

**Как работает**: Определяет `AsyncResult` как асинхронный итератор, который может возвращать строки или объекты типа `ResponseType`.

### `Messages`

```python
Messages = List[Dict[str, Union[str, List[Dict[str, Union[str, Dict[str, str]]]]]]]]
```

**Назначение**: Тип для представления списка сообщений.

**Как работает**: Определяет `Messages` как список словарей, где каждый словарь представляет сообщение и может содержать строки или другие вложенные структуры данных.

### `Cookies`

```python
Cookies = Dict[str, str]
```

**Назначение**: Тип для представления куки.

**Как работает**: Определяет `Cookies` как словарь, где ключи и значения являются строками.

### `ImageType`

```python
ImageType = Union[str, bytes, IO, Image, os.PathLike]
```

**Назначение**: Тип для представления изображений.

**Как работает**: Определяет `ImageType` как объединение различных типов, которые могут представлять изображение: строка, байты, файловый объект, объект `PIL.Image.Image` или путь к файлу.

### `MediaListType`

```python
MediaListType = List[Tuple[ImageType, Optional[str]]]
```

**Назначение**: Тип для представления списка медиафайлов.

**Как работает**: Определяет `MediaListType` как список кортежей, где каждый кортеж содержит `ImageType` и опциональную строку.

## Условный импорт и определение класса `Image`

```python
try:
    from PIL.Image import Image
except ImportError:
    class Image:
        pass
```

**Назначение**: Обеспечивает наличие типа `Image` даже если библиотека Pillow не установлена.

**Как работает**:
1. **Попытка импорта**: Пытается импортировать класс `Image` из модуля `PIL.Image`.
2. **Обработка исключения**: Если импорт не удался (например, Pillow не установлена), создается пустой класс `Image`.

## Использование `TypedDict`

```python
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict
```

**Назначение**: Обеспечивает поддержку `TypedDict` для разных версий Python.

**Как работает**:
1. **Проверка версии Python**: Проверяет, используется ли Python версии 3.8 или выше.
2. **Импорт `TypedDict`**: Импортирует `TypedDict` из `typing`, если версия Python >= 3.8, иначе из `typing_extensions`.

## Функции
В данном модуле функции отсутствуют

## Примеры

Примеры использования определенных типов:

```python
from typing import List, Dict, Union, Optional
from pathlib import Path

# Пример использования SHA256
file_hash: SHA256 = SHA256("a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3")

# Пример использования Messages
message_list: Messages = [
    {"role": "user", "content": "Hello, how are you?"},
    {"role": "assistant", "content": "I'm doing well, thank you!"}
]

# Пример использования ImageType
image_path: ImageType = "path/to/image.jpg"
image_data: ImageType = b"\\xff\\xd8\\xff\\xe1..."

# Пример использования MediaListType
media_list: MediaListType = [
    (image_path, "image/jpeg"),
    (image_data, "image/png")
]