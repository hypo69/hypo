# Анализ кода модуля `src.credentials`

## Качество кода:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Подробное описание функциональности модуля и классов в документации.
    - Использование `PyKeePass` для управления учетными данными.
    - Наличие механизма определения корневой директории проекта.
    - Использование `j_loads_ns` для загрузки конфигурации.
    - Наличие глобального экземпляра `ProgramSettings` для удобства доступа к настройкам.
- **Минусы**:
    - Использование `print` для вывода сообщений об ошибках (следует использовать `logger.error`).
    - Обработка исключений с использованием `...` вместо `pass` или более конкретной обработки.
    - Хранение пароля в файле `password.txt` (потенциальная уязвимость).
    - Отсутствие RST-документации в коде.
    - Непоследовательное использование одинарных и двойных кавычек.
    - Не все импорты приведены в коде.
    - Не используется `from src.logger.logger import logger`
    - Использование `sys.exit()` в блоке обработки исключений.
    - Не используются асинхронные методы.

## Рекомендации по улучшению:

1.  **Форматирование:**
    -   Использовать одинарные кавычки для строк в Python-коде, двойные кавычки только для вывода.
    -   Выровнять названия функций, переменных и импортов.

2.  **Логирование:**
    -   Заменить все `print` на `logger.error`, `logger.critical`.
    -   Использовать `from src.logger.logger import logger`.
    -   Избегать перехвата всех исключений `Exception as ex`.

3.  **Безопасность:**
    -   Убрать хранение пароля в `password.txt`. Реализовать ввод пароля в консоли в режиме разработки.
    -   Использовать `getpass.getpass` для ввода пароля.

4.  **Обработка исключений:**
    -   Заменить `...` на `pass` или более конкретную обработку ошибок.
    -   Использовать `logger.critical` вместо `sys.exit()` для критических ошибок.

5.  **Документация:**
    -   Добавить RST-документацию для всех функций и классов.
    -   Использовать `"""` для docstring.

6.  **Импорты:**
     - Добавить все необходимые импорты в начало файла.

7.  **Общее:**
    -   Удалить лишние комментарии.

## Оптимизированный код:

```python
"""
Модуль для работы с настройками программы и учетными данными.
=============================================================

Модуль содержит класс :class:`ProgramSettings`, который загружает и хранит настройки
и учетные данные, необходимые для работы проекта.

Пример использования
----------------------
.. code-block:: python

    from src.credentials import gs

    print(gs.config.project_name)
"""

import sys
import getpass
from pathlib import Path
from types import SimpleNamespace
from pykeepass import PyKeePass
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger # Используем импорт из src.logger.logger
from functools import wraps

class CredentialsError(Exception):
    """
    Исключение для ошибок, связанных с учетными данными.
    """
    pass

class DefaultSettingsException(Exception):
    """
    Исключение для ошибок, связанных с настройками по умолчанию.
    """
    pass

def singleton(cls):
    """
    Декоратор для создания класса-синглтона.
    
    :param cls: Класс, который нужно преобразовать в синглтон.
    :type cls: class
    :return: Функция, возвращающая экземпляр класса-синглтона.
    :rtype: function
    """
    instance = None

    @wraps(cls)
    def wrapper(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance
    return wrapper


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с текущей директории файла,
    ища вверх и останавливаясь на первой директории, содержащей любой из маркерных файлов.

    :param marker_files: Имена файлов или директорий для идентификации корневой директории проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если найдена, иначе директория, где находится скрипт.
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


@singleton
class ProgramSettings:
    """
    Класс настроек программы.

    Устанавливает основные параметры и настройки проекта. Загружает конфигурацию из
    `config.json` и данные учетных данных из файла `credentials.kdbx` в базе данных KeePass.

    :ivar host_name: Имя хоста.
    :vartype host_name: str
    :ivar base_dir: Путь к корневой директории проекта.
    :vartype base_dir: Path
    :ivar config: Объект, содержащий конфигурацию проекта.
    :vartype config: SimpleNamespace
    :ivar credentials: Объект, содержащий учетные данные.
    :vartype credentials: SimpleNamespace
    :ivar MODE: Режим работы проекта (например, 'dev', 'prod').
    :vartype MODE: str
    :ivar path: Объект, содержащий пути к различным директориям проекта.
    :vartype path: SimpleNamespace
    """

    def __init__(self, **kwargs):
        """
        Инициализирует экземпляр класса ProgramSettings.

        Загружает конфигурацию проекта из `config.json`, инициализирует атрибут `path`
        с путями к различным директориям проекта, выполняет проверку на наличие новой версии
        проекта и загружает учетные данные из `credentials.kdbx`.

        :param kwargs: Произвольные именованные аргументы.
        :type kwargs: dict
        """
        self.host_name: str = "localhost" # Пример
        self.base_dir: Path = set_project_root()
        self.config: SimpleNamespace = self._load_config()
        self.path: SimpleNamespace = self._init_paths()
        self.credentials: SimpleNamespace = SimpleNamespace() # Инициализация credentials
        self._load_credentials()

        if not self.config:
           logger.error('Ошибка при загрузке настроек')
           raise DefaultSettingsException('Ошибка при загрузке настроек')

        self.config.project_name = self.base_dir.name

    def _load_config(self) -> SimpleNamespace:
        """
        Загружает конфигурацию из файла `config.json`.

        :return: Объект SimpleNamespace с конфигурацией.
        :rtype: SimpleNamespace
        """
        config_path = self.base_dir / 'src' / 'config.json'
        config = j_loads_ns(config_path)
        if not config:
           logger.error(f'Не удалось загрузить файл конфигурации: {config_path}')
        return config

    def _init_paths(self) -> SimpleNamespace:
        """
        Инициализирует пути к различным директориям проекта.

        :return: Объект SimpleNamespace с путями.
        :rtype: SimpleNamespace
        """
        return SimpleNamespace(
            logs=self.base_dir / "logs",
            tmp=self.base_dir / "tmp",
            external=self.base_dir / "external",
            gdrive=self.base_dir / "gdrive",
            secrets=self.base_dir / "secrets"
        )

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
            logger.error('Не удалось загрузить учетные данные из KeePass')


    def _open_kp(self, retry: int = 3) -> PyKeePass | None:
        """
        Открывает базу данных KeePass.

        :param retry: Количество попыток открытия базы данных.
        :type retry: int
        :return: Объект PyKeePass, если база данных открыта успешно, иначе None.
        :rtype: PyKeePass | None
        """
        while retry > 0:
            try:
                password_file = self.path.secrets / 'password.txt'
                if password_file.exists():
                    password = password_file.read_text(encoding='utf-8').strip()
                else:
                    password = getpass.getpass(f'Введите мастер-пароль KeePass: ').strip() # Используем getpass
                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), password=password)
                return kp
            except Exception as ex:
                logger.error(f"Не удалось открыть базу данных KeePass. Исключение: {ex}, осталось попыток: {retry-1}.")
                retry -= 1
        logger.critical('Не удалось открыть базу данных KeePass после нескольких попыток', exc_info=True)
        return None

    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Aliexpress из KeePass.
        
        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если учетные данные загружены успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='aliexpress')[0]
            entry = group.find_entries(title='api')[0]
            self.credentials.aliexpress = SimpleNamespace(
                api_key=entry.get_custom_property('api_key'),
                secret=entry.get_custom_property('secret'),
                tracking_id=entry.get_custom_property('tracking_id'),
                email=entry.get_custom_property('email'),
                password=entry.get_custom_property('password'),
            )
            return True
        except Exception as e:
            logger.error(f'Ошибка при загрузке учетных данных Aliexpress: {e}')
            return False


    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные OpenAI из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если учетные данные загружены успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='openai')[0]
            api_entry = group.find_entries(title='entry')[0]
            assistants_entry = group.find_groups(name='assistants')[0].find_entries(title='entry')[0]

            self.credentials.openai = SimpleNamespace(
                api_key=api_entry.get_custom_property('api_key'),
                assistant_id=assistants_entry.get_custom_property('assistant_id'),
            )
            return True
        except Exception as e:
            logger.error(f'Ошибка при загрузке учетных данных OpenAI: {e}')
            return False

    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные GoogleAI из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если учетные данные загружены успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='gemini')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.gemini = SimpleNamespace(
                api_key=entry.get_custom_property('api_key'),
            )
            return True
        except Exception as e:
            logger.error(f'Ошибка при загрузке учетных данных Gemini: {e}')
            return False

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
         """
         Загружает учетные данные Telegram из KeePass.
         
         :param kp: Объект PyKeePass.
         :type kp: PyKeePass
         :return: True, если учетные данные загружены успешно, иначе False.
         :rtype: bool
         """
         try:
             group = kp.find_groups(name='telegram')[0]
             entry = group.find_entries(title='entry')[0]
             self.credentials.telegram = SimpleNamespace(
                 token=entry.get_custom_property('token'),
             )
             return True
         except Exception as e:
             logger.error(f'Ошибка при загрузке учетных данных Telegram: {e}')
             return False


    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Discord из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если учетные данные загружены успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='discord')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.discord = SimpleNamespace(
                application_id=entry.get_custom_property('application_id'),
                public_key=entry.get_custom_property('public_key'),
                bot_token=entry.get_custom_property('bot_token'),
            )
            return True
        except Exception as e:
            logger.error(f'Ошибка при загрузке учетных данных Discord: {e}')
            return False

    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если учетные данные загружены успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='prestashop')[0]
            client_entry = group.find_groups(name='clients')[0].find_entries(title='entry')[0]

            self.credentials.presta = SimpleNamespace(
                client = SimpleNamespace(
                    api_key=client_entry.get_custom_property('api_key'),
                    api_domain=client_entry.get_custom_property('api_domain'),
                    db_server=client_entry.get_custom_property('db_server'),
                    db_user=client_entry.get_custom_property('db_user'),
                    db_password=client_entry.get_custom_property('db_password'),
                    ),
                )
            return True
        except Exception as e:
            logger.error(f'Ошибка при загрузке учетных данных PrestaShop: {e}')
            return False


    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
         """
         Загружает учетные данные PrestaShop Translations из KeePass.
         
         :param kp: Объект PyKeePass.
         :type kp: PyKeePass
         :return: True, если учетные данные загружены успешно, иначе False.
         :rtype: bool
         """
         try:
             group = kp.find_groups(name='prestashop')[0]
             translation_entry = group.find_groups(name='translation')[0].find_entries(title='entry')[0]
             self.credentials.presta.translations = SimpleNamespace(
                 server=translation_entry.get_custom_property('server'),
                 port=translation_entry.get_custom_property('port'),
                 database=translation_entry.get_custom_property('database'),
                 user=translation_entry.get_custom_property('user'),
                 password=translation_entry.get_custom_property('password'),
             )
             return True
         except Exception as e:
             logger.error(f'Ошибка при загрузке учетных данных PrestaShop Translations: {e}')
             return False

    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
         """
         Загружает учетные данные SMTP из KeePass.
         
         :param kp: Объект PyKeePass.
         :type kp: PyKeePass
         :return: True, если учетные данные загружены успешно, иначе False.
         :rtype: bool
         """
         try:
             group = kp.find_groups(name='smtp')[0]
             entry = group.find_entries(title='entry')[0]
             self.credentials.smtp = SimpleNamespace(
                 server=entry.get_custom_property('server'),
                 port=entry.get_custom_property('port'),
                 user=entry.get_custom_property('user'),
                 password=entry.get_custom_property('password'),
             )
             return True
         except Exception as e:
             logger.error(f'Ошибка при загрузке учетных данных SMTP: {e}')
             return False

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Facebook из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если учетные данные загружены успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='facebook')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.facebook = SimpleNamespace(
                app_id=entry.get_custom_property('app_id'),
                app_secret=entry.get_custom_property('app_secret'),
                access_token=entry.get_custom_property('access_token'),
            )
            return True
        except Exception as e:
            logger.error(f'Ошибка при загрузке учетных данных Facebook: {e}')
            return False

    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Google API из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если учетные данные загружены успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='google')[0]
            gapi_group = group.find_groups(name='gapi')[0]
            entry = gapi_group.find_entries(title='entry')[0]
            self.credentials.gapi = SimpleNamespace(
                api_key=entry.get_custom_property('api_key'),
            )
            return True
        except Exception as e:
            logger.error(f'Ошибка при загрузке учетных данных Google API: {e}')
            return False


    def now(self) -> str:
         """
         Возвращает текущую метку времени в формате, указанном в файле `config.json`.

         :return: Текущая метка времени в виде строки.
         :rtype: str
         """
         from datetime import datetime
         return datetime.now().strftime(self.config.time_format)

# Global instance of ProgramSettings
gs: ProgramSettings = ProgramSettings()
```