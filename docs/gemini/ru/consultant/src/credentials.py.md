## Анализ кода модуля `credentials.py`

**Качество кода**
9
-   Плюсы
    -   Код хорошо структурирован с использованием классов и функций.
    -   Применяется паттерн Singleton для `ProgramSettings`.
    -   Используются `dataclass` для хранения настроек, что делает код более читаемым и лаконичным.
    -   Применение `SimpleNamespace` для гибкого хранения конфигураций.
    -   Используется `Path` для работы с путями.
    -   Присутствует обработка ошибок через `try-except`, хотя и можно улучшить.
    -   Код содержит документацию к функциям, хотя и не полная, необходимо использовать rst.
-   Минусы
    -   Не везде используется `logger.error` для обработки ошибок, вместо этого `print` и `...`.
    -   Использование `print` для вывода сообщений об ошибках не соответствует стандартам логирования.
    -   Отсутствуют rst docstring для модуля и классов.
    -   Использование `sys.exit()` для завершения программы при ошибках.
    -   Не все методы `_load_*_credentials` возвращают `True` или `False`.
    -   В некоторых местах, таких как `_open_kp`, используются print и `...` в блоках `except`, вместо логирования ошибок.
    -   Дублирование кода при загрузке различных типов учетных данных.
    -   Отсутствует общий обработчик ошибок для всех методов `_load_*_credentials`.
    -  Использование `sys.path.insert(0, ...)` может вызвать проблемы с порядком импорта модулей.

**Рекомендации по улучшению**

1.  **Документирование**:
    - Добавить rst docstring к модулю, классу и методам.
    - Документировать все переменные, включая те, которые создаются внутри методов.
    - Использовать rst для примеров.
2.  **Логирование**:
    -   Использовать `logger.error` вместо `print` для вывода ошибок.
    -   Использовать `logger.critical` для критических ошибок, которые приводят к завершению программы.
    -   Добавить подробное логирование при открытии базы данных KeePass.
    -   Реализовать общую логику обработки ошибок в методах `_load_*_credentials`.
3.  **Обработка ошибок**:
    -   Избегать `...` в блоках `except`. Вместо этого, регистрировать ошибки с помощью `logger.error` и возвращать `False` из методов, если загрузка не удалась.
    -  Удалить `sys.exit()` из функций и дать возможность вызывающему коду обрабатывать ситуацию.
4.  **Структура**:
    -   Рефакторинг методов `_load_*_credentials`, чтобы избежать дублирования кода.
    -   Реализовать общий метод для загрузки данных из KeePass, который будет вызываться из других методов.
    -   Оптимизировать добавление бинарных путей в `sys.path`, чтобы избежать конфликтов.
    -   Пересмотреть логику добавления путей к бинарникам, так как их добавление в начало `sys.path` может вызвать конфликты.
5.  **Безопасность**:
    -  Рассмотреть варианты хранения пароля KeePass, чтобы избежать его хранения в открытом виде в файле `password.txt`.
6.  **Стиль**:
    - Использовать одинарные кавычки для строк в Python коде, двойные только в операциях вывода.

**Оптимизированный код**

```python
"""
Модуль для управления настройками проекта
=========================================================================================

Этот модуль содержит класс :class:`ProgramSettings`, который используется для хранения и управления
глобальными настройками проекта, включая пути, пароли и API-ключи.

Пример использования
--------------------

Пример инициализации настроек:

.. code-block:: python

    from src.credentials import ProgramSettings

    settings = ProgramSettings()
    print(settings.path.root)
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
    Определяет корневой каталог проекта.

    Ищет корневой каталог проекта, начиная с текущего каталога,
    двигаясь вверх по дереву каталогов, пока не найдет каталог, содержащий один из указанных файлов-маркеров.

    Args:
        marker_files (tuple): Кортеж с именами файлов или каталогов, которые идентифицируют корневой каталог проекта.

    Returns:
        Path: Путь к корневому каталогу проекта, или путь к каталогу, где находится скрипт, если корневой каталог не найден.
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

    Args:
        cls (class): Класс, для которого реализуется паттерн Singleton.

    Returns:
        function: Функция, возвращающая единственный экземпляр класса.
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

    Attributes:
        host_name (str): Имя хоста.
        base_dir (Path): Корневой каталог проекта.
        config (SimpleNamespace): Настройки из файла конфигурации.
        credentials (SimpleNamespace): Учетные данные для различных сервисов.
        MODE (str): Режим работы приложения ('dev', 'prod', и т.д.).
        path (SimpleNamespace): Пути к различным каталогам проекта.
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

        Загружает настройки из файла конфигурации, устанавливает пути и проверяет наличие новой версии.

        Raises:
            SystemExit: Если не удается загрузить файл конфигурации.
        """
        try:
            self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
        except Exception as ex:
            logger.error('Ошибка при загрузке настроек', exc_info=True)
            sys.exit(1)

        if not self.config:
             logger.error('Файл конфигурации не найден')
             sys.exit(1)

        self.config.timestamp_format = getattr(self.config, 'timestamp_format', '%y_%m_%d_%H_%M_%S_%f')
        self.config.project_name = self.base_dir.name

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
            google_drive=Path(getattr(self.config.path, 'google_drive', self.base_dir / 'google_drive')),
            # <- GOOGLE DRIVE ЧЕРЕЗ ЛОКАЛЬНЫЙ ДИСК (NOT API)
            external_storage=Path(getattr(self.config.path, 'external_storage',
                                         self.base_dir / 'external_storage')),  # <- Внешний диск
        )

        if check_latest_release(self.config.git_user, self.config.git):
            logger.info('Обновление не требуется')
            # Логика что делать когда есть новая версия hypo69 на github

        self.MODE = self.config.mode

        # Paths to bin directories
        gtk_bin_dir = self.path.bin / 'gtk' / 'gtk-nsis-pack' / 'bin'
        ffmpeg_bin_dir = self.base_dir / 'bin' / 'ffmpeg' / 'bin'
        graphviz_bin_dir = self.base_dir / 'bin' / 'graphviz' / 'bin'
        wkhtmltopdf_bin_dir = self.base_dir / 'bin' / 'wkhtmltopdf' / 'files' / 'bin'
        
        bin_paths = [self.base_dir, gtk_bin_dir, ffmpeg_bin_dir, graphviz_bin_dir, wkhtmltopdf_bin_dir]
        for bin_path in bin_paths:
           if str(bin_path) not in sys.path:
                sys.path.append(str(bin_path)) # <- определяю пути к бинарникам в системных путях
        
        os.environ['WEASYPRINT_DLL_DIRECTORIES'] = str(gtk_bin_dir)

        # Suppress GTK log output to the console
        warnings.filterwarnings('ignore', category=UserWarning)
        self._load_credentials()

    def _load_credentials(self) -> None:
        """
         Загружает учетные данные из KeePass.

         Открывает базу данных KeePass и загружает учетные данные для различных сервисов.
         В случае неудачи при загрузке учетных данных, выводится сообщение об ошибке в консоль.
        """
        kp = self._open_kp(3)
        if not kp:
             logger.critical('Не удалось открыть базу данных KeePass, выход из программы')
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
            logger.error('Не удалось загрузить учетные данные prestashop')

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

        Пытается открыть базу данных KeePass с заданным количеством попыток.

        Args:
            retry (int): Количество попыток открытия базы данных.

        Returns:
            Optional[PyKeePass]: Объект PyKeePass в случае успешного открытия, иначе None.
        """
        while retry > 0:
            try:
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG ~~~~~~~ ФАЙЛ ПАРОЛЯ В ОТКРЫТОМ ВИДЕ ~~~~~~~~~~~~~~~~~~~~~~~\
                password: str = (Path(self.path.secrets / 'password.txt').read_text(encoding='utf-8')
                                 or None)
                """password: содержит строку пароля в открытом виде. Можно удалить или сам файл или вытереть его содржимое """

                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'),
                              password=password or getpass.getpass(print('Enter KeePass master password: ').lower()))

                return kp
            except Exception as ex:
                 logger.error(f'Не удалось открыть базу данных KeePass. Осталось попыток: {retry - 1}', exc_info=True)
                 retry -= 1
                 if retry < 1:
                     logger.critical('Не удалось открыть базу данных KeePass после нескольких попыток', exc_info=True)
                     return None
        return None

    def _load_credentials_from_entry(self, kp: PyKeePass, path: List[str], service_name: str,
                                     fields: List[str]) -> bool:
        """
          Загружает учетные данные из KeePass по указанному пути.

         Args:
            kp (PyKeePass): Экземпляр базы данных KeePass.
            path (List[str]): Путь к группе в KeePass.
            service_name (str): Имя сервиса, для которого загружаются учетные данные.
            fields (List[str]): Список полей для загрузки.

         Returns:
            bool: True если загрузка прошла успешно, False в противном случае.
         """
        try:
            entry = kp.find_groups(path=path).entries[0]
            if not entry:
                logger.error(f'Не найдены учетные данные для {service_name} в KeePass')
                return False

            for field_name in fields:
                value = entry.custom_properties.get(field_name, None)
                setattr(getattr(self.credentials, service_name), field_name, value)

            if 'password' in fields:
                setattr(getattr(self.credentials, service_name), 'password', entry.password)

            return True

        except Exception as ex:
            logger.error(f'Не удалось извлечь учетные данные для {service_name} из KeePass', exc_info=True)
            return False


    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
         """ Загружает учетные данные Aliexpress API из KeePass.

         Args:
             kp (PyKeePass): Экземпляр базы данных KeePass.
         Returns:
             bool: True если загрузка прошла успешно, False в противном случае.
         """
         return self._load_credentials_from_entry(
             kp,
             ['suppliers', 'aliexpress', 'api'],
             'aliexpress',
             ['api_key', 'secret', 'tracking_id', 'email', 'password']
         )

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные OpenAI из KeePass.

        Args:
            kp (PyKeePass): Экземпляр базы данных KeePass.

        Returns:
             bool: True если загрузка прошла успешно, False в противном случае.
        """
        try:
            openai_api_keys = kp.find_groups(path=['openai']).entries
            assistants = kp.find_groups(path=['openai', 'assistants']).entries
            if not openai_api_keys or not assistants:
                logger.error('Не найдены учетные данные OpenAI в KeePass')
                return False

            for entry in openai_api_keys:
                 setattr(self.credentials.openai, entry.title, entry.custom_properties.get('api_key', None))
                 setattr(self.credentials.openai, entry.title, entry.custom_properties.get('project_api', None))
            for assistant in assistants:
                 setattr(self.credentials.openai.assistant_id, assistant.title,
                          assistant.custom_properties.get('assistant_id', None))
            return True

        except Exception as ex:
            logger.error('Не удалось извлечь учетные данные OpenAI из KeePass', exc_info=True)
            return False

    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные GoogleAI из KeePass.

        Args:
            kp (PyKeePass): Экземпляр базы данных KeePass.

        Returns:
             bool: True если загрузка прошла успешно, False в противном случае.
        """
        try:
            entries = kp.find_groups(path=['gemini']).entries
            if not entries:
                logger.error('Не найдены учетные данные GoogleAI в KeePass')
                return False

            for entry in entries:
                 setattr(self.credentials.gemini, entry.title, entry.custom_properties.get('api_key', None))
            return True

        except Exception as ex:
             logger.error('Не удалось извлечь учетные данные GoogleAI из KeePass', exc_info=True)
             return False

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Telegram из KeePass.

        Args:
            kp (PyKeePass): Экземпляр базы данных KeePass.

        Returns:
             bool: True если загрузка прошла успешно, False в противном случае.
        """
        try:
            entries = kp.find_groups(path=['telegram']).entries
            if not entries:
                logger.error('Не найдены учетные данные Telegram в KeePass')
                return False

            for entry in entries:
                setattr(self.credentials.telegram, entry.title, entry.custom_properties.get('token', None))
            return True
        except Exception as ex:
            logger.error('Не удалось извлечь учетные данные Telegram из KeePass', exc_info=True)
            return False

    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Discord из KeePass.

        Args:
            kp (PyKeePass): Экземпляр базы данных KeePass.

        Returns:
             bool: True если загрузка прошла успешно, False в противном случае.
        """
        return self._load_credentials_from_entry(
           kp,
            ['discord'],
            'discord',
            ['application_id', 'public_key', 'bot_token']
        )

    def _load_prestashop_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop из KeePass.

        Args:
            kp (PyKeePass): Экземпляр базы данных KeePass.

        Returns:
             bool: True если загрузка прошла успешно, False в противном случае.
        """
        try:
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
                    logger.error(f'Не удалось извлечь учетные данные prestashop из KeePass', exc_info=True)
                    return False

            return True

        except Exception as ex:
            logger.error(f'Не удалось извлечь учетные данные prestashop из KeePass', exc_info=True)
            return False

    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные для переводов PrestaShop из KeePass.

        Args:
            kp (PyKeePass): Экземпляр базы данных KeePass.

        Returns:
             bool: True если загрузка прошла успешно, False в противном случае.
        """
        return self._load_credentials_from_entry(
           kp,
           ['prestashop', 'translation'],
           'presta.translations',
           ['server', 'port', 'database', 'user', 'password']
        )

    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные SMTP из KeePass.

        Args:
            kp (PyKeePass): Экземпляр базы данных KeePass.

        Returns:
             bool: True если загрузка прошла успешно, False в противном случае.
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
            logger.error('Не удалось извлечь учетные данные SMTP из KeePass', exc_info=True)
            return False

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Facebook из KeePass.

         Args:
            kp (PyKeePass): Экземпляр базы данных KeePass.

         Returns:
            bool: True если загрузка прошла успешно, False в противном случае.
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
            logger.error('Не удалось извлечь учетные данные Facebook из KeePass', exc_info=True)
            return False

    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Google API из KeePass.

         Args:
            kp (PyKeePass): Экземпляр базы данных KeePass.

        Returns:
            bool: True если загрузка прошла успешно, False в противном случае.
        """
        try:
            entry = kp.find_groups(path=['google', 'gapi']).entries[0]
            self.credentials.gapi['api_key'] = entry.custom_properties.get('api_key', None)
            return True
        except Exception as ex:
            logger.error('Не удалось извлечь учетные данные GAPI из KeePass', exc_info=True)
            return False

    @property
    def now(self) -> str:
        """
        Возвращает текущую метку времени в формате год-месяц-день-часы-минуты-секунды-милисекунды.

        Этот метод возвращает строку, представляющую текущую метку времени, в формате `год_месяц_день_часы_минуты_секунды_миллисекунды`.

        Args:
            dformat (str, optional): Формат для метки времени. По умолчанию `\'%y_%m_%d_%H_%M_%S_%f\'`.

        Returns:
            str: Текущая метка времени в строковом формате.
        """
        timestamp = datetime.datetime.now().strftime(self.config.timestamp_format)
        # Вернём только первые 3 цифры миллисекунд, т.к. %f возвращает микросекунды (6 цифр)
        return f'{timestamp[:-3]}'


# Global instance of ProgamSettings
gs: ProgramSettings = ProgramSettings()