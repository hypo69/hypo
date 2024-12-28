# Анализ кода модуля `src.webdriver.bs`

**Качество кода**

-  Соответствие требованиям по оформлению кода: 6/10
    - Плюсы:
        - Документация в формате reStructuredText (RST) для модуля.
        - Подробное описание конфигурационного файла и его полей.
        - Примеры использования парсера `BS`.
        - Описание логирования и отладки.
        - Наличие раздела о лицензии.
    - Минусы:
        - Не указаны импорты необходимые для корректной работы модуля, в частности `from src.logger.logger import logger`.
        - Отсутствует документация в формате RST для классов, функций и методов,
        - Не используется `j_loads_ns` для загрузки конфигурационного файла.
        - Не используется логгер для обработки ошибок.
        - Присутствуют не используемые переменные и импорты.

**Рекомендации по улучшению**

1.  **Импорты**: Добавить необходимые импорты, такие как `from src.utils.jjson import j_loads_ns` и `from src.logger.logger import logger`.
2.  **Документация**: Добавить документацию в формате RST для классов, функций и методов.
3.  **Обработка ошибок**: Использовать `logger.error` для обработки ошибок вместо `try-except` блоков.
4.  **Загрузка конфигурации**: Использовать `j_loads_ns` для загрузки конфигурационного файла.
5.  **Логирование**: Добавить логирование в методах для отладки и отслеживания ошибок.
6. **Удалить лишние импорты**.
7. **Переписать комментарии в формате RST**

**Оптимизированный код**

```markdown
.. module:: src.webdriver.bs

=========================================================================================

Модуль для парсинга HTML с использованием BeautifulSoup и XPath
--------------------------------------------------------------

Этот модуль предоставляет кастомную реализацию для парсинга HTML-контента с использованием BeautifulSoup и XPath.
Он позволяет загружать HTML-контент из файлов или URL-адресов, парсить его и извлекать элементы с помощью XPath-локаторов.

Ключевые особенности
--------------------

- **Парсинг HTML**: Использует BeautifulSoup и XPath для эффективного парсинга HTML.
- **Поддержка файлов и URL**: Загружает HTML-контент из локальных файлов или веб-адресов.
- **Пользовательские локаторы**: Позволяет определять пользовательские XPath-локаторы для извлечения элементов.
- **Логирование и обработка ошибок**: Предоставляет подробные логи для отладки и отслеживания ошибок.
- **Поддержка конфигурации**: Централизованная конфигурация через файл `bs.json`.

Требования
----------

Перед использованием этого модуля убедитесь, что установлены следующие зависимости:

- Python 3.x
- BeautifulSoup
- lxml
- requests

Установите необходимые зависимости Python::

    pip install beautifulsoup4 lxml requests

Конфигурация
-------------

Конфигурация для парсера `BS` хранится в файле `bs.json`. Ниже приведён пример структуры конфигурационного файла и его описание:

Пример конфигурации (`bs.json`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

    {
      "default_url": "https://example.com",
      "default_file_path": "file://path/to/your/file.html",
      "default_locator": {
        "by": "ID",
        "attribute": "element_id",
        "selector": "//*[@id='element_id']"
      },
      "logging": {
        "level": "INFO",
        "file": "logs/bs.log"
      },
      "proxy": {
        "enabled": false,
        "server": "http://proxy.example.com:8080",
        "username": "user",
        "password": "password"
      },
      "timeout": 10,
      "encoding": "utf-8"
    }

Описание полей конфигурации
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. `default_url`
   URL по умолчанию для загрузки HTML-контента.

2. `default_file_path`
   Путь к файлу по умолчанию для загрузки HTML-контента.

3. `default_locator`
   Локатор по умолчанию для извлечения элементов:

    - **by**: Тип локатора (например, `ID`, `CSS`, `TEXT`).
    - **attribute**: Атрибут для поиска (например, `element_id`).
    - **selector**: XPath-селектор для извлечения элементов.

4. `logging`
   Настройки логирования:

    - **level**: Уровень логирования (например, `INFO`, `DEBUG`, `ERROR`).
    - **file**: Путь к файлу, куда будут записываться логи.

5. `proxy`
   Настройки прокси-сервера:

    - **enabled**: Булевое значение, указывающее, следует ли использовать прокси.
    - **server**: Адрес прокси-сервера.
    - **username**: Имя пользователя для аутентификации на прокси-сервере.
    - **password**: Пароль для аутентификации на прокси-сервере.

6. `timeout`
   Максимальное время ожидания для запросов (в секундах).

7. `encoding`
   Кодировка, используемая при чтении файлов или запросах.

Использование
-------------

Чтобы использовать парсер `BS` в своём проекте, просто импортируйте его и инициализируйте:

.. code-block:: python

    from src.webdriver.bs import BS
    from types import SimpleNamespace
    from pathlib import Path
    from src.utils.jjson import j_loads_ns
    from src.logger.logger import logger

    # Загрузка настроек из конфигурационного файла
    settings_path = Path('path/to/bs.json')
    settings = j_loads_ns(settings_path)

    # Инициализация парсера BS с URL по умолчанию
    parser = BS(url=settings.default_url)

    # Использование локатора по умолчанию из конфигурации
    locator = SimpleNamespace(**settings.default_locator)
    elements = parser.execute_locator(locator)
    print(elements)

Пример: Загрузка HTML из файла
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    parser = BS()
    parser.get_url('file://path/to/your/file.html')
    locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
    elements = parser.execute_locator(locator)
    print(elements)

Пример: Загрузка HTML из URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    parser = BS()
    parser.get_url('https://example.com')
    locator = SimpleNamespace(by='CSS', attribute='class_name', selector='//*[contains(@class, "class_name")]')
    elements = parser.execute_locator(locator)
    print(elements)

Логирование и отладка
---------------------

Парсер `BS` использует `logger` из `src.logger` для логирования ошибок, предупреждений и общей информации.
Все проблемы, возникающие при инициализации, конфигурации или выполнении, будут записываться в логи для удобства отладки.

Примеры логов
~~~~~~~~~~~~~

- **Ошибка при инициализации**: `Ошибка при инициализации парсера BS: <детали ошибки>`
- **Проблемы с конфигурацией**: `Ошибка в файле bs.json: <детали проблемы>`

Лицензия
--------

Этот проект лицензирован на условиях MIT License. Подробности см. в файле [LICENSE](../../LICENSE).
```

```python
# .. module:: src.webdriver.bs
#
# =========================================================================================
#
# Модуль для парсинга HTML с использованием BeautifulSoup и XPath
# --------------------------------------------------------------
#
# Этот модуль предоставляет кастомную реализацию для парсинга HTML-контента с использованием BeautifulSoup и XPath.
# Он позволяет загружать HTML-контент из файлов или URL-адресов, парсить его и извлекать элементы с помощью XPath-локаторов.
#
# Ключевые особенности
# --------------------
#
# - **Парсинг HTML**: Использует BeautifulSoup и XPath для эффективного парсинга HTML.
# - **Поддержка файлов и URL**: Загружает HTML-контент из локальных файлов или веб-адресов.
# - **Пользовательские локаторы**: Позволяет определять пользовательские XPath-локаторы для извлечения элементов.
# - **Логирование и обработка ошибок**: Предоставляет подробные логи для отладки и отслеживания ошибок.
# - **Поддержка конфигурации**: Централизованная конфигурация через файл `bs.json`.
#
# Требования
# ----------
#
# Перед использованием этого модуля убедитесь, что установлены следующие зависимости:
#
# - Python 3.x
# - BeautifulSoup
# - lxml
# - requests
#
# Установите необходимые зависимости Python::
#
#     pip install beautifulsoup4 lxml requests
#
# Конфигурация
# -------------
#
# Конфигурация для парсера `BS` хранится в файле `bs.json`. Ниже приведён пример структуры конфигурационного файла и его описание:
#
# Пример конфигурации (`bs.json`)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# .. code-block:: json
#
#     {
#       "default_url": "https://example.com",
#       "default_file_path": "file://path/to/your/file.html",
#       "default_locator": {
#         "by": "ID",
#         "attribute": "element_id",
#         "selector": "//*[@id='element_id']"
#       },
#       "logging": {
#         "level": "INFO",
#         "file": "logs/bs.log"
#       },
#       "proxy": {
#         "enabled": false,
#         "server": "http://proxy.example.com:8080",
#         "username": "user",
#         "password": "password"
#       },
#       "timeout": 10,
#       "encoding": "utf-8"
#     }
#
# Описание полей конфигурации
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# 1. `default_url`
#    URL по умолчанию для загрузки HTML-контента.
#
# 2. `default_file_path`
#    Путь к файлу по умолчанию для загрузки HTML-контента.
#
# 3. `default_locator`
#    Локатор по умолчанию для извлечения элементов:
#
#     - **by**: Тип локатора (например, `ID`, `CSS`, `TEXT`).
#     - **attribute**: Атрибут для поиска (например, `element_id`).
#     - **selector**: XPath-селектор для извлечения элементов.
#
# 4. `logging`
#    Настройки логирования:
#
#     - **level**: Уровень логирования (например, `INFO`, `DEBUG`, `ERROR`).
#     - **file**: Путь к файлу, куда будут записываться логи.
#
# 5. `proxy`
#    Настройки прокси-сервера:
#
#     - **enabled**: Булевое значение, указывающее, следует ли использовать прокси.
#     - **server**: Адрес прокси-сервера.
#     - **username**: Имя пользователя для аутентификации на прокси-сервере.
#     - **password**: Пароль для аутентификации на прокси-сервере.
#
# 6. `timeout`
#    Максимальное время ожидания для запросов (в секундах).
#
# 7. `encoding`
#    Кодировка, используемая при чтении файлов или запросах.
#
# Использование
# -------------
#
# Чтобы использовать парсер `BS` в своём проекте, просто импортируйте его и инициализируйте:
#
# .. code-block:: python
#
#     from src.webdriver.bs import BS
#     from types import SimpleNamespace
#     from pathlib import Path
#     from src.utils.jjson import j_loads_ns
#     from src.logger.logger import logger
#
#     # Загрузка настроек из конфигурационного файла
#     settings_path = Path('path/to/bs.json')
#     settings = j_loads_ns(settings_path)
#
#     # Инициализация парсера BS с URL по умолчанию
#     parser = BS(url=settings.default_url)
#
#     # Использование локатора по умолчанию из конфигурации
#     locator = SimpleNamespace(**settings.default_locator)
#     elements = parser.execute_locator(locator)
#     print(elements)
#
# Пример: Загрузка HTML из файла
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# .. code-block:: python
#
#     parser = BS()
#     parser.get_url('file://path/to/your/file.html')
#     locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
#     elements = parser.execute_locator(locator)
#     print(elements)
#
# Пример: Загрузка HTML из URL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# .. code-block:: python
#
#     parser = BS()
#     parser.get_url('https://example.com')
#     locator = SimpleNamespace(by='CSS', attribute='class_name', selector='//*[contains(@class, "class_name")]')
#     elements = parser.execute_locator(locator)
#     print(elements)
#
# Логирование и отладка
# ---------------------
#
# Парсер `BS` использует `logger` из `src.logger` для логирования ошибок, предупреждений и общей информации.
# Все проблемы, возникающие при инициализации, конфигурации или выполнении, будут записываться в логи для удобства отладки.
#
# Примеры логов
# ~~~~~~~~~~~~~
#
# - **Ошибка при инициализации**: `Ошибка при инициализации парсера BS: <детали ошибки>`
# - **Проблемы с конфигурацией**: `Ошибка в файле bs.json: <детали проблемы>`
#
# Лицензия
# --------
#
# Этот проект лицензирован на условиях MIT License. Подробности см. в файле [LICENSE](../../LICENSE).
from bs4 import BeautifulSoup
import requests
from lxml import etree
from typing import Any, Optional
from src.utils.jjson import j_loads_ns
from pathlib import Path
from src.logger.logger import logger
from types import SimpleNamespace


class BS:
    """
    Класс для парсинга HTML с использованием BeautifulSoup и XPath.

    :param url: URL для загрузки HTML контента.
    :param file_path: Путь к файлу для загрузки HTML контента.
    :param settings_path: Путь к файлу конфигурации.
    """

    def __init__(self, url: Optional[str] = None, file_path: Optional[str] = None, settings_path: str = 'bs.json') -> None:
        """
        Инициализирует класс BS.
        Загружает конфигурацию, устанавливает URL или путь к файлу.
        """
        # Загрузка настроек из конфигурационного файла
        self.settings = self._load_settings(settings_path)

        self.url = url or self.settings.default_url
        self.file_path = file_path or self.settings.default_file_path
        self.html = None
        self.soup = None
        self.tree = None
        self.session = requests.Session()
        # Инициализация прокси, если он включен в настройках
        if self.settings.proxy.enabled:
             self._init_proxy()

    def _load_settings(self, settings_path: str) -> SimpleNamespace:
        """
        Загружает настройки из JSON файла.

        :param settings_path: Путь к файлу конфигурации.
        :return: Объект SimpleNamespace с настройками.
        """
        try:
            #  код исполняет загрузку настроек из файла
            settings = j_loads_ns(Path(settings_path))
        except Exception as ex:
            #  код исполняет логгирование ошибки загрузки
            logger.error(f'Ошибка при загрузке файла конфигурации: {settings_path}', ex)
            return SimpleNamespace()
        return settings

    def _init_proxy(self) -> None:
        """Инициализирует прокси-сервер для запросов."""
        try:
            #  код исполняет настройку прокси
            self.session.proxies.update({
                'http': self.settings.proxy.server,
                'https': self.settings.proxy.server
            })
            # код исполняет проверку на наличие username
            if self.settings.proxy.username:
                self.session.auth = (self.settings.proxy.username, self.settings.proxy.password)
        except Exception as ex:
            # код исполняет логирование ошибки настройки прокси
            logger.error('Ошибка при инициализации прокси', ex)
    def get_url(self, url: Optional[str] = None) -> Optional[str]:
        """
        Загружает HTML контент из URL или файла.

        :param url: URL для загрузки HTML контента.
        :return: HTML контент.
        """
        url = url or self.url
        try:
            #  код исполняет проверку url на то, является ли он файлом
            if url.startswith('file://'):
                #  код исполняет открытие и чтение файла
                file_path = url[7:]
                with open(file_path, 'r', encoding=self.settings.encoding) as f:
                   self.html = f.read()
            else:
                #  код исполняет отправку GET запроса
                response = self.session.get(url, timeout=self.settings.timeout)
                response.raise_for_status()
                self.html = response.text
            #  код исполняет парсинг html и создание дерева
            self.soup = BeautifulSoup(self.html, 'html.parser')
            self.tree = etree.HTML(self.html)
            return self.html
        except Exception as ex:
            # код исполняет логирование ошибки загрузки HTML
            logger.error(f'Ошибка при загрузке HTML контента с {url}', ex)
            return None

    def execute_locator(self, locator: SimpleNamespace) -> Optional[Any]:
        """
        Выполняет поиск элементов по XPath.

        :param locator: Объект SimpleNamespace с параметрами локатора.
        :return: Список найденных элементов или None.
        """
        try:
             # код исполняет проверку наличия дерева
            if self.tree is None:
                logger.error('HTML дерево не было инициализировано')
                return None
            # код исполняет поиск элементов по XPath
            elements = self.tree.xpath(locator.selector)
            # код исполняет обработку результата
            if not elements:
                logger.debug(f'Элементы не найдены по локатору: {locator.selector}')
                return None

            return elements
        except Exception as ex:
            # код исполняет логирование ошибки поиска элементов
            logger.error(f'Ошибка при выполнении локатора: {locator.selector}', ex)
            return None
```