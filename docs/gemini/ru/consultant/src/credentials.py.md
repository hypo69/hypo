# Анализ кода модуля `credentials.py`

**Качество кода**
8
-  Плюсы
    - Код структурирован и разбит на функции, что облегчает чтение и понимание.
    - Используется `pydantic` для валидации данных и `dataclasses` для создания структур данных.
    - Применяется паттерн Singleton для класса `ProgramSettings`, что гарантирует единственный экземпляр класса.
    - Присутствуют docstring для функций и классов, что способствует лучшей документации.
    - Используется `logger` для логирования ошибок и предупреждений.
    - Есть обработка исключений, хотя ее можно улучшить.
    - Используются `j_loads` и `j_loads_ns` из `src.utils.jjson` для загрузки json файлов.
-  Минусы
    - Некоторые комментарии не соответствуют стандарту RST.
    - В некоторых местах используется print для вывода ошибок, лучше использовать `logger.error`.
    - Есть повторяющийся код, например, при загрузке различных типов учетных данных.
    - Некоторые функции не имеют возвращаемого значения, когда это было бы уместно.
    - Использован `sys.exit()` в обработке ошибок, что может не совсем корректно завершить работу. Лучше использовать исключения.
    - Использованы `...` как заглушки, следует их убрать или заменить на конкретные действия.
    - Есть лишний импорт `from datetime import datetime`, поскольку `datetime` уже импортирован как модуль.
    - Отсутствует проверка наличия необходимых файлов (например, `config.json`, `credentials.kdbx` и `password.txt`).
    - Переменная `__root__` используется как глобальная и внутри функции - стоит переименовать.
    - Не все функции и методы имеют docstring.
    - В методе `_load_PrestaShop_credentials` есть дублирование кода и ошибки логики.
    - Метод `now` форматирует время вручную, хотя можно использовать возможности `datetime` для форматирования.

**Рекомендации по улучшению**
1. **Комментарии и документация**:
   - Переписать все комментарии в формате reStructuredText (RST).
   - Добавить подробные docstring ко всем функциям, методам и классам.
2. **Обработка ошибок**:
   - Заменить `print` на `logger.error` для вывода сообщений об ошибках.
   - Избегать использования `sys.exit()`, предпочесть выбрасывать исключения.
   - Добавить более детальную обработку исключений, с конкретными сообщениями об ошибках.
   - Убрать все `...` и заменить их на конкретные действия.
3. **Рефакторинг**:
   - Избавиться от дублирования кода, особенно в функциях загрузки учетных данных.
   - Пересмотреть логику загрузки учетных данных PrestaShop, исправить ошибки.
   - Улучшить форматирование времени в методе `now`, использовать `datetime` для форматирования.
4. **Импорты**:
   - Удалить лишние импорты.
5. **Проверки**:
    - Добавить проверки на наличие необходимых файлов.
6. **Переменные**:
    - Переименовать `__root__` в `project_root` для избежания конфликтов.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для управления глобальными настройками проекта.
=========================================================================================

Этот модуль определяет класс :class:`ProgramSettings`, который является синглтоном и
хранит основные параметры и настройки проекта, такие как пути, пароли, логины и настройки API.

Модуль обеспечивает загрузку конфигураций и учетных данных из файлов и базы данных KeePass.

Пример использования
--------------------

Пример инициализации и использования класса `ProgramSettings`:

.. code-block:: python

    settings = ProgramSettings()
    print(settings.path.root)
"""

import datetime
import getpass
import os
import sys
import socket
import warnings
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


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определение корневой директории проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    двигаясь вверх по структуре каталогов до первого каталога, содержащего один из
    маркерных файлов.

    :param marker_files: Кортеж имен файлов или каталогов, идентифицирующих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта. Если не найден, возвращает директорию, где находится скрипт.
    :rtype: Path
    """
    project_root: Path
    current_path: Path = Path(__file__).resolve().parent
    project_root = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            project_root = parent
            break
    if project_root not in sys.path:
        sys.path.insert(0, str(project_root))
    return project_root


def singleton(cls):
    """
    Декоратор для реализации Singleton.

    Гарантирует, что класс будет иметь только один экземпляр.

    :param cls: Класс, к которому применяется декоратор.
    :return: Функция, возвращающая экземпляр класса.
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

        Выполняет загрузку конфигурации, установку путей и загрузку учетных данных.

        :param kwargs: Произвольные ключевые аргументы.
        """
        super().__init__(**kwargs)

        # Загружает конфигурацию из файла config.json
        try:
            self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
            if not self.config:
                logger.error('Ошибка при загрузке настроек из config.json')
                return
        except Exception as ex:
            logger.error(f'Ошибка при загрузке файла конфигурации: {ex}')
            return

        # Устанавливает имя проекта из названия базовой директории
        self.config.project_name = self.base_dir.name

        # Устанавливает пути к директориям проекта
        self.path = SimpleNamespace(
            root=Path(self.base_dir),
            bin=Path(self.base_dir / 'bin'),  # <- тут бинарники (chrome, firefox, ffmpeg, ...)
            src=Path(self.base_dir) / 'src',  # <- тут весь код
            endpoints=Path(self.base_dir) / 'src' / 'endpoints',  # <- тут все клиенты
            secrets=Path(self.base_dir / 'secrets'),  # <- это папка с паролями и базой данных ! Ей нельзя попадать в гит!!!
            toolbox=Path(self.base_dir / 'toolbox'),  # <- служебные утилиты

            log=Path(getattr(self.config.path, 'log', self.base_dir / 'log')),
            tmp=Path(getattr(self.config.path, 'tmp', self.base_dir / 'tmp')),
            data=Path(getattr(self.config.path, 'data', self.base_dir / 'data')),
            # <- данные от endpoints (hypo69, kazarinov, prestashop, etc ...)
            google_drive=Path(getattr(self.config.path, 'google_drive', self.base_dir / 'google_drive')),
            # <- GOOGLE DRIVE ЧЕРЕЗ ЛОКАЛЬНЫЙ ДИСК (NOT API)
            external_storage=Path(
                getattr(self.config.path, 'external_storage', self.base_dir / 'external_storage')),
        )

        # Проверяет наличие новой версии hypo69 на github
        if check_latest_release(self.config.git_user, self.config.git):
            logger.info("Доступна новая версия hypo69 на GitHub")  # Логика что делать когда есть новая версия hypo69 на github

        # Устанавливает режим работы (dev, prod)
        self.MODE = self.config.mode

        # Пути к бинарным файлам
        gtk_bin_dir = self.base_dir / 'bin' / 'gtk' / 'gtk-nsis-pack' / 'bin'
        ffmpeg_bin_dir = self.base_dir / 'bin' / 'ffmpeg' / 'bin'
        graphviz_bin_dir = self.base_dir / 'bin' / 'graphviz' / 'bin'
        wkhtmltopdf_bin_dir = self.base_dir / 'bin' / 'wkhtmltopdf' / 'files' / 'bin'

        # Добавляет пути к бинарным файлам в sys.path
        for bin_path in [self.base_dir, gtk_bin_dir, ffmpeg_bin_dir, graphviz_bin_dir, wkhtmltopdf_bin_dir]:
            if bin_path not in sys.path:
                sys.path.insert(0, str(bin_path))

        # Устанавливает переменную окружения для WeasyPrint
        os.environ['WEASYPRINT_DLL_DIRECTORIES'] = str(gtk_bin_dir)

        # Подавляет вывод GTK логов в консоль
        warnings.filterwarnings("ignore", category=UserWarning)
        self._load_credentials()

    def _load_credentials(self) -> None:
        """
        Загружает учетные данные из KeePass.

        Загружает все необходимые учетные данные из базы данных KeePass,
        используя методы для каждого типа сервиса.
        """
        kp = self._open_kp()
        if not kp:
            logger.error("Не удалось открыть базу данных KeePass.")
            return

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
        Открывает базу данных KeePass.

        Открывает базу данных KeePass с заданным количеством попыток.
        
        :param retry: Количество попыток открытия базы данных.
        :type retry: int
        :return: Объект PyKeePass или None в случае неудачи.
        :rtype: Optional[PyKeePass]
        """
        while retry > 0:
            try:
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG ~~~~~~~ ФАЙЛ ПАРОЛЯ В ОТКРЫТОМ ВИДЕ ~~~~~~~~~~~~~~~~~~~~~~
                password_file = self.path.secrets / 'password.txt'
                if not password_file.exists():
                    logger.error(f"Файл с паролем не найден: {password_file}")
                    return None

                password = password_file.read_text(encoding="utf-8").strip()

                if not password:
                    password = getpass.getpass(prompt='Enter KeePass master password: ').strip()

                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), password=password)

                return kp
            except Exception as ex:
                retry -= 1
                logger.error(f"Не удалось открыть базу данных KeePass. Осталось попыток: {retry}, Exception: {ex}")
                if retry < 1:
                    logger.critical('Не удалось открыть базу данных KeePass после нескольких попыток', exc_info=True)
                    return None
        return None

    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Aliexpress из KeePass.
        
        :param kp: Экземпляр базы данных KeePass.
        :type kp: PyKeePass
        :return: True, если загрузка успешна, иначе False.
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
            logger.error(f"Не удалось извлечь учетные данные Aliexpress из KeePass: {ex}")
            return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные OpenAI из KeePass.

        :param kp: Экземпляр базы данных KeePass.
        :type kp: PyKeePass
        :return: True, если загрузка успешна, иначе False.
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
        """
        Загружает учетные данные GoogleAI (Gemini) из KeePass.
        
        :param kp: Экземпляр базы данных KeePass.
        :type kp: PyKeePass
        :return: True, если загрузка успешна, иначе False.
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
        """
        Загружает учетные данные Telegram из KeePass.

        :param kp: Экземпляр базы данных KeePass.
        :type kp: PyKeePass
        :return: True, если загрузка успешна, иначе False.
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
        """
        Загружает учетные данные Discord из KeePass.

        :param kp: Экземпляр базы данных KeePass.
        :type kp: PyKeePass
        :return: True, если загрузка успешна, иначе False.
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
        """
        Загружает учетные данные PrestaShop из KeePass.

        :param kp: Экземпляр базы данных KeePass.
        :type kp: PyKeePass
        :return: True, если загрузка успешна, иначе False.
        :rtype: bool
        """
        try:
            for entry in kp.find_groups(path=['prestashop']).entries:
                setattr(self.credentials.presta, entry.title, entry.custom_properties.get('token', None))

            for entry in kp.find_groups(path=['prestashop', 'clients']).entries:
                client_data = SimpleNamespace(
                    api_key=entry.custom_properties.get('api_key', None),
                    api_domain=entry.custom_properties.get('api_domain', None),
                    db_server=entry.custom_properties.get('db_server', None),
                    db_user=entry.custom_properties.get('db_user', None),
                    db_password=entry.custom_properties.get('db_password', None),
                )
                self.credentials.presta.client.append(client_data)
            return True
        except Exception as ex:
            logger.error(f"Не удалось извлечь учетные данные PrestaShop из KeePass: {ex}")
            return False

    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные для переводов PrestaShop из KeePass.

        :param kp: Экземпляр базы данных KeePass.
        :type kp: PyKeePass
        :return: True, если загрузка успешна, иначе False.
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
        """
        Загружает учетные данные SMTP из KeePass.

        :param kp: Экземпляр базы данных KeePass.
        :type kp: PyKeePass
        :return: True, если загрузка успешна, иначе False.
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
        """
        Загружает учетные данные Facebook из KeePass.

        :param kp: Экземпляр базы данных KeePass.
        :type kp: PyKeePass
        :return: True, если загрузка успешна, иначе False.
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
        """
        Загружает учетные данные Google API из KeePass.

        :param kp: Экземпляр базы данных KeePass.
        :type kp: PyKeePass
        :return: True, если загрузка успешна, иначе False.
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
        """
        Возвращает текущую метку времени.
       
        :return: Текущая метка времени в формате `год_месяц_день_часы_минуты_секунды_милисекунды`.
        :rtype: str
        """
        timestamp = datetime.datetime.now().strftime(self.config.timestamp_format)
        return timestamp[:-3] # Возвращаем только первые 3 цифры миллисекунд


# Глобальный экземпляр класса ProgramSettings
gs: ProgramSettings = ProgramSettings()
```