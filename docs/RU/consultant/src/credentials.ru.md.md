# Анализ кода модуля `src.credentials`

**Качество кода**
7/10
- Плюсы
    - Код хорошо структурирован и документирован, с четким описанием функциональности каждого класса и метода.
    - Используется декоратор `@singleton` для создания единственного экземпляра класса `ProgramSettings`.
    - Присутствует логика определения корневой директории проекта.
    - Загрузка настроек из `config.json` и учетных данных из `credentials.kdbx` реализована корректно.
    - Обработка исключений в методе `_open_kp` присутствует.
    - Использование `j_loads_ns` для загрузки конфигурации.
    - Удобное использование `SimpleNamespace` для хранения настроек и учетных данных.
- Минусы
    - Использование `print` для вывода сообщений об ошибках, лучше использовать `logger.error` для логирования.
    - Чтение пароля из файла `password.txt` в открытом виде является уязвимостью.
    - Обработка ошибок `try-except` местами избыточна.
    - Отсутствие docstring для некоторых методов и атрибутов.
    - Не все импорты указаны в начале файла.

**Рекомендации по улучшению**
1.  Заменить использование `print` на `logger.error` для вывода сообщений об ошибках.
2.  Рассмотреть безопасный способ хранения паролей вместо файла `password.txt`.
3.  Упростить блоки `try-except`, используя `logger.error` для логирования ошибок.
4.  Добавить docstring для всех функций, методов и атрибутов.
5.  Добавить отсутствующие импорты в начало файла.
6.  Привести имена переменных и функций в соответствие с ранее обработанными файлами.
7.  Использовать константы для путей к файлам.
8.  Переработать процесс открытия KeePass, что бы не делать несколько попыток при неверном пароле

**Оптимизированный код**

```python
"""
Модуль для управления настройками и учетными данными программы.
=================================================================

Этот модуль предоставляет класс :class:`ProgramSettings`, который загружает и управляет настройками
и учетными данными, необходимыми для работы программы. Он включает в себя механизм для определения
корневой директории проекта, загрузки конфигурационных файлов и обработки учетных данных из базы
данных KeePass.

Пример использования
--------------------

Пример создания и использования экземпляра класса `ProgramSettings`:

.. code-block:: python

    from src.credentials import gs

    # Доступ к настройкам
    project_name = gs.config.project_name
    api_key = gs.credentials.openai.api_key
"""
import sys
import getpass
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Tuple
from src.utils.jjson import j_loads_ns
from pykeepass import PyKeePass
from src.logger.logger import logger


def singleton(cls):
    """
    Декоратор для создания класса-синглтона.

    :param cls: Класс, который должен быть преобразован в синглтон.
    :return: Функция, возвращающая экземпляр класса-синглтона.
    """
    instances = {}

    def getinstance(**kwargs):
        if cls not in instances:
            instances[cls] = cls(**kwargs)
        return instances[cls]
    return getinstance

def set_project_root(marker_files: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определение корневой директории проекта.

    Поиск ведётся вверх по директориям, пока не будет найдена директория, содержащая один из маркерных файлов.

    :param marker_files: Кортеж строк, представляющих имена файлов или каталогов, которые используются для определения корневой директории проекта.
    :return: Путь к корневой директории проекта.
    """
    current_path:Path = Path(__file__).resolve().parent
    project_root: Path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            project_root = parent
            break
    if project_root not in sys.path:
        sys.path.insert(0, str(project_root))
    return project_root

@singleton
class ProgramSettings:
    """
    Класс для хранения настроек программы.

    Загружает конфигурацию из `config.json` и учетные данные из `credentials.kdbx`.

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
        Инициализация настроек программы.

        Загружает конфигурацию из `config.json` и учетные данные из `credentials.kdbx`.
        """
        self.host_name: str = 'localhost'  #TODO:  рассмотреть возможность определения имени хоста
        self.base_dir: Path = set_project_root()
        self.config_path: Path = self.base_dir / 'src' / 'config.json'
        self.config: SimpleNamespace = self._load_config()
        if not self.config:
            logger.error('Ошибка при загрузке настроек')
            sys.exit(1) # Завершение работы программы, если не удалось загрузить конфигурацию
        self.config.project_name = self.base_dir.name
        self.MODE: str = self.config.MODE
        self.path: SimpleNamespace = SimpleNamespace(
            logs = self.base_dir / self.config.path.logs,
            tmp = self.base_dir / self.config.path.tmp,
            external = self.base_dir / self.config.path.external,
            google = self.base_dir / self.config.path.google,
            secrets = self.base_dir / 'secrets'
        )
        self.credentials: SimpleNamespace = SimpleNamespace() # Инициализируем пустой SimpleNamespace для хранения учетных данных
        self._load_credentials()


    def _load_config(self) -> SimpleNamespace | None:
        """
        Загружает конфигурацию проекта из `config.json`.

        :return: Объект SimpleNamespace с конфигурацией или None в случае ошибки.
        """
        try:
            return j_loads_ns(self.config_path)
        except Exception as ex:
           logger.error(f"Ошибка при загрузке файла конфигурации {self.config_path}: {ex}", exc_info=True)
           return None

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

         :param retry: Количество попыток открытия базы данных.
         :return: Объект PyKeePass, если база данных успешно открыта, иначе None.
        """
        password_file = self.path.secrets / 'password.txt'
        try:
             password = password_file.read_text(encoding="utf-8").strip() if password_file.exists() else None
             if not password:
                 password = getpass.getpass(f'Введите мастер-пароль KeePass: ').lower()
             kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), password=password)
             return kp
        except Exception as ex:
            logger.error(f"Не удалось открыть базу данных KeePass: {ex}", exc_info=True)
            return None


    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Aliexpress из KeePass.

        :param kp: Объект PyKeePass.
        :return: True если учетные данные загружены успешно, иначе False.
        """
        try:
            entry = kp.find_entries(group='suppliers/aliexpress/api', first=True)
            if entry:
                self.credentials.aliexpress = SimpleNamespace(
                    api_key=entry.get_custom_property('api_key'),
                    secret=entry.get_custom_property('secret'),
                    tracking_id=entry.get_custom_property('tracking_id'),
                    email=entry.username,
                    password=entry.password,
                )
                return True
            else:
                logger.error('Не найдены учетные данные Aliexpress в KeePass')
                return False
        except Exception as ex:
             logger.error(f"Ошибка при загрузке учетных данных Aliexpress: {ex}", exc_info=True)
             return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные OpenAI из KeePass.

        :param kp: Объект PyKeePass.
        :return: True если учетные данные загружены успешно, иначе False.
        """
        try:
            entry = kp.find_entries(group='openai', first=True)
            if entry:
                self.credentials.openai = SimpleNamespace(api_key=entry.password)
                assistants_entry = kp.find_entries(group='openai/assistants', first=True)
                if assistants_entry:
                   self.credentials.openai.assistant_id = assistants_entry.password
                return True
            else:
               logger.error('Не найдены учетные данные OpenAI в KeePass')
               return False
        except Exception as ex:
            logger.error(f"Ошибка при загрузке учетных данных OpenAI: {ex}", exc_info=True)
            return False


    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные GoogleAI из KeePass.

        :param kp: Объект PyKeePass.
        :return: True если учетные данные загружены успешно, иначе False.
        """
        try:
            entry = kp.find_entries(group='gemini', first=True)
            if entry:
                self.credentials.gemini = SimpleNamespace(api_key=entry.password)
                return True
            else:
                logger.error('Не найдены учетные данные Gemini в KeePass')
                return False
        except Exception as ex:
            logger.error(f"Ошибка при загрузке учетных данных Gemini: {ex}", exc_info=True)
            return False


    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Telegram из KeePass.

        :param kp: Объект PyKeePass.
        :return: True если учетные данные загружены успешно, иначе False.
        """
        try:
            entry = kp.find_entries(group='telegram', first=True)
            if entry:
                self.credentials.telegram = SimpleNamespace(token=entry.password)
                return True
            else:
                logger.error('Не найдены учетные данные Telegram в KeePass')
                return False
        except Exception as ex:
            logger.error(f"Ошибка при загрузке учетных данных Telegram: {ex}", exc_info=True)
            return False

    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Discord из KeePass.

        :param kp: Объект PyKeePass.
        :return: True если учетные данные загружены успешно, иначе False.
        """
        try:
            entry = kp.find_entries(group='discord', first=True)
            if entry:
                self.credentials.discord = SimpleNamespace(
                    application_id=entry.get_custom_property('application_id'),
                    public_key=entry.get_custom_property('public_key'),
                    bot_token=entry.password,
                )
                return True
            else:
                 logger.error('Не найдены учетные данные Discord в KeePass')
                 return False
        except Exception as ex:
            logger.error(f"Ошибка при загрузке учетных данных Discord: {ex}", exc_info=True)
            return False

    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop из KeePass.

        :param kp: Объект PyKeePass.
        :return: True если учетные данные загружены успешно, иначе False.
        """
        try:
            entry = kp.find_entries(group='prestashop/clients', first=True)
            if entry:
                self.credentials.presta = SimpleNamespace(
                    client=SimpleNamespace(
                        api_key=entry.get_custom_property('api_key'),
                        api_domain=entry.get_custom_property('api_domain'),
                        db_server=entry.get_custom_property('db_server'),
                        db_user=entry.get_custom_property('db_user'),
                        db_password=entry.get_custom_property('db_password'),
                    )
                )
                return True
            else:
                logger.error('Не найдены учетные данные PrestaShop в KeePass')
                return False
        except Exception as ex:
            logger.error(f"Ошибка при загрузке учетных данных PrestaShop: {ex}", exc_info=True)
            return False

    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop Translations из KeePass.

        :param kp: Объект PyKeePass.
        :return: True если учетные данные загружены успешно, иначе False.
        """
        try:
            entry = kp.find_entries(group='prestashop/translation', first=True)
            if entry:
               if not hasattr(self.credentials, 'presta'):
                   self.credentials.presta = SimpleNamespace()
               self.credentials.presta.translations = SimpleNamespace(
                    server=entry.get_custom_property('server'),
                    port=entry.get_custom_property('port'),
                    database=entry.get_custom_property('database'),
                    user=entry.get_custom_property('user'),
                    password=entry.get_custom_property('password'),
                )
               return True
            else:
                logger.error('Не найдены учетные данные PrestaShop translations в KeePass')
                return False
        except Exception as ex:
            logger.error(f"Ошибка при загрузке учетных данных PrestaShop translations: {ex}", exc_info=True)
            return False


    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные SMTP из KeePass.

        :param kp: Объект PyKeePass.
        :return: True если учетные данные загружены успешно, иначе False.
        """
        try:
            entry = kp.find_entries(group='smtp', first=True)
            if entry:
                self.credentials.smtp = SimpleNamespace(
                    server=entry.get_custom_property('server'),
                    port=entry.get_custom_property('port'),
                    user=entry.get_custom_property('user'),
                    password=entry.password,
                )
                return True
            else:
                 logger.error('Не найдены учетные данные SMTP в KeePass')
                 return False
        except Exception as ex:
            logger.error(f"Ошибка при загрузке учетных данных SMTP: {ex}", exc_info=True)
            return False

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Facebook из KeePass.

        :param kp: Объект PyKeePass.
        :return: True если учетные данные загружены успешно, иначе False.
        """
        try:
            entry = kp.find_entries(group='facebook', first=True)
            if entry:
                self.credentials.facebook = SimpleNamespace(
                    app_id=entry.get_custom_property('app_id'),
                    app_secret=entry.get_custom_property('app_secret'),
                    access_token=entry.password,
                )
                return True
            else:
                logger.error('Не найдены учетные данные Facebook в KeePass')
                return False
        except Exception as ex:
            logger.error(f"Ошибка при загрузке учетных данных Facebook: {ex}", exc_info=True)
            return False

    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Google API из KeePass.

        :param kp: Объект PyKeePass.
        :return: True если учетные данные загружены успешно, иначе False.
        """
        try:
            entry = kp.find_entries(group='google/gapi', first=True)
            if entry:
               self.credentials.gapi = SimpleNamespace(api_key=entry.password)
               return True
            else:
                logger.error('Не найдены учетные данные Google API в KeePass')
                return False
        except Exception as ex:
             logger.error(f"Ошибка при загрузке учетных данных Google API: {ex}", exc_info=True)
             return False

    def now(self) -> str:
        """
        Возвращает текущую метку времени в формате, указанном в файле `config.json`.

        :return: Текущая метка времени в виде строки.
        """
        import datetime
        return datetime.datetime.now().strftime(self.config.date_format)


# Global instance of ProgramSettings
gs: ProgramSettings = ProgramSettings()
```