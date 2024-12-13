```python
import pytest
from unittest.mock import MagicMock, patch
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


# Constants for file paths
POPUP_FILE_PATH = "hypotez/src/webdriver/chrome/extentions/openai/popup.html"
CHROME_DRIVER_PATH = 'chromedriver'


@pytest.fixture(scope="module")
def chrome_options():
    """Provides Chrome options for the test."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    return options


@pytest.fixture(scope="module")
def driver(chrome_options):
    """Provides a WebDriver instance for the tests."""
    driver = webdriver.Chrome(options=chrome_options, executable_path=CHROME_DRIVER_PATH)
    file_path = os.path.abspath(POPUP_FILE_PATH)
    driver.get(f'file://{file_path}')
    yield driver
    driver.quit()

def wait_for_element(driver, by, locator, timeout=10):
    """Waits for an element to be present using WebDriverWait."""
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located((by, locator)))

def get_element_text(driver, by, locator):
    """Finds an element and gets its text."""
    element = wait_for_element(driver, by, locator)
    return element.text

def send_input_element(driver, by, locator, value):
    """Finds an input element and sends it value"""
    element = wait_for_element(driver, by, locator)
    element.send_keys(value)
    return element

def click_element(driver, by, locator):
    """Finds a clickable element and clicks it"""
    element = wait_for_element(driver, by, locator)
    element.click()


def test_popup_loads_successfully(driver):
    """Verifies that the popup page loads successfully by checking the title."""
    assert "OpenAI Model Interface" in driver.title

def test_initial_tab_is_chat(driver):
    """Verify that the initial active tab is 'Chat'."""
    chat_tab = wait_for_element(driver, By.XPATH, "//li[contains(text(), 'Chat')]")
    assert "active" in chat_tab.get_attribute("class")
    assert wait_for_element(driver, By.XPATH, "//div[h2[contains(text(), 'Chat with Model')]]").is_displayed()
    assert not wait_for_element(driver, By.XPATH, "//div[h2[contains(text(), 'Model Training and Status')]]").is_displayed()

def test_switch_to_model_tab(driver):
    """Verify that switching to the 'Model' tab works correctly."""
    # Switch to model tab
    model_tab = wait_for_element(driver, By.XPATH, "//li[contains(text(), 'Model')]")
    model_tab.click()
    assert "active" in model_tab.get_attribute("class")
    assert wait_for_element(driver, By.XPATH, "//div[h2[contains(text(), 'Model Training and Status')]]").is_displayed()
    assert not wait_for_element(driver, By.XPATH, "//div[h2[contains(text(), 'Chat with Model')]]").is_displayed()

def test_switch_back_to_chat_tab(driver):
    """Verify that switching back to the 'Chat' tab from 'Model' tab works correctly."""
    # Switch to chat tab
    chat_tab = wait_for_element(driver, By.XPATH, "//li[contains(text(), 'Chat')]")
    chat_tab.click()
    assert "active" in chat_tab.get_attribute("class")
    assert wait_for_element(driver, By.XPATH, "//div[h2[contains(text(), 'Chat with Model')]]").is_displayed()
    assert not wait_for_element(driver, By.XPATH, "//div[h2[contains(text(), 'Model Training and Status')]]").is_displayed()

def test_chat_tab_elements_present(driver):
    """Verifies that the elements within the 'Chat' tab are displayed."""
    # check elements
    wait_for_element(driver, By.XPATH, "//h2[contains(text(), 'Chat with Model')]")
    wait_for_element(driver, By.ID, "assistants")
    wait_for_element(driver, By.XPATH, "//textarea[@placeholder='Enter your message']")
    wait_for_element(driver, By.XPATH, "//button[contains(text(), 'Send')]")
    wait_for_element(driver, By.ID, "response")

def test_model_tab_elements_present(driver):
    """Verifies that the elements within the 'Model' tab are displayed."""
    click_element(driver, By.XPATH, "//li[contains(text(), 'Model')]")
    wait_for_element(driver, By.XPATH, "//h2[contains(text(), 'Model Training and Status')]")
    wait_for_element(driver, By.XPATH, "//textarea[@placeholder='Enter training data']")
    wait_for_element(driver, By.XPATH, "//button[contains(text(), 'Train')]")
    wait_for_element(driver, By.XPATH, "//h3[contains(text(), 'Training Status:')]")
    # switch back to chat tab
    click_element(driver, By.XPATH, "//li[contains(text(), 'Chat')]")

def test_chat_send_message_button_present(driver):
    """Verifies that the 'Send' button in chat tab is present"""
    send_button = wait_for_element(driver, By.XPATH, "//button[contains(text(), 'Send')]")
    assert send_button.is_displayed()

def test_model_train_button_present(driver):
    """Verifies that the 'Train' button in model tab is present"""
    click_element(driver, By.XPATH, "//li[contains(text(), 'Model')]")
    train_button = wait_for_element(driver, By.XPATH, "//button[contains(text(), 'Train')]")
    assert train_button.is_displayed()
    # switch back to chat tab
    click_element(driver, By.XPATH, "//li[contains(text(), 'Chat')]")
    
def test_chat_message_input(driver):
    """Verifies that the message input in chat tab works correctly"""
    input_element = send_input_element(driver, By.XPATH, "//textarea[@placeholder='Enter your message']", "Test message")
    assert input_element.get_attribute("value") == "Test message"

def test_model_training_data_input(driver):
    """Verifies that the training data input in model tab works correctly"""
    click_element(driver, By.XPATH, "//li[contains(text(), 'Model')]")
    input_element = send_input_element(driver, By.XPATH, "//textarea[@placeholder='Enter training data']", "Test training data")
    assert input_element.get_attribute("value") == "Test training data"
    # switch back to chat tab
    click_element(driver, By.XPATH, "//li[contains(text(), 'Chat')]")
```