# Анализ кода модуля src.credentials

**Качество кода**
7
-  Плюсы
    - Код хорошо структурирован и документирован в формате reStructuredText, что облегчает понимание его функциональности.
    - Используется декоратор `@singleton` для создания класса-синглтона.
    - Код обрабатывает исключения при открытии базы данных KeePass.
    - Использование `j_loads_ns` для загрузки JSON-конфигурации.
    - Подробное описание структуры базы данных `credentials.kdbx`
-  Минусы
    -  Используется `sys.exit()` для завершения программы в случае ошибки открытия KeePass, что может быть нежелательно в некоторых сценариях.
    -  Не все функции и методы имеют docstring в формате reStructuredText
    -  Использование `print` для вывода ошибок. Лучше использовать `logger`
    -  В коде есть много `...` как точки останова
    -  Хранение пароля в файле `password.txt` является небезопасным.
    -  Необходимо добавить логирование ошибок с помощью `logger.error`.
    -  Не все исключения обрабатываются с помощью `logger.error`.

**Рекомендации по улучшению**
- Добавить docstring в формате reStructuredText для всех функций и методов.
- Заменить `print` на `logger.error` для вывода ошибок.
- Обработать все возможные исключения с помощью `logger.error`.
- Убрать `sys.exit()` и `...`  из кода.
- Разработать более безопасный механизм хранения пароля.
- Добавить импорты `os`, `sys`, `getpass`, `time`, `SimpleNamespace`.
- Привести в соответствие имена переменных, функций и импортов с ранее обработанными файлами.
- Добавить проверку существования файла перед чтением пароля.

**Оптимизированный код**

```python
"""
Модуль для работы с настройками и учетными данными приложения.
================================================================

Этот модуль содержит класс :class:`ProgramSettings`, который загружает и
сохраняет информацию об учетных данных (ключи API, пароли и т.д.)
из файла базы данных KeePass `credentials.kdbx`. Также он включает
функцию `set_project_root` для определения корневого каталога проекта.

Пример использования
--------------------

Пример использования класса `ProgramSettings`:

.. code-block:: python

   from src.credentials import gs

   print(gs.config.project_name)
   print(gs.credentials.openai.api_key)
"""
import os
import sys
import getpass
import time
from pathlib import Path
from types import SimpleNamespace

from pykeepass import PyKeePass
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Находит корневую директорию проекта, начиная с текущей директории файла,
    ища вверх и останавливаясь на первой директории, содержащей любой из
    маркерных файлов.

    :param marker_files: Имена файлов или директорий для идентификации
                         корневой директории проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если найдена, иначе директория,
             где находится скрипт.
    :rtype: Path
    """
    root_path: Path
    current_path: Path = Path(__file__).resolve().parent
    root_path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root_path = parent
            break
    if root_path not in sys.path:
        sys.path.insert(0, str(root_path))
    return root_path


def singleton(cls):
    """
    Декоратор для создания класса-синглтона.

    :param cls: Класс, который должен быть преобразован в синглтон.
    :type cls: class
    :return: Функция, возвращающая экземпляр класса-синглтона.
    :rtype: function
    """
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance

    return wrapper

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
        Инициализирует экземпляр класса.

        Загружает конфигурацию проекта из `config.json`.
        Инициализирует атрибут `path` с путями к различным директориям проекта.
        Вызывает `check_latest_release` для проверки на наличие новой версии проекта.
        Загружает учетные данные из `credentials.kdbx`.

        :param kwargs: Произвольные ключевые аргументы.
        :type kwargs: dict
        """
        self.host_name: str = os.uname().nodename if hasattr(os, 'uname') else 'unknown'
        self.base_dir: Path = set_project_root()
        self.config: SimpleNamespace = j_loads_ns(self.base_dir / 'src' / 'config.json')
        if not self.config:
            logger.error('Ошибка при загрузке настроек')
            return
        self.config.project_name = self.base_dir.name

        self.MODE: str = self.config.MODE
        self.path: SimpleNamespace = SimpleNamespace(
            logs=self.base_dir / 'logs',
            tmp=self.base_dir / 'tmp',
            secrets=self.base_dir / 'secrets',
            external_storage=self.base_dir / 'external_storage',
            gdrive=self.base_dir / 'gdrive',
            )
        self.credentials: SimpleNamespace = SimpleNamespace()
        self._load_credentials()

    def _load_credentials(self) -> None:
        """
        Загружает учетные данные из KeePass.
        """
        kp = self._open_kp()
        if not kp:
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

        :param retry: Количество попыток.
        :type retry: int
        :return: Объект PyKeePass или None в случае неудачи.
        :rtype: PyKeePass | None
        """
        while retry > 0:
            try:
                password: str = None
                password_file = Path(self.path.secrets / 'password.txt')
                if password_file.exists():
                    password = password_file.read_text(encoding="utf-8").strip()
                if not password:
                    password = getpass.getpass(prompt='Введите мастер-пароль KeePass: ').lower()
                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), password=password)
                return kp
            except Exception as ex:
                logger.error(f'Не удалось открыть базу данных KeePass. Исключение: {ex}, осталось попыток: {retry-1}.', exc_info=True)
                retry -= 1
        logger.critical('Не удалось открыть базу данных KeePass после нескольких попыток', exc_info=True)
        return None


    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Aliexpress из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если загрузка прошла успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='aliexpress', first=True)
            if not group:
                logger.error('Группа "aliexpress" не найдена в KeePass')
                return False
            entry = kp.find_entries(group=group, first=True)
            if not entry:
                logger.error('Запись в группе "aliexpress" не найдена в KeePass')
                return False
            self.credentials.aliexpress = SimpleNamespace(
                api_key=entry.get_custom_property('api_key'),
                secret=entry.get_custom_property('secret'),
                tracking_id=entry.get_custom_property('tracking_id'),
                email=entry.username,
                password=entry.password,
            )
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных Aliexpress', exc_info=True)
            return False


    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные OpenAI из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если загрузка прошла успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='openai', first=True)
            if not group:
                logger.error('Группа "openai" не найдена в KeePass')
                return False
            entry = kp.find_entries(group=group, first=True)
            if not entry:
                logger.error('Запись в группе "openai" не найдена в KeePass')
                return False
            self.credentials.openai = SimpleNamespace(
                api_key=entry.password,
                )
            group_assistants = kp.find_groups(name='assistants', parent=group, first = True)
            if not group_assistants:
                logger.error('Группа "assistants" в "openai" не найдена в KeePass')
                return False
            entry_assistants = kp.find_entries(group=group_assistants, first=True)
            if not entry_assistants:
               logger.error('Запись в группе "assistants" в "openai" не найдена в KeePass')
               return False
            self.credentials.openai.assistant_id=entry_assistants.password
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных OpenAI', exc_info=True)
            return False


    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные GoogleAI из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если загрузка прошла успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='gemini', first=True)
            if not group:
                logger.error('Группа "gemini" не найдена в KeePass')
                return False
            entry = kp.find_entries(group=group, first=True)
            if not entry:
                logger.error('Запись в группе "gemini" не найдена в KeePass')
                return False
            self.credentials.gemini = SimpleNamespace(
                api_key=entry.password,
            )
            return True
        except Exception as ex:
             logger.error('Ошибка при загрузке учетных данных GoogleAI', exc_info=True)
             return False


    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Telegram из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если загрузка прошла успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='telegram', first=True)
            if not group:
                logger.error('Группа "telegram" не найдена в KeePass')
                return False
            entry = kp.find_entries(group=group, first=True)
            if not entry:
                logger.error('Запись в группе "telegram" не найдена в KeePass')
                return False
            self.credentials.telegram = SimpleNamespace(
                token=entry.password,
            )
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных Telegram', exc_info=True)
            return False


    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Discord из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если загрузка прошла успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='discord', first=True)
            if not group:
                logger.error('Группа "discord" не найдена в KeePass')
                return False
            entry = kp.find_entries(group=group, first=True)
            if not entry:
                logger.error('Запись в группе "discord" не найдена в KeePass')
                return False
            self.credentials.discord = SimpleNamespace(
                application_id=entry.get_custom_property('application_id'),
                public_key=entry.get_custom_property('public_key'),
                bot_token=entry.password,
            )
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных Discord', exc_info=True)
            return False


    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если загрузка прошла успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='prestashop', first=True)
            if not group:
                logger.error('Группа "prestashop" не найдена в KeePass')
                return False
            group_client = kp.find_groups(name='clients', parent=group, first = True)
            if not group_client:
                logger.error('Группа "clients" в "prestashop" не найдена в KeePass')
                return False
            entry_client = kp.find_entries(group=group_client, first=True)
            if not entry_client:
                logger.error('Запись в группе "clients" в "prestashop" не найдена в KeePass')
                return False
            self.credentials.presta = SimpleNamespace(
                client = SimpleNamespace(
                api_key=entry_client.get_custom_property('api_key'),
                api_domain=entry_client.get_custom_property('api_domain'),
                db_server=entry_client.get_custom_property('db_server'),
                db_user=entry_client.get_custom_property('db_user'),
                db_password=entry_client.get_custom_property('db_password'),
                )
            )
            return True
        except Exception as ex:
             logger.error('Ошибка при загрузке учетных данных PrestaShop', exc_info=True)
             return False


    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop Translations из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если загрузка прошла успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='translation', first=True, parent = kp.find_groups(name='prestashop', first=True))
            if not group:
                logger.error('Группа "translation" не найдена в KeePass')
                return False
            entry = kp.find_entries(group=group, first=True)
            if not entry:
                logger.error('Запись в группе "translation" не найдена в KeePass')
                return False
            self.credentials.presta.translations = SimpleNamespace(
                server=entry.get_custom_property('server'),
                port=entry.get_custom_property('port'),
                database=entry.get_custom_property('database'),
                user=entry.get_custom_property('user'),
                password=entry.get_custom_property('password'),
                )
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных PrestaShop Translations', exc_info=True)
            return False


    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные SMTP из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если загрузка прошла успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='smtp', first=True)
            if not group:
                logger.error('Группа "smtp" не найдена в KeePass')
                return False
            entry = kp.find_entries(group=group, first=True)
            if not entry:
                logger.error('Запись в группе "smtp" не найдена в KeePass')
                return False
            self.credentials.smtp = SimpleNamespace(
                server=entry.get_custom_property('server'),
                port=entry.get_custom_property('port'),
                user=entry.username,
                password=entry.password,
            )
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных SMTP', exc_info=True)
            return False


    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Facebook из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если загрузка прошла успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='facebook', first=True)
            if not group:
                logger.error('Группа "facebook" не найдена в KeePass')
                return False
            entry = kp.find_entries(group=group, first=True)
            if not entry:
                logger.error('Запись в группе "facebook" не найдена в KeePass')
                return False
            self.credentials.facebook = SimpleNamespace(
                app_id=entry.get_custom_property('app_id'),
                app_secret=entry.get_custom_property('app_secret'),
                access_token=entry.password,
            )
            return True
        except Exception as ex:
           logger.error('Ошибка при загрузке учетных данных Facebook', exc_info=True)
           return False

    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Google API из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если загрузка прошла успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='gapi', first=True, parent = kp.find_groups(name='google', first=True))
            if not group:
                logger.error('Группа "gapi" не найдена в KeePass')
                return False
            entry = kp.find_entries(group=group, first=True)
            if not entry:
                logger.error('Запись в группе "gapi" не найдена в KeePass')
                return False
            self.credentials.gapi = SimpleNamespace(
                api_key=entry.password,
            )
            return True
        except Exception as ex:
           logger.error('Ошибка при загрузке учетных данных Google API', exc_info=True)
           return False

    def now(self) -> str:
        """
        Возвращает текущую метку времени в формате, указанном в файле `config.json`.

        :return: Текущая метка времени.
        :rtype: str
        """
        return time.strftime(self.config.time_format)


# Global instance of ProgramSettings
gs: ProgramSettings = ProgramSettings()
```