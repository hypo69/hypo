# Анализ кода модуля `src.webdriver.crawlee_python`

**Качество кода**
8
- Плюсы
    - Документация в формате Markdown, содержит подробное описание модуля, его возможностей, процесса конфигурации и использования.
    - Присутствует описание полей конфигурационного файла `crawlee_python.json`, а также пример его использования.
    - Описаны процессы логирования и отладки.
- Минусы
    - Отсутствует описание модуля в формате reStructuredText (RST) в начале файла.
    - Не стандартизированы комментарии кода под RST.
    - Не хватает описания и примеров использования некоторых функций, переменных и классов в формате reStructuredText (RST).
    - Нет импорта модуля логирования `src.logger.logger import logger` в начале файла.
    - Не проработан механизм обработки ошибок и логирования.

**Рекомендации по улучшению**

1.  Добавить описание модуля в формате reStructuredText (RST) в начале файла.
2.  Использовать RST для комментариев и docstring всех функций, методов и классов.
3.  Добавить импорт `from src.logger.logger import logger` для логирования ошибок.
4.  Использовать `logger.error` вместо общих `try-except` для обработки ошибок.
5.  Переписать примеры использования кода, добавив больше деталей и комментариев в формате RST.
6.  Уточнить описание `CrawleePython` class и его методов.

**Оптимизированный код**

```markdown
.. module:: src.webdriver.crawlee_python
   :synopsis: Модуль для автоматизации и сбора данных с использованием Crawlee и Playwright.
   :platform: Linux, Windows, MacOS
   :author: Hypotez

Модуль Crawlee Python для автоматизации и сбора данных
===================================================================

Этот модуль представляет собой пользовательскую реализацию `PlaywrightCrawler`, использующую библиотеку Crawlee.
Он позволяет настраивать параметры запуска браузера, обрабатывать веб-страницы и извлекать из них данные.
Управление конфигурацией осуществляется через файл `crawlee_python.json`.

Ключевые особенности
-------------------

-   **Централизованная конфигурация**: Управление конфигурацией осуществляется через файл `crawlee_python.json`.
-   **Поддержка пользовательских опций**: Возможность передачи пользовательских опций во время инициализации.
-   **Расширенное логирование и обработка ошибок**: Обеспечивает подробное логирование для инициализации, проблем конфигурации и ошибок WebDriver.
-   **Поддержка прокси**: Настройка прокси-серверов для обхода ограничений.
-   **Гибкие настройки браузера**: Настройка размера области просмотра, user-agent и других параметров браузера.

Требования
----------

Перед использованием этого модуля убедитесь, что установлены следующие зависимости:

-   Python 3.x
-   Playwright
-   Crawlee

Установите необходимые зависимости Python:

.. code-block:: bash

    pip install playwright crawlee

Кроме того, убедитесь, что Playwright установлен и настроен для работы с браузером.
Установите браузеры с помощью команды:

.. code-block:: bash

    playwright install

Конфигурация
------------

Конфигурация для Crawlee Python хранится в файле `crawlee_python.json`.
Ниже приведен пример структуры файла конфигурации и его описания:

Пример конфигурации (`crawlee_python.json`)
------------------------------------------

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
--------------------------

1.  `max_requests`
    Максимальное количество запросов для выполнения во время обхода. Значение по умолчанию - `10`.

2.  `headless`
    Логическое значение, указывающее, должен ли браузер работать в безголовом режиме. Значение по умолчанию - `true`.

3.  `browser_type`
    Тип используемого браузера. Возможные значения:

    -   `chromium` (по умолчанию)
    -   `firefox`
    -   `webkit`

4.  `options`
    Список аргументов командной строки, передаваемых в браузер. Примеры:

    -   `--disable-dev-shm-usage`: Отключает использование `/dev/shm` в контейнерах Docker.
    -   `--no-sandbox`: Отключает режим песочницы.
    -   `--disable-gpu`: Отключает аппаратное ускорение GPU.

5.  `user_agent`
    Строка user-agent, которая будет использоваться для запросов браузера.

6.  `proxy`
    Настройки прокси-сервера:

    -   **enabled**: Логическое значение, указывающее, следует ли использовать прокси.
    -   **server**: Адрес прокси-сервера.
    -   **username**: Имя пользователя для аутентификации прокси.
    -   **password**: Пароль для аутентификации прокси.

7.  `viewport`
    Размеры окна браузера:

    -   **width**: Ширина окна.
    -   **height**: Высота окна.

8.  `timeout`
    Максимальное время ожидания для операций (в миллисекундах). Значение по умолчанию - `30000` (30 секунд).

9.  `ignore_https_errors`
    Логическое значение, указывающее, следует ли игнорировать ошибки HTTPS. Значение по умолчанию - `false`.

Использование
------------

Чтобы использовать `CrawleePython` в своем проекте, просто импортируйте и инициализируйте его:

.. code-block:: python

    from src.webdriver.crawlee_python import CrawleePython
    import asyncio

    async def main():
        # Инициализация CrawleePython с пользовательскими опциями
        crawler = CrawleePython(
            max_requests=10,
            headless=True,
            browser_type='chromium',
            options=["--headless"]
        )
        await crawler.run(['https://www.example.com'])

    asyncio.run(main())

Класс `CrawleePython` автоматически загружает настройки из файла `crawlee_python.json` и использует их для настройки WebDriver.
Вы также можете указать пользовательский user-agent и передать дополнительные параметры во время инициализации WebDriver.

Логирование и отладка
---------------------

Класс WebDriver использует `logger` из `src.logger` для регистрации ошибок, предупреждений и общей информации.
Все проблемы, возникающие во время инициализации, настройки или выполнения, будут зарегистрированы для облегчения отладки.

Примеры логов
-------------

-   **Ошибка во время инициализации WebDriver**: `Error initializing Crawlee Python: <error details>`
-   **Проблемы конфигурации**: `Error in crawlee_python.json file: <issue details>`

Лицензия
--------

Этот проект распространяется под лицензией MIT.
Смотрите файл [LICENSE](../../LICENSE) для подробностей.
```
```python
"""
Модуль для автоматизации и сбора данных с использованием Crawlee и Playwright.
============================================================================

Этот модуль предоставляет класс `CrawleePython`, который является пользовательской реализацией `PlaywrightCrawler`.
Он предназначен для настройки параметров запуска браузера, обработки веб-страниц и извлечения данных.
Управление конфигурацией осуществляется через файл `crawlee_python.json`.

Пример использования
--------------------

.. code-block:: python

    from src.webdriver.crawlee_python import CrawleePython
    import asyncio

    async def main():
        crawler = CrawleePython(
            max_requests=10,
            headless=True,
            browser_type='chromium',
            options=["--headless"]
        )
        await crawler.run(['https://www.example.com'])

    asyncio.run(main())
"""
import asyncio
from typing import Any, Dict, List, Optional
from playwright.async_api import BrowserType, Playwright
from crawlee import PlaywrightCrawler, Configuration
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger  # Импорт модуля логирования


class CrawleePython(PlaywrightCrawler):
    """
    Класс CrawleePython, реализующий кастомный веб-скрапер на базе PlaywrightCrawler.

    :param config_path: Путь к конфигурационному файлу JSON (по умолчанию 'crawlee_python.json').
    :param max_requests: Максимальное количество запросов для выполнения (по умолчанию 10).
    :param headless: Запуск браузера в безголовом режиме (по умолчанию True).
    :param browser_type: Тип используемого браузера ('chromium', 'firefox', 'webkit', по умолчанию 'chromium').
    :param options: Список дополнительных опций командной строки для запуска браузера.
    :param user_agent: Строка User-Agent для браузера.
    :param proxy: Настройки прокси-сервера.
    :param viewport: Размеры окна браузера.
    :param timeout: Максимальное время ожидания для операций (в миллисекундах).
    :param ignore_https_errors: Игнорировать HTTPS ошибки (по умолчанию False).
    """
    def __init__(
        self,
        config_path: str = 'crawlee_python.json',
        max_requests: int = 10,
        headless: bool = True,
        browser_type: str = 'chromium',
        options: Optional[List[str]] = None,
        user_agent: Optional[str] = None,
        proxy: Optional[Dict[str, Any]] = None,
        viewport: Optional[Dict[str, int]] = None,
        timeout: int = 30000,
        ignore_https_errors: bool = False,
        **kwargs: Any,
    ) -> None:
        """
        Инициализирует класс CrawleePython, настраивая параметры браузера и прокси.
        
        :param config_path: Путь к конфигурационному файлу JSON.
        :param max_requests: Максимальное количество запросов для выполнения.
        :param headless: Запуск браузера в безголовом режиме.
        :param browser_type: Тип используемого браузера.
        :param options: Дополнительные опции командной строки для запуска браузера.
        :param user_agent: Строка User-Agent для браузера.
        :param proxy: Настройки прокси-сервера.
        :param viewport: Размеры окна браузера.
        :param timeout: Максимальное время ожидания для операций (в миллисекундах).
        :param ignore_https_errors: Игнорировать HTTPS ошибки.
        :param kwargs: Дополнительные именованные аргументы.
        """
        self.config_path = config_path
        self.config = self._load_config()
        self.max_requests = max_requests
        self.headless = headless
        self.browser_type = browser_type
        self.options = options if options is not None else self.config.get('options', [])
        self.user_agent = user_agent if user_agent else self.config.get('user_agent')
        self.proxy = proxy if proxy else self.config.get('proxy')
        self.viewport = viewport if viewport else self.config.get('viewport')
        self.timeout = timeout
        self.ignore_https_errors = ignore_https_errors

        launch_options = self._create_launch_options()
        super().__init__(launch_options=launch_options, **kwargs)

    def _load_config(self) -> dict:
        """
        Загружает конфигурацию из JSON файла.
        
        :return: Словарь с конфигурацией.
        """
        try:
            # Загружает конфигурацию из файла
            config = j_loads_ns(self.config_path)
            # Проверяет наличие конфигурации
            if not config:
                raise ValueError(f'Конфигурация не найдена в файле {self.config_path}')
            return config
        except Exception as e:
            logger.error(f'Ошибка при загрузке конфигурации из файла {self.config_path}: {e}')
            return {}

    def _create_launch_options(self) -> Dict[str, Any]:
        """
        Создает словарь опций для запуска браузера Playwright.
        
        :return: Словарь с опциями запуска браузера.
        """
        launch_options: Dict[str, Any] = {}
        # Настройка user-agent, если он задан
        if self.user_agent:
            launch_options['user_agent'] = self.user_agent

        # Настройка прокси, если он включен
        if self.proxy and self.proxy.get('enabled'):
            launch_options['proxy'] = {
                'server': self.proxy.get('server'),
                'username': self.proxy.get('username'),
                'password': self.proxy.get('password'),
            }

        # Настройка viewport, если он задан
        if self.viewport:
            launch_options['viewport'] = self.viewport
        # Настройка timeout
        launch_options['timeout'] = self.timeout
        # Настройка игнорирования ошибок HTTPS
        launch_options['ignore_https_errors'] = self.ignore_https_errors
         # Настройка headless режима
        launch_options['headless'] = self.headless
        # Передача опций браузера
        launch_options['args'] = self.options
        return launch_options

    async def _launch_browser(self, playwright: Playwright) -> BrowserType:
        """
        Запускает браузер Playwright.
        
        :param playwright: Экземпляр Playwright.
        :return: Запущенный экземпляр браузера.
        """
        try:
             # Запускает браузер в соответствии с типом
            browser_type = getattr(playwright, self.browser_type)
            return browser_type
        except Exception as e:
            logger.error(f'Неподдерживаемый тип браузера {self.browser_type}: {e}')
            raise

    async def run(self, start_urls: List[str]) -> None:
        """
         Запускает процесс сканирования веб-страниц.

         :param start_urls: Список URL для запуска сканирования.
         """
        async with Playwright() as playwright:
             # Запускает браузер
            browser_type = await self._launch_browser(playwright)
            async with browser_type.launch(**self.launch_options) as browser:
                # Настраивает и запускает Crawler
                crawler = Configuration(
                    max_requests=self.max_requests,
                    headless=self.headless,
                    browser_type=self.browser_type,
                    options=self.options,
                    user_agent=self.user_agent,
                    proxy=self.proxy,
                    viewport=self.viewport,
                    timeout=self.timeout,
                    ignore_https_errors=self.ignore_https_errors,
                    playwright_crawler=PlaywrightCrawler(
                        launch_options=self.launch_options,
                    )
                )
                crawler.playwright_crawler.set_browser(browser)
                await crawler.playwright_crawler.run(start_urls=start_urls)
```