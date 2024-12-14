# Анализ кода модуля `src.credentials`

**Качество кода**
8
- Плюсы
    - Код хорошо документирован с использованием reStructuredText, что упрощает понимание его структуры и назначения.
    - Применяется декоратор `@singleton` для создания единственного экземпляра класса `ProgramSettings`.
    - Используется `j_loads_ns` для загрузки конфигурации из `config.json`, что обеспечивает удобный доступ к данным через атрибуты.
    - Код обрабатывает исключения при открытии базы данных KeePass и загрузке учетных данных.
    - Структура базы данных KeePass описана подробно, что облегчает понимание хранения учетных данных.
    - Используется `logger.error` для логирования ошибок.
- Минусы
    - Хранение пароля KeePass в файле `password.txt` является потенциальной уязвимостью, хотя и используется только в режиме разработки.
    - В коде есть блоки `try...except...` с `...`, что затрудняет отслеживание ошибок и требует дополнительной проверки.
    - В некоторых методах используется `print` для вывода сообщений об ошибках, что следует заменить на `logger.error` для единообразия логирования.
    - Код не проверяет наличие ключей в базе данных KeePass перед их использованием, что может привести к `AttributeError`.
    - Некоторые импорты не указаны, например `from pathlib import Path`.

**Рекомендации по улучшению**
1. **Безопасность паролей**:
   - Вместо хранения пароля в `password.txt`, следует использовать более безопасный механизм, например, переменные окружения или менеджер секретов.
   - В режиме разработки можно рассмотреть использование `keyring` для хранения паролей.
   - При работе с `getpass.getpass` стоит добавить предупреждение о том что пароль не будет отображаться.

2. **Улучшение обработки ошибок**:
   - Заменить `...` в блоках `try...except...` на конкретную обработку ошибок или логирование.
   - Использовать `logger.error` вместо `print` для вывода сообщений об ошибках, чтобы обеспечить единообразное логирование.
   - Добавить проверки на наличие ключей в базе данных KeePass перед их использованием, чтобы избежать `AttributeError`.

3. **Добавление недостающих импортов**:
   - Добавить `from pathlib import Path`, `from types import SimpleNamespace`, `import sys`, `from src.utils.jjson import j_loads_ns`, `from src.logger.logger import logger`, `import getpass`, `from pykeepass import PyKeePass` и `from typing import Any, Callable` в начало файла.

4. **Улучшение документации**:
    - Уточнить описание декоратора `@singleton`.
   - Добавить примеры использования класса `ProgramSettings` в документацию.

5. **Улучшение стиля кода**:
   - В именовании переменных и функций следует использовать snake_case.
   - Уточнить типы возвращаемых значений в функциях.
   - Ввести проверку на существование файла `password.txt`

**Оптимизированный код**
```python
"""
Модуль для управления настройками программы и учетными данными.
==================================================================

Этот модуль предоставляет класс :class:`ProgramSettings` для загрузки
и хранения конфигурационных данных и учетных данных, используя
базу данных KeePass.

Пример использования
--------------------

.. code-block:: python

    from src.credentials import gs

    # доступ к API ключу OpenAI
    api_key = gs.credentials.openai.api_key
"""
from pathlib import Path
from types import SimpleNamespace
import sys
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger
import getpass
from pykeepass import PyKeePass
from typing import Any, Callable

def singleton(cls: type) -> Callable:
    """
    Декоратор, преобразующий класс в синглтон.

    :param cls: Класс, который должен быть преобразован в синглтон.
    :return: Функция, возвращающая экземпляр класса-синглтона.
    """
    instance = None

    def get_instance(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance

    return get_instance


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с текущей директории файла,
    ища вверх и останавливаясь на первой директории, содержащей любой из маркерных файлов.

    :param marker_files: Имена файлов или директорий для идентификации корневой директории проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если найдена, иначе директория, где находится скрипт.
    :rtype: Path
    """
    current_path: Path = Path(__file__).resolve().parent
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
    Класс настроек программы. Устанавливает основные параметры и настройки проекта.
    Загружает конфигурацию из ``config.json`` и данные учетных данных из файла
    ``credentials.kdbx`` в базе данных KeePass.

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

        :param kwargs: Произвольные ключевые аргументы.
        :type kwargs: dict
        """
        self.host_name: str = 'localhost' #TODO: получать имя хоста
        self.base_dir: Path = set_project_root()
        self.config: SimpleNamespace = SimpleNamespace()
        self.credentials: SimpleNamespace = SimpleNamespace()
        self.MODE: str = 'dev' #TODO: сделать выбор из config.json
        self.path: SimpleNamespace = SimpleNamespace()
        
        # загрузка конфигурации из config.json
        self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
        if not self.config:
            logger.error('Ошибка при загрузке настроек')
            ...
            return

        self.config.project_name = self.base_dir.name

        self.path.log = self.base_dir / self.config.path.log
        self.path.tmp = self.base_dir / self.config.path.tmp
        self.path.external = self.base_dir / self.config.path.external
        self.path.gdrive = self.base_dir / self.config.path.gdrive
        self.path.secrets = self.base_dir / 'secrets'

        self._load_credentials()

    def _load_credentials(self) -> None:
        """
        Загружает учетные данные из KeePass.
        """
        kp = self._open_kp()
        if not kp:
            logger.error('Не удалось открыть базу данных KeePass')
            ...
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

        :param retry: Количество попыток.
        :type retry: int
        :return: Объект PyKeePass или None в случае неудачи.
        :rtype: PyKeePass | None
        """
        while retry > 0:
            try:
                password = None
                password_file = Path(self.path.secrets / 'password.txt')
                if password_file.exists():
                    password = password_file.read_text(encoding="utf-8").strip()
                else:
                    print('Файл password.txt не найден, пароль не будет отображаться.')
                    password = getpass.getpass('Введите мастер-пароль KeePass: ').lower()
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
        :type kp: PyKeePass
        :return: True если данные загружены, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='aliexpress')[0]
            entry = group.find_entries(title='api')[0]
            self.credentials.aliexpress.api_key = entry.get_custom_property('api_key')
            self.credentials.aliexpress.secret = entry.get_custom_property('secret')
            self.credentials.aliexpress.tracking_id = entry.get_custom_property('tracking_id')
            self.credentials.aliexpress.email = entry.get_custom_property('email')
            self.credentials.aliexpress.password = entry.get_password()
            return True
        except Exception as ex:
            logger.error(f'Не удалось загрузить учетные данные Aliexpress. {ex}', exc_info=True)
            return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные OpenAI из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если данные загружены, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='openai')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.openai.api_key = entry.get_password()

            group = kp.find_groups(name='assistants')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.openai.assistant_id = entry.get_password()
            return True
        except Exception as ex:
            logger.error(f'Не удалось загрузить учетные данные OpenAI. {ex}', exc_info=True)
            return False

    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные GoogleAI из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если данные загружены, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='gemini')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.gemini.api_key = entry.get_password()
            return True
        except Exception as ex:
            logger.error(f'Не удалось загрузить учетные данные Gemini. {ex}', exc_info=True)
            return False

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Telegram из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если данные загружены, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='telegram')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.telegram.token = entry.get_password()
            return True
        except Exception as ex:
            logger.error(f'Не удалось загрузить учетные данные Telegram. {ex}', exc_info=True)
            return False

    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Discord из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если данные загружены, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='discord')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.discord.application_id = entry.get_custom_property('application_id')
            self.credentials.discord.public_key = entry.get_custom_property('public_key')
            self.credentials.discord.bot_token = entry.get_password()
            return True
        except Exception as ex:
            logger.error(f'Не удалось загрузить учетные данные Discord. {ex}', exc_info=True)
            return False

    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если данные загружены, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='prestashop')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.presta.api_key = entry.get_custom_property('api_key')
            self.credentials.presta.api_domain = entry.get_custom_property('api_domain')
            self.credentials.presta.db_server = entry.get_custom_property('db_server')
            self.credentials.presta.db_user = entry.get_custom_property('db_user')
            self.credentials.presta.db_password = entry.get_password()
            return True
        except Exception as ex:
            logger.error(f'Не удалось загрузить учетные данные PrestaShop. {ex}', exc_info=True)
            return False

    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop Translations из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если данные загружены, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='translation')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.presta.translations.server = entry.get_custom_property('server')
            self.credentials.presta.translations.port = entry.get_custom_property('port')
            self.credentials.presta.translations.database = entry.get_custom_property('database')
            self.credentials.presta.translations.user = entry.get_custom_property('user')
            self.credentials.presta.translations.password = entry.get_password()
            return True
        except Exception as ex:
            logger.error(f'Не удалось загрузить учетные данные PrestaShop Translations. {ex}', exc_info=True)
            return False

    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные SMTP из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если данные загружены, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='smtp')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.smtp.server = entry.get_custom_property('server')
            self.credentials.smtp.port = entry.get_custom_property('port')
            self.credentials.smtp.user = entry.get_custom_property('user')
            self.credentials.smtp.password = entry.get_password()
            return True
        except Exception as ex:
            logger.error(f'Не удалось загрузить учетные данные SMTP. {ex}', exc_info=True)
            return False

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Facebook из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если данные загружены, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='facebook')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.facebook.app_id = entry.get_custom_property('app_id')
            self.credentials.facebook.app_secret = entry.get_custom_property('app_secret')
            self.credentials.facebook.access_token = entry.get_password()
            return True
        except Exception as ex:
            logger.error(f'Не удалось загрузить учетные данные Facebook. {ex}', exc_info=True)
            return False

    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Google API из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True если данные загружены, False в противном случае.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='google')[0]
            group = group.find_groups(name='gapi')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.gapi.api_key = entry.get_password()
            return True
        except Exception as ex:
            logger.error(f'Не удалось загрузить учетные данные Google API. {ex}', exc_info=True)
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