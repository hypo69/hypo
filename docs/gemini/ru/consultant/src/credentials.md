# Анализ кода модуля `src.credentials`

**Качество кода**
8
-   Плюсы
    -   Хорошая документация в формате RST.
    -   Использование `j_loads_ns` для загрузки JSON-конфигурации.
    -   Применение singleton декоратора для класса `ProgramSettings`.
    -   Четкая структура работы с KeePass и разделение на отдельные методы для загрузки разных типов учетных данных.
    -   Документированная структура базы данных KeePass.
    -   Использование глобальной переменной gs.
-   Минусы
    -   В коде встречается `...`, что нежелательно (не законченный код).
    -   Использование `getpass.getpass` без дополнительного условия может привести к проблемам при работе в автоматическом режиме.
    -   Отсутствует явная обработка некоторых ошибок (например, `FileNotFoundError` при чтении `password.txt`).
    -   В некоторых местах `logger.error` используется без `exc_info=True`, что затрудняет отладку.
    -   Использование print() в `_open_kp` для вывода сообщений, лучше использовать `logger.info/debug`.
    -   Вложенность try/except в `_open_kp`.

**Рекомендации по улучшению**

1.  Удалить все `...` и дописать код.
2.  Обработать ошибку `FileNotFoundError` при чтении файла пароля `password.txt`.
3.  Использовать `logger.error(..., exc_info=True)` для более полной информации об ошибках.
4.  Перенести вывод в `_open_kp` с `print` на `logger.info/debug`.
5.  Упростить `try/except` в `_open_kp` за счет обработки ошибки открытия файла.
6.  Добавить аннотации типов.
7.  Перенести логику проверки пути к `sys.path` в начало функции `set_project_root`.
8.  Разделить логику получения пароля на отдельную функцию.
9.  Добавить docstring к методам `_open_kp`.
10. Использовать Path.read_text() в `_open_kp`.
11. Документировать все атрибуты класса `ProgramSettings`
12. Убрать множественное наследование.
13. Добавить проверку существования каталога `secrets` в `ProgramSettings`.

**Оптимизированный код**

```python
"""
Модуль для загрузки и управления настройками и учетными данными приложения.
=========================================================================================

Этот модуль предоставляет функциональность для загрузки настроек приложения из файла `config.json`,
управления учетными данными из базы данных KeePass `credentials.kdbx`,
и определения корневой директории проекта.

Он включает в себя класс :class:`ProgramSettings`, который является основным компонентом для доступа
к настройкам и учетным данным в других частях проекта.

Пример использования
--------------------

.. code-block:: python

    from src.credentials import gs

    # Доступ к настройкам
    project_name = gs.config.project_name
    log_dir = gs.path.log

    # Доступ к учетным данным
    api_key = gs.credentials.openai.api_key

"""
import getpass
import sys
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Tuple
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns
from pykeepass import PyKeePass
from datetime import datetime

def set_project_root(marker_files: Tuple[str, ...] = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с текущей директории файла,
    переходя вверх по иерархии каталогов до тех пор, пока не будет найден каталог,
    содержащий один из указанных файлов-маркеров.

    Args:
        marker_files (tuple, optional): Список имен файлов или директорий, используемых для идентификации корневой директории проекта.
        По умолчанию: ('__root__', '.git').

    Returns:
        Path: Путь к корневой директории проекта, если она найдена, или путь к директории, где находится скрипт, если нет.

    Example:
        >>> project_root = set_project_root(marker_files=('.git', 'pyproject.toml'))
        >>> print(project_root) # doctest: +SKIP
        /path/to/your/project
    """
    current_path = Path(__file__).resolve().parent
    __root__ = current_path

    if any((current_path / marker).exists() for marker in marker_files):
        __root__ = current_path

    else:
        for parent in current_path.parents:
            if any((parent / marker).exists() for marker in marker_files):
                __root__ = parent
                break
    
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))

    return __root__


def singleton(cls):
    """
    Декоратор для создания класса-одиночки (singleton).
    
    Args:
        cls (class): Класс, который нужно преобразовать в singleton.
    
    Returns:
        function: Функция, возвращающая экземпляр singleton-класса.
    """
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


def _get_keepass_password(secrets_path:Path)->str | None:
    """
    Получает пароль для KeePass из файла password.txt, если он существует.

    Args:
        secrets_path(Path): Путь к каталогу secrets.

    Returns:
        str | None: Пароль KeePass или None, если файл не найден или пуст.
    """
    password_file = secrets_path / 'password.txt'
    if password_file.exists():
        try:
          return password_file.read_text(encoding='utf-8').strip()
        except Exception as ex:
             logger.error(f'Ошибка чтения файла пароля {password_file=}', exc_info=True)
    return None

@singleton
class ProgramSettings:
    """
    Класс для управления настройками программы, включая загрузку конфигурации,
    учетных данных и других параметров, необходимых для работы приложения.

    Attributes:
        host_name (str): Имя хоста.
        base_dir (Path): Путь к корневой директории проекта.
        config (SimpleNamespace): Объект, содержащий настройки проекта из config.json.
        credentials (SimpleNamespace): Объект, содержащий учетные данные, загруженные из KeePass.
        MODE (str): Режим работы проекта (например, 'dev', 'prod').
        path (SimpleNamespace): Объект, содержащий пути к различным директориям проекта.

    """
    def __init__(self, **kwargs):
        """
        Инициализирует экземпляр класса ProgramSettings, загружая настройки из `config.json`,
        устанавливая пути к директориям, проверяя наличие новой версии и загружая учетные данные
        из KeePass.

        Args:
            kwargs (dict): Дополнительные параметры инициализации.

        """
        self.host_name:str = 'localhost'
        self.base_dir: Path = set_project_root()
        self.config: SimpleNamespace = self._load_config()
        self.credentials: SimpleNamespace = SimpleNamespace()
        self.MODE: str = self.config.mode if hasattr(self.config, 'mode') else 'dev'

        self.path: SimpleNamespace = SimpleNamespace(
            log = self.base_dir / self.config.paths.log if hasattr(self.config, 'paths') and hasattr(self.config.paths, 'log') else self.base_dir / 'log',
            temp = self.base_dir / self.config.paths.temp if hasattr(self.config, 'paths') and hasattr(self.config.paths, 'temp') else self.base_dir / 'temp',
            external = self.base_dir / self.config.paths.external if hasattr(self.config, 'paths') and hasattr(self.config.paths, 'external') else self.base_dir / 'external',
            secrets = self.base_dir / 'secrets',
            gdrive = self.base_dir / self.config.paths.gdrive if hasattr(self.config, 'paths') and hasattr(self.config.paths, 'gdrive') else self.base_dir / 'gdrive'
        )
        
        if not self.path.secrets.exists():
            logger.critical(f'Директория secrets не найдена {self.path.secrets=}')
            sys.exit()

        self.config.project_name = self.base_dir.name
        self._load_credentials()

    def _load_config(self) -> SimpleNamespace:
        """
        Загружает конфигурацию из `config.json`.

        Returns:
            SimpleNamespace: Объект, содержащий конфигурацию.

        """
        config = j_loads_ns(self.base_dir / 'src' / 'config.json')
        if not config:
            logger.error('Ошибка загрузки настроек')
            sys.exit()
        return config

    def _load_credentials(self) -> None:
        """
         Загружает учетные данные из KeePass.
        """
        kp = self._open_kp()
        if kp:
            self._load_aliexpress_credentials(kp)
            self._load_openai_credentials(kp)
            self._load_gemini_credentials(kp)
            self._load_telegram_credentials(kp)
            self._load_discord_credentials(kp)
            self._load_PrestaShop_credentials(kp)
            self._load_presta_translations_credentials(kp)
            self._load_smtp_credentials(kp)
            self._load_facebook_credentials(kp)
            self._load_gapi_credentials(kp)
        else:
            logger.critical('Не удалось загрузить учетные данные из KeePass.')
            sys.exit()

    def _open_kp(self, retry: int = 3) -> PyKeePass | None:
        """
        Открывает базу данных KeePass.
        
        Args:
            retry (int, optional): Количество попыток открытия. По умолчанию: 3.
        
        Returns:
            PyKeePass | None: Объект PyKeePass, если база данных успешно открыта, иначе None.
        
        Raises:
            SystemExit: Если не удалось открыть базу данных после нескольких попыток.
        """
        while retry > 0:
            try:
                password = _get_keepass_password(self.path.secrets)
                if not password:
                    password = getpass.getpass('Enter KeePass master password: ').strip()
                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), password=password)
                return kp
            except Exception as ex:
                logger.error(f'Не удалось открыть базу данных KeePass. Осталось {retry-1} попыток.', exc_info=True)
                retry -= 1
        logger.critical('Не удалось открыть базу данных KeePass после нескольких попыток.', exc_info=True)
        sys.exit()
        

    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Aliexpress из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
            bool: True в случае успешной загрузки, False в противном случае.

        """
        try:
            group = kp.find_groups(name='aliexpress')[0]
            entry = group.find_entries(name='api')[0]
            self.credentials.aliexpress = SimpleNamespace(
                api_key = entry.get_custom_property('api_key'),
                secret = entry.get_custom_property('secret'),
                tracking_id = entry.get_custom_property('tracking_id'),
                email = entry.get_custom_property('email'),
                password = entry.password
            )
            return True
        except Exception as ex:
            logger.error(f'Ошибка загрузки Aliexpress credentials {ex=}', exc_info=True)
            return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные OpenAI из KeePass.

         Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
            bool: True в случае успешной загрузки, False в противном случае.

        """
        try:
            group = kp.find_groups(name='openai')[0]
            entry = group.find_entries(name='entry')[0]
            self.credentials.openai = SimpleNamespace(
                api_key = entry.password
            )
            entry = group.find_groups(name='assistants')[0].find_entries(name='entry')[0]
            self.credentials.openai.assistant_id = entry.password

            return True
        except Exception as ex:
            logger.error(f'Ошибка загрузки OpenAI credentials {ex=}', exc_info=True)
            return False

    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
         """
        Загружает учетные данные Gemini из KeePass.

         Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
        """
         try:
             group = kp.find_groups(name='gemini')[0]
             entry = group.find_entries(name='entry')[0]
             self.credentials.gemini = SimpleNamespace(
                 api_key = entry.password
             )
             return True
         except Exception as ex:
            logger.error(f'Ошибка загрузки Gemini credentials {ex=}', exc_info=True)
            return False

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
         """
        Загружает учетные данные Telegram из KeePass.

         Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
        """
         try:
             group = kp.find_groups(name='telegram')[0]
             entry = group.find_entries(name='entry')[0]
             self.credentials.telegram = SimpleNamespace(
                 token = entry.password
             )
             return True
         except Exception as ex:
            logger.error(f'Ошибка загрузки Telegram credentials {ex=}', exc_info=True)
            return False

    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
         """
        Загружает учетные данные Discord из KeePass.

         Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
        """
         try:
             group = kp.find_groups(name='discord')[0]
             entry = group.find_entries(name='entry')[0]
             self.credentials.discord = SimpleNamespace(
                 application_id = entry.get_custom_property('application_id'),
                 public_key = entry.get_custom_property('public_key'),
                 bot_token = entry.password
             )
             return True
         except Exception as ex:
            logger.error(f'Ошибка загрузки Discord credentials {ex=}', exc_info=True)
            return False

    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
         """
        Загружает учетные данные PrestaShop из KeePass.

         Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
        """
         try:
            group = kp.find_groups(name='prestashop')[0]
            entry = group.find_entries(name='entry')[0]
            self.credentials.presta = SimpleNamespace(
                api_key = entry.get_custom_property('api_key'),
                api_domain = entry.get_custom_property('api_domain'),
                db_server = entry.get_custom_property('db_server'),
                db_user = entry.get_custom_property('db_user'),
                db_password = entry.password
            )
            entry = group.find_groups(name='clients')[0].find_entries(name='entry')[0]
            self.credentials.presta.client = SimpleNamespace(
                api_key = entry.get_custom_property('api_key'),
                api_domain = entry.get_custom_property('api_domain'),
                db_server = entry.get_custom_property('db_server'),
                db_user = entry.get_custom_property('db_user'),
                db_password = entry.password
            )
            return True
         except Exception as ex:
            logger.error(f'Ошибка загрузки PrestaShop credentials {ex=}', exc_info=True)
            return False


    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop Translations из KeePass.

         Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
        """
        try:
            group = kp.find_groups(name='prestashop')[0]
            entry = group.find_groups(name='translation')[0].find_entries(name='entry')[0]

            self.credentials.presta.translations = SimpleNamespace(
                server = entry.get_custom_property('server'),
                port = entry.get_custom_property('port'),
                database = entry.get_custom_property('database'),
                user = entry.get_custom_property('user'),
                password = entry.password
            )
            return True
        except Exception as ex:
             logger.error(f'Ошибка загрузки PrestaShop translations credentials {ex=}', exc_info=True)
             return False

    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные SMTP из KeePass.

         Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
        """
        try:
            group = kp.find_groups(name='smtp')[0]
            entry = group.find_entries(name='entry')[0]
            self.credentials.smtp = SimpleNamespace(
                server = entry.get_custom_property('server'),
                port = entry.get_custom_property('port'),
                user = entry.get_custom_property('user'),
                password = entry.password
            )
            return True
        except Exception as ex:
            logger.error(f'Ошибка загрузки SMTP credentials {ex=}', exc_info=True)
            return False

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Facebook из KeePass.

         Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
        """
        try:
            group = kp.find_groups(name='facebook')[0]
            entry = group.find_entries(name='entry')[0]
            self.credentials.facebook = SimpleNamespace(
                 app_id = entry.get_custom_property('app_id'),
                 app_secret = entry.get_custom_property('app_secret'),
                 access_token = entry.password
            )
            return True
        except Exception as ex:
             logger.error(f'Ошибка загрузки Facebook credentials {ex=}', exc_info=True)
             return False

    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Google API из KeePass.

         Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
        """
        try:
            group = kp.find_groups(name='google')[0]
            entry = group.find_groups(name='gapi')[0].find_entries(name='entry')[0]
            self.credentials.gapi = SimpleNamespace(
                 api_key = entry.password
            )
            return True
        except Exception as ex:
            logger.error(f'Ошибка загрузки Google API credentials {ex=}', exc_info=True)
            return False

    def now(self) -> str:
        """
        Возвращает текущую метку времени в формате, указанном в `config.json`.
         Returns:
           str: Строка с текущей датой и временем.
        """
        time_format = self.config.time_format if hasattr(self.config, 'time_format') else "%Y-%m-%d %H:%M:%S"
        return datetime.now().strftime(time_format)

# Global instance of ProgramSettings
gs: ProgramSettings = ProgramSettings()
```