# Анализ кода модуля `credentials`

**Качество кода**

6/10
- Плюсы
    - Код хорошо структурирован и разделен на логические блоки.
    - Использование `PyKeePass` для работы с базой данных KeePass.
    - Реализован механизм для загрузки различных типов учетных данных.
    - Есть описание структуры базы данных KeePass.
    - Использование синглтона для `ProgramSettings`.
- Минусы
    - Используются открытые пароли для режима разработки.
    - Не везде используется `logger.error` для обработки исключений.
    - Отсутствуют docstring для функций и класса `ProgramSettings`.
    - В коде есть `...` как точки остановки.
    - Использование `print` вместо `logger.info` или `logger.debug`.
    - Некоторые комментарии не соответствуют стандарту RST.
    -  Отсутствует описание модуля в начале файла.
    - В коде не используется `j_loads` для загрузки config.json, а вместо этого используется `j_loads_ns`

**Рекомендации по улучшению**

1.  **Безопасность**:
    -   Удалить чтение пароля из файла `password.txt`, и добавить только ввод пароля из консоли, как в режиме production.
    -   Рассмотреть возможность использования более безопасного метода хранения мастер-пароля, например, с использованием переменных окружения или менеджера секретов.
2.  **Обработка ошибок**:
    -   Заменить все `print` на `logger.info` и `logger.debug`.
    -   Использовать `logger.error` с `exc_info=True` для регистрации исключений.
    -   Обработать все возможные исключения в `_load_credentials`, `_open_kp` и других методах с помощью `logger.error`.
    -   Убрать `...` из кода как точки остановки, заменив их либо логикой, либо явными вызовами исключений.
3.  **Документация**:
    -   Добавить описание модуля.
    -   Добавить docstring для класса `ProgramSettings`, всех его методов и декоратора `singleton`.
    -   Уточнить комментарии в коде для соответствия стандарту RST.
4.  **Код**:
    -  Использовать `j_loads` вместо `j_loads_ns` для загрузки `config.json`.
    -   Проверить и привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.
    -  Использовать `from src.logger.logger import logger` для импорта логгера.
5. **Структура**:
    -  Использовать константы для путей к файлам и директориям, чтобы избежать дублирования кода.

**Оптимизированный код**

```python
"""
Модуль для загрузки и управления настройками и учетными данными проекта.
======================================================================

Этот модуль предоставляет класс :class:`ProgramSettings` для управления
конфигурацией проекта и учетными данными, загружаемыми из базы данных KeePass.
Также включает функции для определения корневого каталога проекта и создания синглтона.

Пример использования:
--------------------
.. code-block:: python

    from src.credentials import gs

    # Получение API ключа OpenAI
    api_key = gs.credentials.openai.api_key
"""
import sys
import getpass
from pathlib import Path
from types import SimpleNamespace
from typing import Any, TypeVar, Callable
from src.utils.jjson import j_loads # Используется j_loads вместо j_loads_ns
from src.logger.logger import logger # Исправлен импорт логгера
from pykeepass import PyKeePass
from pykeepass.exceptions import (
    BinaryError,
    CredentialsError,
    DefaultSettingsException,
    HeaderChecksumError,
    KeePassException,
    PayloadChecksumError,
    UnableToSendToRecycleBin,
)


T = TypeVar('T')


def singleton(cls: type[T]) -> Callable[[], T]:
    """Декоратор для создания класса-синглтона.

    Args:
        cls: Класс, который должен быть преобразован в синглтон.

    Returns:
        Функция, возвращающая экземпляр класса-синглтона.
    """
    instance: T | None = None

    def get_instance() -> T:
        nonlocal instance
        if instance is None:
            instance = cls()
        return instance
    return get_instance


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с текущей директории файла,
    ища вверх и останавливаясь на первой директории, содержащей любой из маркерных файлов.

    Args:
        marker_files (tuple): Имена файлов или директорий для идентификации корневой директории проекта.

    Returns:
        Path: Путь к корневой директории, если найдена, иначе директория, где находится скрипт.
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

    Устанавливает основные параметры и настройки проекта.
    Загружает конфигурацию из `config.json` и данные учетных данных
    из файла `credentials.kdbx` в базе данных KeePass.

    Attributes:
        host_name (str): Имя хоста.
        base_dir (Path): Путь к корневой директории проекта.
        config (SimpleNamespace): Объект, содержащий конфигурацию проекта.
        credentials (SimpleNamespace): Объект, содержащий учетные данные.
        MODE (str): Режим работы проекта (например, 'dev', 'prod').
        path (SimpleNamespace): Объект, содержащий пути к различным директориям проекта.
    """

    def __init__(self, **kwargs: Any) -> None:
        """
        Инициализирует экземпляр класса.

        Загружает конфигурацию проекта из `config.json`.
        Инициализирует атрибут `path` с путями к различным директориям проекта.
        Вызывает `check_latest_release` для проверки на наличие новой версии проекта.
        Загружает учетные данные из `credentials.kdbx`.
        """
        self.host_name: str = 'localhost'  # TODO: check host name
        self.base_dir: Path = set_project_root()
        # Загрузка конфигурации из config.json
        config_path = self.base_dir / 'src' / 'config.json' # Вынесено в переменную для удобства
        self.config: SimpleNamespace = j_loads(config_path)  # Используется j_loads
        if not self.config:
            logger.error('Ошибка при загрузке настроек')
            return # Заменили ... на return

        self.config.project_name = self.base_dir.name

        self.path = SimpleNamespace(
            **{
                'logs': self.base_dir / self.config.path.logs,
                'tmp': self.base_dir / self.config.path.tmp,
                'external': self.base_dir / self.config.path.external,
                'gdrive': self.base_dir / self.config.path.gdrive,
                'secrets': self.base_dir / 'secrets',
            }
        )

        self.MODE = self.config.MODE #TODO check mode
        self.credentials: SimpleNamespace = SimpleNamespace()
        self._load_credentials()


    def _load_credentials(self) -> None:
        """Загружает учетные данные из KeePass."""
        kp = self._open_kp()
        if not kp:
            logger.error('Не удалось открыть базу данных KeePass.')
            return

        # Загрузка различных учетных данных
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
        """Открывает базу данных KeePass.

        Args:
            retry (int): Количество попыток.

        Returns:
            PyKeePass | None: Объект PyKeePass или None в случае ошибки.
        """
        while retry > 0:
            try:
                password = getpass.getpass(
                    prompt='Введите мастер-пароль KeePass: '
                ).lower() # Пароль вводится только из консоли.
                kp = PyKeePass(
                    str(self.path.secrets / 'credentials.kdbx'), password=password
                )
                return kp
            except Exception as ex:
                logger.error(f'Не удалось открыть базу данных KeePass. Осталось попыток: {retry-1}.', exc_info=True)
                retry -= 1
                if retry < 1:
                     logger.critical(
                        'Не удалось открыть базу данных KeePass после нескольких попыток',
                        exc_info=True,
                    )
                     sys.exit()
        return None


    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Aliexpress из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
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
        except (IndexError, KeyError) as ex:
           logger.error(f'Ошибка загрузки учетных данных Aliexpress: {ex}', exc_info=True)
           return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные OpenAI из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
        """
        try:
            group = kp.find_groups(name='openai')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.openai = SimpleNamespace(
                api_key=entry.password,
            )
            group = kp.find_groups(name='assistants')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.openai.assistant_id = entry.password
            return True
        except (IndexError, KeyError) as ex:
            logger.error(f'Ошибка загрузки учетных данных OpenAI: {ex}', exc_info=True)
            return False

    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные GoogleAI из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
        """
        try:
            group = kp.find_groups(name='gemini')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.gemini = SimpleNamespace(
                api_key=entry.password,
            )
            return True
        except (IndexError, KeyError) as ex:
            logger.error(f'Ошибка загрузки учетных данных Gemini: {ex}', exc_info=True)
            return False

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Telegram из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
        """
        try:
            group = kp.find_groups(name='telegram')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.telegram = SimpleNamespace(
                token=entry.password,
            )
            return True
        except (IndexError, KeyError) as ex:
            logger.error(f'Ошибка загрузки учетных данных Telegram: {ex}', exc_info=True)
            return False

    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Discord из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
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
        except (IndexError, KeyError) as ex:
            logger.error(f'Ошибка загрузки учетных данных Discord: {ex}', exc_info=True)
            return False

    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные PrestaShop из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
        """
        try:
            group = kp.find_groups(name='prestashop')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.presta = SimpleNamespace(
                 api_key=entry.get_custom_property('api_key'),
                 api_domain=entry.get_custom_property('api_domain'),
                 db_server=entry.get_custom_property('db_server'),
                 db_user=entry.get_custom_property('db_user'),
                 db_password=entry.get_custom_property('db_password'),
            )
            return True
        except (IndexError, KeyError) as ex:
            logger.error(f'Ошибка загрузки учетных данных PrestaShop: {ex}', exc_info=True)
            return False

    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные PrestaShop Translations из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
        """
        try:
            group = kp.find_groups(name='translation')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.presta.translations = SimpleNamespace(
                server=entry.get_custom_property('server'),
                port=entry.get_custom_property('port'),
                database=entry.get_custom_property('database'),
                user=entry.get_custom_property('user'),
                password=entry.get_custom_property('password'),
            )
            return True
        except (IndexError, KeyError) as ex:
            logger.error(f'Ошибка загрузки учетных данных PrestaShop Translations: {ex}', exc_info=True)
            return False

    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные SMTP из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
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
        except (IndexError, KeyError) as ex:
            logger.error(f'Ошибка загрузки учетных данных SMTP: {ex}', exc_info=True)
            return False

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Facebook из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
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
        except (IndexError, KeyError) as ex:
           logger.error(f'Ошибка загрузки учетных данных Facebook: {ex}', exc_info=True)
           return False

    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Google API из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True в случае успешной загрузки, False в противном случае.
        """
        try:
            group = kp.find_groups(name='google')[0]
            entry = group.find_entries(title='gapi')[0]
            self.credentials.gapi = SimpleNamespace(
                api_key=entry.password,
            )
            return True
        except (IndexError, KeyError) as ex:
            logger.error(f'Ошибка загрузки учетных данных Google API: {ex}', exc_info=True)
            return False


    def now(self) -> str:
        """Возвращает текущую метку времени в формате, указанном в файле `config.json`."""
        from datetime import datetime

        return datetime.now().strftime(self.config.datetime_format)


# Global instance of ProgramSettings
gs: ProgramSettings = ProgramSettings()
```