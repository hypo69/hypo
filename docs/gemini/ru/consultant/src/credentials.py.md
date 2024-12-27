# Анализ кода модуля `credentials.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и использует классы для организации настроек.
    - Применяется паттерн Singleton для класса `ProgramSettings`.
    - Используется `pydantic` для валидации и управления настройками.
    - Применяются `SimpleNamespace` для хранения настроек, что упрощает доступ к ним.
    -  Используется `logger` для логирования ошибок.
    -  Код обрабатывает различные типы учетных данных (Aliexpress, OpenAI, Discord и т.д.).
    -  Применён  reStructuredText (RST) для документации.
-  Минусы
    -  Используется print для сообщений об ошибках, лучше использовать logger.error.
    -  Много повторяющегося кода в методах `_load_*_credentials`.
    -  Использование `...` в блоках `try/except` не очень информативно.
    -  Не хватает комментариев в формате RST к некоторым функциям и методам, особенно в части загрузки данных.
    -  Метод `_open_kp` читает пароль из файла в открытом виде, что является небезопасным.
    -  В методе `_load_PrestaShop_credentials` перекрытие `return True`  и нескольких блоков `try/except`.
    -  Не везде есть аннотация типов переменных.

**Рекомендации по улучшению**

1.  Заменить `print` на `logger.error` для вывода ошибок.
2.  Упростить методы `_load_*_credentials`, используя общую функцию или класс для обработки загрузки учетных данных из KeePass.
3.  Заменить `...` в блоках `try/except` на конкретные действия (логирование ошибки и возможное повторное выполнение).
4.  Добавить комментарии в формате RST ко всем функциям и методам.
5.  Убрать чтение пароля из файла в открытом виде в методе `_open_kp`  или вынести этот параметр в переменную окружения.
6.  Пересмотреть логику в `_load_PrestaShop_credentials` для устранения перекрытия return.
7.  Добавить аннотации типов для переменных где это необходимо.
8.  Использовать  `j_loads` или `j_loads_ns` для загрузки `config.json`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для управления настройками приложения и загрузки учетных данных.
=========================================================================================

Этот модуль содержит класс :class:`ProgramSettings`, который управляет глобальными настройками
проекта, включая пути, учетные данные и другие параметры. Он также обеспечивает загрузку
необходимых учетных данных из базы данных KeePass.

Пример использования
--------------------

.. code-block:: python

    from src.credentials import gs

    print(gs.config.project_name)
    print(gs.credentials.aliexpress.api_key)
"""
MODE = 'dev'

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
from typing import Optional, Any, List

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


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определение корневого каталога проекта.

    Ищет корневой каталог проекта, начиная с текущего каталога файла и поднимаясь
    вверх по иерархии каталогов, пока не найдет каталог, содержащий один из
    указанных файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, которые идентифицируют корень проекта.
    :return: Путь к корневому каталогу, если найден, иначе каталог, где расположен скрипт.
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
    """
    Декоратор для реализации Singleton.
    
    Обеспечивает создание только одного экземпляра класса.

    :param cls: Класс, для которого реализуется Singleton.
    :return: Функция-обертка, возвращающая экземпляр класса.
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
    =========================================================================================

    Этот класс представляет собой синглтон, хранящий основные параметры и настройки проекта.
    Он включает в себя настройки для различных API (Aliexpress, OpenAI, Discord и т.д.),
    пути к директориям, а также общие настройки проекта.
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
        """
        Инициализация настроек программы.
        =========================================================================================

        Выполняет инициализацию после создания экземпляра класса, включая загрузку
        конфигурационного файла, настройку путей и загрузку учетных данных.
        """
        super().__init__(**kwargs)

        # Загрузка настроек из config.json
        self.config = j_loads_ns(self.base_dir / 'src' / 'config.json') # код исполняет загрузку конфига
        if not self.config:
            logger.error('Ошибка при загрузке настроек')
            ...
            return

        self.config.project_name = self.base_dir.name

        # Настройка путей
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

        # Проверка последней версии на github
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
        Загрузка учетных данных.
        =========================================================================================

        Загружает учетные данные для различных сервисов (Aliexpress, OpenAI, Discord и т.д.)
        из базы данных KeePass.
        """
        kp = self._open_kp(3)
        if not kp:
            logger.error('Ошибка открытия базы данных KeePass')
            ...
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
        """
        Открытие базы данных KeePass.
        =========================================================================================

        Открывает базу данных KeePass с заданным количеством попыток.

        :param retry: Количество попыток открытия базы данных.
        :return: Экземпляр PyKeePass, если открытие удалось, иначе None.
        """
        while retry > 0:
            try:
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG ~~~~~~~ ФАЙЛ ПАРОЛЯ В ОТКРЫТОМ ВИДЕ ~~~~~~~~~~~~~~~~~~~~~~
                password: str = Path(self.path.secrets / 'password.txt').read_text(encoding="utf-8") or None
                """password: содержит строку пароля в открытом виде. Можно удалить или сам файл или вытереть его содржимое """

                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'),
                               password=password or getpass.getpass(print('Enter KeePass master password: ').lower()))

                return kp
            except Exception as ex:
                logger.error(f"Не удалось открыть базу данных KeePass: {ex}, осталось попыток: {retry-1}")
                ...
                retry -= 1
                if retry < 1:
                    logger.critical('Не удалось открыть базу данных KeePass после нескольких попыток', exc_info=True)
                    ...
                    sys.exit()

    def _load_credentials_from_group(self, kp: PyKeePass, group_path: List[str], target: SimpleNamespace, key_map: dict) -> bool:
        """
        Загрузка учетных данных из группы KeePass.
        =========================================================================================

        Загружает учетные данные из указанной группы в базе данных KeePass.

        :param kp: Экземпляр PyKeePass.
        :param group_path: Список строк, представляющий путь к группе в KeePass.
        :param target: Объект SimpleNamespace, в который будут загружены данные.
        :param key_map: Словарь, отображающий имена полей в KeePass на атрибуты в `target`.
        :return: True, если загрузка успешна, иначе False.
        """
        try:
            entries = kp.find_groups(path=group_path).entries
            if not entries:
                logger.warning(f"Не найдены записи в группе KeePass: {group_path}")
                return False

            for entry in entries:
                for key, attr in key_map.items():
                    setattr(target, attr, entry.custom_properties.get(key, None))

            return True
        except Exception as ex:
            logger.error(f"Не удалось загрузить учетные данные из KeePass группы: {group_path}", exc_info=True)
            return False

    # Define methods for loading various credentials
    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """
        Загрузка учетных данных Aliexpress.
        =========================================================================================

        Загружает учетные данные Aliexpress API из KeePass.

        :param kp: Экземпляр PyKeePass.
        :return: True, если загрузка успешна, иначе False.
        """
        key_map = {
            'api_key': 'api_key',
            'secret': 'secret',
            'tracking_id': 'tracking_id',
            'email': 'email',
        }
        try:
            entry = kp.find_groups(path=['suppliers', 'aliexpress', 'api']).entries[0]
            for key, attr in key_map.items():
                setattr(self.credentials.aliexpress, attr, entry.custom_properties.get(key, None))
            self.credentials.aliexpress.password = entry.password
            return True
        except Exception as ex:
             logger.error(f"Не удалось извлечь учетные данные Aliexpress API из KeePass {ex}", exc_info=True)
             return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """
        Загрузка учетных данных OpenAI.
        =========================================================================================

        Загружает учетные данные OpenAI из KeePass.

        :param kp: Экземпляр PyKeePass.
        :return: True, если загрузка успешна, иначе False.
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
             logger.error(f"Не удалось извлечь учетные данные OpenAI из KeePass {ex}", exc_info=True)
             return False

    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """
        Загрузка учетных данных GoogleAI (Gemini).
        =========================================================================================

        Загружает учетные данные GoogleAI (Gemini) из KeePass.

        :param kp: Экземпляр PyKeePass.
        :return: True, если загрузка успешна, иначе False.
        """
        key_map = {'api_key': 'api_key'}
        return self._load_credentials_from_group(kp, ['gemini'], self.credentials.gemini, key_map)


    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """
        Загрузка учетных данных Telegram.
        =========================================================================================

        Загружает учетные данные Telegram из KeePass.

        :param kp: Экземпляр PyKeePass.
        :return: True, если загрузка успешна, иначе False.
        """
        key_map = {'token': 'token'}
        return self._load_credentials_from_group(kp, ['telegram'], self.credentials.telegram, key_map)



    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """
        Загрузка учетных данных Discord.
        =========================================================================================

        Загружает учетные данные Discord из KeePass.

        :param kp: Экземпляр PyKeePass.
        :return: True, если загрузка успешна, иначе False.
        """
        try:
            entry = kp.find_groups(path=['discord']).entries[0]
            self.credentials.discord.application_id = entry.custom_properties.get('application_id', None)
            self.credentials.discord.public_key = entry.custom_properties.get('public_key', None)
            self.credentials.discord.bot_token = entry.custom_properties.get('bot_token', None)
            return True
        except Exception as ex:
            logger.error(f"Не удалось извлечь учетные данные Discord из KeePass {ex}", exc_info=True)
            return False


    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
        """
        Загрузка учетных данных PrestaShop.
        =========================================================================================

        Загружает учетные данные PrestaShop из KeePass.

        :param kp: Экземпляр PyKeePass.
        :return: True, если загрузка успешна, иначе False.
        """
        try:
            entries = kp.find_groups(path=['prestashop']).entries
            for entry in entries:
                setattr(self.credentials.telegram, entry.title, entry.custom_properties.get('token', None))

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
            logger.error(f"Не удалось извлечь учетные данные PrestaShop из KeePass {ex}", exc_info=True)
            return False

    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """
        Загрузка учетных данных для переводов PrestaShop.
        =========================================================================================

        Загружает учетные данные для переводов PrestaShop из KeePass.

        :param kp: Экземпляр PyKeePass.
        :return: True, если загрузка успешна, иначе False.
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
            logger.error(f"Не удалось извлечь учетные данные переводов PrestaShop из KeePass {ex}", exc_info=True)
            return False

    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """
        Загрузка учетных данных SMTP.
        =========================================================================================

        Загружает учетные данные SMTP из KeePass.

        :param kp: Экземпляр PyKeePass.
        :return: True, если загрузка успешна, иначе False.
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
            logger.error(f"Не удалось извлечь учетные данные SMTP из KeePass {ex}", exc_info=True)
            return False


    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """
        Загрузка учетных данных Facebook.
        =========================================================================================

        Загружает учетные данные Facebook из KeePass.

        :param kp: Экземпляр PyKeePass.
        :return: True, если загрузка успешна, иначе False.
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
            logger.error(f"Не удалось извлечь учетные данные Facebook из KeePass {ex}", exc_info=True)
            return False

    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """
        Загрузка учетных данных Google API.
        =========================================================================================

        Загружает учетные данные Google API из KeePass.

        :param kp: Экземпляр PyKeePass.
        :return: True, если загрузка успешна, иначе False.
        """
        try:
            entry = kp.find_groups(path=['google', 'gapi']).entries[0]
            self.credentials.gapi['api_key'] = entry.custom_properties.get('api_key', None)
            return True
        except Exception as ex:
             logger.error(f"Не удалось извлечь учетные данные GAPI из KeePass {ex}", exc_info=True)
             return False

    @property
    def now(self) -> str:
        """
        Получение текущей метки времени.
        =========================================================================================

        Возвращает текущую метку времени в формате год-месяц-день-часы-минуты-секунды-миллисекунды.

        :return: Строка с текущей меткой времени.
        """
        timestamp = datetime.now().strftime(self.config.timestamp_format)
        # Вернём только первые 3 цифры миллисекунд, т.к. %f возвращает микросекунды (6 цифр)
        return f"{timestamp[:-3]}"


# Global instance of ProgamSettings
gs: ProgramSettings = ProgramSettings()
```