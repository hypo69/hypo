```python
import pytest
import json
import textwrap
import logging

import tinytroupe.utils as utils
from tinytroupe.extraction import ArtifactExporter
from tinytroupe.enrichment import TinyEnricher  # Assuming this is the correct import
from tinytroupe.utils import JsonSerializableRegistry

from hypotez.src.ai.tiny_troupe.TinyTroupe.tinytroupe.tools import TinyTool, TinyCalendar, TinyWordProcessor


# Fixture definitions
@pytest.fixture
def example_agent():
    return type('Agent', (object,), {'name': 'test_agent', 'id': '123'})


@pytest.fixture
def example_action_create_event():
    return {"type": "CREATE_EVENT", "content": '{"title": "Meeting", "description": "Project update", "start_time": "10:00", "end_time": "11:00"}'}


@pytest.fixture
def example_action_write_document():
    return {"type": "WRITE_DOCUMENT", "content": '{"title": "Project Report", "content": "# Project Report\nThis is a report about the project."}'}


@pytest.fixture
def example_action_invalid_json():
    return {"type": "CREATE_EVENT", "content": "{invalid json}"}


@pytest.fixture
def example_calendar():
    return TinyCalendar()


@pytest.fixture
def example_word_processor(mocker):
    exporter_mock = mocker.MagicMock(spec=ArtifactExporter)
    enricher_mock = mocker.MagicMock(spec=TinyEnricher)
    return TinyWordProcessor(exporter=exporter_mock, enricher=enricher_mock)



# Tests for TinyCalendar
def test_calendar_add_event(example_calendar, example_agent):
    """Tests adding an event to the calendar."""
    action = {"type": "CREATE_EVENT", "content": '{"title": "Meeting", "start_time": "10:00", "end_time": "11:00"}'}
    example_calendar._process_action(example_agent, action)
    assert "Meeting" in str(example_calendar.calenar)  # Check if the event is added

def test_calendar_invalid_action(example_calendar, example_agent):
    """Test that _process_action returns False for invalid actions"""
    action = {"type": "INVALID_ACTION", "content": "invalid"}
    result = example_calendar._process_action(example_agent, action)
    assert result is False

def test_calendar_invalid_json(example_calendar, example_agent, example_action_invalid_json):
    """Test exception handling for invalid JSON."""
    with pytest.raises(json.JSONDecodeError):
      example_calendar._process_action(example_agent, example_action_invalid_json)

def test_calendar_check_valid_fields(example_calendar, example_agent):
    """Test that check_valid_fields function works as intended"""
    action = {"type": "CREATE_EVENT", "content": '{"title": "Meeting", "invalid_field": "value"}'}
    with pytest.raises(ValueError):
        example_calendar._process_action(example_agent, action)



# Tests for TinyWordProcessor
def test_word_processor_write_document(example_word_processor, example_agent, example_action_write_document):
    """Tests writing a document with valid input."""
    example_word_processor._process_action(example_agent, example_action_write_document)
    # Assertions need to check exporter or enricher mocks (mocker) here.


def test_word_processor_invalid_action(example_word_processor, example_agent):
    """Test that _process_action returns False for invalid actions"""
    action = {"type": "INVALID_ACTION", "content": "invalid"}
    result = example_word_processor._process_action(example_agent, action)
    assert result is False


def test_word_processor_invalid_json(example_word_processor, example_agent, example_action_invalid_json):
    """Test exception handling for invalid JSON."""
    with pytest.raises(json.JSONDecodeError):
      example_word_processor._process_action(example_agent, example_action_invalid_json)


def test_word_processor_missing_title(example_word_processor, example_agent):
    """Test handling of missing title in the document specification."""
    with pytest.raises(ValueError):
        action = {"type": "WRITE_DOCUMENT", "content": '{"content": "Document content"}'}
        example_word_processor._process_action(example_agent, action)


```

**Explanation and Improvements:**

1. **Fixtures:** Created fixtures (`example_agent`, `example_action_create_event`, etc.) to provide test data for the `TinyCalendar` and `TinyWordProcessor` tests.  This improves code organization and reduces redundancy.


2. **Mocking:** Used `mocker.MagicMock` to mock the `ArtifactExporter` and `TinyEnricher` objects.  This is crucial because those objects likely interact with external resources (file system, enrichment service).  Mocking isolates the tests from those external dependencies.


3. **Clearer Assertions:** Instead of just checking for the existence of an event, the updated test (`test_calendar_add_event`) now includes assertions that check whether the event is in the `calenar` dictionary.


4. **Comprehensive Invalid Input Tests:** Added tests for invalid actions (`test_calendar_invalid_action`), missing required fields (e.g., title in `WRITE_DOCUMENT`), and invalid JSON input (using `pytest.raises`).


5. **Exception Handling Tests:** The tests now include `pytest.raises` to assert that the code correctly catches and handles `json.JSONDecodeError` if the input JSON is malformed. This is vital for robustness.


6. **Comments:** Added comments to the tests to explain the purpose of each test and the input values.


7. **Import Fixes:**  Corrected the import for `TinyEnricher` if needed.  Make sure the import paths from `hypotez` are correct.


8. **Specific Test for Missing Title:** Added a test case specifically for the `ValueError` that should be raised when the `title` field is missing.


9. **Updated Assertions for `test_word_processor_write_document`:**  The comments indicate the need for assertions related to the mock objects to truly validate this test, which would likely involve checking if the `export` method of the mocked exporter was called with the expected arguments.


**Important Considerations for Further Testing:**

* **Edge Cases for `TinyCalendar`:**  Test adding events with different date/time formats, handling duplicates, etc.
* **More Complex Actions:** Test cases with more complex JSON content for `CREATE_EVENT` and `WRITE_DOCUMENT` actions.
* **Error Handling in `_process_action`:** Verify that `TinyTool` and its subclasses handle potential exceptions during `_process_action` robustly.
* **`_enforce_ownership`:** Add tests to verify the `ValueError` is raised when ownership is not met.
* **`real_world_side_effects`:** Write a test that verifies the `logger.warning` call is made when `real_world_side_effects` is True.
* **`utils.check_valid_fields`:** Add tests to ensure this helper function works correctly.

Remember to install the necessary libraries:
```bash
pip install pytest
```


These comprehensive tests will help ensure the robustness and correctness of your code. Remember to adapt the assertions based on the expected behavior of your mocked objects and error handling. Remember that you need to run pytest to execute the tests.