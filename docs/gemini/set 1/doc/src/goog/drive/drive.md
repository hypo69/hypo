# Модуль `hypotez/src/goog/drive/drive.py`

## Обзор

Модуль `drive.py` предоставляет базовый класс `GoogleDriveHandler` для взаимодействия с Google Диском.  Этот модуль позволяет загружать файлы в Google Диск.

## Классы

### `GoogleDriveHandler`

**Описание**: Класс `GoogleDriveHandler` управляет взаимодействием с Google Диском. Он содержит методы для авторизации и загрузки файлов.

**Методы**

- `__init__(self, folder_name: str)`: Инициализирует экземпляр класса.
  - **Параметры**:
    - `folder_name` (str): Название папки на Google Диске, куда будут загружаться файлы.
  - **Возвращает**:
    - None

- `_create_credentials(self)`: Получает валидные учетные данные пользователя из хранилища.
  - **Возвращает**:
    - `Credentials`: Объект с учетными данными пользователя.
  - **Обрабатывает исключения**:
    - `FileNotFoundError`: Если файл `token.pickle` не найден.
    - Возможны и другие исключения, связанные с OAuth2.

- `upload_file(self, file_path: Path)`: Загружает файл в Google Диск.
  - **Параметры**:
    - `file_path` (Path): Путь к файлу, который необходимо загрузить.
  - **Возвращает**:
    - None
  - **Обрабатывает исключения**:
    - Возможны исключения, связанные с ошибками загрузки файлов, например, `IOError`, `requests.exceptions.RequestException` и т.п.

## Функции

### `main()`

**Описание**:  Функция `main` демонстрирует базовые функции работы с Drive v3 API.  Она запрашивает список файлов в Google Диске.

**Возвращает**:
- None


**Обрабатывает исключения**:
- Возможны исключения, связанные с ошибками API или обработки данных.



## Примеры использования

```python
if __name__ == "__main__":
    from pathlib import Path

    file_path = Path('/mnt/data/google_extracted/sample_file.txt')  # Замените на ваш путь
    folder_name = 'My Drive Folder'  # Замените на имя вашей папки

    google_drive_handler = GoogleDriveHandler(
        folder_name=folder_name,
    )
    google_drive_handler.upload_file(file_path)
```

**Примечание:**  В примере `upload_file` не реализован, потому что он требует доступа к Google Drive API и не должен быть в документации. Вместо него демонстрируется пример вызова метода.


```python
if __name__ == '__main__':
    main()
```
Этот пример демонстрирует, как вызвать функцию `main()` для получения списка файлов в Google Диске.
```
```