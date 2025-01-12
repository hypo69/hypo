# Модуль `creds.py`

## Обзор

Модуль `creds.py` содержит класс `Creds`, предназначенный для хранения учетных данных, таких как токен Telegram бота и идентификаторы Google Drive (папки и тимдрайва). Эти данные используются для настройки и аутентификации при работе с Telegram ботом и Google Drive API.

## Оглавление

- [Классы](#классы)
  - [`Creds`](#creds)

## Классы

### `Creds`

**Описание**: Класс для хранения учетных данных, необходимых для работы с Telegram ботом и Google Drive API.

**Атрибуты**:

- `TG_TOKEN` (str): Токен Telegram бота.
- `TEAMDRIVE_FOLDER_ID` (str): Идентификатор папки на Google Team Drive.
- `TEAMDRIVE_ID` (str): Идентификатор Google Team Drive.