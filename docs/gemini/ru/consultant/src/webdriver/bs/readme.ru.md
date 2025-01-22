## Анализ кода модуля `bs`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Хорошее объяснение функциональности модуля.
    - Наличие примеров использования.
    - Описание конфигурации с примерами.
- **Минусы**:
    - Отсутствует детальное описание RST для модуля и его функций.
    - В примерах кода используются двойные кавычки для строк, что не соответствует стандарту.
    - Не используется `j_loads` из `src.utils.jjson`.
    - Примеры кода не соответствуют стандарту в части кавычек.
    - Нет подробных RST описаний методов и классов.

**Рекомендации по улучшению**:
- Добавить RST-заголовки в начало документа, чтобы улучшить его структурирование и помочь в автоматической генерации документации.
- Использовать одинарные кавычки в примерах кода Python, кроме случаев вывода в консоль.
- Добавить RST-документацию для каждой функции и класса, включая подробное описание параметров, возвращаемых значений и возможных исключений.
- Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки конфигурации.
- Указать пути к файлам в примерах кода, используя `pathlib.Path`.
- Расширить раздел "Логирование и отладка", описав формат логов и их важность для отладки.
- Привести примеры кода, используя асинхронный подход.
- Уточнить лицензию, указав ссылку на файл в репозитории.
- Уточнить, что модуль `BS` является классом, а не просто парсером.
- Следовать стандарту PEP8 при форматировании кода.
- Переписать примеры кодов с использованием `logger` для логирования ошибок.
- Заменить неясные формулировки, такие как "получаем", на более точные, например "выполняем".

**Оптимизированный код**:

```rst
.. module:: src.webdriver.bs

=================================================
Модуль для парсинга HTML с использованием BeautifulSoup и XPath
=================================================

:mod:`src.webdriver.bs` предоставляет класс :class:`BS` для парсинга HTML-контента с использованием `BeautifulSoup` и `XPath`.
Он позволяет загружать HTML из файлов или URL-адресов, парсить его и извлекать элементы, используя XPath-локаторы.

Ключевые особенности
--------------------

- **Парсинг HTML**: Использует `BeautifulSoup` и `XPath` для эффективного парсинга HTML.
- **Поддержка файлов и URL**: Загружает HTML-контент из локальных файлов или веб-адресов.
- **Пользовательские локаторы**: Позволяет определять пользовательские `XPath`-локаторы для извлечения элементов.
- **Логирование и обработка ошибок**: Предоставляет подробные логи для отладки и отслеживания ошибок.
- **Поддержка конфигурации**: Централизованная конфигурация через файл `bs.json`.

Требования
----------

Перед использованием этого модуля убедитесь, что установлены следующие зависимости:

- Python 3.x
- BeautifulSoup4
- lxml
- requests

Установите необходимые зависимости Python:

.. code-block:: bash

   pip install beautifulsoup4 lxml requests

Конфигурация
-------------

Конфигурация для парсера `BS` хранится в файле `bs.json`. Ниже приведён пример структуры конфигурационного файла и его описание:

Пример конфигурации (`bs.json`)
------------------------------

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
---------------------------

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
------------

Чтобы использовать класс :class:`BS` в своём проекте, просто импортируйте его и инициализируйте:

.. code-block:: python

    from src.webdriver.bs import BS
    from types import SimpleNamespace
    from src.utils.jjson import j_loads_ns #  Используем j_loads_ns для загрузки конфигурации
    from pathlib import Path
    from src.logger import logger # Импортируем logger из src.logger

    # Загрузка настроек из конфигурационного файла
    settings_path = Path('path/to/bs.json') # Используем pathlib.Path для работы с путями
    try:
        settings = j_loads_ns(settings_path)
    except Exception as e:
        logger.error(f"Ошибка при загрузке конфигурации: {e}")
        settings = None

    if settings:
        # Инициализация парсера BS с URL по умолчанию
        parser = BS(url=settings.default_url)

        # Использование локатора по умолчанию из конфигурации
        locator = SimpleNamespace(**settings.default_locator)
        elements = parser.execute_locator(locator)
        print(elements)
    else:
      logger.error(f"Конфигурация не загружена. Проверьте файл: {settings_path}")

Пример: Загрузка HTML из файла
-----------------------------

.. code-block:: python

    from src.webdriver.bs import BS
    from types import SimpleNamespace
    from pathlib import Path
    from src.logger import logger

    parser = BS()
    try:
        file_path = Path('path/to/your/file.html')
        parser.get_url(f'file://{file_path}') # Используем f-строку для формирования пути
        locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id=\'element_id\']')
        elements = parser.execute_locator(locator)
        print(elements)
    except Exception as e:
      logger.error(f"Ошибка при загрузке файла или выполнении локатора: {e}")


Пример: Загрузка HTML из URL
---------------------------

.. code-block:: python

    from src.webdriver.bs import BS
    from types import SimpleNamespace
    from src.logger import logger

    parser = BS()
    try:
        parser.get_url('https://example.com')
        locator = SimpleNamespace(by='CSS', attribute='class_name', selector='//*[contains(@class, \'class_name\')]')
        elements = parser.execute_locator(locator)
        print(elements)
    except Exception as e:
        logger.error(f"Ошибка при загрузке URL или выполнении локатора: {e}")


Логирование и отладка
----------------------

Класс :class:`BS` использует `logger` из `src.logger` для логирования ошибок, предупреждений и общей информации.
Все проблемы, возникающие при инициализации, конфигурации или выполнении, будут записываться в логи для удобства отладки.

**Примеры логов**

- **Ошибка при инициализации**: `Ошибка при инициализации парсера BS: <детали ошибки>`
- **Проблемы с конфигурацией**: `Ошибка в файле bs.json: <детали проблемы>`
- **Ошибка при загрузке URL или файла**: `Ошибка при загрузке URL или файла: <детали ошибки>`
- **Ошибка при выполнении локатора**: `Ошибка при выполнении локатора: <детали ошибки>`

Лицензия
--------

Этот проект лицензирован на условиях MIT License. Подробности см. в файле `LICENSE` в корне репозитория.
(../../LICENSE)
```
```python
"""
Модуль для работы с парсером BeautifulSoup и XPath
=================================================

Модуль предоставляет класс :class:`BS`, который используется для парсинга HTML-контента с использованием BeautifulSoup и XPath.
Он позволяет загружать HTML-контент из файлов или URL-адресов, парсить его и извлекать элементы с помощью XPath-локаторов.

Пример использования
----------------------
.. code-block:: python

    from src.webdriver.bs import BS
    from types import SimpleNamespace
    from src.utils.jjson import j_loads_ns
    from pathlib import Path

    # Загрузка настроек из конфигурационного файла
    settings_path = Path('path/to/bs.json')
    settings = j_loads_ns(settings_path)

    # Инициализация парсера BS с URL по умолчанию
    parser = BS(url=settings.default_url)

    # Использование локатора по умолчанию из конфигурации
    locator = SimpleNamespace(**settings.default_locator)
    elements = parser.execute_locator(locator)
    print(elements)
"""
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from lxml import etree
from src.utils.jjson import j_loads_ns  #  Используем j_loads_ns для загрузки конфигурации
from src.logger import logger  #  Импортируем logger из src.logger


class BS:
    """
    Класс для парсинга HTML с использованием BeautifulSoup и XPath.

    :param url: URL-адрес для загрузки HTML-контента.
    :type url: str, optional
    :param file_path: Путь к файлу для загрузки HTML-контента.
    :type file_path: str, optional
    :raises Exception: Если не указан URL или file_path.

    Пример использования:
        >>> from src.webdriver.bs import BS
        >>> parser = BS(url='https://example.com')
        >>> parser = BS(file_path='file://path/to/your/file.html')
    """

    def __init__(self, url: Optional[str] = None, file_path: Optional[str] = None) -> None:
        """Инициализация BS с URL или путем к файлу."""
        self.html: Optional[str] = None  # Типизация self.html
        if url:
            self.get_url(url)
        elif file_path:
            self.get_url(file_path)
        else:
            logger.error("Необходимо указать url или file_path.")
            raise Exception("Необходимо указать url или file_path.")

    def get_url(self, url: str) -> None:
        """
        Получает HTML-контент из URL или файла.

        :param url: URL-адрес или путь к файлу.
        :type url: str
        :raises Exception: В случае ошибки загрузки контента.

        Пример:
            >>> parser = BS()
            >>> parser.get_url('https://example.com')
        """
        try:
            if url.startswith('file://'):  # Проверяем, является ли url файлом
                file_path = url[7:]
                with open(file_path, 'r', encoding='utf-8') as file:
                    self.html = file.read()
            else:
                response = requests.get(url)
                response.raise_for_status()
                self.html = response.text
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при загрузке URL: {url}. Ошибка: {e}")
            raise Exception(f"Ошибка при загрузке URL: {url}. Ошибка: {e}")
        except FileNotFoundError as e:
            logger.error(f"Файл не найден: {url}. Ошибка: {e}")
            raise Exception(f"Файл не найден: {url}. Ошибка: {e}")
        except Exception as e:
            logger.error(f"Ошибка при получении контента: {url}. Ошибка: {e}")
            raise Exception(f"Ошибка при получении контента: {url}. Ошибка: {e}")


    def execute_locator(self, locator: Any) -> List[str]:
        """
        Выполняет XPath-локатор и возвращает список найденных элементов.

        :param locator: Объект с атрибутами 'by', 'attribute' и 'selector'.
        :type locator: Any
        :return: Список найденных элементов.
        :rtype: List[str]
        :raises Exception: В случае ошибки при выполнении локатора.

        Пример:
            >>> parser = BS(url='https://example.com')
            >>> locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
            >>> elements = parser.execute_locator(locator)
            >>> print(elements)
        """
        if not self.html:
            logger.error("HTML контент не загружен.")
            raise Exception("HTML контент не загружен.")
        try:
            soup = BeautifulSoup(self.html, 'lxml')
            if locator.by == 'ID':  # проверяем тип локатора
                element = soup.find(id=locator.attribute)  # Ищем по id
                if element:
                     return [str(element)]
                else:
                    logger.warning(f"Элемент с id '{locator.attribute}' не найден.")
                    return []
            if locator.by == 'CSS':
                elements = soup.select(locator.selector) # ищем по css
                return [str(el) for el in elements]
            
            tree = etree.HTML(str(soup))
            elements = tree.xpath(locator.selector)
            return [str(el) for el in elements] #  Приводим к строке
        except Exception as e:
            logger.error(f"Ошибка при выполнении локатора: {locator}. Ошибка: {e}")
            raise Exception(f"Ошибка при выполнении локатора: {locator}. Ошибка: {e}")