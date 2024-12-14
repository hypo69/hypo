# Анализ кода модуля `credentials.py`

**Качество кода**
7/10
-   Плюсы
    -   Используется `pydantic` для валидации настроек.
    -   Применяется паттерн Singleton для класса `ProgramSettings`.
    -   Удобное использование `SimpleNamespace` для хранения конфигурационных данных.
    -   Код разбит на логические блоки и функции, что облегчает чтение.
-   Минусы
    -   Не везде используется `logger.error` для обработки исключений, вместо этого используется `print` и `...`.
    -   Не все функции имеют docstring в формате reStructuredText (RST).
    -   Много мест с `...` для пропуска кода, которые могут быть источниками ошибок.
    -   Использование `getpass.getpass` внутри `_open_kp` без вывода приглашения пользователю может привести к неожиданному поведению.
    -   Дублирование кода при загрузке разных типов учетных данных.
    -   Отсутствует обработка ошибок при чтении `password.txt`

**Рекомендации по улучшению**

1.  **Использование `logger.error`**: Заменить все `print` и `...` в блоках `except` на `logger.error`. Добавить информацию об ошибках (текст и исключение).
2.  **Документация RST**: Добавить недостающую документацию в формате RST ко всем функциям, методам и классам.
3.  **Обработка исключений**: Вместо `...` использовать конкретную логику обработки ошибок или, как минимум, логгировать их.
4.  **Чтение пароля из файла**: Использовать `try-except` при чтении пароля из файла, чтобы обрабатывать возможные ошибки (например, если файла нет).
5.  **Унификация загрузки учетных данных**: Создать общий метод для загрузки учетных данных, чтобы избежать дублирования кода.
6.  **Улучшение обработки пароля**: Улучшить способ получения пароля из `password.txt` или через `getpass`, например, добавив логику проверки наличия файла или приглашение для ввода пароля.
7.  **Удалить магические значения**: Заменить  магические значения на константы.
8.  **Удалить избыточные импорты**: Удалить дублирующиеся импорты `datetime`
9.  **Упростить конкатенацию строк**: Заменить f-строки на конкатенацию при формировании путей.
10. **Использовать Path** : Использовать Path в `__init__`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для управления настройками проекта и загрузки учетных данных.
========================================================================

Этот модуль содержит класс :class:`ProgramSettings`, который управляет глобальными
настройками проекта, включая пути, учетные данные и параметры API. Он также
обеспечивает загрузку учетных данных из базы данных KeePass и настройку путей
к различным ресурсам проекта.

Пример использования
--------------------

.. code-block:: python

    from src.credentials import ProgramSettings

    settings = ProgramSettings()
    print(settings.config.project_name)
"""

import getpass
import os
import sys
import json
import warnings
import socket
from dataclasses import dataclass, field
from pathlib import Path
from types import SimpleNamespace
from typing import Optional

from pydantic import BaseModel, Field
from pykeepass import PyKeePass

from src.check_release import check_latest_release
from src.logger.logger import logger
from src.logger.exceptions import (
    BinaryError,
    CredentialsError,
    DefaultSettingsException,
    HeaderChecksumError,
    KeePassException,
    PayloadChecksumError,
    UnableToSendToRecycleBin,
)
from src.utils.file import read_text_file
from src.utils.jjson import j_loads, j_loads_ns
from src.utils.printer import pprint
from datetime import datetime


MODE = 'dev'

PROJECT_MARKER_FILES = ('pyproject.toml', 'requirements.txt', '.git')
DEFAULT_RETRY_COUNT = 3
ENCODING = "utf-8"
def set_project_root(marker_files: tuple = PROJECT_MARKER_FILES) -> Path:
    """
    Определяет корневую директорию проекта.

    Ищет корневую директорию проекта, начиная с директории текущего файла,
    поднимаясь вверх и останавливаясь на первой директории, содержащей один из
    маркерных файлов.

    :param marker_files: Список файлов или директорий, определяющих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории или директория, где расположен скрипт.
    :rtype: Path
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__

def singleton(cls):
    """
    Декоратор для реализации Singleton.
    
    Этот декоратор гарантирует, что у класса будет только один экземпляр.

    :param cls: Класс, для которого нужно применить Singleton.
    :return: Функция-обёртка, которая возвращает единственный экземпляр класса.
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class ProgramSettings(BaseModel):
    """
    Класс настроек программы.

    Синглтон, хранящий основные параметры и настройки проекта.
    Используется для централизованного доступа к конфигурационным данным.
    """
    
    class Config:
        arbitrary_types_allowed = True

    host_name:str = socket.gethostname()
    print(f'host_name: {host_name}')

    base_dir: Path = Field(default_factory=lambda: set_project_root())
    config: SimpleNamespace = Field(default_factory=lambda: SimpleNamespace())
    credentials: SimpleNamespace = field(default_factory=lambda: SimpleNamespace(
        aliexpress=SimpleNamespace(
            api_key=None,
            secret=None,
            tracking_id=None,
            username=None,
            email=None,
            password=None
        ),
        presta=SimpleNamespace(
            translations=SimpleNamespace(
                server=None,
                port=None,
                database=None,
                user=None,
                password=None,
            ),
            client=[SimpleNamespace(
                server=None,
                port=None,
                database=None,
                user=None,
                password=None,
            )]
        ),
        openai=SimpleNamespace(
            api_key=None, 
            assistant_id=SimpleNamespace(), 
            project_api=None
        ),
        gemini=SimpleNamespace(api_key=None),
        rev_com=SimpleNamespace(client_api=None,
                                user_api=None),
        shutter_stock=SimpleNamespace(token=None),
        discord=SimpleNamespace(
            application_id=None, 
            public_key=None, 
            bot_token=None
        ),
        telegram=SimpleNamespace(
            bot=SimpleNamespace()
        ),
        smtp=[],
        facebook=[],
        gapi={}
    ))
    MODE: str = Field(default='dev')
    path: SimpleNamespace = Field(default_factory=lambda: SimpleNamespace(
        root = None,
        src = None,
        bin = None,
        log = None,
        tmp = None,
        data = None,
        secrets = None,
        google_drive = None,
        external_storage = None,
        tools = None,
        dev_null ='nul' if sys.platform == 'win32' else '/dev/null'
    ))
    

    def __init__(self, **kwargs):
        """
        Инициализирует объект `ProgramSettings`.

        Выполняет загрузку конфигурации, устанавливает пути и настраивает окружение
        после создания экземпляра класса.
        """
        super().__init__(**kwargs)

        # Загрузка конфигурации из файла config.json
        self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
        if not self.config:
            logger.error('Ошибка при загрузке настроек')
            ...
            return

        self.config.project_name = self.base_dir.name
        
        self.path = SimpleNamespace(
            root = Path(self.base_dir),
            bin = Path(self.base_dir / 'bin'), # <- тут бинарники (chrome, firefox, ffmpeg, ...)
            src = Path(self.base_dir) / 'src', # <- тут весь код
            endpoints = Path(self.base_dir) / 'src' / 'endpoints', # <- тут все клиенты
            secrets = Path(self.base_dir / 'secrets'),  # <- это папка с паролями и базой данных ! Ей нельзя попадать в гит!!!
            toolbox = Path(self.base_dir / 'toolbox'), # <- служебные утилиты

            log = Path(getattr(self.config.path, 'log', self.base_dir / 'log')), 
            tmp = Path(getattr(self.config.path, 'tmp', self.base_dir / 'tmp')),
            data = Path(getattr(self.config.path, 'data', self.base_dir / 'data')), # <- данные от endpoints (hypo69, kazarinov, prestashop, etc ...)
            google_drive = Path(getattr(self.config.path, 'google_drive', self.base_dir / 'google_drive')), # <- GOOGLE DRIVE ЧЕРЕЗ ЛОКАЛЬНЫЙ ДИСК (NOT API) 
            external_storage = Path(getattr(self.config.path, 'external_storage',  self.base_dir / 'external_storage') ),
        )

        if check_latest_release(self.config.git_user, self.config.git):
            ...  # Логика что делать когда есть новая версия hypo69 на github 

        self.MODE = self.config.mode

        # Paths to bin directories
        gtk_bin_dir = self.base_dir / 'bin' / 'gtk' / 'gtk-nsis-pack' / 'bin'
        ffmpeg_bin_dir = self.base_dir / 'bin' / 'ffmpeg' / 'bin'
        graphviz_bin_dir = self.base_dir / 'bin' / 'graphviz' / 'bin'
        wkhtmltopdf_bin_dir = self.base_dir / 'bin' / 'wkhtmltopdf' / 'files' / 'bin'

        for bin_path in [self.base_dir, gtk_bin_dir, ffmpeg_bin_dir, graphviz_bin_dir, wkhtmltopdf_bin_dir]:
            if bin_path not in sys.path:
                sys.path.insert(0, str(bin_path))

        os.environ['WEASYPRINT_DLL_DIRECTORIES'] = str(gtk_bin_dir)

        # Suppress GTK log output to the console
        warnings.filterwarnings("ignore", category=UserWarning)
        self._load_credentials()


    def _load_credentials(self) -> None:
        """
        Загружает учетные данные из KeePass.

        Вызывает методы для загрузки учетных данных для различных сервисов,
        таких как AliExpress, OpenAI, Discord и т.д.
        """
        kp = self._open_kp(DEFAULT_RETRY_COUNT)
        if not kp:
            print("Error :( ")
            ...
            sys.exit(1)

        if not self._load_aliexpress_credentials(kp):
            print('Failed to load Aliexpress credentials')

        if not self._load_openai_credentials(kp):
            print('Failed to load OpenAI credentials')

        if not self._load_gemini_credentials(kp):
            print('Failed to load GoogleAI credentials')

        if not self._load_discord_credentials(kp):
            print('Failed to load Discord credentials')

        if not self._load_telegram_credentials(kp):
            print('Failed to load Telegram credentials')

        if not self._load_PrestaShop_credentials(kp):
            print('Failed to load PrestaShop credentials')

        if not self._load_smtp_credentials(kp):
            print('Failed to load SMTP credentials')

        if not self._load_facebook_credentials(kp):
            print('Failed to load Facebook credentials')

        if not self._load_presta_translations_credentials(kp):
            print('Failed to load Translations credentials')

        if not self._load_gapi_credentials(kp):
            print('Failed to load GAPI credentials')

    def _open_kp(self, retry: int = DEFAULT_RETRY_COUNT) -> PyKeePass | None:
        """
        Открывает базу данных KeePass.

        :param retry: Количество попыток открытия базы данных.
        :type retry: int
        :return: Экземпляр PyKeePass или None в случае ошибки.
        :rtype: PyKeePass | None
        """
        while retry > 0:
            try:
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG ~~~~~~~ ФАЙЛ ПАРОЛЯ В ОТКРЫТОМ ВИДЕ ~~~~~~~~~~~~~~~~~~~~~~
                password_file = self.path.secrets / 'password.txt'
                password = None
                if password_file.exists():
                    try:
                        password = password_file.read_text(encoding=ENCODING).strip()
                    except Exception as e:
                         logger.error(f'Ошибка при чтении файла пароля: {e}')
                
                """password: содержит строку пароля в открытом виде. Можно удалить или сам файл или вытереть его содржимое """

                if not password:
                   password = getpass.getpass('Enter KeePass master password: ').lower()
                
                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), password=password)
                return kp
            except Exception as ex:
                logger.error(f"Failed to open KeePass database Exception: {ex}, {retry-1} retries left.")
                retry -= 1
                if retry < 1:
                    logger.critical('Failed to open KeePass database after multiple attempts', exc_info=True)
                    ...
                    sys.exit()
    
    def _load_credentials_from_group(self, kp: PyKeePass, path: list, target: SimpleNamespace,
                                     properties: dict, is_list: bool = False) -> bool:
        """
        Загружает учетные данные из группы KeePass.
    
        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :param path: Путь к группе в KeePass.
        :type path: list
        :param target: Целевой объект SimpleNamespace для хранения данных.
        :type target: SimpleNamespace
        :param properties: Словарь с именами свойств для загрузки.
        :type properties: dict
        :param is_list: Флаг, указывающий, является ли результат списком.
        :type is_list: bool
        :return: True, если загрузка успешна, иначе False.
        :rtype: bool
        """
        try:
            entries = kp.find_groups(path=path).entries
            if not entries:
                 logger.error(f"No entries found for path: {path}")
                 return False
            if is_list:
                for entry in entries:
                    entry_data = SimpleNamespace()
                    for key, prop in properties.items():
                         setattr(entry_data,key,entry.custom_properties.get(prop))
                    target.append(entry_data)
            else:
               
                if len(entries) == 1:
                   entry = entries[0]
                   for key, prop in properties.items():
                       setattr(target,key,entry.custom_properties.get(prop))
                   if hasattr(target, 'password'):
                       target.password = entry.password
                else:
                     for entry in entries:
                       for key, prop in properties.items():
                           setattr(target, key, entry.custom_properties.get(prop))

            return True
        except Exception as ex:
             logger.error(f"Failed to extract credentials from KeePass with path {path} Exception: {ex}")
             return False
    # Define methods for loading various credentials
    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные AliExpress из KeePass.
    
        :param kp: Экземпляр PyKeePass.
        :type kp: PyKeePass
        :return: True, если загрузка успешна, иначе False.
        :rtype: bool
        """
        properties = {
            "api_key":"api_key",
            "secret":"secret",
            "tracking_id":"tracking_id",
            "email":"email",
            "password":"password"
        }
        return self._load_credentials_from_group(kp, ['suppliers', 'aliexpress', 'api'], self.credentials.aliexpress, properties)

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные OpenAI из KeePass.
    
        :param kp: Экземпляр PyKeePass.
        :type kp: PyKeePass
        :return: True, если загрузка успешна, иначе False.
        :rtype: bool
        """
        try:
            openai_api_keys = kp.find_groups(path=['openai']).entries
            assistants = kp.find_groups(path=['openai','assistants']).entries
    
            for entry in openai_api_keys:
                setattr(self.credentials.openai, entry.title, entry.custom_properties.get('api_key', None))
                setattr(self.credentials.openai, entry.title, entry.custom_properties.get('project_api', None))
            for assistant in assistants:
                setattr(self.credentials.openai.assistant_id, assistant.title, assistant.custom_properties.get('assistant_id', None))
            return True
        except Exception as ex:
            logger.error(f"Failed to extract OpenAI credentials from KeePass {ex}")
            return False
            

    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Gemini из KeePass.
    
        :param kp: Экземпляр PyKeePass.
        :type kp: PyKeePass
        :return: True, если загрузка успешна, иначе False.
        :rtype: bool
        """
        properties = {
            "api_key":"api_key",
        }
        return self._load_credentials_from_group(kp, ['gemini'], self.credentials.gemini, properties)

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Telegram из KeePass.
    
        :param kp: Экземпляр PyKeePass.
        :type kp: PyKeePass
        :return: True, если загрузка успешна, иначе False.
        :rtype: bool
        """
        properties = {
            "token":"token",
        }
        return self._load_credentials_from_group(kp, ['telegram'], self.credentials.telegram, properties)


    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Discord из KeePass.
    
        :param kp: Экземпляр PyKeePass.
        :type kp: PyKeePass
        :return: True, если загрузка успешна, иначе False.
        :rtype: bool
        """
        properties = {
            "application_id":"application_id",
            "public_key":"public_key",
            "bot_token":"bot_token"
        }
        return self._load_credentials_from_group(kp, ['discord'], self.credentials.discord, properties)

    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
       """
       Загружает учетные данные PrestaShop из KeePass.
    
       :param kp: Экземпляр PyKeePass.
       :type kp: PyKeePass
       :return: True, если загрузка успешна, иначе False.
       :rtype: bool
       """
       properties = {
           "token": "token",
       }
       if not self._load_credentials_from_group(kp, ['prestashop'], self.credentials.telegram, properties):
          return False

       client_properties = {
          "api_key":"api_key",
          "api_domain":"api_domain",
          "db_server":"db_server",
          "db_user":"db_user",
          "db_password":"db_password",
       }
       return self._load_credentials_from_group(kp, ['prestashop', 'clients'], self.credentials.presta.client, client_properties, is_list=True)


    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
       """
       Загружает учетные данные для переводов PrestaShop из KeePass.
    
       :param kp: Экземпляр PyKeePass.
       :type kp: PyKeePass
       :return: True, если загрузка успешна, иначе False.
       :rtype: bool
       """
       properties = {
            "server":"server",
            "port":"port",
            "database":"database",
            "user":"user",
            "password":"password"
        }
       return self._load_credentials_from_group(kp, ['prestashop','translation'], self.credentials.presta.translations, properties)


    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
       """
       Загружает учетные данные SMTP из KeePass.
    
       :param kp: Экземпляр PyKeePass.
       :type kp: PyKeePass
       :return: True, если загрузка успешна, иначе False.
       :rtype: bool
       """
       properties = {
            "server":"server",
            "port":"port",
            "user":"user",
            "password":"password"
        }
       return self._load_credentials_from_group(kp, ['smtp'], self.credentials.smtp, properties, is_list=True)

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Facebook из KeePass.
    
        :param kp: Экземпляр PyKeePass.
        :type kp: PyKeePass
        :return: True, если загрузка успешна, иначе False.
        :rtype: bool
        """
        properties = {
            "app_id":"app_id",
            "app_secret":"app_secret",
            "access_token":"access_token"
        }
        return self._load_credentials_from_group(kp, ['facebook'], self.credentials.facebook, properties, is_list=True)

    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Google API из KeePass.
    
        :param kp: Экземпляр PyKeePass.
        :type kp: PyKeePass
        :return: True, если загрузка успешна, иначе False.
        :rtype: bool
        """
        properties = {
            "api_key":"api_key",
        }
        return self._load_credentials_from_group(kp, ['google','gapi'], self.credentials.gapi, properties)
    

    @property
    def now(self) -> str:
        """
        Возвращает текущую метку времени.

        Возвращает текущую метку времени в формате, определенном в конфигурации.
    
        :return: Текущая метка времени в формате год_месяц_день_часы_минуты_секунды_миллисекунды.
        :rtype: str
        """
        timestamp = datetime.now().strftime(self.config.timestamp_format)
        # Вернём только первые 3 цифры миллисекунд, т.к. %f возвращает микросекунды (6 цифр)
        return f"{timestamp[:-3]}"


# Global instance of ProgamSettings
gs: ProgramSettings = ProgramSettings()
```