```python
import pytest
from hypotez.src.webdriver.edge import Edge  # Assuming Edge class is in edge.py

# Fixture definitions, if needed
@pytest.fixture
def valid_edge_options():
    """Provides valid options for Edge."""
    return {
        "headless": False,
        "disable_gpu": False,
        "user_data_dir": "test_user_data_dir",
        "profile_dir": "test_profile_dir",
        "binary_location": "test_binary_location",
        "arguments": ["--test-arg1", "--test-arg2"],
        "prefs": {"test_pref1": "test_val1"},
        "extensions_paths": ["test_ext1", "test_ext2"]
    }

@pytest.fixture
def invalid_edge_options():
    """Provides invalid options for Edge."""
    return {
        "headless": "invalid_value",
        "disable_gpu": 123,
        "user_data_dir": 123,
        "profile_dir": None,
        "binary_location": None,
        "arguments": 123,
        "prefs": "invalid",
        "extensions_paths": None
    }

# Tests for Edge class initialization
def test_edge_init_valid_options(valid_edge_options):
    """Checks correct initialization of Edge with valid options."""
    edge = Edge(**valid_edge_options)
    assert edge.options.headless == valid_edge_options["headless"]
    assert edge.options.disable_gpu == valid_edge_options["disable_gpu"]
    assert edge.options.user_data_dir == valid_edge_options["user_data_dir"]
    assert edge.options.profile_dir == valid_edge_options["profile_dir"]
    assert edge.options.binary_location == valid_edge_options["binary_location"]
    assert edge.options.arguments == valid_edge_options["arguments"]
    assert edge.options.prefs == valid_edge_options["prefs"]
    assert edge.options.extensions_paths == valid_edge_options["extensions_paths"]
    
    # Additional check to make sure all expected attributes are initialized
    assert hasattr(edge, 'webdriver_path')
    assert hasattr(edge, 'webdriver')
    

def test_edge_init_default_options():
    """Checks correct initialization of Edge with default options."""
    edge = Edge()
    assert edge.options.headless is False
    assert edge.options.disable_gpu is False
    assert edge.options.user_data_dir is None
    assert edge.options.profile_dir is None
    assert edge.options.binary_location is None
    assert edge.options.arguments == []
    assert edge.options.prefs == {}
    assert edge.options.extensions_paths == []

def test_edge_init_invalid_options(invalid_edge_options):
    """Checks that incorrect types for options raise a ValueError during init."""
    with pytest.raises(ValueError):
        Edge(**invalid_edge_options)

def test_edge_init_invalid_option_key():
    """Checks that invalid option keys raise a TypeError during init."""
    with pytest.raises(TypeError):
        Edge(invalid_option="invalid_key")

# Test for start() method of Edge class
# NOTE:
# These test will require mocked WebDriver to actually work since they can't 
# actually start a browser or webdriver. It's recommended to mock or patch the call
# to the actual Selenium WebDriver in this case.
@pytest.mark.skip(reason="Skipping until a way to mock or patch the selenium calls is added.")
def test_edge_start_valid_driver():
    """Checks if driver starts with a valid configuration"""
    edge = Edge()
    edge.start()
    assert edge.webdriver is not None
    assert edge.webdriver.name == "msedge"
    edge.webdriver.quit()

@pytest.mark.skip(reason="Skipping until a way to mock or patch the selenium calls is added.")
def test_edge_start_already_started():
     """Checks if start() raises an exception when called while there is already a driver."""
     edge = Edge()
     edge.start()
     with pytest.raises(Exception):
          edge.start()
     edge.webdriver.quit() # Important to stop running driver.
    
@pytest.mark.skip(reason="Skipping until a way to mock or patch the selenium calls is added.")
def test_edge_close_valid_driver():
     """Checks if driver is closed with a valid configuration"""
     edge = Edge()
     edge.start()
     assert edge.webdriver is not None
     edge.close()
     assert edge.webdriver is None

def test_edge_close_no_driver():
     """Checks if calling close() when no driver is present is handled properly"""
     edge = Edge()
     edge.close()
     assert edge.webdriver is None
```