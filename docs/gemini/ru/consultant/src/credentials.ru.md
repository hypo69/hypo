# Анализ кода модуля `credentials`

## Качество кода:

- **Соответствие стандартам**: 6/10
- **Плюсы**:
    - Подробное описание структуры и назначения модуля.
    - Наличие комментариев и разделение на функции и классы.
    - Использование KeePass для хранения учетных данных.
    - Описание процесса инициализации и настройки проекта.
    - Использование глобального экземпляра `ProgramSettings`.
- **Минусы**:
    -  Использование двойных кавычек для строк.
    -  Отсутствие обработки ошибок через `logger.error`.
    -  Не полное соответствие стандартам PEP8.
    -  Пароль от KeePass в `password.txt`  в режиме разработки - потенциальная уязвимость.
    -  Отсутствие документации RST у функций и классов.
    -  Много `...` в коде.
    -  Использование `print` для сообщений об ошибках (должно быть через `logger`).
    -  Импорт `logger` не из `src.logger`.
    -  Использование `j_loads_ns` без импорта.
    -  Отсутствие импорта `sys`.

## Рекомендации по улучшению:

1.  **Использование одинарных кавычек**: Все строки в коде, кроме тех, что выводятся на экран или передаются в logger, должны быть заключены в одинарные кавычки.
2.  **Логирование ошибок**: Замените `print` на `logger.error` или `logger.critical` для всех сообщений об ошибках. Импортируйте `logger` из `src.logger`.
3.  **Обработка исключений**: Используйте `logger.error` для записи ошибок вместо `try-except` с `print`.
4.  **Безопасное хранение паролей**: Разработать более безопасный механизм хранения паролей, особенно для режима разработки.
5.  **Документирование кода**: Добавьте docstrings в формате RST для всех функций, классов и методов.
6.  **Удалить маркеры**: Заменить все `...` на реальный код или удалить их.
7.  **Импорт `sys`**: Добавьте импорт `import sys` в начале файла.
8.  **Импорт `j_loads_ns`**: Добавьте импорт `from src.utils.jjson import j_loads_ns`
9.  **Удаление лишних коментариев**: Удалите `Args`, `Returns` и тд, все описание должно быть в RST.
10. **Форматирование**: Приведите код в соответствие со стандартами PEP8.

## Оптимизированный код:

```python
"""
Модуль для управления учетными данными и настройками программы.
==============================================================

Этот модуль предоставляет функциональность для загрузки и управления
учетными данными из базы данных KeePass, а также для установки
инициализационных настроек проекта.

Пример использования
----------------------
.. code-block:: python

    from src.credentials import gs

    # Доступ к настройкам
    print(gs.config.project_name)

    # Доступ к API ключу OpenAI
    print(gs.credentials.openai.api_key)
"""
import getpass
import sys
from pathlib import Path
from types import SimpleNamespace
from src.utils.jjson import j_loads_ns
from src.logger import logger  #  Импорт logger из src.logger
from pykeepass import PyKeePass


def singleton(cls):
    """
    Декоратор для создания класса-синглтона.

    :param cls: Класс, который нужно преобразовать в синглтон.
    :type cls: class
    :return: Функция, возвращающая экземпляр класса-синглтона.
    :rtype: function

    Пример:
        >>> @singleton
        >>> class MyClass:
        >>>     pass
        >>> instance1 = MyClass()
        >>> instance2 = MyClass()
        >>> assert instance1 is instance2

    """
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневую директорию проекта.

    Начиная с текущей директории файла, ищет вверх по дереву каталогов
    и останавливается на первой директории, содержащей любой из маркерных файлов.

    :param marker_files: Кортеж имен файлов или директорий для идентификации корневой директории проекта.
    :type marker_files: tuple, optional
    :return: Путь к корневой директории, если она найдена, иначе - директория, где находится скрипт.
    :rtype: Path

    Пример:
        >>> root = set_project_root()
        >>> print(root)
        <path_to_project>
    """
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

    Устанавливает основные параметры и настройки проекта.
    Загружает конфигурацию из `config.json` и данные учетных данных
    из файла `credentials.kdbx` в базе данных KeePass.

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

        - Загружает конфигурацию проекта из `config.json`.
        - Инициализирует атрибут `path` с путями к различным директориям проекта.
        - Вызывает `check_latest_release` для проверки на наличие новой версии проекта.
        - Загружает учетные данные из `credentials.kdbx`.
        """
        self.host_name: str = 'localhost'  #  хост
        self.base_dir: Path = set_project_root()  #  корневой каталог проекта
        self.config: SimpleNamespace = SimpleNamespace()  #  конфигурация проекта
        self.credentials: SimpleNamespace = SimpleNamespace()  #  учетные данные
        self.MODE: str = 'dev'  #  режим работы проекта

        self.path: SimpleNamespace = SimpleNamespace()  # пути
        self.path.src: Path = self.base_dir / 'src'  #  путь к исходному коду
        self.path.logs: Path = self.base_dir / 'logs'  #  путь к логам
        self.path.temp: Path = self.base_dir / 'temp'  #  путь к временным файлам
        self.path.external: Path = self.base_dir / 'external' #  путь к внешнему хранилищу
        self.path.google_drive: Path = self.base_dir / 'google_drive'  #  путь к google drive
        self.path.secrets: Path = self.base_dir / 'secrets'  #  путь к секретам

        self.config = j_loads_ns(self.base_dir / 'src' / 'config.json') #  загрузка конфигурации из config.json
        if not self.config:
            logger.error('Ошибка при загрузке настроек')  #  лог ошибки
            return

        self.config.project_name = self.base_dir.name #  имя проекта

        self._load_credentials() # загрузка учетных данных

    def _load_credentials(self) -> None:
        """
        Загружает учетные данные из KeePass.
        """
        kp = self._open_kp()
        if not kp:
            return
        self.credentials.aliexpress = SimpleNamespace()
        self._load_aliexpress_credentials(kp)
        self.credentials.openai = SimpleNamespace()
        self._load_openai_credentials(kp)
        self.credentials.gemini = SimpleNamespace()
        self._load_gemini_credentials(kp)
        self.credentials.telegram = SimpleNamespace()
        self._load_telegram_credentials(kp)
        self.credentials.discord = SimpleNamespace()
        self._load_discord_credentials(kp)
        self.credentials.presta = SimpleNamespace()
        self._load_PrestaShop_credentials(kp)
        self.credentials.presta.translations = SimpleNamespace()
        self._load_presta_translations_credentials(kp)
        self.credentials.smtp = SimpleNamespace()
        self._load_smtp_credentials(kp)
        self.credentials.facebook = SimpleNamespace()
        self._load_facebook_credentials(kp)
        self.credentials.gapi = SimpleNamespace()
        self._load_gapi_credentials(kp)

    def _open_kp(self, retry: int = 3) -> PyKeePass | None:
        """
        Открывает базу данных KeePass.

        :param retry: Количество попыток открытия базы данных.
        :type retry: int, optional
        :return: Объект PyKeePass или None, если не удалось открыть базу данных.
        :rtype: PyKeePass | None
        """
        while retry > 0:
            try:
                password: str | None = None
                password_file = self.path.secrets / 'password.txt'
                if password_file.exists():
                  password = password_file.read_text(encoding='utf-8')
                if password:
                  kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), password=password)
                else:
                   password=getpass.getpass(print('Введите мастер-пароль KeePass: ').lower())
                   kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), password=password)
                return kp
            except Exception as ex:
                logger.error(f'Не удалось открыть базу данных KeePass. Исключение: {ex}, осталось попыток: {retry-1}.')
                retry -= 1
                if retry < 1:
                   logger.critical('Не удалось открыть базу данных KeePass после нескольких попыток', exc_info=True)
                   sys.exit()
        return None


    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Aliexpress из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если учетные данные загружены, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='aliexpress')[0]
            entry = group.find_entries(title='api')[0]
            self.credentials.aliexpress.api_key = entry.get_custom_property('api_key')
            self.credentials.aliexpress.secret = entry.get_custom_property('secret')
            self.credentials.aliexpress.tracking_id = entry.get_custom_property('tracking_id')
            self.credentials.aliexpress.email = entry.get_custom_property('email')
            self.credentials.aliexpress.password = entry.get_custom_property('password')
            return True
        except Exception as ex:
            logger.error(f'Ошибка при загрузке учетных данных Aliexpress: {ex}')
            return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные OpenAI из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если учетные данные загружены, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='openai')[0]
            entry_api = group.find_entries(title='entry')[0]
            entry_assistant = group.find_groups(name='assistants')[0].find_entries(title='entry')[0]

            self.credentials.openai.api_key = entry_api.get_custom_property('api_key')
            self.credentials.openai.assistant_id = entry_assistant.get_custom_property('assistant_id')
            return True
        except Exception as ex:
            logger.error(f'Ошибка при загрузке учетных данных OpenAI: {ex}')
            return False

    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
         """
         Загружает учетные данные GoogleAI из KeePass.

         :param kp: Объект PyKeePass.
         :type kp: PyKeePass
         :return: True, если учетные данные загружены, иначе False.
         :rtype: bool
         """
         try:
             group = kp.find_groups(name='gemini')[0]
             entry = group.find_entries(title='entry')[0]
             self.credentials.gemini.api_key = entry.get_custom_property('api_key')
             return True
         except Exception as ex:
             logger.error(f'Ошибка при загрузке учетных данных Gemini: {ex}')
             return False

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Telegram из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если учетные данные загружены, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='telegram')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.telegram.token = entry.get_custom_property('token')
            return True
        except Exception as ex:
            logger.error(f'Ошибка при загрузке учетных данных Telegram: {ex}')
            return False

    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Discord из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если учетные данные загружены, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='discord')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.discord.application_id = entry.get_custom_property('application_id')
            self.credentials.discord.public_key = entry.get_custom_property('public_key')
            self.credentials.discord.bot_token = entry.get_custom_property('bot_token')
            return True
        except Exception as ex:
            logger.error(f'Ошибка при загрузке учетных данных Discord: {ex}')
            return False

    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если учетные данные загружены, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='prestashop')[0]
            client_group = group.find_groups(name='clients')[0]
            client_entry = client_group.find_entries(title='entry')[0]

            self.credentials.presta.client.api_key = client_entry.get_custom_property('api_key')
            self.credentials.presta.client.api_domain = client_entry.get_custom_property('api_domain')
            self.credentials.presta.client.db_server = client_entry.get_custom_property('db_server')
            self.credentials.presta.client.db_user = client_entry.get_custom_property('db_user')
            self.credentials.presta.client.db_password = client_entry.get_custom_property('db_password')
            return True
        except Exception as ex:
             logger.error(f'Ошибка при загрузке учетных данных PrestaShop: {ex}')
             return False

    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop Translations из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если учетные данные загружены, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='prestashop')[0]
            translation_group = group.find_groups(name='translation')[0]
            translation_entry = translation_group.find_entries(title='entry')[0]

            self.credentials.presta.translations.server = translation_entry.get_custom_property('server')
            self.credentials.presta.translations.port = translation_entry.get_custom_property('port')
            self.credentials.presta.translations.database = translation_entry.get_custom_property('database')
            self.credentials.presta.translations.user = translation_entry.get_custom_property('user')
            self.credentials.presta.translations.password = translation_entry.get_custom_property('password')
            return True
        except Exception as ex:
            logger.error(f'Ошибка при загрузке учетных данных PrestaShop translations: {ex}')
            return False

    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные SMTP из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если учетные данные загружены, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='smtp')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.smtp.server = entry.get_custom_property('server')
            self.credentials.smtp.port = entry.get_custom_property('port')
            self.credentials.smtp.user = entry.get_custom_property('user')
            self.credentials.smtp.password = entry.get_custom_property('password')
            return True
        except Exception as ex:
            logger.error(f'Ошибка при загрузке учетных данных SMTP: {ex}')
            return False

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Facebook из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если учетные данные загружены, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='facebook')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.facebook.app_id = entry.get_custom_property('app_id')
            self.credentials.facebook.app_secret = entry.get_custom_property('app_secret')
            self.credentials.facebook.access_token = entry.get_custom_property('access_token')
            return True
        except Exception as ex:
             logger.error(f'Ошибка при загрузке учетных данных Facebook: {ex}')
             return False


    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
         """
         Загружает учетные данные Google API из KeePass.

         :param kp: Объект PyKeePass.
         :type kp: PyKeePass
         :return: True, если учетные данные загружены, иначе False.
         :rtype: bool
         """
         try:
             group = kp.find_groups(name='google')[0]
             gapi_group = group.find_groups(name='gapi')[0]
             entry = gapi_group.find_entries(title='entry')[0]
             self.credentials.gapi.api_key = entry.get_custom_property('api_key')
             return True
         except Exception as ex:
            logger.error(f'Ошибка при загрузке учетных данных Google API: {ex}')
            return False

    def now(self) -> str:
        """
        Возвращает текущую метку времени в формате, указанном в файле `config.json`.

        :return: Текущая метка времени в формате из конфига
        :rtype: str
        """
        from datetime import datetime
        return datetime.now().strftime(self.config.date_format)

# Global instance of ProgramSettings
gs: ProgramSettings = ProgramSettings()
```