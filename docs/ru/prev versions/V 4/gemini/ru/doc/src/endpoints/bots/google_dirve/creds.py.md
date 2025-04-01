# Модуль `creds.py`

## Обзор

Модуль `creds.py` предназначен для хранения учетных данных и настроек, необходимых для работы бота, в частности, токена Telegram и идентификаторов TeamDrive для загрузки файлов в Google Drive.

## Подробней

Этот файл содержит класс `Creds`, который определяет атрибуты для хранения токена Telegram (`TG_TOKEN`), идентификатора папки TeamDrive (`TEAMDRIVE_FOLDER_ID`) и идентификатора самого TeamDrive (`TEAMDRIVE_ID`). Эти параметры используются для аутентификации и авторизации бота при взаимодействии с Telegram API и Google Drive API.

## Классы

### `Creds`

**Описание**: Класс для хранения учетных данных и настроек, необходимых для работы бота.

**Методы**:
- Нет

**Параметры**:
- `TG_TOKEN` (str): Токен Telegram бота.
- `TEAMDRIVE_FOLDER_ID` (str): Идентификатор папки TeamDrive.
- `TEAMDRIVE_ID` (str): Идентификатор TeamDrive.

**Примеры**

```python
creds = Creds()
creds.TG_TOKEN = "your_telegram_bot_token"
creds.TEAMDRIVE_FOLDER_ID = "your_teamdrive_folder_id"
creds.TEAMDRIVE_ID = "your_teamdrive_id"
print(creds.TG_TOKEN)
```