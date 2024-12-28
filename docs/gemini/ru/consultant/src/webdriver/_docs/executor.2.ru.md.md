# Анализ кода модуля `executor`

**Качество кода**
**7**
-  Плюсы
    - Код содержит подробные описания функций, что облегчает понимание их назначения и параметров.
    - Используются docstring для документирования функций.
    - Присутствует разделение функций по логическому назначению.
-  Минусы
    -  Отсутствуют импорты, которые могут понадобится для работы с кодом.
    -  В описаниях функций и параметрах используются `@param`, `@return`, что не соответствует reStructuredText (RST), нужно использовать `:param:` и `:return:`.
    -  Не указаны типы возвращаемых значений, а это важно при использовании RST.
    -  Не используется логирование ошибок.
    -  Нет единого стиля для документирования.
    -  Используются `...` в коде, что не является хорошей практикой.

**Рекомендации по улучшению**

1.  **Импорты:** Добавить необходимые импорты, такие как `typing`, `webdriver`, `logger`
2.  **Формат документации:** Использовать reStructuredText (RST) для всех комментариев и docstring. Заменить `@param` и `@return` на `:param:` и `:return:`. Добавить типы возвращаемых значений.
3.  **Логирование:** Добавить логирование ошибок с помощью `from src.logger.logger import logger`
4.  **Обработка ошибок:** Избегать `try-except` блоков, предпочитая использование `logger.error`.
5.  **Убрать ...:** Убрать `...` и реализовать функционал кода.
6.  **Стандартизация:** Привести в соответствие имена переменных и функций с ранее обработанными файлами.

**Оптимизированный код**
```python
"""
Модуль executor для выполнения действий с веб-элементами.
========================================================

Этот модуль предоставляет набор функций для взаимодействия с веб-страницами,
включая выполнение действий с элементами, получение их атрибутов и отправку сообщений.

Функции модуля:
    - :func:`execute_locator`: Выполняет действия с веб-элементом по локатору.
    - :func:`get_webelement_by_locator`: Получает веб-элемент по локатору.
    - :func:`get_attribute_by_locator`: Получает значение атрибута веб-элемента.
    - :func:`send_message`: Отправляет сообщение веб-элементу.
    - :func:`get_url`: Загружает HTML-контент с URL или файла.

"""
from typing import Any, Dict, Union
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import WebDriverException
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns

def execute_locator(driver: WebDriver, locator: Dict, message: str = '', typing_speed: float = 0.0, continue_on_error: bool = True) -> Union[WebElement, list, str, None]:
    """
    Выполняет действия с веб-элементом, основываясь на предоставленном локаторе.

    :param driver: Экземпляр веб-драйвера.
    :param locator: Словарь, содержащий информацию о локаторе (тип, селектор и т.д.).
    :param message: Сообщение для отправки веб-элементу (например, текст для ввода).
    :param typing_speed: Скорость набора текста при отправке сообщения (в секундах между нажатиями клавиш).
    :param continue_on_error: Флаг, указывающий, следует ли продолжать выполнение при возникновении ошибки.
    :return: Результат выполнения локатора: веб-элемент, список элементов, значение атрибута или результат действия.
    :raises WebDriverException: Если произошла ошибка при выполнении действий с веб-элементом и continue_on_error=False.
    """
    try:
        # Код выполняет получение веб-элемента на основе предоставленного локатора
        element = get_webelement_by_locator(driver, locator)
        if not element:
            logger.error(f'Веб-элемент не найден {locator=}')
            return None

        # Проверка наличия сообщения для отправки.
        if message:
             # Код выполняет отправку сообщения в веб-элемент с учетом скорости печати
            send_message(driver, locator, message, typing_speed, continue_on_error)
            return True
        
        # Проверка наличия атрибута в локаторе, если есть, то код возвращает его значение
        if 'attribute' in locator:
            return get_attribute_by_locator(driver, locator, message)

        return element

    except WebDriverException as ex:
        logger.error(f'Ошибка выполнения действий с локатором {locator=}: {ex}')
        if not continue_on_error:
            raise
        return None


def get_webelement_by_locator(driver: WebDriver, locator: Dict) -> Union[WebElement, list, None]:
    """
    Находит и возвращает веб-элемент или список веб-элементов, основываясь на предоставленном локаторе.

    :param driver: Экземпляр веб-драйвера.
    :param locator: Словарь, содержащий информацию о локаторе (тип, селектор и т.д.).
    :return: Найденный веб-элемент, список элементов, или None если элемент не найден.
    :raises WebDriverException: В случае ошибки при поиске элементов.
    """
    try:
        # Код определяет метод поиска элемента на основе типа локатора
        find_by = getattr(driver, f'find_element{locator.get("type", "").lower()}')
        # Код выполняет поиск элемента с помощью определенного метода
        if 'selector' in locator:
            return find_by(locator['selector'])
        
        # Код определяет метод поиска элементов на основе типа локатора
        find_by = getattr(driver, f'find_elements{locator.get("type", "").lower()}')
          # Код выполняет поиск элементов с помощью определенного метода
        if 'selectors' in locator:
             return find_by(locator['selectors'])
        
        logger.error(f'Некорректный локатор {locator=}, отсутсвует поле `selector` или `selectors`')
        return None

    except WebDriverException as ex:
        logger.error(f'Ошибка поиска элемента по локатору {locator=}: {ex}')
        return None


def get_attribute_by_locator(driver: WebDriver, locator: Dict, message: str = '') -> Union[str, None]:
    """
    Извлекает значение атрибута веб-элемента, определенного локатором.

    :param driver: Экземпляр веб-драйвера.
    :param locator: Словарь, содержащий информацию о локаторе (тип, селектор и т.д.).
    :param message: Сообщение для отправки веб-элементу перед получением атрибута (необязательно).
    :return: Значение атрибута веб-элемента или None, если произошла ошибка или атрибут не найден.
    :raises WebDriverException: В случае ошибки при получении атрибута элемента.
    """
    try:
        # Код получает веб-элемент по локатору.
        element = get_webelement_by_locator(driver, locator)
        if not element:
            logger.error(f'Элемент не найден для получения атрибута {locator=}')
            return None
         # Код получает значение атрибута у веб-элемента.
        if 'attribute' in locator:
            return element.get_attribute(locator['attribute'])
        
        logger.error(f'Некорректный локатор {locator=}, отсутсвует поле `attribute`')
        return None

    except WebDriverException as ex:
        logger.error(f'Ошибка получения атрибута элемента по локатору {locator=}: {ex}')
        return None


def send_message(driver: WebDriver, locator: Dict, message: str, typing_speed: float = 0.0, continue_on_error: bool = True) -> bool:
    """
    Отправляет сообщение (текст) веб-элементу, определенному локатором.

    :param driver: Экземпляр веб-драйвера.
    :param locator: Словарь, содержащий информацию о локаторе (тип, селектор и т.д.).
    :param message: Сообщение для отправки веб-элементу.
    :param typing_speed: Скорость набора текста при отправке сообщения (в секундах между нажатиями клавиш).
    :param continue_on_error: Флаг, указывающий, следует ли продолжать выполнение при возникновении ошибки.
    :return: True, если сообщение отправлено успешно, иначе False.
     :raises WebDriverException: В случае ошибки при отправке сообщения.
    """
    try:
        # Код получает веб-элемент по локатору.
        element = get_webelement_by_locator(driver, locator)
        if not element:
            logger.error(f'Элемент не найден для отправки сообщения {locator=}')
            return False

        if typing_speed > 0:
           # Код отправляет сообщение посимвольно с заданной скоростью.
            for char in message:
                element.send_keys(char)
                import time
                time.sleep(typing_speed)
        else:
             # Код отправляет сообщение сразу.
            element.send_keys(message)
        return True
    
    except WebDriverException as ex:
        logger.error(f'Ошибка отправки сообщения элементу по локатору {locator=}: {ex}')
        if not continue_on_error:
             raise
        return False


def get_url(driver: WebDriver, url: str, protocol: str = 'https://') -> bool:
    """
    Загружает HTML-контент с указанного URL-адреса или файла.

    :param driver: Экземпляр веб-драйвера.
    :param url: URL-адрес или путь к файлу для загрузки HTML-контента.
    :param protocol: Протокол для URL (по умолчанию 'https://').
    :return: True, если контент успешно загружен, иначе False.
    :raises WebDriverException: В случае ошибки при загрузке страницы.
    """
    try:
       # Проверка, является ли URL путем к файлу
        if url.startswith('/'):
           # Код загружает содержимое файла, если путь к файлу.
           data = j_loads_ns(url)
           driver.get(f'data:text/html;charset=utf-8,{data}')
           return True
        else:
            # Код загружает страницу по URL.
            driver.get(protocol + url)
            return True

    except WebDriverException as ex:
        logger.error(f'Ошибка при загрузке URL {url=}: {ex}')
        return False
```