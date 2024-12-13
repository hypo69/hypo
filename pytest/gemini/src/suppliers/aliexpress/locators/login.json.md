```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def login_data():
    """Loads the login data from the JSON file."""
    file_path = 'hypotez/src/suppliers/aliexpress/locators/login.json'  
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Test cases for 'login' locators
def test_login_close_banner_locator(login_data):
    """Tests the close banner locator."""
    locator = login_data['login']['close banner']
    assert locator['attribute'] == "text"
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//div[contains(text(), \'אפשר\')]"
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "send_keys(Key.RETURN)"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True

def test_login_open_login_locator(login_data):
     """Tests the open login locator."""
     locator = login_data['login']['open_login']
     assert locator['attribute'] is None
     assert locator['by'] == "XPATH"
     assert locator['selector'] == "//div[@class = \'account-main\']//span[. = \'Sign in\'] | //div[@class = \'account-main\']//span[. = \'Se connecter\'] | //div[@class = \'account-main\']//span[. = \'כניסה\'] "
     assert locator['timeout'] == 0
     assert locator['timeout_for_event'] == "presence_of_element_located"
     assert locator['event'] == "click()"
     assert locator['if_list'] == "first"
     assert locator['use_mouse'] is False
     assert locator['mandatory'] is True

def test_login_email_locator(login_data):
    """Tests the email locator."""
    locator = login_data['login']['email_locator']
    assert locator['attribute'] is None
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//input[@id=\'fm-login-id\']"
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "send_keys(\'one.last.bit@gmail.com\')"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True

def test_login_password_locator(login_data):
    """Tests the password locator."""
    locator = login_data['login']['password_locator']
    assert locator['attribute'] is None
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//input[@id=\'fm-login-password\']"
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "send_keys(\'7p3ato9kijsosw7\')"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True

def test_login_loginbutton_locator(login_data):
    """Tests the login button locator."""
    locator = login_data['login']['loginbutton_locator']
    assert locator['attribute'] is None
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//button[@type=\'submit\']"
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "click()"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True

def test_login_cookies_accept_locator(login_data):
    """Tests the cookies accept locator."""
    locator = login_data['login']['cookies_accept']
    assert locator['attribute'] is None
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//button[contains(@data-role,\'gdpr-accept\')]"
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "click()"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True


# Test cases for 'currency_language_shipto_locators'

def test_currency_language_shipto_block_opener_locator(login_data):
     """Tests the block opener locator."""
     locator = login_data['currency_language_shipto_locators']['currency_language_shipto_block_opener_locator']
     assert locator['attribute'] is None
     assert locator['by'] == "XPATH"
     assert locator['selector'] == "//div[@data-role = \'region-pannel\']/a"
     assert locator['timeout'] == 0
     assert locator['timeout_for_event'] == "presence_of_element_located"
     assert locator['event'] == "click()"
     assert locator['if_list'] == "first"
     assert locator['use_mouse'] is False
     assert locator['mandatory'] is True

def test_shipto_locator(login_data):
    """Tests the shipto locator."""
    locator = login_data['currency_language_shipto_locators']['shipto_locator']
    assert locator['attribute'] == [None, None, None]
    assert locator['by'] == ["XPATH", "XPATH", "XPATH"]
    assert locator['selector'] == [
        "//a[contains(@class,\'address-select-trigger\') and contains(@data-role,\'country\')]",
        "//div[@class = \'filter-list-container\']",
        "//li[contains(@data-code,\'il\')]"
    ]
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == ["click()", "click()", "click()"]
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True


def test_language_locator(login_data):
    """Tests the language locator."""
    locator = login_data['currency_language_shipto_locators']['language_locator']
    assert locator['attribute'] == [None, None, None]
    assert locator['by'] == ["XPATH", "XPATH", "XPATH"]
    assert locator['selector'] == [
        "//span[contains( @data-role , \'language-input\')]",
        "//input[contains(@data-role,\'language-search\')]",
        "//a[contains(@data-locale,\'en-US\')]"
    ]
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == ["click()", "click()", "click()"]
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True


def test_currency_locator(login_data):
    """Tests the currency locator."""
    locator = login_data['currency_language_shipto_locators']['currency_locator']
    assert locator['attribute'] == [None, None, None]
    assert locator['by'] == ["XPATH", "XPATH", "XPATH"]
    assert locator['selector'] == [
        "//div[contains(@class , \'switcher-currency-c language-selector\')]",
        "//span[contains(@class , \'select-item\')]",
        "//a[contains(@data-currency , \'ILS\')]"
    ]
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == ["click()", "click()", "click()"]
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True


def test_save_button_locator(login_data):
    """Tests the save button locator."""
    locator = login_data['currency_language_shipto_locators']['save_button_locator']
    assert locator['attribute'] is None
    assert locator['by'] == "XPATH"
    assert locator['selector'] == "//div[contains(@class , \'switcher-btn\')]"
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "click()"
    assert locator['if_list'] == "first"
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
```