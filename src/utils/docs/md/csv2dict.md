# `csv2json_csv2dict` Module

## `csv2dict()`

The `csv2dict` function converts CSV data to JSON format, returning the data as a list of dictionaries or a list of values, depending on the CSV structure.

### How the function works:

1. **File Reading**: Opens and reads the CSV file.
2. **Data Parsing**: Determines if the CSV has one or multiple columns and parses the data accordingly.
3. **Data Conversion**: Converts the CSV rows into a dictionary format or a list of values.
4. **Error Handling**: Logs errors if CSV reading or data conversion fails.

### Args:
- **csv_file (str | Path)**: Path to the CSV file to read.

### Returns:
- **dict | bool**: A dictionary containing the data from CSV converted to JSON format, or `False` if conversion failed.

### Raises:
- **Exception**: Logs error if unable to read CSV.

### Examples:

```python
>>> csv_file = 'data.csv'
>>> data = csv2dict(csv_file)
>>> print(data)
{'data': [{'name': 'John', 'age': '30', 'city': 'New York'}, {'name': 'Alice', 'age': '25', 'city': 'Los Angeles'}]}
```

## `csv2json()`

The `csv2json` function converts CSV data to JSON format and saves it to a JSON file.

### How the function works:

1. **CSV to Dictionary**: Uses `csv2dict` to convert CSV data into a dictionary format.
2. **JSON Writing**: Writes the converted data to a JSON file.
3. **Error Handling**: Logs errors if CSV reading or JSON writing fails.

### Args:
- **csv_file (str | Path)**: Path to the CSV file to read.
- **json_file (str | Path)**: Path to the JSON file to write.

### Returns:
- **dict**: A dictionary containing the data from CSV converted to JSON format, or an error message if conversion or writing failed.

### Raises:
- **Exception**: Logs error if unable to read CSV or write JSON.

### Examples:

```python
>>> csv_file = 'data.csv'
>>> json_file = 'data.json'
>>> data = csv2json(csv_file, json_file)
>>> print(data)
{'data': [{'name': 'John', 'age': '30', 'city': 'New York'}, {'name': 'Alice', 'age': '25', 'city': 'Los Angeles'}]}
```
