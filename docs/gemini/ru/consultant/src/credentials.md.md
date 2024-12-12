# Анализ кода модуля `src.credentials`

**Качество кода**

*   **Соответствие требованиям по оформлению кода: 6/10**
    *   **Плюсы:**
        *   Код содержит подробную документацию в формате Markdown.
        *   Присутствуют описания классов, методов и переменных.
        *   Используются аннотации типов.
    *   **Минусы:**
        *   Не используется reStructuredText (RST) для docstring.
        *   Не все функции и методы имеют docstring.
        *   В коде есть стандартные `try-except` блоки, которые следует заменить на использование `logger.error`.
        *   Не используются `j_loads` или `j_loads_ns` для чтения JSON файлов.
        *   Отсутствуют некоторые необходимые импорты.
        *   Не все комментарии после `#` объясняют следующий за ними код.
        *   Не все функции имеют описание в RST формате.
        *   Стиль комментариев в коде не соответствует стандарту.

**Рекомендации по улучшению**

1.  **Документация:**
    *   Переписать все docstring в формате reStructuredText (RST).
    *   Добавить docstring для всех функций, методов и классов.
2.  **Импорты:**
    *   Добавить недостающие импорты: `sys`, `getpass`, `Path`, `SimpleNamespace`, `j_loads_ns`, `PyKeePass`
    *   Использовать `from src.utils.jjson import j_loads_ns` вместо `json.load`.
    *   Использовать `from pathlib import Path` для работы с путями.
    *   Использовать `from types import SimpleNamespace` для создания объекта настроек.
3.  **Логирование:**
    *   Заменить стандартные блоки `try-except` на использование `logger.error`.
    *   Добавить логирование ошибок при загрузке настроек и работы с KeePass.
4.  **Безопасность:**
    *   Заменить хранение пароля в `password.txt` на более безопасный механизм, например, через переменные окружения.
5.  **Структура кода:**
    *   Привести имена функций, переменных и импортов в соответствии с остальным кодом.
6.  **Комментарии:**
    *   Комментарии после `#` должны подробно описывать следующий за ними код.
    *   Переписать комментарии в формате RST.
    *   Избегать слов "получаем", "делаем" и т.п., использовать более конкретные формулировки.
7.  **Singleton:**
    *   Переписать реализацию декоратора singleton.

**Оптимизированный код**

```python
"""
Модуль для управления настройками программы и учетными данными.
==================================================================

Этот модуль предоставляет класс :class:`ProgramSettings`, который загружает настройки из
файла `config.json` и учетные данные из базы данных KeePass (`credentials.kdbx`).
Также предоставляет функцию :func:`set_project_root` для определения корневой директории проекта.

Пример использования
--------------------

.. code-block:: python

    from src.credentials import ProgramSettings

    settings = ProgramSettings()
    print(settings.credentials.openai.api_key)
"""
import sys
import getpass
from pathlib import Path
from types import SimpleNamespace
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger
from pykeepass import PyKeePass


def singleton(cls):
    """
    Декоратор для создания singleton класса.
    
    :param cls: Класс, который должен быть преобразован в singleton.
    :return: Функция, возвращающая экземпляр singleton класса.
    """
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с текущей директории файла,
    поднимаясь вверх по дереву каталогов, пока не найдет каталог, содержащий один из файлов-маркеров.

    :param marker_files:  Кортеж имен файлов или директорий для идентификации корневой директории проекта.
    :return: Путь к корневой директории проекта, если она найдена, иначе - путь к директории, где находится скрипт.
    """
    current_path: Path = Path(__file__).resolve().parent
    __root__:Path = current_path
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
    Класс для хранения настроек программы.
    
    Управляет основными параметрами и настройками проекта. Загружает конфигурацию
    из `config.json` и учетные данные из `credentials.kdbx`.

    :ivar host_name: Имя хоста.
    :vartype host_name: str
    :ivar base_dir: Путь к корневой директории проекта.
    :vartype base_dir: Path
    :ivar config: Объект, содержащий настройки проекта.
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
        Инициализация класса.

        Загружает настройки проекта из `config.json`, инициализирует атрибут `path` путями к директориям проекта,
        вызывает `check_latest_release` для проверки наличия новой версии проекта и загружает учетные данные из `credentials.kdbx`.
        """
        self.host_name: str = 'localhost'
        self.base_dir: Path = set_project_root()
        
        # Загрузка настроек из config.json
        self.config:SimpleNamespace = j_loads_ns(self.base_dir / 'src' / 'config.json')
        if not self.config:
            logger.error('Ошибка загрузки настроек')
            ...
            return

        self.config.project_name = self.base_dir.name
        
        # Инициализация путей проекта
        self.path:SimpleNamespace = SimpleNamespace()
        self.path.logs: Path = self.base_dir / self.config.paths.logs
        self.path.tmp: Path = self.base_dir / self.config.paths.tmp
        self.path.external: Path = self.base_dir / self.config.paths.external
        self.path.gdrive: Path = self.base_dir / self.config.paths.gdrive
        self.path.secrets: Path = self.base_dir / 'secrets'
        self.MODE = self.config.MODE if hasattr(self.config, 'MODE') else 'dev'

        # Загрузка учетных данных из KeePass
        self.credentials: SimpleNamespace = SimpleNamespace()
        self._load_credentials()
        # self.check_latest_release() # TODO
        

    def _load_credentials(self) -> None:
        """Загружает учетные данные из KeePass."""
        kp = self._open_kp()
        if not kp:
            logger.error('Не удалось открыть KeePass базу данных')
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
        :return: Объект PyKeePass или None, если не удалось открыть базу данных.
        """
        while retry > 0:
            try:
                # Чтение пароля из файла или ввод с консоли
                password: str = (Path(self.path.secrets / 'password.txt').read_text(encoding="utf-8") 
                                 if (self.path.secrets / 'password.txt').exists() 
                                 else None)
                kp: PyKeePass = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), 
                                         password=password or getpass.getpass(print('Введите мастер-пароль KeePass: ').lower()))
                return kp
            except Exception as ex:
                logger.error(f'Не удалось открыть KeePass базу данных. Ошибка: {ex}, {retry-1} попыток осталось.', exc_info=True)
                retry -= 1
                if retry < 1:
                    logger.critical('Не удалось открыть KeePass базу данных после нескольких попыток', exc_info=True)
                    sys.exit()
        return None

    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Aliexpress из KeePass."""
        try:
            group = kp.find_entries(path='suppliers/aliexpress/api', first=True)
            if not group:
                logger.error('Группа `suppliers/aliexpress/api` не найдена в KeePass.')
                return False
            self.credentials.aliexpress.api_key = group.get_custom_property('api_key')
            self.credentials.aliexpress.secret = group.get_custom_property('secret')
            self.credentials.aliexpress.tracking_id = group.get_custom_property('tracking_id')
            self.credentials.aliexpress.email = group.get_custom_property('email')
            self.credentials.aliexpress.password = group.get_custom_property('password')
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных Aliexpress', exc_info=True)
            return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные OpenAI из KeePass."""
        try:
            group = kp.find_entries(path='openai', first=True)
            if not group:
                logger.error('Группа `openai` не найдена в KeePass.')
                return False
            self.credentials.openai.api_key = group.get_custom_property('api_key')

            group = kp.find_entries(path='openai/assistants', first=True)
            if not group:
                logger.error('Группа `openai/assistants` не найдена в KeePass.')
                return False
            self.credentials.openai.assistant_id = group.get_custom_property('assistant_id')
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных OpenAI', exc_info=True)
            return False
    
    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные GoogleAI из KeePass."""
        try:
            group = kp.find_entries(path='gemini', first=True)
            if not group:
                logger.error('Группа `gemini` не найдена в KeePass.')
                return False
            self.credentials.gemini.api_key = group.get_custom_property('api_key')
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных GoogleAI', exc_info=True)
            return False

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Telegram из KeePass."""
        try:
            group = kp.find_entries(path='telegram', first=True)
            if not group:
               logger.error('Группа `telegram` не найдена в KeePass.')
               return False
            self.credentials.telegram.token = group.get_custom_property('token')
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных Telegram', exc_info=True)
            return False
    
    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Discord из KeePass."""
        try:
            group = kp.find_entries(path='discord', first=True)
            if not group:
                logger.error('Группа `discord` не найдена в KeePass.')
                return False
            self.credentials.discord.application_id = group.get_custom_property('application_id')
            self.credentials.discord.public_key = group.get_custom_property('public_key')
            self.credentials.discord.bot_token = group.get_custom_property('bot_token')
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных Discord', exc_info=True)
            return False

    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные PrestaShop из KeePass."""
        try:
            group = kp.find_entries(path='prestashop/clients', first=True)
            if not group:
                logger.error('Группа `prestashop/clients` не найдена в KeePass.')
                return False
            self.credentials.presta.client.api_key = group.get_custom_property('api_key')
            self.credentials.presta.client.api_domain = group.get_custom_property('api_domain')
            self.credentials.presta.client.db_server = group.get_custom_property('db_server')
            self.credentials.presta.client.db_user = group.get_custom_property('db_user')
            self.credentials.presta.client.db_password = group.get_custom_property('db_password')
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных PrestaShop', exc_info=True)
            return False

    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные PrestaShop Translation из KeePass."""
        try:
            group = kp.find_entries(path='prestashop/translation', first=True)
            if not group:
                logger.error('Группа `prestashop/translation` не найдена в KeePass.')
                return False
            self.credentials.presta.translations.server = group.get_custom_property('server')
            self.credentials.presta.translations.port = group.get_custom_property('port')
            self.credentials.presta.translations.database = group.get_custom_property('database')
            self.credentials.presta.translations.user = group.get_custom_property('user')
            self.credentials.presta.translations.password = group.get_custom_property('password')
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных PrestaShop Translation', exc_info=True)
            return False

    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные SMTP из KeePass."""
        try:
            group = kp.find_entries(path='smtp', first=True)
            if not group:
                logger.error('Группа `smtp` не найдена в KeePass.')
                return False
            self.credentials.smtp.server = group.get_custom_property('server')
            self.credentials.smtp.port = group.get_custom_property('port')
            self.credentials.smtp.user = group.get_custom_property('user')
            self.credentials.smtp.password = group.get_custom_property('password')
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных SMTP', exc_info=True)
            return False

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Facebook из KeePass."""
        try:
            group = kp.find_entries(path='facebook', first=True)
            if not group:
                logger.error('Группа `facebook` не найдена в KeePass.')
                return False
            self.credentials.facebook.app_id = group.get_custom_property('app_id')
            self.credentials.facebook.app_secret = group.get_custom_property('app_secret')
            self.credentials.facebook.access_token = group.get_custom_property('access_token')
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных Facebook', exc_info=True)
            return False
    
    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Google API из KeePass."""
        try:
            group = kp.find_entries(path='google/gapi', first=True)
            if not group:
                logger.error('Группа `google/gapi` не найдена в KeePass.')
                return False
            self.credentials.gapi.api_key = group.get_custom_property('api_key')
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных Google API', exc_info=True)
            return False

    def now(self) -> str:
        """
        Возвращает текущую временную метку в формате, указанном в `config.json`.
        
        :return: Текущая временная метка в виде строки.
        """
        return datetime.now().strftime(self.config.format.time) if hasattr(self.config, 'format') and hasattr(self.config.format, 'time') else str(datetime.now())


# Глобальный экземпляр ProgramSettings
gs = ProgramSettings()
```