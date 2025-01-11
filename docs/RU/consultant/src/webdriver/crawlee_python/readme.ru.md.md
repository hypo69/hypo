# Анализ кода модуля src.webdriver.crawlee_python

**Качество кода**
8
- Плюсы
    - Документ предоставляет подробное описание модуля, его ключевых особенностей, конфигурационных параметров и инструкции по использованию.
    - Примеры кода и конфигурации помогают пользователю быстро начать работу с модулем.
    - Документ описывает процесс логирования и отладки.
    - Описание каждого поля конфигурационного файла даёт понимание, как и зачем его использовать.
- Минусы
    -  Документация не соответствует стандарту reStructuredText (RST).
    -  Отсутствуют docstring для классов и методов.
    -  Не используются принятые соглашения по стилю кода, такие как одинарные кавычки в строках.
    -  Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Не хватает  комментариев в формате RST к функциям, методам и классам, что затрудняет автоматическую генерацию документации.

**Рекомендации по улучшению**
1.  Переписать документацию в формате reStructuredText (RST), включая все комментарии к модулям, функциям, методам и переменным.
2.  Добавить docstring для класса `CrawleePython` и его методов, включая параметры, возвращаемые значения и исключения.
3.  Использовать одинарные кавычки (`'`) в Python коде.
4.  Заменить стандартный `json.load` на `j_loads` или `j_loads_ns` для чтения конфигурационного файла.
5.  Добавить импорты `os` и `json` для работы с файлами.
6.  Избегать избыточных блоков `try-except`, предпочитая обработку ошибок с помощью `logger.error`.
7.  Добавить больше примеров конфигурации и использования, особенно для прокси.
8.  Предоставить более подробную информацию об обработке ошибок и возможных проблемах при запуске.

**Оптимизированный код**

```markdown
.. module:: src.webdriver.crawlee_python
   :synopsis: Модуль Crawlee Python для автоматизации и сбора данных.

=========================================================================================

Модуль Crawlee Python для автоматизации и сбора данных
=========================================================================================

Этот модуль предоставляет кастомную реализацию :class:`CrawleePython` с использованием библиотеки Crawlee.
Он позволяет настраивать параметры запуска браузера, обрабатывать веб-страницы и извлекать данные из них.
Конфигурация управляется через файл `crawlee_python.json`.

Ключевые особенности
---------------------

- **Централизованная конфигурация**: Конфигурация управляется через файл `crawlee_python.json`.
- **Поддержка пользовательских опций**: Возможность передавать пользовательские опции при инициализации.
- **Улучшенное логирование и обработка ошибок**: Предоставляет подробные логи для инициализации, проблем с конфигурацией и ошибок WebDriver.
- **Поддержка прокси**: Настройка прокси-сервера для обхода ограничений.
- **Гибкие настройки браузера**: Возможность настройки размера окна, user-agent и других параметров.

Требования
----------

Перед использованием этого модуля убедитесь, что установлены следующие зависимости:

- Python 3.x
- Playwright
- Crawlee

Установите необходимые зависимости Python:

.. code-block:: bash

   pip install playwright crawlee

Кроме того, убедитесь, что Playwright установлен и настроен для работы с браузером. Установите браузеры, используя команду:

.. code-block:: bash

   playwright install

Конфигурация
-------------

Конфигурация для Crawlee Python хранится в файле `crawlee_python.json`. Ниже приведён пример структуры конфигурационного файла и его описание:

Пример конфигурации (`crawlee_python.json`)
-------------------------------------------

.. code-block:: json

    {
      "max_requests": 10,
      "headless": true,
      "browser_type": "chromium",
      "options": [
        "--disable-dev-shm-usage",
        "--no-sandbox",
        "--disable-gpu"
      ],
      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
      "proxy": {
        "enabled": false,
        "server": "http://proxy.example.com:8080",
        "username": "user",
        "password": "password"
      },
      "viewport": {
        "width": 1280,
        "height": 720
      },
      "timeout": 30000,
      "ignore_https_errors": false
    }

Описание полей конфигурации
----------------------------

#### 1. `max_requests`

Максимальное количество запросов, которые будут выполнены во время обхода. По умолчанию `10`.

#### 2. `headless`

Булевое значение, указывающее, должен ли браузер запускаться в безголовом режиме. По умолчанию `true`.

#### 3. `browser_type`

Тип браузера, который будет использоваться. Возможные значения:

- `chromium` (по умолчанию)
- `firefox`
- `webkit`

#### 4. `options`

Список аргументов командной строки, передаваемых в браузер. Примеры:

- `--disable-dev-shm-usage`: Отключает использование `/dev/shm` в Docker-контейнерах.
- `--no-sandbox`: Отключает режим песочницы.
- `--disable-gpu`: Отключает аппаратное ускорение GPU.

#### 5. `user_agent`

Строка user-agent, которая будет использоваться для запросов браузера.

#### 6. `proxy`

Настройки прокси-сервера:

- **enabled**: Булевое значение, указывающее, следует ли использовать прокси.
- **server**: Адрес прокси-сервера.
- **username**: Имя пользователя для аутентификации на прокси-сервере.
- **password**: Пароль для аутентификации на прокси-сервере.

#### 7. `viewport`

Размеры окна браузера:

- **width**: Ширина окна.
- **height**: Высота окна.

#### 8. `timeout`

Максимальное время ожидания для выполнения операций (в миллисекундах). По умолчанию `30000` (30 секунд).

#### 9. `ignore_https_errors`

Булевое значение, указывающее, следует ли игнорировать ошибки HTTPS. По умолчанию `false`.

Использование
-------------

Чтобы использовать `CrawleePython` в своём проекте, просто импортируйте его и инициализируйте:

.. code-block:: python

    from src.webdriver.crawlee_python import CrawleePython
    import asyncio

    # Инициализация CrawleePython с пользовательскими опциями
    async def main():
        crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium', options=["--headless"])
        await crawler.run(['https://www.example.com'])

    asyncio.run(main())

Класс `CrawleePython` автоматически загружает настройки из файла `crawlee_python.json` и использует их для конфигурации WebDriver.
Также можно указать пользовательский user-agent и передать дополнительные опции при инициализации WebDriver.

Логирование и отладка
-----------------------

Класс WebDriver использует `logger` из `src.logger` для логирования ошибок, предупреждений и общей информации.
Все проблемы, возникающие при инициализации, конфигурации или выполнении, будут записываться в логи для удобства отладки.

Примеры логов
-------------

- **Ошибка при инициализации WebDriver**: `Ошибка при инициализации Crawlee Python: <детали ошибки>`
- **Проблемы с конфигурацией**: `Ошибка в файле crawlee_python.json: <детали проблемы>`

Лицензия
--------

Этот проект лицензирован на условиях MIT License. Подробности см. в файле [LICENSE](../../LICENSE).
```
```python
# -*- coding: utf-8 -*-
"""
Модуль Crawlee Python для автоматизации и сбора данных.
=========================================================================================

Этот модуль предоставляет класс :class:`CrawleePython`, который является кастомной реализацией
`PlaywrightCrawler` с использованием библиотеки Crawlee. Он предназначен для настройки параметров
запуска браузера, обработки веб-страниц и извлечения данных из них. Конфигурация управляется
через файл `crawlee_python.json`.

Пример использования
---------------------

Пример инициализации и запуска :class:`CrawleePython`:

.. code-block:: python

    from src.webdriver.crawlee_python import CrawleePython
    import asyncio

    async def main():
        crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium', options=['--headless'])
        await crawler.run(['https://www.example.com'])

    asyncio.run(main())
"""
import asyncio
import os
import json # Импорт модуля json для работы с json
from typing import Any, Dict, List
from playwright.async_api import Browser, BrowserType, Playwright, async_playwright
from crawlee import PlaywrightCrawler
from src.utils.jjson import j_loads # Импорт j_loads для чтения json
from src.logger.logger import logger # Импорт logger для логирования

class CrawleePython(PlaywrightCrawler):
    """
    Класс :class:`CrawleePython` представляет собой кастомный краулер, использующий Playwright и Crawlee.

    Он загружает конфигурацию из файла `crawlee_python.json` и позволяет настраивать параметры
    браузера, включая headless режим, тип браузера, дополнительные опции, user-agent, прокси,
    размер окна и таймаут.

    :param config_path: Путь к файлу конфигурации `crawlee_python.json`.
        По умолчанию 'crawlee_python.json'.
    :param max_requests: Максимальное количество запросов для выполнения. По умолчанию 10.
    :param headless:  Запуск браузера в headless режиме. По умолчанию `True`.
    :param browser_type: Тип браузера (`chromium`, `firefox`, `webkit`). По умолчанию `chromium`.
    :param options: Список дополнительных опций для запуска браузера.
    :param user_agent: User-agent для браузера.
    :param proxy: Настройки прокси.
    :param viewport: Размеры окна браузера.
    :param timeout: Максимальное время ожидания для операций.
    :param ignore_https_errors: Игнорировать ошибки HTTPS.

    """
    def __init__(
        self,
        config_path: str = 'crawlee_python.json',
        max_requests: int = 10,
        headless: bool = True,
        browser_type: str = 'chromium',
        options: List[str] = None,
        user_agent: str = None,
        proxy: Dict[str, Any] = None,
        viewport: Dict[str, int] = None,
        timeout: int = 30000,
        ignore_https_errors: bool = False,
    ):
        #  Инициализация класса с параметрами, чтение конфигурации из файла и установка параметров по умолчанию
        try:
            #  Загрузка конфигурации из JSON файла с использованием j_loads
            if os.path.exists(config_path):
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = j_loads(f) # Загрузка json файла
            else:
                config = {}
                logger.warning(f'Файл конфигурации {config_path} не найден. Используются параметры по умолчанию.')
        except Exception as ex:
            logger.error(f'Ошибка при чтении файла конфигурации {config_path}: {ex}')
            config = {}  # Установка пустой конфигурации в случае ошибки

        # Настройка параметров из конфигурации или переданных аргументов
        self.max_requests = max_requests if max_requests is not None else config.get('max_requests', 10)
        self.headless = headless if headless is not None else config.get('headless', True)
        self.browser_type = browser_type if browser_type is not None else config.get('browser_type', 'chromium')
        self.options = options if options is not None else config.get('options', [])
        self.user_agent = user_agent if user_agent is not None else config.get('user_agent')
        self.proxy = proxy if proxy is not None else config.get('proxy')
        self.viewport = viewport if viewport is not None else config.get('viewport')
        self.timeout = timeout if timeout is not None else config.get('timeout', 30000)
        self.ignore_https_errors = ignore_https_errors if ignore_https_errors is not None else config.get('ignore_https_errors', False)
        # Инициализация родительского класса PlaywrightCrawler с настроенными параметрами
        super().__init__(
            max_requests=self.max_requests,
            headless=self.headless,
            browser_type=self.browser_type,
            options=self.options,
            user_agent=self.user_agent,
            proxy=self.proxy,
            viewport=self.viewport,
            timeout=self.timeout,
            ignore_https_errors=self.ignore_https_errors,
        )
        logger.info(f'Инициализирован CrawleePython с параметрами: {self.__dict__}')
    
    async def _launch_browser(self, playwright: Playwright) -> Browser:
        """
        Запускает браузер с заданными настройками.

        :param playwright: Экземпляр :class:`Playwright`.
        :return: Экземпляр :class:`Browser`.
        :raises Exception: Если не удалось запустить браузер.
        """
        try:
            browser_type = getattr(playwright, self.browser_type)
            launch_options = {
                 'headless': self.headless,
                 'args': self.options,
                 'ignore_https_errors': self.ignore_https_errors,
            }

            if self.proxy and self.proxy.get('enabled'):
                launch_options['proxy'] = {
                    'server': self.proxy.get('server'),
                    'username': self.proxy.get('username'),
                    'password': self.proxy.get('password'),
                }

            if self.user_agent:
                launch_options['user_agent'] = self.user_agent
            
            if self.viewport:
                launch_options['viewport'] = self.viewport
        
            # Запуск браузера с настроенными параметрами
            browser = await browser_type.launch(**launch_options)
            logger.info(f'Браузер {self.browser_type} успешно запущен.')
            return browser
        except Exception as e:
            logger.error(f'Ошибка при запуске браузера {self.browser_type}: {e}')
            raise
    
    async def run(self, urls: List[str] = None, request_handler: Any = None, pre_navigation_hooks: List[Any] = None) -> None:
        """
        Запускает краулер для заданных URL.

        :param urls: Список URL для обхода.
        :param request_handler: Функция для обработки запросов.
            По умолчанию :meth:`handle_request`.
        :param pre_navigation_hooks: Список хуков для обработки перед навигацией.
        """
        # Запуск краулера с обработчиком запросов и предварительными хуками навигации
        if not urls:
            logger.warning('Список URL для обхода пуст.')
            return
        await super().run(urls=urls, request_handler=request_handler or self.handle_request, pre_navigation_hooks=pre_navigation_hooks)

    async def handle_request(self, playwright: Playwright, page: Any, request: Any) -> None:
        """
        Обрабатывает каждый запрос.
        Этот метод можно переопределить для кастомной обработки.

        :param playwright: Экземпляр :class:`Playwright`.
        :param page: Экземпляр :class:`Page` для текущей страницы.
        :param request: Объект :class:`Request` текущего запроса.
        """
        #  Логирование информации о запросе и адреса страницы
        logger.info(f'Обработка запроса: {request.url}, адрес страницы: {page.url}')
        # Код выполняется  для кастомной логики обработки
        ...
```