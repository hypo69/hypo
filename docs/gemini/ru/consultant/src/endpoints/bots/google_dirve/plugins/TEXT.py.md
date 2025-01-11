# Анализ кода модуля TEXT

**Качество кода**
   - 7
   - Плюсы
        - Код содержит основные константы и сообщения для бота.
        - Есть разделение на константы для сообщений, путей и логических флагов.
   - Минусы
        - Отсутствует описание модуля.
        - Нет документации для переменных.
        - Использование двойных кавычек для строк в коде (не соответствует гайду).
        - Жестко заданные пути (не кроссплатформенно).
        - Отсутствие импортов.
        - Не соответствие PEP8.

**Рекомендации по улучшению**

1.  Добавить описание модуля.
2.  Добавить документацию для каждой переменной.
3.  Использовать одинарные кавычки для строк в коде.
4.  Использовать `Path` для путей.
5.  Добавить импорты для `Path`
6.  Привести код к PEP8.
7.  Добавить `logger` для логирования.
8.  Разнести константы по смыслу, например в `MESSAGE`, `PATH`, `FLAG`.

**Оптимизированный код**

```python
"""
Модуль TEXT содержит константы и сообщения для бота Google Drive Uploader.
=======================================================================

Этот модуль определяет все текстовые константы, пути и флаги, используемые
в боте для загрузки файлов на Google Drive. Он включает сообщения для
пользователей, пути к загрузкам и флаги для управления функциональностью бота.

"""
from pathlib import Path
from src.logger import logger

# Определение констант для бота
# ------------------------------------------------------------------------------
# Общие настройки
drive_folder_name = 'GDriveUploaderBot'  # Имя папки в Google Drive (опционально)

# Настройки Mega.nz
MEGA_EMAIL = 'bearyan8@yandex.com'  # Email для Mega.nz
MEGA_PASSWORD = 'bearyan8@yandex.com'  # Пароль для Mega.nz

# Константы для сообщений
# ------------------------------------------------------------------------------
class MESSAGE:
    """
     Содержит константы для сообщений, отправляемых пользователю
    """
    START = " Hi {}  \nI am Drive Uploader Bot . Please Authorise To use me .By using /auth \n\n For more info /help \n\n Third-Party Website \n Support Added /update \n\n For Bot Updates  \n <a href ='https://t.me/aryan_bots'>Join Channel</a>\nPlease Report Bugs  @aryanvikash"
    HELP = """   <b>AUTHORISE BOT</b> \n       Use  /auth Command Generate\n       Your Google Drive Token And \n       Send It To Bot  \n<b> You Wanna Change Your Login \n        Account ?</b> \n\n        You Can Use /revoke \n        command            \n<b>What I Can Do With This Bot? </b>\n            You Can Upload Any Internet\n            Files On Your google\n            Drive Account.\n<b> Links Supported By Bot</b>\n            * Direct Links \n            * Openload links [Max Speed \n              500 KBps :(   ]\n            * Dropbox links \n            *  Mega links\n            \n            + More On Its way:)\n                \nBug Report @aryanvikash\n        """
    DP_DOWNLOAD = 'Dropbox Link !! Downloading Started ...'
    OL_DOWNLOAD = 'Openload Link !! Downloading Started ... \\n Openload Links Are Extremely Slow'
    PROCESSING = 'Processing Your Request ...!!'
    DOWNLOAD = 'Downloading Started ...'
    DOWN_MEGA = 'Downloading Started... \\n  Mega Links are \\n Extremely Slow :('
    DOWN_COMPLETE = 'Downloading complete !!'
    NOT_AUTH = 'You Are Not Authorised To Using this Bot \\n\\n Please Authorise Me Using /auth  \\n\\n @aryanvikash'
    REVOKE_FAIL = 'You Are Already UnAuthorised \\n. Please Use /auth To Authorise \\n\\n report At @aryanvikash '
    AUTH_SUCC = 'Authorised Successfully  !! \\n\\n Now Send me A direct Link :)'
    ALREADY_AUTH = 'You Are Already Authorised ! \\n\\n Wanna Change Drive Account? \\n\\n Use /revoke \\n\\n report At @aryanvikash '
    AUTH_URL = '<a href ="{}">Vist This Url</a> \\n Generate And Copy Your Google Drive Token And Send It To Me'
    UPLOADING = 'Download Complete !! \\n Uploading Your file'
    REVOKE_TOK = ' Your Token is Revoked Successfully !! \\n\\n Use /auth To Re-Authorise Your Drive Acc. '
    DOWNLOAD_URL = 'Your File Uploaded Successfully \\n\\n <b>Filename</b> : {} \\n\\n <b> Size</b> : {} MB \\n\\n <b>Download</b> {}'
    AUTH_ERROR = 'AUTH Error !! Please  Send Me a  valid Token or Re - Authorise Me  \\n\\n report At @aryanvikash'
    UPDATE = """ <b> Update  on  27.07.2019</b>\n            * MEGA LINK added\n            * Error Handling Improved\n\n<b> Links Supported By Bot</b>\n            * Direct Links \n            * Openload links [Max Speed \n              500 KBps :(   ]\n            * Dropbox links \n            *  Mega links (only files)\n            \n            + More are in way:) """

# Константы для путей
# ------------------------------------------------------------------------------
class PATH:
    """
    Содержит константы для путей
    """
    DOWN_PATH = Path('Downloads/')  # Путь для загрузок

# Логические флаги
# ------------------------------------------------------------------------------
class FLAG:
    """
    Содержит логические флаги
    """
    DOWN_TWO = True  # Флаг для двойной загрузки
    OPENLOAD = True  # Флаг для поддержки Openload
    DROPBOX = True  # Флаг для поддержки Dropbox
    MEGA = True  # Флаг для поддержки Mega.nz

```