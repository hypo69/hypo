# Анализ кода модуля `src.webdriver.crawlee_python`

## Качество кода:

- **Соответствие стандартам**: 7
- **Плюсы**:
    - Документация в формате `RST`.
    - Подробное описание функциональности модуля.
    - Описаны основные функции, параметры и их предназначение.
    - Есть пример конфигурационного файла.
- **Минусы**:
    - Отсутствует описание в формате RST для класса `CrawleePython`.
    - Отсутствует описание в формате RST для методов класса `CrawleePython`.
    - Примеры кода в документации не форматированы как python code blocks.
    - Используются двойные кавычки для строковых литералов в Python-коде в примере использования.
    - Не указанно, что используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Отсутствуют примеры вызова функций.

## Рекомендации по улучшению:

-   Добавить описание класса `CrawleePython` в формате **RST**.
-   Добавить описания методов класса `CrawleePython` в формате **RST**.
-   Исправить примеры кода, поместив их в `code-block:: python`.
-   Использовать одинарные кавычки для строковых литералов в Python-коде, кроме операций вывода.
-   Указать явно, что для загрузки конфигурации используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
-   Добавить примеры вызова функций.
-   Указать, что используется `logger` из `src.logger`.

## Оптимизированный код:

```rst
.. module:: src.webdriver.crawlee_python

Модуль Crawlee Python для автоматизации и сбора данных
=====================================================

Этот модуль предоставляет пользовательскую реализацию `PlaywrightCrawler` с использованием библиотеки Crawlee.
Он позволяет настраивать параметры запуска браузера, обрабатывать веб-страницы и извлекать из них данные.
Конфигурация управляется через файл `crawlee_python.json`.

Ключевые особенности
--------------------

-   **Централизованная конфигурация**: Управление конфигурацией осуществляется через файл `crawlee_python.json`.
-   **Поддержка пользовательских опций**: Возможность передачи пользовательских опций во время инициализации.
-   **Улучшенное логирование и обработка ошибок**: Предоставляет подробные логи для инициализации, проблем с конфигурацией и ошибок WebDriver.
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

Кроме того, убедитесь, что Playwright установлен и настроен для работы с браузером. Установите браузеры, используя команду:

.. code-block:: bash

    playwright install

Конфигурация
-------------

Конфигурация для Crawlee Python хранится в файле `crawlee_python.json`.
Ниже приведена примерная структура файла конфигурации и ее описание:

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
----------------------------

#### 1. `max_requests`

Максимальное количество запросов для выполнения во время обхода. По умолчанию `10`.

#### 2. `headless`

Логическое значение, указывающее, следует ли запускать браузер в режиме без графического интерфейса. По умолчанию `true`.

#### 3. `browser_type`

Тип браузера для использования. Возможные значения:

-   `chromium` (по умолчанию)
-   `firefox`
-   `webkit`

#### 4. `options`

Список аргументов командной строки, передаваемых браузеру. Примеры:

-   `--disable-dev-shm-usage`: Отключает использование `/dev/shm` в контейнерах Docker.
-   `--no-sandbox`: Отключает режим песочницы.
-   `--disable-gpu`: Отключает аппаратное ускорение GPU.

#### 5. `user_agent`

Строка user-agent для использования в запросах браузера.

#### 6. `proxy`

Настройки прокси-сервера:

-   **enabled**: Логическое значение, указывающее, следует ли использовать прокси.
-   **server**: Адрес прокси-сервера.
-   **username**: Имя пользователя для аутентификации прокси.
-   **password**: Пароль для аутентификации прокси.

#### 7. `viewport`

Размеры окна браузера:

-   **width**: Ширина окна.
-   **height**: Высота окна.

#### 8. `timeout`

Максимальное время ожидания для операций (в миллисекундах). По умолчанию `30000` (30 секунд).

#### 9. `ignore_https_errors`

Логическое значение, указывающее, следует ли игнорировать ошибки HTTPS. По умолчанию `false`.

Использование
-------------

Для использования `CrawleePython` в вашем проекте просто импортируйте и инициализируйте его:

.. code-block:: python

    from src.webdriver.crawlee_python import CrawleePython
    import asyncio

    # Инициализация CrawleePython с пользовательскими опциями
    async def main():
        crawler = CrawleePython(
            max_requests=10,
            headless=True,
            browser_type='chromium',
            options=['--headless']
        )
        await crawler.run(['https://www.example.com'])

    asyncio.run(main())

Класс `CrawleePython` автоматически загружает настройки из файла `crawlee_python.json` и использует их для настройки WebDriver.
Вы также можете указать пользовательский user-agent и передать дополнительные параметры во время инициализации WebDriver.

Логирование и отладка
---------------------

Класс WebDriver использует `logger` из `src.logger` для регистрации ошибок, предупреждений и общей информации.
Все проблемы, возникшие во время инициализации, настройки или выполнения, будут зарегистрированы для облегчения отладки.

Примеры логов
-------------

-   **Ошибка во время инициализации WebDriver**: `Error initializing Crawlee Python: <error details>`
-   **Проблемы с конфигурацией**: `Error in crawlee_python.json file: <issue details>`

Лицензия
--------

Этот проект лицензирован в соответствии с лицензией MIT. Подробности см. в файле `LICENSE`

.. code-block:: python
    
    """
    Модуль для работы с веб-драйвером Crawlee
    ========================================

    Этот модуль предоставляет класс :class:`CrawleePython`, который используется для управления браузером с помощью Playwright и библиотеки Crawlee.
    Конфигурация загружается из файла `crawlee_python.json`, и есть возможность задавать дополнительные параметры.
    """

    import asyncio
    import json
    from pathlib import Path
    from typing import Any

    from playwright.async_api import BrowserType, Playwright, async_playwright
    from crawlee import PlaywrightCrawler, Request, Router
    
    from src.logger import logger  # Используем logger из src.logger
    from src.utils.jjson import j_loads  # Используем j_loads из src.utils.jjson


    class CrawleePython(PlaywrightCrawler):
        """
        Класс для управления браузером с помощью Playwright и библиотеки Crawlee.
        Конфигурация загружается из файла `crawlee_python.json`, и есть возможность задавать дополнительные параметры.

        :param config_path: Путь к файлу конфигурации.
        :type config_path: str, optional
        :param max_requests: Максимальное количество запросов.
        :type max_requests: int, optional
        :param headless: Запуск браузера в headless-режиме.
        :type headless: bool, optional
        :param browser_type: Тип браузера.
        :type browser_type: str, optional
        :param options: Список дополнительных опций запуска браузера.
        :type options: list[str], optional
        :param user_agent: User-agent для браузера.
        :type user_agent: str, optional
        
        :raises FileNotFoundError: Если файл конфигурации не найден.
        :raises json.JSONDecodeError: Если файл конфигурации не является корректным JSON.
        """

        def __init__(
            self,
            config_path: str | Path = 'crawlee_python.json',
            max_requests: int | None = None,
            headless: bool | None = None,
            browser_type: str | None = None,
            options: list[str] | None = None,
            user_agent: str | None = None,
            **kwargs: Any,
        ) -> None:
            try:
                with open(config_path, 'r', encoding='utf-8') as f: # Открываем файл конфигурации
                    config_data = j_loads(f) # Используем j_loads из src.utils.jjson
            except FileNotFoundError:
                logger.error(f"Config file not found: {config_path}") # Логируем ошибку, если файл не найден
                raise
            except json.JSONDecodeError as e:
                logger.error(f"Error decoding JSON in {config_path}: {e}") # Логируем ошибку декодирования JSON
                raise

            self.max_requests = max_requests if max_requests is not None else config_data.get('max_requests', 10) # Получаем максимальное количество запросов или устанавливаем значение по умолчанию
            self.headless = headless if headless is not None else config_data.get('headless', True) # Получаем флаг headless или устанавливаем значение по умолчанию
            self.browser_type = browser_type if browser_type is not None else config_data.get('browser_type', 'chromium') # Получаем тип браузера или устанавливаем значение по умолчанию
            self.options = options if options is not None else config_data.get('options', []) # Получаем дополнительные опции или устанавливаем значение по умолчанию
            self.user_agent = user_agent if user_agent is not None else config_data.get('user_agent') # Получаем user-agent или устанавливаем значение по умолчанию
            self.proxy = config_data.get('proxy', {}) # Получаем настройки прокси
            self.viewport = config_data.get('viewport', {}) # Получаем настройки viewport
            self.timeout = config_data.get('timeout', 30000) # Получаем таймаут
            self.ignore_https_errors = config_data.get('ignore_https_errors', False) # Получаем флаг игнорирования ошибок HTTPS
            self._extend_init(**kwargs) # Расширяем инициализацию с помощью дополнительных аргументов

            router = Router() # Создаем роутер
            router.add_default_handler(self.default_handler) # Добавляем обработчик по умолчанию
            
            super().__init__(router=router, **kwargs) # Инициализируем родительский класс

        def _extend_init(self, **kwargs: Any) -> None:
            """
            Расширяет инициализацию класса, добавляя дополнительные параметры.

            :param kwargs: Дополнительные параметры для инициализации.
            :type kwargs: dict
            """
            for key, value in kwargs.items(): # Проходим по всем дополнительным параметрам
                setattr(self, key, value) # Устанавливаем атрибуты объекта

        async def default_handler(self, request: Request, playwright: Playwright, browser_type: BrowserType, **kwargs: Any) -> None:
            """
            Асинхронный обработчик по умолчанию для запросов.

            :param request: Объект запроса.
            :type request: crawlee.request.Request
            :param playwright: Объект playwright.
            :type playwright: playwright.async_api.Playwright
            :param browser_type: Объект типа браузера.
            :type browser_type: playwright.async_api.BrowserType
            :param kwargs: Дополнительные параметры.
            :type kwargs: dict
            :raises Exception: В случае возникновения ошибки при работе с браузером.

            Пример:
                >>> crawler = CrawleePython()
                >>> request = Request(url='https://example.com')
                >>> async def run_handler():
                ...    async with async_playwright() as playwright:
                ...        browser_type = playwright.chromium
                ...        await crawler.default_handler(request, playwright, browser_type)
                >>> asyncio.run(run_handler())
            """
            try:
                browser = None # Инициализируем переменную браузера
                if self.browser_type == 'chromium': # Проверяем тип браузера
                    browser = await browser_type.launch(
                        headless=self.headless, # Устанавливаем флаг headless
                        args=self.options, # Устанавливаем дополнительные опции
                        ignore_https_errors=self.ignore_https_errors, # Устанавливаем флаг игнорирования ошибок HTTPS
                        **self.get_proxy_settings(),  # Получаем настройки прокси
                        
                    )
                elif self.browser_type == 'firefox': # Проверяем тип браузера
                     browser = await browser_type.launch(
                        headless=self.headless,
                        args=self.options,
                        ignore_https_errors=self.ignore_https_errors,
                        **self.get_proxy_settings(),
                    )
                elif self.browser_type == 'webkit': # Проверяем тип браузера
                     browser = await browser_type.launch(
                        headless=self.headless,
                        args=self.options,
                        ignore_https_errors=self.ignore_https_errors,
                        **self.get_proxy_settings(),
                     )
                else:
                    logger.error(f'Unknown browser type: {self.browser_type}') # Логируем ошибку, если тип браузера неизвестен
                    return

                context = await browser.new_context(user_agent=self.user_agent, **self.get_viewport_settings()) # Создаем новый контекст
                page = await context.new_page() # Создаем новую страницу
                await page.goto(request.url, timeout=self.timeout)  # Переходим по URL
                await self.handle_page_function(page, request) # Вызываем функцию обработки страницы
            except Exception as e:
                logger.error(f"Error during page processing {request.url}: {e}") # Логируем ошибку обработки страницы
            finally:
                 if browser:
                     await browser.close() # Закрываем браузер в любом случае
                
        def get_proxy_settings(self) -> dict[str,str] | dict:
           """
           Возвращает настройки прокси, если они включены.

           :return: Словарь с настройками прокси или пустой словарь.
           :rtype: dict
           """
           if self.proxy.get('enabled'): # Проверяем, включен ли прокси
             server = self.proxy.get('server') # Получаем адрес прокси-сервера
             username = self.proxy.get('username') # Получаем имя пользователя прокси
             password = self.proxy.get('password') # Получаем пароль пользователя прокси
             
             if server and username and password: # Проверяем наличие всех необходимых параметров
                return {'proxy': {'server': server, 'username': username, 'password': password}} # Возвращаем настройки прокси
             elif server:
                return {'proxy': {'server': server}} # Возвращаем настройки прокси без авторизации
             else:
               logger.error("Proxy server address is required when proxy is enabled.") # Логируем ошибку, если не указан адрес прокси-сервера
               return {} # Возвращаем пустой словарь
           else:
                return {} # Возвращаем пустой словарь, если прокси не включен

        def get_viewport_settings(self) -> dict[str,int]:
             """
             Возвращает настройки viewport.

             :return: Словарь с настройками viewport.
             :rtype: dict
             """
             return {'viewport': self.viewport} # Возвращаем настройки viewport

        async def handle_page_function(self, page, request:Request) -> None:
            """
            Обрабатывает страницу.

            :param page: Объект страницы.
            :type page: playwright.async_api.Page
            :param request: Объект запроса.
            :type request: crawlee.request.Request
            
            Пример:
                >>> crawler = CrawleePython()
                >>> async def run_handler():
                ...    async with async_playwright() as playwright:
                ...        browser_type = playwright.chromium
                ...        browser = await browser_type.launch()
                ...        context = await browser.new_context()
                ...        page = await context.new_page()
                ...        request = Request(url='https://example.com')
                ...        await page.goto(request.url)
                ...        await crawler.handle_page_function(page,request)
                ...        await browser.close()
                >>> asyncio.run(run_handler())
            """
            ... # Обработка страницы
```