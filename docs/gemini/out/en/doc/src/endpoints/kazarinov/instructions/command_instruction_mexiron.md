# command_instruction_mexiron

## Overview

This module provides instructions for analyzing computer components from JSON input, classifying build types (e.g., gaming, workstation), and generating structured JSON output in Hebrew and Russian.  The output includes titles, descriptions, translated component details, and confidence scores.  Detailed guidelines for descriptions and component handling are crucial for accurate and comprehensive results.


## Functions

### `analyze_computer_components`

**Description**: This function analyzes computer component data from JSON input, classifying build type, and generating structured JSON output in Hebrew and Russian.

**Parameters**:

- `input_json` (str): The JSON string containing computer component data.


**Returns**:

- `dict`: A dictionary containing the structured JSON output in Hebrew and Russian.  The structure follows the provided template, including titles, descriptions, build type confidence scores, and component details.

**Raises**:

- `ValueError`: Raised if the input JSON is invalid or malformed.
- `TypeError`: Raised if the input data does not match the expected structure.


```
```python
def analyze_computer_components(input_json: str) -> dict | None:
    """
    Args:
        input_json (str): The JSON string containing computer component data.

    Returns:
        dict | None: A dictionary containing the structured JSON output in Hebrew and Russian, following the provided template. Returns None if the input is invalid.

    Raises:
        ValueError: Raised if the input JSON is invalid or malformed.
        TypeError: Raised if the input data does not match the expected structure.
    """
    try:
        # Parse the input JSON.  Error handling is crucial.
        data = json.loads(input_json)
    except json.JSONDecodeError as ex:
        raise ValueError(f"Invalid JSON input: {ex}") from ex
    except TypeError as ex:
        raise TypeError(f"Invalid input data type: {ex}") from ex

    # ... (Implementation for analyzing components, classifying, translating, and generating output)
    #  This would be the core logic of your analysis.
    # ...
    return output_json

```


##  Example Usage (IlluStartive)

```python
import json

input_data = """
# Example JSON Input
{
  "components": [
    {"name": "CPU", "model": "Intel i7-14700F"},
    {"name": "GPU", "model": "Nvidia RTX 4070"}
  ]
}
"""
try:
    result = analyze_computer_components(input_data)
    if result:
        print(json.dumps(result, indent=2, ensure_ascii=False))
except (ValueError, TypeError) as ex:
    print(f"Error: {ex}")

```


```
```