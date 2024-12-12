# Анализ кода модуля `src.credentials`

**Качество кода**
7
 -  Плюсы
        -  Хорошая структурированность и подробное документирование функционала в формате `markdown`.
        -  Используется декоратор `@singleton` для создания синглтона.
        -  Присутствует обработка исключений при открытии базы данных KeePass.
        -  Организовано хранение различных учетных данных в базе данных KeePass.
        -  Используется `j_loads_ns` для загрузки конфигурации.

 -  Минусы
    -  Не все комментарии и docstring соответствуют формату reStructuredText (RST).
    -  В коде используется `print` для вывода сообщений об ошибках, следует использовать `logger.error`.
    -  Некоторые исключения обрабатываются без явного логирования.
    -  Файл `password.txt` для хранения пароля в режиме разработки является уязвимостью. Необходимо разработать более безопасный способ хранения.
    -  Не хватает документации в формате RST для функций и методов в самом коде.
    -  Некоторые переменные в коде не имеют аннотаций типов.

**Рекомендации по улучшению**

1.  **Привести документацию в коде к формату RST:**
    -  Переписать docstring функций, методов и классов в формате RST.
    -  Добавить описание модуля в начале файла в формате RST.
2.  **Использовать logger для вывода ошибок:**
    -  Заменить все `print` на `logger.error` или `logger.critical` для вывода ошибок.
    -  Добавить `logger.debug` для отладочных сообщений.
3.  **Улучшить обработку исключений:**
    -  Использовать `logger.error` для обработки исключений вместо `try-except` без логирования.
4.  **Улучшить безопасность хранения паролей:**
    -  Рассмотреть использование более безопасных способов хранения паролей в режиме разработки (например, переменные окружения).
5.  **Добавить аннотации типов:**
    -  Добавить аннотации типов для всех переменных и параметров функций.
6.  **Убрать избыточные блоки `try-except`:**
    -  Избегать `try-except` там где можно использовать проверку на наличие данных.
7. **Соблюдение PEP 8:**
    - Привести код в соответствие со стандартами PEP 8, например, добавить пробелы вокруг операторов.

**Оптимизированный код**

```python
"""
Модуль для управления настройками и учетными данными приложения.
=========================================================================================

Этот модуль содержит класс :class:`ProgramSettings`, который используется для загрузки и хранения конфигурации,
учетных данных и путей проекта. Также включает функции для определения корневой директории проекта и
декоратор для создания синглтона.

Пример использования
--------------------

Пример использования класса `ProgramSettings`:

.. code-block:: python

    from src.credentials import gs
    api_key = gs.credentials.openai.api_key

"""
import sys
import getpass
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Tuple
from pykeepass import PyKeePass
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger


class CredentialsError(Exception):
    """Исключение для ошибок с данными учетных данных."""
    ...


class DefaultSettingsException(Exception):
    """Исключение для ошибок с настройками по умолчанию."""
    ...


def singleton(cls):
    """
    Декоратор для создания класса-синглтона.

    :param cls: Класс, который должен быть преобразован в синглтон.
    :return: Функция, возвращающая экземпляр класса-синглтона.
    """
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


def set_project_root(marker_files: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с текущей директории файла,
    ища вверх и останавливаясь на первой директории, содержащей любой из маркерных файлов.

    :param marker_files: Имена файлов или директорий для идентификации корневой директории проекта.
    :return: Путь к корневой директории, если найдена, иначе директория, где находится скрипт.
    """
    current_path: Path = Path(__file__).resolve().parent
    root_path: Path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root_path = parent
            break
    if root_path not in sys.path:
        sys.path.insert(0, str(root_path))
    return root_path


@singleton
class ProgramSettings:
    """
    Класс настроек программы. Устанавливает основные параметры и настройки проекта.
    Загружает конфигурацию из ``config.json`` и данные учетных данных из файла ``credentials.kdbx``
    в базе данных KeePass.
    """
    host_name: str = 'localhost'
    base_dir: Path = set_project_root()
    config: SimpleNamespace
    credentials: SimpleNamespace
    MODE: str = 'dev'  # TODO:  Добавить возможность переключения режимов
    path: SimpleNamespace

    def __init__(self, **kwargs):
        """
        Инициализирует экземпляр класса.

        :param kwargs: Произвольные ключевые аргументы.
        """
        # код загружает конфигурацию из config.json
        self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
        if not self.config:
            logger.error('Ошибка при загрузке настроек')
            ...
            return

        self.config.project_name = self.base_dir.name

        # код устанавливает пути к директориям проекта
        self.path = SimpleNamespace(
            logs=self.base_dir / 'logs',
            tmp=self.base_dir / 'tmp',
            external=self.base_dir / 'external',
            gdrive=self.base_dir / 'gdrive',
            secrets=self.base_dir / 'secrets'
        )

        # код загружает учетные данные из credentials.kdbx
        self._load_credentials()

        # TODO:  self.check_latest_release()

    def _load_credentials(self) -> None:
        """Загружает учетные данные из KeePass."""
        kp = self._open_kp()
        if not kp:
            logger.error('Не удалось открыть базу данных KeePass')
            return
        self.credentials = SimpleNamespace()
        self.credentials.aliexpress = SimpleNamespace()
        self.credentials.openai = SimpleNamespace()
        self.credentials.gemini = SimpleNamespace()
        self.credentials.telegram = SimpleNamespace()
        self.credentials.discord = SimpleNamespace()
        self.credentials.presta = SimpleNamespace()
        self.credentials.presta.client = SimpleNamespace()
        self.credentials.presta.translations = SimpleNamespace()
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

        :param retry: Количество попыток.
        :return: Объект PyKeePass или None в случае неудачи.
        """
        while retry > 0:
            try:
                # код считывает пароль из файла password.txt или запрашивает его через консоль
                password = (Path(self.path.secrets / 'password.txt').read_text(encoding="utf-8") or None)
                if not password:
                    password = getpass.getpass(prompt='Введите мастер-пароль KeePass: ').lower()
                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), password=password)
                return kp
            except Exception as ex:
                logger.error(f"Не удалось открыть базу данных KeePass. Исключение: {ex}, осталось попыток: {retry-1}.")
                retry -= 1
                if retry < 1:
                    logger.critical('Не удалось открыть базу данных KeePass после нескольких попыток', exc_info=True)
                    sys.exit()
        return None


    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Aliexpress из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если данные загружены, иначе False.
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
            logger.error('Ошибка при загрузке учетных данных Aliexpress', exc_info=True)
            ...
            return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные OpenAI из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если данные загружены, иначе False.
        """
        try:
            group = kp.find_groups(name='openai')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.openai.api_key = entry.get_custom_property('api_key')
            entry = group.find_groups(name='assistants')[0].find_entries(title='entry')[0]
            self.credentials.openai.assistant_id = entry.get_custom_property('assistant_id')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных OpenAI', exc_info=True)
            ...
            return False

    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные GoogleAI из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если данные загружены, иначе False.
        """
        try:
            group = kp.find_groups(name='gemini')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.gemini.api_key = entry.get_custom_property('api_key')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных Gemini', exc_info=True)
            ...
            return False

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Telegram из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если данные загружены, иначе False.
        """
        try:
            group = kp.find_groups(name='telegram')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.telegram.token = entry.get_custom_property('token')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных Telegram', exc_info=True)
            ...
            return False

    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Discord из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если данные загружены, иначе False.
        """
        try:
            group = kp.find_groups(name='discord')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.discord.application_id = entry.get_custom_property('application_id')
            self.credentials.discord.public_key = entry.get_custom_property('public_key')
            self.credentials.discord.bot_token = entry.get_custom_property('bot_token')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных Discord', exc_info=True)
            ...
            return False

    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если данные загружены, иначе False.
        """
        try:
            group = kp.find_groups(name='prestashop')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.presta.api_key = entry.get_custom_property('api_key')
            self.credentials.presta.api_domain = entry.get_custom_property('api_domain')
            self.credentials.presta.db_server = entry.get_custom_property('db_server')
            self.credentials.presta.db_user = entry.get_custom_property('db_user')
            self.credentials.presta.db_password = entry.get_custom_property('db_password')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных PrestaShop', exc_info=True)
            ...
            return False

    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop Translations из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если данные загружены, иначе False.
        """
        try:
            group = kp.find_groups(name='prestashop')[0].find_groups(name='translation')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.presta.translations.server = entry.get_custom_property('server')
            self.credentials.presta.translations.port = entry.get_custom_property('port')
            self.credentials.presta.translations.database = entry.get_custom_property('database')
            self.credentials.presta.translations.user = entry.get_custom_property('user')
            self.credentials.presta.translations.password = entry.get_custom_property('password')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных PrestaShop Translations', exc_info=True)
            ...
            return False

    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные SMTP из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если данные загружены, иначе False.
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
            logger.error('Ошибка при загрузке учетных данных SMTP', exc_info=True)
            ...
            return False

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Facebook из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если данные загружены, иначе False.
        """
        try:
            group = kp.find_groups(name='facebook')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.facebook.app_id = entry.get_custom_property('app_id')
            self.credentials.facebook.app_secret = entry.get_custom_property('app_secret')
            self.credentials.facebook.access_token = entry.get_custom_property('access_token')
            return True
        except Exception as ex:
            logger.error('Ошибка при загрузке учетных данных Facebook', exc_info=True)
            ...
            return False

    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Google API из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если данные загружены, иначе False.
        """
        try:
            group = kp.find_groups(name='google')[0].find_groups(name='gapi')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.gapi.api_key = entry.get_custom_property('api_key')
            return True
        except Exception as ex:
             logger.error('Ошибка при загрузке учетных данных Google API', exc_info=True)
             ...
             return False

    def now(self) -> str:
        """
        Возвращает текущую метку времени в формате, указанном в файле ``config.json``.

        :return: Строка с текущей меткой времени.
        """
        from datetime import datetime

        return datetime.now().strftime(self.config.time_format)


# Global instance of ProgramSettings
gs: ProgramSettings = ProgramSettings()
```