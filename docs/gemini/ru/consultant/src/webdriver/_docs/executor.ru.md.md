# Анализ кода модуля `executor.py`

**Качество кода**
    
**7/10**
 -  Плюсы
        - Код хорошо структурирован и разделен на логические блоки.
        - Используются стандартные библиотеки Selenium.
        - Присутствуют основные методы для взаимодействия с веб-элементами.
        - Есть обработка исключений для предотвращения сбоев.
        - Используются `logger` для отслеживания ошибок и отладки.
 -  Минусы
    - Отсутствует документация в формате reStructuredText (RST) для классов, методов и функций.
    - Используется стандартный блок `try-except` без явного логирования ошибок в некоторых местах.
    - Некоторые части кода не соответствуют PEP8 (например, отсутствие пробелов в `By.XPATH`).
    - Присутсвуют неиспользуемые импорты `from src import gs`.
    - Есть избыточные `return` в функциях, где они не требуются.
    - Не стандартизирован подход к формированию сообщений об ошибках.

**Рекомендации по улучшению**

1.  **Документирование кода**:
    *   Добавить docstring в формате RST для всех классов, методов и функций.
    *   Улучшить комментарии, сделав их более подробными и информативными.

2.  **Улучшение обработки исключений**:
    *   Использовать `logger.error` для логирования исключений вместо стандартного `try-except`.
    *   Добавить более конкретные сообщения об ошибках в logger.

3.  **Унификация сообщений**:
    *   Привести к единому стилю сообщения об ошибках.
    *   Улучшить сообщения об ошибках, добавив контекст.

4.  **Улучшение `evaluate_locator`**:
     * Улучшить обработку исключений внутри `evaluate_locator` и `_evaluate`
     * Обеспечить более явное логирование ошибок в этих методах.

5.  **Удаление избыточных импортов**:
    *   Удалить неиспользуемые импорты, такие как `from src import gs`.

6.  **Стиль кода**:
    *   Привести код в соответствие с PEP8.
    *   Добавить пробелы в `By.XPATH`.

7.  **Удаление избыточных `return`**:
    *   Убрать избыточные `return` в функциях, где они не влияют на ход выполнения.

**Оптимизированный код**

```python
"""
Модуль для выполнения действий с веб-элементами на основе локаторов.
===================================================================

Этот модуль содержит класс :class:`ExecuteLocator`, который используется
для взаимодействия с элементами веб-страницы через Selenium WebDriver.

Класс предоставляет методы для поиска элементов, отправки сообщений, получения атрибутов
и выполнения других действий на веб-странице на основе заданных локаторов.

Пример использования
--------------------

.. code-block:: python

    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator

    driver = webdriver.Chrome()  # Замените на нужный драйвер
    executor = ExecuteLocator(driver)

    locator = {
        "by": "xpath",
        "selector": "//input[@id='myInput']"
    }
    element = executor.get_webelement_by_locator(locator)
    if element:
        element.send_keys("Hello World!")
    driver.quit()
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from types import SimpleNamespace
from typing import Union, List, Dict, Any

from src.utils.printer import pprint, j_loads, j_loads_ns, j_dumps, save_png
from src.logger.logger import logger
from src.logger.exceptions import DefaultSettingsException, WebDriverException, ExecuteLocatorException


class ExecuteLocator:
    """
    Класс для выполнения действий с элементами веб-страницы на основе локаторов.
    
    :param driver: Экземпляр Selenium WebDriver.
    :type driver: selenium.webdriver.remote.webdriver.WebDriver
    
    """

    def __init__(self, driver, *args, **kwargs):
        """
        Инициализирует экземпляр класса `ExecuteLocator`.

        :param driver: Экземпляр Selenium WebDriver.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.actions = ActionChains(driver)
        self.by_mapping = {
            'id': By.ID,
            'xpath': By.XPATH,
            'class': By.CLASS_NAME,
            'css': By.CSS_SELECTOR,
            'name': By.NAME,
            'link': By.LINK_TEXT,
            'tag': By.TAG_NAME,
        }
    def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
        """
        Выполняет действие с элементом веб-страницы на основе переданного локатора.

        :param locator: Словарь, содержащий параметры локатора.
        :type locator: dict
        :param message: Сообщение для отправки элементу.
        :type message: str, optional
        :param typing_speed: Скорость набора текста.
        :type typing_speed: float, optional
        :param continue_on_error: Флаг, определяющий, следует ли продолжать выполнение при ошибке.
        :type continue_on_error: bool, optional
        :return: Результат выполнения действия.
        :rtype: Union[str, list, dict, WebElement, bool]
        
        :raises ExecuteLocatorException: Если возникает ошибка во время выполнения.
        """
        if not locator:
            logger.error(f'Локатор не определен: {locator=}')
            return False
        
        if isinstance(locator, SimpleNamespace):
            locator = vars(locator)
        
        action = locator.get('action', None)
        attribute = locator.get('attribute', None)
        
        try:
            if action == 'send_message' and message:
                # код исполняет отправку сообщения
                return self.send_message(locator, message, typing_speed, continue_on_error)
            elif attribute:
                # код исполняет получение атрибута
                return self.get_attribute_by_locator(locator, message)
            else:
                # код исполняет получение элемента
                return self.get_webelement_by_locator(locator, message)
        except Exception as ex:
            if continue_on_error:
                logger.error(f'Ошибка при выполнении локатора: {locator=}', exc_info=ex)
                return False
            else:
                raise ExecuteLocatorException(f'Ошибка при выполнении локатора {locator=}', ex)
    
    def get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> Union[WebElement, List[WebElement], bool]:
        """
        Получает элемент или список элементов на веб-странице по заданному локатору.

        :param locator: Словарь или объект SimpleNamespace, содержащий параметры локатора.
        :type locator: Union[dict, SimpleNamespace]
        :param message: Сообщение для логирования.
        :type message: str, optional
        :return: Найденный элемент(ы) или False в случае ошибки.
        :rtype: Union[WebElement, List[WebElement], bool]
        """
        if isinstance(locator, SimpleNamespace):
             locator = vars(locator)
             
        by = locator.get('by')
        selector = locator.get('selector')
        selector_2 = locator.get('selector 2')
        if_list = locator.get('if_list')
        timeout = locator.get('timeout', 10)
        timeout_for_event = locator.get('timeout_for_event', 'presence_of_element_located')
        
        if not (by and selector):
            logger.error(f'Не определены `by` или `selector` в локаторе {locator=}')
            return False
        
        try:
            by_value = self.by_mapping.get(by)
            if not by_value:
                logger.error(f'Неизвестный тип локатора: {by=}')
                return False

            wait = WebDriverWait(self.driver, timeout)
            
            if timeout_for_event == 'presence_of_element_located':
                element = wait.until(EC.presence_of_element_located((by_value, selector)))
            elif timeout_for_event == 'visibility_of_element_located':
                element = wait.until(EC.visibility_of_element_located((by_value, selector)))
            elif timeout_for_event == 'presence_of_all_elements_located':
                 elements = wait.until(EC.presence_of_all_elements_located((by_value, selector)))
                 if if_list == 'first':
                     return elements[0] if elements else False
                 return elements
            else:
                logger.error(f'Не известный тип события {timeout_for_event=}')
                return False

            if element:
                 return element
        except TimeoutException:
            logger.debug(f'Элемент не найден по локатору: {locator=}')
            if selector_2:
                try:
                   if timeout_for_event == 'presence_of_element_located':
                        element = wait.until(EC.presence_of_element_located((self.by_mapping.get(by), selector_2)))
                   elif timeout_for_event == 'visibility_of_element_located':
                        element = wait.until(EC.visibility_of_element_located((self.by_mapping.get(by), selector_2)))
                   elif timeout_for_event == 'presence_of_all_elements_located':
                         elements = wait.until(EC.presence_of_all_elements_located((self.by_mapping.get(by), selector_2)))
                         if if_list == 'first':
                            return elements[0] if elements else False
                         return elements
                   else:
                         logger.error(f'Не известный тип события {timeout_for_event=}')
                         return False
                   if element:
                        return element
                except TimeoutException as ex:
                   logger.debug(f'Элемент не найден по локатору selector 2: {locator=}', exc_info=ex)
                   return False
            return False
        except Exception as ex:
            logger.error(f'Непредвиденная ошибка при получении элемента: {locator=}', exc_info=ex)
            return False

    def get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> Union[str, list, dict, bool]:
        """
        Получает значение атрибута элемента на веб-странице по заданному локатору.

        :param locator: Словарь или объект SimpleNamespace, содержащий параметры локатора.
        :type locator: Union[dict, SimpleNamespace]
        :param message: Сообщение для логирования.
        :type message: str, optional
        :return: Значение атрибута или False в случае ошибки.
        :rtype: Union[str, list, dict, bool]
        """
        if isinstance(locator, SimpleNamespace):
             locator = vars(locator)
        
        attribute = locator.get('attribute')
        if not attribute:
            logger.error(f'Атрибут не определен в локаторе: {locator=}')
            return False

        element = self.get_webelement_by_locator(locator, message)
        if not element:
            return False
        
        try:
             if isinstance(element, list):
                return [self._get_element_attribute(el, attribute) for el in element]
             return self._get_element_attribute(element, attribute)
        except Exception as ex:
             logger.error(f'Ошибка при получении атрибута {attribute} для элемента: {locator=}', exc_info=ex)
             return False

    def _get_element_attribute(self, element: WebElement, attribute: str) -> Union[str, None]:
        """
        Получает значение указанного атрибута элемента.

        :param element: Экземпляр веб-элемента.
        :type element: WebElement
        :param attribute: Имя атрибута, значение которого нужно получить.
        :type attribute: str
        :return: Значение атрибута или None, если атрибут не найден.
        :rtype: Union[str, None]
        """
        try:
            return element.get_attribute(attribute)
        except Exception as ex:
            logger.error(f'Ошибка при получении атрибута {attribute}: {element=}', exc_info=ex)
            return None

    def send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool:
        """
        Отправляет сообщение в элемент веб-страницы.

        :param locator: Словарь или объект SimpleNamespace, содержащий параметры локатора.
        :type locator: Union[dict, SimpleNamespace]
        :param message: Сообщение для отправки.
        :type message: str
        :param typing_speed: Скорость набора текста.
        :type typing_speed: float
        :param continue_on_error: Флаг, определяющий, следует ли продолжать выполнение при ошибке.
        :type continue_on_error: bool
        :return: True в случае успешной отправки, False в случае ошибки.
        :rtype: bool
        """
        element = self.get_webelement_by_locator(locator)
        if not element:
            return False

        try:
            if typing_speed > 0:
                for char in message:
                    element.send_keys(char)
                    import time
                    time.sleep(typing_speed)
            else:
                element.send_keys(message)
            return True
        except Exception as ex:
            if continue_on_error:
                logger.error(f'Ошибка при отправке сообщения: {locator=}, {message=}', exc_info=ex)
                return False
            else:
               raise  ExecuteLocatorException(f'Ошибка при отправке сообщения {locator=}, {message=}', ex)
    
    def evaluate_locator(self, attribute: str | list | dict) -> Union[str, None]:
        """
        Оценивает атрибут локатора.

        :param attribute: Атрибут для оценки.
        :type attribute: Union[str, list, dict]
        :return: Оцененное значение атрибута.
        :rtype: Union[str, None]
        """
        if isinstance(attribute, str):
           return self._evaluate(attribute)
        elif isinstance(attribute, list):
            res = []
            for attr in attribute:
                res.append(self._evaluate(attr))
            return res
        elif isinstance(attribute, dict):
            res = {}
            for key, value in attribute.items():
                res[key] = self._evaluate(value)
            return res
        return None
    
    def _evaluate(self, attribute: str) -> Union[str, None]:
        """
        Вспомогательный метод для оценки одного атрибута.

        :param attribute: Атрибут для оценки.
        :type attribute: str
        :return: Оцененное значение атрибута.
        :rtype: Union[str, None]
        """
        try:
          return str(eval(attribute, {}, {'driver':self.driver}))
        except Exception as ex:
            logger.error(f'Ошибка при вычислении атрибута: {attribute=}', exc_info=ex)
            return None

    @staticmethod
    def get_locator_keys() -> list:
        """
        Возвращает список ключей, которые могут быть использованы в локаторах.

        :return: Список ключей локаторов.
        :rtype: list
        """
        return [
            'by',
            'selector',
            'selector 2',
            'attribute',
            'action',
            'message',
            'typing_speed',
            'if_list',
            'timeout',
            'timeout_for_event',
            'event',
            'mandatory',
             'continue_on_error'
        ]
```