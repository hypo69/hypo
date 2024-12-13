```python
import pytest
import os
import json
import configparser
from datetime import datetime
from tinytroupe import utils
from unittest.mock import mock_open, patch
from pytest import raises

# Fixture to provide test data for the template rendering
@pytest.fixture
def mock_template_files(tmp_path):
    """Creates mock template files for testing."""
    system_template_content = "System: {{variable}}"
    user_template_content = "User: {{variable}}"
    
    system_template_path = tmp_path / "system_template.md"
    user_template_path = tmp_path / "user_template.md"

    with open(system_template_path, 'w') as f:
        f.write(system_template_content)
    with open(user_template_path, 'w') as f:
        f.write(user_template_content)
        
    return str(system_template_path.resolve()), str(user_template_path.resolve())


# Tests for compose_initial_LLM_messages_with_templates
def test_compose_initial_LLM_messages_with_templates_valid(mock_template_files, monkeypatch):
    """Checks correct message composition with system and user templates."""
    system_template_path, user_template_path = mock_template_files
    
    monkeypatch.setattr(os.path, "join", lambda *args: str(args[-1]))
    monkeypatch.setattr(os.path, "dirname", lambda *args: "")
    monkeypatch.setattr(utils.chevron, "render", lambda text, data: text.replace("{{variable}}", data.get("variable")))
    
    messages = utils.compose_initial_LLM_messages_with_templates(
        system_template_name=system_template_path,
        user_template_name=user_template_path,
        rendering_configs={"variable": "test"}
    )
    assert len(messages) == 2
    assert messages[0]["role"] == "system"
    assert messages[0]["content"] == "System: test"
    assert messages[1]["role"] == "user"
    assert messages[1]["content"] == "User: test"

def test_compose_initial_LLM_messages_with_templates_no_user_template(mock_template_files, monkeypatch):
    """Checks message composition with only system template."""
    system_template_path, _ = mock_template_files
    monkeypatch.setattr(os.path, "join", lambda *args: str(args[-1]))
    monkeypatch.setattr(os.path, "dirname", lambda *args: "")
    monkeypatch.setattr(utils.chevron, "render", lambda text, data: text.replace("{{variable}}", data.get("variable")))

    messages = utils.compose_initial_LLM_messages_with_templates(
        system_template_name=system_template_path,
        rendering_configs={"variable": "test"}
    )
    assert len(messages) == 1
    assert messages[0]["role"] == "system"
    assert messages[0]["content"] == "System: test"

def test_compose_initial_LLM_messages_with_templates_no_rendering_config(mock_template_files, monkeypatch):
    """Checks message composition without rendering config."""
    system_template_path, user_template_path = mock_template_files
    monkeypatch.setattr(os.path, "join", lambda *args: str(args[-1]))
    monkeypatch.setattr(os.path, "dirname", lambda *args: "")
    monkeypatch.setattr(utils.chevron, "render", lambda text, data: text.replace("{{variable}}", ""))

    messages = utils.compose_initial_LLM_messages_with_templates(
        system_template_name=system_template_path,
        user_template_name=user_template_path
    )
    assert len(messages) == 2
    assert messages[0]["role"] == "system"
    assert messages[0]["content"] == "System: "
    assert messages[1]["role"] == "user"
    assert messages[1]["content"] == "User: "


# Tests for extract_json
def test_extract_json_valid_json():
    """Checks extraction of valid JSON from a string."""
    text = 'some text {"key": "value"} more text'
    expected_json = {"key": "value"}
    assert utils.extract_json(text) == expected_json

def test_extract_json_with_markdown_tags():
    """Checks extraction of JSON with Markdown tags."""
    text = '```json\n{"key": "value"}\n```'
    expected_json = {"key": "value"}
    assert utils.extract_json(text) == expected_json

def test_extract_json_invalid_json():
    """Checks handling of invalid JSON."""
    text = 'some text {invalid json} more text'
    assert utils.extract_json(text) == {}

def test_extract_json_empty_string():
    """Checks handling of an empty string."""
    text = ''
    assert utils.extract_json(text) == {}

def test_extract_json_no_json():
    """Checks when no JSON is present in the string."""
    text = 'some text with no json'
    assert utils.extract_json(text) == {}

def test_extract_json_with_escaped_quotes():
    """Checks handling of escaped quotes in JSON."""
    text = '{"key": "\\"value\\""}'
    expected_json = {"key": "\"value\""}
    assert utils.extract_json(text) == expected_json
    
def test_extract_json_with_invalid_escape_sequences():
    """Checks handling of invalid escape sequences in JSON."""
    text = '{\'key\': \\\'value\\\'}'
    expected_json = {"key": "\'value\'"}
    assert utils.extract_json(text) == expected_json
    
def test_extract_json_with_nested_json_objects():
    """Checks handling of nested JSON objects."""
    text = '{"key1": {"key2": "value2"}}'
    expected_json = {"key1": {"key2": "value2"}}
    assert utils.extract_json(text) == expected_json

def test_extract_json_with_array():
     """Checks handling of arrays in JSON."""
     text = '[1,2,3]'
     expected_json = [1,2,3]
     assert utils.extract_json(text) == expected_json

def test_extract_json_with_mixed_braces():
    """Checks handling of JSON with mixed braces."""
    text = '  [{"key": "value"}]  '
    expected_json = [{"key": "value"}]
    assert utils.extract_json(text) == expected_json


# Tests for extract_code_block
def test_extract_code_block_valid():
    """Checks extraction of code block from a string."""
    text = 'some text ```code block``` more text'
    expected_code = '```code block```'
    assert utils.extract_code_block(text) == expected_code

def test_extract_code_block_no_code():
    """Checks handling of string with no code block."""
    text = 'some text with no code block'
    assert utils.extract_code_block(text) == ""

def test_extract_code_block_empty_string():
     """Checks handling of empty string."""
     text = ''
     assert utils.extract_code_block(text) == ""

def test_extract_code_block_multiple_blocks():
    """Checks extraction of code blocks with multiple blocks."""
    text = 'text ```code1``` more text ```code2```'
    expected_code = '```code2```'
    assert utils.extract_code_block(text) == expected_code

def test_extract_code_block_code_at_start():
    """Checks when the code block is at the start of the string."""
    text = '```code block``` more text'
    expected_code = '```code block```'
    assert utils.extract_code_block(text) == expected_code

def test_extract_code_block_code_at_end():
    """Checks when the code block is at the end of the string."""
    text = 'some text ```code block```'
    expected_code = '```code block```'
    assert utils.extract_code_block(text) == expected_code

def test_extract_code_block_with_no_closing_backticks():
    """Checks when the string has no closing backticks."""
    text = 'some text ```code block'
    assert utils.extract_code_block(text) == ""

# Tests for repeat_on_error
def test_repeat_on_error_no_exception():
    """Checks that the function works as expected when no exceptions are raised."""
    @utils.repeat_on_error(retries=3, exceptions=[ValueError])
    def test_func():
        return "Success"
    
    assert test_func() == "Success"

def test_repeat_on_error_with_exception_and_retry():
    """Checks that the function works correctly if exceptions are raised and a retry is performed."""
    
    call_count = 0
    @utils.repeat_on_error(retries=3, exceptions=[ValueError])
    def test_func():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
          raise ValueError("Test Error")
        return "Success"
    
    assert test_func() == "Success"
    assert call_count == 3
    
def test_repeat_on_error_with_exception_and_no_retry():
    """Checks that the function correctly raises exceptions if the number of retries is exceeded."""
    
    call_count = 0
    @utils.repeat_on_error(retries=2, exceptions=[ValueError])
    def test_func():
        nonlocal call_count
        call_count += 1
        raise ValueError("Test Error")
        
    with raises(ValueError, match="Test Error"):
        test_func()

    assert call_count == 2
        
def test_repeat_on_error_with_different_exception():
    """Checks that the function does not retry if the wrong type of exception is raised."""
    call_count = 0
    @utils.repeat_on_error(retries=2, exceptions=[ValueError])
    def test_func():
        nonlocal call_count
        call_count += 1
        raise TypeError("Test Error")
    
    with pytest.raises(TypeError, match="Test Error"):
        test_func()
    
    assert call_count == 1

# Tests for check_valid_fields
def test_check_valid_fields_valid():
    """Checks that the function does not raise an exception with valid fields."""
    obj = {"key1": "value1", "key2": "value2"}
    valid_fields = ["key1", "key2"]
    utils.check_valid_fields(obj, valid_fields)

def test_check_valid_fields_invalid():
    """Checks that the function raises an exception with invalid fields."""
    obj = {"key1": "value1", "key3": "value3"}
    valid_fields = ["key1", "key2"]
    with pytest.raises(ValueError, match="Invalid key key3 in dictionary. Valid keys are: \['key1', 'key2'\]"):
        utils.check_valid_fields(obj, valid_fields)

def test_check_valid_fields_empty_dict():
    """Checks that the function works with an empty dict."""
    obj = {}
    valid_fields = ["key1", "key2"]
    utils.check_valid_fields(obj, valid_fields)

def test_check_valid_fields_empty_valid_fields():
    """Checks when the valid fields are empty."""
    obj = {"key1": "value1"}
    valid_fields = []
    with pytest.raises(ValueError, match="Invalid key key1 in dictionary. Valid keys are: \[\]"):
      utils.check_valid_fields(obj, valid_fields)

# Tests for sanitize_raw_string
def test_sanitize_raw_string_valid():
    """Checks that the function works as expected when sanitizing a valid string."""
    value = "valid string"
    assert utils.sanitize_raw_string(value) == value

def test_sanitize_raw_string_with_invalid_chars():
    """Checks that the function correctly removes invalid characters."""
    value = "invalid\x00string"
    assert utils.sanitize_raw_string(value) == "invalidstring"

def test_sanitize_raw_string_long_string():
    """Checks that the function correctly truncates very long strings."""
    long_string = "a" * (sys.maxsize + 10)
    assert len(utils.sanitize_raw_string(long_string)) == sys.maxsize

def test_sanitize_raw_string_empty_string():
    """Checks that the function works with empty strings."""
    value = ""
    assert utils.sanitize_raw_string(value) == ""

# Tests for sanitize_dict
def test_sanitize_dict_valid():
    """Checks that the function works as expected when sanitizing a valid dict."""
    value = {"key1": "value1", "key2": "value2"}
    assert utils.sanitize_dict(value) == value

def test_sanitize_dict_with_invalid_chars():
    """Checks that the function correctly sanitizes dicts with invalid characters in values."""
    value = {"key1": "value\x001"}
    assert utils.sanitize_dict(value) == {"key1": "value1"}

def test_sanitize_dict_with_nested_dict():
    """Checks that the function correctly sanitizes nested dicts."""
    value = {"key1": {"key2": "value\x002"}}
    assert utils.sanitize_dict(value) == {"key1": {"key2": "value2"}}

def test_sanitize_dict_with_long_string_value():
    """Checks that the function correctly sanitizes dicts with long string values."""
    long_string = "a" * (sys.maxsize + 10)
    value = {"key1": long_string}
    sanitized = utils.sanitize_dict(value)
    assert len(sanitized["key1"]) == sys.maxsize

def test_sanitize_dict_empty_dict():
    """Checks that the function works with empty dicts."""
    value = {}
    assert utils.sanitize_dict(value) == {}

# Tests for add_rai_template_variables_if_enabled
@patch("tinytroupe.utils.config")
def test_add_rai_template_variables_if_enabled_rai_enabled(mock_config, tmp_path):
    """Checks that the function correctly sets RAI variables if enabled."""
    mock_config.__getitem__.return_value.getboolean.side_effect = [True, True]
    
    harmful_content_path = tmp_path / "rai_harmful_content_prevention.md"
    copyright_path = tmp_path / "rai_copyright_infringement_prevention.md"
    
    with open(harmful_content_path, "w") as f:
        f.write("Harmful content disclaimer")
    with open(copyright_path, "w") as f:
        f.write("Copyright disclaimer")
        
    with patch("tinytroupe.utils.os.path.join", side_effect=lambda *args: str(tmp_path / args[-1])):
        template_variables = {}
        result = utils.add_rai_template_variables_if_enabled(template_variables)
        assert result["rai_harmful_content_prevention"] == "Harmful content disclaimer"
        assert result["rai_copyright_infringement_prevention"] == "Copyright disclaimer"

@patch("tinytroupe.utils.config")
def test_add_rai_template_variables_if_enabled_rai_disabled(mock_config, tmp_path):
    """Checks that the function correctly sets RAI variables to None if disabled."""
    mock_config.__getitem__.return_value.getboolean.side_effect = [False, False]
    
    harmful_content_path = tmp_path / "rai_harmful_content_prevention.md"
    copyright_path = tmp_path / "rai_copyright_infringement_prevention.md"
    
    with open(harmful_content_path, "w") as f:
        f.write("Harmful content disclaimer")
    with open(copyright_path, "w") as f:
        f.write("Copyright disclaimer")
        
    with patch("tinytroupe.utils.os.path.join", side_effect=lambda *args: str(tmp_path / args[-1])):
        template_variables = {}
        result = utils.add_rai_template_variables_if_enabled(template_variables)
        assert result["rai_harmful_content_prevention"] is None
        assert result["rai_copyright_infringement_prevention"] is None
        
@patch("tinytroupe.utils.config")
def test_add_rai_template_variables_if_enabled_partial_disable(mock_config, tmp_path):
    """Checks that the function correctly sets RAI variables if partially disabled."""
    mock_config.__getitem__.return_value.getboolean.side_effect = [True, False]

    harmful_content_path = tmp_path / "rai_harmful_content_prevention.md"
    copyright_path = tmp_path / "rai_copyright_infringement_prevention.md"
    
    with open(harmful_content_path, "w") as f:
        f.write("Harmful content disclaimer")
    with open(copyright_path, "w") as f:
        f.write("Copyright disclaimer")

    with patch("tinytroupe.utils.os.path.join", side_effect=lambda *args: str(tmp_path / args[-1])):
        template_variables = {}
        result = utils.add_rai_template_variables_if_enabled(template_variables)
        assert result["rai_harmful_content_prevention"] == "Harmful content disclaimer"
        assert result["rai_copyright_infringement_prevention"] is None

# Tests for inject_html_css_style_prefix
def test_inject_html_css_style_prefix_valid():
    """Checks that the function correctly injects the style prefix."""
    html = '<div style="color: red;">Hello</div>'
    style_prefix = "font-size: 20px;"
    expected_html = '<div style="font-size: 20px;;color: red;">Hello</div>'
    assert utils.inject_html_css_style_prefix(html, style_prefix) == expected_html

def test_inject_html_css_style_prefix_empty_style():
    """Checks that the function works correctly with empty style attribute."""
    html = '<div style="">Hello</div>'
    style_prefix = "font-size: 20px;"
    expected_html = '<div style="font-size: 20px;;">Hello</div>'
    assert utils.inject_html_css_style_prefix(html, style_prefix) == expected_html

def test_inject_html_css_style_prefix_no_style():
    """Checks that the function does not change the string when no style is present."""
    html = '<div>Hello</div>'
    style_prefix = "font-size: 20px;"
    assert utils.inject_html_css_style_prefix(html, style_prefix) == html

def test_inject_html_css_style_prefix_multiple_style():
    """Checks that the function injects the style prefix to multiple style attributes."""
    html = '<div style="color: red;"><span style="font-weight: bold;">Hello</span></div>'
    style_prefix = "font-size: 20px;"
    expected_html = '<div style="font-size: 20px;;color: red;"><span style="font-size: 20px;;font-weight: bold;">Hello</span></div>'
    assert utils.inject_html_css_style_prefix(html, style_prefix) == expected_html

def test_inject_html_css_style_prefix_empty_prefix():
    """Checks that the function does not inject anything with an empty prefix."""
    html = '<div style="color: red;">Hello</div>'
    style_prefix = ""
    assert utils.inject_html_css_style_prefix(html, style_prefix) == html

# Tests for break_text_at_length
def test_break_text_at_length_valid():
    """Checks that the function correctly breaks text at the specified length."""
    text = "This is a test string"
    max_length = 10
    expected_text = "This is a  (...)"
    assert utils.break_text_at_length(text, max_length) == expected_text

def test_break_text_at_length_no_break():
    """Checks that the function does not break the text when max length is not specified."""
    text = "This is a test string"
    assert utils.break_text_at_length(text) == text

def test_break_text_at_length_shorter_than_max():
    """Checks that the function does not break the text when the string is shorter than max."""
    text = "short"
    max_length = 10
    assert utils.break_text_at_length(text, max_length) == text
    
def test_break_text_at_length_with_dict():
    """Checks that the function works with dict objects, turning them into strings and truncating them if needed."""
    data = {"key1": "value1", "key2": "value2"}
    max_length = 20
    expected_text = '{\n    "key1": "valu (...)'
    assert utils.break_text_at_length(data, max_length) == expected_text
    
def test_break_text_at_length_with_dict_no_truncation():
    """Checks that the function works with dict objects, and does not truncate them if they are shorter than the max length."""
    data = {"key1": "value1", "key2": "value2"}
    max_length = 100
    expected_text = '{\n    "key1": "value1",\n    "key2": "value2"\n}'
    assert utils.break_text_at_length(data, max_length) == expected_text

def test_break_text_at_length_empty_string():
    """Checks handling of an empty string."""
    text = ""
    max_length = 5
    assert utils.break_text_at_length(text, max_length) == ""

# Tests for pretty_datetime
def test_pretty_datetime_valid():
    """Checks that the function correctly formats datetime objects."""
    dt = datetime(2023, 1, 1, 12, 30)
    expected_str = "2023-01-01 12:30"
    assert utils.pretty_datetime(dt) == expected_str

# Tests for dedent
def test_dedent_valid():
    """Checks that the function correctly dedents a string."""
    text = """
        This is a
        multiline
        string.
    """
    expected_text = "This is a\nmultiline\nstring."
    assert utils.dedent(text) == expected_text

def test_dedent_no_indent():
    """Checks that the function works correctly when no indents are present."""
    text = "No indent here."
    assert utils.dedent(text) == text

def test_dedent_empty_string():
    """Checks handling of an empty string."""
    text = ""
    assert utils.dedent(text) == ""

def test_dedent_with_leading_whitespace():
    """Checks that the function removes leading whitespace."""
    text = "  Leading space"
    assert utils.dedent(text) == "Leading space"

def test_dedent_with_only_whitespace():
    """Checks that the function correctly handles a string with only spaces."""
    text = "   "
    assert utils.dedent(text) == ""

# Tests for read_config_file
@patch("tinytroupe.utils.configparser.ConfigParser")
def test_read_config_file_use_cache_valid(mock_configparser):
    """Checks that the function uses the cached config if available and valid."""
    global _config
    _config = mock_configparser()

    assert utils.read_config_file() == _config
    
def test_read_config_file_default_valid(monkeypatch, tmp_path):
    """Checks that the function correctly reads the config from the default location."""
    config_file_path = tmp_path / "config.ini"
    with open(config_file_path, 'w') as f:
        f.write("[test]\nkey=value")
        
    monkeypatch.setattr(utils.Path, "cwd", lambda *args: tmp_path)
    monkeypatch.setattr(utils.Path, "parent", lambda *args: tmp_path)
    monkeypatch.setattr(utils.Path, "absolute", lambda *args: tmp_path)
    
    config = utils.read_config_file(use_cache=False)
    assert config.get("test","key") == "value"
    
def test_read_config_file_custom_valid(monkeypatch, tmp_path):
    """Checks that the function correctly reads a custom config file when present."""
    default_config_file_path = tmp_path / "config.ini"
    custom_config_file_path = tmp_path / "config.ini" # same path for simplicity

    with open(default_config_file_path, 'w') as f:
        f.write("[DEFAULT]\nkey=default_value")
    with open(custom_config_file_path, 'w') as f:
        f.write("[test]\nkey=custom_value")
    
    monkeypatch.setattr(utils.Path, "cwd", lambda *args: tmp_path)
    monkeypatch.setattr(utils.Path, "parent", lambda *args: tmp_path)
    monkeypatch.setattr(utils.Path, "absolute", lambda *args: tmp_path)

    config = utils.read_config_file(use_cache=False)
    assert config.get("test","key") == "custom_value"
    assert config.get("DEFAULT","key") == "default_value"

def test_read_config_file_default_not_found(monkeypatch, tmp_path):
    """Checks that the function raises exception if no default config is found."""
    
    monkeypatch.setattr(utils.Path, "cwd", lambda *args: tmp_path)
    monkeypatch.setattr(utils.Path, "parent", lambda *args: tmp_path)
    monkeypatch.setattr(utils.Path, "absolute", lambda *args: tmp_path)
    
    with pytest.raises(ValueError, match=f"Failed to find default config on: {tmp_path / 'config.ini'}"):
        utils.read_config_file(use_cache=False)


def test_read_config_file_no_custom(monkeypatch, tmp_path):
    """Checks that the function uses default values when no custom config is present."""
    config_file_path = tmp_path / "config.ini"
    with open(config_file_path, 'w') as f:
        f.write("[DEFAULT]\nkey=default_value")

    monkeypatch.setattr(utils.Path, "cwd", lambda *args: tmp_path)
    monkeypatch.setattr(utils.Path, "parent", lambda *args: tmp_path)
    monkeypatch.setattr(utils.Path, "absolute", lambda *args: tmp_path)
    
    config = utils.read_config_file(use_cache=False)
    assert config.get("DEFAULT","key") == "default_value"
    

# Tests for pretty_print_config
def test_pretty_print_config(capsys):
    """Checks that the function correctly prints the config."""
    config = configparser.ConfigParser()
    config.add_section("Section1")
    config.set("Section1", "key1", "value1")
    config.add_section("Section2")
    config.set("Section2", "key2", "value2")
    utils.pretty_print_config(config)
    captured = capsys.readouterr()
    
    assert "Current TinyTroupe configuration" in captured.out
    assert "[Section1]" in captured.out
    assert "key1 = value1" in captured.out
    assert "[Section2]" in captured.out
    assert "key2 = value2" in captured.out

# Tests for start_logger
@patch("tinytroupe.utils.logging.getLogger")
def test_start_logger_valid(mock_get_logger):
    """Checks that the function correctly configures the logger."""
    mock_logger = mock_get_logger.return_value
    mock_config = configparser.ConfigParser()
    mock_config.add_section("Logging")
    mock_config.set("Logging", "LOGLEVEL", "DEBUG")
    utils.start_logger(mock_config)
    mock_logger.setLevel.assert_called_with("DEBUG")
    mock_logger.addHandler.assert_called()
    
@patch("tinytroupe.utils.logging.getLogger")
def test_start_logger_default_level(mock_get_logger):
    """Checks that the function uses default log level if none is specified in the config."""
    mock_logger = mock_get_logger.return_value
    mock_config = configparser.ConfigParser()
    mock_config.add_section("Logging")
    utils.start_logger(mock_config)
    mock_logger.setLevel.assert_called_with("INFO")
    mock_logger.addHandler.assert_called()

# Tests for JsonSerializableRegistry
def test_json_serializable_registry_to_json_valid():
    """Checks that the function correctly serializes objects to JSON."""
    @utils.post_init
    class TestClass(utils.JsonSerializableRegistry):
        serializable_attributes = ["attr1", "attr2"]
        def __init__(self, attr1, attr2):
            self.attr1 = attr1
            self.attr2 = attr2
            self._post_init()
            
        def _post_init(self):
            self.attr3 = "value3" # this attribute is not serialized
    
    test_obj = TestClass(attr1="value1", attr2=2)
    expected_json = {"json_serializable_class_name": "TestClass", "attr1": "value1", "attr2": 2}
    assert test_obj.to_json() == expected_json

def test_json_serializable_registry_to_json_with_include():
    """Checks that the function correctly serializes objects to JSON, including attributes specified in the parameter."""
    @utils.post_init
    class TestClass(utils.JsonSerializableRegistry):
        serializable_attributes = ["attr1"]
        def __init__(self, attr1, attr2):
            self.attr1 = attr1
            self.attr2 = attr2
            self._post_init()
            
        def _post_init(self):
            self.attr3 = "value3" # this attribute is not serialized
            
    test_obj = TestClass(attr1="value1", attr2=2)
    expected_json = {"json_serializable_class_name": "TestClass", "attr1": "value1", "attr2": 2}
    assert test_obj.to_json(include=["attr1", "attr2"]) == expected_json
    
def test_json_serializable_registry_to_json_with_suppress():
    """Checks that the function correctly serializes objects to JSON, suppressing attributes specified in the parameter."""
    @utils.post_init
    class TestClass(utils.JsonSerializableRegistry):
        serializable_attributes = ["attr1", "attr2"]
        def __init__(self, attr1, attr2):
            self.attr1 = attr1
            self.attr2 = attr2
            self._post_init()
            
        def _post_init(self):
            self.attr3 = "value3" # this attribute is not serialized
    
    test_obj = TestClass(attr1="value1", attr2=2)
    expected_json = {"json_serializable_class_name": "TestClass", "attr1": "value1"}
    assert test_obj.to_json(suppress=["attr2"]) == expected_json
    
def test_json_serializable_registry_to_json_nested_objects():
    """Checks that the function correctly serializes nested objects."""
    @utils.post_init
    class InnerClass(utils.JsonSerializableRegistry):
        serializable_attributes = ["inner_attr"]
        def __init__(self, inner_attr):
            self.inner_attr = inner_attr
            self._post_init()
            
    @utils.post_init
    class OuterClass(utils.JsonSerializableRegistry):
        serializable_attributes = ["outer_attr", "inner"]
        def __init__(self, outer_attr, inner):
            self.outer_attr = outer_attr
            self.inner = inner
            self._post_init()

    inner_obj = InnerClass(inner_attr="inner_value")
    outer_obj = OuterClass(outer_attr="outer_value", inner=inner_obj)
    expected_json = {
        "json_serializable_class_name": "OuterClass",
        "outer_attr": "outer_value",
        "inner": {
            "json_serializable_class_name": "InnerClass",
            "inner_attr": "inner_value"
        }
    }
    assert outer_obj.to_json() == expected_json

def test_json_serializable_registry_to_json_with_list():
    """Checks that the function correctly serializes a list of objects."""
    @utils.post_init
    class TestClass(utils.JsonSerializableRegistry