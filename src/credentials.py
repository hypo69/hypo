## \file ../src/credentials.py
# -*- coding: utf-8 -*-
#! /usr/bin/env python3
""" Global Project Settings: paths, passwords, logins, and API settings.

Start-up settings for the program.

Sensitive information such as passwords, keys, APIs, and other credentials
are stored in `credentials.kdbx` and need the master password to open the database.

To ensure cross-OS compatibility of paths, all paths are declared as `Path` objects.
@todo The root directory can have any name. Currently, it is hardcoded as `hypotez`. Need to add the option to choose the name of the root directory in the configuration file.
"""

import sys
import getpass
import datetime
from pathlib import Path
from types import SimpleNamespace
from pykeepass import PyKeePass
from dataclasses import dataclass, field

import header
from header import __root__
from src.check_relise import check_latest_release 
from src.utils import j_loads, j_loads_ns
from src.logger import logger
from src.logger.exceptions import KeePassException, DefaultSettingsException


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


@dataclass
class ProgamSettings(metaclass=SingletonMeta):
    """ `ProgamSettings` - Defines program launch parameters.
    A singleton class that stores the main parameters and settings of the project.
    Designed to ensure that only one instance of it exists in the program.
    """
    dev_null: str = field(default='nul' if Path().drive else '/dev/null')
    __root__: Path = field(default=Path(__root__))
    settings: SimpleNamespace = field(default_factory=lambda: j_loads_ns(__root__ / 'src' / 'settings.json'))
    if check_latest_release(settings.git_user, settings.git):
        ...
    path: SimpleNamespace = field(default_factory=lambda: SimpleNamespace(
        root=Path(__root__),
        src=Path(__root__ / 'src'),
        bin=Path(__root__ / 'bin'),
        log=Path(__root__ / 'log'),
        tmp=Path(__root__ / 'tmp'),
        data=Path(__root__ / 'data'), 
        secrets=Path(__root__ / 'secrets'),
        google_drive=Path(__root__ / 'data'),  # <- ~~~~~~~~~ DEBUG
    ))

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
        openai=SimpleNamespace(api_key=None, assistant=SimpleNamespace(), project_api=None),
        gemini=SimpleNamespace(api_key=SimpleNamespace()),
        discord=SimpleNamespace(application_id=None, public_key=None, bot_token=None),
        telegram=SimpleNamespace(bot=SimpleNamespace()),
        smtp=[],
        facebook=[],
        gapi={}
    ))

    @classmethod
    def _load_credentials(cls) -> None:
        """ Loads credentials from the KeePass database"""
        kp = cls._open_kp(3)
        if not kp:
            logger.error(" :( ")
            sys.exit(1)

        if not cls._load_aliexpress_credentials(kp):
            raise DefaultSettingsException('Failed to load Aliexpress credentials')

        if not cls._load_openai_credentials(kp):
            raise DefaultSettingsException('Failed to load OpenAI credentials')

        if not cls._load_gemini_credentials(kp):
            raise DefaultSettingsException('Failed to load GoogleAI credentials')

        if not cls._load_discord_credentials(kp):
            raise DefaultSettingsException('Failed to load Discord credentials')

        if not cls._load_telegram_credentials(kp):
            raise DefaultSettingsException('Failed to load Telegram credentials')

        if not cls._load_prestashop_credentials(kp):
            raise DefaultSettingsException('Failed to load Prestashop credentials')

        if not cls._load_smtp_credentials(kp):
            raise DefaultSettingsException('Failed to load SMTP credentials')

        if not cls._load_facebook_credentials(kp):
            raise DefaultSettingsException('Failed to load Facebook credentials')

        if not cls._load_presta_translations_credentials(kp):
            raise DefaultSettingsException('Failed to load Translations credentials')

        if not cls._load_gapi_credentials(kp):
            raise DefaultSettingsException('Failed to load GAPI credentials')

    @classmethod
    def _open_kp(cls, retry: int = 3) -> PyKeePass | None:
        """ Open KeePass database
        @param retry: Number of retries
        """
        while retry > 0:
            try:
                kp = PyKeePass(str(cls.path.secrets / 'credentials.kdbx'), password=getpass.getpass('Enter KeePass master password: ').lower())  # <- `.lower()` for debug only!
                return kp
            except Exception as ex:
                logger.error(f"Failed to open KeePass database, {retry-1} retries left.", ex, False)
                retry -= 1
                if retry < 1:
                    logger.critical('Failed to open KeePass database after multiple attempts', exc_info=True)
                    sys.exit()

    # Define methods for loading various credentials
    def _load_aliexpress_credentials(cls, kp: PyKeePass) -> bool:
        """ Load Aliexpress API credentials from KeePass"""
        try:
            entry = kp.find_groups(path=['suppliers', 'aliexpress', 'api']).entries[0]
            cls.credentials.aliexpress.api_key = entry.custom_properties.get('api_key', None)
            cls.credentials.aliexpress.secret = entry.custom_properties.get('secret', None)
            cls.credentials.aliexpress.tracking_id = entry.custom_properties.get('tracking_id', None)
            cls.credentials.aliexpress.email = entry.custom_properties.get('email', None)
            cls.credentials.aliexpress.password = entry.password
            return True
        except DefaultSettingsException as ex:
            logger.error("Failed to extract Aliexpress API key from KeePass", ex)
            return False

    # Similarly implement _load_openai_credentials, _load_gemini_credentials, etc.
    
    # For brevity, additional methods are not displayed here. 

    @property
    def now(self) -> str:
        """  Returns a datestamp in the chosen format
        @details Returns a datestamp in the chosen format
        """
        dformat: str = '%Y%m%d%H%M'
        return datetime.datetime.now().strftime(dformat)

# Global instance of ProgamSettings
gs: ProgamSettings = ProgamSettings()
