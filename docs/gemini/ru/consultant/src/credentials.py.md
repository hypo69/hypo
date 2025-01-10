# Анализ кода модуля `credentials.py`

**Качество кода**

- Соответствие требованиям: 7/10
-  Плюсы:
    -  Код хорошо структурирован и разбит на функции, что улучшает читаемость и поддерживает принцип единственной ответственности.
    -  Используется `dataclass` для `ProgramSettings`, что уменьшает объем шаблонного кода.
    -  Применяется декоратор `@singleton` для обеспечения единственного экземпляра `ProgramSettings`.
    -  Используется `SimpleNamespace` для хранения настроек и учетных данных, что упрощает доступ к атрибутам.
    -  Присутствует базовая обработка ошибок с использованием `try-except` блоков.
    -  Есть проверки на наличие маркеров корневой директории проекта.
 -  Минусы:
    -  Множественное использование `print()` для вывода сообщений об ошибках, лучше заменить на логирование.
    -  Дублирование кода в методах `_load_*_credentials` (общая структура `try-except`).
    -  В методе `_open_kp` пароль считывается из файла в открытом виде, что является уязвимостью.
    -  Отсутствует подробная документация в формате RST для всех функций и методов.
    -  Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` при чтении конфигурационного файла.
    -  Не все импорты соответствуют стандартам, например, `from datetime import datetime` дублирует `import datetime`.
    -  Используется `sys.exit()` напрямую, без логирования фатальной ошибки.
    -  Используются двойные кавычки в строках, где должны быть одинарные (особенно в `SimpleNamespace`).
    -  Не все комментарии достаточно подробные.
    -  Использование `...` в коде, не всегда является хорошей практикой.

**Рекомендации по улучшению**

1.  **Логирование:** Заменить все `print()` на `logger.error()`, `logger.info()` и `logger.debug()`, чтобы обеспечить централизованное логирование.
2.  **Обработка паролей:** Убрать чтение пароля из файла в открытом виде и использовать `getpass.getpass` для ввода пароля из консоли, если он не был передан.
3.  **Рефакторинг методов `_load_*_credentials`:** Вынести общую логику загрузки данных из `KeePass` в отдельную функцию, чтобы избежать дублирования кода.
4.  **Документация:** Добавить документацию в формате RST для всех функций, методов и класса `ProgramSettings`, включая подробное описание аргументов и возвращаемых значений.
5.  **Использование `j_loads_ns`:** Использовать `j_loads_ns` для загрузки файла конфигурации `config.json`.
6.  **Импорты:** Убрать дублирующие импорты и привести все импорты к единому стилю.
7.  **Обработка ошибок:** Использовать `logger.critical()` вместо `sys.exit()` для критических ошибок, а `logger.error()` для обычных ошибок, также убрать `...` в блоках обработки ошибок.
8.  **Форматирование строк:** Использовать одинарные кавычки для строковых литералов в коде.
9.  **Расширить комментарии:** Добавить более подробные комментарии для пояснения логики работы кода.
10. **Использовать f-строки:** Для форматирования строк использовать f-строки, а не конкатенацию.
11. **`SimpleNamespace`:** Привести `SimpleNamespace` к единому стилю с использованием одинарных кавычек.

**Оптимизированный код**

```python
"""
.. module:: src
    :platform: Windows, Unix
    :synopsis: Global Project Settings: paths, passwords, logins, and API settings

Модуль для управления глобальными настройками проекта, включая пути, пароли, логины и API-ключи.
=================================================================================================

Этот модуль содержит класс :class:`ProgramSettings`, который является синглтоном и используется
для хранения и управления глобальными настройками проекта. Включает в себя настройку путей к
директориям, загрузку учетных данных из KeePass, и общие настройки приложения.

Пример использования
--------------------

Пример инициализации и доступа к настройкам:

.. code-block:: python

    from src.credentials import ProgramSettings
    settings = ProgramSettings()
    print(settings.path.log)
    print(settings.credentials.aliexpress.api_key)
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


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла,
    поиск ведется вверх до первой директории, содержащей любой из файлов-маркеров.

    Args:
        marker_files (tuple): Имена файлов или директорий, которые идентифицируют корень проекта.

    Returns:
        Path: Путь к корневой директории, если найдена, иначе - директория, где находится скрипт.
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
    
    Этот декоратор гарантирует, что класс будет иметь только один экземпляр.
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
    `ProgramSettings` - класс настроек программы.

    Синглтон, хранящий основные параметры и настройки проекта.
    Этот класс управляет глобальными настройками приложения, включая пути к директориям,
    учетные данные и общие параметры.
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
        """
        Выполняет инициализацию после создания экземпляра класса.

        Загружает конфигурацию из `config.json`, устанавливает пути к директориям
        и настраивает параметры проекта.
        """
        # Загрузка конфигурации из файла `config.json` с помощью `j_loads_ns`
        self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
        if not self.config:
            logger.error('Ошибка при загрузке настроек')
            sys.exit()

        # Установка формата времени и имени проекта
        self.config.timestamp_format = getattr(self.config, 'timestamp_format', '%y_%m_%d_%H_%M_%S_%f')
        self.config.project_name = self.base_dir.name

        # Установка путей к директориям проекта
        self.path = SimpleNamespace(
            root=Path(self.base_dir),
            bin=Path(self.base_dir / 'bin'),  # <- тут бинарники (chrome, firefox, ffmpeg, ...)
            src=Path(self.base_dir) / 'src',  # <- тут весь код
            endpoints=Path(self.base_dir) / 'src' / 'endpoints',  # <- тут все клиенты
            secrets=Path(self.base_dir / 'secrets'),  # <- это папка с паролями и базой данных ! Ей нельзя попадать в гит!!!
            toolbox=Path(self.base_dir / 'toolbox'),  # <- служебные утилиты
            log=Path(getattr(self.config.path, 'log', self.base_dir / 'log')),
            tmp=Path(getattr(self.config.path, 'tmp', self.base_dir / 'tmp')),
            data=Path(getattr(self.config.path, 'data', self.base_dir / 'data')),  # <- дата от endpoints (hypo69, kazarinov, prestashop, etc ...)
            google_drive=Path(getattr(self.config.path, 'google_drive', self.base_dir / 'google_drive')),  # <- GOOGLE DRIVE ЧЕРЕЗ ЛОКАЛЬНЫЙ ДИСК (NOT API)
            external_storage=Path(getattr(self.config.path, 'external_storage', self.base_dir / 'external_storage')),  # <- Внешний диск
        )

        # Проверка наличия новой версии на GitHub
        if check_latest_release(self.config.git_user, self.config.git):
            logger.info('Новая версия на GitHub')  # Логика что делать когда есть новая версия hypo69 на github

        self.MODE = self.config.mode

        # Пути к бинарным файлам
        gtk_bin_dir = self.path.bin / 'gtk' / 'gtk-nsis-pack' / 'bin'
        ffmpeg_bin_dir = self.base_dir / 'bin' / 'ffmpeg' / 'bin'
        graphviz_bin_dir = self.base_dir / 'bin' / 'graphviz' / 'bin'
        wkhtmltopdf_bin_dir = self.base_dir / 'bin' / 'wkhtmltopdf' / 'files' / 'bin'

        # Добавление путей к бинарникам в системный путь
        for bin_path in [self.base_dir, gtk_bin_dir, ffmpeg_bin_dir, graphviz_bin_dir, wkhtmltopdf_bin_dir]:
            if bin_path not in sys.path:
                sys.path.insert(0, str(bin_path))  # <- определяю пути к бунарникам в системных путях

        # Установка переменной окружения для WeasyPrint
        os.environ['WEASYPRINT_DLL_DIRECTORIES'] = str(gtk_bin_dir)

        # Подавление предупреждений GTK
        warnings.filterwarnings("ignore", category=UserWarning)
        self._load_credentials()

    def _load_credentials(self) -> None:
        """
        Загружает учетные данные из KeePass.

        Этот метод открывает базу данных KeePass и загружает учетные данные для
        различных сервисов, таких как Aliexpress, OpenAI, Gemini, Discord, Telegram и т.д.
        """
        kp = self._open_kp(3)
        if not kp:
            logger.error('Не удалось открыть базу данных KeePass')
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

        if not self._load_prestashop_credentials(kp):
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

        Args:
            retry (int): Количество попыток открытия базы данных.

        Returns:
             Optional[PyKeePass]: Объект PyKeePass, если открытие прошло успешно, иначе None.
        """
        while retry > 0:
            try:
                # Получаем пароль для KeePass
                password_file = Path(self.path.secrets / 'password.txt')
                if password_file.exists() and password_file.stat().st_size > 0 :
                    # Чтение пароля из файла, если он существует
                    password = password_file.read_text(encoding="utf-8").strip()
                else:
                    # Запрос пароля через консоль, если файл не существует или пуст
                    password = getpass.getpass('Enter KeePass master password: ').lower()

                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), password=password)
                return kp
            except Exception as ex:
                logger.error(f"Не удалось открыть базу данных KeePass, {retry - 1} попыток осталось. Ошибка: {ex}")
                retry -= 1
                if retry < 1:
                    logger.critical('Не удалось открыть базу данных KeePass после нескольких попыток', exc_info=True)
                    sys.exit()
        return None


    def _load_credentials_from_group(self, kp: PyKeePass, path: List[str], attribute_name: str, nested_attribute:str = None) -> bool:
        """
        Загружает учетные данные из группы KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.
            path (List[str]): Путь к группе в KeePass.
            attribute_name (str): Имя атрибута для сохранения данных.
            nested_attribute (str): Вложенный атрибут, если есть.

        Returns:
            bool: True, если загрузка прошла успешно, иначе False.
        """
        try:
            entries = kp.find_groups(path=path).entries
            for entry in entries:
                if nested_attribute:
                    target_attribute = getattr(getattr(self.credentials, attribute_name), nested_attribute)
                    setattr(target_attribute, entry.title, entry.custom_properties.get('api_key', None))
                else:
                    target_attribute = getattr(self.credentials, attribute_name)
                    setattr(target_attribute, entry.title, entry.custom_properties.get('api_key', None))
            return True
        except Exception as ex:
             logger.error(f"Не удалось извлечь данные из KeePass, путь: {path}. Ошибка: {ex}")
             return False


    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Aliexpress API из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если загрузка прошла успешно, иначе False.
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
        """
        Загружает учетные данные OpenAI из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если загрузка прошла успешно, иначе False.
        """
        try:
            openai_api_keys = kp.find_groups(path=['openai']).entries
            assistants = kp.find_groups(path=['openai', 'assistants']).entries

            for entry in openai_api_keys:
                setattr(self.credentials.openai, entry.title, entry.custom_properties.get('api_key', None))
                setattr(self.credentials.openai, entry.title, entry.custom_properties.get('project_api', None))
            for assistant in assistants:
                setattr(self.credentials.openai.assistant_id, assistant.title, assistant.custom_properties.get('assistant_id', None))
            return True
        except Exception as ex:
            logger.error(f"Не удалось извлечь учетные данные OpenAI из KeePass: {ex}")
            return False

    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """
         Загружает учетные данные GoogleAI из KeePass.

         Args:
             kp (PyKeePass): Объект PyKeePass.

         Returns:
             bool: True, если загрузка прошла успешно, иначе False.
         """
        return self._load_credentials_from_group(kp, ['gemini'], 'gemini')


    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """
         Загружает учетные данные Telegram из KeePass.

         Args:
             kp (PyKeePass): Объект PyKeePass.

         Returns:
             bool: True, если загрузка прошла успешно, иначе False.
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

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если загрузка прошла успешно, иначе False.
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

    def _load_prestashop_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если загрузка прошла успешно, иначе False.
        """
        try:
            for entry in kp.find_groups(path=['prestashop', 'clients']).entries:
                client_ns = SimpleNamespace()
                setattr(self.credentials.presta.client, entry.title, client_ns)
                current_client = getattr(self.credentials.presta.client, entry.title)

                setattr(current_client, 'api_key', entry.custom_properties.get('api_key', None))
                setattr(current_client, 'api_domain', entry.custom_properties.get('api_domain', None))
                setattr(current_client, 'db_server', entry.custom_properties.get('db_server', None))
                setattr(current_client, 'db_user', entry.custom_properties.get('db_user', None))
                setattr(current_client, 'db_password', entry.custom_properties.get('db_password', None))

            return True
        except Exception as ex:
            logger.error(f"Не удалось извлечь учетные данные PrestaShop из KeePass: {ex}")
            return False


    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Translations из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если загрузка прошла успешно, иначе False.
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

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если загрузка прошла успешно, иначе False.
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

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если загрузка прошла успешно, иначе False.
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

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если загрузка прошла успешно, иначе False.
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
        Возвращает текущую метку времени в формате год-месяц-день-часы-минуты-секунды-милисекунды.

        Этот метод возвращает строку, представляющую текущую метку времени, в формате
        `год_месяц_день_часы_минуты_секунды_миллисекунды`.

        Returns:
            str: Текущая метка времени в строковом формате.
        """
        timestamp = datetime.datetime.now().strftime(self.config.timestamp_format)
        # Вернём только первые 3 цифры миллисекунд, т.к. %f возвращает микросекунды (6 цифр)
        return f"{timestamp[:-3]}"


# Global instance of ProgamSettings
gs: ProgramSettings = ProgramSettings()
```