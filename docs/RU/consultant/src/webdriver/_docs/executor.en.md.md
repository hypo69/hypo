## Анализ кода модуля `executor.py`

**Качество кода:** 8/10
- **Плюсы:**
    - Код хорошо структурирован и разбит на логические блоки, что упрощает понимание и поддержку.
    - Используются аннотации типов, что повышает читаемость и помогает в отладке.
    - Присутствуют подробные комментарии, объясняющие назначение каждого метода и класса.
    - Реализована обработка ошибок с использованием try-except блоков, хотя есть возможность улучшить это, используя `logger.error`.
    -  Используется `ActionChains` для сложных действий с элементами.
- **Минусы:**
    - Некоторые комментарии можно улучшить, переформулировав в стиле RST и убрав лишние слова.
    - Следует избегать стандартных блоков `try-except` и вместо них использовать `logger.error` для обработки ошибок.
    - Не все docstring оформлены в стиле RST (необходимо добавить параметры, возвращаемые значения).
    - Не хватает docstring для модуля.
    - Не все импорты соответствуют соглашениям по именованию из других модулей.
    - Необходимо использовать `j_loads_ns` для загрузки JSON.

**Рекомендации по улучшению:**

1. **Улучшение документации:**
    - Добавить описание модуля в стиле RST.
    - Документировать все функции, методы и классы с помощью docstring в стиле RST, включая параметры и возвращаемые значения.
    - Переписать комментарии после `#` в стиле RST, убрав лишние слова и используя более конкретные формулировки.

2. **Обработка ошибок:**
    - Заменить использование `try-except` на `logger.error` для обработки исключений.

3. **Импорты:**
    - Добавить отсутствующие импорты, такие как `Union`, `List`, `Any`, `SimpleNamespace`
    - Привести в соответствие импорты с другими файлами (например `from src.utils.jjson import j_loads, j_loads_ns, j_dumps`).
    
4. **Использование `j_loads_ns`:**
    - Заменить стандартный `json.load` на `j_loads_ns` из `src.utils.jjson` при работе с json.
    
5.  **Стиль кода**
    -   Убрать избыточное использование try-except, где это возможно
    -   Использовать `logger.error` вместо `print` для логирования ошибок

6. **Дополнительно:**
    - Добавить примеры docstring для функций, классов, методов в RST формате.
    - Проверить код на наличие неиспользуемых переменных и методов и удалить их.

**Оптимизированный код:**

```python
"""
Модуль для работы с веб-драйвером и выполнения действий с элементами на странице.
===============================================================================

Этот модуль содержит класс :class:`ExecuteLocator`, который используется для выполнения
различных действий на веб-страницах с помощью Selenium WebDriver.

Пример использования
--------------------

Пример использования класса `ExecuteLocator`:

.. code-block:: python

    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator

    driver = webdriver.Chrome()
    executor = ExecuteLocator(driver)
    locator = {
      "by": "id",
      "selector": "some_id",
    }
    element = executor.get_webelement_by_locator(locator)
    if element:
        print(f'Найден элемент {element=}')
    driver.quit()
"""
from typing import Union, List, Any
from types import SimpleNamespace
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from src import gs
from src.utils.printer import pprint, j_dumps #j_loads,
from src.utils.jjson import j_loads_ns # j_loads, j_loads_ns
from src.logger.logger import logger
from src.logger.exceptions import DefaultSettingsException, WebDriverException, ExecuteLocatorException


class ExecuteLocator:
    """
    Класс для выполнения действий с элементами на веб-странице с использованием Selenium WebDriver.

    :param driver: Экземпляр WebDriver.
    :type driver: selenium.webdriver.remote.webdriver.WebDriver
    :raises WebDriverException: Если передан неверный тип драйвера.

    """
    def __init__(self, driver: webdriver.remote.webdriver.WebDriver, *args, **kwargs):
        """
        Инициализирует экземпляр класса ExecuteLocator.

        :param driver: Экземпляр WebDriver.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        :raises WebDriverException: Если передан неверный тип драйвера.

        """
        if not isinstance(driver, webdriver.remote.webdriver.WebDriver):
            logger.error(f'Неверный тип драйвера {type(driver)=}')
            raise WebDriverException(f'Неверный тип драйвера {type(driver)=}')

        # Инициализация драйвера и действий
        self.driver = driver
        self.actions = ActionChains(driver)
        # Словарь для преобразования строковых представлений локаторов в объекты By
        self.by_mapping = {
            'id': By.ID,
            'name': By.NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'tag_name': By.TAG_NAME,
            'class_name': By.CLASS_NAME,
            'css_selector': By.CSS_SELECTOR
        }
    
    def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
        """
        Выполняет действие с элементом на основе предоставленного локатора.

        :param locator: Словарь с параметрами локатора.
        :type locator: dict
        :param message: Сообщение для отправки (опционально).
        :type message: str, optional
        :param typing_speed: Скорость печати сообщения (опционально).
        :type typing_speed: float, optional
        :param continue_on_error: Флаг для продолжения выполнения при ошибке (опционально).
        :type continue_on_error: bool, optional
        :return: Результат выполнения действия.
        :rtype: Union[str, list, dict, WebElement, bool]
        
        """
        try:
            # Проверяет, что локатор - это словарь
            if not isinstance(locator, dict):
                logger.error(f'Неверный тип локатора: {type(locator)=}')
                return False
            
            # Проверяет наличие ключа 'by' в локаторе
            if 'by' not in locator:
                logger.error(f'В локаторе отсутствует ключ \'by\': {locator=}')
                return False
            
            # Получает тип локатора и селектор
            by_locator = locator.get('by').lower()
            selector = locator.get('selector')

            # Проверяет наличие селектора в локаторе
            if not selector:
               logger.error(f'В локаторе отсутствует ключ \'selector\': {locator=}')
               return False

            # Выбор действия в зависимости от наличия ключей 'attribute' и 'send_keys' в локаторе
            if 'attribute' in locator:
                # Если есть атрибут, то возвращаем его значение
                return self.get_attribute_by_locator(locator, message)
            elif 'send_keys' in locator:
                # Если есть `send_keys`, то отправляем сообщение
                if not message:
                     message = locator.get('send_keys')
                return self.send_message(locator, message, typing_speed, continue_on_error)
            else:
                 # Если нет ни атрибута, ни сообщения, получаем веб-элемент
                 return self.get_webelement_by_locator(locator, message)

        except Exception as ex:
            logger.error(f'Ошибка при выполнении локатора: {locator=}', exc_info=ex)
            if not continue_on_error:
                raise ExecuteLocatorException(f'Ошибка при выполнении локатора: {locator=}') from ex
            return False

    def get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) ->  Union[WebElement, List[WebElement], bool]:
        """
        Возвращает веб-элемент(ы), найденный по заданному локатору.

        :param locator: Словарь или SimpleNamespace с параметрами локатора.
        :type locator: dict | SimpleNamespace
        :param message: Сообщение для логирования (опционально).
        :type message: str, optional
        :raises ExecuteLocatorException: Если неверный тип локатора, нет `by` или `selector`
        :return: Веб-элемент, список веб-элементов или False, если элемент не найден.
        :rtype: Union[WebElement, List[WebElement], bool]

        """
        try:
            # Проверяет, что локатор - это словарь или SimpleNamespace
            if not isinstance(locator, (dict, SimpleNamespace)):
                logger.error(f'Неверный тип локатора: {type(locator)=}')
                return False
            
            # Преобразует SimpleNamespace в словарь, если это необходимо
            if isinstance(locator, SimpleNamespace):
                locator = vars(locator)

            # Проверяет наличие ключа 'by' в локаторе
            if 'by' not in locator:
                logger.error(f'В локаторе отсутствует ключ \'by\': {locator=}')
                return False
            
            # Получает тип локатора, селектор и таймаут
            by_locator = locator.get('by').lower()
            selector = locator.get('selector')
            timeout = locator.get('timeout', 1)
            timeout_for_event = locator.get('timeout_for_event')

            # Проверяет наличие селектора в локаторе
            if not selector:
                logger.error(f'В локаторе отсутствует ключ \'selector\': {locator=}')
                return False

            # Проверяет, что тип локатора допустимый
            if by_locator not in self.by_mapping:
                 logger.error(f'Неверный тип локатора: {by_locator=}')
                 return False
            
            # Получает объект By на основе строкового представления
            by = self.by_mapping[by_locator]

            # Ждет появления элемента на странице
            if timeout_for_event == 'presence_of_element_located':
                  element = WebDriverWait(self.driver, timeout).until(
                       EC.presence_of_element_located((by, selector))
                  )
            elif timeout_for_event == 'visibility_of_element_located':
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((by, selector))
                  )
            else:
                 element = self.driver.find_elements(by, selector)

            # Если элемент не список, возвращает его
            if not isinstance(element, list):
                return element
            
            # Если элемент - список, определяем, как его обрабатывать
            if_list = locator.get('if_list')
            if if_list == 'first':
                # Возвращаем первый элемент списка
                return element[0] if element else False
            elif if_list == 'all':
                 # Возвращаем весь список элементов
                return element
            else:
                logger.debug(f'Невалидное значение `if_list`:{if_list}')
                # Если значение `if_list` не определено, возвращаем весь список
                return element
    
        except (NoSuchElementException, TimeoutException) as ex:
            logger.error(f'Элемент не найден: {locator=}', exc_info=ex)
            return False
        except Exception as ex:
            logger.error(f'Ошибка при получении веб-элемента: {locator=}', exc_info=ex)
            return False
    
    def get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) ->  Union[str, list, dict, bool]:
        """
        Возвращает атрибут(ы) элемента, найденного по заданному локатору.

        :param locator: Словарь или SimpleNamespace с параметрами локатора.
        :type locator: dict | SimpleNamespace
        :param message: Сообщение для логирования (опционально).
        :type message: str, optional
        :return: Значение атрибута, список атрибутов или False, если элемент не найден.
        :rtype: Union[str, list, dict, bool]

        """
        try:
             # Проверяет, что локатор - это словарь или SimpleNamespace
            if not isinstance(locator, (dict, SimpleNamespace)):
                logger.error(f'Неверный тип локатора: {type(locator)=}')
                return False
            
             # Преобразует SimpleNamespace в словарь, если это необходимо
            if isinstance(locator, SimpleNamespace):
                 locator = vars(locator)

            # Получает атрибут(ы) из локатора
            attribute = locator.get('attribute')

             # Проверяет наличие атрибута в локаторе
            if not attribute:
                logger.error(f'В локаторе отсутствует ключ \'attribute\': {locator=}')
                return False

            # Получает веб-элемент(ы) по локатору
            element = self.get_webelement_by_locator(locator, message)

            # Если элемент не найден, возвращает False
            if not element:
                return False
             
            # Если атрибут - строка, возвращаем значение атрибута
            if isinstance(attribute, str):
                 if not isinstance(element, list):
                    return self._get_element_attribute(element, attribute)
                 else:
                     # Если элемент является списком, обрабатываем каждый элемент
                    return [self._get_element_attribute(el, attribute) for el in element ]
            
            # Если атрибут - список, возвращаем список значений атрибутов
            if isinstance(attribute, list):
                if not isinstance(element, list):
                    return [self._get_element_attribute(element, attr) for attr in attribute]
                else:
                    # Если элемент и атрибут являются списками, возвращаем список списков
                    return [[self._get_element_attribute(el, attr) for attr in attribute] for el in element]
            
            # Если атрибут не строка и не список, возвращает False
            logger.error(f'Неверный тип атрибута: {type(attribute)=}')
            return False
            
        except Exception as ex:
             logger.error(f'Ошибка при получении атрибута элемента: {locator=}', exc_info=ex)
             return False

    def _get_element_attribute(self, element: WebElement, attribute: str) ->  Union[str, None]:
        """
        Возвращает значение атрибута элемента.

        :param element: Веб-элемент.
        :type element: selenium.webdriver.remote.webelement.WebElement
        :param attribute: Название атрибута.
        :type attribute: str
        :return: Значение атрибута или None, если атрибут не найден.
        :rtype: Union[str, None]
        """
        try:
            # Получение значения атрибута элемента
            value = element.get_attribute(attribute)
            return value
        except Exception as ex:
            logger.error(f'Ошибка при получении значения атрибута {attribute=} элемента {element=}', exc_info=ex)
            return None

    def send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool:
        """
        Отправляет сообщение в веб-элемент.

        :param locator: Словарь или SimpleNamespace с параметрами локатора.
        :type locator: dict | SimpleNamespace
        :param message: Сообщение для отправки.
        :type message: str
        :param typing_speed: Скорость печати сообщения.
        :type typing_speed: float
        :param continue_on_error: Флаг для продолжения выполнения при ошибке (опционально).
        :type continue_on_error: bool, optional
        :return: True, если сообщение отправлено успешно, False в случае ошибки.
        :rtype: bool

        """
        try:
            # Получает веб-элемент по локатору
            element = self.get_webelement_by_locator(locator)
            # Если элемент не найден, возвращает False
            if not element:
                return False
            
            # Если скорость печати не указана, отправляет сообщение сразу
            if typing_speed <= 0:
                element.send_keys(message)
                return True
            
            # Если скорость печати указана, имитирует ввод сообщения
            for char in message:
                element.send_keys(char)
                self.driver.implicitly_wait(typing_speed)
            return True
            
        except Exception as ex:
             logger.error(f'Ошибка при отправке сообщения {message=} в элемент {locator=}', exc_info=ex)
             if not continue_on_error:
                 raise ExecuteLocatorException(f'Ошибка при отправке сообщения {message=} в элемент {locator=}') from ex
             return False

    def evaluate_locator(self, attribute: str | list | dict) -> str:
        """
        Оценивает атрибут локатора.

        :param attribute: Атрибут для оценки.
        :type attribute: str | list | dict
        :return: Оцененное значение атрибута.
        :rtype: str

        """
        # Проверяет тип атрибута
        if isinstance(attribute, str):
            # Если атрибут - строка, проводит оценку
            return self._evaluate(attribute)
        elif isinstance(attribute, list):
            # Если атрибут - список, применяет оценку к каждому элементу и объединяет результаты
             return ''.join([self._evaluate(attr) or '' for attr in attribute])
        elif isinstance(attribute, dict):
             # Если атрибут - словарь, применяет оценку к значениям и объединяет результаты
            return ''.join([self._evaluate(attr) or '' for attr in attribute.values() ])
        else:
             # В случае если тип атрибута не строка, список или словарь, то возвращает пустую строку
            logger.error(f'Неверный тип данных {type(attribute)=}')
            return ''
    
    def _evaluate(self, attribute: str) ->  Union[str, None]:
        """
        Оценивает отдельный атрибут.

        :param attribute: Атрибут для оценки.
        :type attribute: str
        :return: Оцененное значение атрибута или None, если атрибут не найден.
        :rtype: Union[str, None]

        """
        try:
            # Проверяет, является ли атрибут строкой
            if not isinstance(attribute, str):
                 logger.error(f'Неверный тип атрибута {type(attribute)=}')
                 return None
            
            # Проверяет, является ли атрибут шаблоном для внешнего сообщения
            if attribute == '%EXTERNAL_MESSAGE%':
                # Если да, возвращает внешнее сообщение
                return gs.EXTERNAL_MESSAGE
            else:
                # Иначе возвращает атрибут без изменений
                return attribute
        except Exception as ex:
            logger.error(f'Ошибка при оценке атрибута {attribute=}', exc_info=ex)
            return None

    @staticmethod
    def get_locator_keys() -> list:
        """
        Возвращает список ключей локаторов.

        :return: Список ключей локаторов.
        :rtype: list
        """
        # Возвращает список всех допустимых ключей локаторов
        return [
            'attribute',
            'by',
            'selector',
            'selector 2',
            'if_list',
            'use_mouse',
            'mandatory',
            'timeout',
             'timeout_for_event',
            'event',
            'send_keys',
             'locator_description'
        ]