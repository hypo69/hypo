# Improved `pprint()` Function

The improved `pprint` function I frequently use in my development is an upgraded version of the standard `pprint`, tailored to handle more complex scenarios such as reading from files and inspecting objects. I found this particularly useful when I need to work with various objects, print structured data, and quickly read file contents—all within the console in a human-readable format.

Here are some of its key features and enhancements:

### Key Features:
- **String Handling**: Detects if a string is a file path and reads the content if it's a `.txt`, `.csv`, or `.xlsx` file. If the string is not a file path, it simply prints the string.
  
- **Data Structures**: 
  - **Dictionaries**: Pretty-prints dictionaries in a JSON-like format. Path objects within dictionaries are automatically converted to strings for compatibility.
  - **Lists**: Similarly, lists are formatted neatly, with Path objects converted for easier reading.
  
- **Object Introspection**: Provides detailed insights into objects, such as class name, base classes, methods, and properties, making it easier to understand their structure.
  
- **File Support**:
  - **Text Files**: Reads and prints `.txt` files.
  - **CSV Files**: Prints the first few rows of `.csv` files, which is especially useful for quickly inspecting data.
  - **XLS/XLSX Files**: Reads and prints the first few rows of Excel files.
  
- **Error Handling**: When the function encounters an error (e.g., file not found, unsupported file type), it prints an error message instead of raising exceptions, allowing the rest of the program to continue running smoothly.

### How it Works:
- **String Processing**: Checks if the input string is a file path. If yes, it reads the file's content. If not, it prints the string as is.
- **Dictionaries & Lists**: Path objects within these structures are converted to strings before formatting and printing them.
- **Object Introspection**: When handling objects, it prints detailed information about the object's structure, including class name, methods, and properties.
- **File Handling**: Reads and prints text, CSV, and Excel files, previewing the data for a quick glance.
- **Error Management**: Provides detailed error messages and ensures the program continues execution without crashing.

### Example Usages:

#### 1. Printing a String:
```python
pprint("Hello, World!")
```

**Output**:
```
Hello, World!
```

#### 2. Printing a List:
```python
example_list = ["Hello", Path("C:/example/path"), 42, {"key": "value"}]
pprint(example_list)
```

**Output**:
```python
[
    "Hello",
    "C:/example/path",
    42,
    {
        "key": "value"
    }
]
```

#### 3. Printing a Dictionary:
```python
example_dict = {
    "name": "Alice",
    "age": 30,
    "files": [Path("C:/file1.txt"), Path("C:/file2.txt")]
}
pprint(example_dict)
```

**Output**:
```json
{
    "name": "Alice",
    "age": 30,
    "files": [
        "C:/file1.txt",
        "C:/file2.txt"
    ]
}
```

#### 4. Printing Object Information:
```python
class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

obj = MyClass(name="TestObject", value=100)
pprint(obj)
```

**Output**:
```python
Class: MyClass
Bases: ('object',)
Methods:
display()
Properties:
name = TestObject
value = 100
```

#### 5. Reading from a CSV File:
```python
pprint('example.csv', max_lines=2)
```

**Output**:
```
CSV Header: ['name', 'age', 'city']
Row 1: ['Alice', '30', 'Wonderland']
```

### Conclusion:
This enhanced version of `pprint` has been a valuable tool in my development workflow, making it easier to inspect data, read files, and debug complex structures. I'm always open to suggestions for further improving it!