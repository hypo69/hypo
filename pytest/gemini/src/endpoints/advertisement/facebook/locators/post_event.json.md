```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def event_locators():
    """Loads the JSON data for testing."""
    json_data = """
    {
      "event_title": {
        "attribute": null,
        "by": "XPATH",
        "selector": "//label[@aria-label = 'Название мероприятия']//input",
        "if_list":"first","use_mouse": false,
        "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click();%EXTERNAL_MESSAGE%",
        "mandatory": true,
        "locator_description": "поле ввода названия сообщения. При переходе по специально сконструированной ссылке откроется сразу. См код сценария"
    
      },
      "start_date": {
        "attribute": null,
        "by": "XPATH",
        "selector": "//label[@aria-label = 'Дата начала']//input",
        "if_list":"first","use_mouse": false,
        "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click();backspace(10);%EXTERNAL_MESSAGE%",
        "mandatory": true,
        "locator_description": "поле ввода даты начала мероприятия"
    
      },
      "start_time": {
        "attribute": null,
        "by": "XPATH",
        "selector": "//label[@aria-label = 'Время начала']//input",
        "if_list":"first","use_mouse": false,
        "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click();backspace();%EXTERNAL_MESSAGE%",
        "mandatory": true,
        "locator_description": "поле ввода даты начала мероприятия"
      },
    
      "event_description": {
        "attribute": null,
        "by": "XPATH",
        "selector": "//label[@aria-label = 'Расскажите подробнее о мероприятии.']//textarea",
        "if_list":"first","use_mouse": false,
        "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click();%EXTERNAL_MESSAGE%",
        "mandatory": true,
        "locator_description": "поле ввода даты начала мероприятия"
      },
    
    
      "event_send": {
        "attribute": null,
        "by": "XPATH",
        "selector": "//div[@aria-label = 'Создать мероприятие']",
        "if_list":"first","use_mouse": false,
        "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()",
        "mandatory": true,
        "locator_description": "Кнопка отправки"
    
      }
    }
    """
    return json.loads(json_data)

def test_event_title_locator(event_locators):
    """Test the event_title locator configuration."""
    title_locator = event_locators["event_title"]
    assert title_locator["by"] == "XPATH"
    assert title_locator["selector"] == "//label[@aria-label = 'Название мероприятия']//input"
    assert title_locator["if_list"] == "first"
    assert title_locator["use_mouse"] is False
    assert title_locator["timeout"] == 0
    assert title_locator["timeout_for_event"] == "presence_of_element_located"
    assert title_locator["event"] == "click();%EXTERNAL_MESSAGE%"
    assert title_locator["mandatory"] is True
    assert title_locator["locator_description"] == "поле ввода названия сообщения. При переходе по специально сконструированной ссылке откроется сразу. См код сценария"


def test_start_date_locator(event_locators):
    """Test the start_date locator configuration."""
    date_locator = event_locators["start_date"]
    assert date_locator["by"] == "XPATH"
    assert date_locator["selector"] == "//label[@aria-label = 'Дата начала']//input"
    assert date_locator["if_list"] == "first"
    assert date_locator["use_mouse"] is False
    assert date_locator["timeout"] == 0
    assert date_locator["timeout_for_event"] == "presence_of_element_located"
    assert date_locator["event"] == "click();backspace(10);%EXTERNAL_MESSAGE%"
    assert date_locator["mandatory"] is True
    assert date_locator["locator_description"] == "поле ввода даты начала мероприятия"
    
def test_start_time_locator(event_locators):
    """Test the start_time locator configuration."""
    time_locator = event_locators["start_time"]
    assert time_locator["by"] == "XPATH"
    assert time_locator["selector"] == "//label[@aria-label = 'Время начала']//input"
    assert time_locator["if_list"] == "first"
    assert time_locator["use_mouse"] is False
    assert time_locator["timeout"] == 0
    assert time_locator["timeout_for_event"] == "presence_of_element_located"
    assert time_locator["event"] == "click();backspace();%EXTERNAL_MESSAGE%"
    assert time_locator["mandatory"] is True
    assert time_locator["locator_description"] == "поле ввода даты начала мероприятия"

def test_event_description_locator(event_locators):
    """Test the event_description locator configuration."""
    description_locator = event_locators["event_description"]
    assert description_locator["by"] == "XPATH"
    assert description_locator["selector"] == "//label[@aria-label = 'Расскажите подробнее о мероприятии.']//textarea"
    assert description_locator["if_list"] == "first"
    assert description_locator["use_mouse"] is False
    assert description_locator["timeout"] == 0
    assert description_locator["timeout_for_event"] == "presence_of_element_located"
    assert description_locator["event"] == "click();%EXTERNAL_MESSAGE%"
    assert description_locator["mandatory"] is True
    assert description_locator["locator_description"] == "поле ввода даты начала мероприятия"

def test_event_send_locator(event_locators):
    """Test the event_send locator configuration."""
    send_locator = event_locators["event_send"]
    assert send_locator["by"] == "XPATH"
    assert send_locator["selector"] == "//div[@aria-label = 'Создать мероприятие']"
    assert send_locator["if_list"] == "first"
    assert send_locator["use_mouse"] is False
    assert send_locator["timeout"] == 0
    assert send_locator["timeout_for_event"] == "presence_of_element_located"
    assert send_locator["event"] == "click()"
    assert send_locator["mandatory"] is True
    assert send_locator["locator_description"] == "Кнопка отправки"


def test_all_locators_present(event_locators):
    """Test that all expected locators are present in the JSON data."""
    expected_keys = ["event_title", "start_date", "start_time", "event_description", "event_send"]
    assert all(key in event_locators for key in expected_keys)

def test_locator_values_not_empty(event_locators):
  """Test that all locators contain data"""
  for locator in event_locators.values():
    assert locator
    for field in locator.values():
        assert field is not None
```