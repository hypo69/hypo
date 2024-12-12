# Анализ кода модуля pw_executor

**Качество кода**
8
 -  Плюсы
    - Присутствует описание модуля в docstring.
    - Указана кодировка файла.
 -  Минусы
    - Отсутствуют необходимые импорты.
    - Не используется `logger` для отладки и логирования.
    - MODE не является константой и должен быть описан как константа (с использованием заглавных букв).

**Рекомендации по улучшению**

1. **Добавить необходимые импорты**: Необходимо добавить импорты для работы с `asyncio`, `json` и `typing`, а также `logger`.
2. **Использовать `j_loads` для чтения JSON**:  Заменить стандартный `json.load` на `j_loads` из `src.utils.jjson` (если применимо).
3. **Добавить логирование**: Использовать `logger` для логирования ошибок и отладочной информации.
4. **Обновить docstring**: Добавить подробное описание модуля и класса, а также добавить описание к методам.
5. **Форматирование констант**: Объявить константы в соответствии с общепринятыми соглашениями (заглавные буквы).
6. **Обработка ошибок**: Заменить общие блоки `try-except` на более конкретную обработку с использованием `logger.error`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для взаимодействия с браузером через Playwright.
=========================================================================================

Этот модуль предоставляет класс :class:`PlaywrightExecutor`, который используется для выполнения различных
действий в браузере, таких как запуск и закрытие браузера, навигация по страницам,
взаимодействие с элементами и т.д.

Пример использования
--------------------

Пример использования класса `PlaywrightExecutor`:

.. code-block:: python

    executor = PlaywrightExecutor()
    await executor.init_browser()
    await executor.go_to_page("https://example.com")
    # ... другие операции
    await executor.close_browser()
"""
import asyncio
import json
from typing import Any, Dict, List, Optional, Union

from playwright.async_api import Browser, BrowserContext, Page, Playwright, async_playwright

from src.utils.jjson import j_loads, j_loads_ns # Импорт для работы с JSON
from src.logger.logger import logger # Импорт для логирования

MODE = 'dev' # Объявление константы
# TODO: Добавить класс для выполнения операций через Playwright
class PlaywrightExecutor:
    """
    Класс для управления браузером через Playwright.

    Предоставляет методы для запуска, управления браузером и выполнения различных действий
    на веб-страницах.
    """
    def __init__(self):
        """
        Инициализирует экземпляр класса PlaywrightExecutor.

        Устанавливает начальные значения для необходимых переменных.
        """
        self.playwright: Optional[Playwright] = None
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None
        self.is_init = False


    async def init_browser(self, browser_type='chromium', **kwargs) -> bool:
        """
        Инициализирует браузер Playwright.

        :param browser_type: Тип браузера для запуска (например, 'chromium', 'firefox', 'webkit').
        :param **kwargs: Дополнительные параметры для запуска браузера.
        :return: True в случае успешной инициализации, False в противном случае.
        """
        try:
            # Запускаем Playwright
            self.playwright = await async_playwright().start() # запускаем асинхронный playwright

            # Запускаем браузер с заданными параметрами
            self.browser = await getattr(self.playwright, browser_type).launch(**kwargs)

            # Создаем контекст браузера
            self.context = await self.browser.new_context()

            # Открываем новую страницу
            self.page = await self.context.new_page()
            self.is_init = True # устанавливаем флаг инициализации
            return True

        except Exception as e:
            logger.error(f'Ошибка инициализации браузера: {e}')
            return False

    async def go_to_page(self, url: str) -> bool:
        """
        Переходит по указанному URL.

        :param url: URL для перехода.
        :return: True если переход выполнен, False в случае ошибки.
        """
        if not self.page:
            logger.error('Страница не инициализирована.')
            return False
        try:
           await self.page.goto(url) # переходим по заданному url
           return True
        except Exception as e:
            logger.error(f'Ошибка при переходе на страницу: {url}, {e}')
            return False

    async def execute_locator(self, locator: str, timeout: float = 10) -> Union[str, List[str], None]:
        """
        Выполняет поиск элемента на странице с заданным локатором.

        :param locator: Локатор элемента для поиска.
        :param timeout: Максимальное время ожидания элемента в секундах.
        :return: Текст элемента или список текстов элементов, None в случае ошибки.
        """
        if not self.page:
             logger.error('Страница не инициализирована')
             return None
        try:
             await self.page.wait_for_selector(locator, timeout=timeout * 1000)
             element = await self.page.locator(locator) # ищем элемент по локатору
             if await element.count() > 1:
                text_list = []
                for el in await element.all():
                    text_list.append(await el.text_content())
                return text_list # возвращаем список текстов если элементов найдено больше 1
             return await element.text_content()
        except Exception as e:
            logger.error(f'Ошибка при выполнении локатора {locator}: {e}')
            return None

    async def close_browser(self) -> bool:
        """
        Закрывает браузер и все связанные ресурсы.

        :return: True если браузер закрыт успешно, False в случае ошибки.
        """
        try:
             if self.page:
                await self.page.close() # Закрываем страницу
             if self.context:
                await self.context.close() # Закрываем контекст
             if self.browser:
                await self.browser.close() # Закрываем браузер
             if self.playwright:
                await self.playwright.stop() # Останавливаем Playwright
             return True
        except Exception as e:
            logger.error(f'Ошибка при закрытии браузера: {e}')
            return False
        finally:
            self.is_init = False # сбрасываем флаг инициализации
```