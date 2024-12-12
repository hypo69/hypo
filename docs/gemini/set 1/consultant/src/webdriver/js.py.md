# Анализ кода модуля `src.webdriver.js`

**Качество кода**
9
-  Плюсы
    -  Хорошая структура модуля, класс `JavaScript` предоставляет набор функций для взаимодействия со страницей через JavaScript.
    -  Используются docstring для описания классов, методов и функций.
    -  Присутствует обработка ошибок с помощью `try-except` и логирования ошибок.
    -  Код соответствует PEP8.
-  Минусы
    -  В некоторых функциях отсутствуют проверки на пустые или `None` значения возвращаемых данных из JavaScript.
    -  Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Не все блоки try-except имеют `return`

**Рекомендации по улучшению**
1.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` (если это необходимо для обработки данных, получаемых через JavaScript, что не является случаем в текущем коде).
2.  Добавить проверки на пустые или `None` значения для результатов выполнения JavaScript, чтобы избежать ошибок при дальнейшей работе с данными.
3.  Улучшить обработку ошибок, добавив `return` после логирования ошибки, чтобы предотвратить дальнейшее выполнение кода с невалидными данными.
4.  Уточнить комментарии в формате reStructuredText.
5.  Добавить `from src.logger.logger import logger` для логирования ошибок.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с JavaScript в WebDriver
=========================================================================================

Этот модуль предоставляет класс :class:`JavaScript`, который используется для выполнения JavaScript-кода
в контексте веб-страницы, управляемой Selenium WebDriver. Он включает в себя методы для управления
видимостью элементов, получения информации о странице и управлением фокусом браузера.

Основные возможности:
    1. Управление видимостью DOM элементов.
    2. Получение метаданных, таких как статус загрузки документа, реферер и язык страницы.
    3. Управление фокусом окна браузера.

Пример использования
--------------------

Пример создания экземпляра класса `JavaScript`:

.. code-block:: python

    from selenium import webdriver
    from src.webdriver.js import JavaScript

    driver = webdriver.Chrome()
    js_executor = JavaScript(driver)

    # Пример использования методов
    js_executor.window_focus()
    print(js_executor.ready_state)
"""
MODE = 'dev'

#from src.utils.jjson import j_loads, j_loads_ns #TODO: not used
import header
from src import gs
from src.logger.logger import logger
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class JavaScript:
    """
    Предоставляет набор JavaScript утилит для взаимодействия с веб-страницей.

    :param driver: Экземпляр Selenium WebDriver для выполнения JavaScript.
    :type driver: WebDriver
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализирует JavaScript хелпер с экземпляром Selenium WebDriver.

        :param driver: Экземпляр Selenium WebDriver, который будет использоваться для выполнения JavaScript кода.
        :type driver: WebDriver
        """
        self.driver = driver

    def unhide_DOM_element(self, element: WebElement) -> bool:
        """
        Делает невидимый DOM-элемент видимым, изменяя его CSS свойства.

        :param element: DOM-элемент, который необходимо сделать видимым.
        :type element: WebElement
        :return: True, если скрипт выполнен успешно, False в противном случае.
        :rtype: bool
        """
        #  JavaScript код для изменения свойств элемента и прокрутки к нему
        script = """
        arguments[0].style.opacity = 1;
        arguments[0].style.transform = 'translate(0px, 0px) scale(1)';
        arguments[0].style.MozTransform = 'translate(0px, 0px) scale(1)';
        arguments[0].style.WebkitTransform = 'translate(0px, 0px) scale(1)';
        arguments[0].style.msTransform = 'translate(0px, 0px) scale(1)';
        arguments[0].style.OTransform = 'translate(0px, 0px) scale(1)';
        arguments[0].scrollIntoView(true);
        return true;
        """
        try:
            #  Выполняет JavaScript код для изменения видимости элемента
            self.driver.execute_script(script, element)
            return True
        except Exception as ex:
            #  Логирует ошибку, если выполнение скрипта не удалось
            logger.error('Error in unhide_DOM_element: %s', ex)
            return False

    @property
    def ready_state(self) -> str:
        """
        Возвращает статус загрузки документа.

        :return: 'loading', если документ еще загружается, 'complete', если загрузка завершена.
        :rtype: str
        """
        try:
            #  Выполняет JavaScript код для получения состояния документа
            result = self.driver.execute_script('return document.readyState;')
            return result or '' # Возвращаем пустую строку если результат пустой
        except Exception as ex:
            #  Логирует ошибку при получении состояния документа
            logger.error('Error retrieving document.readyState: %s', ex)
            return ''

    def window_focus(self) -> None:
        """
        Устанавливает фокус на окно браузера, используя JavaScript.
        """
        try:
            #  Выполняет JavaScript код для установки фокуса на окно
            self.driver.execute_script('window.focus();')
        except Exception as ex:
            #  Логирует ошибку при установке фокуса на окно
            logger.error('Error executing window.focus(): %s', ex)

    def get_referrer(self) -> str:
        """
        Возвращает URL реферера текущего документа.

        :return: URL реферера, или пустую строку, если реферер недоступен.
        :rtype: str
        """
        try:
             #  Выполняет JavaScript код для получения реферера
            result = self.driver.execute_script('return document.referrer;')
            return result or ''# Возвращаем пустую строку если результат пустой
        except Exception as ex:
            #  Логирует ошибку при получении реферера документа
            logger.error('Error retrieving document.referrer: %s', ex)
            return ''

    def get_page_lang(self) -> str:
        """
        Возвращает язык текущей страницы.

        :return: Языковой код страницы или пустую строку, если код не доступен.
        :rtype: str
        """
        try:
            #  Выполняет JavaScript код для получения языка страницы
            result = self.driver.execute_script('return document.documentElement.lang;')
            return result or '' # Возвращаем пустую строку если результат пустой
        except Exception as ex:
            #  Логирует ошибку при получении языка страницы
            logger.error('Error retrieving document.documentElement.lang: %s', ex)
            return ''
```