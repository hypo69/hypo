# `src/goog/drive/drive.py`

## Обзор

Модуль `drive.py` предоставляет минимальную библиотеку для работы с Google Drive. Он включает класс `GoogleDriveHandler`, который инкапсулирует логику аутентификации и загрузки файлов в Google Drive.

## Оглавление

1.  [Классы](#классы)
    *   [GoogleDriveHandler](#googledrivehandler)
        *   [`__init__`](#__init__)
        *   [`_create_credentials`](#_create_credentials)
        *   [`upload_file`](#upload_file)
2.  [Функции](#функции)
    *   [`main`](#main)

## Классы

### `GoogleDriveHandler`

**Описание**: Класс `GoogleDriveHandler` предназначен для управления взаимодействием с Google Drive. Он обеспечивает аутентификацию и возможность загрузки файлов.

#### `__init__`

**Описание**: Инициализирует объект `GoogleDriveHandler`.

**Параметры**:
- `folder_name` (str): Имя папки в Google Drive, в которую будут загружаться файлы.

**Возвращает**:
- `None`

#### `_create_credentials`

**Описание**: Получает действительные учетные данные пользователя из хранилища.

**Параметры**:
- `None`

**Возвращает**:
- `google.oauth2.credentials.Credentials`: Объект с учетными данными пользователя.

#### `upload_file`

**Описание**: Загружает файл в указанную папку на Google Drive.
**Параметры**:
- `file_path` (Path): Путь к файлу, который нужно загрузить.

**Возвращает**:
- `None`

## Функции

### `main`

**Описание**: Показывает базовое использование Drive v3 API.

**Параметры**:
- `None`

**Возвращает**:
- `None`