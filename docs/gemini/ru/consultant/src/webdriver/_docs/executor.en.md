# Анализ кода модуля `executor`

**Качество кода: 8/10**

- **Плюсы:**
    - Код хорошо структурирован и разделен на методы, каждый из которых выполняет определенную задачу.
    - Используются стандартные библиотеки Selenium для взаимодействия с браузером.
    - Присутствует обработка исключений, что повышает устойчивость кода.
    - Используется `ActionChains` для выполнения сложных действий.
    - Есть примеры конфигурационных данных в формате JSON.
    - Документация модуля в целом полная, даёт общее представление о работе класса `ExecuteLocator`
- **Минусы:**
    - Некоторые docstring отсутствуют, например, у методов `_get_element_attribute`, `_evaluate` и `get_locator_keys`.
    - Не все методы имеют подробные описания в формате RST.
    - Есть избыточное использование `try-except` блоков, которые можно заменить на `logger.error`.
    - Необходимо добавить комментарии для описания логики работы каждого блока кода.
    - Использование `SimpleNamespace` в качестве одного из типов входных данных не документировано, следует использовать `dict` или  `Mapping`
    - Необходимо добавить импорты `Union`, `List`, `Any`, `Dict`, `SimpleNamespace`, `Path`, `Mapping`
    - Для улучшения читаемости следует использовать `from selenium.webdriver.common.by import By`
    - Отсутствует документация для переменных класса `driver`, `actions`, `by_mapping`
    - В примере не используется `ExecuteLocator`

**Рекомендации по улучшению:**

1. **Документация:**
    - Добавить docstring в формате RST для всех методов и переменных, включая `_get_element_attribute`, `_evaluate` и `get_locator_keys`.
    - Документировать все входные и выходные параметры, а так же возможные ошибки.
    - Описать каждый метод, что он делает, какие есть условия для его выполнения.
    - Привести в соответствие примеры кода в документации с фактическим кодом.

2. **Логирование:**
    - Использовать `logger.error` вместо стандартных `try-except` блоков, где это возможно, для упрощения кода и улучшения логирования ошибок.
    - Добавить информативные сообщения в логи для отслеживания хода выполнения кода.

3. **Импорты:**
    - Явно указать все необходимые импорты, включая `Union`, `List`, `Any`, `Dict`, `SimpleNamespace`, `Path`, `Mapping` и `from selenium.webdriver.common.by import By`.
    - Избегать импорта `from src import gs`

4. **Типизация:**
     - Добавить аннотации типов для переменных и возвращаемых значений, где это возможно.
     - Использовать `Mapping` вместо `SimpleNamespace`

5. **Комментарии:**
     - Добавить подробные комментарии к каждому блоку кода, объясняя его логику и назначение.

6. **Рефакторинг:**
    - Упростить сложные конструкции, где это возможно.

7. **Примеры:**
    - Добавить в документацию примеры использования класса `ExecuteLocator` и его методов.

**Оптимизированный код:**

```python
"""
Модуль для выполнения действий с элементами веб-страницы с использованием Selenium WebDriver.
=========================================================================================

Этот модуль содержит класс :class:`ExecuteLocator`, который используется для выполнения
различных действий с элементами веб-страницы на основе словаря локаторов.

Пример использования
--------------------

Пример использования класса `ExecuteLocator`:

.. code-block:: python

    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator
    from src.logger.logger import logger

    driver = webdriver.Chrome()
    executor = ExecuteLocator(driver)
    locator = {
        'by': 'xpath',
        'selector': '//button[@id="myButton"]',
        'action': 'click()',
    }
    try:
        result = executor.execute_locator(locator)
        if result:
            logger.info("Элемент успешно найден и действие выполнено")
    except Exception as e:
        logger.error(f"Ошибка при выполнении локатора: {e}")
    finally:
        driver.quit()

"""
from typing import Union, List, Any, Dict, Mapping
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# from src import gs # удален неиспользуемый импорт
from src.utils.printer import pprint, j_loads, j_loads_ns, j_dumps, save_png
from src.logger.logger import logger
from src.logger.exceptions import DefaultSettingsException, WebDriverException, ExecuteLocatorException
from types import SimpleNamespace

class ExecuteLocator:
    """
    Класс для выполнения действий с элементами веб-страницы на основе словаря локаторов.

    Args:
        driver (webdriver): Экземпляр WebDriver для взаимодействия с браузером.

    Attributes:
        driver (webdriver): Экземпляр WebDriver для взаимодействия с браузером.
        actions (ActionChains): Экземпляр ActionChains для выполнения сложных действий.
        by_mapping (dict): Словарь, который связывает строковые представления локаторов с объектами By Selenium.
    """
    by_mapping = {
        'id': By.ID,
        'name': By.NAME,
        'xpath': By.XPATH,
        'link_text': By.LINK_TEXT,
        'partial_link_text': By.PARTIAL_LINK_TEXT,
        'tag_name': By.TAG_NAME,
        'class_name': By.CLASS_NAME,
        'css_selector': By.CSS_SELECTOR,
    }

    def __init__(self, driver: webdriver, *args, **kwargs) -> None:
        """
        Инициализирует экземпляр класса ExecuteLocator.

        Args:
            driver (webdriver): Экземпляр WebDriver для взаимодействия с браузером.
        """
        self.driver = driver
        self.actions = ActionChains(driver)

    def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
        """
        Выполняет действие на основе переданного словаря локаторов.

        Args:
            locator (dict): Словарь с параметрами для выполнения действий.
                Пример:
                {
                    'by': 'xpath',
                    'selector': '//button[@id="myButton"]',
                    'action': 'click()',
                    'attribute': 'href'
                    'message': 'текст для ввода',
                    'typing_speed': 0.1
                    'timeout': 10,
                    'timeout_for_event': "presence_of_element_located"
                }
            message (str, optional): Сообщение для отправки в элемент.
            typing_speed (float, optional): Скорость печати сообщения (в секундах).
            continue_on_error (bool, optional): Флаг, указывающий, следует ли продолжать выполнение при ошибке.

        Returns:
            Union[str, list, dict, WebElement, bool]: Результат выполнения действия,
                либо значение атрибута, либо список элементов, либо WebElement, либо `True`,
                либо `False` в случае неудачи.
        """
        # Код проверяет, что переданный локатор является словарем
        if not isinstance(locator, dict):
            logger.error(f"Локатор должен быть словарем, получен {type(locator)}")
            return False

        pprint(f"Execute locator: {locator=}")
        action = locator.get('action')

        if not action:
            # Код выполняет получение элемента, если действие не указано
            return self.get_webelement_by_locator(locator, message)
        if "send_keys" in action:
            # Код выполняет отправку сообщения, если действие содержит "send_keys"
            return self.send_message(locator, message, typing_speed, continue_on_error)
        if "get_attribute" in action:
            # Код получает значение атрибута, если действие содержит "get_attribute"
            return self.get_attribute_by_locator(locator, message)
        if "click" in action:
            # Код выполняет клик по элементу, если действие содержит "click"
            return self.click(locator, message)
        if "get_screenshot" in action:
            # Код получает скриншот элемента, если действие содержит "get_screenshot"
            return self.get_webelement_as_screenshot(locator, message)

        logger.error(f"Неизвестное действие: {action=}")
        return False

    def get_webelement_by_locator(self, locator: dict | Mapping, message: str = None) -> WebElement | List[WebElement] | bool:
        """
        Получает веб-элемент(ы) по заданному локатору.

        Args:
            locator (dict | Mapping): Словарь с параметрами локатора.
            message (str, optional): Сообщение для логирования.

        Returns:
            WebElement | List[WebElement] | bool: Найденный веб-элемент(ы) или `False`, если элемент(ы) не найден(ы).
        """
        # Код проверяет, что локатор является словарем или Mapping
        if not isinstance(locator, (dict, Mapping)):
            logger.error(f"Локатор должен быть словарем или Mapping, получен {type(locator)}")
            return False

        by_value = locator.get('by')
        selector = locator.get('selector')
        selector_2 = locator.get('selector 2')
        timeout = locator.get('timeout', 10)
        timeout_for_event = locator.get('timeout_for_event', "presence_of_element_located")
        if_list = locator.get('if_list')
        mandatory = locator.get('mandatory', True)

        # Код проверяет наличие обязательных ключей
        if not all([by_value, selector]):
            logger.error(f"Не указаны обязательные ключи 'by' и 'selector' в локаторе: {locator=}")
            return False

        if by_value not in self.by_mapping:
            logger.error(f"Неизвестный тип локатора: {by_value=}")
            return False
        
        by = self.by_mapping[by_value]

        try:
            # Код ожидает появления элемента на странице
            element = WebDriverWait(self.driver, timeout).until(
                getattr(EC, timeout_for_event)((by, selector))
            )
            # Проверяем если элемент нужно получить из списка, получаем его по индексу
            if if_list == 'first':
                 return self.driver.find_elements(by, selector)[0]
            if if_list == 'last':
                return self.driver.find_elements(by, selector)[-1]
            # Если нужно получить список, возвращаем его
            return self.driver.find_elements(by, selector)
        except TimeoutException:
            # Код обрабатывает ситуацию, когда элемент не найден в течение таймаута
            if mandatory:
                 logger.error(f"Элемент не найден по локатору: {locator=} timeout: {timeout=}  timeout_for_event: {timeout_for_event=}")
                 return False
            else:
                logger.debug(f"Элемент не найден по локатору: {locator=} timeout: {timeout=}  timeout_for_event: {timeout_for_event=}")
                return False

        except Exception as e:
           # Код обрабатывает другие исключения
            logger.error(f"Ошибка при поиске элемента: {locator=}", e)
            return False

    def get_attribute_by_locator(self, locator: dict | Mapping, message: str = None) -> str | list | dict | bool:
        """
        Получает значение атрибута элемента(-ов) по локатору.

        Args:
            locator (dict | Mapping): Словарь с параметрами локатора.
            message (str, optional): Сообщение для логирования.

        Returns:
             str | list | dict | bool: Значение атрибута или `False`, если элемент не найден.
        """
        # Код проверяет, что локатор является словарем или Mapping
        if not isinstance(locator, (dict, Mapping)):
           logger.error(f"Локатор должен быть словарем или Mapping, получен {type(locator)}")
           return False

        element_or_elements = self.get_webelement_by_locator(locator, message)
        attribute = locator.get('attribute')
        # Проверяем что есть атрибут который нужно получить
        if not attribute:
            logger.error(f'Не указан атрибут для получения {locator=}')
            return False
        # Если результат поиска элемент, получаем его атрибут
        if isinstance(element_or_elements, WebElement):
            return self._get_element_attribute(element_or_elements, attribute)
        # Если результат поиска список, получаем атрибут у каждого элемента
        if isinstance(element_or_elements, list):
            return [self._get_element_attribute(element, attribute) for element in element_or_elements]
        # В случае если элемент не найден, возвращаем False
        return element_or_elements

    def _get_element_attribute(self, element: WebElement, attribute: str) -> str | None:
        """
        Получает значение атрибута элемента.

        Args:
            element (WebElement): Веб-элемент, у которого нужно получить атрибут.
            attribute (str): Имя атрибута.

        Returns:
            str | None: Значение атрибута или None, если атрибут не найден.
        """
        try:
             # Код получает значение атрибута
            return element.get_attribute(attribute)
        except Exception as e:
            logger.error(f"Не удалось получить значение атрибута {attribute=} у элемента {element=}", e)
            return None

    def send_message(self, locator: dict | Mapping, message: str, typing_speed: float, continue_on_error:bool) -> bool:
        """
        Отправляет сообщение в веб-элемент.

        Args:
            locator (dict | Mapping): Словарь с параметрами локатора.
            message (str): Сообщение для отправки.
            typing_speed (float): Скорость печати сообщения (в секундах).
            continue_on_error (bool): Флаг, указывающий, продолжать ли выполнение при ошибке.
        Returns:
             bool: True если сообщение отправлено успешно, иначе False.
        """
        # Код проверяет, что локатор является словарем или Mapping
        if not isinstance(locator, (dict, Mapping)):
           logger.error(f"Локатор должен быть словарем или Mapping, получен {type(locator)}")
           return False

        element = self.get_webelement_by_locator(locator)
        if not element:
            logger.error(f"Элемент не найден для отправки сообщения {locator=}")
            return False
        try:
            # Код эмулирует ввод сообщения
            for char in message:
                element.send_keys(char)
                import time
                time.sleep(typing_speed)
            return True
        except Exception as e:
             # Код обрабатывает исключения при отправке сообщения
            logger.error(f"Ошибка при отправке сообщения: {message=} {locator=}", e)
            return False

    def evaluate_locator(self, attribute: str | list | dict) -> str:
        """
        Оценивает значение атрибута локатора.

        Args:
             attribute (str | list | dict): Атрибут локатора.

        Returns:
             str: Оцененное значение атрибута.
        """
        if isinstance(attribute, str):
            # Код оценивает атрибут если это строка
            return self._evaluate(attribute)
        if isinstance(attribute, list):
             # Код рекурсивно оценивает атрибуты, если это список
            return [self._evaluate(item) for item in attribute]
        if isinstance(attribute, dict):
            # Код рекурсивно оценивает атрибуты, если это словарь
            return {key: self._evaluate(value) for key, value in attribute.items()}
        return str(attribute)

    def _evaluate(self, attribute: str) -> str | None:
        """
        Оценивает значение одного атрибута.

        Args:
            attribute (str): Атрибут для оценки.

        Returns:
            str | None: Оцененное значение атрибута или None, если атрибут не найден.
        """
        if "%EXTERNAL_MESSAGE%" in attribute:
            # Код обрабатывает случай, когда атрибут содержит плейсхолдер "%EXTERNAL_MESSAGE%"
            return "EXTERNAL_MESSAGE"
        return attribute

    @staticmethod
    def get_locator_keys() -> list:
        """
        Возвращает список доступных ключей локатора.

        Returns:
            list: Список ключей локатора.
        """
        return list(ExecuteLocator.by_mapping.keys())

    def click(self, locator: dict | Mapping, message: str = None) -> bool:
        """
         Выполняет клик по элементу, найденному по локатору.

        Args:
            locator (dict | Mapping): Словарь с параметрами локатора.
            message (str, optional): Сообщение для логирования.

        Returns:
            bool: True, если клик успешен, False в противном случае.
        """
        # Код проверяет, что локатор является словарем или Mapping
        if not isinstance(locator, (dict, Mapping)):
           logger.error(f"Локатор должен быть словарем или Mapping, получен {type(locator)}")
           return False

        element = self.get_webelement_by_locator(locator, message)
        if not element:
            logger.error(f"Элемент не найден для клика: {locator=}")
            return False
        try:
            # Код выполняет клик по элементу
            element.click()
            return True
        except Exception as e:
           # Код обрабатывает исключения при клике
            logger.error(f"Не удалось выполнить клик по элементу {locator=}", e)
            return False

    def get_webelement_as_screenshot(self, locator: dict | Mapping, message: str = None) -> str | bool:
        """
        Делает скриншот веб-элемента(ов).

        Args:
            locator (dict | Mapping): Словарь с параметрами локатора.
             message (str, optional): Сообщение для логирования.
        Returns:
             str | bool: Путь к скриншоту или `False` в случае ошибки.
        """
        # Код проверяет, что локатор является словарем или Mapping
        if not isinstance(locator, (dict, Mapping)):
            logger.error(f"Локатор должен быть словарем или Mapping, получен {type(locator)}")
            return False

        element_or_elements = self.get_webelement_by_locator(locator, message)
        if not element_or_elements:
            logger.error(f"Элемент не найден для получения скриншота: {locator=}")
            return False

        try:
            # Код создает скриншот элемента
            if isinstance(element_or_elements, WebElement):
                 return save_png(element_or_elements)
            if isinstance(element_or_elements, list):
                return [save_png(element) for element in element_or_elements ]
            return False

        except Exception as e:
           # Код обрабатывает исключения при создании скриншота
            logger.error(f"Не удалось получить скриншот элемента {locator=}", e)
            return False
```