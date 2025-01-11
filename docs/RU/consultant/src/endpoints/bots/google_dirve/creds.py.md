# Анализ кода модуля `creds`

**Качество кода**
8
 -  Плюсы
    - Код структурирован и понятен.
    - Есть комментарии, объясняющие назначение переменных.
 -  Минусы
    - Отсутствует документация модуля и класса.
    - Нет обработки ошибок.
    - Использованы двойные кавычки вместо одинарных в строковых значениях.

**Рекомендации по улучшению**

1.  Добавить документацию модуля и класса в формате RST.
2.  Использовать одинарные кавычки для строковых значений.
3.  Добавить импорты модуля `src.logger.logger` для логирования.
4.  Ввести проверку на наличие токенов и id, а также логирование.
5.  Изменить название класса на `CredsGoogleDrive` для более точного понимания назначения.

**Оптимизированный код**
```python
"""
Модуль для хранения учетных данных Google Drive.
===================================================

Этот модуль содержит класс :class:`CredsGoogleDrive`, который используется для хранения учетных данных, 
необходимых для работы с Google Drive API, включая токен Telegram бота, ID папки Team Drive и ID самого Team Drive.

Пример использования
--------------------

Пример использования класса `CredsGoogleDrive`:

.. code-block:: python

    creds = CredsGoogleDrive()
    print(creds.TG_TOKEN)
    print(creds.TEAMDRIVE_FOLDER_ID)
    print(creds.TEAMDRIVE_ID)
"""
from src.logger.logger import logger


class CredsGoogleDrive:
    """
    Класс для хранения учетных данных Google Drive.

    :param TG_TOKEN: Токен Telegram бота.
    :type TG_TOKEN: str
    :param TEAMDRIVE_FOLDER_ID: ID папки Team Drive.
    :type TEAMDRIVE_FOLDER_ID: str
    :param TEAMDRIVE_ID: ID Team Drive.
    :type TEAMDRIVE_ID: str

    Пример:

    .. code-block:: python

        creds = CredsGoogleDrive()
        print(creds.TG_TOKEN)
        print(creds.TEAMDRIVE_FOLDER_ID)
        print(creds.TEAMDRIVE_ID)

    """
    # ENTER Your bot Token Here
    TG_TOKEN = ''

    #  Make Sure You Are Providing both value if you need Teamdrive upload
    # Because of pydrive And pydrive v2 Api

    # Folder Id Of Teamdrive
    TEAMDRIVE_FOLDER_ID = ''

    # Id of Team drive
    TEAMDRIVE_ID = ''

    # Example
    # TG_TOKEN = 'dkjfksdkffdkfdkfdj'
    # TEAMDRIVE_FOLDER_ID = '13v4MaZnBz-iEHlZ0gFXk7rh'
    # TEAMDRIVE_ID = '0APh6R4WVvguEUk9PV'

    def __post_init__(self):
        """
        Проверяет наличие необходимых токенов и ID.
        Если токен или ID отсутствуют, выводит предупреждение.
        """
        if not self.TG_TOKEN:
            logger.warning('TG_TOKEN не установлен')
        if not self.TEAMDRIVE_FOLDER_ID:
            logger.warning('TEAMDRIVE_FOLDER_ID не установлен')
        if not self.TEAMDRIVE_ID:
            logger.warning('TEAMDRIVE_ID не установлен')
```