## Usage Guide for `src.scenario` Module

This guide details how to use the `src.scenario` module to automate interactions with suppliers, extract product data from their websites, and synchronize it with your system's database (e.g., PrestaShop).

### Prerequisites

- Python 3.x
- Libraries: `requests`, `BeautifulSoup4`, `PrestaShop` (assuming you have a PrestaShop integration library)
- A working internet connection
- Valid supplier credentials, if required
- JSON scenario files in the correct format (see Example Scenario below)

### Running Scenarios

The core functionality resides in the `Supplier` class.  You need to instantiate this class with the relevant supplier information. The `run()` method is the entry point for scenario execution.


**1. Instantiate the `Supplier` Class:**

```python
from your_module import Supplier  # Replace your_module with the actual module name

s = Supplier('aliexpress')  # Replace 'aliexpress' with the supplier type
```

**2. Running Scenarios from Files:**

To execute scenarios from a JSON file, provide the file path (or list of file paths) to the `run()` method:

```python
s.run('path/to/scenario_file.json')  # For a single file
s.run(['path/to/scenario1.json', 'path/to/scenario2.json'])  # For multiple files
```

**3. Running Scenarios from a List of Dictionaries:**

You can directly provide a list of scenario dictionaries to the `run()` method. This is useful when scenarios are not stored in individual files.

```python
scenarios = [
    {'url': 'https://example.com/category1', 'presta_categories': {'default_category': 123}},
    {'url': 'https://example.com/category2', 'presta_categories': {'default_category': 456}}
]
s.run(scenarios)
```


**4. Running Scenarios from a Single Dictionary (Single Scenario):**

```python
scenario = {'url': 'https://example.com/category1', 'presta_categories': {'default_category': 123}}
s.run(scenario)
```


### Example Scenario (JSON Format)

```json
{
  "scenarios": {
    "electronics": {
      "url": "https://example.com/electronics",
      "name": "electronics",
      "presta_categories": {
        "default_category": 101,
        "additional_categories": [102, 103]
      },
      "condition": "new"
    }
  }
}
```

**Explanation of Fields:**

* `"url"`: The URL of the product category page on the supplier's website.
* `"name"`: A descriptive name for the scenario (used for logging).
* `"presta_categories"`:
    * `"default_category"`: The primary PrestaShop category ID for the products.
    * `"additional_categories"`: A list of additional PrestaShop category IDs for the products.
* `"condition"` (optional): Filters product results based on specific criteria (e.g., "new," "used").


### Error Handling and Logging

The module includes logging mechanisms to track the success or failure of each scenario execution and to provide insights into potential errors during data extraction or insertion.  Check the logs for error messages and specific reasons for any failures.  The `journal` is automatically updated.


### Important Considerations

- **Error Handling:**  Ensure robust error handling within the `Supplier` class to gracefully deal with network issues, invalid JSON formats, or problems connecting to the database.
- **Rate Limiting:** Be mindful of the supplier's website's rate limits and implement appropriate delays to avoid being blocked.
- **Data Validation:**  Validate the extracted data before inserting it into the database to prevent inconsistencies.


This guide provides a basic framework.  Adjust the code and adapt the `Supplier` class to fit your specific needs and integration with your database system and supplier. Remember to replace placeholders like `your_module` and `aliexpress` with the actual module and supplier type.