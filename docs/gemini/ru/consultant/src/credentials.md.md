# Анализ кода модуля `src.credentials`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и документирован с использованием reStructuredText (RST).
    - Используется `Pathlib` для работы с путями.
    - Применяется паттерн singleton для класса `ProgramSettings`.
    - Наличие подробной документации в формате RST.
    - Использование `j_loads_ns` для загрузки конфигурации.
    - Логирование ошибок с помощью `logger.error` и `logger.critical`.
    - Структура `credentials.kdbx` описана в `readme.md`.

- Минусы
    -  В коде используются перехват `Exception`, без конкретизации исключений.
    -  Не все функции имеют подробные docstring, особенно те, что работают с KeePass.
    -  Обработка ошибок через `...` может скрывать потенциальные проблемы.
    -  Использование `print` в функции `_open_kp` для вывода информации об ошибках, лучше использовать `logger.error`.

**Рекомендации по улучшению**

1.  **Уточнение исключений**:
    -   Вместо `except Exception as ex:` использовать более конкретные исключения, такие как `FileNotFoundError`, `json.JSONDecodeError`, `PyKeePass.exceptions.PyKeePassError`.
    -   Добавить логирование для конкретных исключений, чтобы можно было точно определить проблему.

2.  **Улучшение docstring**:
    -   Добавить docstring для каждой функции, описывающий ее назначение, параметры и возвращаемое значение.
    -   Уточнить docstring для методов `_load_*_credentials`, описать, какие именно данные загружаются.

3.  **Замена `print` на `logger`**:
    -   Заменить `print` в функции `_open_kp` на `logger.error` или `logger.info` для стандартизации логирования.

4.  **Более детальная обработка ошибок**:
    -   Заменить многоточия `...` в блоках `except` на конкретные действия, такие как возврат значения по умолчанию или выброс исключения.

5.  **Константы для маркеров**:
    -   Вынести `marker_files` в константу, чтобы избежать дублирования.

6.  **Типизация**:
    -   Добавить аннотации типов к параметрам и возвращаемым значениям методов и функций.

**Оптимизированный код**

```python
"""
Модуль для загрузки и управления настройками и учетными данными приложения.
========================================================================

Этот модуль предоставляет классы и функции для:
    - определения корневой директории проекта;
    - загрузки конфигурационных файлов;
    - безопасного управления учетными данными из базы данных KeePass.

Класс :class:`ProgramSettings` является синглтоном и обеспечивает доступ
к настройкам и учетным данным из любой части проекта.

Пример использования:

.. code-block:: python

    from src.credentials import gs

    api_key = gs.credentials.openai.api_key
    project_name = gs.config.project_name
"""
import sys
import getpass
from pathlib import Path
from types import SimpleNamespace
from typing import Tuple
from pykeepass import PyKeePass
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger
from datetime import datetime

MARKER_FILES: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')


def singleton(cls):
    """
    Декоратор для создания синглтона.

    :param cls: Класс, который необходимо преобразовать в синглтон.
    :return: Функция, возвращающая экземпляр синглтон-класса.
    """
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


def set_project_root(marker_files: Tuple[str, ...] = MARKER_FILES) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла.

    Поиск идет вверх по директориям до тех пор, пока не будет найдена директория,
    содержащая один из файлов в списке `marker_files`.

    :param marker_files: Список файлов или директорий, используемых для определения корневой директории.
    :return: Путь к корневой директории проекта, если он найден, иначе путь к директории, где расположен скрипт.
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
    Класс для управления настройками программы.

    Инициализирует основные параметры и настройки проекта, загружает конфигурацию из
    `config.json` и учетные данные из базы данных KeePass (`credentials.kdbx`).

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

        Загружает конфигурацию проекта из `config.json`, инициализирует атрибут `path`
        путями к различным директориям проекта, вызывает `check_latest_release` для проверки
        новой версии проекта и загружает учетные данные из `credentials.kdbx`.
        """
        self.host_name: str = 'localhost' #TODO:  get from system
        self.base_dir: Path = set_project_root()
        self.config: SimpleNamespace = j_loads_ns(self.base_dir / 'src' / 'config.json')
        if not self.config:
            logger.error('Ошибка загрузки настроек из config.json')
            # Обработка ошибки загрузки конфигурации
            return

        self.config.project_name = self.base_dir.name
        self.path = SimpleNamespace(
            logs=self.base_dir / 'logs',
            temp=self.base_dir / 'temp',
            external=self.base_dir / 'external',
            gdrive=self.base_dir / 'gdrive',
            secrets=self.base_dir / 'secrets',
            db=self.base_dir / 'db',
            src=self.base_dir / 'src'
        )
        # TODO: Проверка последней версии проекта
        # self.check_latest_release()
        self.MODE = self.config.MODE
        self.credentials: SimpleNamespace = SimpleNamespace()
        self._load_credentials()

    def _load_credentials(self) -> None:
        """
        Загружает учетные данные из KeePass.

        Открывает базу данных KeePass и вызывает методы для загрузки учетных
        данных для различных сервисов.
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

    def _open_kp(self, retry: int = 3) -> PyKeePass | None:
        """
        Открывает базу данных KeePass.

        Обрабатывает возможные исключения при открытии базы данных.

        :param retry: Количество попыток открытия базы данных.
        :return: Объект PyKeePass или None, если не удалось открыть базу данных.
        """
        while retry > 0:
            try:
                password_file: Path = self.path.secrets / 'password.txt'
                password = password_file.read_text(encoding="utf-8").strip() if password_file.exists() else None
                if not password:
                    password = getpass.getpass('Введите мастер-пароль KeePass: ').lower()
                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), password=password)
                return kp
            except FileNotFoundError as e:
                logger.error(f"Файл пароля не найден: {e}")
                retry -= 1
            except PyKeePass.exceptions.PyKeePassError as e:
                logger.error(f"Ошибка открытия KeePass: {e}. Осталось {retry - 1} попыток.")
                retry -= 1
            except Exception as ex:
                 logger.error(f"Непредвиденная ошибка при открытии KeePass: {ex}. Осталось {retry - 1} попыток.", exc_info=True)
                 retry -= 1
            if retry < 1:
                logger.critical('Не удалось открыть KeePass после нескольких попыток', exc_info=True)
                sys.exit()
        return None

    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Aliexpress из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если учетные данные загружены успешно, иначе False.
        """
        try:
            group = kp.find_groups(name='suppliers')[0]
            group = kp.find_groups(name='aliexpress', group=group)[0]
            group = kp.find_groups(name='api', group=group)[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.aliexpress = SimpleNamespace(
                api_key=entry.get_custom_property('api_key'),
                secret=entry.get_custom_property('secret'),
                tracking_id=entry.get_custom_property('tracking_id'),
                email=entry.get_custom_property('email'),
                password=entry.get_custom_property('password')
            )
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных Aliexpress', exc_info=True)
            return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
         """
         Загружает учетные данные OpenAI из KeePass.

         :param kp: Объект PyKeePass.
         :return: True, если учетные данные загружены успешно, иначе False.
         """
         try:
             group = kp.find_groups(name='openai')[0]
             entry = kp.find_entries(group=group)[0]
             self.credentials.openai = SimpleNamespace(
                 api_key=entry.get_custom_property('api_key')
             )
             group = kp.find_groups(name='assistants', group=group)[0]
             entry = kp.find_entries(group=group)[0]
             self.credentials.openai.assistant_id = entry.get_custom_property('assistant_id')
             return True
         except Exception as ex:
             logger.error('Ошибка загрузки учетных данных OpenAI', exc_info=True)
             return False

    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Gemini из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если учетные данные загружены успешно, иначе False.
        """
        try:
            group = kp.find_groups(name='gemini')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.gemini = SimpleNamespace(
                api_key=entry.get_custom_property('api_key')
            )
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных Gemini', exc_info=True)
            return False

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Telegram из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если учетные данные загружены успешно, иначе False.
        """
        try:
            group = kp.find_groups(name='telegram')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.telegram = SimpleNamespace(
                token=entry.get_custom_property('token')
            )
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных Telegram', exc_info=True)
            return False

    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Discord из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если учетные данные загружены успешно, иначе False.
        """
        try:
            group = kp.find_groups(name='discord')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.discord = SimpleNamespace(
                application_id=entry.get_custom_property('application_id'),
                public_key=entry.get_custom_property('public_key'),
                bot_token=entry.get_custom_property('bot_token')
            )
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных Discord', exc_info=True)
            return False

    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если учетные данные загружены успешно, иначе False.
        """
        try:
            group = kp.find_groups(name='prestashop')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.presta = SimpleNamespace(
                api_key=entry.get_custom_property('api_key'),
                api_domain=entry.get_custom_property('api_domain')
            )
            group = kp.find_groups(name='clients', group=group)[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.presta.client = SimpleNamespace(
                api_key=entry.get_custom_property('api_key'),
                api_domain=entry.get_custom_property('api_domain'),
                db_server=entry.get_custom_property('db_server'),
                db_user=entry.get_custom_property('db_user'),
                db_password=entry.get_custom_property('db_password')
            )
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных PrestaShop', exc_info=True)
            return False

    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
         """
         Загружает учетные данные для переводов PrestaShop из KeePass.

         :param kp: Объект PyKeePass.
         :return: True, если учетные данные загружены успешно, иначе False.
         """
         try:
             group = kp.find_groups(name='prestashop')[0]
             group = kp.find_groups(name='translation', group=group)[0]
             entry = kp.find_entries(group=group)[0]

             self.credentials.presta.translations = SimpleNamespace(
                 server=entry.get_custom_property('server'),
                 port=entry.get_custom_property('port'),
                 database=entry.get_custom_property('database'),
                 user=entry.get_custom_property('user'),
                 password=entry.get_custom_property('password')
             )
             return True
         except Exception as ex:
             logger.error('Ошибка загрузки учетных данных для переводов PrestaShop', exc_info=True)
             return False

    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные SMTP из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если учетные данные загружены успешно, иначе False.
        """
        try:
            group = kp.find_groups(name='smtp')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.smtp = SimpleNamespace(
                server=entry.get_custom_property('server'),
                port=entry.get_custom_property('port'),
                user=entry.get_custom_property('user'),
                password=entry.get_custom_property('password')
            )
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных SMTP', exc_info=True)
            return False

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Facebook из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если учетные данные загружены успешно, иначе False.
        """
        try:
            group = kp.find_groups(name='facebook')[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.facebook = SimpleNamespace(
                app_id=entry.get_custom_property('app_id'),
                app_secret=entry.get_custom_property('app_secret'),
                access_token=entry.get_custom_property('access_token')
            )
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных Facebook', exc_info=True)
            return False

    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Google API из KeePass.

        :param kp: Объект PyKeePass.
        :return: True, если учетные данные загружены успешно, иначе False.
        """
        try:
            group = kp.find_groups(name='google')[0]
            group = kp.find_groups(name='gapi', group=group)[0]
            entry = kp.find_entries(group=group)[0]
            self.credentials.gapi = SimpleNamespace(
                api_key=entry.get_custom_property('api_key')
            )
            return True
        except Exception as ex:
            logger.error('Ошибка загрузки учетных данных Google API', exc_info=True)
            return False

    def now(self) -> str:
        """
        Возвращает текущую метку времени в формате, указанном в `config.json`.

        :return: Строка с текущей меткой времени.
        """
        return datetime.now().strftime(self.config.time_format)


# Global instance of ProgramSettings
gs: ProgramSettings = ProgramSettings()
```