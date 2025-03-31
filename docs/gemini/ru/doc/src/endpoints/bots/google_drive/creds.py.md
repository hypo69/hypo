# Модуль для хранения учетных данных

## Обзор

Модуль содержит класс `Creds`, предназначенный для хранения учетных данных, таких как токен Telegram-бота, ID папки TeamDrive и ID TeamDrive. Это позволяет удобно хранить и использовать эти данные в других частях проекта.

## Подробней

Этот модуль предоставляет простой способ централизованного хранения учетных данных, необходимых для работы с Telegram Bot API и Google Drive API. Использование класса `Creds` позволяет избежать жесткого кодирования учетных данных непосредственно в коде, что повышает безопасность и упрощает управление конфигурацией.

## Классы

### `Creds`

**Описание**: Класс для хранения учетных данных.

**Как работает класс**:
Класс `Creds` содержит статические атрибуты, которые хранят токен Telegram-бота (`TG_TOKEN`), ID папки TeamDrive (`TEAMDRIVE_FOLDER_ID`) и ID TeamDrive (`TEAMDRIVE_ID`). Эти атрибуты предназначены для хранения и доступа к соответствующим учетным данным.

**Атрибуты**:
- `TG_TOKEN` (str): Токен Telegram-бота.
- `TEAMDRIVE_FOLDER_ID` (str): ID папки TeamDrive.
- `TEAMDRIVE_ID` (str): ID TeamDrive.

**Примеры**:

```python
# Пример использования класса Creds
creds = Creds()
creds.TG_TOKEN = "your_bot_token"
creds.TEAMDRIVE_FOLDER_ID = "your_teamdrive_folder_id"
creds.TEAMDRIVE_ID = "your_teamdrive_id"

# Получение значений
token = creds.TG_TOKEN
folder_id = creds.TEAMDRIVE_FOLDER_ID
teamdrive_id = creds.TEAMDRIVE_ID
```
```python
class Creds():
    # ENTER Your bot Token Here
    TG_TOKEN = ""
    
    
    
    #  Make Sure You Are Providing both value if you need Teamdrive upload
    # Because of pydrive And pydrive v2 Api
    
    #Folder Id Of Teamdrive
    TEAMDRIVE_FOLDER_ID = ""
    
    # Id of Team drive 
    TEAMDRIVE_ID = ""
    
    
    
    #Example 
    #TG_TOKEN = "dkjfksdkffdkfdkfdj"
    #TEAMDRIVE_FOLDER_ID = "13v4MaZnBz-iEHlZ0gFXk7rh"
    #TEAMDRIVE_ID = "0APh6R4WVvguEUk9PV"