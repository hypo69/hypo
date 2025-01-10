# Анализ кода модуля `credentials`

**Качество кода**
8
-   Плюсы
    -   Код хорошо структурирован, используются классы и методы.
    -   Используется декоратор `@singleton` для реализации паттерна "одиночка".
    -   Есть подробное описание структуры KeePass и загрузки данных из него.
    -   Присутствует обработка исключений.
    -   Используется `j_loads_ns` для загрузки JSON.
-   Минусы
    -   Файл `password.txt` содержит пароль в открытом виде. Это уязвимость.
    -   Много повторяющегося кода в методах `_load_*_credentials`. Можно использовать цикл или функцию.
    -   Не все ошибки логируются с использованием `logger.error`.
    -   Отсутствуют docstring для функций и методов.
    -   Используется `print` для вывода информации об ошибках, необходимо использовать `logger.error`.
    -   Не используются f-строки для форматирования вывода логов.
    -   Не используется `Path` для конкатенации путей.

**Рекомендации по улучшению**

1.  **Безопасность паролей**:
    -   Убрать чтение пароля из файла `password.txt`. Использовать `getpass` в любом режиме.
2.  **Рефакторинг**:
    -   Создать общий метод для загрузки учетных данных из KeePass, параметризовать названия групп.
    -   Использовать f-строки для форматирования строк.
    -   Заменить `print` на `logger.error` для логирования ошибок.
    -   Добавить docstring для всех функций, методов и класса.
    -   Использовать `Path` для конкатенации путей.
3.  **Обработка ошибок**:
    -   Улучшить логирование ошибок, добавить вывод `exc_info` во все логгеры ошибок.
4.  **Импорты**:
    -   Добавить недостающие импорты в начале файла.
    -   Привести импорты в соответствие с ранее обработанными файлами.

**Оптимизированный код**
```python
"""
Модуль для загрузки и хранения учетных данных и настроек программы.
=========================================================================================

Этот модуль содержит класс :class:`ProgramSettings`, который отвечает за загрузку и хранение
конфигурационных данных и учетных данных из файла KeePass.
Также включает в себя функцию :func:`set_project_root`, которая определяет корневую
директорию проекта.

Пример использования
--------------------

Пример использования класса `ProgramSettings`:

.. code-block:: python

    from src.credentials import gs

    print(gs.config.project_name)
    print(gs.credentials.openai.api_key)

"""
import sys
import getpass
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Callable
from pykeepass import PyKeePass
from src.utils.jjson import j_loads_ns
from src.logger import logger


def singleton(cls: type) -> Callable:
    """Декоратор для создания класса-синглтона.

    Args:
        cls (type): Класс, который должен быть преобразован в синглтон.

    Returns:
        Callable: Функция, возвращающая экземпляр класса-синглтона.
    """
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """Находит корневую директорию проекта.

    Ищет вверх по директориям, пока не найдет директорию, содержащую
    один из маркерных файлов.

    Args:
        marker_files (tuple, optional): Кортеж файлов или директорий.
            Defaults to ('__root__', '.git').

    Returns:
        Path: Путь к корневой директории проекта.
    """
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path

    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if str(__root__) not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


@singleton
class ProgramSettings:
    """Класс для хранения настроек программы.

    Загружает конфигурацию из `config.json` и учетные данные из `credentials.kdbx`.

    Attributes:
        host_name (str): Имя хоста.
        base_dir (Path): Корневая директория проекта.
        config (SimpleNamespace): Конфигурация проекта.
        credentials (SimpleNamespace): Учетные данные.
        MODE (str): Режим работы проекта.
        path (SimpleNamespace): Пути к директориям проекта.
    """
    def __init__(self, **kwargs):
        """Инициализирует экземпляр класса ProgramSettings.

        Загружает конфигурацию проекта из `config.json`, инициализирует атрибут `path`
        с путями к различным директориям проекта, вызывает `check_latest_release`
        для проверки наличия новой версии проекта и загружает учетные данные из `credentials.kdbx`.
        """
        self.host_name = 'localhost'
        self.base_dir = set_project_root()
        self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
        if not self.config:
            logger.error('Ошибка при загрузке настроек', exc_info=True)
            ...
            return

        self.config.project_name = self.base_dir.name
        self.path = SimpleNamespace(
            logs=self.base_dir / 'logs',
            tmp=self.base_dir / 'tmp',
            storage=self.base_dir / 'storage',
            secrets=self.base_dir / 'secrets',
            gdrive=self.base_dir / 'gdrive',
        )
        self.MODE = self.config.mode
        self.credentials = SimpleNamespace()
        self._load_credentials()


    def _load_credentials(self) -> None:
        """Загружает учетные данные из KeePass."""
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
        """Открывает базу данных KeePass.

        Args:
            retry (int, optional): Количество попыток. Defaults to 3.

        Returns:
            PyKeePass | None: Объект PyKeePass или None в случае ошибки.
        """
        while retry > 0:
            try:
                # Чтение пароля только через getpass
                password = getpass.getpass(f'Введите мастер-пароль KeePass: ').lower()
                kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), password=password)
                return kp
            except Exception as ex:
                logger.error(f"Не удалось открыть базу данных KeePass. Исключение: {ex}, осталось попыток: {retry-1}.", exc_info=True)
                ...
                retry -= 1
        logger.critical('Не удалось открыть базу данных KeePass после нескольких попыток', exc_info=True)
        ...
        sys.exit()
        return None

    def _load_credentials_from_group(self, kp: PyKeePass, group_path: str, target: SimpleNamespace) -> bool:
        """Загружает учетные данные из группы KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.
            group_path (str): Путь к группе в KeePass.
            target (SimpleNamespace): Объект, куда будут записаны данные.

        Returns:
            bool: True, если данные загружены успешно, False в противном случае.
        """
        try:
            group = kp.find_entries(group=group_path, first=True)
            if group:
                for key, value in group.fields.items():
                    setattr(target, key, value)
                return True
            else:
                logger.error(f'Группа {group_path} не найдена в KeePass', exc_info=True)
                return False
        except Exception as ex:
            logger.error(f'Ошибка при загрузке данных из группы {group_path}: {ex}', exc_info=True)
            return False


    def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
      """Загружает учетные данные Aliexpress из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если данные загружены успешно, False в противном случае.
      """
      return self._load_credentials_from_group(kp, 'suppliers/aliexpress/api', self.credentials.aliexpress)


    def _load_openai_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные OpenAI из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если данные загружены успешно, False в противном случае.
        """
        if self._load_credentials_from_group(kp, 'openai', self.credentials.openai):
          self.credentials.openai.assistants = SimpleNamespace()
          return self._load_credentials_from_group(kp, 'openai/assistants',self.credentials.openai.assistants)
        return False


    def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные GoogleAI из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если данные загружены успешно, False в противном случае.
        """
        return self._load_credentials_from_group(kp, 'gemini', self.credentials.gemini)


    def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Telegram из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если данные загружены успешно, False в противном случае.
        """
        return self._load_credentials_from_group(kp, 'telegram', self.credentials.telegram)


    def _load_discord_credentials(self, kp: PyKeePass) -> bool:
      """Загружает учетные данные Discord из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если данные загружены успешно, False в противном случае.
      """
      return self._load_credentials_from_group(kp, 'discord', self.credentials.discord)

    def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
      """Загружает учетные данные PrestaShop из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если данные загружены успешно, False в противном случае.
      """
      if self._load_credentials_from_group(kp, 'prestashop', self.credentials.presta):
         self.credentials.presta.client = SimpleNamespace()
         return self._load_credentials_from_group(kp, 'prestashop/clients', self.credentials.presta.client)
      return False

    def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
      """Загружает учетные данные PrestaShop Translations из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если данные загружены успешно, False в противном случае.
      """
      return self._load_credentials_from_group(kp, 'prestashop/translation', self.credentials.presta.translations)


    def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные SMTP из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если данные загружены успешно, False в противном случае.
        """
        return self._load_credentials_from_group(kp, 'smtp', self.credentials.smtp)


    def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Facebook из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если данные загружены успешно, False в противном случае.
        """
        return self._load_credentials_from_group(kp, 'facebook', self.credentials.facebook)

    def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
        """Загружает учетные данные Google API из KeePass.

        Args:
            kp (PyKeePass): Объект PyKeePass.

        Returns:
            bool: True, если данные загружены успешно, False в противном случае.
        """
        return self._load_credentials_from_group(kp, 'google/gapi', self.credentials.gapi)

    def now(self) -> str:
        """Возвращает текущую метку времени.

        Returns:
            str: Текущая метка времени в формате, указанном в файле `config.json`.
        """
        from datetime import datetime
        return datetime.now().strftime(self.config.datetime_format)


# Global instance of ProgramSettings
gs: ProgramSettings = ProgramSettings()
```