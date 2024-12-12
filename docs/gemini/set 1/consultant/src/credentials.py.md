# Анализ кода модуля `credentials.py`

**Качество кода: 7/10**
   -  Плюсы
        -  Используется `pydantic` для валидации настроек.
        -  Применяется паттерн Singleton для класса `ProgramSettings`.
        -  Используется `PyKeePass` для безопасного хранения учетных данных.
        -  Код структурирован, логические блоки разделены на функции.
   -  Минусы
        -  Используется много `print` для логирования, что не подходит для продакшн окружения.
        -  Не всегда используется `logger` для обработки ошибок.
        -  Присутствуют множественные блоки `try-except` с `...`, которые нужно конкретизировать.
        -  В некоторых местах используется `sys.exit()` для завершения программы, что не всегда корректно.
        -  Не все функции и классы имеют docstring в формате reStructuredText.
        -  Много вложенных `SimpleNamespace` что затрудняет чтение кода.
        -  В некоторых местах есть дублирование кода.
        -  Используется чтение пароля из файла в открытом виде.

**Рекомендации по улучшению**

1.  **Логирование:** Заменить все `print` на `logger.info`, `logger.error` и `logger.debug` для структурированного логирования.
2.  **Обработка ошибок:**  Вместо общих `try-except` с `...`  использовать `logger.error`  и  обработку конкретных исключений.
3.  **Docstrings:** Добавить docstrings в формате reStructuredText для всех функций, методов и классов.
4.  **Удалить:** чтение пароля из файла `password.txt` в открытом виде.
5.  **Использовать j_loads:** использовать  `j_loads` из `src.utils.jjson` вместо стандартного `json.load`.
6.  **Улучшить структуру данных:** Упростить использование `SimpleNamespace`, возможно, заменив их на более структурированные dataclass или pydantic модели.
7. **Использовать `Path`:** Убедиться, что все пути в коде используют `Path` для обеспечения кроссплатформенности.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для управления настройками и учетными данными проекта
=========================================================================================

Этот модуль содержит класс :class:`ProgramSettings`, который используется
для загрузки и управления настройками, путями и учетными данными проекта.
Модуль использует :mod:`pydantic` для валидации настроек и :mod:`PyKeePass`
для безопасного хранения учетных данных.

Пример использования
--------------------

Пример использования класса `ProgramSettings`:

.. code-block:: python

    gs = ProgramSettings()
    print(gs.config.project_name)
"""

import datetime
from datetime import datetime
import getpass
import os
import sys
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
# from src.logger.exceptions import ( # не используется но указан в задании
#     BinaryError,
#     CredentialsError,
#     DefaultSettingsException,
#     HeaderChecksumError,
#     KeePassException,
#     PayloadChecksumError,
#     UnableToSendToRecycleBin,
# )
from src.utils.file import read_text_file
from src.utils.jjson import j_loads, j_loads_ns
from src.utils.printer import pprint


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.

    Функция ищет корневой каталог проекта, начиная с текущего каталога файла,
    двигаясь вверх по дереву каталогов и останавливаясь на первом каталоге,
    содержащем любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, идентифицирующих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если найден, иначе - каталог, где находится скрипт.
    :rtype: Path
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


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
    Класс :class:`ProgramSettings` для хранения настроек программы.

    Синглтон, хранящий основные параметры и настройки проекта.
    """

    class Config:
        arbitrary_types_allowed = True

    host_name: str = socket.gethostname()
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
        root=None,
        src=None,
        bin=None,
        log=None,
        tmp=None,
        data=None,
        secrets=None,
        google_drive=None,
        external_storage=None,
        tools=None,
        dev_null='nul' if sys.platform == 'win32' else '/dev/null'
    ))

    def __init__(self, **kwargs):
        """Инициализирует объект :class:`ProgramSettings`.

        Выполняет инициализацию после создания экземпляра класса, загружая
        конфигурационные файлы, устанавливая пути и загружая учетные данные.

        :param kwargs: Произвольные именованные аргументы.
        """
        super().__init__(**kwargs)

        # код загружает конфигурацию из файла config.json
        try:
            self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
            if not self.config:
                logger.error('Ошибка при загрузке настроек')
                return
        except Exception as ex:
            logger.error(f"Ошибка при загрузке файла конфигурации: {ex}")
            return


        self.config.project_name = self.base_dir.name
        # код устанавливает пути к директориям проекта
        self.path = SimpleNamespace(
            root=Path(self.base_dir),
            bin=Path(self.base_dir / 'bin'),  # <- тут бинарники (chrome, firefox, ffmpeg, ...)
            src=Path(self.base_dir) / 'src',  # <- тут весь код
            endpoints=Path(self.base_dir) / 'src' / 'endpoints',  # <- тут все клиенты
            secrets=Path(self.base_dir / 'secrets'),  # <- это папка с паролями и базой данных ! Ей нельзя попадать в гит!!!
            toolbox=Path(self.base_dir / 'toolbox'),  # <- служебные утилиты

            log=Path(getattr(self.config.path, 'log', self.base_dir / 'log')),
            tmp=Path(getattr(self.config.path, 'tmp', self.base_dir / 'tmp')),
            data=Path(getattr(self.config.path, 'data', self.base_dir / 'data')),  # <- данные от endpoints (hypo69, kazarinov, prestashop, etc ...)
            google_drive=Path(getattr(self.config.path, 'google_drive', self.base_dir / 'google_drive')),  # <- GOOGLE DRIVE ЧЕРЕЗ ЛОКАЛЬНЫЙ ДИСК (NOT API)
            external_storage=Path(getattr(self.config.path, 'external_storage', self.base_dir / 'external_storage')),
        )
        #  код проверяет наличие новой версии на github
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
        """Загружает учетные данные из KeePass.

        Вызывает методы для загрузки учетных данных для различных сервисов,
        таких как Aliexpress, OpenAI, Discord и других.

        """
        kp = self._open_kp(3)
        if not kp:
            logger.error("Не удалось открыть базу данных KeePass")
            sys.exit(1)

        if not self._load_aliexpress_credentials(kp):
            logger.error('Не удалось загрузить учетные данные Aliexpress')

        if not self._load_openai_credentials(kp):
            logger.error('Не удалось загрузить учетные данные OpenAI')

        if not self._load_gemini_credentials(kp):
            logger.error('Не удалось загрузить учетные данные GoogleAI')

        if not self._load_discord_credentials(kp):
            logger.error('Не удалось загрузить учетные данные Discord')

        if not self._load_telegram_credentials(kp):
            logger.error('Не удалось загрузить учетные данные Telegram')

        if not self._load_PrestaShop_credentials(kp):
            logger.error('Не удалось загрузить учетные данные PrestaShop')

        if not self._load_smtp_credentials(kp):
            logger.error('Не удалось загрузить учетные данные SMTP')

        if not self._load_facebook_credentials(kp):
            logger.error('Не удалось загрузить учетные данные Facebook')

        if not self._load_presta_translations_credentials(kp):
            logger.error('Не удалось загрузить учетные данные Translations')

        if not self._load_gapi_credentials(kp):
            logger.error('Не удалось загрузить учетные данные GAPI')

    def _open_kp(self, retry: int = 3) -> Optional[PyKeePass]:
        """Открывает базу данных KeePass.

        Пытается открыть базу данных KeePass с заданным количеством попыток.

        :param retry: Количество попыток открытия.
        :type retry: int
        :return: Экземпляр :class:`PyKeePass`, если удалось открыть базу данных, иначе - :obj:`None`.
        :rtype: Optional[PyKeePass]
        """
        while retry > 0:
            try:
                #  код запрашивает пароль от KeePass
                password = getpass.getpass(prompt='Enter KeePass master password: ').lower()
                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), password=password)

                return kp
            except Exception as ex:
                logger.error(f"Не удалось открыть базу данных KeePass. Осталось попыток: {retry-1}", exc_info=True)
                retry -= 1
                if retry < 1:
                    logger.critical('Не удалось открыть базу данных KeePass после нескольких попыток', exc_info=True)
                    sys.exit(1)
        return None

    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Aliexpress API из KeePass.

        :param kp: Экземпляр :class:`PyKeePass`.
        :type kp: PyKeePass
        :return: :obj:`True`, если загрузка прошла успешно, иначе - :obj:`False`.
        :rtype: bool
        """
        try:
            entry = kp.find_groups(path=['suppliers', 'aliexpress', 'api']).entries[0]
            self.credentials.aliexpress.api_key = entry.custom_properties.get('api_key', None)
            self.credentials.aliexpress.secret = entry.custom_properties.get('secret', None)
            self.credentials.aliexpress.tracking_id = entry.custom_properties.get('tracking_id', None)
            self.credentials.aliexpress.email = entry.custom_properties.get('email', None)
            self.credentials.aliexpress.password = entry.password
            return True
        except Exception as ex:
            logger.error(f"Не удалось извлечь API-ключ Aliexpress из KeePass: {ex}")
            return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные OpenAI из KeePass.

        :param kp: Экземпляр :class:`PyKeePass`.
        :type kp: PyKeePass
        :return: :obj:`True`, если загрузка прошла успешно, иначе - :obj:`False`.
        :rtype: bool
        """
        try:
            openai_api_keys = kp.find_groups(path=['openai']).entries
            assistants = kp.find_groups(path=['openai', 'assistants']).entries

            for entry in openai_api_keys:
                setattr(self.credentials.openai, entry.title, entry.custom_properties.get('api_key', None))
                setattr(self.credentials.openai, entry.title, entry.custom_properties.get('project_api', None))
            for assistant in assistants:
                setattr(self.credentials.openai.assistant_id, assistant.title,
                        assistant.custom_properties.get('assistant_id', None))
            return True
        except Exception as ex:
            logger.error(f"Не удалось извлечь учетные данные OpenAI из KeePass: {ex}")
            return False

    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные GoogleAI из KeePass.

        :param kp: Экземпляр :class:`PyKeePass`.
        :type kp: PyKeePass
        :return: :obj:`True`, если загрузка прошла успешно, иначе - :obj:`False`.
        :rtype: bool
        """
        try:
            entries = kp.find_groups(path=['gemini']).entries

            for entry in entries:
                setattr(self.credentials.gemini, entry.title, entry.custom_properties.get('api_key', None))
            return True
        except Exception as ex:
            logger.error(f"Не удалось извлечь учетные данные GoogleAI из KeePass: {ex}")
            return False

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Telegram из KeePass.

        :param kp: Экземпляр :class:`PyKeePass`.
        :type kp: PyKeePass
        :return: :obj:`True`, если загрузка прошла успешно, иначе - :obj:`False`.
        :rtype: bool
        """
        try:
            entries = kp.find_groups(path=['telegram']).entries
            for entry in entries:
                setattr(self.credentials.telegram, entry.title, entry.custom_properties.get('token', None))
            return True
        except Exception as ex:
            logger.error(f"Не удалось извлечь учетные данные Telegram из KeePass: {ex}")
            return False

    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Discord из KeePass.

        :param kp: Экземпляр :class:`PyKeePass`.
        :type kp: PyKeePass
        :return: :obj:`True`, если загрузка прошла успешно, иначе - :obj:`False`.
        :rtype: bool
        """
        try:
            entry = kp.find_groups(path=['discord']).entries[0]
            self.credentials.discord.application_id = entry.custom_properties.get('application_id', None)
            self.credentials.discord.public_key = entry.custom_properties.get('public_key', None)
            self.credentials.discord.bot_token = entry.custom_properties.get('bot_token', None)
            return True
        except Exception as ex:
            logger.error(f"Не удалось извлечь учетные данные Discord из KeePass: {ex}")
            return False

    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
         """Загружает учетные данные PrestaShop из KeePass.

        :param kp: Экземпляр :class:`PyKeePass`.
        :type kp: PyKeePass
        :return: :obj:`True`, если загрузка прошла успешно, иначе - :obj:`False`.
        :rtype: bool
         """
         try:
             entries = kp.find_groups(path=['prestashop']).entries
             for entry in entries:
                setattr(self.credentials.telegram, entry.title, entry.custom_properties.get('token', None))
         except Exception as ex:
            logger.error(f"Не удалось извлечь токен PrestaShop из KeePass {ex}")
            return False
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
         except Exception as ex:
            logger.error(f"Не удалось извлечь учетные данные PrestaShop из KeePass {ex}")
            return False

    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Translations для PrestaShop из KeePass.

        :param kp: Экземпляр :class:`PyKeePass`.
        :type kp: PyKeePass
        :return: :obj:`True`, если загрузка прошла успешно, иначе - :obj:`False`.
        :rtype: bool
        """
        try:
            entry = kp.find_groups(path=['prestashop', 'translation']).entries[0]
            self.credentials.presta.translations.server = entry.custom_properties.get('server', None)
            self.credentials.presta.translations.port = entry.custom_properties.get('port', None)
            self.credentials.presta.translations.database = entry.custom_properties.get('database', None)
            self.credentials.presta.translations.user = entry.custom_properties.get('user', None)
            self.credentials.presta.translations.password = entry.custom_properties.get('password', None)
            return True
        except Exception as ex:
            logger.error(f"Не удалось извлечь учетные данные Translations из KeePass: {ex}")
            return False

    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные SMTP из KeePass.

        :param kp: Экземпляр :class:`PyKeePass`.
        :type kp: PyKeePass
        :return: :obj:`True`, если загрузка прошла успешно, иначе - :obj:`False`.
        :rtype: bool
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
        except Exception as ex:
            logger.error(f"Не удалось извлечь учетные данные SMTP из KeePass: {ex}")
            return False

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Facebook из KeePass.

        :param kp: Экземпляр :class:`PyKeePass`.
        :type kp: PyKeePass
        :return: :obj:`True`, если загрузка прошла успешно, иначе - :obj:`False`.
        :rtype: bool
        """
        try:
            for entry in kp.find_groups(path=['facebook']).entries:
                self.credentials.facebook.append(SimpleNamespace(
                    app_id=entry.custom_properties.get('app_id', None),
                    app_secret=entry.custom_properties.get('app_secret', None),
                    access_token=entry.custom_properties.get('access_token', None),
                ))
            return True
        except Exception as ex:
            logger.error(f"Не удалось извлечь учетные данные Facebook из KeePass: {ex}")
            return False

    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Google API из KeePass.

        :param kp: Экземпляр :class:`PyKeePass`.
        :type kp: PyKeePass
        :return: :obj:`True`, если загрузка прошла успешно, иначе - :obj:`False`.
        :rtype: bool
        """
        try:
            entry = kp.find_groups(path=['google', 'gapi']).entries[0]
            self.credentials.gapi['api_key'] = entry.custom_properties.get('api_key', None)
            return True
        except Exception as ex:
            logger.error(f"Не удалось извлечь учетные данные GAPI из KeePass: {ex}")
            return False

    @property
    def now(self) -> str:
        """Возвращает текущую метку времени в формате год-месяц-день-часы-минуты-секунды-милисекунды.

        :return: Текущая метка времени в строковом формате.
        :rtype: str
        """
        timestamp = datetime.now().strftime(self.config.timestamp_format)
        return f"{timestamp[:-3]}"


# Global instance of ProgamSettings
gs: ProgramSettings = ProgramSettings()
```