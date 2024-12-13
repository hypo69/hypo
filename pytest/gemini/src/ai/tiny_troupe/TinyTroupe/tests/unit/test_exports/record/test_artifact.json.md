```python
import pytest
import json

# Since the provided code is a JSON string, we'll test that it can be parsed
# and that it contains the expected data structure and keys. 

def test_json_parsing():
    """Tests that the JSON string can be parsed successfully and is the expected structure."""
    json_string = """
    {
        "name": "John Doe",
        "age": 30,
        "occupation": "Engineer",
        "content": "This is a sample JSON data."
    }
    """
    try:
        data = json.loads(json_string)
        assert isinstance(data, dict), "The parsed JSON should be a dictionary."
        assert "name" in data, "The dictionary should have a 'name' key."
        assert "age" in data, "The dictionary should have an 'age' key."
        assert "occupation" in data, "The dictionary should have an 'occupation' key."
        assert "content" in data, "The dictionary should have a 'content' key."
        
        # Check the value types
        assert isinstance(data["name"], str), "The 'name' should be a string."
        assert isinstance(data["age"], int), "The 'age' should be an integer."
        assert isinstance(data["occupation"], str), "The 'occupation' should be a string."
        assert isinstance(data["content"], str), "The 'content' should be a string."

        # Check the actual values to verify integrity
        assert data["name"] == "John Doe", "The 'name' value is incorrect."
        assert data["age"] == 30, "The 'age' value is incorrect."
        assert data["occupation"] == "Engineer", "The 'occupation' value is incorrect."
        assert data["content"] == "This is a sample JSON data.", "The 'content' value is incorrect."


    except json.JSONDecodeError as e:
        pytest.fail(f"JSON decoding failed: {e}")


def test_json_parsing_invalid_json():
    """Tests that an exception is raised when parsing an invalid JSON string."""
    invalid_json_string = """
    {
        "name": "John Doe",
        "age": 30,
        "occupation": "Engineer",
         "content": "This is a sample JSON data.",
    """  # Missing closing brace
    with pytest.raises(json.JSONDecodeError):
        json.loads(invalid_json_string)
    
def test_json_parsing_empty_string():
    """Tests that an exception is raised when parsing an empty JSON string."""
    empty_json_string = ""
    with pytest.raises(json.JSONDecodeError):
        json.loads(empty_json_string)

def test_json_parsing_invalid_data_types():
    """Tests that an exception is raised when the JSON data types are invalid."""
    
    # Testing with invalid data types will not raise a JSONDecodeError during parsing.
    # They will be parsed successfully.
    # Here we test that if for instance, the age is provided as a string we get type error.
    json_string_invalid_types = """
    {
        "name": "John Doe",
        "age": "30",
        "occupation": "Engineer",
        "content": "This is a sample JSON data."
    }
    """
    data = json.loads(json_string_invalid_types)
    assert isinstance(data, dict), "The parsed JSON should be a dictionary."
    assert "name" in data, "The dictionary should have a 'name' key."
    assert "age" in data, "The dictionary should have an 'age' key."
    assert "occupation" in data, "The dictionary should have an 'occupation' key."
    assert "content" in data, "The dictionary should have a 'content' key."
    
    assert isinstance(data["name"], str), "The 'name' should be a string."
    assert isinstance(data["age"], str), "The 'age' should be a string." # This will fail if the type is checked like in test_json_parsing. 
    assert isinstance(data["occupation"], str), "The 'occupation' should be a string."
    assert isinstance(data["content"], str), "The 'content' should be a string."
```