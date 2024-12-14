# Анализ кода модуля `executor.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и документирован с использованием reStructuredText.
    - Использование `SimpleNamespace` для представления локаторов упрощает работу с их атрибутами.
    - Поддержка нескольких типов локаторов и действий с ними.
    - Наличие диаграмм потока Mermaid для ключевых методов.
    - Обработка ошибок с использованием `try-except` и логирование.
- Минусы
    - Необходимо добавление импортов `j_loads`, `j_loads_ns` и `logger`.
    - В некоторых местах можно сократить `try-except` блоки и использовать `logger.error`.
    - Следует пересмотреть именование переменных в соответствие с PEP8
    - Требуется более точная документация для некоторых методов и переменных.

**Рекомендации по улучшению**

1.  Добавить отсутствующие импорты `j_loads`, `j_loads_ns` и `logger`.
2.  Заменить `json.loads` на `j_loads_ns` для чтения данных.
3.  Улучшить обработку ошибок с использованием `logger.error` вместо `try-except` в некоторых местах.
4.  Добавить более подробные комментарии и docstring в формате RST для всех функций, методов и переменных.
5.  Улучшить форматирование кода в соответствии с PEP8.
6.  Переименовать переменные в соответствии со стилем кода (например, `webelement` -> `web_element`).
7.  Использовать f-строки для форматирования логов.
8.  Уточнить документацию для методов с параметрами.

**Оптимизированный код**

```python
"""
Модуль для работы с веб-элементами через Selenium WebDriver.
=============================================================

Предоставляет класс :class:`ExecuteLocator` для выполнения действий над веб-элементами
на основе заданных локаторов. Поддерживает различные типы локаторов, а также
выполнение событий и извлечение атрибутов.

Пример использования
--------------------

.. code-block:: python

    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator

    driver = webdriver.Chrome()
    executor = ExecuteLocator(driver=driver)
    locator = {
        "by": "ID",
        "selector": "some_element_id",
        "event": "click()"
    }
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

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement

#from src.utils.jjson import j_loads_ns
from src.logger.logger import logger #  импорт логгера
from src.utils.jjson import j_loads_ns # импорт j_loads_ns


@dataclass
class ExecuteLocator:
    """
    Класс для выполнения действий с веб-элементами на основе локаторов.

    :param driver: Экземпляр Selenium WebDriver.
    :type driver: WebDriver
    :param actions: Объект ActionChains для выполнения сложных действий.
    :type actions: ActionChains
    :param by_mapping: Словарь, сопоставляющий типы локаторов с методами By Selenium.
    :type by_mapping: dict
    :param mode: Режим выполнения ('debug', 'dev' и т.д.).
    :type mode: str
    """
    driver: WebDriver
    actions: Optional[ActionChains] = None
    by_mapping: Dict[str, str] = field(default_factory=lambda: {
        'ID': By.ID,
        'XPATH': By.XPATH,
        'CSS': By.CSS_SELECTOR,
        'CLASS_NAME': By.CLASS_NAME,
        'TAG_NAME': By.TAG_NAME,
        'LINK_TEXT': By.LINK_TEXT,
        'PARTIAL_LINK_TEXT': By.PARTIAL_LINK_TEXT,
        'NAME': By.NAME
    })
    mode: str = 'debug'

    def __post_init__(self):
        """
        Инициализирует объект ActionChains, если предоставлен драйвер.
        """
        if self.driver:
            self.actions = ActionChains(self.driver)

    async def execute_locator(self, locator: Union[dict, SimpleNamespace]) -> Any:
        """
        Выполняет действия над веб-элементом на основе предоставленного локатора.

        :param locator: Локатор веб-элемента в виде словаря или SimpleNamespace.
        :type locator: Union[dict, SimpleNamespace]
        :return: Результат выполнения действий над веб-элементом.
        :rtype: Any
        """
        # Проверка типа локатора
        if isinstance(locator, dict):
            locator = SimpleNamespace(**locator) #  преобразовываем dict в SimpleNamespace

        async def _parse_locator(locator: SimpleNamespace) -> Any:
            """
            Внутренняя функция для обработки локатора.

            :param locator: Локатор веб-элемента.
            :type locator: SimpleNamespace
            :return: Результат выполнения действий над веб-элементом.
            :rtype: Any
            """
            # проверка наличия события, атрибута или обязательного поля
            if not any([getattr(locator, 'event', None),
                        getattr(locator, 'attribute', None),
                        getattr(locator, 'mandatory', None)]):
                return None

            try:
                by = self.by_mapping.get(locator.by) #  определяем метод поиска элемента
                if not by:
                   logger.error(f'Неизвестный тип локатора {locator.by}')
                   return None #  если тип локатора не найден возвращаем None

                if hasattr(locator, 'attribute'): #  проверяем, есть ли атрибут в локаторе
                   return await self.evaluate_locator(locator) # если атрибут есть, вызываем метод `evaluate_locator`
                elif hasattr(locator, 'event'):  #  проверяем, есть ли событие в локаторе
                    return await self.execute_event(locator) #  если событие есть, вызываем метод `execute_event`
                else:
                    return await self.get_webelement_by_locator(locator) # если нет ни события ни атрибута, то возвращаем веб элемент
            except Exception as ex:
                logger.error(f'Ошибка обработки локатора {locator=}', exc_info=ex)
                return None


        return await _parse_locator(locator)

    async def evaluate_locator(self, locator: SimpleNamespace) -> Any:
        """
        Оценивает и обрабатывает атрибуты локатора.

        :param locator: Локатор веб-элемента.
        :type locator: SimpleNamespace
        :return: Результат обработки атрибута.
        :rtype: Any
        """
        async def _evaluate(attribute: str) -> Any:
            """
            Внутренняя функция для оценки атрибута.

            :param attribute: Атрибут веб-элемента.
            :type attribute: str
            :return: Результат оценки атрибута.
            :rtype: Any
            """
            if attribute == 'text':
                #  если атрибут текст, то получаем текст элемента
                element = await self.get_webelement_by_locator(locator)
                if element:
                   return  element.text
                return None

            return await self.get_attribute_by_locator(locator) #  вызываем метод `get_attribute_by_locator` для получения атрибута

        attribute = locator.attribute #  получаем атрибут из локатора
        if isinstance(attribute, list): #  проверяем, является ли атрибут списком
           return await asyncio.gather(*[_evaluate(attr) for attr in attribute]) #  вызываем `_evaluate` для каждого атрибута в списке и собираем результаты
        return await _evaluate(attribute)  # вызываем `_evaluate` для одного атрибута

    async def get_attribute_by_locator(self, locator: SimpleNamespace) -> Optional[Union[str, List[str]]]:
        """
        Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.

        :param locator: Локатор веб-элемента.
        :type locator: SimpleNamespace
        :return: Значение атрибута или список значений атрибутов.
        :rtype: Optional[Union[str, List[str]]]
        """
        # преобразовываем в SimpleNamespace если локатор является dict
        if isinstance(locator, dict):
            locator = SimpleNamespace(**locator)
        web_element = await self.get_webelement_by_locator(locator) # получаем веб-элемент
        if not web_element:
            logger.debug(f'Элемент не найден: {locator=}')#  если элемент не найден возвращаем None
            return None

        attribute = locator.attribute #  получаем атрибут из локатора
        if isinstance(attribute, str) and attribute.startswith('{') and attribute.endswith('}'): # проверяем, является ли атрибут строкой, похожей на словарь
            try:
                attribute = j_loads_ns(attribute) # преобразовываем строку в словарь
            except Exception as ex:
                logger.error(f'Не удалось преобразовать строку атрибута в словарь: {attribute=}', exc_info=ex) #  если не удалось преобразовать, то логируем ошибку
                return None
        if isinstance(web_element, list): # проверяем, является ли web_element списком
            if isinstance(attribute,dict): # проверяем, является ли атрибут словарем
               return [element.get_attribute(key) for element in web_element for key, value in attribute.items() if value]#  получаем атрибут для каждого элемента в списке
            return [element.get_attribute(attribute) for element in web_element] # получаем атрибут для каждого элемента в списке
        if isinstance(attribute,dict):# проверяем, является ли атрибут словарем
           return [web_element.get_attribute(key) for key, value in attribute.items() if value ] #  получаем атрибут для одного элемента
        return web_element.get_attribute(attribute) #  получаем атрибут для одного элемента

    async def get_webelement_by_locator(self, locator: SimpleNamespace) -> Optional[Union[WebElement, List[WebElement]]]:
        """
        Извлекает веб-элементы на основе предоставленного локатора.

        :param locator: Локатор веб-элемента.
        :type locator: SimpleNamespace
        :return: Веб-элемент или список веб-элементов.
        :rtype: Optional[Union[WebElement, List[WebElement]]]
        """
        by = self.by_mapping.get(locator.by) #  определяем метод поиска элемента
        if not by:
            logger.error(f'Неизвестный тип локатора: {locator.by}')#  если тип локатора не найден возвращаем None
            return None

        selector = locator.selector #  получаем селектор из локатора
        try:
           if getattr(locator, 'many', None):
              #  если указан флаг 'many', то ищем все элементы
               web_element = self.driver.find_elements(by, selector)
           else:
              # иначе ищем один элемент
               web_element = self.driver.find_element(by, selector)
           return web_element #  возвращаем найденные элементы
        except Exception as ex:
             logger.error(f'Не удалось получить веб-элемент: {locator=}', exc_info=ex) # если не удалось получить элемент, то логируем ошибку
             return None # если не удалось получить элемент, возвращаем None


    async def get_webelement_as_screenshot(self, locator: SimpleNamespace, path: Path) -> bool:
        """
        Делает скриншот найденного веб-элемента.

        :param locator: Локатор веб-элемента.
        :type locator: SimpleNamespace
        :param path: Путь для сохранения скриншота.
        :type path: Path
        :return: True, если скриншот сделан успешно, иначе False.
        :rtype: bool
        """
        web_element = await self.get_webelement_by_locator(locator) # получаем веб-элемент
        if not web_element:
            logger.debug(f'Элемент не найден: {locator=}')#  если элемент не найден, то логируем ошибку и возвращаем False
            return False
        try:
            web_element.screenshot(path) #  делаем скриншот элемента и сохраняем его по указанному пути
            return True
        except Exception as ex:
            logger.error(f'Не удалось сделать скриншот элемента: {locator=}, path={path}', exc_info=ex)# если не удалось сделать скриншот, то логируем ошибку
            return False

    async def execute_event(self, locator: SimpleNamespace) -> Optional[bool]:
        """
        Выполняет события, связанные с локатором.

        :param locator: Локатор веб-элемента.
        :type locator: SimpleNamespace
        :return: True, если событие выполнено успешно, иначе False.
        :rtype: Optional[bool]
        """
        web_element = await self.get_webelement_by_locator(locator) #  получаем веб-элемент
        if not web_element:
            logger.debug(f'Элемент не найден: {locator=}')#  если элемент не найден, то логируем ошибку и возвращаем None
            return None

        event = locator.event #  получаем событие из локатора
        try:
            if event == 'click()':#  проверяем, является ли событие кликом
                web_element.click() #  если событие клик, то выполняем клик по элементу
                return True
            elif event == 'focus()': #  проверяем, является ли событие фокусом
                self.actions.move_to_element(web_element).perform() # если событие фокус, то выполняем фокус на элемент
                return True
            elif event == 'submit()': # проверяем, является ли событие отправкой формы
                web_element.submit() #  если событие отправка формы, то отправляем форму
                return True
            elif event.startswith('send_keys('): # проверяем, является ли событие отправкой текста
                match = re.match(r"send_keys\((.*)\)", event) #  извлекаем текст из события
                if match:
                   keys = match.group(1).strip("'").strip('"') #  извлекаем текст из события
                   web_element.send_keys(keys) # отправляем текст
                   return True
            else:
                logger.error(f'Неизвестное событие: {event=}')#  если событие неизвестно, то логируем ошибку
                return None
        except Exception as ex:
           logger.error(f'Не удалось выполнить событие: {event=}, {locator=}', exc_info=ex) #  если не удалось выполнить событие, то логируем ошибку
           return None

    async def send_message(self, locator: SimpleNamespace, message: str) -> Optional[bool]:
        """
        Отправляет сообщение веб-элементу.

        :param locator: Локатор веб-элемента.
        :type locator: SimpleNamespace
        :param message: Сообщение для отправки.
        :type message: str
        :return: True, если сообщение отправлено успешно, иначе False.
        :rtype: Optional[bool]
        """
        web_element = await self.get_webelement_by_locator(locator) #  получаем веб-элемент
        if not web_element:
            logger.debug(f'Элемент не найден: {locator=}')#  если элемент не найден, то логируем ошибку и возвращаем None
            return None

        try:
            web_element.send_keys(message) # отправляем сообщение в элемент
            return True
        except Exception as ex:
            logger.error(f'Не удалось отправить сообщение: {message=}, {locator=}', exc_info=ex) #  если не удалось отправить сообщение, то логируем ошибку
            return None
```