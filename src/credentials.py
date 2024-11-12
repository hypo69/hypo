## \file hypotez/src/credentials.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src """
""" Global Project Settings: paths, passwords, logins, and API settings.

Start-up settings for the program.

Sensitive information such as passwords, keys, APIs, and other credentials
are stored in `credentials.kdbx` and need the master password to open the database.

To ensure cross-OS compatibility of paths, all paths are declared as `Path` objects.
@todo The root directory can have any name. Currently, it is hardcoded as `hypotez`. Need to add the option to choose the name of the root directory in the configuration file.
"""
# Встроенные библиотеки
import datetime
import getpass
import os
import sys
import json
import warnings
from dataclasses import dataclass, field
from pathlib import Path
from types import SimpleNamespace
from typing import Optional

# Сторонние библиотеки
from pydantic import BaseModel, Field

from pykeepass import PyKeePass

# Локальные модули
from src.check_relise import check_latest_release
from src.logger import logger
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

def singleton(cls):
    """Декоратор для реализации Singleton."""
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class ProgramSettings(BaseModel):
    """ 
    `ProgramSettings` - класс настроек программы.
    
    Синглтон, хранящий основные параметры и настройки проекта.
    """
    
    model_config = {
        "arbitrary_types_allowed": True
    }

    base_dir: Path = Field(default_factory=lambda: Path(__file__).resolve().parent.parent)
    settings: SimpleNamespace = Field(default_factory=lambda: SimpleNamespace())
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
            assistant=SimpleNamespace(), 
            project_api=None
        ),
        gemini=SimpleNamespace(api_key=SimpleNamespace()),
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
    mode: str = Field(default='debug')
    path: SimpleNamespace = Field(default_factory=lambda: SimpleNamespace(
        root = None,
        src = None,
        bin = None,
        log = None,
        tmp = None,
        data = None,
        secrets = None,
        google_drive = None,
        dev_null ='nul' if sys.platform == 'win32' else '/dev/null'
    ))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Ваш код для выполнения __post_init__

        """! Выполняет инициализацию после создания экземпляра класса."""
        
        def _get_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')):
            """! Находит корневую директорию проекта, начиная с текущей директории."""
            current_path = Path(__file__).resolve().parent
            for parent in [current_path] + list(current_path.parents):
                if any((parent / marker).exists() for marker in marker_files):
                    return parent
            return current_path

        self.base_dir = _get_project_root()
        sys.path.append(str(self.base_dir))
        self.settings = j_loads_ns(Path(self.base_dir) / 'src' / 'settings.json')

        self.settings.project_name = self.base_dir.name
        
        self.path = SimpleNamespace(
            root=Path(self.base_dir),
            src=Path(self.base_dir) / 'src',
            bin=Path(self.base_dir) / 'bin',
            log=Path(self.base_dir) / 'log',
            tmp=Path(self.base_dir) / 'tmp',
            data=Path(self.base_dir) / 'data',
            secrets=Path(self.base_dir) / 'secrets',
            google_drive=Path(self.base_dir) / 'data',  # <- DEBUG path
        )

        if check_latest_release(self.settings.git_user, self.settings.git):
            ...  # Логика для новой версии

        self.mode = self.settings.mode

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
        """! Загружает учетные данные из настроек."""

        kp = self._open_kp(3)
        if not kp:
            logger.error(" :( ")
            ...
            sys.exit(1)

        if not self._load_aliexpress_credentials(kp):
            raise DefaultSettingsException('Failed to load Aliexpress credentials')

        if not self._load_openai_credentials(kp):
            raise DefaultSettingsException('Failed to load OpenAI credentials')

        if not self._load_gemini_credentials(kp):
            raise DefaultSettingsException('Failed to load GoogleAI credentials')

        if not self._load_discord_credentials(kp):
            raise DefaultSettingsException('Failed to load Discord credentials')

        if not self._load_telegram_credentials(kp):
            raise DefaultSettingsException('Failed to load Telegram credentials')

        if not self._load_prestashop_credentials(kp):
            raise DefaultSettingsException('Failed to load Prestashop credentials')

        if not self._load_smtp_credentials(kp):
            raise DefaultSettingsException('Failed to load SMTP credentials')

        if not self._load_facebook_credentials(kp):
            raise DefaultSettingsException('Failed to load Facebook credentials')

        if not self._load_presta_translations_credentials(kp):
            raise DefaultSettingsException('Failed to load Translations credentials')

        if not self._load_gapi_credentials(kp):
            raise DefaultSettingsException('Failed to load GAPI credentials')

    def _open_kp(self, retry: int = 3) -> PyKeePass | None:
        """ Open KeePass database
        Args:
            retry (int): Number of retries
        """
        while retry > 0:
            try:
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                password:str = read_text_file( self.path.secrets / 'password.txt') or None
                """password: содержит строку пароля в открытом виде. Можно удалить или сам файл или вытереть его содржимое """
                
                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), 
                               password = password or getpass.getpass(pprint('Enter KeePass master password: ', text_color='ligt_blue', bg_color='dark_gray').lower()))
               
                return kp
            except Exception as ex:
                logger.error(f"Failed to open KeePass database, {retry-1} retries left.", ex, False)
                ...
                retry -= 1
                if retry < 1:
                    logger.critical('Failed to open KeePass database after multiple attempts', exc_info=True)
                    ...
                    sys.exit()

    # Define methods for loading various credentials
    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """ Load Aliexpress API credentials from KeePass
        Args:
            kp (PyKeePass): The KeePass database instance.

        Returns:
            bool: True if loading was successful, False otherwise.
        """
        try:
            entry = kp.find_groups(path=['suppliers', 'aliexpress', 'api']).entries[0]
            self.credentials.aliexpress.api_key = entry.custom_properties.get('api_key', None)
            self.credentials.aliexpress.secret = entry.custom_properties.get('secret', None)
            self.credentials.aliexpress.tracking_id = entry.custom_properties.get('tracking_id', None)
            self.credentials.aliexpress.email = entry.custom_properties.get('email', None)
            self.credentials.aliexpress.password = entry.password
            return True
        except DefaultSettingsException as ex:
            logger.error("Failed to extract Aliexpress API key from KeePass", ex)
            ...
            return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """ Load OpenAI credentials from KeePass
        Args:
            kp (PyKeePass): The KeePass database instance.

        Returns:
            bool: True if loading was successful, False otherwise.
        """
        try:
            entries = kp.find_groups(path=['openai']).entries

            for entry in entries:
                setattr(self.credentials.openai, entry.title, entry.custom_properties.get('api_key', None))
            return True
        except DefaultSettingsException as ex:
            ...
            logger.error("Failed to extract GoogleAI credentials from KeePass", ex)
            return           


    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """ Load GoogleAI credentials from KeePass
        Args:
            kp (PyKeePass): The KeePass database instance.

        Returns:
            bool: True if loading was successful, False otherwise.
        """
        try:
            entries = kp.find_groups(path=['gemini']).entries

            for entry in entries:
                setattr(self.credentials.gemini, entry.title, entry.custom_properties.get('api_key', None))
            return True
        except DefaultSettingsException as ex:
            ...
            logger.error("Failed to extract GoogleAI credentials from KeePass", ex)
            return 

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """Load Telegram credentials from KeePass.

        Args:
            kp (PyKeePass): The KeePass database instance.

        Returns:
            bool: True if loading was successful, False otherwise.
        """
        try:
            entries = kp.find_groups(path=['telegram']).entries
            for entry in entries:
                setattr(self.credentials.telegram, entry.title, entry.custom_properties.get('token', None))
            return True
        except DefaultSettingsException as ex:
            logger.error("Failed to extract Telegram credentials from KeePass", ex)
            ...
            return 

    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """ Load Discord credentials from KeePass
        Args:
            kp (PyKeePass): The KeePass database instance.

        Returns:
            bool: True if loading was successful, False otherwise.
        """
        try:
            entry = kp.find_groups(path=['discord']).entries[0]
            self.credentials.discord.application_id = entry.custom_properties.get('application_id', None)
            self.credentials.discord.public_key = entry.custom_properties.get('public_key', None)
            self.credentials.discord.bot_token = entry.custom_properties.get('bot_token', None)
            return True
        except DefaultSettingsException as ex:
            logger.error("Failed to extract Discord credentials from KeePass", ex)
            ...
            return 

    def _load_prestashop_credentials(self, kp: PyKeePass) -> bool:
        """ Load Prestashop credentials from KeePass
        Args:
            kp (PyKeePass): The KeePass database instance.

        Returns:
            bool: True if loading was successful, False otherwise.
        """
        try:
            entries = kp.find_groups(path=['prestashop']).entries
            for entry in entries:
                setattr(self.credentials.telegram, entry.title, entry.custom_properties.get('token', None))
            return True
        except DefaultSettingsException as ex:
            logger.error("Failed to extract Telegram credentials from KeePass", ex)
            ...
            return 
        try:
            for entry in kp.find_groups(path=['prestashop', 'clients']).entries:
                self.credentials.presta.client.append(SimpleNamespace(
                    api_key=entry.custom_properties.get('api_key', None),
                    api_domain=entry.custom_properties.get('api_domain', None),
                    db_server=entry.custom_properties.get('db_server', None),
                    db_user=entry.custom_properties.get('db_user', None),
                    db_password=entry.custom_properties.get('db_password', None),
                ))
            return True
        except DefaultSettingsException as ex:
            logger.error("Failed to extract Prestashop credentials from KeePass", ex)
            ...
            return 
        
    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """ Load Translations credentials from KeePass
        Args:
            kp (PyKeePass): The KeePass database instance.

        Returns:
            bool: True if loading was successful, False otherwise.
        """
        try:
            entry = kp.find_groups(path=['prestashop','translation']).entries[0]
            self.credentials.presta.translations.server = entry.custom_properties.get('server', None)
            self.credentials.presta.translations.port = entry.custom_properties.get('port', None)
            self.credentials.presta.translations.database = entry.custom_properties.get('database', None)
            self.credentials.presta.translations.user = entry.custom_properties.get('user', None)
            self.credentials.presta.translations.password = entry.custom_properties.get('password', None)
            return True
        except DefaultSettingsException as ex:
            logger.error("Failed to extract Translations credentials from KeePass", ex)
            ...
            return 
        
    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """ Load SMTP credentials from KeePass
        Args:
            kp (PyKeePass): The KeePass database instance.

        Returns:
            bool: True if loading was successful, False otherwise.
        """
        try:
            for entry in kp.find_groups(path=['smtp']).entries:
                self.credentials.smtp.append(SimpleNamespace(
                    server=entry.custom_properties.get('server', None),
                    port=entry.custom_properties.get('port', None),
                    user=entry.custom_properties.get('user', None),
                    password=entry.custom_properties.get('password', None),
                ))
            return True
        except DefaultSettingsException as ex:
            logger.error("Failed to extract SMTP credentials from KeePass", ex)
            ...
            return 

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """ Load Facebook credentials from KeePass
        Args:
            kp (PyKeePass): The KeePass database instance.

        Returns:
            bool: True if loading was successful, False otherwise.
        """
        try:
            for entry in kp.find_groups(path=['facebook']).entries:
                self.credentials.facebook.append(SimpleNamespace(
                    app_id=entry.custom_properties.get('app_id', None),
                    app_secret=entry.custom_properties.get('app_secret', None),
                    access_token=entry.custom_properties.get('access_token', None),
                ))
            return True
        except DefaultSettingsException as ex:
            ...
            logger.error("Failed to extract Facebook credentials from KeePass", ex)
            return 

    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """ Load Google API credentials from KeePass
        Args:
            kp (PyKeePass): The KeePass database instance.

        Returns:
            bool: True if loading was successful, False otherwise.
        """
        try:
            entry = kp.find_groups(path=['google','gapi']).entries[0]
            self.credentials.gapi['api_key'] = entry.custom_properties.get('api_key', None)
            return True
        except DefaultSettingsException as ex:
            logger.error("Failed to extract GAPI credentials from KeePass", ex) 
            ...
            return 

    @property
    def now(self, dformat: str = '%Y%m%d%H%M') -> str:
        """ Returns the current timestamp in the specified format and sets up paths for binary files.

        This method returns a string representing the current timestamp in the format `YYYYMMDDHHMM`. It also checks and adds the necessary binary file paths to the system if they haven't been added already.

        Args:
            dformat (str, optional): The format for the timestamp. Defaults to `'%Y%m%d%H%M'`.

        Returns:
            str: The current timestamp in string format.
        """
    
        return datetime.datetime.now().strftime(dformat)


# Global instance of ProgamSettings
gs: ProgramSettings = ProgramSettings()
