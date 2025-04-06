# Модуль конфигурации и текстовых констант для бота Google Drive

## Обзор

Этот модуль содержит конфигурационные параметры и текстовые константы, используемые ботом для загрузки файлов в Google Drive. Он определяет настройки для авторизации, путей загрузки, сообщений для пользователя и поддержки различных типов ссылок.

## Подробней

Модуль служит централизованным местом для хранения настроек и текстовых сообщений, что упрощает изменение поведения бота и локализацию. Он определяет имя папки в Google Drive, учетные данные для Mega, приветственные и справочные сообщения, а также сообщения об ошибках и статусе загрузки.

## Переменные

### `drive_folder_name`

```python
drive_folder_name = "GDriveUploaderBot"
```

**Описание**: Имя папки в Google Drive, в которую будут загружаться файлы.

### `MEGA_EMAIL`

```python
MEGA_EMAIL = "bearyan8@yandex.com"
```

**Описание**: Email аккаунта Mega, используемый для загрузки файлов с Mega.

### `MEGA_PASSWORD`

```python
MEGA_PASSWORD = "bearyan8@yandex.com"
```

**Описание**: Пароль от аккаунта Mega, используемый для загрузки файлов с Mega.

### `START`

```python
START = " Hi {}  \nI am Drive Uploader Bot . Please Authorise To use me .By using /auth \n\n For more info /help \n\n Third-Party Website \n Support Added /update \n\n For Bot Updates  \n <a href ='https://t.me/aryan_bots'>Join Channel</a>\nPlease Report Bugs  @aryanvikash"
```

**Описание**: Приветственное сообщение для пользователя при запуске бота.

### `HELP`

```python
HELP = """   <b>AUTHORISE BOT</b> 
       Use  /auth Command Generate
       Your Google Drive Token And 
       Send It To Bot  
<b> You Wanna Change Your Login 
        Account ?</b> \n\n        You Can Use /revoke 
        command            
<b>What I Can Do With This Bot? </b>
            You Can Upload Any Internet
            Files On Your google
            Drive Account.\n<b> Links Supported By Bot</b>
            * Direct Links 
            * Openload links [Max Speed 
              500 KBps :(   ]\n            * Dropbox links 
            *  Mega links
            
            + More On Its way:)
                
Bug Report @aryanvikash
        """
```

**Описание**: Справочное сообщение для пользователя, содержащее инструкции по использованию бота.

### `DP_DOWNLOAD`

```python
DP_DOWNLOAD = "Dropbox Link !! Downloading Started ..."
```

**Описание**: Сообщение, отображаемое при начале загрузки файла с Dropbox.

### `OL_DOWNLOAD`

```python
OL_DOWNLOAD = "Openload Link !! Downloading Started ... \n Openload Links Are Extremely Slow"
```

**Описание**: Сообщение, отображаемое при начале загрузки файла с Openload.

### `PROCESSING`

```python
PROCESSING = "Processing Your Request ...!!"
```

**Описание**: Сообщение, отображаемое во время обработки запроса пользователя.

### `DOWN_TWO`

```python
DOWN_TWO = True
```

**Описание**: Флаг, определяющий необходимость загрузки двух файлов.

### `DOWNLOAD`

```python
DOWNLOAD = "Downloading Started ..."
```

**Описание**: Сообщение, отображаемое при начале загрузки файла.

### `DOWN_MEGA`

```python
DOWN_MEGA = "Downloading Started... \n  Mega Links are \n Extremely Slow :("
```

**Описание**: Сообщение, отображаемое при начале загрузки файла с Mega.

### `DOWN_COMPLETE`

```python
DOWN_COMPLETE = "Downloading complete !!"
```

**Описание**: Сообщение, отображаемое после завершения загрузки файла.

### `NOT_AUTH`

```python
NOT_AUTH = "You Are Not Authorised To Using this Bot \n\n Please Authorise Me Using /auth  \n\n @aryanvikash"
```

**Описание**: Сообщение, отображаемое, когда пользователь не авторизован.

### `REVOKE_FAIL`

```python
REVOKE_FAIL = "You Are Already UnAuthorised \n. Please Use /auth To Authorise \n\n report At @aryanvikash "
```

**Описание**: Сообщение, отображаемое при попытке отзыва авторизации, когда пользователь уже не авторизован.

### `AUTH_SUCC`

```python
AUTH_SUCC = "Authorised Successfully  !! \n\n Now Send me A direct Link :)"
```

**Описание**: Сообщение, отображаемое после успешной авторизации пользователя.

### `ALREADY_AUTH`

```python
ALREADY_AUTH = "You Are Already Authorised ! \n\n Wanna Change Drive Account? \n\n Use /revoke \n\n report At @aryanvikash "
```

**Описание**: Сообщение, отображаемое, когда пользователь уже авторизован.

### `AUTH_URL`

```python
AUTH_URL = '<a href ="{}">Vist This Url</a> \n Generate And Copy Your Google Drive Token And Send It To Me'
```

**Описание**: Сообщение, содержащее ссылку для авторизации в Google Drive.

### `UPLOADING`

```python
UPLOADING = "Download Complete !! \n Uploading Your file"
```

**Описание**: Сообщение, отображаемое во время загрузки файла в Google Drive.

### `REVOKE_TOK`

```python
REVOKE_TOK = " Your Token is Revoked Successfully !! \n\n Use /auth To Re-Authorise Your Drive Acc. "
```

**Описание**: Сообщение, отображаемое после успешного отзыва токена авторизации.

### `DOWN_PATH`

```python
DOWN_PATH = "Downloads/"  # Linux path
```

**Описание**: Путь к папке, в которую будут загружаться файлы.

### `DOWNLOAD_URL`

```python
DOWNLOAD_URL = "Your File Uploaded Successfully \n\n <b>Filename</b> : {} \n\n <b> Size</b> : {} MB \n\n <b>Download</b> {}"
```

**Описание**: Сообщение, отображаемое после успешной загрузки файла в Google Drive, содержащее информацию о файле и ссылку для скачивания.

### `AUTH_ERROR`

```python
AUTH_ERROR = "AUTH Error !! Please  Send Me a  valid Token or Re - Authorise Me  \n\n report At @aryanvikash"
```

**Описание**: Сообщение, отображаемое в случае ошибки авторизации.

### `OPENLOAD`

```python
OPENLOAD = True
```

**Описание**: Флаг, определяющий поддержку загрузки файлов с Openload.

### `DROPBOX`

```python
DROPBOX = True
```

**Описание**: Флаг, определяющий поддержку загрузки файлов с Dropbox.

### `MEGA`

```python
MEGA = True
```

**Описание**: Флаг, определяющий поддержку загрузки файлов с Mega.

### `UPDATE`

```python
UPDATE = """ <b> Update  on  27.07.2019</b>
            * MEGA LINK added
            * Error Handling Improved

<b> Links Supported By Bot</b>
            * Direct Links 
            * Openload links [Max Speed 
              500 KBps :(   ]\n            * Dropbox links 
            *  Mega links (only files)
            
            + More are in way:) """
```

**Описание**: Сообщение, содержащее информацию об обновлениях бота.

## Принцип работы

Этот модуль предоставляет набор констант, которые используются в различных частях бота. Например, `START` и `HELP` используются для отображения приветственного и справочного сообщений пользователю, а `AUTH_URL` используется для генерации ссылки для авторизации в Google Drive. Флаги `OPENLOAD`, `DROPBOX` и `MEGA` определяют, какие типы ссылок поддерживаются ботом. Путь загрузки `DOWN_PATH` указывает, куда сохранять загруженные файлы.

##
```
Конфигурация и константы
│
├─── drive_folder_name: Имя папки в Google Drive
├─── MEGA_EMAIL: Email аккаунта Mega
├─── MEGA_PASSWORD: Пароль от аккаунта Mega
├─── START: Приветственное сообщение
├─── HELP: Справочное сообщение
├─── DP_DOWNLOAD: Сообщение о начале загрузки с Dropbox
├─── OL_DOWNLOAD: Сообщение о начале загрузки с Openload
├─── PROCESSING: Сообщение об обработке запроса
├─── DOWN_TWO: Флаг для загрузки двух файлов
├─── DOWNLOAD: Сообщение о начале загрузки
├─── DOWN_MEGA: Сообщение о начале загрузки с Mega
├─── DOWN_COMPLETE: Сообщение о завершении загрузки
├─── NOT_AUTH: Сообщение о неавторизованном доступе
├─── REVOKE_FAIL: Сообщение о неуспешном отзыве авторизации
├─── AUTH_SUCC: Сообщение об успешной авторизации
├─── ALREADY_AUTH: Сообщение об уже выполненной авторизации
├─── AUTH_URL: URL для авторизации в Google Drive
├─── UPLOADING: Сообщение о загрузке файла
├─── REVOKE_TOK: Сообщение об успешном отзыве токена
├─── DOWN_PATH: Путь для сохранения загрузок
├─── DOWNLOAD_URL: Сообщение об успешной загрузке в Google Drive
├─── AUTH_ERROR: Сообщение об ошибке авторизации
├─── OPENLOAD: Флаг поддержки Openload
├─── DROPBOX: Флаг поддержки Dropbox
├─── MEGA: Флаг поддержки Mega
└─── UPDATE: Сообщение об обновлении бота
│
Логика работы
```
## Примеры

Пример использования констант для отображения сообщений пользователю:

```python
print(START.format("Username"))
print(HELP)
```

Пример использования флагов для определения поддержки типа ссылок:

```python
if MEGA:
    print("Mega links are supported")