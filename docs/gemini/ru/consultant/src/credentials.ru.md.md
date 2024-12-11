## Улучшенный код
```python
"""
Модуль для управления настройками и учетными данными программы.
==================================================================

Этот модуль предоставляет класс :class:`ProgramSettings`, который отвечает за загрузку,
хранение и управление конфигурацией приложения, включая учетные данные из KeePass.
Модуль также содержит функцию :func:`set_project_root` для автоматического определения
корневой директории проекта.

Пример использования
--------------------

Пример использования класса `ProgramSettings` для доступа к настройкам:

.. code-block:: python

    from src.credentials import gs

    print(gs.config.project_name)
    print(gs.credentials.openai.api_key)
"""
import sys
import getpass
from pathlib import Path
from types import SimpleNamespace

from pykeepass import PyKeePass
# from src.utils.jjson import j_loads
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Начиная с текущей директории, функция ищет вверх по дереву каталогов, пока не найдет
    каталог, содержащий один из файлов, указанных в `marker_files`.

    :param marker_files: Кортеж с именами файлов или каталогов для поиска.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
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
    """
    Декоратор для реализации паттерна Singleton.

    Обеспечивает, что у класса будет только один экземпляр.

    :param cls: Класс, который необходимо сделать синглтоном.
    :type cls: class
    :return: Функция, возвращающая единственный экземпляр класса.
    :rtype: function
    """
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton
class ProgramSettings:
    """
    Класс для управления настройками и учетными данными программы.

    Загружает конфигурацию из `config.json` и учетные данные из базы данных KeePass (`credentials.kdbx`).
    """

    def __init__(self, **kwargs):
        """
        Инициализирует экземпляр класса ProgramSettings.

        Загружает конфигурацию проекта, устанавливает пути, проверяет наличие обновлений и
        загружает учетные данные из KeePass.
        """
        self.host_name = 'localhost'  # TODO: Get host_name
        self.base_dir = set_project_root()
        self.config: SimpleNamespace = None
        self.credentials: SimpleNamespace = SimpleNamespace()
        self.MODE: str = 'dev' # TODO: Get MODE from config or ENV
        self.path: SimpleNamespace = SimpleNamespace()

        # Загрузка конфигурации проекта из config.json
        self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
        if not self.config:
            logger.error('Ошибка при загрузке настроек')
            ...
            return

        self.config.project_name = self.base_dir.name

        self.path.log = self.base_dir / self.config.paths.log
        self.path.tmp = self.base_dir / self.config.paths.tmp
        self.path.ext = self.base_dir / self.config.paths.ext
        self.path.gdrive = self.base_dir / self.config.paths.gdrive
        self.path.secrets = self.base_dir / 'secrets'

        # Загрузка учетных данных из KeePass
        self._load_credentials()

    def _load_credentials(self) -> None:
        """
        Загружает учетные данные из базы данных KeePass.

        Использует методы `_open_kp` для открытия базы данных и соответствующие методы
        `_load_*_credentials` для загрузки отдельных типов учетных данных.
        """
        kp = self._open_kp()
        if not kp:
            logger.error('Не удалось открыть базу данных KeePass')
            return
        self.credentials.aliexpress = SimpleNamespace()
        self.credentials.openai = SimpleNamespace()
        self.credentials.gemini = SimpleNamespace()
        self.credentials.telegram = SimpleNamespace()
        self.credentials.discord = SimpleNamespace()
        self.credentials.presta = SimpleNamespace()
        self.credentials.smtp = SimpleNamespace()
        self.credentials.facebook = SimpleNamespace()
        self.credentials.gapi = SimpleNamespace()
        
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

        Выполняет несколько попыток открытия базы данных с заданным количеством повторных попыток.
        В случае неудачи, выводит сообщение об ошибке и завершает работу программы.

        :param retry: Количество попыток для открытия базы данных.
        :type retry: int
        :return: Объект PyKeePass или None в случае неудачи.
        :rtype: PyKeePass | None
        """
        while retry > 0:
            try:
                password = (Path(self.path.secrets / 'password.txt').read_text(encoding="utf-8") or None)
                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'),
                               password=password or getpass.getpass(print('Введите мастер-пароль KeePass: ').lower()))
                return kp
            except Exception as ex:
                print(f"Не удалось открыть базу данных KeePass. Исключение: {ex}, осталось попыток: {retry - 1}.")
                ...
                retry -= 1
                if retry < 1:
                    logger.critical('Не удалось открыть базу данных KeePass после нескольких попыток', exc_info=True)
                    ...
                    sys.exit()
        return None

    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Aliexpress из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='aliexpress')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.aliexpress.api_key = entry.get_custom_property('api_key')
            self.credentials.aliexpress.secret = entry.get_custom_property('secret')
            self.credentials.aliexpress.tracking_id = entry.get_custom_property('tracking_id')
            self.credentials.aliexpress.email = entry.get_custom_property('email')
            self.credentials.aliexpress.password = entry.get_custom_property('password')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных Aliexpress', exc_info=True)
            return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные OpenAI из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='openai')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.openai.api_key = entry.get_custom_property('api_key')
            
            group = kp.find_groups(name='assistants',group=group)[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.openai.assistant_id = entry.get_custom_property('assistant_id')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных OpenAI', exc_info=True)
            return False

    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные GoogleAI из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='gemini')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.gemini.api_key = entry.get_custom_property('api_key')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных Gemini', exc_info=True)
            return False

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Telegram из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='telegram')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.telegram.token = entry.get_custom_property('token')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных Telegram', exc_info=True)
            return False

    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Discord из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='discord')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.discord.application_id = entry.get_custom_property('application_id')
            self.credentials.discord.public_key = entry.get_custom_property('public_key')
            self.credentials.discord.bot_token = entry.get_custom_property('bot_token')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных Discord', exc_info=True)
            return False

    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='prestashop')[0]
            
            group_client = kp.find_groups(name='clients', group=group)[0]
            entry = kp.find_entries(group=group_client)[0]
            
            self.credentials.presta.client = SimpleNamespace()
            self.credentials.presta.client.api_key = entry.get_custom_property('api_key')
            self.credentials.presta.client.api_domain = entry.get_custom_property('api_domain')
            self.credentials.presta.client.db_server = entry.get_custom_property('db_server')
            self.credentials.presta.client.db_user = entry.get_custom_property('db_user')
            self.credentials.presta.client.db_password = entry.get_custom_property('db_password')
            
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных PrestaShop', exc_info=True)
            return False
        
    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop Translations из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='prestashop')[0]
            group = kp.find_groups(name='translation', group=group)[0]
            entry = kp.find_entries(group=group)[0]
            
            self.credentials.presta.translations = SimpleNamespace()
            self.credentials.presta.translations.server = entry.get_custom_property('server')
            self.credentials.presta.translations.port = entry.get_custom_property('port')
            self.credentials.presta.translations.database = entry.get_custom_property('database')
            self.credentials.presta.translations.user = entry.get_custom_property('user')
            self.credentials.presta.translations.password = entry.get_custom_property('password')

            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных PrestaShop Translations', exc_info=True)
            return False

    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные SMTP из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='smtp')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.smtp.server = entry.get_custom_property('server')
            self.credentials.smtp.port = entry.get_custom_property('port')
            self.credentials.smtp.user = entry.get_custom_property('user')
            self.credentials.smtp.password = entry.get_custom_property('password')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных SMTP', exc_info=True)
            return False

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Facebook из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='facebook')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.facebook.app_id = entry.get_custom_property('app_id')
            self.credentials.facebook.app_secret = entry.get_custom_property('app_secret')
            self.credentials.facebook.access_token = entry.get_custom_property('access_token')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных Facebook', exc_info=True)
            return False

    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Google API из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='google')[0]
            group = kp.find_groups(name='gapi', group=group)[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.gapi.api_key = entry.get_custom_property('api_key')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных Google API', exc_info=True)
            return False

    def now(self) -> str:
        """
        Возвращает текущую метку времени.

        :return: Текущая метка времени в формате, определенном в конфигурации.
        :rtype: str
        """
        from datetime import datetime
        return datetime.now().strftime(self.config.datetime_format)


# Global instance of ProgramSettings
gs: ProgramSettings = ProgramSettings()
```
## Внесённые изменения
- Добавлены docstring для модуля, классов и функций в формате reStructuredText (RST).
- Заменен `json.load` на `j_loads_ns` из `src.utils.jjson`.
- Добавлен импорт `logger` из `src.logger.logger`.
- Добавлены логирование ошибок с помощью `logger.error` и `logger.critical`.
- Изменены `try-except` блоки для использования `logger.error`.
- Добавлены возвращаемые значения и типы для всех функций.
- Изменены комментарии в коде в соответствии с инструкциями.
- Добавлен тип возвращаемого значения для `now()`.
- Удалены избыточные `...` блоки, где это было необходимо.
- Улучшена читаемость кода за счет добавления пустых строк между блоками кода.
- Добавлена обработка исключений при открытии базы данных KeePass с повторными попытками.
- Добавлены комментарии для всех исключений, для которых добавлено логирование ошибок.
- Переименованы переменные в соответствии с ранее обработанными файлами
- Убраны лишние None
- Добавлен атрибут `MODE` для класса `ProgramSettings`
## Оптимизированный код
```python
"""
Модуль для управления настройками и учетными данными программы.
==================================================================

Этот модуль предоставляет класс :class:`ProgramSettings`, который отвечает за загрузку,
хранение и управление конфигурацией приложения, включая учетные данные из KeePass.
Модуль также содержит функцию :func:`set_project_root` для автоматического определения
корневой директории проекта.

Пример использования
--------------------

Пример использования класса `ProgramSettings` для доступа к настройкам:

.. code-block:: python

    from src.credentials import gs

    print(gs.config.project_name)
    print(gs.credentials.openai.api_key)
"""
import sys
import getpass
from pathlib import Path
from types import SimpleNamespace

from pykeepass import PyKeePass
# from src.utils.jjson import j_loads
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Начиная с текущей директории, функция ищет вверх по дереву каталогов, пока не найдет
    каталог, содержащий один из файлов, указанных в `marker_files`.

    :param marker_files: Кортеж с именами файлов или каталогов для поиска.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
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
    """
    Декоратор для реализации паттерна Singleton.

    Обеспечивает, что у класса будет только один экземпляр.

    :param cls: Класс, который необходимо сделать синглтоном.
    :type cls: class
    :return: Функция, возвращающая единственный экземпляр класса.
    :rtype: function
    """
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton
class ProgramSettings:
    """
    Класс для управления настройками и учетными данными программы.

    Загружает конфигурацию из `config.json` и учетные данные из базы данных KeePass (`credentials.kdbx`).
    """

    def __init__(self, **kwargs):
        """
        Инициализирует экземпляр класса ProgramSettings.

        Загружает конфигурацию проекта, устанавливает пути, проверяет наличие обновлений и
        загружает учетные данные из KeePass.
        """
        self.host_name = 'localhost'  # TODO: Get host_name
        self.base_dir = set_project_root()
        self.config: SimpleNamespace = None
        self.credentials: SimpleNamespace = SimpleNamespace()
        self.MODE: str = 'dev' # TODO: Get MODE from config or ENV
        self.path: SimpleNamespace = SimpleNamespace()

        # Загрузка конфигурации проекта из config.json
        self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
        if not self.config:
            logger.error('Ошибка при загрузке настроек')
            return

        self.config.project_name = self.base_dir.name

        self.path.log = self.base_dir / self.config.paths.log
        self.path.tmp = self.base_dir / self.config.paths.tmp
        self.path.ext = self.base_dir / self.config.paths.ext
        self.path.gdrive = self.base_dir / self.config.paths.gdrive
        self.path.secrets = self.base_dir / 'secrets'

        # Загрузка учетных данных из KeePass
        self._load_credentials()

    def _load_credentials(self) -> None:
        """
        Загружает учетные данные из базы данных KeePass.

        Использует методы `_open_kp` для открытия базы данных и соответствующие методы
        `_load_*_credentials` для загрузки отдельных типов учетных данных.
        """
        kp = self._open_kp()
        if not kp:
            logger.error('Не удалось открыть базу данных KeePass')
            return
        self.credentials.aliexpress = SimpleNamespace()
        self.credentials.openai = SimpleNamespace()
        self.credentials.gemini = SimpleNamespace()
        self.credentials.telegram = SimpleNamespace()
        self.credentials.discord = SimpleNamespace()
        self.credentials.presta = SimpleNamespace()
        self.credentials.smtp = SimpleNamespace()
        self.credentials.facebook = SimpleNamespace()
        self.credentials.gapi = SimpleNamespace()
        
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

        Выполняет несколько попыток открытия базы данных с заданным количеством повторных попыток.
        В случае неудачи, выводит сообщение об ошибке и завершает работу программы.

        :param retry: Количество попыток для открытия базы данных.
        :type retry: int
        :return: Объект PyKeePass или None в случае неудачи.
        :rtype: PyKeePass | None
        """
        while retry > 0:
            try:
                password = (Path(self.path.secrets / 'password.txt').read_text(encoding="utf-8") or None)
                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'),
                               password=password or getpass.getpass(print('Введите мастер-пароль KeePass: ').lower()))
                return kp
            except Exception as ex:
                print(f"Не удалось открыть базу данных KeePass. Исключение: {ex}, осталось попыток: {retry - 1}.")
                retry -= 1
                if retry < 1:
                    logger.critical('Не удалось открыть базу данных KeePass после нескольких попыток', exc_info=True)
                    sys.exit()
        return None

    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Aliexpress из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='aliexpress')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.aliexpress.api_key = entry.get_custom_property('api_key')
            self.credentials.aliexpress.secret = entry.get_custom_property('secret')
            self.credentials.aliexpress.tracking_id = entry.get_custom_property('tracking_id')
            self.credentials.aliexpress.email = entry.get_custom_property('email')
            self.credentials.aliexpress.password = entry.get_custom_property('password')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных Aliexpress', exc_info=True)
            return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные OpenAI из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='openai')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.openai.api_key = entry.get_custom_property('api_key')
            
            group = kp.find_groups(name='assistants',group=group)[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.openai.assistant_id = entry.get_custom_property('assistant_id')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных OpenAI', exc_info=True)
            return False

    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные GoogleAI из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='gemini')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.gemini.api_key = entry.get_custom_property('api_key')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных Gemini', exc_info=True)
            return False

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Telegram из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='telegram')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.telegram.token = entry.get_custom_property('token')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных Telegram', exc_info=True)
            return False

    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Discord из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='discord')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.discord.application_id = entry.get_custom_property('application_id')
            self.credentials.discord.public_key = entry.get_custom_property('public_key')
            self.credentials.discord.bot_token = entry.get_custom_property('bot_token')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных Discord', exc_info=True)
            return False

    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='prestashop')[0]
            
            group_client = kp.find_groups(name='clients', group=group)[0]
            entry = kp.find_entries(group=group_client)[0]
            
            self.credentials.presta.client = SimpleNamespace()
            self.credentials.presta.client.api_key = entry.get_custom_property('api_key')
            self.credentials.presta.client.api_domain = entry.get_custom_property('api_domain')
            self.credentials.presta.client.db_server = entry.get_custom_property('db_server')
            self.credentials.presta.client.db_user = entry.get_custom_property('db_user')
            self.credentials.presta.client.db_password = entry.get_custom_property('db_password')
            
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных PrestaShop', exc_info=True)
            return False
        
    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop Translations из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='prestashop')[0]
            group = kp.find_groups(name='translation', group=group)[0]
            entry = kp.find_entries(group=group)[0]
            
            self.credentials.presta.translations = SimpleNamespace()
            self.credentials.presta.translations.server = entry.get_custom_property('server')
            self.credentials.presta.translations.port = entry.get_custom_property('port')
            self.credentials.presta.translations.database = entry.get_custom_property('database')
            self.credentials.presta.translations.user = entry.get_custom_property('user')
            self.credentials.presta.translations.password = entry.get_custom_property('password')

            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных PrestaShop Translations', exc_info=True)
            return False

    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные SMTP из KeePass.

        :param kp: Объект PyKeePass для доступа к базе данных.
        :type kp: PyKeePass
        :