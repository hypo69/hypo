# Анализ кода модуля `src.credentials`

**Качество кода**
9
- Плюсы
    - Код хорошо документирован с использованием rst.
    - Присутствует описание структуры хранения данных.
    - Использование `j_loads_ns` для загрузки конфигурации.
    - Использование синглтона `ProgramSettings`.
    - Подробное описание назначения кода.
- Минусы
    -   Отсутствуют импорты `Path`, `sys`, `getpass`, `SimpleNamespace`, `PyKeePass`, `j_loads_ns`, `logger`.
    -   Не используется `from src.logger import logger` для логирования ошибок.
    -   Некоторые блоки `try-except` используют `...` и `print`, стоит заменить на логирование через `logger.error`.
    -   В комментариях встречаются слова "получаем", "делаем", нужно заменить на более конкретные формулировки.
    -   Отсутствуют docstring у функций `_open_kp`, `_load_aliexpress_credentials`, `_load_openai_credentials` и т.д.

**Рекомендации по улучшению**

1.  Добавить все недостающие импорты.
2.  Заменить `print` и `...` внутри `try-except` блоков на `logger.error` для более корректной обработки ошибок.
3.  Добавить docstring к функциям `_open_kp`, `_load_aliexpress_credentials`, `_load_openai_credentials` и т.д.
4.  Уточнить комментарии, заменив слова "получаем", "делаем" на более конкретные формулировки, такие как "проверка", "загрузка", "код исполняет...".
5.  Улучшить безопасность, пересмотрев хранение пароля от KeePass (не в текстовом файле).

**Оптимизированный код**

```python
"""
Модуль для загрузки и управления учетными данными.
=========================================================================================

Этот модуль содержит класс :class:`ProgramSettings`, который используется для
загрузки и хранения учетных данных (ключи API, пароли и т. д.) из файла базы
данных KeePass `credentials.kdbx`. Он также включает функцию `set_project_root`
для определения корневого каталога проекта.

Пример использования
--------------------

Пример использования класса `ProgramSettings`:

.. code-block:: python

    settings = ProgramSettings()
    api_key = settings.credentials.openai.api_key
"""
import sys
import getpass
from pathlib import Path
from types import SimpleNamespace

from pykeepass import PyKeePass
from src.utils.jjson import j_loads_ns
from src.logger import logger #  Импорт логгера

def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневой каталог проекта, начиная с текущего каталога файла.
    
    Поиск идет вверх по каталогам, останавливаясь на первом каталоге, содержащем любой из маркеров.

    Args:
        marker_files (tuple): Имена файлов или каталогов, используемые для определения корневого каталога проекта.

    Returns:
        Path: Путь к корневому каталогу, если найден, в противном случае - путь к каталогу, где находится скрипт.
    
    Example:
        >>> set_project_root()
        PosixPath('/path/to/your/project')
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
    Декоратор для создания синглтон-класса.

    Args:
        cls: Класс, который нужно преобразовать в синглтон.

    Returns:
        function: Функция, возвращающая экземпляр синглтон-класса.

    Example:
    
    .. code-block:: python
    
        @singleton
        class MyClass:
            def __init__(self):
                self.value = 10
        
        instance1 = MyClass()
        instance2 = MyClass()
        
        print(instance1.value)
        instance2.value = 20
        print(instance1.value)
        print(instance2.value)

    """
    instances = {}

    def getinstance(**kwargs):
        if cls not in instances:
            instances[cls] = cls(**kwargs)
        return instances[cls]

    return getinstance


@singleton
class ProgramSettings:
    """
    Класс для настроек программы.

    Устанавливает основные параметры и настройки проекта,
    загружает конфигурацию из `config.json` и учетные данные из файла
    базы данных KeePass `credentials.kdbx`.

    Attributes:
        host_name (str): Имя хоста.
        base_dir (Path): Путь к корневому каталогу проекта.
        config (SimpleNamespace): Объект, содержащий конфигурацию проекта.
        credentials (SimpleNamespace): Объект, содержащий учетные данные.
        MODE (str): Режим работы проекта (например, 'dev', 'prod').
        path (SimpleNamespace): Объект, содержащий пути к различным каталогам проекта.

    Example:
       
       .. code-block:: python

            settings = ProgramSettings()
            print(settings.config.project_name)
            print(settings.credentials.openai.api_key)
    """
    host_name: str = 'localhost'
    base_dir: Path = set_project_root()

    def __init__(self, **kwargs):
        """
        Инициализация экземпляра класса.

        Загружает конфигурацию проекта из `config.json`.
        Инициализирует атрибут `path` путями к различным каталогам проекта.
        Вызывает `check_latest_release` для проверки новой версии проекта.
        Загружает учетные данные из `credentials.kdbx`.
        """
        self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
        if not self.config:
            logger.error('Ошибка при загрузке настроек')  #  Логирование ошибки
            return
        self.config.project_name = self.base_dir.name
        self.MODE = self.config.available_modes[0] #TODO mode

        self.path = SimpleNamespace(**{
            'root': self.base_dir,
            'src': self.base_dir / 'src',
            'log': self.base_dir / 'log',
            'tmp': self.base_dir / 'tmp',
            'storage': self.base_dir / 'storage',
            'secrets': self.base_dir / 'secrets',
            'gdrive': self.base_dir / 'gdrive'
        })

        self.credentials = SimpleNamespace()
        self._load_credentials()



    def _load_credentials(self) -> None:
        """
        Загружает учетные данные из KeePass.
        """
        kp = self._open_kp()
        if not kp:
            logger.error('Не удалось открыть базу данных KeePass')#  Логирование ошибки
            return

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

    def _open_kp(self, retry: int = 3) -> PyKeePass | None:
        """
        Открывает базу данных KeePass.

        Args:
            retry (int): Количество попыток.

        Returns:
            PyKeePass | None: Объект PyKeePass или None в случае неудачи.
        """
        while retry > 0:
            try:
                password: str = (Path(self.path.secrets / 'password.txt').read_text(encoding='utf-8') or None)
                kp = PyKeePass(
                    str(self.path.secrets / 'credentials.kdbx'),
                    password=password or getpass.getpass(print('Введите мастер-пароль KeePass: ').lower())
                )
                return kp
            except Exception as ex:
                logger.error(f'Не удалось открыть базу данных KeePass. Ошибка: {ex}, осталось {retry-1} попыток.') #  Логирование ошибки
                retry -= 1
                if retry < 1:
                    logger.critical('Не удалось открыть базу данных KeePass после нескольких попыток', exc_info=True) #  Логирование критической ошибки
                    sys.exit()
        return None

    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """
         Загружает учетные данные Aliexpress из KeePass.

         Args:
            kp (PyKeePass): Объект PyKeePass.
         Returns:
             bool: True, если загрузка прошла успешно, False - в противном случае.
        """
        try:
            group = kp.find_groups(path='suppliers/aliexpress/api')[0]
            entry = group.entries[0]
            self.credentials.aliexpress = SimpleNamespace(
                api_key=entry.get_custom_property('api_key'),
                secret=entry.get_custom_property('secret'),
                tracking_id=entry.get_custom_property('tracking_id'),
                email=entry.get_custom_property('email'),
                password=entry.get_custom_property('password'),
            )
            return True
        except Exception as ex:
            logger.error(f'Ошибка загрузки учетных данных Aliexpress: {ex}')#  Логирование ошибки
            return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные OpenAI из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
             bool: True, если загрузка прошла успешно, False - в противном случае.
        """
        try:
            group = kp.find_groups(path='openai')[0]
            entry = group.entries[0]
            self.credentials.openai = SimpleNamespace(api_key=entry.password)
            
            group = kp.find_groups(path='openai/assistants')[0]
            entry = group.entries[0]
            self.credentials.openai.assistant_id = entry.password
            return True
        except Exception as ex:
            logger.error(f'Ошибка загрузки учетных данных OpenAI: {ex}')#  Логирование ошибки
            return False

    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные GoogleAI из KeePass.
        Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
             bool: True, если загрузка прошла успешно, False - в противном случае.
        """
        try:
            group = kp.find_groups(path='gemini')[0]
            entry = group.entries[0]
            self.credentials.gemini = SimpleNamespace(api_key=entry.password)
            return True
        except Exception as ex:
            logger.error(f'Ошибка загрузки учетных данных GoogleAI: {ex}')#  Логирование ошибки
            return False

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Telegram из KeePass.
        Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
             bool: True, если загрузка прошла успешно, False - в противном случае.
        """
        try:
            group = kp.find_groups(path='telegram')[0]
            entry = group.entries[0]
            self.credentials.telegram = SimpleNamespace(token=entry.password)
            return True
        except Exception as ex:
            logger.error(f'Ошибка загрузки учетных данных Telegram: {ex}')#  Логирование ошибки
            return False

    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Discord из KeePass.
        Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
             bool: True, если загрузка прошла успешно, False - в противном случае.
        """
        try:
            group = kp.find_groups(path='discord')[0]
            entry = group.entries[0]
            self.credentials.discord = SimpleNamespace(
                application_id=entry.get_custom_property('application_id'),
                public_key=entry.get_custom_property('public_key'),
                bot_token=entry.password
            )
            return True
        except Exception as ex:
            logger.error(f'Ошибка загрузки учетных данных Discord: {ex}')#  Логирование ошибки
            return False

    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
         """
        Загружает учетные данные PrestaShop из KeePass.
         Args:
            kp (PyKeePass): Объект PyKeePass.
         Returns:
             bool: True, если загрузка прошла успешно, False - в противном случае.
        """
        try:
            group = kp.find_groups(path='prestashop/clients')[0]
            entry = group.entries[0]
            self.credentials.presta = SimpleNamespace(
                client=SimpleNamespace(
                    api_key=entry.get_custom_property('api_key'),
                    api_domain=entry.get_custom_property('api_domain'),
                    db_server=entry.get_custom_property('db_server'),
                    db_user=entry.get_custom_property('db_user'),
                    db_password=entry.get_custom_property('db_password')
                )
            )
            return True
        except Exception as ex:
             logger.error(f'Ошибка загрузки учетных данных PrestaShop: {ex}')#  Логирование ошибки
             return False

    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop Translations из KeePass.
        Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
             bool: True, если загрузка прошла успешно, False - в противном случае.
        """
        try:
            group = kp.find_groups(path='prestashop/translation')[0]
            entry = group.entries[0]
            self.credentials.presta.translations = SimpleNamespace(
                server=entry.get_custom_property('server'),
                port=entry.get_custom_property('port'),
                database=entry.get_custom_property('database'),
                user=entry.get_custom_property('user'),
                password=entry.get_custom_property('password'),
            )
            return True
        except Exception as ex:
            logger.error(f'Ошибка загрузки учетных данных PrestaShop Translations: {ex}')#  Логирование ошибки
            return False

    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные SMTP из KeePass.
         Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
             bool: True, если загрузка прошла успешно, False - в противном случае.
        """
        try:
            group = kp.find_groups(path='smtp')[0]
            entry = group.entries[0]
            self.credentials.smtp = SimpleNamespace(
                server=entry.get_custom_property('server'),
                port=entry.get_custom_property('port'),
                user=entry.get_custom_property('user'),
                password=entry.password
            )
            return True
        except Exception as ex:
            logger.error(f'Ошибка загрузки учетных данных SMTP: {ex}')#  Логирование ошибки
            return False

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Facebook из KeePass.
        Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
             bool: True, если загрузка прошла успешно, False - в противном случае.
        """
        try:
            group = kp.find_groups(path='facebook')[0]
            entry = group.entries[0]
            self.credentials.facebook = SimpleNamespace(
                app_id=entry.get_custom_property('app_id'),
                app_secret=entry.get_custom_property('app_secret'),
                access_token=entry.get_custom_property('access_token')
            )
            return True
        except Exception as ex:
            logger.error(f'Ошибка загрузки учетных данных Facebook: {ex}')#  Логирование ошибки
            return False

    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Google API из KeePass.
        Args:
            kp (PyKeePass): Объект PyKeePass.
        Returns:
             bool: True, если загрузка прошла успешно, False - в противном случае.
        """
        try:
            group = kp.find_groups(path='google/gapi')[0]
            entry = group.entries[0]
            self.credentials.gapi = SimpleNamespace(api_key=entry.password)
            return True
        except Exception as ex:
             logger.error(f'Ошибка загрузки учетных данных Google API: {ex}')#  Логирование ошибки
             return False

    def now(self) -> str:
        """
         Возвращает текущую временную метку в формате, указанном в `config.json`.
        """
        from datetime import datetime
        return datetime.now().strftime(self.config.time_format)


# Глобальный экземпляр ProgramSettings
gs: ProgramSettings = ProgramSettings()
```