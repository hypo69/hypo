# Анализ кода модуля `executor.py`

**Качество кода**
6
-  Плюсы
    - Код структурирован, разделен на методы, что облегчает понимание и поддержку.
    - Используются стандартные библиотеки Selenium и Python.
    - Наличие документации, хотя и не в формате RST.
    - Есть обработка ошибок, но без использования `logger.error`.
-  Минусы
    - Отсутствует документация в формате reStructuredText (RST) для модуля, классов, методов и переменных.
    - Не используются `j_loads` или `j_loads_ns` для чтения файлов.
    - Избыточное использование `try-except` без применения `logger.error`.
    - Некоторые имена переменных и методов можно улучшить для лучшей читаемости.
    - Отсутствует использование `from src.logger.logger import logger` для логирования ошибок.

**Рекомендации по улучшению**

1.  **Документация RST**:
    - Добавить документацию в формате RST для модуля, классов, методов и переменных.
    - Примеры docstring для функций и методов должны соответствовать стандарту.

2.  **Обработка ошибок**:
    - Заменить стандартные блоки `try-except` на использование `logger.error` для обработки исключений.

3.  **Импорты**:
    - Убедиться, что все необходимые импорты присутствуют и соответствуют другим файлам проекта.

4.  **Использование `j_loads`**:
    - Заменить стандартный `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.

5.  **Стиль кода**:
    - Улучшить стиль кода, следуя стандартам PEP 8.
    - Использовать консистентные имена переменных и функций.

6.  **Примеры**:
    - Предоставить примеры использования методов и классов в формате RST.

**Оптимизированный код**

```python
"""
Модуль `executor.py` для выполнения действий с веб-элементами.
==============================================================

Этот модуль содержит класс :class:`ExecuteLocator`, который используется
для взаимодействия с веб-страницей через Selenium WebDriver.
Он предоставляет методы для поиска элементов, выполнения действий и
получения атрибутов.

Пример использования
--------------------

.. code-block:: python

    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator

    driver = webdriver.Chrome()
    executor = ExecuteLocator(driver)
    locator = {
        "by": "xpath",
        "selector": "//button[@id='myButton']",
    }
    element = executor.get_webelement_by_locator(locator)
    element.click()
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

#  Импортируем необходимые модули
from src import gs
from src.utils.printer import pprint, j_loads, j_loads_ns, j_dumps, save_png
from src.logger.logger import logger
from src.logger.exceptions import DefaultSettingsException, WebDriverException, ExecuteLocatorException


class ExecuteLocator:
    """
    Класс для выполнения действий с веб-элементами с использованием Selenium WebDriver.

    :param driver: Экземпляр WebDriver.
    :type driver: selenium.webdriver.remote.webdriver.WebDriver
    """
    by_mapping = {
        'id': By.ID,
        'name': By.NAME,
        'xpath': By.XPATH,
        'class_name': By.CLASS_NAME,
        'css_selector': By.CSS_SELECTOR,
        'link_text': By.LINK_TEXT,
        'partial_link_text': By.PARTIAL_LINK_TEXT,
        'tag_name': By.TAG_NAME,
    }

    def __init__(self, driver, *args, **kwargs):
        """
        Инициализирует класс ExecuteLocator.

        :param driver: Экземпляр WebDriver.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.actions = ActionChains(driver)

    def execute_locator(self, locator: Dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
        """
        Выполняет действие с веб-элементом, основываясь на параметрах локатора.

        :param locator: Словарь с параметрами локатора.
        :type locator: dict
        :param message: Сообщение для отправки (если применимо).
        :type message: str, optional
        :param typing_speed: Скорость набора текста при отправке сообщения.
        :type typing_speed: float, optional
        :param continue_on_error: Флаг для продолжения выполнения при ошибке.
        :type continue_on_error: bool, optional
        :return: Результат выполнения действия.
        :rtype: Union[str, list, dict, WebElement, bool]
        """
        if not locator:
            logger.error(f'Локатор не может быть пустым. {locator=}')
            return False
        
        action = locator.get('action')
        if action == 'send_message':
            # Код выполняет отправку сообщения, если указано действие 'send_message'
            return self.send_message(locator, message, typing_speed, continue_on_error)
        elif action == 'get_attribute':
            # Код выполняет получение атрибута элемента, если указано действие 'get_attribute'
            return self.get_attribute_by_locator(locator, message)
        elif action is None or action == 'get_element':
            # Код выполняет получение элемента, если действие не указано или равно 'get_element'
            return self.get_webelement_by_locator(locator, message)

        logger.error(f'Неизвестное действие локатора {action=}')
        return False

    def get_webelement_by_locator(self, locator: Dict | SimpleNamespace, message: str = None) -> Union[WebElement, List[WebElement], bool]:
        """
        Получает веб-элемент(ы) на основе заданного локатора.

        :param locator: Словарь или SimpleNamespace с параметрами локатора.
        :type locator: dict | SimpleNamespace
        :param message: Сообщение для логирования.
        :type message: str, optional
        :return: Веб-элемент, список веб-элементов или False в случае ошибки.
        :rtype: Union[WebElement, List[WebElement], bool]
        """
        by = locator.get('by')
        selector = locator.get('selector')
        selector2 = locator.get('selector2')
        timeout = locator.get('timeout', 10)
        timeout_for_event = locator.get('timeout_for_event', 'presence_of_element_located')
        if_list = locator.get('if_list')
        mandatory = locator.get('mandatory')
        event = locator.get('event')

        if not by or not selector:
             logger.error(f'Некорректный локатор {locator=}')
             return False
            
        try:
            by_type = self.by_mapping.get(by)
            if not by_type:
                 logger.error(f'Неверный тип локатора {by=}')
                 return False
            
            wait = WebDriverWait(self.driver, timeout)
            
            if timeout_for_event == 'presence_of_element_located':
                element = wait.until(EC.presence_of_element_located((by_type, selector)))
            elif timeout_for_event == 'visibility_of_element_located':
               element = wait.until(EC.visibility_of_element_located((by_type, selector)))
            else:
                 logger.error(f'Неверный параметр `timeout_for_event` = {timeout_for_event=}')
                 return False

            if if_list == 'first':
                #  Код возвращает первый элемент из списка, если указано `if_list = 'first'`
                 return element
            elif if_list == 'all':
                #  Код возвращает все элементы, если указано `if_list = 'all'`
                if selector2:
                    elements = self.driver.find_elements(by_type, selector)
                    elements = elements if elements else self.driver.find_elements(by_type, selector2)
                else:
                    elements = self.driver.find_elements(by_type, selector)
                return elements
            else:
                 #  Код возвращает найденный элемент
                 return element
            
        except TimeoutException as ex:
                #  Код логирует ошибку, если элемент не найден за отведенное время
            logger.error(f'Элемент не найден по локатору {locator=}', exc_info=ex)
            if mandatory:
                 logger.error(f'Элемент по локатору {locator=} обязателен')
                 raise ExecuteLocatorException (f'Элемент не найден по локатору {locator=}')

            return False
        except Exception as ex:
             #  Код логирует ошибку при возникновении других исключений
             logger.error(f'Ошибка при поиске элемента по локатору {locator=}', exc_info=ex)
             return False

    def get_attribute_by_locator(self, locator: Dict | SimpleNamespace, message: str = None) -> Union[str, list, dict, bool]:
        """
        Получает атрибут элемента(ов) на основе заданного локатора.

        :param locator: Словарь или SimpleNamespace с параметрами локатора.
        :type locator: dict | SimpleNamespace
        :param message: Сообщение для логирования.
        :type message: str, optional
        :return: Значение атрибута, список значений, словарь или False в случае ошибки.
        :rtype: Union[str, list, dict, bool]
        """
        element = self.get_webelement_by_locator(locator, message)
        attribute = locator.get('attribute')
        if not element or not attribute:
            logger.error(f'Не удалось получить элемент или атрибут. {element=}, {attribute=}')
            return False

        try:
             #  Код обрабатывает случай, когда элемент является списком
            if isinstance(element, list):
                return [self._get_element_attribute(el, attribute) for el in element]
            #  Код получает атрибут, если элемент один
            return self._get_element_attribute(element, attribute)
        except Exception as ex:
             #  Код логирует ошибку при получении атрибута
             logger.error(f'Ошибка при получении атрибута элемента {attribute=}', exc_info=ex)
             return False

    def _get_element_attribute(self, element: WebElement, attribute: str) -> Union[str, None]:
        """
        Получает значение конкретного атрибута элемента.

        :param element: Веб-элемент.
        :type element: selenium.webdriver.remote.webelement.WebElement
        :param attribute: Имя атрибута.
        :type attribute: str
        :return: Значение атрибута или None, если атрибут не найден.
        :rtype: Union[str, None]
        """
        try:
            #  Код возвращает значение атрибута элемента
            return element.get_attribute(attribute)
        except Exception as ex:
             #  Код логирует ошибку, если атрибут не найден
             logger.error(f'Не удалось получить атрибут {attribute=}', exc_info=ex)
             return None
    
    def send_message(self, locator: Dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool:
        """
        Отправляет сообщение в веб-элемент.

        :param locator: Словарь или SimpleNamespace с параметрами локатора.
        :type locator: dict | SimpleNamespace
        :param message: Сообщение для отправки.
        :type message: str
        :param typing_speed: Скорость набора текста.
        :type typing_speed: float
         :param continue_on_error: Флаг для продолжения выполнения при ошибке.
        :type continue_on_error: bool, optional
        :return: True, если отправка прошла успешно, иначе False.
        :rtype: bool
        """
        element = self.get_webelement_by_locator(locator)
        if not element:
            logger.error(f'Элемент не найден для отправки сообщения {locator=}')
            return False
        try:
             #  Код очищает поле перед отправкой сообщения
            element.clear()
            #  Код отправляет сообщение с заданной скоростью набора
            if typing_speed > 0:
                for char in message:
                    element.send_keys(char)
                    gs.sleep(typing_speed)
            else:
                element.send_keys(message)
                
            return True
        except Exception as ex:
             #  Код логирует ошибку при отправке сообщения
            logger.error(f'Ошибка при отправке сообщения {message=} в элемент {locator=}', exc_info=ex)
            if continue_on_error:
                return False
            raise
    
    def evaluate_locator(self, attribute: str | list | dict) -> str:
        """
        Оценивает значение атрибута локатора.

        :param attribute: Атрибут для оценки (строка, список или словарь).
        :type attribute: Union[str, list, dict]
        :return: Оцененное значение атрибута.
        :rtype: str
        """
        if isinstance(attribute, str):
            #  Код возвращает оцененное значение атрибута, если это строка
            return self._evaluate(attribute)
        if isinstance(attribute, list):
            #  Код преобразует список атрибутов к строке
            return  '\n'.join(map(str, (self._evaluate(attr) for attr in attribute if self._evaluate(attr))))
        if isinstance(attribute, dict):
            #  Код преобразует словарь атрибутов к строке
             return '\n'.join(f'{key}: {value}' for key, value in attribute.items() if value)
        
        return ''

    def _evaluate(self, attribute: str) -> Union[str, None]:
        """
        Оценивает значение одного атрибута.

        :param attribute: Атрибут для оценки.
        :type attribute: str
        :return: Оцененное значение атрибута или None.
        :rtype: Union[str, None]
        """
        try:
            #  Код возвращает значение атрибута, если оно не пустое
            return str(eval(attribute, {'element': self.driver.execute_script('return arguments[0]', self.driver.find_element(By.TAG_NAME,'body'))}))
        except Exception as ex:
             #  Код логирует ошибку при оценке атрибута
            logger.error(f'Ошибка при оценке атрибута {attribute=}', exc_info=ex)
            return None

    @staticmethod
    def get_locator_keys() -> list:
         """
        Возвращает список ключей локатора.

        :return: Список ключей локатора.
        :rtype: list
         """
         #  Код возвращает список ключей локатора
         return list(ExecuteLocator.by_mapping.keys())
```