# Конфигурационные параметры и текстовые константы для Google Drive Uploader Bot

## Обзор

Этот модуль содержит набор конфигурационных параметров и текстовых констант, используемых в Google Drive Uploader Bot. Он определяет настройки, такие как имя папки на Google Диске, учетные данные для Mega, текстовые сообщения для взаимодействия с пользователем, и другие параметры, необходимые для работы бота.

## Подробней

Модуль содержит переменные, определяющие основные параметры работы бота, такие как имя папки для загрузок на Google Диске (`drive_folder_name`), учетные данные для доступа к Mega (`MEGA_EMAIL`, `MEGA_PASSWORD`), а также текстовые сообщения, используемые для взаимодействия с пользователем через Telegram.

## Переменные

### `drive_folder_name`

**Описание**: Имя папки на Google Диске, в которую будут загружаться файлы.
**Тип**: `str`
**Значение по умолчанию**: `"GDriveUploaderBot"`

### `MEGA_EMAIL`

**Описание**: Email аккаунта Mega, используемый для скачивания файлов.
**Тип**: `str`
**Значение**: `"bearyan8@yandex.com"`

### `MEGA_PASSWORD`

**Описание**: Пароль от аккаунта Mega, используемый для скачивания файлов.
**Тип**: `str`
**Значение**: `"bearyan8@yandex.com"`

### `START`

**Описание**: Приветственное сообщение для пользователя при первом взаимодействии с ботом.
**Тип**: `str`
**Пример**:
```python
START = " Hi {}  \\nI am Drive Uploader Bot . Please Authorise To use me .By using /auth \\n\\n For more info /help \\n\\n Third-Party Website \\n Support Added /update \\n\\n For Bot Updates  \\n <a href =\'https://t.me/aryan_bots\'>Join Channel</a>\\nPlease Report Bugs  @aryanvikash"
```

### `HELP`

**Описание**: Сообщение с информацией о командах и возможностях бота.
**Тип**: `str`
**Пример**:
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
              500 KBps :(   ]
            * Dropbox links 
            *  Mega links
            
            + More On Its way:)
                
Bug Report @aryanvikash
        """
```

### `DP_DOWNLOAD`

**Описание**: Сообщение о начале загрузки файла с Dropbox.
**Тип**: `str`
**Значение**: `"Dropbox Link !! Downloading Started ..."`

### `OL_DOWNLOAD`

**Описание**: Сообщение о начале загрузки файла с Openload.
**Тип**: `str`
**Значение**: `"Openload Link !! Downloading Started ... \\n Openload Links Are Extremely Slow"`

### `PROCESSING`

**Описание**: Сообщение об обработке запроса пользователя.
**Тип**: `str`
**Значение**: `"Processing Your Request ...!!"`

### `DOWN_TWO`

**Описание**: Флаг, указывающий на необходимость двойной загрузки.
**Тип**: `bool`
**Значение**: `True`

### `DOWNLOAD`

**Описание**: Сообщение о начале загрузки файла.
**Тип**: `str`
**Значение**: `"Downloading Started ..."`

### `DOWN_MEGA`

**Описание**: Сообщение о начале загрузки файла с Mega.
**Тип**: `str`
**Значение**: `"Downloading Started... \\n  Mega Links are \\n Extremely Slow :("`

### `DOWN_COMPLETE`

**Описание**: Сообщение об успешном завершении загрузки файла.
**Тип**: `str`
**Значение**: `"Downloading complete !!"`

### `NOT_AUTH`

**Описание**: Сообщение об отсутствии авторизации у пользователя.
**Тип**: `str`
**Значение**: `"You Are Not Authorised To Using this Bot \\n\\n Please Authorise Me Using /auth  \\n\\n @aryanvikash"`

### `REVOKE_FAIL`

**Описание**: Сообщение о неудачной попытке отзыва авторизации.
**Тип**: `str`
**Значение**: `"You Are Already UnAuthorised \\n. Please Use /auth To Authorise \\n\\n report At @aryanvikash "`

### `AUTH_SUCC`

**Описание**: Сообщение об успешной авторизации пользователя.
**Тип**: `str`
**Значение**: `"Authorised Successfully  !! \\n\\n Now Send me A direct Link :)"`

### `ALREADY_AUTH`

**Описание**: Сообщение об уже выполненной авторизации пользователя.
**Тип**: `str`
**Значение**: `"You Are Already Authorised ! \\n\\n Wanna Change Drive Account? \\n\\n Use /revoke \\n\\n report At @aryanvikash "`

### `AUTH_URL`

**Описание**: URL для авторизации через Google Drive.
**Тип**: `str`
**Формат**: `\'<a href ="{}">Vist This Url</a> \\n Generate And Copy Your Google Drive Token And Send It To Me\'`

### `UPLOADING`

**Описание**: Сообщение о начале загрузки файла на Google Drive.
**Тип**: `str`
**Значение**: `"Download Complete !! \\n Uploading Your file"`

### `REVOKE_TOK`

**Описание**: Сообщение об успешном отзыве токена авторизации.
**Тип**: `str`
**Значение**: `" Your Token is Revoked Successfully !! \\n\\n Use /auth To Re-Authorise Your Drive Acc. "`

### `DOWN_PATH`

**Описание**: Путь к папке для сохранения загруженных файлов.
**Тип**: `str`
**Значение**: `"Downloads/"`

### `DOWNLOAD_URL`

**Описание**: Сообщение с информацией об успешной загрузке файла на Google Drive.
**Тип**: `str`
**Формат**: `"Your File Uploaded Successfully \\n\\n <b>Filename</b> : {} \\n\\n <b> Size</b> : {} MB \\n\\n <b>Download</b> {}"`

### `AUTH_ERROR`

**Описание**: Сообщение об ошибке авторизации.
**Тип**: `str`
**Значение**: `"AUTH Error !! Please  Send Me a  valid Token or Re - Authorise Me  \\n\\n report At @aryanvikash"`

### `OPENLOAD`

**Описание**: Флаг, указывающий на поддержку ссылок Openload.
**Тип**: `bool`
**Значение**: `True`

### `DROPBOX`

**Описание**: Флаг, указывающий на поддержку ссылок Dropbox.
**Тип**: `bool`
**Значение**: `True`

### `MEGA`

**Описание**: Флаг, указывающий на поддержку ссылок Mega.
**Тип**: `bool`
**Значение**: `True`

### `UPDATE`

**Описание**: Сообщение с информацией об обновлениях бота.
**Тип**: `str`
**Пример**:
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