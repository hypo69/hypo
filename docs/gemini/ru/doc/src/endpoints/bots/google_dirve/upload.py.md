# Модуль `upload.py`

## Обзор

Модуль `upload.py` предназначен для загрузки файлов в Google Drive с использованием библиотеки PyDrive. Он поддерживает загрузку как в личный Google Drive, так и в Team Drive, если соответствующий идентификатор указан в настройках. Модуль также позволяет создавать папки, если они не существуют, и предоставлять публичный доступ к загруженным файлам.

## Содержание

1.  [Обзор](#обзор)
2.  [Импорт](#импорт)
3.  [Глобальные переменные](#глобальные-переменные)
4.  [Функции](#функции)
    -   [`upload`](#upload)

## Импорт

```python
import argparse
import json
import os
import os.path as path
import re
from creds import Creds
from plugins import TEXT
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
```

## Глобальные переменные

-   `FOLDER_MIME_TYPE`: MIME-тип для папок Google Drive (`'application/vnd.google-apps.folder'`).
-   `drive`: Объект `GoogleDrive` для взаимодействия с Google Drive API.
-   `http`: Объект для HTTP-запросов, используется PyDrive.
-   `initial_folder`: Переменная для хранения ID начальной папки (не используется в текущей версии).

## Функции

### `upload`

**Описание**: Функция загружает файл в Google Drive, создавая папку при необходимости и настраивая публичный доступ.

**Параметры**:

-   `filename` (str): Путь к файлу, который нужно загрузить.
-   `update` (any): Объект, содержащий информацию об обновлении от Telegram (используется для получения ID пользователя).
-   `context` (any): Контекст исполнения (не используется в текущей версии).
-   `parent_folder` (Optional[str], optional): Имя папки, в которую нужно загрузить файл. Если `None`, файл загружается в корень диска. По умолчанию `None`.

**Возвращает**:

-   `str | None`: Ссылка на загруженный файл или `None`, если загрузка не удалась.

**Вызывает исключения**:

-   `Exception`: Возникает при ошибках загрузки файла в Google Drive.

```python
def upload(filename: str, update, context, parent_folder: str = None) -> str | None:
    """
    Args:
        filename (str): Путь к файлу, который нужно загрузить.
        update (any): Объект, содержащий информацию об обновлении от Telegram (используется для получения ID пользователя).
        context (any): Контекст исполнения (не используется в текущей версии).
        parent_folder (Optional[str], optional): Имя папки, в которую нужно загрузить файл. Если `None`, файл загружается в корень диска. По умолчанию `None`.

    Returns:
         str | None: Ссылка на загруженный файл или `None`, если загрузка не удалась.

    Raises:
        Exception: Возникает при ошибках загрузки файла в Google Drive.
    """
```
```python
    FOLDER_MIME_TYPE = 'application/vnd.google-apps.folder'
    drive: GoogleDrive
    http = None
    initial_folder = None
    gauth: drive.GoogleAuth = GoogleAuth()

    ID = update.message.from_user.id
    ID = str(ID)
    gauth.LoadCredentialsFile(
        path.join(path.dirname(path.abspath(__file__)), ID))
```
```python
    if gauth.credentials is None:
        print("not Auth Users")
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
        gauth.SaveCredentialsFile(
            path.join(path.dirname(path.abspath(__file__)), ID))
    else:
        # Initialize the saved creds
        gauth.Authorize()
    drive = GoogleDrive(gauth)
    http = drive.auth.Get_Http_Object()
    if not path.exists(filename):
        print(f"Specified filename {filename} does not exist!")
        return
```
```python
    if not Creds.TEAMDRIVE_FOLDER_ID :
        if parent_folder:
                # Check the files and folers in the root foled
                file_list = drive.ListFile(
                    {'q': "\'root\' in parents and trashed=false"}).GetList()
                for file_folder in file_list:
                    if file_folder['title'] == parent_folder:
                        # Get the matching folder id
                        folderid = file_folder['id']
                        # print(folderid)
                        print("Folder Already Exist  !!  Trying To Upload")
                        # We need to leave this if it's done
                        break
                else:
                    # Create folder
                    folder_metadata = {'title': parent_folder,
                                       'mimeType': 'application/vnd.google-apps.folder'}
                    folder = drive.CreateFile(folder_metadata)
                    folder.Upload()
                    folderid = folder['id']
                    # Get folder info and print to screen
                    foldertitle = folder['title']
                    # folderid = folder['id']
                    print('title: %s, id: %s' % (foldertitle, folderid))
```
```python
    file_params = {'title': filename.split('/')[-1]}
    
    if Creds.TEAMDRIVE_FOLDER_ID :
        file_params['parents'] = [{"kind": "drive#fileLink", "teamDriveId": Creds.TEAMDRIVE_ID, "id":Creds.TEAMDRIVE_FOLDER_ID}]
        
    else:
        if parent_folder:
            file_params['parents'] = [{"kind": "drive#fileLink", "id": folderid}]
        
    file_to_upload = drive.CreateFile(file_params)
    file_to_upload.SetContentFile(filename)
    try:
        file_to_upload.Upload(param={"supportsTeamDrives" : True , "http": http})
        
        
    except Exception as ex:
        print("upload",ex)
    if not Creds.TEAMDRIVE_FOLDER_ID:
        file_to_upload.FetchMetadata()
        file_to_upload.InsertPermission({
        'type':  'anyone', 'value': 'anyone', 'role':  'reader', 'withLink': True
    })
        
    return file_to_upload['webContentLink']
```