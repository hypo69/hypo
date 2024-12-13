```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def config_data():
    """Provides the JSON configuration data."""
    return {
        "storage": "external_storage",
        "storage_choices": [
            "external_storage",
            "data",
            "google_drive"
        ],
        "model": "gemini-2.0-flash-exp",
        "model_choices": [
            "gemini-2.0-flash-exp",
            "gemini-1.5-flash-8b-exp-0924",
            "gemini-1.5-flash"
        ]
    }


def test_config_data_storage_valid(config_data):
    """Checks that the storage value is within the allowed storage choices."""
    assert config_data["storage"] in config_data["storage_choices"]

def test_config_data_model_valid(config_data):
    """Checks that the model value is within the allowed model choices."""
    assert config_data["model"] in config_data["model_choices"]

def test_config_data_storage_invalid():
    """Checks behavior when storage value is not in allowed choices. """
    config_data = {
        "storage": "invalid_storage",
        "storage_choices": ["external_storage", "data", "google_drive"],
        "model": "gemini-2.0-flash-exp",
        "model_choices": ["gemini-2.0-flash-exp", "gemini-1.5-flash-8b-exp-0924", "gemini-1.5-flash"]
    }
    with pytest.raises(AssertionError):
        assert config_data["storage"] in config_data["storage_choices"]

def test_config_data_model_invalid():
    """Checks behavior when model value is not in allowed choices. """
    config_data = {
        "storage": "external_storage",
        "storage_choices": ["external_storage", "data", "google_drive"],
        "model": "invalid_model",
        "model_choices": ["gemini-2.0-flash-exp", "gemini-1.5-flash-8b-exp-0924", "gemini-1.5-flash"]
    }
    with pytest.raises(AssertionError):
        assert config_data["model"] in config_data["model_choices"]


def test_config_data_empty_choices():
    """Checks behavior when choices are empty."""
    config_data = {
        "storage": "external_storage",
        "storage_choices": [],
        "model": "gemini-2.0-flash-exp",
        "model_choices": []
    }
    with pytest.raises(AssertionError):
         assert config_data["storage"] in config_data["storage_choices"]
    with pytest.raises(AssertionError):
         assert config_data["model"] in config_data["model_choices"]


def test_config_data_missing_keys():
    """Checks behavior when essential keys are missing."""
    config_data_no_storage = {
        "storage_choices": ["external_storage", "data", "google_drive"],
        "model": "gemini-2.0-flash-exp",
        "model_choices": ["gemini-2.0-flash-exp", "gemini-1.5-flash-8b-exp-0924", "gemini-1.5-flash"]
    }
    config_data_no_model = {
        "storage": "external_storage",
        "storage_choices": ["external_storage", "data", "google_drive"],
        "model_choices": ["gemini-2.0-flash-exp", "gemini-1.5-flash-8b-exp-0924", "gemini-1.5-flash"]
    }
    with pytest.raises(KeyError):
        _ = config_data_no_storage["storage"]
    with pytest.raises(KeyError):
        _ = config_data_no_model["model"]

def test_config_data_storage_choices_not_list():
        """Checks behavior when storage_choices is not a list."""
        config_data = {
            "storage": "external_storage",
            "storage_choices": "not_a_list",
            "model": "gemini-2.0-flash-exp",
            "model_choices": ["gemini-2.0-flash-exp", "gemini-1.5-flash-8b-exp-0924", "gemini-1.5-flash"]
        }
        with pytest.raises(TypeError):
             assert config_data["storage"] in config_data["storage_choices"]
def test_config_data_model_choices_not_list():
        """Checks behavior when model_choices is not a list."""
        config_data = {
            "storage": "external_storage",
            "storage_choices": ["external_storage", "data", "google_drive"],
            "model": "gemini-2.0-flash-exp",
            "model_choices": "not_a_list"
        }
        with pytest.raises(TypeError):
             assert config_data["model"] in config_data["model_choices"]

def test_config_data_valid_with_extra_fields(config_data):
    """ Checks valid config with extra fields."""
    config_data["extra_field"] = "extra_value"
    assert config_data["storage"] in config_data["storage_choices"]
    assert config_data["model"] in config_data["model_choices"]
```