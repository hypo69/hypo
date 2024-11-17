


""" Фикстуры:

driver_mock: создает фиктивный объект веб-драйвера.
execute_locator: создает экземпляр класса ExecuteLocator с фиктивным веб-драйвером.
#Тесты:
 - test_get_webelement_by_locator_single_element: Проверяет получение одного элемента.
 - test_get_webelement_by_locator_multiple_elements: Проверяет получение нескольких элементов.
 - test_get_webelement_by_locator_no_element: Проверяет случай, когда элемент не найден.
 - test_get_attribute_by_locator: Проверяет получение атрибута элемента.
 - test_send_message: Проверяет отправку сообщения элементу.
 - test_send_message_typing_speed: Проверяет отправку сообщения элементу с задержкой между символами.
"""

import pytest
from unittest.mock import MagicMock, patch, create_autospec
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from src.webdriver.executor import ExecuteLocator
from src.logger.exceptions import ExecuteLocatorException

@pytest.fixture
def driver_mock():
    return MagicMock()

@pytest.fixture
def execute_locator(driver_mock):
    return ExecuteLocator(driver_mock)

def test_get_webelement_by_locator_single_element(execute_locator, driver_mock):
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]

    locator = {
        "by": "XPATH",
        "selector": "//div[@id='test']"
    }
    
    result = execute_locator.get_webelement_by_locator(locator)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@id='test']")
    assert result == element

def test_get_webelement_by_locator_multiple_elements(execute_locator, driver_mock):
    elements = [MagicMock(spec=WebElement) for _ in range(3)]
    driver_mock.find_elements.return_value = elements

    locator = {
        "by": "XPATH",
        "selector": "//div[@class='test']"
    }

    result = execute_locator.get_webelement_by_locator(locator)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@class='test']")
    assert result == elements

def test_get_webelement_by_locator_no_element(execute_locator, driver_mock):
    driver_mock.find_elements.return_value = []

    locator = {
        "by": "XPATH",
        "selector": "//div[@id='not_exist']"
    }

    result = execute_locator.get_webelement_by_locator(locator)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@id='not_exist']")
    assert result is False

def test_get_attribute_by_locator(execute_locator, driver_mock):
    element = MagicMock(spec=WebElement)
    element.get_attribute.return_value = "test_value"
    driver_mock.find_elements.return_value = [element]

    locator = {
        "by": "XPATH",
        "selector": "//div[@id='test']",
        "attribute": "data-test"
    }

    result = execute_locator.get_attribute_by_locator(locator)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@id='test']")
    element.get_attribute.assert_called_once_with("data-test")
    assert result == "test_value"

def test_send_message(execute_locator, driver_mock):
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]

    locator = {
        "by": "XPATH",
        "selector": "//input[@id='test']"
    }
    message = "Hello World"

    result = execute_locator.send_message(locator, message, typing_speed=0, continue_on_error=True)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//input[@id='test']")
    element.send_keys.assert_called_once_with(message)
    assert result is True

def test_send_message_typing_speed(execute_locator, driver_mock):
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]

    locator = {
        "by": "XPATH",
        "selector": "//input[@id='test']"
    }
    message = "Hello"
    typing_speed = 0.1

    with patch('time.sleep', return_value=None) as mock_sleep:
        result = execute_locator.send_message(locator, message, typing_speed=typing_speed, continue_on_error=True)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//input[@id='test']")
    assert element.send_keys.call_count == len(message)
    mock_sleep.assert_called_with(typing_speed)
    assert result is True

