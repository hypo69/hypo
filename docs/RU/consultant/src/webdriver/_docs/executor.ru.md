# Анализ кода модуля `executor.py`

**Качество кода**

7
-  Плюсы
    - Код хорошо структурирован, с использованием классов и методов для организации функциональности.
    - Присутствуют импорты необходимых библиотек и модулей.
    - Используется `logger` для логирования ошибок.
    - Есть разделение на методы для различных действий с веб-элементами.
-  Минусы
    - Отсутствует документация к классам, методам и атрибутам.
    - Используется `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Код использует стандартные блоки `try-except`, которые можно заменить на `logger.error`.
    - Используется `pprint` вместо `logger.debug`.
    - Есть дублирование кода в некоторых методах.
    - Не все комментарии соответствуют стандарту оформления docstring в Python (для Sphinx).
    - Имена переменных и функций не стандартизированы и требуют приведения в соответствие с общим стилем проекта.
    - Отсутствует проверка типов при получении аргументов.
    - В коде не производится проверка существования методов и ключей в словарях.
    - Не используется `Path` вместо `str` для работы с путями.
    - Отсутствуют примеры документации RST.
    - Местами код не соответствует PEP8.

**Рекомендации по улучшению**

1.  **Документирование**: Добавить подробные docstring для класса `ExecuteLocator`, всех его методов и атрибутов, чтобы соответствовать стандартам оформления docstring в Python (для Sphinx).
2.  **Импорт `j_loads`**: Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3.  **Логирование ошибок**: Использовать `logger.error` для обработки исключений вместо стандартных блоков `try-except`, при этом сохраняя `...` для точек остановок.
4.  **Замена `pprint`**: Заменить `pprint` на `logger.debug`.
5.  **Рефакторинг**: Избегать дублирования кода, создать вспомогательные методы для повторяющихся действий.
6.  **Проверка типов**: Добавить проверку типов для входных параметров.
7.  **Проверка существования**: Проверять существование методов и ключей в словарях.
8.  **Использование `Path`**: Использовать `Path` вместо `str` для работы с путями.
9.  **Стандартизация имен**: Привести имена переменных, функций и импортов в соответствие с общим стилем проекта.
10. **Документация RST**: Добавить примеры документации RST.
11. **Соответствие PEP8**: Привести код в соответствие со стандартами PEP8.
12. **Контроль скорости печати**: Вынести ожидание между вводом символов в отдельную функцию.

**Оптимизированный код**

```python
"""
Модуль для выполнения действий с элементами веб-страницы с использованием Selenium WebDriver.
=========================================================================================

Этот модуль содержит класс :class:`ExecuteLocator`, который используется для выполнения навигационных
алгоритмов и взаимодействий с веб-страницей на основе конфигурационных данных,
которые предоставлены в виде словарей локаторов.

Пример использования
--------------------

Пример использования класса `ExecuteLocator`:

.. code-block:: python

    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator
    from src.logger import logger

    driver = webdriver.Chrome()
    executor = ExecuteLocator(driver=driver)
    locator = {
        'by': 'xpath',
        'selector': '//input[@id="login"]',
        'action': 'send_keys',
        'message': 'my_login',
    }
    executor.execute_locator(locator)
    driver.quit()
"""
from typing import Any, List, Union
from types import SimpleNamespace
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from src import gs
from src.utils.jjson import j_loads, j_loads_ns, j_dumps, save_png
from src.logger.logger import logger
from src.logger.exceptions import DefaultSettingsException, WebDriverException, ExecuteLocatorException


class ExecuteLocator:
    """
    Класс для выполнения действий с веб-элементами на основе локаторов.

    Args:
        driver (webdriver): Экземпляр WebDriver.

    Attributes:
        driver (webdriver): Экземпляр WebDriver.
        actions (ActionChains): Экземпляр ActionChains для выполнения сложных действий.
        by_mapping (dict): Словарь для преобразования строковых представлений локаторов в объекты Selenium By.
    """
    def __init__(self, driver: webdriver, *args, **kwargs) -> None:
        """Инициализирует экземпляр класса ExecuteLocator.

        Args:
            driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.actions = ActionChains(driver)
        self.by_mapping = {
            'xpath': By.XPATH,
            'css': By.CSS_SELECTOR,
            'id': By.ID,
            'class_name': By.CLASS_NAME,
            'name': By.NAME,
            'link_text': By.LINK_TEXT,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'tag_name': By.TAG_NAME
        }

    def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
        """Выполняет действия с веб-элементом на основе предоставленного локатора.

        Args:
            locator (dict): Словарь, содержащий параметры локатора.
                - 'by' (str): Тип локатора (например, 'xpath', 'css').
                - 'selector' (str): Строка-селектор для поиска элемента.
                - 'action' (str): Действие для выполнения (например, 'click', 'send_keys').
                - 'attribute' (str): Атрибут для получения (если применимо).
                - 'message' (str): Сообщение для отправки в поле ввода.
                - 'typing_speed' (float): Скорость набора текста при отправке сообщения.
                - 'if_list' (str): Индекс для обработки списка элементов ('first', 'all').
                - 'use_mouse' (bool): Использовать мышь при клике (если применимо).
                - 'timeout' (int): Время ожидания элемента.
                - 'timeout_for_event' (str): Событие для ожидания.
                - 'event' (str): Событие для отслеживания.
            message (str, optional): Сообщение для отправки в поле ввода.
            typing_speed (float, optional): Скорость набора текста при отправке сообщения.
            continue_on_error (bool, optional): Флаг для продолжения выполнения при ошибке.

        Returns:
            Union[str, list, dict, WebElement, bool]: Результат выполнения действия.

        Raises:
            ExecuteLocatorException: Если возникает ошибка при выполнении действия с локатором.
        """
        if not isinstance(locator, dict):
            logger.error(f'Локатор должен быть словарем, но получен {type(locator)}')
            return False

        action = locator.get('action')
        if not action:
            logger.error(f'Не указано действие в локаторе {locator}')
            return False

        try:
            if action == 'get_element':
                return self.get_webelement_by_locator(locator, message)
            elif action == 'get_attribute':
                return self.get_attribute_by_locator(locator, message)
            elif action == 'send_keys':
                return self.send_message(locator, message or locator.get('message', ''), typing_speed, continue_on_error)
            elif action in ['click', 'hover', 'double_click']:
                element = self.get_webelement_by_locator(locator)
                if not element:
                    return False
                return self._perform_action(element, action, locator.get('use_mouse', False))
            elif action == 'evaluate':
                return self.evaluate_locator(locator.get('attribute'))
            else:
                 logger.error(f'Неизвестное действие {action} в локаторе {locator}')
                 return False
        except Exception as ex:
            logger.error(f'Ошибка при выполнении действия {action} с локатором {locator}', exc_info=ex)
            if not continue_on_error:
                raise ExecuteLocatorException(f'Ошибка при выполнении действия {action} с локатором {locator}', ex) from ex
            return False

    def get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool:
        """Получает веб-элемент(ы) на основе предоставленного локатора.

        Args:
            locator (dict | SimpleNamespace): Словарь или объект SimpleNamespace, содержащий параметры локатора.
            message (str, optional): Сообщение для логирования.

        Returns:
            WebElement | List[WebElement] | bool: Найденный веб-элемент, список элементов или False в случае неудачи.
        """
        if not isinstance(locator, (dict, SimpleNamespace)):
           logger.error(f'Локатор должен быть словарем или SimpleNamespace, но получен {type(locator)}')
           return False
        
        by = locator.get('by')
        selector = locator.get('selector')
        if not by or not selector:
             logger.error(f'Не указан тип локатора или селектор {locator}')
             return False

        try:
            by_type = self.by_mapping.get(by)
            if not by_type:
                logger.error(f'Неизвестный тип локатора {by}')
                return False
                
            timeout = locator.get('timeout', 10)
            timeout_for_event = locator.get('timeout_for_event', 'presence_of_element_located')
            
            if timeout_for_event == 'presence_of_element_located':
                 element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by_type, selector)))
            elif timeout_for_event == 'visibility_of_element_located':
                element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by_type, selector)))
            elif timeout_for_event == 'element_to_be_clickable':
                element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by_type, selector)))
            else:
                element = self.driver.find_element(by_type, selector)

            if locator.get('if_list') == 'first':
                return element
            elif locator.get('if_list') == 'all':
                 return self.driver.find_elements(by_type, selector)
            return element
        except TimeoutException as ex:
             logger.error(f'Элемент не найден по локатору {locator} за {timeout} секунд', exc_info=ex)
             return False
        except NoSuchElementException as ex:
            logger.error(f'Элемент не найден по локатору {locator}', exc_info=ex)
            return False
        except Exception as ex:
           logger.error(f'Ошибка получения элемента по локатору {locator}', exc_info=ex)
           return False

    def get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool:
        """Получает атрибут(ы) веб-элемента на основе локатора.

        Args:
            locator (dict | SimpleNamespace): Словарь или объект SimpleNamespace, содержащий параметры локатора.
            message (str, optional): Сообщение для логирования.

        Returns:
            str | list | dict | bool: Значение атрибута, список значений атрибутов или False в случае ошибки.
        """
        if not isinstance(locator, (dict, SimpleNamespace)):
           logger.error(f'Локатор должен быть словарем или SimpleNamespace, но получен {type(locator)}')
           return False
        
        element = self.get_webelement_by_locator(locator)
        if not element:
            return False
        
        attribute = locator.get('attribute')
        if not attribute:
           logger.error(f'Не указан атрибут для получения в локаторе {locator}')
           return False

        try:
            if isinstance(element, list):
                return [self._get_element_attribute(el, attribute) for el in element]
            return self._get_element_attribute(element, attribute)
        except Exception as ex:
            logger.error(f'Ошибка получения атрибута {attribute} у элемента {element} по локатору {locator}', exc_info=ex)
            return False

    def _get_element_attribute(self, element: WebElement, attribute: str) -> str | None:
        """Получает значение атрибута веб-элемента.

        Args:
            element (WebElement): Веб-элемент.
            attribute (str): Имя атрибута.

        Returns:
            str | None: Значение атрибута или None, если атрибут не найден.
        """
        try:
            return element.get_attribute(attribute)
        except Exception as ex:
             logger.error(f'Ошибка получения атрибута {attribute} у элемента {element}', exc_info=ex)
             return None
    
    def _perform_action(self, element: WebElement, action: str, use_mouse: bool) -> bool:
        """Выполняет действие с веб-элементом.

        Args:
            element (WebElement): Веб-элемент.
            action (str): Тип действия ('click', 'hover', 'double_click').
            use_mouse (bool): Использовать мышь при клике.

        Returns:
            bool: True если действие выполнено успешно, иначе False.
        """
        try:
            if use_mouse:
                if action == 'click':
                     self.actions.move_to_element(element).click().perform()
                elif action == 'hover':
                    self.actions.move_to_element(element).perform()
                elif action == 'double_click':
                    self.actions.move_to_element(element).double_click().perform()
            else:
                if action == 'click':
                    element.click()
                elif action == 'hover':
                     self.actions.move_to_element(element).perform()
                elif action == 'double_click':
                    self.actions.double_click(element).perform()
            return True
        except Exception as ex:
            logger.error(f'Ошибка выполнения действия {action} с элементом {element}', exc_info=ex)
            return False
    
    def send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool:
        """Отправляет сообщение в поле ввода веб-элемента.

        Args:
            locator (dict | SimpleNamespace): Словарь или объект SimpleNamespace, содержащий параметры локатора.
            message (str): Сообщение для отправки.
            typing_speed (float): Скорость набора текста.
            continue_on_error (bool): Флаг для продолжения выполнения при ошибке.

        Returns:
            bool: True, если сообщение успешно отправлено, False в противном случае.
        """
        if not isinstance(locator, (dict, SimpleNamespace)):
           logger.error(f'Локатор должен быть словарем или SimpleNamespace, но получен {type(locator)}')
           return False

        element = self.get_webelement_by_locator(locator)
        if not element:
             return False
        try:
            element.clear()
            if typing_speed > 0:
                for char in message:
                     element.send_keys(char)
                     self.driver.implicitly_wait(typing_speed)
            else:
                element.send_keys(message)
            return True
        except Exception as ex:
             logger.error(f'Ошибка отправки сообщения {message} в элемент {element} по локатору {locator}', exc_info=ex)
             if not continue_on_error:
                raise ExecuteLocatorException(f'Ошибка отправки сообщения {message} в элемент {element} по локатору {locator}', ex) from ex
             return False
    
    def evaluate_locator(self, attribute: str | list | dict) -> str:
       """Оценивает значение атрибута, возвращая его строковое представление.

       Args:
           attribute (str | list | dict): Атрибут для оценки.

       Returns:
           str: Строковое представление атрибута.
       """
       if isinstance(attribute, str):
            return self._evaluate(attribute) or ''
       if isinstance(attribute, list):
            return  ' '.join(filter(None, [self._evaluate(item) for item in attribute]))
       if isinstance(attribute, dict):
           return j_dumps({key: self._evaluate(value) for key, value in attribute.items()})
       return ''

    def _evaluate(self, attribute: str) -> str | None:
        """Вспомогательный метод для оценки одного атрибута.

        Args:
           attribute (str): Атрибут для оценки.

        Returns:
           str | None: Значение атрибута или None, если атрибут не найден.
        """
        try:
            if attribute.startswith('gs.'):
                return str(eval(attribute))
            return attribute
        except Exception as ex:
            logger.error(f'Ошибка при оценки значения {attribute}', exc_info=ex)
            return None

    @staticmethod
    def get_locator_keys() -> list:
        """Возвращает список ключей, которые могут быть использованы в локаторах.

        Returns:
            list: Список ключей.
        """
        return ['by', 'selector', 'action', 'attribute', 'message', 'typing_speed',
                'if_list', 'use_mouse', 'timeout', 'timeout_for_event', 'event']
```