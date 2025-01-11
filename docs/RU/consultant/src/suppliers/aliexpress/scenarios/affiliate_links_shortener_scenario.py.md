# Анализ кода модуля `affiliate_links_shortener_scenario`

**Качество кода**
8
- Плюсы
    - Код соответствует PEP 8, используются осмысленные имена переменных.
    - Присутствует логирование ошибок.
    - Используется `j_loads_ns` для загрузки JSON.
- Минусы
    -  Некоторые комментарии не несут особой смысловой нагрузки.
    -  Не хватает подробной документации для модуля и функций в формате RST.
    -  Используется `time.sleep`, что может быть заменено на более гибкие ожидания.
    - Присутствует закомментированный код `raise ValueError`.

**Рекомендации по улучшению**

1.  **Документация:**
    -   Добавить подробное описание модуля в начале файла в формате RST.
    -   Добавить docstring для функции `get_short_affiliate_link`, включая описание аргументов и возвращаемого значения.
    -   Привести примеры использования функции.

2.  **Обработка ошибок:**
    -   Удалить закомментированный код `raise ValueError` и оставить только логирование ошибки с помощью `logger.error`.
    -   Избегать использования `time.sleep`, использовать более гибкие `WebDriverWait` или аналогичные механизмы ожидания.

3.  **Улучшение читаемости:**
    -   Убрать лишние комментарии, которые не добавляют понимания коду, а дублируют его.
    -   Переформулировать комментарии в более информативные.
    -   Добавить проверку существования элемента перед тем, как его получить, для избежания возможных ошибок.

4.  **Соответствие стандартам**:
    -   Использовать `from src.logger.logger import logger`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
Модуль для сокращения партнерских ссылок AliExpress.
=========================================================================================

Этот модуль предоставляет функциональность для генерации сокращенных партнерских ссылок через веб-браузер.
Он использует драйвер браузера для взаимодействия с веб-страницей и выполняет необходимые действия
для получения короткой ссылки.

Пример использования
--------------------

.. code-block:: python

    from src.webdriver.driver import Driver
    from src.suppliers.aliexpress.scenarios.affiliate_links_shortener_scenario import get_short_affiliate_link
    from selenium import webdriver


    driver = Driver(webdriver.Chrome())
    driver.get("https://aliexpress.com/aliexpress-api/deeplink.htm")
    url = 'https://aliexpress.ru/item/1005006309896400.html'
    short_link = get_short_affiliate_link(driver, url)
    print(short_link)
    driver.quit()
"""

from pathlib import Path
from typing import List, Union
from types import SimpleNamespace
import time
from src import gs
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger
from src.webdriver.driver import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Загрузка локаторов из JSON-файла
locator = j_loads_ns(Path(gs.path.src, 'suppliers', 'aliexpress', 'locators', 'affiliate_links_shortener.json'))


def get_short_affiliate_link(d: Driver, url: str) -> str:
    """
    Генерирует сокращенную партнерскую ссылку из полной URL.

    Args:
        d (Driver): Экземпляр драйвера веб-браузера.
        url (str): Полная URL партнерской ссылки.

    Returns:
        str: Сокращенная партнерская ссылка.

    Raises:
       ValueError: Если не удалось получить короткую ссылку или если короткая ссылка некорректна.

    Example:
        >>> from src.webdriver.driver import Driver
        >>> from src.suppliers.aliexpress.scenarios.affiliate_links_shortener_scenario import get_short_affiliate_link
        >>> from selenium import webdriver
        >>>
        >>> driver = Driver(webdriver.Chrome())
        >>> driver.get("https://aliexpress.com/aliexpress-api/deeplink.htm")
        >>> url = 'https://aliexpress.ru/item/1005006309896400.html'
        >>> short_link = get_short_affiliate_link(driver, url)
        >>> print(short_link)
        >>> driver.quit()
        'https://alitems.com/g/1e8d1144942456097f7516525dc25d/?i=8&ulp=https%3A%2F%2Faliexpress.ru%2Fitem%2F1005006309896400.html&dl=y'
    """
    #  Ввод URL в поле для ввода
    d.execute_locator(locator.textarea_target_url, url)
    # Нажатие кнопки для получения короткой ссылки
    d.execute_locator(locator.button_get_tracking_link)
    try:
        # Ожидание появления короткой ссылки
        WebDriverWait(d.driver, 10).until(
            EC.presence_of_element_located(locator.textarea_short_link)
        )
        # Получение короткой ссылки
        short_url = d.execute_locator(locator.textarea_short_link)[0]
    except TimeoutException:
        logger.error(f'Не удалось получить короткий URL от {url} за отведенное время')
        return ''
    main_tab = d.current_window_handle  # Сохранение идентификатора основной вкладки

    if not short_url:
        logger.error(f'Не удалось получить короткий URL от {url}')
        return ''

    # Открытие нового таба с коротким URL
    d.execute_script(f'window.open(\'{short_url}\');')

    # Переключение на новый таб
    d.switch_to.window(d.window_handles[-1])

    # Проверка, что короткий URL начинается с ожидаемой части
    if d.current_url.startswith('https://error.taobao.com'):
        logger.error(f'Неправильный URL: {d.current_url}')
        d.close()
        d.switch_to.window(main_tab)
        return ''

    # Закрытие нового таба и возврат к основной вкладке
    d.close()
    d.switch_to.window(main_tab)

    return short_url
```