# Модуль для хранения учетных данных

## Обзор

Модуль `creds.py` предназначен для хранения учетных данных, таких как токен Telegram-бота и идентификаторы TeamDrive для Google Drive.

## Подробнее

Этот модуль содержит класс `Creds`, который используется для хранения учетных данных, необходимых для работы с Telegram и Google Drive. Учетные данные включают токен Telegram-бота (`TG_TOKEN`), идентификатор папки TeamDrive (`TEAMDRIVE_FOLDER_ID`) и идентификатор TeamDrive (`TEAMDRIVE_ID`). Этот модуль важен для настройки и аутентификации при взаимодействии с Telegram API и Google Drive API.

## Классы

### `Creds`

**Описание**: Класс `Creds` предназначен для хранения учетных данных, необходимых для работы с Telegram и Google Drive.

**Принцип работы**:
Класс `Creds` содержит статические переменные, которые хранят учетные данные. Эти переменные могут быть изменены для настройки бота и доступа к TeamDrive.

**Аттрибуты**:
- `TG_TOKEN` (str): Токен Telegram-бота.
- `TEAMDRIVE_FOLDER_ID` (str): Идентификатор папки TeamDrive.
- `TEAMDRIVE_ID` (str): Идентификатор TeamDrive.

**Методы**: Нет

**Примеры**

```python
# Пример использования класса Creds
creds = Creds()
creds.TG_TOKEN = "your_telegram_bot_token"
creds.TEAMDRIVE_FOLDER_ID = "your_teamdrive_folder_id"
creds.TEAMDRIVE_ID = "your_teamdrive_id"