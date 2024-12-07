# Модуль hypotez/src/goog/drive/drive.py

## Обзор

Модуль `hypotez/src/goog/drive/drive.py` предоставляет класс `GoogleDriveHandler` для взаимодействия с Google Диском.  Он позволяет загружать файлы в указанную папку на Google Диск.  Модуль использует Google API для работы с диском и требует предварительной настройки аутентификации.

## Классы

### `GoogleDriveHandler`

**Описание**: Класс `GoogleDriveHandler` отвечает за взаимодействие с Google Диском. Он хранит данные об авторизации и предоставляет метод для загрузки файлов.

**Методы**:

- `__init__(self, folder_name: str)`:
    **Описание**: Инициализирует обработчик Google Диска.
    **Параметры**:
    - `folder_name` (str): Имя папки на Google Диске, куда следует загружать файлы.
    - `creds` (Credentials): Объект аутентификации.
    **Возвращает**:
    - Нет возвращаемого значения.

- `_create_credentials(self):`
    **Описание**: Получает валидные учетные данные пользователя из хранилища.
    **Параметры**:
    - Нет параметров.
    **Возвращает**:
    - `Credentials`: Объект аутентификации.
    **Вызывает исключения**:
        - Возможны исключения, связанные с чтением/записью из/в хранилище токенов.


- `upload_file(self, file_path: Path)`:
    **Описание**: Загружает файл в указанную папку на Google Диске.
    **Параметры**:
    - `file_path` (Path): Путь к файлу, который нужно загрузить.
    **Возвращает**:
    - Нет возвращаемого значения.
    **Вызывает исключения**:
        - Возможны исключения, связанные с ошибками при взаимодействии с Google API.


## Функции

### `main()`

**Описание**:  Демонстрирует базовый способ использования API Google Диска.  Выводит список файлов в корневом каталоге Google Диска.

**Параметры**:
- Нет параметров.
**Возвращает**:
- Нет возвращаемого значения.
**Вызывает исключения**:
- Возможны исключения, связанные с ошибками API.



## Примеры использования

```python
if __name__ == "__main__":
    from pathlib import Path

    file_path = Path('/mnt/data/google_extracted/sample_file.txt')  # Замените на фактический путь к файлу
    folder_name = 'My Drive Folder'  # Замените на фактическую папку на Google Диске

    google_drive_handler = GoogleDriveHandler(
        folder_name=folder_name,
    )
    google_drive_handler.upload_file(file_path)
```

**Примечания**:  Для корректной работы необходимо установить необходимые библиотеки (google-api-python-client, google-auth-httplib2, google-auth-oauthlib).  Необходимо также настроить аутентификацию для доступа к Google Диску.  Замените примерные пути на ваши.