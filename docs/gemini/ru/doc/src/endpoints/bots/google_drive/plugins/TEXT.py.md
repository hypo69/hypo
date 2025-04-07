# Модуль конфигурации и текстовых констант для Google Drive Uploader Bot

## Обзор

Этот модуль содержит конфигурационные параметры и текстовые константы, используемые в Google Drive Uploader Bot. Он определяет настройки, такие как имя папки на Google Диске, учетные данные Mega, приветственные сообщения, справку и другие текстовые элементы интерфейса бота.

## Подробней

Модуль содержит настройки для работы Google Drive Uploader Bot. Здесь хранятся основные параметры, такие как имя папки для загрузки на Google Диске, учетные данные для доступа к Mega, текстовые сообщения для различных команд и статусов, а также флаги, определяющие поддержку определенных типов ссылок. Этот модуль облегчает настройку и изменение поведения бота без необходимости изменения основного кода.

## Переменные

### `drive_folder_name`

```python
drive_folder_name = "GDriveUploaderBot"
```

Имя папки на Google Диске, в которую будут загружаться файлы. Это имя можно изменить по желанию.

### `MEGA_EMAIL`

```python
MEGA_EMAIL = "bearyan8@yandex.com"
```

Email для доступа к аккаунту Mega, используется для скачивания файлов с Mega. **Требуется для работы с Mega ссылками.**

### `MEGA_PASSWORD`

```python
MEGA_PASSWORD = "bearyan8@yandex.com"
```

Пароль для доступа к аккаунту Mega, используется для скачивания файлов с Mega. **Требуется для работы с Mega ссылками.**

### `START`

```python
START = " Hi {}  \\nI am Drive Uploader Bot . Please Authorise To use me .By using /auth \\n\\n For more info /help \\n\\n Third-Party Website \\n Support Added /update \\n\\n For Bot Updates  \\n <a href =\'https://t.me/aryan_bots\'>Join Channel</a>\\nPlease Report Bugs  @aryanvikash"
```

Приветственное сообщение, которое бот отправляет пользователю при первом взаимодействии. Содержит информацию о необходимости авторизации, командах и каналах поддержки.

### `HELP`

```python
HELP = """   <b>AUTHORISE BOT</b> \n       Use  /auth Command Generate\n       Your Google Drive Token And \n       Send It To Bot  \n<b> You Wanna Change Your Login \n        Account ?</b> \\n\n        You Can Use /revoke \n        command            \n<b>What I Can Do With This Bot? </b>\n            You Can Upload Any Internet\n            Files On Your google\n            Drive Account.\n<b> Links Supported By Bot</b>\n            * Direct Links \n            * Openload links [Max Speed \n              500 KBps :(   ]\n            * Dropbox links \n            *  Mega links\n            \n            + More On Its way:)\n                \nBug Report @aryanvikash\n        """
```

Текст справки, который бот отправляет в ответ на команду `/help`. Содержит инструкции по авторизации, использованию бота и список поддерживаемых типов ссылок.

### `DP_DOWNLOAD`

```python
DP_DOWNLOAD = "Dropbox Link !! Downloading Started ..."
```

Сообщение, отправляемое ботом при начале скачивания файла по ссылке Dropbox.

### `OL_DOWNLOAD`

```python
OL_DOWNLOAD = "Openload Link !! Downloading Started ... \\n Openload Links Are Extremely Slow"
```

Сообщение, отправляемое ботом при начале скачивания файла по ссылке Openload. Указывает на низкую скорость скачивания с Openload.

### `PROCESSING`

```python
PROCESSING = "Processing Your Request ...!!"
```

Сообщение о том, что запрос пользователя обрабатывается.

### `DOWN_TWO`

```python
DOWN_TWO = True
```

Флаг, указывающий, можно ли одновременно загружать два файла. 

### `DOWNLOAD`

```python
DOWNLOAD = "Downloading Started ..."
```

Сообщение, отправляемое ботом при начале скачивания файла.

### `DOWN_MEGA`

```python
DOWN_MEGA = "Downloading Started... \\n  Mega Links are \\n Extremely Slow :("
```

Сообщение, отправляемое ботом при начале скачивания файла по ссылке Mega. Указывает на низкую скорость скачивания с Mega.

### `DOWN_COMPLETE`

```python
DOWN_COMPLETE = "Downloading complete !!"
```

Сообщение об успешном завершении скачивания файла.

### `NOT_AUTH`

```python
NOT_AUTH = "You Are Not Authorised To Using this Bot \\n\\n Please Authorise Me Using /auth  \\n\\n @aryanvikash"
```

Сообщение об ошибке, отправляемое ботом, если пользователь не авторизован и пытается использовать функциональность бота.

### `REVOKE_FAIL`

```python
REVOKE_FAIL = "You Are Already UnAuthorised \\n. Please Use /auth To Authorise \\n\\n report At @aryanvikash "
```

Сообщение об ошибке, отправляемое ботом, если пользователь пытается отозвать авторизацию, но уже не авторизован.

### `AUTH_SUCC`

```python
AUTH_SUCC = "Authorised Successfully  !! \\n\\n Now Send me A direct Link :)"
```

Сообщение об успешной авторизации, отправляемое ботом после успешной авторизации пользователя.

### `ALREADY_AUTH`

```python
ALREADY_AUTH = "You Are Already Authorised ! \\n\\n Wanna Change Drive Account? \\n\\n Use /revoke \\n\\n report At @aryanvikash "
```

Сообщение, отправляемое ботом, если пользователь пытается авторизоваться, но уже авторизован.

### `AUTH_URL`

```python
AUTH_URL = \'<a href ="{}">Vist This Url</a> \\n Generate And Copy Your Google Drive Token And Send It To Me\'
```

Сообщение, содержащее ссылку для авторизации в Google Drive. Пользователь должен перейти по этой ссылке, получить токен и отправить его боту.

### `UPLOADING`

```python
UPLOADING = "Download Complete !! \\n Uploading Your file"
```

Сообщение, отправляемое ботом после завершения скачивания и перед началом загрузки файла на Google Диск.

### `REVOKE_TOK`

```python
REVOKE_TOK = " Your Token is Revoked Successfully !! \\n\\n Use /auth To Re-Authorise Your Drive Acc. "
```

Сообщение об успешном отзыве токена авторизации.

### `DOWN_PATH`

```python
DOWN_PATH = "Downloads/"  # Linux path
```

Путь к папке, в которую скачиваются файлы.  Указан путь для Linux.

### `DOWNLOAD_URL`

```python
DOWNLOAD_URL = "Your File Uploaded Successfully \\n\\n <b>Filename</b> : {} \\n\\n <b> Size</b> : {} MB \\n\\n <b>Download</b> {}"
```

Сообщение об успешной загрузке файла на Google Диск. Содержит имя файла, размер и ссылку для скачивания.

### `AUTH_ERROR`

```python
AUTH_ERROR = "AUTH Error !! Please  Send Me a  valid Token or Re - Authorise Me  \\n\\n report At @aryanvikash"
```

Сообщение об ошибке авторизации. Отправляется ботом, если предоставлен неверный токен.

### `OPENLOAD`

```python
OPENLOAD = True
```

Флаг, указывающий, поддерживаются ли ссылки Openload.

### `DROPBOX`

```python
DROPBOX = True
```

Флаг, указывающий, поддерживаются ли ссылки Dropbox.

### `MEGA`

```python
MEGA = True
```

Флаг, указывающий, поддерживаются ли ссылки Mega.

### `UPDATE`

```python
UPDATE = """ <b> Update  on  27.07.2019</b>\n            * MEGA LINK added\n            * Error Handling Improved\n\n<b> Links Supported By Bot</b>\n            * Direct Links \n            * Openload links [Max Speed \n              500 KBps :(   ]\n            * Dropbox links \n            *  Mega links (only files)\n            \n            + More are in way:) """
```

Текст с информацией об обновлениях бота и поддерживаемых типах ссылок.