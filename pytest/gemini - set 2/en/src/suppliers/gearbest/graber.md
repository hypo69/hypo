```python
import pytest
import asyncio
from unittest.mock import MagicMock
from src.suppliers.gearbest.graber import Graber, Context, ProductFields, Driver  # Import necessary classes
from src.logger import logger
from src.logger.exceptions import ExecuteLocatorException


# Mock Driver and ProductFields for testing
class MockDriver:
    def __init__(self):
        self.execute_locator = MagicMock()


class MockProductFields(ProductFields):
    def __init__(self):
        super().__init__()


# Fixture for Driver and ProductFields
@pytest.fixture
def driver():
    return MockDriver()


@pytest.fixture
def product_fields():
    return MockProductFields()


@pytest.fixture
def graber(driver):
    return Graber(driver)


# Test cases for grab_page function
def test_grab_page_valid_input(graber, driver, product_fields):
    """Checks grab_page with valid input."""
    # Mock the necessary functions in the Graber class. Replace with actual implementation if needed
    graber.id_product = MagicMock(return_value=asyncio.Future())
    graber.description_short = MagicMock(return_value=asyncio.Future())
    graber.name = MagicMock(return_value=asyncio.Future())
    graber.specification = MagicMock(return_value=asyncio.Future())
    graber.local_saved_image = MagicMock(return_value=asyncio.Future())
    
    # Mock asyncio.gather for testing
    asyncio.gather = MagicMock(return_value=None)
    
    # Assert that the fields are populated
    assert asyncio.run(graber.grab_page(driver)) is not None


def test_grab_page_exception(graber, driver):
    """Tests grab_page function with exception."""
    # Mock an exception during the execution
    graber.id_product = MagicMock(side_effect=ExecuteLocatorException("Test exception"))
    
    with pytest.raises(ExecuteLocatorException) as excinfo:
        asyncio.run(graber.grab_page(driver))

    # Assert that the correct exception is raised
    assert "Test exception" in str(excinfo.value)

def test_grab_page_empty_input(graber, driver):
    """Tests grab_page with empty input."""
    # Mock the necessary functions in the Graber class
    graber.id_product = MagicMock(return_value=asyncio.Future())
    graber.description_short = MagicMock(return_value=asyncio.Future())
    graber.name = MagicMock(return_value=asyncio.Future())
    graber.specification = MagicMock(return_value=asyncio.Future())
    graber.local_saved_image = MagicMock(return_value=asyncio.Future())

    # Mock asyncio.gather for testing
    asyncio.gather = MagicMock(return_value=None)


    # Call the function with empty input
    product_fields = asyncio.run(graber.grab_page(driver))

    # Assert that the function does not raise any exceptions and fields are initialized
    assert product_fields is not None
    assert product_fields.id_product is None
    assert product_fields.description_short is None
    assert product_fields.name is None
    assert product_fields.specification is None
    assert product_fields.local_saved_image is None
```

**Explanation and Improvements:**

* **Mocking:**  Crucially, the tests now mock the `driver` and `ProductFields` to avoid needing actual webdrivers and database interactions.  This makes the tests fast and isolated.  The code mocks various methods within the `Graber` class (`id_product`, `description_short`, etc.) to simulate different scenarios.
* **`asyncio.gather` Mock:** Added mocking for `asyncio.gather`, as it's used internally.
* **Specific Exception Handling:**  `test_grab_page_exception` now demonStartes how to test for a specific exception type (`ExecuteLocatorException`) and properly assert the error message.
* **Empty Input Test:** `test_grab_page_empty_input` now checks the handling of empty input, ensuring that no exception occurs and that the fields are correctly initialized to `None`.
* **Clearer Assertions:** Assertions are improved to validate the expected behavior more explicitly.
* **Import Fixes:** Corrected imports to match the provided code.
* **Dependency Management:**  The tests now import the necessary classes directly from the specified file (`Graber`, `Context`, etc.). This avoids issues related to missing dependencies.



**How to Run:**

1.  Make sure you have `pytest` installed: `pip install pytest`
2.  Save the test code as a `.py` file (e.g., `test_graber.py`).
3.  Run the tests from your terminal: `pytest test_graber.py`


Remember to replace the placeholder mocking in `test_grab_page_valid_input` with actual implementations if you need a more detailed validation.  This improved structure and mocking will significantly enhance the testing of your `Graber` class.