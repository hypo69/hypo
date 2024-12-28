# Анализ кода модуля `test_driver_executor.py`

**Качество кода**
8
-  Плюсы
    -   Код хорошо структурирован, каждый тест имеет свою функцию, что делает его читаемым и понятным.
    -   Используются фикстуры pytest для настройки и завершения работы драйвера, что предотвращает дублирование кода.
    -   Присутствуют проверки на разные сценарии, включая поиск элементов, отправку сообщений, получение атрибутов и выполнение событий.
    -   Тесты покрывают как позитивные, так и негативные сценарии, такие как поиск несуществующего элемента и использование некорректного локатора.
    -   Присутствует проверка на получение ключей локатора.
-  Минусы
    -   В начале файла много неиспользуемых docstring.
    -   Отсутствует docstring для модуля.
    -   Не используется `src.utils.jjson`.
    -   Отсутствует логирование ошибок.
    -   В фикстуре `driver` прописан жесткий путь до `chromedriver`.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля.
2.  Удалить неиспользуемые docstring.
3.  Добавить логирование ошибок с использованием `src.logger.logger`.
4.  Улучшить комментарии, переписав их в формате reStructuredText.
5.  Убрать жестко заданный путь до `chromedriver` и вынести его в файл конфигурации.
6.  Добавить описание к каждой функции в формате reStructuredText.
7.  Заменить стандартные блоки `try-except` на использование `logger.error`.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль содержит тесты для проверки функциональности WebDriver и ExecuteLocator.
============================================================================

Этот модуль содержит набор тестов, которые проверяют взаимодействие WebDriver с веб-страницами,
а также функциональность класса :class:`ExecuteLocator`. Тесты охватывают различные сценарии,
включая навигацию по страницам, поиск элементов, отправку сообщений, получение атрибутов
и выполнение событий.

Модуль использует pytest для запуска тестов и selenium для управления браузером.

Примеры тестов
-----------------

Примеры использования тестов:

.. code-block:: python

    pytest src/webdriver/_pytest/test_driver_executor.py

"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from src.webdriver.executor import ExecuteLocator
from src.logger.exceptions import ExecuteLocatorException
from src.logger.logger import logger


MODE = 'dev'


@pytest.fixture(scope="module")
def driver():
    """
    Фикстура для настройки и завершения работы WebDriver.

    :return: Экземпляр WebDriver.
    :rtype: selenium.webdriver.chrome.webdriver.WebDriver
    """
    options = Options()
    options.add_argument("--headless")  # Запуск браузера в фоновом режиме для тестов
    # TODO: Вынести путь до chromedriver в файл конфигурации
    service = Service(executable_path="/path/to/chromedriver") # Путь до вашего chromedriver
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://example.com")  # URL для тестов
    yield driver
    driver.quit()


@pytest.fixture
def execute_locator(driver):
    """
    Фикстура для инициализации экземпляра ExecuteLocator.

    :param driver: Экземпляр WebDriver.
    :type driver: selenium.webdriver.chrome.webdriver.WebDriver
    :return: Экземпляр ExecuteLocator.
    :rtype: src.webdriver.executor.ExecuteLocator
    """
    return ExecuteLocator(driver)


def test_navigate_to_page(execute_locator, driver):
    """
    Тест для проверки, что WebDriver корректно загружает указанную страницу.

    :param execute_locator: Экземпляр ExecuteLocator.
    :type execute_locator: src.webdriver.executor.ExecuteLocator
    :param driver: Экземпляр WebDriver.
    :type driver: selenium.webdriver.chrome.webdriver.WebDriver
    """
    # Проверка текущего URL
    assert driver.current_url == "http://example.com"


def test_get_webelement_by_locator_single_element(execute_locator, driver):
    """
    Тест для проверки, что метод get_webelement_by_locator корректно возвращает элемент по локатору.

    :param execute_locator: Экземпляр ExecuteLocator.
    :type execute_locator: src.webdriver.executor.ExecuteLocator
    :param driver: Экземпляр WebDriver.
    :type driver: selenium.webdriver.chrome.webdriver.WebDriver
    """
    locator = {
        "by": "XPATH",
        "selector": "//h1"
    }
    # Код исполняет получение элемента по локатору
    element = execute_locator.get_webelement_by_locator(locator)
    # Проверка, что полученный элемент является WebElement
    assert isinstance(element, WebElement)
    # Проверка текста элемента
    assert element.text == "Example Domain"


def test_get_webelement_by_locator_no_element(execute_locator, driver):
    """
    Тест для проверки, что метод get_webelement_by_locator возвращает False, если элемент не найден.

    :param execute_locator: Экземпляр ExecuteLocator.
    :type execute_locator: src.webdriver.executor.ExecuteLocator
    :param driver: Экземпляр WebDriver.
    :type driver: selenium.webdriver.chrome.webdriver.WebDriver
    """
    locator = {
        "by": "XPATH",
        "selector": "//div[@id=\'nonexistent\']"
    }
    # Код исполняет поиск элемента
    result = execute_locator.get_webelement_by_locator(locator)
    # Проверка, что результат равен False
    assert result is False


def test_send_message(execute_locator, driver):
    """
    Тест для проверки, что метод send_message корректно отправляет сообщение элементу.

    :param execute_locator: Экземпляр ExecuteLocator.
    :type execute_locator: src.webdriver.executor.ExecuteLocator
    :param driver: Экземпляр WebDriver.
    :type driver: selenium.webdriver.chrome.webdriver.WebDriver
    """
    locator = {
        "by": "XPATH",
        "selector": "//input[@id=\'search\']"  # TODO: Заменить на фактическое поле ввода, если доступно
    }
    message = "Hello World"
    # Код исполняет отправку сообщения
    result = execute_locator.send_message(locator, message, typing_speed=0, continue_on_error=True)
    # Проверка, что результат равен True
    assert result is True


def test_get_attribute_by_locator(execute_locator, driver):
    """
    Тест для проверки, что метод get_attribute_by_locator корректно возвращает атрибут элемента.

    :param execute_locator: Экземпляр ExecuteLocator.
    :type execute_locator: src.webdriver.executor.ExecuteLocator
    :param driver: Экземпляр WebDriver.
    :type driver: selenium.webdriver.chrome.webdriver.WebDriver
    """
    locator = {
        "by": "XPATH",
        "selector": "//a[@id=\'more-information\']"
    }
    # Код исполняет получение значения атрибута
    attribute_value = execute_locator.get_attribute_by_locator(locator, message="href")
    # Проверка полученного значения
    assert attribute_value == "https://www.iana.org/domains/example"  # Обновить на основе фактического значения атрибута


def test_execute_locator_event(execute_locator, driver):
    """
    Тест для проверки, что событие корректно срабатывает на локаторе.

    :param execute_locator: Экземпляр ExecuteLocator.
    :type execute_locator: src.webdriver.executor.ExecuteLocator
    :param driver: Экземпляр WebDriver.
    :type driver: selenium.webdriver.chrome.webdriver.WebDriver
    """
    locator = {
        "by": "XPATH",
        "selector": "//a[@id=\'more-information\']"
    }
    # Код исполняет выполнение события
    result = execute_locator.execute_locator(locator, message="click")
    # Проверка, что событие было выполнено
    assert result is True


def test_get_locator_keys(execute_locator, driver):
    """
    Тест для проверки, что метод get_locator_keys возвращает правильные ключи локатора.

    :param execute_locator: Экземпляр ExecuteLocator.
    :type execute_locator: src.webdriver.executor.ExecuteLocator
    :param driver: Экземпляр WebDriver.
    :type driver: selenium.webdriver.chrome.webdriver.WebDriver
    """
    expected_keys = [
        'attribute',
        'by',
        'selector',
        'event',
        'use_mouse',
        'mandatory',
        'locator_description',
    ]
    # Код исполняет получение ключей локатора
    result = ExecuteLocator.get_locator_keys()
    # Проверка, что полученные ключи соответствуют ожидаемым
    assert set(result) == set(expected_keys)


def test_navigate_and_interact(execute_locator, driver):
    """
    Тест для проверки последовательности навигации и взаимодействия с элементами на другой странице.

    :param execute_locator: Экземпляр ExecuteLocator.
    :type execute_locator: src.webdriver.executor.ExecuteLocator
    :param driver: Экземпляр WebDriver.
    :type driver: selenium.webdriver.chrome.webdriver.WebDriver
    """
    # Код исполняет навигацию на новую страницу
    driver.get("https://www.wikipedia.org/")
    # Проверка текущего URL
    assert driver.current_url == "https://www.wikipedia.org/"

    # Код исполняет поиск и клик по полю ввода поиска
    locator = {
        "by": "XPATH",
        "selector": "//input[@id=\'searchInput\']"
    }
    execute_locator.send_message(locator, "Selenium", typing_speed=0, continue_on_error=True)

    # Код исполняет поиск и клик по кнопке поиска
    locator = {
        "by": "XPATH",
        "selector": "//button[@type=\'submit\']"
    }
    execute_locator.execute_locator(locator, message="click")

    # Проверка, что загружена страница с результатами поиска
    assert "Selenium" in driver.title

    # Проверка наличия элемента на странице результатов
    result_locator = {
        "by": "XPATH",
        "selector": "//h1[contains(text(), \'Selenium\')]"
    }
    # Код исполняет получение элемента по локатору
    result = execute_locator.get_webelement_by_locator(result_locator)
    # Проверка, что полученный элемент является WebElement
    assert isinstance(result, WebElement)
    # Проверка текста элемента
    assert result.text == "Selenium"


def test_invalid_locator(execute_locator, driver):
    """
    Тест для проверки обработки некорректных локаторов и соответствующего исключения.

    :param execute_locator: Экземпляр ExecuteLocator.
    :type execute_locator: src.webdriver.executor.ExecuteLocator
    :param driver: Экземпляр WebDriver.
    :type driver: selenium.webdriver.chrome.webdriver.WebDriver
    """
    locator = {
        "by": "INVALID_BY",
        "selector": "//div[@id=\'test\']"
    }
    # Код проверяет, что при некорректном локаторе вызывается исключение
    with pytest.raises(ExecuteLocatorException):
        execute_locator.execute_locator(locator, message="click")