```python
import pytest
import json

# Sample input data (replace with your actual input data)
input_data = [
    {"product_id": "1", "product_title": "Intel i9-14900K", "product_description": "High-end processor", "image_local_saved_path": "path/to/image1"},
    {"product_id": "2", "product_title": "NVIDIA RTX 4060 Ti", "product_description": "Graphics card", "image_local_saved_path": "path/to/image2"},
]


def process_components(components):
    """Processes the component list and returns a structured output."""

    if not isinstance(components, list):
        raise TypeError("Input must be a list of dictionaries.")
    
    output = {"he": {"build_types": {}, "title": "", "description": "", "products": []},
              "ru": {"build_types": {}, "title": "", "description": "", "products": []}}
    
    output["he"]["build_types"]["gaming"] = 0.9
    output["he"]["build_types"]["workstation"] = 0.1
    
    output["ru"]["build_types"]["gaming"] = 0.9
    output["ru"]["build_types"]["workstation"] = 0.1

    output["he"]["title"] = "מחשב גיימינג מתקדם"
    output["he"]["description"] = "מחשב גיימינג בעל ביצועים גבוהים. כולל מעבד מהיר וכרטיס מסך מתקדם."
    output["ru"]["title"] = "Высокопроизводительный игровой компьютер"
    output["ru"]["description"] = "Современный компьютер для требовательных игр. Включает мощный процессор и продвинутую видеокарту."

    for component in components:
        output["he"]["products"].append({
            "product_id": component.get("product_id"),
            "product_title": component.get("product_title"),
            "product_description": component.get("product_description"),
            "image_local_saved_path": component.get("image_local_saved_path"),
            "language": "he"
        })
        output["ru"]["products"].append({
            "product_id": component.get("product_id"),
            "product_title": component.get("product_title"),
            "product_description": component.get("product_description"),
            "image_local_saved_path": component.get("image_local_saved_path"),
            "language": "ru"
        })
    return output




def test_process_components_valid_input():
    """Tests with valid input."""
    result = process_components(input_data)
    assert isinstance(result, dict)
    assert "he" in result
    assert "ru" in result
    assert "products" in result["he"]
    assert "products" in result["ru"]


def test_process_components_empty_input():
    """Tests with empty input list."""
    with pytest.raises(TypeError):
        process_components([])  


def test_process_components_invalid_input_type():
    """Test with invalid input type."""
    with pytest.raises(TypeError):
        process_components("not a list")

def test_process_components_missing_key():
    """Test with missing key."""
    input_data_missing = [{"product_id": "1", "product_title": "Intel i9-14900K", "image_local_saved_path": "path/to/image1"}]
    result = process_components(input_data_missing)
    assert result["he"]["products"][0]["product_description"] == None
    assert result["ru"]["products"][0]["product_description"] == None


# Example usage (replace with your actual function call)
output_data = process_components(input_data)
# print(json.dumps(output_data, indent=2))  # Uncomment to print the output
```