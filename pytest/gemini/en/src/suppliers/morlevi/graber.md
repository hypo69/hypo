```python
import pytest
import asyncio
from pathlib import Path
from unittest.mock import patch
from types import SimpleNamespace
from src.suppliers import Graber, Context, close_pop_up
from src.product import ProductFields
from src.webdriver import Driver
from src.utils.jjson import j_loads_ns
from src.utils.image import save_png
from src.logger import logger
from src.logger.exceptions import ExecuteLocatorException

# Mock the webdriver for testing
@pytest.fixture
def mock_driver():
    class MockDriver:
        async def execute_locator(self, locator):
            if locator == 'close_pop_up':
                return "Pop-up closed"
            elif locator == 'default_image_url':
                return b"Image bytes"
            else:
                raise ExecuteLocatorException("Locator not found")
        async def close(self):
            pass
        
    return MockDriver()

@pytest.fixture
def graber(mock_driver):
    graber = Graber(mock_driver)
    graber.fields = ProductFields()
    return graber

# Mock save_png to avoid file interaction
@pytest.fixture
def mock_save_png():
    def mock_save_png_func(raw, path):
        return str(path)

    return mock_save_png_func


# Mock the logger for testing
@pytest.fixture
def mock_logger():
    mock_logger = logger
    mock_logger.debug = lambda msg, ex: None
    mock_logger.error = lambda msg, ex: None
    return mock_logger


def test_local_saved_image_success(graber, mock_save_png, mock_driver, mock_logger):
    # Arrange
    graber.fields.id_product = "123"
    # Patch save_png to avoid file interaction
    with patch('src.suppliers.morlevi.graber.save_png', mock_save_png):
        # Act
        asyncio.run(graber.local_saved_image())
    
    # Assert
    assert graber.fields.local_saved_image == str(Path(Graber.gs.path.tmp / f'123.png'))


def test_local_saved_image_id_product_missing(graber, mock_logger):
    # Arrange
    graber.fields.id_product = None
    # Act and Assert
    with pytest.raises(ExecuteLocatorException):
        asyncio.run(graber.local_saved_image())


def test_local_saved_image_error(graber, mock_driver, mock_logger):
    # Arrange
    graber.fields.id_product = "123"
    
    # Mock a failure for execute_locator (e.g., element not found)
    with patch('src.suppliers.morlevi.graber.Driver', autospec=True) as mock_driver_cls:
      mock_driver_instance = mock_driver_cls.return_value
      mock_driver_instance.execute_locator.side_effect = ExecuteLocatorException("Mock error")

      with pytest.raises(ExecuteLocatorException):
        asyncio.run(graber.local_saved_image())


def test_local_saved_image_no_image_returned(graber, mock_driver, mock_logger):
    # Arrange
    graber.fields.id_product = "123"
    # Mock a failure for image retrieval
    with patch('src.suppliers.morlevi.graber.Driver', autospec=True) as mock_driver_cls:
      mock_driver_instance = mock_driver_cls.return_value
      mock_driver_instance.execute_locator.return_value = [None]


      with pytest.raises(Exception) as excinfo:
        asyncio.run(graber.local_saved_image())

      assert "Ошибка сохранения изображения" in str(excinfo.value)

```

**Explanation and Improvements:**

* **Mocking:**  Crucially, the code now mocks the `Driver` and `save_png` functions. This is essential for unit testing because it isolates the `Graber` class from external dependencies like the web driver and file system.  Without mocking, the tests would fail if `Context.driver` or `save_png` couldn't connect to the outside world, and they'd create real files which is undesirable and makes tests harder to run in CI.
* **`pytest.raises` for Exceptions:** Uses `pytest.raises` correctly to verify that the expected exceptions are raised in specific failure cases.
* **Clearer Test Cases:**  Test names are more specific and descriptive (e.g., `test_local_saved_image_success`, `test_local_saved_image_error`).
* **Edge Case Testing:** Includes a test (`test_local_saved_image_id_product_missing`) for the case where `id_product` is missing, which is a critical edge case.
* **Mocking Logger:** The test now correctly mocks the logger (`mock_logger`) so it won't print to the console and won't interfere with your actual application's logging.
* **Comprehensive Error Handling:** Added tests to handle cases where `execute_locator` fails (element not found, general error) and where the image retrieval returns an empty value.


**How to Run:**

1.  Install `pytest`:
    ```bash
    pip install pytest
    ```

2.  Run the tests:
    ```bash
    pytest hypotez/tests/suppliers/morlevi/test_graber.py
    ```

**Important Considerations (and next steps):**

* **`gs.path` and `Context`:** The tests need to have access to the `gs.path` variable.  If `gs.path` is a global variable, you'll need to set it properly. Otherwise, add it as a fixture to the `test_graber.py` file and pass it into your test functions:

```python
import pytest
from src.utils import gs

@pytest.fixture
def gs_path_fixture():
    # Set the value of gs.path correctly for testing.  This depends on the way gs.path is set up.
    gs.path = Path("./tmp")  # Example - a temporary directory
    return gs.path


# ... (rest of your test file)

def test_local_saved_image_success(graber, mock_save_png, mock_driver, mock_logger, gs_path_fixture):
    # ... (rest of your test)
```

* **`ProductFields` Initialization:**   This example mocks `ProductFields()`, but you should make sure this is appropriately initialized in your tests.


This significantly improved solution ensures your tests are more reliable and comprehensive, allowing for early detection of potential issues. Remember to adapt the mocking and fixture definitions to match the actual implementation of your code.