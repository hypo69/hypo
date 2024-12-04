```python
import pytest
from src.webdriver import Driver, Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def driver_instance():
    """Provides a Driver instance for testing."""
    driver = Driver(Chrome)
    yield driver
    driver.quit()


def test_get_url_valid(driver_instance):
    """Tests successful navigation to a valid URL."""
    result = driver_instance.get_url("https://www.example.com")
    assert result is True, "Navigation failed"


def test_get_url_invalid(driver_instance):
    """Tests navigation to an invalid URL (should not raise exception)."""
    result = driver_instance.get_url("invalid_url")
    assert result is False, "Navigation succeeded unexpectedly"


def test_extract_domain(driver_instance):
    """Tests extracting the domain from a URL."""
    driver_instance.get_url("https://www.example.com/path/to/page")
    domain = driver_instance.extract_domain("https://www.example.com/path/to/page")
    assert domain == "example.com", f"Incorrect domain extracted: {domain}"

def test_extract_domain_invalid(driver_instance):
    """Tests extraction of domain from an invalid URL."""
    domain = driver_instance.extract_domain("invalid_url")
    assert domain == None, f"Domain extracted from an invalid URL: {domain}"



def test_save_cookies(driver_instance):
    """Tests saving cookies to a local file."""
    driver_instance.get_url("https://www.example.com")
    success = driver_instance._save_cookies_localy()
    assert success is True, "Cookies were not saved successfully"

def test_page_refresh(driver_instance):
    """Tests refreshing the current page."""
    driver_instance.get_url("https://www.example.com")
    success = driver_instance.page_refresh()
    assert success is True, "Page refresh failed."


def test_scroll(driver_instance):
    """Tests scrolling the page down."""
    driver_instance.get_url("https://www.example.com")
    success = driver_instance.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1)
    assert success is True, "Scrolling failed."


def test_locale(driver_instance):
    """Tests getting the language of the current page."""
    driver_instance.get_url("https://www.example.com")
    page_language = driver_instance.locale
    # Check that locale is not None.  Actual language checking is beyond the scope of these tests.
    assert page_language is not None, "Page language is None"


def test_custom_user_agent(driver_instance):
    """Tests setting a custom user agent."""
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    custom_driver = Driver(Chrome, user_agent=user_agent)
    success = custom_driver.get_url("https://www.example.com")
    assert success is True, "Navigation failed with custom user agent."


def test_find_element_success(driver_instance):
    """Tests finding an element by CSS selector."""
    driver_instance.get_url("https://www.example.com")
    element = driver_instance.find_element(By.CSS_SELECTOR, "h1")
    assert element is not None, "Element not found"


def test_find_element_failure(driver_instance):
    """Tests handling of NoSuchElementException."""
    driver_instance.get_url("https://www.example.com")
    with pytest.raises(NoSuchElementException):
        driver_instance.find_element(By.CSS_SELECTOR, "nonexistent_element")


def test_current_url(driver_instance):
    """Tests getting the current URL."""
    driver_instance.get_url("https://www.example.com")
    current_url = driver_instance.current_url
    assert current_url == "https://www.example.com"


def test_window_focus(driver_instance):
    """Tests focusing the window."""
    driver_instance.get_url("https://www.example.com")
    driver_instance.window_focus()
```

**Explanation and Improvements:**

* **Fixtures:**  A `driver_instance` fixture is introduced to manage the driver creation and teardown within each test, ensuring that each test uses a fresh driver instance. This prevents issues caused by state retention between tests.
* **`driver_instance.quit()` in fixture:** Crucially, the `driver.quit()` method is now called in the fixture's `yield` block. This is *essential* to ensure that each test works correctly and doesn't leave browser windows or resources hanging around.
* **Explicit Assertions:** Instead of relying on printing, the tests now use `assert` statements to verify expected results. This is critical for proper testing.
* **Invalid URL Handling:** Added `test_get_url_invalid` to test the handling of an invalid URL.
* **Invalid URL Extraction:** Added `test_extract_domain_invalid` to test the handling of an invalid URL for domain extraction
* **Exception Handling:** The `test_find_element_failure` test demonstrates how to use `pytest.raises` to verify that the expected exception (`NoSuchElementException`) is raised when an element is not found.
* **Realistic Checks (Locale):** The `test_locale` test now checks if the `page_language` is not `None`, which is a more realistic assertion for checking if the method returned something.  Actual language validation is beyond the scope of this test.
* **Clearer Test Names:** Test names are more descriptive, making the purpose of each test immediately apparent.


**Before running these tests:**

1.  **Install pytest:**
    ```bash
    pip install pytest
    ```

2.  **Install Selenium:**
    ```bash
    pip install selenium
    ```

3.  **Have your `src.webdriver` module:**  Make sure the `Driver` and `Chrome` classes exist in the `src/webdriver` location.


Now, running `pytest` in the same directory as your test file should execute these tests and report the results. Remember to replace `"https://www.example.com"` with a valid URL during testing if needed.   Adjust imports and file paths as needed for your project structure. Remember to install the necessary dependencies.