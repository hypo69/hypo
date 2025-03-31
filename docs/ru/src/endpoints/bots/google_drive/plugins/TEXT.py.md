# Модуль конфигурации и текстовых констант для Google Drive Uploader Bot

## Обзор

Этот модуль содержит конфигурационные параметры и текстовые константы, используемые в Google Drive Uploader Bot. Он определяет имя папки на Google Диске, учетные данные для Mega.nz, текстовые сообщения для различных состояний и операций бота, а также флаги для включения/выключения поддержки определенных сервисов.

## Подробней

Модуль содержит переменные, которые задают основные параметры работы бота, такие как имя папки для загрузок, учетные данные для доступа к Mega.nz, текстовые сообщения для приветствия, помощи и уведомлений о различных этапах загрузки файлов. Также определены флаги для включения/выключения поддержки Openload, Dropbox и Mega.

## Переменные

### `drive_folder_name`

```python
drive_folder_name = "GDriveUploaderBot"
```

**Описание**: Имя папки на Google Диске, куда будут загружаться файлы.

### `MEGA_EMAIL`

```python
MEGA_EMAIL = "bearyan8@yandex.com"
```

**Описание**: Email, используемый для авторизации в сервисе Mega.

### `MEGA_PASSWORD`

```python
MEGA_PASSWORD = "bearyan8@yandex.com"
```

**Описание**: Пароль, используемый для авторизации в сервисе Mega.

### `START`

```python
START = " Hi {}  \nI am Drive Uploader Bot . Please Authorise To use me .By using /auth \n\n For more info /help \n\n Third-Party Website \n Support Added /update \n\n For Bot Updates  \n <a href ='https://t.me/aryan_bots'>Join Channel</a>\nPlease Report Bugs  @aryanvikash"
```

**Описание**: Приветственное сообщение бота, которое отображается при первом взаимодействии с пользователем.

### `HELP`

```python
HELP = """   <b>AUTHORISE BOT</b> 
       Use  /auth Command Generate
       Your Google Drive Token And 
       Send It To Bot  
<b> You Wanna Change Your Login 
        Account ?</b> \n

        You Can Use /revoke 
        command            
<b>What I Can Do With This Bot? </b>
            You Can Upload Any Internet
            Files On Your google
            Drive Account.
<b> Links Supported By Bot</b>
            * Direct Links 
            * Openload links [Max Speed 
              500 KBps :(   ]
            * Dropbox links 
            *  Mega links

            + More On Its way:)

Bug Report @aryanvikash
        """
```

**Описание**: Справочное сообщение бота, содержащее информацию о командах и поддерживаемых сервисах.

### `DP_DOWNLOAD`

```python
DP_DOWNLOAD = "Dropbox Link !! Downloading Started ..."
```

**Описание**: Уведомление о начале загрузки файла с Dropbox.

### `OL_DOWNLOAD`

```python
OL_DOWNLOAD = "Openload Link !! Downloading Started ... \n Openload Links Are Extremely Slow"
```

**Описание**: Уведомление о начале загрузки файла с Openload.

### `PROCESSING`

```python
PROCESSING = "Processing Your Request ...!!"
```

**Описание**: Уведомление о начале обработки запроса пользователя.

### `DOWN_TWO`

```python
DOWN_TWO = True
```

**Описание**: Флаг, указывающий на необходимость загрузки двух файлов (возможно, устаревшая переменная).

### `DOWNLOAD`

```python
DOWNLOAD = "Downloading Started ..."
```

**Описание**: Уведомление о начале загрузки файла.

### `DOWN_MEGA`

```python
DOWN_MEGA = "Downloading Started... \n  Mega Links are \n Extremely Slow :("
```

**Описание**: Уведомление о начале загрузки файла с Mega.

### `DOWN_COMPLETE`

```python
DOWN_COMPLETE = "Downloading complete !!"
```

**Описание**: Уведомление об успешном завершении загрузки файла.

### `NOT_AUTH`

```python
NOT_AUTH = "You Are Not Authorised To Using this Bot \n\n Please Authorise Me Using /auth  \n\n @aryanvikash"
```

**Описание**: Сообщение об ошибке, которое отображается, если пользователь не авторизован.

### `REVOKE_FAIL`

```python
REVOKE_FAIL = "You Are Already UnAuthorised \n. Please Use /auth To Authorise \n\n report At @aryanvikash "
```

**Описание**: Сообщение об ошибке, которое отображается, если пользователь пытается отозвать авторизацию, когда она уже отсутствует.

### `AUTH_SUCC`

```python
AUTH_SUCC = "Authorised Successfully  !! \n\n Now Send me A direct Link :)"
```

**Описание**: Уведомление об успешной авторизации пользователя.

### `ALREADY_AUTH`

```python
ALREADY_AUTH = "You Are Already Authorised ! \n\n Wanna Change Drive Account? \n\n Use /revoke \n\n report At @aryanvikash "
```

**Описание**: Уведомление о том, что пользователь уже авторизован.

### `AUTH_URL`

```python
AUTH_URL = '<a href ="{}">Vist This Url</a> \n Generate And Copy Your Google Drive Token And Send It To Me'
```

**Описание**: Сообщение, содержащее URL для авторизации в Google Drive.

### `UPLOADING`

```python
UPLOADING = "Download Complete !! \n Uploading Your file"
```

**Описание**: Уведомление о начале загрузки файла на Google Drive.

### `REVOKE_TOK`

```python
REVOKE_TOK = " Your Token is Revoked Successfully !! \n\n Use /auth To Re-Authorise Your Drive Acc. "
```

**Описание**: Уведомление об успешном отзыве токена авторизации.

### `DOWN_PATH`

```python
DOWN_PATH = "Downloads/"  # Linux path
```

**Описание**: Путь к папке, куда временно сохраняются загруженные файлы.

### `DOWNLOAD_URL`

```python
DOWNLOAD_URL = "Your File Uploaded Successfully \n\n <b>Filename</b> : {} \n\n <b> Size</b> : {} MB \n\n <b>Download</b> {}"
```

**Описание**: Сообщение, содержащее информацию об успешной загрузке файла на Google Drive.

### `AUTH_ERROR`

```python
AUTH_ERROR = "AUTH Error !! Please  Send Me a  valid Token or Re - Authorise Me  \n\n report At @aryanvikash"
```

**Описание**: Сообщение об ошибке авторизации.

### `OPENLOAD`

```python
OPENLOAD = True
```

**Описание**: Флаг, указывающий, включена ли поддержка загрузки файлов с Openload.

### `DROPBOX`

```python
DROPBOX = True
```

**Описание**: Флаг, указывающий, включена ли поддержка загрузки файлов с Dropbox.

### `MEGA`

```python
MEGA = True
```

**Описание**: Флаг, указывающий, включена ли поддержка загрузки файлов с Mega.

### `UPDATE`

```python
UPDATE = """ <b> Update  on  27.07.2019</b>
            * MEGA LINK added
            * Error Handling Improved

<b> Links Supported By Bot</b>
            * Direct Links 
            * Openload links [Max Speed 
              500 KBps :(   ]
            * Dropbox links 
            *  Mega links (only files)

            + More are in way:) """
```

**Описание**: Сообщение, содержащее информацию об обновлениях бота.