```python
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from hypotez.src.webdriver.executor import ExecuteLocator
from hypotez.src.logger.exceptions import ExecuteLocatorException
from unittest.mock import MagicMock

# Fixture for setting up a mock WebDriver and ExecuteLocator
@pytest.fixture
def mock_driver():
    """Provides a mock WebDriver instance."""
    mock_driver = MagicMock(spec=webdriver.Chrome)
    mock_driver.get.return_value = None
    mock_element = MagicMock()
    mock_element.text = "Test Header"
    mock_element.get_attribute.return_value = "test_attribute_value"
    mock_driver.find_element.return_value = mock_element
    mock_driver.find_elements.return_value = [mock_element]
    return mock_driver

@pytest.fixture
def executor(mock_driver):
    """Provides an ExecuteLocator instance with a mock driver."""
    return ExecuteLocator(mock_driver)


# Test cases for execute_locator method
def test_execute_locator_simple(executor, mock_driver):
    """Checks the correct behavior of execute_locator with a simple locator."""
    simple_locator = {
        "by": "XPATH",
        "selector": "//h1",
        "attribute": "textContent",
        "timeout":0,
        "timeout_for_event":"presence_of_element_located",
        "event": None,
        "if_list":"first",
        "use_mouse": False,
        "mandatory": True,
        "locator_description": "Получение заголовка страницы"
    }
    result = executor.execute_locator(simple_locator)
    assert result == "Test Header"
    mock_driver.find_element.assert_called_once_with(By.XPATH, "//h1")

def test_execute_locator_complex(executor, mock_driver):
    """Checks the correct behavior of execute_locator with a complex locator."""
    complex_locator = {
        "product_links": {
            "attribute": "href",
            "by": "XPATH",
            "selector": "//a[contains(@class, 'product')]",
            "timeout": 0,
            "timeout_for_event": "presence_of_element_located",
            "event": None,
            "if_list":"first",
            "use_mouse": False,
            "mandatory": True,
            "locator_description": "Получение ссылки на продукт"
        },
        "pagination": {
            "ul": {
                "attribute": None,
                "by": "XPATH",
                "selector": "//ul[@class='pagination']",
                "timeout": 0,
                "timeout_for_event": "presence_of_element_located",
                "event": "click()",
                "if_list":"first",
                "use_mouse": False,
                "mandatory": True,
                "locator_description": "Нажатие на пагинацию"
            },
            "->": {
                "attribute": None,
                "by": "XPATH",
                "selector": "//*[@class = 'ui-pagination-navi util-left']/a[@class='ui-pagination-next']",
                 "timeout": 0,
                 "timeout_for_event": "presence_of_element_located",
                "event": "click()",
                "if_list":"first",
                "use_mouse": False,
                "mandatory": True,
                "locator_description": "Клик по следующей странице"
            }
        }
    }
    result = executor.execute_locator(complex_locator)
    assert result is None  # Expected return is None when clicks are performed
    mock_driver.find_element.assert_called_with(By.XPATH, "//*[@class = 'ui-pagination-navi util-left']/a[@class='ui-pagination-next']")


def test_execute_locator_continue_on_error(executor, mock_driver):
    """Checks the correct behavior when continue_on_error is True."""
    mock_driver.find_element.side_effect = Exception("Element not found")
    complex_locator = {
        "product_links": {
            "attribute": "href",
            "by": "XPATH",
            "selector": "//a[contains(@class, 'product')]",
            "timeout": 0,
            "timeout_for_event": "presence_of_element_located",
            "event": None,
            "if_list":"first",
            "use_mouse": False,
            "mandatory": True,
            "locator_description": "Получение ссылки на продукт"
        },
        "pagination": {
            "ul": {
                "attribute": None,
                "by": "XPATH",
                "selector": "//ul[@class='pagination']",
                "timeout": 0,
                "timeout_for_event": "presence_of_element_located",
                "event": "click()",
                "if_list":"first",
                "use_mouse": False,
                "mandatory": True,
                "locator_description": "Нажатие на пагинацию"
            },
            "->": {
                "attribute": None,
                "by": "XPATH",
                "selector": "//*[@class = 'ui-pagination-navi util-left']/a[@class='ui-pagination-next']",
                 "timeout": 0,
                 "timeout_for_event": "presence_of_element_located",
                "event": "click()",
                "if_list":"first",
                "use_mouse": False,
                "mandatory": True,
                "locator_description": "Клик по следующей странице"
            }
        }
    }
    try:
      result = executor.execute_locator(complex_locator, continue_on_error=True)
      assert result is None
    except ExecuteLocatorException:
      pytest.fail("Exception was not expected")

def test_execute_locator_exception(executor, mock_driver):
    """Checks that execute_locator raises an exception when continue_on_error is False and element is not found."""
    mock_driver.find_element.side_effect = Exception("Element not found")
    simple_locator = {
        "by": "XPATH",
        "selector": "//h1",
        "attribute": "textContent",
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": None,
        "if_list": "first",
        "use_mouse": False,
        "mandatory": True,
        "locator_description": "Получение заголовка страницы"
    }
    with pytest.raises(ExecuteLocatorException) as ex:
        executor.execute_locator(simple_locator)
    assert str(ex.value) == 'Element not found'

def test_execute_locator_with_send_message(executor, mock_driver):
    """Checks correct behaviour with send message"""
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    message_locator = {
        "by": "XPATH",
        "selector": "//input[@name='search']",
        "attribute": None,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": "%SEARCH%",
        "if_list":"first",
        "use_mouse": False,
        "mandatory": True,
        "locator_description": "Отправка поискового запроса"
    }
    message = "Купить новый телефон"
    result = executor.send_message(message_locator, message, typing_speed=0.05, continue_on_error=True)
    assert result is None  # Expects None as result
    mock_element.send_keys.assert_called_once_with("Купить новый телефон")

def test_execute_locator_with_multi_locator(executor, mock_driver):
    """Checks behavior of execute_locator with multiple locators."""
    mock_element = MagicMock()
    mock_element.text = "submit"
    mock_element.get_attribute.return_value = 'user'
    mock_driver.find_elements.return_value = [mock_element]
    multi_locator = {
        "by": ["XPATH", "XPATH"],
        "selector": ["//button[@id='submit']", "//input[@id='username']"],
        "attribute": ["textContent", "value"],
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": ["click()", "send_keys('user')"],
        "if_list":"first",
        "use_mouse": [True, False],
        "mandatory": [True, True],
        "locator_description": ["Нажатие кнопки отправки", "Ввод имени пользователя"]
    }

    results = executor.execute_locator(multi_locator)
    assert results == ["submit", "user"]
    mock_driver.find_element.assert_called_with(By.XPATH, "//input[@id='username']")

def test_evaluate_locator(executor, mock_driver):
    """Checks the evaluate_locator method."""
    mock_element = MagicMock()
    mock_element.get_attribute.return_value = "test_content"
    mock_driver.find_element.return_value = mock_element
    attribute_locator = {
        "by": "XPATH",
        "selector": "//meta[@name='description']",
        "attribute": "content",
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": None,
        "if_list":"first",
        "use_mouse": False,
        "mandatory": True,
        "locator_description": "Получение значения мета-описания страницы"
    }
    attribute_value = executor.evaluate_locator(attribute_locator['attribute'])
    assert attribute_value == "test_content"
    mock_driver.find_element.assert_called_once_with(By.XPATH, "//meta[@name='description']")


def test_evaluate_locator_exception(executor, mock_driver):
    """Checks that evaluate_locator raises exception if no element found"""
    mock_driver.find_element.side_effect = Exception("Element not found")
    attribute_locator = {
        "by": "XPATH",
        "selector": "//meta[@name='description']",
        "attribute": "content",
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": None,
        "if_list":"first",
        "use_mouse": False,
        "mandatory": True,
        "locator_description": "Получение значения мета-описания страницы"
    }
    with pytest.raises(ExecuteLocatorException) as ex:
        executor.evaluate_locator(attribute_locator['attribute'])
    assert str(ex.value) == 'Element not found'

def test_send_message_continue_on_error(executor, mock_driver):
    """Tests send_message with continue_on_error set to True"""
    mock_driver.find_element.side_effect = Exception("Element not found")
    message_locator = {
        "by": "XPATH",
        "selector": "//input[@name='search']",
        "attribute": None,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": "%SEARCH%",
        "if_list": "first",
        "use_mouse": False,
        "mandatory": True,
        "locator_description": "Отправка поискового запроса"
    }
    message = "Купить новый телефон"
    try:
      result = executor.send_message(message_locator, message, typing_speed=0.05, continue_on_error=True)
      assert result is None
    except ExecuteLocatorException:
      pytest.fail("Exception was not expected")

def test_send_message_exception(executor, mock_driver):
    """Tests send_message with exception"""
    mock_driver.find_element.side_effect = Exception("Element not found")
    message_locator = {
        "by": "XPATH",
        "selector": "//input[@name='search']",
        "attribute": None,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": "%SEARCH%",
        "if_list": "first",
        "use_mouse": False,
        "mandatory": True,
        "locator_description": "Отправка поискового запроса"
    }
    message = "Купить новый телефон"
    with pytest.raises(ExecuteLocatorException) as ex:
        executor.send_message(message_locator, message, typing_speed=0.05, continue_on_error=False)
    assert str(ex.value) == 'Element not found'
```