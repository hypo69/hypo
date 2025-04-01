# Модуль конфигурации и текстовых констант для Google Drive Uploader Bot

## Обзор

Модуль содержит конфигурационные параметры и текстовые константы, используемые Google Drive Uploader Bot. Он определяет имена папок, учетные данные для Mega, приветственные сообщения, справку, уведомления о процессе загрузки и сообщения об ошибках.

## Подробней

Этот модуль предоставляет значения по умолчанию для различных параметров и сообщений, которые могут быть изменены в соответствии с потребностями пользователя. В частности, он содержит:

-   Имя папки на Google Диске (drive_folder_name).
-   Учетные данные для доступа к Mega (MEGA_EMAIL, MEGA_PASSWORD).
-   Текстовые константы для различных сообщений бота, таких как приветствие, справка, уведомления о процессе загрузки и сообщения об ошибках.
-   Флаги для включения/выключения поддержки Openload, Dropbox и Mega (OPENLOAD, DROPBOX, MEGA).
-   Путь для загрузки файлов (DOWN_PATH).
-   Сообщение об обновлении бота (UPDATE).

## Переменные

### `drive_folder_name`

```python
drive_folder_name = "GDriveUploaderBot"
```

**Описание**: Имя папки на Google Диске, в которой будут сохраняться загруженные файлы. Может быть изменено по желанию пользователя.

### `MEGA_EMAIL`

```python
MEGA_EMAIL = "bearyan8@yandex.com"
```

**Описание**: Email, используемый для доступа к аккаунту Mega. **Требуется** для работы с Mega ссылками.

### `MEGA_PASSWORD`

```python
MEGA_PASSWORD = "bearyan8@yandex.com"
```

**Описание**: Пароль для доступа к аккаунту Mega. **Требуется** для работы с Mega ссылками.

### `START`

```python
START = " Hi {}  \\nI am Drive Uploader Bot . Please Authorise To use me .By using /auth \\n\\n For more info /help \\n\\n Third-Party Website \\n Support Added /update \\n\\n For Bot Updates  \\n <a href =\'https://t.me/aryan_bots\'>Join Channel</a>\\nPlease Report Bugs  @aryanvikash"
```

**Описание**: Приветственное сообщение бота. Содержит информацию о необходимости авторизации, командах `/auth` и `/help`, а также ссылку на канал с обновлениями бота.

### `HELP`

```python
HELP = """   <b>AUTHORISE BOT</b> 
       Use  /auth Command Generate
       Your Google Drive Token And 
       Send It To Bot  
<b> You Wanna Change Your Login 
        Account ?</b> \\n
        You Can Use /revoke 
        command            
<b>What I Can Do With This Bot? </b>
            You Can Upload Any Internet
            Files On Your google
            Drive Account.
<b> Links Supported By Bot</b>
            * Direct Links 
            * Openload links [Max Speed 
              500 KBps :(   ]\n            * Dropbox links 
            *  Mega links
            
            + More On Its way:)
                
Bug Report @aryanvikash
        """
```

**Описание**: Справочное сообщение бота. Содержит информацию о командах `/auth` и `/revoke`, а также о поддерживаемых типах ссылок.

### `DP_DOWNLOAD`

```python
DP_DOWNLOAD = "Dropbox Link !! Downloading Started ..."
```

**Описание**: Сообщение, отображаемое при начале загрузки файла с Dropbox.

### `OL_DOWNLOAD`

```python
OL_DOWNLOAD = "Openload Link !! Downloading Started ... \\n Openload Links Are Extremely Slow"
```

**Описание**: Сообщение, отображаемое при начале загрузки файла с Openload. Предупреждает о низкой скорости загрузки.

### `PROCESSING`

```python
PROCESSING = "Processing Your Request ...!!"
```

**Описание**: Сообщение, отображаемое во время обработки запроса пользователя.

### `DOWN_TWO`

```python
DOWN_TWO = True
```

**Описание**: Булевая переменная, значение которой всегда `True`. Вероятно, определяет какую-то логику двойной загрузки, однако ее фактическое использование в коде неясно.

### `DOWNLOAD`

```python
DOWNLOAD = "Downloading Started ..."
```

**Описание**: Сообщение, отображаемое при начале загрузки файла.

### `DOWN_MEGA`

```python
DOWN_MEGA = "Downloading Started... \\n  Mega Links are \\n Extremely Slow :("
```

**Описание**: Сообщение, отображаемое при начале загрузки файла с Mega. Предупреждает о низкой скорости загрузки.

### `DOWN_COMPLETE`

```python
DOWN_COMPLETE = "Downloading complete !!"
```

**Описание**: Сообщение, отображаемое при завершении загрузки файла.

### `NOT_AUTH`

```python
NOT_AUTH = "You Are Not Authorised To Using this Bot \\n\\n Please Authorise Me Using /auth  \\n\\n @aryanvikash"
```

**Описание**: Сообщение, отображаемое при попытке использовать бота без авторизации.

### `REVOKE_FAIL`

```python
REVOKE_FAIL = "You Are Already UnAuthorised \\n. Please Use /auth To Authorise \\n\\n report At @aryanvikash "
```

**Описание**: Сообщение, отображаемое при попытке отменить авторизацию, когда пользователь уже не авторизован.

### `AUTH_SUCC`

```python
AUTH_SUCC = "Authorised Successfully  !! \\n\\n Now Send me A direct Link :)"
```

**Описание**: Сообщение, отображаемое при успешной авторизации пользователя.

### `ALREADY_AUTH`

```python
ALREADY_AUTH = "You Are Already Authorised ! \\n\\n Wanna Change Drive Account? \\n\\n Use /revoke \\n\\n report At @aryanvikash "
```

**Описание**: Сообщение, отображаемое при попытке авторизоваться, когда пользователь уже авторизован.

### `AUTH_URL`

```python
AUTH_URL = '<a href ="{}">Vist This Url</a> \\n Generate And Copy Your Google Drive Token And Send It To Me'
```

**Описание**: Сообщение, содержащее ссылку для получения токена Google Drive.

### `UPLOADING`

```python
UPLOADING = "Download Complete !! \\n Uploading Your file"
```

**Описание**: Сообщение, отображаемое при начале загрузки файла на Google Drive.

### `REVOKE_TOK`

```python
REVOKE_TOK = " Your Token is Revoked Successfully !! \\n\\n Use /auth To Re-Authorise Your Drive Acc. "
```

**Описание**: Сообщение, отображаемое при успешной отмене авторизации пользователя.

### `DOWN_PATH`

```python
DOWN_PATH = "Downloads/"  # Linux path
```

**Описание**: Путь к папке, в которую сохраняются загруженные файлы.

### `DOWNLOAD_URL`

```python
DOWNLOAD_URL = "Your File Uploaded Successfully \\n\\n <b>Filename</b> : {} \\n\\n <b> Size</b> : {} MB \\n\\n <b>Download</b> {}"
```

**Описание**: Сообщение, отображаемое при успешной загрузке файла на Google Drive. Содержит информацию об имени файла, размере и ссылке для скачивания.

### `AUTH_ERROR`

```python
AUTH_ERROR = "AUTH Error !! Please  Send Me a  valid Token or Re - Authorise Me  \\n\\n report At @aryanvikash"
```

**Описание**: Сообщение, отображаемое при ошибке авторизации.

### `OPENLOAD`

```python
OPENLOAD = True
```

**Описание**: Флаг, определяющий, поддерживаются ли ссылки Openload.

### `DROPBOX`

```python
DROPBOX = True
```

**Описание**: Флаг, определяющий, поддерживаются ли ссылки Dropbox.

### `MEGA`

```python
MEGA = True
```

**Описание**: Флаг, определяющий, поддерживаются ли ссылки Mega.

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

**Описание**: Сообщение об обновлении бота. Содержит информацию о добавленных функциях и поддерживаемых типах ссылок.