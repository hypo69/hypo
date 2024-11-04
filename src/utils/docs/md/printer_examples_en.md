
# Examples of `pprint` usage:
### Example 1: print string data
```python
pprint("Hello, World!")
```
### output
```
'Hello, World!'
```

### Example 1: print string data
```python
example_list = [
    "Hello, World!",
    Path("/example/path"),
    42,
    {"key": "value"}
]
pprint(example_list)
```

## Example 3: Printing First 5 Lines from a CSV File
```python
import csv
from pathlib import Path

# Contents of example.csv:
csv_data = """name,age,city
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago
David,28,Houston
Eve,22,Phoenix
"""
with open(Path('example.csv'), 'w', encoding='utf-8') as f:
    f.write(csv_data)

pprint('example.csv', max_lines=5)
```

## Example 4: Printing First 3 Rows from an XLS File
```python
import pandas as pd
from pathlib import Path

# Create a sample DataFrame and save it as an Excel file
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [30, 25, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
df.to_excel('example.xls', index=False)

pprint('example.xls', max_lines=3)
```

## Example 5: Reading from a JSON File
```python
import json
from pathlib import Path

# Contents of example_json.json:
dct = {
    "name": "Bob",
    "age": 25,
    "city": "New York",
    "skills": ["Python", "Data Science"]
}

# Save the dictionary to a JSON file
with open(Path('example_json.json'), 'w', encoding='utf-8') as f:
    json.dump(dct, f, ensure_ascii=False, indent=4)

pprint('example_json.json')
```

## Example 6: Printing 10 Lines from a TXT File
```python
from pathlib import Path

s = """Line 1: This is a line from the file.
Line 2: Here's another line.
Line 3: And one more for good measure.
Line 4: This is the fourth line.
Line 5: Here's the fifth line.
Line 6: Now we are on the sixth line.
Line 7: The seventh line is here.
Line 8: This is the eighth line.
Line 9: Line number nine is next.
Line 10: We've reached the tenth line.
Line 11: This is the eleventh line.
Line 12: Now on the twelfth line.
Line 13: Thirteen lines down.
Line 14: Almost there, this is the fourteenth line.
Line 15: Finally, this is the fifteenth line."""

# Save text file
with open(Path('example_txt.txt'), 'w', encoding='utf-8') as f:
    f.write(s)

# Call pprint with the correct filename
pprint('example_txt.txt')
```

## Example 7: Pretty Printing a Custom Class Instance
```python
class MyClass:
    def __init__(self, var1: str, var2: bool = False):
        self.var1 = var1
        self.var2 = var2

    def method1(self):
        return "method1 called"

obj = MyClass("value1", True)
pprint(obj)
```

## Example 8: Pretty Printing a Nested List
```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pprint(nested_list)
```

## Example 9: Pretty Printing JSON-like Data Structure
```python
example_json = {
    "name": "Bob",
    "age": 25,
    "languages": ["Python", "JavaScript"],
    "details": {"employed": True, "skills": ["Django", "Flask"]}
}
pprint(example_json)
```

## Example 10: Printing a Path Object
```python
pprint(Path("/example/path"))
```

## Example 11: Printing Various Primitive Types
```python
pprint("This is a simple string.")
pprint(123)
pprint(3.14159)
pprint(True)
```
