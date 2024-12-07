# Модуль hypotez/src/goog/drive/drive.py

## Обзор

Модуль `hypotez/src/goog/drive/drive.py` предоставляет базовый класс `GoogleDriveHandler` для взаимодействия с сервисом Google Диск.  Класс позволяет загружать файлы на Google Диск.  Включает в себя обработку аутентификации и получение необходимых токенов доступа.

## Классы

### `GoogleDriveHandler`

**Описание**:  Класс `GoogleDriveHandler` отвечает за взаимодействие с Google Диском. Он хранит информацию о папке назначения и токенах доступа.

**Методы**:

#### `__init__(self, folder_name: str)`

**Описание**: Инициализирует объект `GoogleDriveHandler`.

**Параметры**:

- `folder_name` (str): Имя папки на Google Диске, куда будут загружаться файлы.


#### `_create_credentials(self)`

**Описание**: Получает валидные учетные данные пользователя из хранилища.

**Возвращает**:

- `Credentials`: Объект, содержащий учетные данные пользователя.

**Обрабатывает исключения**:

- Возможны исключения, связанные с ошибками доступа к файлу `token.pickle`.


#### `upload_file(self, file_path: Path)`

**Описание**: Загружает файл на Google Диск в указанную папку.

**Параметры**:

- `file_path` (Path): Путь к файлу, который нужно загрузить.

**Обрабатывает исключения**:

-  Возможны исключения, связанные с проблемой загрузки файла на Google Диск.


## Функции

### `main()`

**Описание**:  Показывает базовый пример использования API Google Диска.

**Возвращает**:

-  Не возвращает ничего.


## Модули

- `header`
- `gs`
- `src.utils.printer`
- `src.logger`
- `googleapiclient.discovery`
- `google_auth_httplib2`
- `google.auth.transport.requests`
- `google.oauth2.credentials`
- `google_auth_oauthlib.flow`
- `pickle`
- `os`
- `pathlib`


## Константы

- `MODE`: Строка, хранящая значение режима работы (`'dev'`).


## Пример использования

```python
from pathlib import Path

file_path = Path('/mnt/data/google_extracted/sample_file.txt')
folder_name = 'My Drive Folder'

google_drive_handler = GoogleDriveHandler(folder_name=folder_name)
google_drive_handler.upload_file(file_path)
```

Этот пример демонстрирует, как создать экземпляр класса `GoogleDriveHandler` и вызвать метод `upload_file` для загрузки файла на Google Диск.  Замените `/mnt/data/google_extracted/sample_file.txt` и `'My Drive Folder'` на ваши реальные пути и название папки соответственно.

**Примечание:** Для работы этого кода необходимы установленные библиотеки `google-api-python-client`, `google-auth-httplib2`, `google-auth-oauthlib`. Необходимо также настроить необходимые ключи доступа Google API.