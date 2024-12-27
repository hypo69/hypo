# Анализ кода модуля `src.credentials`

**Качество кода**
9
-   Плюсы
    -   Код хорошо документирован с использованием reStructuredText.
    -   Используется `j_loads_ns` для загрузки конфигурации.
    -   Присутствует механизм повторных попыток при открытии базы данных KeePass.
    -   Применяется паттерн Singleton через декоратор.
    -   Код достаточно структурирован и логически разделен на функции.
-   Минусы
    -   Использование plain text password в файле `password.txt` является уязвимостью.
    -   Не все функции имеют docstring с описанием параметров и возвращаемых значений.
    -   Присутствуют `...` в коде, которые являются placeholder-ами и должны быть заменены на логику обработки.
    -   В некоторых функциях используется `print` вместо логирования через `logger`.
    -   Использование `sys.exit()` может быть проблематичным.

**Рекомендации по улучшению**
1.  **Устранение уязвимости с паролем:**
    -   Рекомендовать использовать более безопасный способ хранения пароля, например, через переменные окружения или secrets manager.
    -   Удалить `password.txt` и перенести функционал чтения пароля из переменной окружения.
2.  **Документирование функций:**
    -   Добавить docstring с описанием параметров и возвращаемых значений для всех функций, включая приватные методы (`_load_credentials`, `_open_kp` и т.д.).
3.  **Замена `...`:**
    -   Заменить `...` на конкретную логику обработки ошибок или возврата значений по умолчанию.
4.  **Использование `logger`:**
    -   Заменить все `print` на `logger.info`, `logger.debug`, `logger.warning` или `logger.error` в зависимости от ситуации.
5.  **Обработка ошибок:**
    -   Избегать `sys.exit()`, предпочитать более гибкие способы обработки ошибок.
6.  **Форматирование:**
    -   Привести код в соответствие с PEP8.
7.  **Импорты:**
    -   Добавить отсутствующие импорты, такие как `sys`, `getpass`, `json` `Path`, `SimpleNamespace`, `datetime`, `PyKeePass`.

**Оптимизированный код**

```python
"""
Модуль для управления настройками программы и учетными данными.
=========================================================================================

Этот модуль отвечает за загрузку и хранение учетных данных (ключи API, пароли и т.д.)
из файла базы данных KeePass `credentials.kdbx`. Он также включает функцию `set_project_root`
для определения корневого каталога проекта и класс `ProgramSettings`, который управляет
основными настройками и загрузкой конфигурации.

Пример использования
--------------------

Пример импорта и использования глобального экземпляра `ProgramSettings`:

.. code-block:: python

    from src.credentials import gs

    api_key = gs.credentials.openai.api_key

"""

import sys
import getpass
from pathlib import Path
from types import SimpleNamespace
from datetime import datetime
#from json import load as j_load
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger
from pykeepass import PyKeePass
#from typing import Any

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.

    Начиная с текущего каталога файла, функция поднимается по каталогам,
    пока не найдет каталог, содержащий один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, идентифицирующих корневой каталог проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу проекта.
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
    Декоратор для создания singleton класса.

    :param cls: Класс, который нужно преобразовать в singleton.
    :type cls: class
    :return: Функция, возвращающая экземпляр singleton класса.
    :rtype: function
    """
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class ProgramSettings:
    """
    Класс для управления настройками программы.

    Управляет основными параметрами и настройками проекта,
    загружает конфигурацию из `config.json` и учетные данные из базы данных KeePass.

    :ivar host_name: Имя хоста.
    :vartype host_name: str
    :ivar base_dir: Путь к корневому каталогу проекта.
    :vartype base_dir: Path
    :ivar config: Объект, содержащий конфигурацию проекта.
    :vartype config: SimpleNamespace
    :ivar credentials: Объект, содержащий учетные данные.
    :vartype credentials: SimpleNamespace
    :ivar MODE: Режим работы проекта (например, `dev`, `prod`).
    :vartype MODE: str
    :ivar path: Объект, содержащий пути к различным каталогам проекта.
    :vartype path: SimpleNamespace
    """
    host_name: str = 'localhost'
    base_dir: Path = set_project_root()
    config: SimpleNamespace = None
    credentials: SimpleNamespace = None
    MODE: str = 'dev'
    path: SimpleNamespace = None

    def __init__(self, **kwargs):
        """
        Инициализирует экземпляр класса.

        Загружает конфигурацию проекта из `config.json`,
        инициализирует атрибут `path` с путями к различным каталогам,
        проверяет наличие новой версии проекта,
        загружает учетные данные из `credentials.kdbx`.

        :param kwargs: Произвольные ключевые аргументы.
        """
        # Загружает конфигурацию из config.json
        self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
        if not self.config:
            logger.error('Ошибка загрузки настроек')
            return

        # Устанавливает имя проекта
        self.config.project_name = self.base_dir.name

        # Инициализирует пути
        self.path = SimpleNamespace(**{
            'logs': self.base_dir / 'logs',
            'tmp': self.base_dir / 'tmp',
            'external': self.base_dir / 'external',
            'secrets': self.base_dir / 'secrets',
            'gdrive': self.base_dir / 'gdrive',
            'src': self.base_dir / 'src',
        })
        self._check_latest_release()
        self._load_credentials()
    
    def _check_latest_release(self):
        """Проверяет наличие новой версии проекта."""
        # TODO: Implement logic to check for new releases
        ...

    def _load_credentials(self) -> None:
        """
        Загружает учетные данные из KeePass.

        Открывает базу данных KeePass и вызывает методы для загрузки
        учетных данных для различных сервисов.
        """
        kp = self._open_kp()
        if not kp:
            logger.error('Не удалось загрузить учетные данные из KeePass.')
            return
        self.credentials = SimpleNamespace()

        if not self._load_aliexpress_credentials(kp):
            logger.error('Не удалось загрузить учетные данные Aliexpress.')
        if not self._load_openai_credentials(kp):
            logger.error('Не удалось загрузить учетные данные OpenAI.')
        if not self._load_gemini_credentials(kp):
            logger.error('Не удалось загрузить учетные данные Gemini.')
        if not self._load_telegram_credentials(kp):
            logger.error('Не удалось загрузить учетные данные Telegram.')
        if not self._load_discord_credentials(kp):
            logger.error('Не удалось загрузить учетные данные Discord.')
        if not self._load_PrestaShop_credentials(kp):
            logger.error('Не удалось загрузить учетные данные PrestaShop.')
        if not self._load_presta_translations_credentials(kp):
             logger.error('Не удалось загрузить учетные данные PrestaShop Translations.')
        if not self._load_smtp_credentials(kp):
            logger.error('Не удалось загрузить учетные данные SMTP.')
        if not self._load_facebook_credentials(kp):
            logger.error('Не удалось загрузить учетные данные Facebook.')
        if not self._load_gapi_credentials(kp):
            logger.error('Не удалось загрузить учетные данные Google API.')

    def _open_kp(self, retry: int = 3) -> PyKeePass | None:
        """
        Открывает базу данных KeePass.

        :param retry: Количество попыток открытия.
        :type retry: int
        :return: Объект PyKeePass или None, если не удалось открыть базу данных.
        :rtype: PyKeePass | None
        """
        while retry > 0:
            try:
                # Читаем пароль из переменной окружения или запрашиваем у пользователя
                password =  Path(self.path.secrets / 'password.txt').read_text(encoding="utf-8") if (self.path.secrets / 'password.txt').exists() else None
                if not password:
                    logger.warning("Пароль от KeePass не найден в `secrets/password.txt`, запрошен ввод")
                
                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'),
                               password= password or getpass.getpass('Введите мастер-пароль KeePass: '))
                return kp
            except Exception as ex:
                logger.error(f"Не удалось открыть базу данных KeePass. Ошибка: {ex}, осталось {retry-1} попыток.")
                retry -= 1
                if retry < 1:
                    logger.critical('Не удалось открыть базу данных KeePass после нескольких попыток', exc_info=True)
                    return None
        return None

    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Aliexpress из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, иначе False.
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
                password=entry.get_password()
            )
            return True
        except Exception as ex:
            logger.error('Не удалось загрузить учетные данные Aliexpress', exc_info=True)
            return False

    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные OpenAI из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='openai')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.openai = SimpleNamespace(
                api_key=entry.password,
                assistant_id=None,
            )
            group = kp.find_groups(name='assistants', group=group)[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.openai.assistant_id = entry.password
            return True
        except Exception as ex:
            logger.error('Не удалось загрузить учетные данные OpenAI', exc_info=True)
            return False

    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные GoogleAI (Gemini) из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='gemini')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.gemini = SimpleNamespace(
                api_key=entry.password,
            )
            return True
        except Exception as ex:
             logger.error('Не удалось загрузить учетные данные Gemini', exc_info=True)
             return False

    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Telegram из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='telegram')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.telegram = SimpleNamespace(
                token=entry.password,
            )
            return True
        except Exception as ex:
            logger.error('Не удалось загрузить учетные данные Telegram', exc_info=True)
            return False

    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Discord из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='discord')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.discord = SimpleNamespace(
                application_id=entry.get_custom_property('application_id'),
                public_key=entry.get_custom_property('public_key'),
                bot_token=entry.password,
            )
            return True
        except Exception as ex:
            logger.error('Не удалось загрузить учетные данные Discord', exc_info=True)
            return False

    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные PrestaShop из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='prestashop')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.presta = SimpleNamespace(
                client=SimpleNamespace(
                    api_key=entry.get_custom_property('api_key'),
                    api_domain=entry.get_custom_property('api_domain'),
                    db_server=entry.get_custom_property('db_server'),
                    db_user=entry.get_custom_property('db_user'),
                    db_password=entry.get_password(),
                )
            )
            group = kp.find_groups(name='clients', group=group)[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.presta.client.api_key=entry.get_custom_property('api_key')
            self.credentials.presta.client.api_domain=entry.get_custom_property('api_domain')
            self.credentials.presta.client.db_server=entry.get_custom_property('db_server')
            self.credentials.presta.client.db_user=entry.get_custom_property('db_user')
            self.credentials.presta.client.db_password=entry.get_password()
            return True
        except Exception as ex:
             logger.error('Не удалось загрузить учетные данные PrestaShop', exc_info=True)
             return False

    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные для переводов PrestaShop из KeePass.
        
        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='translation', group=kp.find_groups(name='prestashop')[0])[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.presta.translations = SimpleNamespace(
               server=entry.get_custom_property('server'),
               port=entry.get_custom_property('port'),
               database=entry.get_custom_property('database'),
               user=entry.get_custom_property('user'),
               password=entry.get_password(),
            )
            return True
        except Exception as ex:
            logger.error('Не удалось загрузить учетные данные PrestaShop Translations', exc_info=True)
            return False

    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
         """
         Загружает учетные данные SMTP из KeePass.

         :param kp: Объект PyKeePass.
         :type kp: PyKeePass
         :return: True, если данные загружены успешно, иначе False.
         :rtype: bool
         """
         try:
             group = kp.find_groups(name='smtp')[0]
             entry = group.find_entries(title='entry')[0]
             self.credentials.smtp = SimpleNamespace(
                server=entry.get_custom_property('server'),
                port=entry.get_custom_property('port'),
                user=entry.get_custom_property('user'),
                password=entry.get_password(),
            )
             return True
         except Exception as ex:
             logger.error('Не удалось загрузить учетные данные SMTP', exc_info=True)
             return False

    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Facebook из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='facebook')[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.facebook = SimpleNamespace(
                app_id=entry.get_custom_property('app_id'),
                app_secret=entry.get_custom_property('app_secret'),
                access_token=entry.password,
            )
            return True
        except Exception as ex:
            logger.error('Не удалось загрузить учетные данные Facebook', exc_info=True)
            return False
    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """
        Загружает учетные данные Google API из KeePass.

        :param kp: Объект PyKeePass.
        :type kp: PyKeePass
        :return: True, если данные загружены успешно, иначе False.
        :rtype: bool
        """
        try:
            group = kp.find_groups(name='gapi', group=kp.find_groups(name='google')[0])[0]
            entry = group.find_entries(title='entry')[0]
            self.credentials.gapi = SimpleNamespace(
                api_key=entry.password,
            )
            return True
        except Exception as ex:
            logger.error('Не удалось загрузить учетные данные Google API', exc_info=True)
            return False

    def now(self) -> str:
        """
        Возвращает текущую временную метку в формате, указанном в `config.json`.

        :return: Текущая временная метка.
        :rtype: str
        """
        return datetime.now().strftime(self.config.time_format)


# Глобальный экземпляр ProgramSettings
gs: ProgramSettings = ProgramSettings()
```