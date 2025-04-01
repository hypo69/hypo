# Модуль конфигурации и текстовых сообщений для Google Drive Uploader Bot

## Обзор

Этот модуль содержит конфигурационные параметры и текстовые сообщения, используемые в Google Drive Uploader Bot. Он определяет различные переменные, такие как имена папок, учетные данные, текстовые сообщения для различных состояний и операций бота.

## Подробней

Модуль содержит настройки для авторизации, загрузки и обработки файлов. Он также включает текстовые сообщения для информирования пользователя о статусе операций.
Этот код используется для определения констант и настроек, необходимых для работы бота, таких как имя папки на Google Диске, учетные данные для Mega, текстовые сообщения для различных этапов работы бота и пути для загрузки файлов.

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

**Описание**: Email аккаунта Mega.

### `MEGA_PASSWORD`

```python
MEGA_PASSWORD = "bearyan8@yandex.com"
```

**Описание**: Пароль от аккаунта Mega.

### `START`

```python
START = " Hi {}  \nI am Drive Uploader Bot . Please Authorise To use me .By using /auth \n\n For more info /help \n\n Third-Party Website \n Support Added /update \n\n For Bot Updates  \n <a href ='https://t.me/aryan_bots'>Join Channel</a>\nPlease Report Bugs  @aryanvikash"
```

**Описание**: Приветственное сообщение бота при старте.
Содержит инструкции по авторизации и использованию бота, а также ссылки на канал с обновлениями и контакты для сообщения об ошибках.

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

**Описание**: Справочное сообщение бота.
Содержит информацию о командах авторизации, смены аккаунта, возможностях бота и поддерживаемых типах ссылок.

### `DP_DOWNLOAD`

```python
DP_DOWNLOAD = "Dropbox Link !! Downloading Started ..."
```

**Описание**: Сообщение о начале загрузки файла из Dropbox.

### `OL_DOWNLOAD`

```python
OL_DOWNLOAD = "Openload Link !! Downloading Started ... \n Openload Links Are Extremely Slow"
```

**Описание**: Сообщение о начале загрузки файла из Openload.
Указывает на низкую скорость загрузки с Openload.

### `PROCESSING`

```python
PROCESSING = "Processing Your Request ...!!"
```

**Описание**: Сообщение об обработке запроса пользователя.

### `DOWN_TWO`

```python
DOWN_TWO = True
```

**Описание**: Флаг, определяющий, нужно ли выполнять двойную загрузку (возможно, для проверки). Значение всегда `True`.

### `DOWNLOAD`

```python
DOWNLOAD = "Downloading Started ..."
```

**Описание**: Сообщение о начале загрузки файла.

### `DOWN_MEGA`

```python
DOWN_MEGA = "Downloading Started... \n  Mega Links are \n Extremely Slow :("
```

**Описание**: Сообщение о начале загрузки файла из Mega.
Указывает на низкую скорость загрузки с Mega.

### `DOWN_COMPLETE`

```python
DOWN_COMPLETE = "Downloading complete !!"
```

**Описание**: Сообщение об успешном завершении загрузки файла.

### `NOT_AUTH`

```python
NOT_AUTH = "You Are Not Authorised To Using this Bot \n\n Please Authorise Me Using /auth  \n\n @aryanvikash"
```

**Описание**: Сообщение об отсутствии авторизации пользователя.
Предлагает авторизоваться с помощью команды `/auth`.

### `REVOKE_FAIL`

```python
REVOKE_FAIL = "You Are Already UnAuthorised \n. Please Use /auth To Authorise \n\n report At @aryanvikash "
```

**Описание**: Сообщение об ошибке при попытке отмены авторизации.
Указывает, что пользователь уже не авторизован.

### `AUTH_SUCC`

```python
AUTH_SUCC = "Authorised Successfully  !! \n\n Now Send me A direct Link :)"
```

**Описание**: Сообщение об успешной авторизации пользователя.
Предлагает отправить прямую ссылку для загрузки.

### `ALREADY_AUTH`

```python
ALREADY_AUTH = "You Are Already Authorised ! \n\n Wanna Change Drive Account? \n\n Use /revoke \n\n report At @aryanvikash "
```

**Описание**: Сообщение о том, что пользователь уже авторизован.
Предлагает использовать команду `/revoke` для смены аккаунта.

### `AUTH_URL`

```python
AUTH_URL = '<a href ="{}">Vist This Url</a> \n Generate And Copy Your Google Drive Token And Send It To Me'
```

**Описание**: Шаблон сообщения с URL для авторизации в Google Drive.
Содержит инструкцию по генерации токена и отправке его боту.

### `UPLOADING`

```python
UPLOADING = "Download Complete !! \n Uploading Your file"
```

**Описание**: Сообщение о начале загрузки файла на Google Drive.

### `REVOKE_TOK`

```python
REVOKE_TOK = " Your Token is Revoked Successfully !! \n\n Use /auth To Re-Authorise Your Drive Acc. "
```

**Описание**: Сообщение об успешной отмене авторизации.
Предлагает повторно авторизоваться с помощью команды `/auth`.

### `DOWN_PATH`

```python
DOWN_PATH = "Downloads/"  # Linux path
```

**Описание**: Путь к папке для загрузок.
Указан путь для Linux.

### `DOWNLOAD_URL`

```python
DOWNLOAD_URL = "Your File Uploaded Successfully \n\n <b>Filename</b> : {} \n\n <b> Size</b> : {} MB \n\n <b>Download</b> {}"
```

**Описание**: Шаблон сообщения об успешной загрузке файла на Google Drive.
Содержит информацию об имени файла, размере и ссылке для скачивания.

### `AUTH_ERROR`

```python
AUTH_ERROR = "AUTH Error !! Please  Send Me a  valid Token or Re - Authorise Me  \n\n report At @aryanvikash"
```

**Описание**: Сообщение об ошибке авторизации.
Предлагает отправить валидный токен или повторно авторизоваться.

### `OPENLOAD`

```python
OPENLOAD = True
```

**Описание**: Флаг, указывающий, поддерживается ли загрузка с Openload. Значение всегда `True`.

### `DROPBOX`

```python
DROPBOX = True
```

**Описание**: Флаг, указывающий, поддерживается ли загрузка с Dropbox. Значение всегда `True`.

### `MEGA`

```python
MEGA = True
```

**Описание**: Флаг, указывающий, поддерживается ли загрузка с Mega. Значение всегда `True`.

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

**Описание**: Сообщение об обновлении бота.
Содержит информацию о добавленных функциях и улучшении обработки ошибок.