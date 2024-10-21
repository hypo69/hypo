## \file ../src/credentials.py
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
import threading
import datetime
from pathlib import Path
from types import SimpleNamespace
from pykeepass import PyKeePass

import header
from header import __root__
from src.utils import j_loads,j_loads_ns
from src.logger import logger
from src.logger.exceptions import KeePassException, DefaultSettingsException

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class ProjectSettings(metaclass = SingletonMeta):
    """ `ProjectSettings` - Defines program launch parameters.
    A singleton class that stores the main parameters and settings of the project.
    Designed to ensure that only one instance of it exists in the program.
    """
    dev_null: str = 'nul' if Path().drive else '/dev/null'
    __root__: Path = Path(__root__)
    settings:SimpleNamespace = j_loads_ns(__root__ / 'src' / 'settings.json')
    path: SimpleNamespace = SimpleNamespace(
        root=Path(__root__),
        src=Path(__root__ / 'src'),
        bin=Path(__root__ / 'bin'),
        log=Path(__root__ / 'log'),
        tmp=Path(__root__ / 'tmp'),
        data=Path(__root__ / 'data'), 
        secrets = Path(__root__ / 'secrets'),
        # google_drive = Path(settings.google_drive),  
        google_drive = Path(__root__ / 'data'),       # <- ~~~~~~~~~ DEBUG
    )
    
    sys.path.extend([str(path.root), str(path.src)])
    
    credentials = SimpleNamespace(
        aliexpress=SimpleNamespace(
            api_key=None,
            secret=None,
            tracking_id=None,
            username=None,
            email=None,
            password=None
        ),
        presta = SimpleNamespace(
            translations=SimpleNamespace(
                server=None,        
                port=None,
                database=None,
                user=None,
                password=None,),
            client = [SimpleNamespace(                
                server=None,        
                port=None,
                database=None,
                user=None,
                password=None,)]
        ),
        openai=SimpleNamespace(api_key = None, assistant = SimpleNamespace(), project_api = None),
        gemini=SimpleNamespace(api_key = SimpleNamespace()),
        discord=SimpleNamespace(application_id = None, public_key = None, bot_token = None),
        telegram=SimpleNamespace( bot = SimpleNamespace()),
        smtp=[],
        facebook=[],
        gapi={} 
    )
    
    def __init__(self, project_root: str | None = 'hypotez', *attrs, **kwargs) -> None:
        """ Constructor"""
        self._load_credentials()
        """ @todo logic for project_root"""
        if project_root != 'hypotez':
            self.path.root = Path(project_root)
            self.path.src = Path(self.path.root, 'src')
            # Update other paths if necessary

    def _load_credentials(self) -> None:
        """ Loads credentials from the KeePass database"""
        kp = self._open_kp(3)
        if not kp:
            #raise KeePassException('Failed to open KeePass database')
            logger.error(" :( ")
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
        @param retry: Number of retries
        """
        #path = self.path.src /  'credentials.kdbx'
        while retry > 0:
            try:
                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), password=getpass.getpass('Enter KeePass master password: ').lower()) # <- `.lower()` for debug only!
                return kp
            except Exception as ex:
                logger.error(f"Failed to open KeePass database, {retry-1} retries left.", ex, False)
                retry -= 1
                if retry < 1:
                    logger.critical('Failed to open KeePass database after multiple attempts', exc_info=True)
                    sys.exit() 

    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """ Load Aliexpress API credentials from KeePass"""
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
            return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """ Load OpenAI credentials from KeePass"""
        try:
            entry = kp.find_groups(path=['openai']).entries[0]
            self.credentials.openai.api_key = entry.custom_properties.get('api_key', None)
            self.credentials.openai.project_api = entry.custom_properties.get('project_api', None)

            #setattr (self.credentials.openai, 'assistant', None)

            setattr( self.credentials.openai.assistant, 
                    'category_descriptions', 
                    entry.custom_properties.get('create_categories_with_description_from_product_titles', None))

            setattr( self.credentials.openai.assistant, 
                    'emil', 
                    entry.custom_properties.get('emil', None))

            setattr( self.credentials.openai.assistant, 
                    'kazarinov', 
                    entry.custom_properties.get('kazarinov', None))            

            
            return True
        except DefaultSettingsException as ex:
            logger.error("Failed to extract OpenAI credentials from KeePass", ex)
            return False

    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """ Load GoogleAI credentials from KeePass"""
        try:
            entries = kp.find_groups(path=['gemini']).entries

            for entry in entries:
                setattr(self.credentials.gemini, entry.title, entry.custom_properties.get('api_key', None))
            return True
        except DefaultSettingsException as ex:
            logger.error("Failed to extract GoogleAI credentials from KeePass", ex)
            return False

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """ Load Telegram credentials from KeePass"""
        try:
            entry = kp.find_groups(path=['telegram']).entries[0]
            setattr( self.credentials.telegram.bot, 
            'onela', 
            entry.custom_properties.get('onela', None))

            setattr( self.credentials.telegram.bot, 
            'kazarinov', 
            entry.custom_properties.get('kazarinov', None))

            setattr( self.credentials.telegram.bot, 
            'test', 
            entry.custom_properties.get('test', None))
            return True
        except DefaultSettingsException as ex:
            logger.error("Failed to extract Telegram credentials from KeePass", ex)
            return False

    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """ Load Discord credentials from KeePass"""
        try:
            entry = kp.find_groups(path=['discord']).entries[0]
            self.credentials.discord.application_id = entry.custom_properties.get('application_id', None)
            self.credentials.discord.public_key = entry.custom_properties.get('public_key', None)
            self.credentials.discord.bot_token = entry.custom_properties.get('bot_token', None)
            return True
        except DefaultSettingsException as ex:
            logger.error("Failed to extract Discord credentials from KeePass", ex)
            return False

    def _load_prestashop_credentials(self, kp: PyKeePass) -> bool:
        """ Load Prestashop credentials from KeePass"""
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
            return False
        
    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """ Load Translations credentials from KeePass"""
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
            return False
        
    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """ Load SMTP credentials from KeePass"""
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
            return False

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """ Load Facebook credentials from KeePass"""
        try:
            for entry in kp.find_groups(path=['facebook']).entries:
                self.credentials.facebook.append(SimpleNamespace(
                    app_id=entry.custom_properties.get('app_id', None),
                    app_secret=entry.custom_properties.get('app_secret', None),
                    access_token=entry.custom_properties.get('access_token', None),
                ))
            return True
        except DefaultSettingsException as ex:
            logger.error("Failed to extract Facebook credentials from KeePass", ex)
            return False



    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """ Load Google API credentials from KeePass"""
        try:
            entry = kp.find_groups(path=['google','gapi']).entries[0]
            self.credentials.gapi['api_key'] = entry.custom_properties.get('api_key', None)
            return True
        except DefaultSettingsException as ex:
            logger.error("Failed to extract GAPI credentials from KeePass", ex)
            return False
        
    @property
    def now(self) -> str:
        """  Returns a datestamp in the chosen format
        @details Returns a datestamp in the chosen format
        """
        ...
        dformat: str = '%Y%m%d%H%M'
        return datetime.datetime.now().strftime(dformat)
    
    ...
# Global instance of ProjectSettings
gs: ProjectSettings = ProjectSettings()
