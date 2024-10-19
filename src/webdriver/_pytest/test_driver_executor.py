## \file src/webdriver/_pytest/test_driver_executor.py
## \file ../src/webdriver/_pytest/test_driver_executor.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Общий тест для driver и executor
test_navigate_to_page: Проверяет, что WebDriver корректно загружает указанную страницу.
test_get_webelement_by_locator_single_element: Проверяет, что метод get_webelement_by_locator корректно возвращает элемент по локатору.
test_get_webelement_by_locator_no_element: Проверяет, что метод get_webelement_by_locator возвращает False, если элемент не найден.
test_send_message: Проверяет, что метод send_message корректно отправляет сообщение элементу.
test_get_attribute_by_locator: Проверяет, что метод get_attribute_by_locator корректно возвращает атрибут элемента.
test_execute_locator_event: Проверяет, что метод execute_locator корректно выполняет событие на локаторе.
test_get_locator_keys: Проверяет, что метод get_locator_keys возвращает правильные ключи локатора.
test_navigate_and_interact: Проверяет последовательность навигации и взаимодействия с элементами на другой странице.
test_invalid_locator: Проверяет обработку некорректных локаторов и соответствующее исключение.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.webdriver.executor import ExecuteLocator
from src.logger.exceptions import ExecuteLocatorException

@pytest.fixture(scope="module")
def driver():
    """Fixture to set up and tear down the WebDriver."""
    options = Options()
    options.add_argument("--headless")  # Run headless browser for testing
    service = Service(executable_path="/path/to/chromedriver")  # Path to your chromedriver
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://example.com")  # URL for the tests
    yield driver
    driver.quit()

@pytest.fixture
def execute_locator(driver):
    """Fixture to initialize the ExecuteLocator instance."""
    return ExecuteLocator(driver)

# Примеры тестов для взаимодействия с WebDriver и ExecuteLocator

def test_navigate_to_page(execute_locator, driver):
    """Test to ensure that the WebDriver can navigate to a page."""
    assert driver.current_url == "http://example.com"

def test_get_webelement_by_locator_single_element(execute_locator, driver):
    """Test to get a single web element by locator."""
    locator = {
        "by": "XPATH",
        "selector": "//h1"
    }
    element = execute_locator.get_webelement_by_locator(locator)
    assert isinstance(element, WebElement)
    assert element.text == "Example Domain"

def test_get_webelement_by_locator_no_element(execute_locator, driver):
    """Test when no element is found by the locator."""
    locator = {
        "by": "XPATH",
        "selector": "//div[@id='nonexistent']"
    }
    result = execute_locator.get_webelement_by_locator(locator)
    assert result is False

def test_send_message(execute_locator, driver):
    """Test sending a message to a web element."""
    locator = {
        "by": "XPATH",
        "selector": "//input[@id='search']"  # Change to an actual input field if available
    }
    message = "Hello World"
    result = execute_locator.send_message(locator, message, typing_speed=0, continue_on_error=True)
    assert result is True

def test_get_attribute_by_locator(execute_locator, driver):
    """Test to get an attribute value from a web element."""
    locator = {
        "by": "XPATH",
        "selector": "//a[@id='more-information']"
    }
    attribute_value = execute_locator.get_attribute_by_locator(locator, message="href")
    assert attribute_value == "https://www.iana.org/domains/example"  # Update based on actual attribute value

def test_execute_locator_event(execute_locator, driver):
    """Test to ensure that an event is correctly triggered on the locator."""
    locator = {
        "by": "XPATH",
        "selector": "//a[@id='more-information']"
    }
    result = execute_locator.execute_locator(locator, message="click")
    assert result is True  # Ensure that the event was triggered as expected

def test_get_locator_keys(execute_locator, driver):
    """Test to get available locator keys."""
    expected_keys = [
        'attribute',
        'by',
        'selector',
        'event',
        'use_mouse',
        'mandatory',
        'locator_description',
    ]
    result = ExecuteLocator.get_locator_keys()
    assert set(result) == set(expected_keys)

def test_navigate_and_interact(execute_locator, driver):
    """Test to navigate to a page and interact with elements."""
    # Navigate to a new page
    driver.get("https://www.wikipedia.org/")
    assert driver.current_url == "https://www.wikipedia.org/"
    
    # Find and click the search input field
    locator = {
        "by": "XPATH",
        "selector": "//input[@id='searchInput']"
    }
    execute_locator.send_message(locator, "Selenium", typing_speed=0, continue_on_error=True)
    
    # Find and click the search button
    locator = {
        "by": "XPATH",
        "selector": "//button[@type='submit']"
    }
    execute_locator.execute_locator(locator, message="click")

    # Validate that the search results page is loaded
    assert "Selenium" in driver.title

    # Optionally check for an element on the results page
    result_locator = {
        "by": "XPATH",
        "selector": "//h1[contains(text(), 'Selenium')]"
    }
    result = execute_locator.get_webelement_by_locator(result_locator)
    assert isinstance(result, WebElement)
    assert result.text == "Selenium"

def test_invalid_locator(execute_locator, driver):
    """Test handling of invalid locators."""
    locator = {
        "by": "INVALID_BY",
        "selector": "//div[@id='test']"
    }
    with pytest.raises(ExecuteLocatorException):
        execute_locator.execute_locator(locator, message="click")

