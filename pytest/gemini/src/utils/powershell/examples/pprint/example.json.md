```python
import pytest
import json

# Since the input code is a JSON object, we'll create a fixture to load and provide it for tests.
@pytest.fixture
def example_json_data():
    """Provides the example JSON data as a Python dictionary."""
    json_string = """
    {
      "keys": {
        "key_hello": {
          "messages": [
            {
              "en": "Hello, World!"
            },
            {
              "ru": "Привет, Мир!"
            }
          ]
        },
        "key_goodbye": {
          "messages": [
            {
              "en": "Have a nice day!"
            },
            {
              "ru": "Всего хорошего!"
            }
          ]
        }
      }
    }
    """
    return json.loads(json_string)

def test_example_json_data_structure(example_json_data):
    """Test if the basic structure of the loaded JSON is correct."""
    assert isinstance(example_json_data, dict)
    assert "keys" in example_json_data
    assert isinstance(example_json_data["keys"], dict)


def test_example_json_data_key_hello_exists(example_json_data):
    """Test if the key_hello key exists in 'keys'"""
    assert "key_hello" in example_json_data["keys"]


def test_example_json_data_key_goodbye_exists(example_json_data):
    """Test if the key_goodbye key exists in 'keys'"""
    assert "key_goodbye" in example_json_data["keys"]

def test_example_json_data_key_hello_messages_structure(example_json_data):
    """Test the structure of the messages under key_hello"""
    assert "messages" in example_json_data["keys"]["key_hello"]
    assert isinstance(example_json_data["keys"]["key_hello"]["messages"], list)
    assert len(example_json_data["keys"]["key_hello"]["messages"]) == 2
    assert isinstance(example_json_data["keys"]["key_hello"]["messages"][0], dict)
    assert isinstance(example_json_data["keys"]["key_hello"]["messages"][1], dict)

def test_example_json_data_key_goodbye_messages_structure(example_json_data):
    """Test the structure of the messages under key_goodbye"""
    assert "messages" in example_json_data["keys"]["key_goodbye"]
    assert isinstance(example_json_data["keys"]["key_goodbye"]["messages"], list)
    assert len(example_json_data["keys"]["key_goodbye"]["messages"]) == 2
    assert isinstance(example_json_data["keys"]["key_goodbye"]["messages"][0], dict)
    assert isinstance(example_json_data["keys"]["key_goodbye"]["messages"][1], dict)


def test_example_json_data_key_hello_messages_content(example_json_data):
    """Test the content of messages under key_hello"""
    messages = example_json_data["keys"]["key_hello"]["messages"]
    assert "en" in messages[0]
    assert messages[0]["en"] == "Hello, World!"
    assert "ru" in messages[1]
    assert messages[1]["ru"] == "Привет, Мир!"

def test_example_json_data_key_goodbye_messages_content(example_json_data):
    """Test the content of messages under key_goodbye"""
    messages = example_json_data["keys"]["key_goodbye"]["messages"]
    assert "en" in messages[0]
    assert messages[0]["en"] == "Have a nice day!"
    assert "ru" in messages[1]
    assert messages[1]["ru"] == "Всего хорошего!"
```