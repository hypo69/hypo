# Анализ кода модуля `executor.py`

**Качество кода: 7**

-   **Плюсы**
    -   Код хорошо структурирован, класс `ExecuteLocator` чётко выполняет свою задачу по взаимодействию с веб-элементами.
    -   Используются `ActionChains` для выполнения сложных действий.
    -   Присутствует обработка исключений, связанных с Selenium, что повышает устойчивость кода.
    -   Используется логгер для записи ошибок и отладочной информации.
    -   Есть примеры использования, что облегчает понимание работы кода.

-   **Минусы**
    -   Отсутствуют docstring для классов, методов, что затрудняет понимание назначения кода.
    -   Используется `try-except` без конкретизации исключений, что может привести к скрытию ошибок.
    -   В некоторых методах, например `execute_locator`, используется много условных переходов, что усложняет чтение кода.
    -   Не используется `j_loads` или `j_loads_ns` для загрузки JSON данных, хотя это указано в инструкции.
    -   Не все ошибки логируются с помощью `logger.error`.
    -   Не везде используется f-строки для форматирования логов.
    -   Много `...` для пропуска кода, что затрудняет анализ.

**Рекомендации по улучшению**

1.  **Документация:**
    -   Добавить docstring к классу `ExecuteLocator` и всем его методам.
    -   Использовать reStructuredText (RST) для оформления docstring.
2.  **Обработка ошибок:**
    -   Использовать `logger.error` для логирования исключений вместо стандартного `try-except` в случаях, где это возможно.
    -   Конкретизировать исключения в блоках `try-except`.
3.  **Использование `j_loads`:**
    -   Использовать `j_loads` или `j_loads_ns` для чтения данных, где это необходимо.
4.  **Улучшение читаемости:**
    -   Разбить метод `execute_locator` на несколько более мелких, чтобы уменьшить его сложность.
    -   Использовать f-строки для форматирования логов.
5.  **Логирование:**
    -   Добавить логирование в начале и в конце выполнения методов для отслеживания последовательности выполнения.
    -   Логировать переменные, передаваемые в метод.
6.  **Удаление `...`:**
    -   Убрать точки остановки `...` для полного анализа кода.
7.  **Импорты:**
    -  Импортировать `SimpleNamespace` из `types`.
    -  Убедиться что все импорты используються

**Оптимизированный код**

```python
"""
Модуль для выполнения действий с веб-элементами с использованием Selenium WebDriver.
==================================================================================

Этот модуль содержит класс :class:`ExecuteLocator`, который используется для выполнения
различных действий с веб-элементами на основе переданных локаторов.

Пример использования
--------------------

Пример использования класса `ExecuteLocator`:

.. code-block:: python

    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator

    driver = webdriver.Chrome()
    executor = ExecuteLocator(driver)
    locator = {
        "by": "xpath",
        "selector": "//h1",
    }
    element = executor.get_webelement_by_locator(locator)
    if element:
        print(f"Нашли элемент: {element.text}")
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
from src import gs
from src.utils.printer import pprint, j_loads, j_loads_ns, j_dumps, save_png
from src.logger.logger import logger
from src.logger.exceptions import DefaultSettingsException, WebDriverException, ExecuteLocatorException


class ExecuteLocator:
    """
    Класс для выполнения действий с веб-элементами на основе локаторов.
    """
    def __init__(self, driver: webdriver.Chrome, *args, **kwargs):
        """
        Инициализирует экземпляр класса ExecuteLocator.

        :param driver: Экземпляр WebDriver.
        :param args: Дополнительные аргументы.
        :param kwargs: Дополнительные именованные аргументы.
        """
        self.driver = driver
        self.actions = ActionChains(driver)
        self.by_mapping = {
            "id": By.ID,
            "xpath": By.XPATH,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "name": By.NAME,
            "tag_name": By.TAG_NAME,
            "class_name": By.CLASS_NAME,
            "css_selector": By.CSS_SELECTOR,
        }
        logger.debug(f"Инициализирован {self.__class__.__name__} с {driver=}")

    def execute_locator(self, locator: Dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
        """
        Выполняет действие на веб-элементе на основе переданного локатора.

        :param locator: Словарь с параметрами локатора.
        :param message: Сообщение для отправки элементу, если необходимо.
        :param typing_speed: Скорость печати сообщения (если применяется).
        :param continue_on_error: Продолжать ли выполнение при ошибке.
        :return: Результат выполнения действия (текст, список, элемент, или bool).
        """
        logger.debug(f"Вызван execute_locator с {locator=}, {message=}, {typing_speed=}, {continue_on_error=}")
        if not locator:
            logger.error('Локатор не определен')
            return False

        action = locator.get("action")
        attribute = locator.get("attribute")

        try:
            if action == 'send_keys' and message:
                return self.send_message(locator, message, typing_speed, continue_on_error)
            elif action == 'click()':
                 return self.click(locator, continue_on_error)
            elif attribute:
                return self.get_attribute_by_locator(locator, message)
            else:
                 return self.get_webelement_by_locator(locator, message)
        except Exception as ex:
            logger.error(f"Ошибка при выполнении локатора {locator=}: {ex}", exc_info=True)
            if not continue_on_error:
                raise ExecuteLocatorException(f"Ошибка при выполнении локатора: {ex}")
            return False
        finally:
            logger.debug(f"Завершено выполнение  execute_locator с {locator=}, {message=}, {typing_speed=}, {continue_on_error=}")

    def get_webelement_by_locator(self, locator: Dict | SimpleNamespace, message: str = None) -> Union[WebElement, List[WebElement], bool]:
        """
        Получает веб-элемент(ы) по заданному локатору.

        :param locator: Словарь или SimpleNamespace с параметрами локатора.
        :param message: Сообщение для логирования.
        :return: Веб-элемент, список веб-элементов или False.
        """
        logger.debug(f"Вызван get_webelement_by_locator с {locator=}, {message=}")
        if not locator:
            logger.error('Локатор не определен')
            return False
        
        if isinstance(locator, SimpleNamespace):
            locator = locator.__dict__
        
        by = locator.get("by")
        selector = locator.get("selector")
        selector_2 = locator.get("selector 2")
        timeout = locator.get("timeout", 10)
        timeout_for_event = locator.get("timeout_for_event", "presence_of_element_located")
        if_list = locator.get("if_list")
        use_mouse = locator.get("use_mouse", False)


        if not by or not selector:
            logger.error(f'Неверный локатор {locator=}')
            return False
        
        by_method = self.by_mapping.get(by)
        if not by_method:
           logger.error(f'Неизвестный метод поиска: {by=}')
           return False
        try:
             wait = WebDriverWait(self.driver, timeout)
             if timeout_for_event == 'presence_of_element_located':
                 elements = wait.until(EC.presence_of_all_elements_located((by_method, selector)))
             elif timeout_for_event == 'element_to_be_clickable':
                 elements = wait.until(EC.element_to_be_clickable((by_method, selector)))
             else:
                 logger.error(f'Неизвестное событие ожидания: {timeout_for_event=}')
                 return False

        except (NoSuchElementException, TimeoutException) as ex:
            logger.error(f"Элемент не найден: {selector=}, {by=}: {ex}", exc_info=True)
            if selector_2:
                try:
                    if timeout_for_event == 'presence_of_element_located':
                        elements = wait.until(EC.presence_of_all_elements_located((by_method, selector_2)))
                    elif timeout_for_event == 'element_to_be_clickable':
                        elements = wait.until(EC.element_to_be_clickable((by_method, selector_2)))
                    else:
                       logger.error(f'Неизвестное событие ожидания: {timeout_for_event=}')
                       return False
                except (NoSuchElementException, TimeoutException) as ex:
                    logger.error(f"Элемент не найден: {selector_2=}, {by=}: {ex}", exc_info=True)
                    return False
            else:
                return False
        except Exception as ex:
             logger.error(f"Ошибка при поиске элемента {selector=}, {by=}: {ex}", exc_info=True)
             return False
             
        if not elements:
            logger.debug(f'Элемент не найден {locator=}')
            return False

        if if_list == 'first':
            logger.debug(f'Возвращен первый элемент {locator=}')
            return elements[0]
        
        logger.debug(f'Возвращен список элементов {locator=}')
        return elements
    
    def get_attribute_by_locator(self, locator: Dict | SimpleNamespace, message: str = None) -> Union[str, list, dict, bool]:
        """
        Получает атрибут элемента(ов) по заданному локатору.

        :param locator: Словарь или SimpleNamespace с параметрами локатора.
        :param message: Сообщение для логирования.
        :return: Значение атрибута, список значений, словарь или False.
        """
        logger.debug(f"Вызван get_attribute_by_locator с {locator=}, {message=}")
        if not locator:
            logger.error('Локатор не определен')
            return False

        if isinstance(locator, SimpleNamespace):
           locator = locator.__dict__
        
        attribute = locator.get("attribute")
        if not attribute:
            logger.error(f'Атрибут не определен {locator=}')
            return False
        
        elements = self.get_webelement_by_locator(locator, message)

        if not elements:
            logger.debug(f'Элементы не найдены {locator=}')
            return False
        try:
            if isinstance(elements, list):
                if isinstance(attribute, list):
                    result = []
                    for element in elements:
                        element_attr = {}
                        for attr in attribute:
                            element_attr[attr] = self._get_element_attribute(element, attr)
                        result.append(element_attr)
                    return result
                else:
                   return [self._get_element_attribute(element, attribute) for element in elements]
            else:
                return self._get_element_attribute(elements, attribute)
        except Exception as ex:
            logger.error(f"Ошибка при получении атрибута {attribute=}, {locator=}: {ex}", exc_info=True)
            return False
        finally:
            logger.debug(f"Завершено выполнение get_attribute_by_locator c {locator=}, {message=}")

    def _get_element_attribute(self, element: WebElement, attribute: str) -> Union[str, None]:
        """
        Получает значение атрибута у веб-элемента.

        :param element: Веб-элемент.
        :param attribute: Название атрибута.
        :return: Значение атрибута или None.
        """
        try:
            value = element.get_attribute(attribute)
            logger.debug(f"Получен атрибут {attribute=} со значением: {value=}")
            return value
        except Exception as ex:
             logger.error(f"Ошибка при получении атрибута {attribute=} элемента {element=}: {ex}", exc_info=True)
             return None

    def send_message(self, locator: Dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error: bool) -> bool:
        """
        Отправляет сообщение в веб-элемент.

        :param locator: Словарь или SimpleNamespace с параметрами локатора.
        :param message: Сообщение для отправки.
        :param typing_speed: Скорость печати сообщения.
        :param continue_on_error: Продолжать ли выполнение при ошибке.
        :return: True, если сообщение отправлено успешно, иначе False.
        """
        logger.debug(f"Вызван send_message с {locator=}, {message=}, {typing_speed=}, {continue_on_error=}")

        if not locator:
           logger.error('Локатор не определен')
           return False

        if isinstance(locator, SimpleNamespace):
            locator = locator.__dict__

        element = self.get_webelement_by_locator(locator)
        if not element:
            logger.debug('Элемент для отправки сообщения не найден')
            return False

        try:
            if typing_speed > 0:
                for char in message:
                   element.send_keys(char)
                   import time
                   time.sleep(typing_speed)
            else:
                element.send_keys(message)
            logger.debug(f"Сообщение '{message}' отправлено в элемент {locator=}")
            return True
        except Exception as ex:
             logger.error(f"Ошибка при отправке сообщения '{message}' в элемент {locator=}: {ex}", exc_info=True)
             if not continue_on_error:
                raise ExecuteLocatorException(f"Ошибка при отправке сообщения: {ex}")
             return False
        finally:
            logger.debug(f"Завершено выполнение send_message с {locator=}, {message=}, {typing_speed=}, {continue_on_error=}")


    def evaluate_locator(self, attribute: Union[str, list, dict]) -> Union[str, None]:
        """
        Оценивает атрибут локатора, заменяя плейсхолдеры.

        :param attribute: Атрибут локатора (строка, список или словарь).
        :return: Оцененный атрибут (строка) или None, если атрибут не строка.
        """
        logger.debug(f"Вызван evaluate_locator с {attribute=}")
        try:
            if isinstance(attribute, str):
               return self._evaluate(attribute)
            elif isinstance(attribute, list):
                return [self._evaluate(item) for item in attribute]
            elif isinstance(attribute, dict):
                result = {}
                for key, value in attribute.items():
                    result[key] = self._evaluate(value)
                return result
            else:
                logger.error(f"Неверный тип атрибута: {type(attribute)=}")
                return None
        except Exception as ex:
            logger.error(f"Ошибка при оценке локатора {attribute=}: {ex}", exc_info=True)
            return None
        finally:
            logger.debug(f"Завершено выполнение evaluate_locator c {attribute=}")


    def _evaluate(self, attribute: str) ->  Union[str, None]:
        """
        Оценивает единичный атрибут, заменяя плейсхолдеры.

        :param attribute: Атрибут локатора (строка).
        :return: Оцененный атрибут (строка) или None.
        """
        if not isinstance(attribute, str):
             logger.error(f"Атрибут не строка: {attribute=}")
             return None
        logger.debug(f"Вызван _evaluate с {attribute=}")
        if "%EXTERNAL_MESSAGE%" in attribute:
           message = gs.get('message')
           attribute = attribute.replace("%EXTERNAL_MESSAGE%", message if message else '')
           logger.debug(f"Атрибут после замены {attribute=}")
        return attribute

    def click(self, locator: Dict | SimpleNamespace, continue_on_error: bool) -> bool:
        """
        Выполняет клик по веб-элементу.

        :param locator: Словарь или SimpleNamespace с параметрами локатора.
        :param continue_on_error: Продолжать ли выполнение при ошибке.
        :return: True, если клик выполнен успешно, иначе False.
        """
        logger.debug(f"Вызван click с {locator=}, {continue_on_error=}")

        if not locator:
            logger.error('Локатор не определен')
            return False

        if isinstance(locator, SimpleNamespace):
            locator = locator.__dict__

        element = self.get_webelement_by_locator(locator)
        if not element:
            logger.error('Элемент для клика не найден')
            return False

        try:
            self.actions.move_to_element(element).click().perform()
            logger.debug(f"Клик выполнен по элементу {locator=}")
            return True
        except Exception as ex:
            logger.error(f"Ошибка при клике по элементу {locator=}: {ex}", exc_info=True)
            if not continue_on_error:
                raise ExecuteLocatorException(f"Ошибка при клике: {ex}")
            return False
        finally:
            logger.debug(f"Завершено выполнение click с {locator=}, {continue_on_error=}")


    @staticmethod
    def get_locator_keys() -> list:
        """
        Возвращает список доступных ключей локаторов.

        :return: Список ключей локаторов.
        """
        return [
            "attribute",
            "by",
            "selector",
            "selector 2",
            "if_list",
            "use_mouse",
            "mandatory",
            "timeout",
            "timeout_for_event",
            "event",
            "action",
            "locator_description"
        ]