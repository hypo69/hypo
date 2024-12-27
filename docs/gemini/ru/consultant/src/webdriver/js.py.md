# Анализ кода модуля `src.webdriver.js`

**Качество кода: 8**
-   Плюсы
    -   Код хорошо структурирован, с четким разделением на классы и методы.
    -   Используются docstring для описания классов, методов и параметров.
    -   Присутствует базовая обработка исключений с использованием `logger.error`.
    -   Применены константы для магических строк.
-   Минусы
    -   Не все импорты приведены в соответствие с ранее обработанными файлами.
    -   Некоторые комментарии не соответствуют формату RST.
    -   Используется `try-except` без необходимости в некоторых местах, что можно упростить, применяя `logger.error`.
    -   `MODE` не используется и не должен быть константой.
    -   `header` не используется и должен быть удален.
    -   Импорт `gs` не используется, и его следует удалить, если он не нужен.
    -   Отсутствует обработка возвращаемых значений в методах, где это ожидается.

**Рекомендации по улучшению**

1.  **Импорты**: Удалить неиспользуемые импорты `header`, `gs`.
2.  **Комментарии**: Переписать все комментарии в формате RST.
3.  **Обработка исключений**: Упростить блоки `try-except` используя `logger.error` и возвращать значения.
4.  **Переменные**: Убрать неиспользуемую константу `MODE`.
5.  **Документация**: Добавить более подробные описания в docstring, включая примеры использования и возвращаемых значений.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с JavaScript в Selenium WebDriver
=========================================================================================

Этот модуль предоставляет класс :class:`JavaScript` для выполнения JavaScript кода в контексте
веб-страницы, используя Selenium WebDriver.
Модуль включает функции для управления видимостью элементов, получения данных о странице и
управления фокусом браузера.

:Example:

.. code-block:: python

    from selenium import webdriver
    from src.webdriver.js import JavaScript

    driver = webdriver.Chrome()
    js_executor = JavaScript(driver)

    # Пример использования unhide_DOM_element
    element = driver.find_element_by_id('hidden_element')
    if js_executor.unhide_DOM_element(element):
        print("Элемент стал видимым")

    # Пример получения ready_state
    state = js_executor.ready_state
    print(f"Состояние документа: {state}")

    driver.quit()
"""
from src.logger.logger import logger  # Импорт логгера
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class JavaScript:
    """
    Предоставляет утилиты для выполнения JavaScript в контексте веб-страницы.

    :param driver: Экземпляр Selenium WebDriver.
    :type driver: WebDriver
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализирует JavaScript хелпер с экземпляром Selenium WebDriver.

        :param driver: Экземпляр Selenium WebDriver для выполнения JavaScript.
        :type driver: WebDriver
        """
        self.driver = driver

    def unhide_DOM_element(self, element: WebElement) -> bool:
        """
        Делает невидимый DOM-элемент видимым, изменяя его свойства стиля.

        :param element: WebElement, который необходимо сделать видимым.
        :type element: WebElement
        :return: True, если скрипт выполнен успешно, иначе False.
        :rtype: bool

        :Example:
            >>> from selenium import webdriver
            >>> from src.webdriver.js import JavaScript
            >>> driver = webdriver.Chrome()
            >>> element = driver.find_element_by_id('my_hidden_element')
            >>> js = JavaScript(driver)
            >>> js.unhide_DOM_element(element)
            True
        """
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
            # Код исполняет JavaScript для изменения стиля элемента
            self.driver.execute_script(script, element)
            return True
        except Exception as ex:
            # Логирование ошибки и возврат False в случае неудачи
            logger.error('Ошибка в unhide_DOM_element: %s', ex)
            return False

    @property
    def ready_state(self) -> str:
        """
        Возвращает статус загрузки документа.

        :return: 'loading', если документ все еще загружается, 'complete', если загрузка завершена, или пустую строку в случае ошибки.
        :rtype: str

        :Example:
            >>> from selenium import webdriver
            >>> from src.webdriver.js import JavaScript
            >>> driver = webdriver.Chrome()
            >>> js = JavaScript(driver)
            >>> js.ready_state
            'complete'
        """
        try:
            # Код исполняет JavaScript для получения статуса загрузки документа
            return self.driver.execute_script('return document.readyState;')
        except Exception as ex:
            # Логирование ошибки и возврат пустой строки в случае неудачи
            logger.error('Ошибка при получении document.readyState: %s', ex)
            return ''

    def window_focus(self) -> None:
        """
        Устанавливает фокус на окно браузера с помощью JavaScript.

        Попытка вынести окно браузера на передний план.
        :Example:
           >>> from selenium import webdriver
           >>> from src.webdriver.js import JavaScript
           >>> driver = webdriver.Chrome()
           >>> js = JavaScript(driver)
           >>> js.window_focus()
        """
        try:
             # Код исполняет JavaScript для установки фокуса на окно браузера
            self.driver.execute_script('window.focus();')
        except Exception as ex:
             # Логирование ошибки при установке фокуса на окно
            logger.error('Ошибка при выполнении window.focus(): %s', ex)

    def get_referrer(self) -> str:
        """
        Возвращает URL-адрес реферера текущего документа.

        :return: URL реферера или пустую строку, если он недоступен.
        :rtype: str
        :Example:
            >>> from selenium import webdriver
            >>> from src.webdriver.js import JavaScript
            >>> driver = webdriver.Chrome()
            >>> js = JavaScript(driver)
            >>> js.get_referrer()
            'https://www.google.com/'
        """
        try:
            # Код исполняет JavaScript для получения URL реферера
            return self.driver.execute_script('return document.referrer;') or ''
        except Exception as ex:
            # Логирование ошибки при получении URL реферера
            logger.error('Ошибка при получении document.referrer: %s', ex)
            return ''

    def get_page_lang(self) -> str:
        """
        Возвращает язык текущей страницы.

        :return: Код языка страницы или пустую строку, если он недоступен.
        :rtype: str
        :Example:
            >>> from selenium import webdriver
            >>> from src.webdriver.js import JavaScript
            >>> driver = webdriver.Chrome()
            >>> js = JavaScript(driver)
            >>> js.get_page_lang()
            'ru'
        """
        try:
            # Код исполняет JavaScript для получения языка страницы
            return self.driver.execute_script('return document.documentElement.lang;') or ''
        except Exception as ex:
            # Логирование ошибки при получении языка страницы
            logger.error('Ошибка при получении document.documentElement.lang: %s', ex)
            return ''
```