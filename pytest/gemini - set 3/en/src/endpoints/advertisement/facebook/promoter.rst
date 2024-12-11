```python
import pytest
import re
from datetime import datetime, timedelta
from urllib.parse import urlencode
from types import SimpleNamespace
from pathlib import Path

from hypotez.src.endpoints.advertisement.facebook.promoter import (
    FacebookPromoter,
    get_event_url,
    parse_interval,
    check_interval,
)
from hypotez.src import gs


# Dummy data for fixtures (replace with actual data loading)
@pytest.fixture
def dummy_driver():
    class MockDriver:
        def get_url(self, url):
            return True

        def quit(self):
            pass
    return MockDriver()


@pytest.fixture
def dummy_group():
    return SimpleNamespace(
        group_url="https://www.facebook.com/groups/12345",
        group_categories=["sales", "marketing"],
        language="en",
        currency="USD",
        interval="1H",
        last_promo_sended="01/01/23 10:00",
        promoted_categories=[],
        promoted_events=[],
        status="active"
    )


@pytest.fixture
def dummy_item():
    return SimpleNamespace(
        event_name="Test Event",
        category_name="Test Category",
        start=datetime.now(),
        end=datetime.now() + timedelta(days=1),
        promotional_link="https://example.com",
        language=SimpleNamespace(en="test"),
    )

@pytest.fixture
def dummy_group_file_paths():
    return ["ru_usd.json", "usa.json", "ger_en_eur.json", "he_il.json", "ru_il.json"]


def test_get_event_url(dummy_group):
    """Tests the get_event_url function with valid input."""
    expected_url = "https://www.facebook.com/events/create/?acontext=%7B%22event_action_history%22%3A%5B%7B%22surface%22%3A%22group%22%7D%2C%7B%22mechanism%22%3A%22upcoming_events_for_group%22%2C%22surface%22%3A%22group%22%7D%5D%2C%22ref_notif_type%22%3Anull%7D&dialog_entry_point=group_events_tab&group_id=12345"
    actual_url = get_event_url(dummy_group.group_url)
    assert actual_url == expected_url


def test_check_interval_valid_input(dummy_group):
    """Tests check_interval with a valid interval and recent promotion."""
    assert check_interval(dummy_group)


def test_check_interval_interval_not_passed(dummy_group):
    """Tests check_interval with an interval that hasn't passed."""
    dummy_group.last_promo_sended = datetime.now().strftime("%d/%m/%y %H:%M")
    assert not check_interval(dummy_group)


def test_check_interval_invalid_interval_format(dummy_group):
    """Tests check_interval with an invalid interval format."""
    dummy_group.interval = "invalid_format"
    with pytest.raises(ValueError):
        check_interval(dummy_group)


def test_parse_interval(dummy_group):
    """Tests parse_interval with a valid interval."""
    interval = "1H"
    expected_timedelta = timedelta(hours=1)
    actual_timedelta = parse_interval(interval)
    assert actual_timedelta == expected_timedelta


def test_parse_interval_invalid_format(dummy_group):
    """Tests parse_interval with an invalid interval."""
    interval = "invalid"
    with pytest.raises(ValueError):
        parse_interval(interval)


def test_promote_valid_input(dummy_driver, dummy_group, dummy_item):
    """Tests promote function with valid input and successful posting."""
    promoter = FacebookPromoter(d=dummy_driver, promoter="test", group_file_paths=None)
    result = promoter.promote(group=dummy_group, item=dummy_item)
    assert result is True
    


# Add more test cases for other functions like process_groups, run_campaigns, etc.
#  These would require more complex mock data and assertions.
# Example for process_groups:
# def test_process_groups_valid_input(dummy_driver, dummy_group, dummy_item, dummy_group_file_paths):
#     # ... (mock data and assertions)


# Remember to adapt the test cases to the specific logic of your functions
# and ensure they effectively cover the possible scenarios.
```

**Explanation and Improvements:**

1. **Dummy Fixtures:**  Crucially, I've added dummy fixtures (`dummy_driver`, `dummy_group`, `dummy_item`, `dummy_group_file_paths`) to mock the necessary objects.  This is essential for unit testing because your `FacebookPromoter` class relies on external dependencies like a `Driver` object, group data, and items.  These fixtures provide realistic-looking but controllable data. **Replace the dummy data with actual data loading** if possible.


2. **Clear Test Cases:**  The tests are now much more specific and cover different cases (valid interval, invalid interval format).


3. **`pytest.raises`:**  I've included an example using `pytest.raises` to test the expected exception when the interval format is invalid.

4. **Complete Coverage (Important):** The previous response lacked comprehensive tests. This updated example includes a test for `get_event_url` and `check_interval`, but more tests are needed.  Focus on edge cases (e.g., empty lists, incorrect data types), invalid inputs, and scenarios where exceptions are raised.

5. **`SimpleNamespace` Handling:** The tests now correctly use the `SimpleNamespace` objects, as expected in the original code.

6. **Example for `process_groups` (placeholder):** The comment demonStartes how you should add a test for the `process_groups` function. You'll need to mock data for campaigns, file paths, and other arguments to appropriately test this function.


**How to Run the Tests:**

1.  Make sure you have `pytest` installed:
    ```bash
    pip install pytest
    ```

2.  Save the test code (as `test_promoter.py` for example) in the same directory as the `promoter.py` file.

3.  Run the tests from your terminal:
    ```bash
    pytest test_promoter.py
    ```

**Crucial Next Steps:**

*   **Mock Data Loading:**  Replace the dummy data fixtures with fixtures that load actual data from your data sources (JSON files, databases, etc.). This makes the tests significantly more realistic.
*   **Comprehensive Tests for `process_groups` and `run_campaigns`:** These are critical functions, and you need extensive tests to cover different scenarios (empty lists, invalid campaigns, errors during promotion, etc.). Use mocks to isolate these functions from external dependencies.
*   **Test Exception Handling:** Thoroughly test that your functions handle potential exceptions (e.g., invalid file paths, invalid JSON data, errors during web requests) gracefully.
*   **Data Validation:** Ensure your tests validate the format of the input data, such as checking that your JSON files are correctly structured.


By adding more detailed mock data, extensive tests for `process_groups`, `run_campaigns`, exception handling, and data validation, you'll create a much more robust test suite. Remember to keep the test data separate from the test code and use fixtures effectively to control the testing environment.