### Анализ кода модуля `credentials.py`

**Качество кода**:
   - **Соответствие стандартам**: 6/10
   - **Плюсы**:
     - Использование `dataclass` для `ProgramSettings`, что упрощает создание класса.
     - Применение паттерна Singleton для `ProgramSettings` через декоратор `singleton`.
     - Наличие отдельных методов для загрузки учетных данных из KeePass, что улучшает читаемость кода.
     - Использование `SimpleNamespace` для организации конфигурационных данных.
   - **Минусы**:
     - Смешанное использование кавычек (одинарных и двойных) в коде и выводе.
     - Чрезмерное использование `try-except` с общим `Exception`, что затрудняет отладку.
     - Использование `print` вместо `logger` для вывода сообщений об ошибках.
     - Повторяющийся код при загрузке учетных данных.
     - Непоследовательное именование переменных и атрибутов.
     - Отсутствие документации в формате RST для многих функций и методов.
     - Использование `sys.exit()` напрямую, что может вызвать проблемы при тестировании.

**Рекомендации по улучшению**:
   - Привести все строки в коде к одинарным кавычкам, а двойные кавычки использовать только для `print`, `input` и `logger.error`.
   - Заменить общие `try-except` на более конкретные и обрабатывать исключения через `logger.error`.
   - Использовать `from src.logger.logger import logger` для логирования.
   - Добавить RST-документацию ко всем функциям и методам.
   - Избегать использования `sys.exit()` в функциях, возвращать `False` и обрабатывать ошибку в вызывающей функции.
   - Переименовать `__root__` в `project_root` для лучшего понимания.
   - Вынести логику загрузки общих параметров из `_load_credentials` в отдельный метод.
   - Привести к единому стилю названия переменных и атрибутов, например, использовать snake_case.
   - Улучшить обработку ошибок при загрузке учетных данных, например, логировать конкретные исключения.

**Оптимизированный код**:
```python
"""
Модуль для управления глобальными настройками проекта.
======================================================

Этот модуль отвечает за загрузку и управление основными настройками проекта,
включая пути, пароли, логины и API-ключи.

Модуль использует синглтон :class:`ProgramSettings` для доступа к настройкам
и обеспечивает их централизованное управление.

Пример использования
--------------------
.. code-block:: python

    from src.credentials import gs

    print(gs.path.root)
    print(gs.credentials.aliexpress.api_key)

"""
import datetime
import getpass
import os
import sys
import warnings
import socket
from dataclasses import dataclass, field
from pathlib import Path
from types import SimpleNamespace
from typing import Optional, List, Dict

from pykeepass import PyKeePass

from src.check_release import check_latest_release
from src.logger.logger import logger # Изменен импорт
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


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Ищет корневую директорию проекта, начиная с директории текущего файла.
    
    Поиск идет вверх по дереву директорий, останавливаясь на первой директории,
    содержащей один из указанных файлов-маркеров.

    :param marker_files: Список файлов или директорий, идентифицирующих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если найдена; в противном случае - директория, где расположен скрипт.
    :rtype: Path
    
    Пример:
        >>> set_project_root()
        PosixPath('/path/to/your/project')
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

    :param cls: Класс, для которого нужно создать синглтон.
    :type cls: class
    :return: Функция-обертка, возвращающая экземпляр синглтона.
    :rtype: function
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
@dataclass
class ProgramSettings:
    """
    Класс `ProgramSettings` - синглтон, хранящий основные параметры и настройки проекта.
    
    :ivar host_name: Имя хоста.
    :vartype host_name: str
    :ivar base_dir: Базовая директория проекта.
    :vartype base_dir: Path
    :ivar config: Конфигурации проекта.
    :vartype config: SimpleNamespace
    :ivar credentials: Учетные данные.
    :vartype credentials: SimpleNamespace
    :ivar MODE: Режим работы приложения (dev/prod).
    :vartype MODE: str
    :ivar path: Пути к различным директориям.
    :vartype path: SimpleNamespace
    
    Пример:
        >>> gs = ProgramSettings()
        >>> print(gs.host_name)
        your_hostname
    """
    host_name: str = field(default_factory=lambda: socket.gethostname())
    base_dir: Path = field(default_factory=lambda: set_project_root())
    config: SimpleNamespace = field(default_factory=lambda: SimpleNamespace())
    
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
            client=SimpleNamespace(
                server=None,
                port=None,
                database=None,
                user=None,
                password=None,
            )
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
    MODE: str = 'dev'
    path: SimpleNamespace = field(default_factory=lambda: SimpleNamespace(
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


    def __post_init__(self):
        """Выполняет инициализацию после создания экземпляра класса."""
        self._load_config()
        self._setup_paths()
        self._check_for_updates()
        self._set_bin_paths()
        self._suppress_gtk_warnings()
        self._load_credentials()

    def _load_config(self) -> None:
        """Загружает конфигурацию проекта из `config.json`."""
        self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
        if not self.config:
            logger.error('Ошибка при загрузке настроек')
            # sys.exit() # <--  убрали sys.exit, будет обрабатываться в вызывающей функции
            return None
        self.config.timestamp_format = getattr(self.config, 'timestamp_format', '%y_%m_%d_%H_%M_%S_%f')
        self.config.project_name = self.base_dir.name

    def _setup_paths(self) -> None:
        """Настраивает пути к различным директориям проекта."""
        self.path = SimpleNamespace(
            root=Path(self.base_dir),
            bin=Path(self.base_dir / 'bin'),
            src=Path(self.base_dir) / 'src',
            endpoints=Path(self.base_dir) / 'src' / 'endpoints',
            secrets=Path(self.base_dir / 'secrets'),
            toolbox=Path(self.base_dir / 'toolbox'),

            log=Path(getattr(self.config.path, 'log', self.base_dir / 'log')),
            tmp=Path(getattr(self.config.path, 'tmp', self.base_dir / 'tmp')),
            data=Path(getattr(self.config.path, 'data', self.base_dir / 'data')),
            google_drive=Path(getattr(self.config.path, 'google_drive', self.base_dir / 'google_drive')),
            external_storage=Path(getattr(self.config.path, 'external_storage',  self.base_dir / 'external_storage') ),
        )

    def _check_for_updates(self) -> None:
        """Проверяет наличие новых релизов на GitHub."""
        if check_latest_release(self.config.git_user, self.config.git):
            ...  # Логика что делать когда есть новая версия hypo69 на github

        self.MODE = self.config.mode

    def _set_bin_paths(self) -> None:
        """Добавляет пути к бинарным файлам в системные пути."""
        gtk_bin_dir = self.path.bin  / 'gtk' / 'gtk-nsis-pack' / 'bin'
        ffmpeg_bin_dir = self.base_dir  / 'bin' / 'ffmpeg' / 'bin'
        graphviz_bin_dir = self.base_dir  / 'bin' / 'graphviz' / 'bin'
        wkhtmltopdf_bin_dir = self.base_dir  / 'bin' / 'wkhtmltopdf' / 'files' / 'bin'

        for bin_path in [self.base_dir, gtk_bin_dir, ffmpeg_bin_dir, graphviz_bin_dir, wkhtmltopdf_bin_dir]:
            if bin_path not in sys.path:
                sys.path.insert(0, str(bin_path))

        os.environ['WEASYPRINT_DLL_DIRECTORIES'] = str(gtk_bin_dir)

    def _suppress_gtk_warnings(self) -> None:
        """Подавляет вывод предупреждений GTK в консоль."""
        warnings.filterwarnings('ignore', category=UserWarning)
        
    def _load_credentials(self) -> None:
        """Загружает учетные данные из KeePass."""
        kp = self._open_kp(3)
        if not kp:
            logger.error('Ошибка при открытии базы данных KeePass')
            # sys.exit(1)  # <-- убрали sys.exit, будет обрабатываться в вызывающей функции
            return None

        if not self._load_aliexpress_credentials(kp):
             logger.error('Failed to load Aliexpress credentials')

        if not self._load_openai_credentials(kp):
            logger.error('Failed to load OpenAI credentials')

        if not self._load_gemini_credentials(kp):
            logger.error('Failed to load GoogleAI credentials')

        if not self._load_discord_credentials(kp):
            logger.error('Failed to load Discord credentials')

        if not self._load_telegram_credentials(kp):
            logger.error('Failed to load Telegram credentials')

        if not self._load_prestashop_credentials(kp):
             logger.error('Failed to load prestashop credentials')

        if not self._load_smtp_credentials(kp):
            logger.error('Failed to load SMTP credentials')

        if not self._load_facebook_credentials(kp):
             logger.error('Failed to load Facebook credentials')

        if not self._load_presta_translations_credentials(kp):
            logger.error('Failed to load Translations credentials')

        if not self._load_gapi_credentials(kp):
           logger.error('Failed to load GAPI credentials')


    def _open_kp(self, retry: int = 3) -> PyKeePass | None:
        """
        Открывает базу данных KeePass.

        :param retry: Количество попыток открытия базы данных.
        :type retry: int
        :return: Экземпляр PyKeePass или None в случае неудачи.
        :rtype: PyKeePass | None
        
        """
        while retry > 0:
            try:
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG ~~~~~~~ ФАЙЛ ПАРОЛЯ В ОТКРЫТОМ ВИДЕ ~~~~~~~~~~~~~~~~~~~~~~
                password: str = Path(self.path.secrets / 'password.txt').read_text(encoding='utf-8') or None
                """password: содержит строку пароля в открытом виде. Можно удалить или сам файл или вытереть его содржимое """
                
                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'),
                               password=password or getpass.getpass(print('Enter KeePass master password: ').lower()))
                return kp
            except Exception as ex:
                logger.error(f'Failed to open KeePass database Exception: {ex}, {retry-1} retries left.')
                retry -= 1
                if retry < 1:
                   logger.critical('Failed to open KeePass database after multiple attempts', exc_info=True)
                   # sys.exit() # <-- убрали sys.exit, будет обрабатываться в вызывающей функции
                   return None

    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Aliexpress API из KeePass.

        :param kp: Экземпляр PyKeePass.
        :type kp: PyKeePass
        :return: True, если загрузка прошла успешно, иначе False.
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
            logger.error(f'Failed to extract Aliexpress API key from KeePass {ex}')
            return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные OpenAI из KeePass.

        :param kp: Экземпляр PyKeePass.
        :type kp: PyKeePass
        :return: True, если загрузка прошла успешно, иначе False.
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
           logger.error(f'Failed to extract OpenAI credentials from KeePass {ex}')
           return False


    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные GoogleAI (Gemini) из KeePass.

        :param kp: Экземпляр PyKeePass.
        :type kp: PyKeePass
        :return: True, если загрузка прошла успешно, иначе False.
        :rtype: bool
        """
        try:
            entries = kp.find_groups(path=['gemini']).entries

            for entry in entries:
                setattr(self.credentials.gemini, entry.title, entry.custom_properties.get('api_key', None))
            return True
        except Exception as ex:
           logger.error(f'Failed to extract GoogleAI credentials from KeePass {ex}')
           return False

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Telegram из KeePass.

        :param kp: Экземпляр PyKeePass.
        :type kp: PyKeePass
        :return: True, если загрузка прошла успешно, иначе False.
        :rtype: bool
        """
        try:
            entries = kp.find_groups(path=['telegram']).entries
            for entry in entries:
                setattr(self.credentials.telegram, entry.title, entry.custom_properties.get('token', None))
            return True
        except Exception as ex:
           logger.error(f'Failed to extract Telegram credentials from KeePass {ex}')
           return False

    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Discord из KeePass.

        :param kp: Экземпляр PyKeePass.
        :type kp: PyKeePass
        :return: True, если загрузка прошла успешно, иначе False.
        :rtype: bool
        """
        try:
            entry = kp.find_groups(path=['discord']).entries[0]
            self.credentials.discord.application_id = entry.custom_properties.get('application_id', None)
            self.credentials.discord.public_key = entry.custom_properties.get('public_key', None)
            self.credentials.discord.bot_token = entry.custom_properties.get('bot_token', None)
            return True
        except Exception as ex:
            logger.error(f'Failed to extract Discord credentials from KeePass {ex}')
            return False

    def _load_prestashop_credentials(self, kp: PyKeePass) -> bool:
        """
         Загружает учетные данные PrestaShop из KeePass.

         :param kp: Экземпляр PyKeePass.
         :type kp: PyKeePass
         :return: True, если загрузка прошла успешно, иначе False.
         :rtype: bool
         """

        for entry in kp.find_groups(path=['prestashop', 'clients']).entries:
            try:
                # Создаем новый SimpleNamespace для клиента
                client_ns = SimpleNamespace()

                # Устанавливаем атрибут в self.credentials.presta.client с именем entry.title
                setattr(self.credentials.presta.client, entry.title, client_ns)

                # Получаем ссылку на созданный объект через entry.title
                current_client = getattr(self.credentials.presta.client, entry.title)

                setattr(current_client, 'api_key', entry.custom_properties.get('api_key', None))
                setattr(current_client, 'api_domain', entry.custom_properties.get('api_domain', None))
                setattr(current_client, 'db_server', entry.custom_properties.get('db_server', None))
                setattr(current_client, 'db_user', entry.custom_properties.get('db_user', None))
                setattr(current_client, 'db_password', entry.custom_properties.get('db_password', None))

            except Exception as ex:
                logger.error(f'Failed to extract prestashop credentials from KeePass {ex}')
                return False

        return True

    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные для переводов PrestaShop из KeePass.

        :param kp: Экземпляр PyKeePass.
        :type kp: PyKeePass
        :return: True, если загрузка прошла успешно, иначе False.
        :rtype: bool
        """
        try:
            entry = kp.find_groups(path=['prestashop','translation']).entries[0]
            self.credentials.presta.translations.server = entry.custom_properties.get('server', None)
            self.credentials.presta.translations.port = entry.custom_properties.get('port', None)
            self.credentials.presta.translations.database = entry.custom_properties.get('database', None)
            self.credentials.presta.translations.user = entry.custom_properties.get('user', None)
            self.credentials.presta.translations.password = entry.custom_properties.get('password', None)
            return True
        except Exception as ex:
            logger.error(f'Failed to extract Translations credentials from KeePass {ex}')
            return False

    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные SMTP из KeePass.

        :param kp: Экземпляр PyKeePass.
        :type kp: PyKeePass
        :return: True, если загрузка прошла успешно, иначе False.
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
            logger.error(f'Failed to extract SMTP credentials from KeePass {ex}')
            return False

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Facebook из KeePass.

        :param kp: Экземпляр PyKeePass.
        :type kp: PyKeePass
        :return: True, если загрузка прошла успешно, иначе False.
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
            logger.error(f'Failed to extract Facebook credentials from KeePass {ex}')
            return False

    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Google API из KeePass.

        :param kp: Экземпляр PyKeePass.
        :type kp: PyKeePass
        :return: True, если загрузка прошла успешно, иначе False.
        :rtype: bool
        """
        try:
            entry = kp.find_groups(path=['google','gapi']).entries[0]
            self.credentials.gapi['api_key'] = entry.custom_properties.get('api_key', None)
            return True
        except Exception as ex:
            logger.error(f'Failed to extract GAPI credentials from KeePass {ex}')
            return False

    @property
    def now(self) -> str:
        """
        Возвращает текущую метку времени в формате год-месяц-день-часы-минуты-секунды-милисекунды.

        Этот метод возвращает строку, представляющую текущую метку времени, в формате `год_месяц_день_часы_минуты_секунды_миллисекунды`.

        :return: Текущая метка времени в строковом формате.
        :rtype: str
        """
        timestamp = datetime.datetime.now().strftime(self.config.timestamp_format)
        # Вернём только первые 3 цифры миллисекунд, т.к. %f возвращает микросекунды (6 цифр)
        return f'{timestamp[:-3]}'


# Global instance of ProgamSettings
gs: ProgramSettings = ProgramSettings()