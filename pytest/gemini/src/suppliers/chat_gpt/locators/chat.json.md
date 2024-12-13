```python
import pytest
import json


@pytest.fixture
def chat_locators():
    """Provides a fixture with the chat locator data loaded from the JSON."""
    json_data = """
    {
      "assistant": {
        "attribute": null,
        "by": "XPATH",
        "selector": "//div[@data-message-author-role='assistant']",
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": null,
        "if_list": "first",
        "use_mouse": false,
        "mandatory": true,
        "locator_description": "Я получаю весь контейнер и в коде вытескиваю .text"
      },
      "user": {
        "attribute": null,
        "by": "XPATH",
        "selector": "//div[@data-message-author-role='user']",
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": null,
        "if_list": "first",
        "use_mouse": false,
        "mandatory": true,
        "locator_description": "Я получаю весь контейнер и в коде вытескиваю .text"
      }
    }
    """
    return json.loads(json_data)


def test_chat_locators_structure(chat_locators):
    """Tests if the loaded JSON has the expected top-level keys ('assistant' and 'user')."""
    assert "assistant" in chat_locators
    assert "user" in chat_locators

def test_assistant_locator_keys(chat_locators):
    """Tests if the 'assistant' locator has all expected keys."""
    assistant_locator = chat_locators["assistant"]
    expected_keys = {"attribute", "by", "selector", "timeout", "timeout_for_event", "event", "if_list", "use_mouse", "mandatory", "locator_description"}
    assert set(assistant_locator.keys()) == expected_keys

def test_user_locator_keys(chat_locators):
    """Tests if the 'user' locator has all expected keys."""
    user_locator = chat_locators["user"]
    expected_keys = {"attribute", "by", "selector", "timeout", "timeout_for_event", "event", "if_list", "use_mouse", "mandatory", "locator_description"}
    assert set(user_locator.keys()) == expected_keys

def test_assistant_locator_values(chat_locators):
    """Tests the values for 'assistant' locator."""
    assistant_locator = chat_locators["assistant"]

    assert assistant_locator["attribute"] is None
    assert assistant_locator["by"] == "XPATH"
    assert assistant_locator["selector"] == "//div[@data-message-author-role='assistant']"
    assert assistant_locator["timeout"] == 0
    assert assistant_locator["timeout_for_event"] == "presence_of_element_located"
    assert assistant_locator["event"] is None
    assert assistant_locator["if_list"] == "first"
    assert assistant_locator["use_mouse"] is False
    assert assistant_locator["mandatory"] is True
    assert assistant_locator["locator_description"] == "Я получаю весь контейнер и в коде вытескиваю .text"

def test_user_locator_values(chat_locators):
    """Tests the values for 'user' locator."""
    user_locator = chat_locators["user"]

    assert user_locator["attribute"] is None
    assert user_locator["by"] == "XPATH"
    assert user_locator["selector"] == "//div[@data-message-author-role='user']"
    assert user_locator["timeout"] == 0
    assert user_locator["timeout_for_event"] == "presence_of_element_located"
    assert user_locator["event"] is None
    assert user_locator["if_list"] == "first"
    assert user_locator["use_mouse"] is False
    assert user_locator["mandatory"] is True
    assert user_locator["locator_description"] == "Я получаю весь контейнер и в коде вытескиваю .text"

def test_chat_locators_empty_json():
  """Tests the behaviour with an empty JSON"""
  empty_json = "{}"
  with pytest.raises(KeyError):
     json.loads(empty_json)["assistant"]

def test_chat_locators_invalid_json():
  """Tests the behaviour with an invalid JSON"""
  invalid_json = "invalid json"
  with pytest.raises(json.JSONDecodeError):
     json.loads(invalid_json)
```