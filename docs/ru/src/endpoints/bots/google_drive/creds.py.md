# Модуль для хранения учетных данных

## Обзор

Модуль `creds.py` предназначен для хранения учетных данных, необходимых для работы с Telegram ботом и Google Drive API. Он содержит класс `Creds`, в котором определены атрибуты для хранения токена Telegram бота, ID папки TeamDrive и ID TeamDrive.

## Подробнее

Этот модуль предоставляет централизованное место для хранения и управления учетными данными, что упрощает их использование в других частях проекта. Модуль позволяет настроить загрузку файлов в TeamDrive, предоставляя соответствующие параметры.

## Классы

### `Creds`

**Описание**: Класс `Creds` предназначен для хранения учетных данных, используемых в проекте.

**Принцип работы**: Класс определяет статические атрибуты, которые содержат учетные данные, необходимые для работы с Telegram ботом и Google Drive API. Это позволяет избежать жесткого кодирования учетных данных непосредственно в коде и упрощает их изменение при необходимости.

**Атрибуты**:
- `TG_TOKEN` (str): Токен Telegram бота.
- `TEAMDRIVE_FOLDER_ID` (str): ID папки TeamDrive.
- `TEAMDRIVE_ID` (str): ID TeamDrive.

## Примеры

```python
from src.endpoints.bots.google_drive.creds import Creds

# Пример использования атрибутов класса Creds
TG_TOKEN = Creds.TG_TOKEN
TEAMDRIVE_FOLDER_ID = Creds.TEAMDRIVE_FOLDER_ID
TEAMDRIVE_ID = Creds.TEAMDRIVE_ID

print(f"TG_TOKEN: {TG_TOKEN}")
print(f"TEAMDRIVE_FOLDER_ID: {TEAMDRIVE_FOLDER_ID}")
print(f"TEAMDRIVE_ID: {TEAMDRIVE_ID}")