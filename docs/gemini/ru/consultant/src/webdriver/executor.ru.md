# Анализ кода модуля `executor`

## Качество кода:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Хорошо структурированный и описанный модуль с подробной документацией.
    - Наличие диаграмм потоков для ключевых методов.
    -  Подробное описание структуры модуля, классов, методов и параметров.
    -  Примеры использования кода.
- **Минусы**:
    - Отсутствует код модуля, только описание.
    - Не все комментарии соответствуют стандарту RST.
    - Не везде используется единый стиль кавычек.
    - Нет обработки импортов и структуры модуля.
    - Нет рекомендаций по PEP8.

## Рекомендации по улучшению:
- Необходимо добавить код модуля для анализа и улучшения.
- Код модуля должен использовать одинарные кавычки для строк в Python и двойные кавычки только для вывода.
- Необходимо добавить проверку наличия всех необходимых импортов и их выравнивание.
- В коде следует использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load`.
- Необходимо добавить комментарии в формате RST для всех функций, методов и классов.
-  Следует избегать стандартных блоков `try-except`, отдавая предпочтение обработке ошибок через `logger.error`.
-  Рекомендации по PEP8 должны быть соблюдены для форматирования.
-  Необходимо добавить более точные описания в комментариях, например: "проверяем", "отправляем", "выполняем".
- Необходимо использовать `from src.logger.logger import logger` для логирования ошибок.

## Оптимизированный код:
```python
"""
Модуль для автоматизации взаимодействия с веб-элементами с использованием Selenium.
==============================================================================

Модуль предоставляет класс :class:`ExecuteLocator`, который используется для взаимодействия с веб-элементами
на основе предоставленных конфигураций (локаторов).

Пример использования:
---------------------

.. code-block:: python

    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator

    # Инициализация WebDriver
    driver = webdriver.Chrome()

    # Инициализация класса ExecuteLocator
    executor = ExecuteLocator(driver=driver)

    # Определение локатора
    locator = {
        'by': 'ID',
        'selector': 'some_element_id',
        'event': 'click()'
    }

    # Выполнение локатора
    result = await executor.execute_locator(locator)
    print(result)
"""
import asyncio
import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict, List, Optional, Union

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from src.logger.logger import logger #  Импорт логгера из src.logger
from src.utils.jjson import j_loads_ns #  Импорт j_loads_ns


class LocatorType(str, Enum):
    """
    Перечисление для типов локаторов.
    """
    ID = 'id'
    XPATH = 'xpath'
    CLASS_NAME = 'class_name'
    CSS_SELECTOR = 'css_selector'
    TAG_NAME = 'tag_name'
    LINK_TEXT = 'link_text'
    PARTIAL_LINK_TEXT = 'partial_link_text'
    NAME = 'name'


@dataclass
class ExecuteLocator:
    """
    Класс для выполнения действий с веб-элементами на основе предоставленных локаторов.

    :param driver: Экземпляр Selenium WebDriver.
    :type driver: WebDriver
    :param mode: Режим выполнения ('debug', 'dev' и т.д.).
    :type mode: str, optional
    """
    driver: Optional[WebDriver] = None
    mode: str = 'dev'
    actions: Optional[ActionChains] = field(init=False, default=None)
    by_mapping: Dict[str, str] = field(
        default_factory=lambda: {
            LocatorType.ID: By.ID,
            LocatorType.XPATH: By.XPATH,
            LocatorType.CLASS_NAME: By.CLASS_NAME,
            LocatorType.CSS_SELECTOR: By.CSS_SELECTOR,
            LocatorType.TAG_NAME: By.TAG_NAME,
            LocatorType.LINK_TEXT: By.LINK_TEXT,
            LocatorType.PARTIAL_LINK_TEXT: By.PARTIAL_LINK_TEXT,
            LocatorType.NAME: By.NAME,
        }
    )

    def __post_init__(self):
        """
        Инициализация объекта ActionChains, если предоставлен драйвер.
        """
        if self.driver:
            self.actions = ActionChains(self.driver)

    async def execute_locator(self, locator: Union[Dict, SimpleNamespace]) -> Optional[Any]:
        """
        Выполняет действия над веб-элементом на основе предоставленного локатора.

        :param locator: Локатор в виде словаря или SimpleNamespace.
        :type locator: Union[Dict, SimpleNamespace]
        :return: Результат выполнения действий над веб-элементом.
        :rtype: Optional[Any]
        """
        if isinstance(locator, dict):
           locator = j_loads_ns(locator)  #  Используем j_loads_ns для преобразования dict в SimpleNamespace
        
        async def _parse_locator(loc: SimpleNamespace) -> Optional[Any]: #  Объявляем асинхронную функцию _parse_locator
            if not any([loc.get('event'), loc.get('attribute'), loc.get('mandatory')]): #  Проверяем наличие события, атрибута или mandatory
                return None

            try:
                by = self.by_mapping.get(loc.by.lower()) #  Получаем значение by из словаря by_mapping
                if by is None:
                   logger.error(f'Недопустимый тип локатора: {loc.by}') #  Логируем ошибку, если тип локатора недействительный
                   return None

                element = await self.get_webelement_by_locator(loc) #  Получаем веб-элемент по локатору
                if not element and loc.get('mandatory'):
                   logger.error(f'Элемент не найден, локатор: {loc}') #  Логируем ошибку, если элемент не найден и он обязательный
                   return None

                if loc.get('event'):  # Проверяем, есть ли событие
                    return await self.execute_event(loc, element) # Выполняем событие
                elif loc.get('attribute'):  # Проверяем, есть ли атрибут
                    return await self.get_attribute_by_locator(loc) # Получаем атрибут по локатору
                else:
                    return element  # Возвращаем веб-элемент, если нет ни события, ни атрибута
            except Exception as e: #  Перехватываем возможные исключения
                logger.error(f'Ошибка при обработке локатора {loc}: {e}')  # Логируем ошибку
                return None

        return await _parse_locator(locator) #  Вызываем асинхронную функцию _parse_locator

    async def evaluate_locator(self, locator: SimpleNamespace) -> Optional[Union[List[Any], Any]]:
        """
        Оценивает и обрабатывает атрибуты локатора.

        :param locator: Локатор в виде SimpleNamespace.
        :type locator: SimpleNamespace
        :return: Результат оценки атрибутов локатора.
        :rtype: Optional[Union[List[Any], Any]]
        """
        async def _evaluate(loc: SimpleNamespace) -> Optional[Any]: #  Объявляем асинхронную функцию _evaluate
            try:
               if loc.get('attribute') and isinstance(loc.attribute, list): #  Проверяем, является ли атрибут списком
                   return await asyncio.gather(
                       *[self.get_attribute_by_locator(SimpleNamespace(**{**loc.__dict__, 'attribute': attr})) for attr in loc.attribute ]
                   ) #  Возвращаем результаты вызова get_attribute_by_locator для каждого атрибута
               else:
                    return await self.get_attribute_by_locator(loc) #  Возвращаем результат вызова get_attribute_by_locator для одного атрибута
            except Exception as e:
                logger.error(f'Ошибка при оценке атрибута локатора {loc}: {e}') #  Логируем ошибку
                return None
        return await _evaluate(locator) #  Вызываем асинхронную функцию _evaluate

    async def get_attribute_by_locator(self, locator: SimpleNamespace) -> Optional[Union[List[Any], Any]]:
        """
        Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.

        :param locator: Локатор в виде SimpleNamespace.
        :type locator: SimpleNamespace
        :return: Атрибут(ы) элемента или список атрибутов элементов.
        :rtype: Optional[Union[List[Any], Any]]
        """
        if isinstance(locator, dict):  #  Преобразуем dict в SimpleNamespace если нужно
            locator = j_loads_ns(locator)
        element = await self.get_webelement_by_locator(locator) #  Получаем веб-элемент по локатору
        if not element:
            logger.debug(f'Элемент не найден, локатор: {locator}') # Логируем в debug, что элемент не найден
            return None
        
        attribute = locator.get('attribute') #  Получаем атрибут из локатора
        if attribute and isinstance(attribute, str) and (attribute.startswith('{') and attribute.endswith('}')): # Проверяем, является ли атрибут строкой, похожей на словарь
            try:
                attribute = j_loads_ns(attribute) #  Парсим строку в словарь
            except Exception as e:
                logger.error(f'Ошибка при парсинге строки атрибута в словарь {attribute}: {e}') #  Логируем ошибку парсинга
        
        if isinstance(element, list): #  Проверяем, является ли элемент списком
                if isinstance(attribute, dict): #  Проверяем, является ли атрибут словарем
                   return [
                        {key: el.get_attribute(value) for key, value in attribute.items()}
                        for el in element
                    ] #  Возвращаем список атрибутов для каждого элемента
                else:
                     return [el.get_attribute(attribute) for el in element] #  Возвращаем список атрибутов для каждого элемента
        else:
            if isinstance(attribute, dict): #  Проверяем, является ли атрибут словарем
                 return {key: element.get_attribute(value) for key, value in attribute.items()} #  Возвращаем словарь атрибутов
            else:
                return element.get_attribute(attribute)  #  Возвращаем атрибут одного элемента

    async def get_webelement_by_locator(self, locator: SimpleNamespace) -> Optional[Union[WebElement, List[WebElement]]]:
        """
        Извлекает веб-элементы на основе предоставленного локатора.

        :param locator: Локатор в виде SimpleNamespace.
        :type locator: SimpleNamespace
        :return: Веб-элемент(ы), найденный(е) по локатору.
        :rtype: Optional[Union[WebElement, List[WebElement]]]
        """
        if isinstance(locator, dict):  #  Преобразуем dict в SimpleNamespace если нужно
            locator = j_loads_ns(locator)
        by = self.by_mapping.get(locator.by.lower()) #  Получаем значение by из словаря by_mapping
        if not by:
            logger.error(f'Недопустимый тип локатора: {locator.by}') #  Логируем ошибку, если тип локатора недействительный
            return None
        selector = locator.selector #  Получаем селектор из локатора
        try:
            if locator.get('many'): #  Проверяем, нужно ли вернуть список элементов
                 elements = self.driver.find_elements(by, selector) #  Ищем все элементы
                 return elements if elements else None #  Возвращаем список элементов, если найдены, иначе None
            else:
                element = self.driver.find_element(by, selector) #  Ищем один элемент
                return element #  Возвращаем найденный элемент
        except Exception as e:
             logger.error(f'Ошибка при поиске элемента {selector} : {e}') #  Логируем ошибку поиска элемента
             return None

    async def get_webelement_as_screenshot(self, locator: SimpleNamespace, file_path: Union[str, Path]) -> bool:
        """
        Делает скриншот найденного веб-элемента.

        :param locator: Локатор в виде SimpleNamespace.
        :type locator: SimpleNamespace
        :param file_path: Путь для сохранения скриншота.
        :type file_path: Union[str, Path]
        :return: True, если скриншот успешно сделан, иначе False.
        :rtype: bool
        """
        if isinstance(locator, dict):  #  Преобразуем dict в SimpleNamespace если нужно
            locator = j_loads_ns(locator)
        element = await self.get_webelement_by_locator(locator) #  Получаем веб-элемент по локатору
        if element:
            try:
                element.screenshot(str(file_path)) #  Делаем скриншот элемента
                return True
            except Exception as e:
                logger.error(f'Ошибка при создании скриншота элемента {locator}: {e}') #  Логируем ошибку создания скриншота
        return False

    async def execute_event(self, locator: SimpleNamespace, element: Optional[WebElement] = None) -> Optional[Any]:
        """
        Выполняет события, связанные с локатором.

        :param locator: Локатор в виде SimpleNamespace.
        :type locator: SimpleNamespace
        :param element: Веб-элемент, над которым нужно выполнить событие.
        :type element: Optional[WebElement], optional
        :return: Результат выполнения события.
        :rtype: Optional[Any]
        """
        if isinstance(locator, dict):  #  Преобразуем dict в SimpleNamespace если нужно
            locator = j_loads_ns(locator)
        event = locator.event #  Получаем событие из локатора
        if not element:
           element = await self.get_webelement_by_locator(locator)  # Получаем веб-элемент по локатору
        if not element:
            logger.error(f'Элемент для события не найден, локатор: {locator}')  # Логируем ошибку, если элемент не найден
            return None

        if event and '()' in event:
            event = event.replace('()', '') #  Удаляем скобки из названия события
            try:
                if hasattr(element, event): #  Проверяем наличие события у элемента
                   method = getattr(element, event) #  Получаем метод события
                   if callable(method): #  Проверяем, является ли метод вызываемым
                        method() #  Вызываем метод события
                        return True
                   else:
                        logger.error(f'Событие {event} не является методом') # Логируем ошибку, если событие не метод
                        return None
                else:
                    logger.error(f'У элемента нет события {event}')  # Логируем ошибку, если у элемента нет события
                    return None

            except Exception as e:
                logger.error(f'Ошибка при выполнении события {event} у элемента {locator}: {e}') # Логируем ошибку при выполнении события
                return None

        elif event and 'send_keys' in event :
            send_keys =  re.search(r'send_keys\((.*?)\)', event) #  Ищем аргументы send_keys
            if send_keys:
                try:
                    text = send_keys.group(1).strip().replace("'", "").replace('"', "") #  Извлекаем текст из аргументов
                    element.send_keys(text) #  Отправляем текст элементу
                    return True
                except Exception as e:
                   logger.error(f'Ошибка при отправке сообщения {text} у элемента {locator}: {e}') #  Логируем ошибку при отправке сообщения
                   return None
        return None

    async def send_message(self, locator: SimpleNamespace, message: str) -> bool:
        """
        Отправляет сообщение веб-элементу.

        :param locator: Локатор в виде SimpleNamespace.
        :type locator: SimpleNamespace
        :param message: Сообщение для отправки.
        :type message: str
        :return: True, если сообщение успешно отправлено, иначе False.
        :rtype: bool
        """
        if isinstance(locator, dict):  #  Преобразуем dict в SimpleNamespace если нужно
            locator = j_loads_ns(locator)
        element = await self.get_webelement_by_locator(locator) #  Получаем веб-элемент по локатору
        if element:
            try:
                element.send_keys(message) #  Отправляем сообщение элементу
                return True
            except Exception as e:
                logger.error(f'Ошибка при отправке сообщения {message} элементу {locator}: {e}') #  Логируем ошибку отправки сообщения
        return False
```