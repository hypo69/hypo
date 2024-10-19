## Руководство для тестера

### Введение
Это руководство предназначено для тестирования модуля `pprint` из библиотеки `src.utils.printer.py`. Модуль `pprint` используется для форматирования и красивой печати различных структур данных, включая словари, списки, строки и экземпляры классов.

### Установка окружения
Перед началом тестирования необходимо настроить рабочее окружение:

1. **Клонируйте репозиторий**:
   ```sh
   git clone <URL_РЕПОЗИТОРИЯ>
   cd <ИМЯ_РЕПОЗИТОРИЯ>
   ```

2. **Создайте виртуальное окружение**:
   ```sh
   python -m venv venv
   ```

3. **Активируйте виртуальное окружение**:
   - Для Windows:
     ```sh
     venv\Scripts\activate
     ```
   - Для Unix или MacOS:
     ```sh
     source venv/bin/activate
     ```

4. **Установите зависимости**:
   ```sh
   pip install -r requirements.txt
   ```

### Запуск тестов
Для запуска тестов используется `pytest`. Убедитесь, что вы находитесь в корневой директории проекта.

1. **Запустите все тесты**:
   ```sh
   pytest
   ```

2. **Запустите тесты для конкретного модуля**:
   ```sh
   pytest tests/test_printer.py
   ```

### Описание тестов
Ниже приведены описания тестов, которые покрывают функциональность модуля `pprint`.

#### `test_pprint_dict`
Этот тест проверяет корректность вывода функции `pprint` при передаче словаря, содержащего объекты `Path`.

#### `test_pprint_list`
Этот тест проверяет корректность вывода функции `pprint` при передаче списка, содержащего объекты `Path`.

#### `test_pprint_str`
Этот тест проверяет корректность вывода функции `pprint` при передаче строки.

#### `test_pprint_class_instance`
Этот тест проверяет корректность вывода функции `pprint` при передаче экземпляра класса `A`.

#### `test_pprint_empty`
Этот тест проверяет поведение функции `pprint`, когда данные не передаются.

#### `test_pprint_exception`
Этот тест проверяет логгирование ошибок в случае возникновения исключений при печати.

### Логирование
Функция `pprint` использует модуль `logger` для логгирования ошибок. Убедитесь, что при возникновении ошибок соответствующие сообщения логируются.

### Дополнительная информация
Если при тестировании обнаруживаются баги или несоответствия, пожалуйста, создайте новый `issue` в репозитории с детальным описанием проблемы и шагами для ее воспроизведения.

Here's a set of `pytest` tests for the `pprint` function based on the examples provided. These tests cover various data types such as strings, lists, dictionaries, objects, and file reading. I'll assume that the function `pprint` is defined in a file called `printer.py` in your project structure.

### Test file: `test_printer.py`

```python
import pytest
from pathlib import Path
from printer import pprint
import json
import os

class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def display(self):
        return f"{self.name} has value {self.value}"

@pytest.fixture
def tmp_text_file(tmpdir):
    """Creates a temporary text file for testing."""
    file = tmpdir.join("example_list.txt")
    file.write("Line 1: This is a line from the file.\nLine 2: Here's another line.\nLine 3: And one more for good measure.")
    return file

@pytest.fixture
def tmp_json_file(tmpdir):
    """Creates a temporary JSON file for testing."""
    file = tmpdir.join("example.json")
    json_data = {
        "name": "Bob",
        "age": 25,
        "city": "New York",
        "skills": ["Python", "Data Science"]
    }
    file.write(json.dumps(json_data, indent=4))
    return file

def test_pprint_string(capsys):
    """Test pprint with a simple string."""
    pprint("Hello, World!")
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"

def test_pprint_list(capsys):
    """Test pprint with a list."""
    example_list = ["Hello, World!", Path("C:/example/path"), 42, {"key": "value"}]
    pprint(example_list)
    captured = capsys.readouterr()
    expected_output = (
        '[\n'
        '    "Hello, World!",\n'
        '    "C:/example/path",\n'
        '    42,\n'
        '    {\n'
        '        "key": "value"\n'
        '    }\n'
        ']\n'
    )
    assert captured.out == expected_output

def test_pprint_dict(capsys):
    """Test pprint with a dictionary."""
    example_dict = {
        "name": "Alice",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "Wonderland"
        },
        "files": [Path("C:/file1.txt"), Path("C:/file2.txt")]
    }
    pprint(example_dict)
    captured = capsys.readouterr()
    expected_output = (
        '{\n'
        '    "name": "Alice",\n'
        '    "age": 30,\n'
        '    "address": {\n'
        '        "street": "123 Main St",\n'
        '        "city": "Wonderland"\n'
        '    },\n'
        '    "files": [\n'
        '        "C:/file1.txt",\n'
        '        "C:/file2.txt"\n'
        '    ]\n'
        '}\n'
    )
    assert captured.out == expected_output

def test_pprint_object(capsys):
    """Test pprint with a custom object."""
    obj = MyClass(name="TestObject", value=100)
    pprint(obj)
    captured = capsys.readouterr()
    expected_output = (
        "Class: MyClass\n"
        "Bases: ('object',)\n"
        "Methods:\n"
        "display()\n"
        "Properties:\n"
        "name = TestObject\n"
        "value = 100\n"
    )
    assert captured.out == expected_output

def test_pprint_json_file(capsys, tmp_json_file):
    """Test pprint by reading from a JSON file."""
    pprint(str(tmp_json_file))
    captured = capsys.readouterr()
    expected_output = (
        '{\n'
        '    "name": "Bob",\n'
        '    "age": 25,\n'
        '    "city": "New York",\n'
        '    "skills": [\n'
        '        "Python",\n'
        '        "Data Science"\n'
        '    ]\n'
        '}\n'
    )
    assert captured.out == expected_output

def test_pprint_txt_file(capsys, tmp_text_file):
    """Test pprint by reading from a TXT file."""
    pprint(str(tmp_text_file))
    captured = capsys.readouterr()
    expected_output = (
        "Line 1: This is a line from the file.\n"
        "Line 2: Here's another line.\n"
        "Line 3: And one more for good measure.\n"
    )
    assert captured.out == expected_output

def test_pprint_nonexistent_file(capsys):
    """Test pprint with a non-existent file path."""
    with pytest.raises(FileNotFoundError):
        pprint("nonexistent_file.txt")

```

### Explanation of Tests:

1. **`test_pprint_string`**: Tests the `pprint` function with a simple string.
2. **`test_pprint_list`**: Tests the function with a list containing various types, including `Path` objects and dictionaries.
3. **`test_pprint_dict`**: Tests the function with a dictionary, including nested dictionaries and `Path` objects.
4. **`test_pprint_object`**: Tests the function with a custom object of class `MyClass`.
5. **`test_pprint_json_file`**: Tests the function by reading a temporary JSON file and asserting the output.
6. **`test_pprint_txt_file`**: Tests the function by reading a temporary text file and checking the printed content.
7. **`test_pprint_nonexistent_file`**: Tests the function when given a non-existent file, which should raise a `FileNotFoundError`.

### Fixtures:

- **`tmp_text_file`**: Creates a temporary text file for testing file reading.
- **`tmp_json_file`**: Creates a temporary JSON file for testing file reading.

### Running the Tests:

To run these tests, save the above code in a file named `test_printer.py` in the same directory as your `pprint` function. Then, run the following command from your terminal:

```bash
pytest test_printer.py
```

This will execute the test cases and verify that the `pprint` function behaves as expected across different data types and file input scenarios.

Here’s a `test_printer_guide.md` that explains the setup and usage of the tests for the `pprint` function.

---

# Guide to Testing the `pprint` Function with Pytest

This document provides a step-by-step guide on how to test the `pprint` function using `pytest`. These tests cover various scenarios such as handling lists, dictionaries, custom objects, and reading from files.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Setting Up the Project](#setting-up-the-project)
3. [Understanding the Test Cases](#understanding-the-test-cases)
4. [Running the Tests](#running-the-tests)
5. [Interpreting the Results](#interpreting-the-results)

---

## Prerequisites

To run the tests for the `pprint` function, make sure you have the following installed:

- Python 3.x
- `pytest` testing framework

### Installing Pytest

If `pytest` is not installed, you can install it using pip:

```bash
pip install pytest
```

## Setting Up the Project

Assuming your project structure looks like this:

```
/my_project
    /src
        printer.py       # File containing the pprint function
    /tests
        test_printer.py  # File containing the test cases
```

1. **`printer.py`**: This file contains the `pprint` function that we are testing.
2. **`test_printer.py`**: This file contains the tests written in `pytest` to validate the behavior of the `pprint` function.

## Understanding the Test Cases

The tests are designed to cover multiple scenarios, ensuring that the `pprint` function works correctly with different types of data and files.

### Test Cases Overview

Here’s a summary of the test cases in `test_printer.py`:

1. **`test_pprint_string`**:
   - This test verifies that when a simple string is passed to the `pprint` function, it is printed correctly.

2. **`test_pprint_list`**:
   - This test checks if the function properly prints a list that contains a mix of strings, `Path` objects, integers, and dictionaries. The `Path` objects should be correctly converted to strings before printing.

3. **`test_pprint_dict`**:
   - This test ensures that dictionaries, including nested dictionaries and lists containing `Path` objects, are printed in a human-readable format (e.g., as JSON).

4. **`test_pprint_object`**:
   - This test validates that the function can print information about a custom object, including its class name, base classes, methods, and properties.

5. **`test_pprint_json_file`**:
   - This test verifies the function's ability to read and print the contents of a JSON file.

6. **`test_pprint_txt_file`**:
   - This test checks if the function can read and print the contents of a text file.

7. **`test_pprint_nonexistent_file`**:
   - This test ensures that the function raises an appropriate `FileNotFoundError` when attempting to read a non-existent file.

### Fixtures

- **`tmp_text_file`** and **`tmp_json_file`**:
  - These are pytest fixtures that create temporary files (a text file and a JSON file) for testing. The files are automatically deleted after the test completes.

## Running the Tests

Once the `pprint` function and the tests are set up, you can run the tests using `pytest`.

### Running All Tests

To run all tests in the `test_printer.py` file, execute the following command in the terminal from your project’s root directory:

```bash
pytest tests/test_printer.py
```

### Running a Specific Test

To run a specific test, use the `-k` option followed by the name of the test:

```bash
pytest -k test_pprint_list tests/test_printer.py
```

### Verbose Mode

For more detailed output, you can use the `-v` flag:

```bash
pytest -v tests/test_printer.py
```

## Interpreting the Results

After running the tests, pytest will provide feedback in the terminal. Here’s how to interpret the results:

- **.** (dot): Indicates a passing test.
- **F**: Indicates a failing test.

For example, the output might look like this:

```
============================= test session starts ==============================
collected 7 items

test_printer.py::test_pprint_string PASSED                                     [ 14%]
test_printer.py::test_pprint_list PASSED                                       [ 28%]
test_printer.py::test_pprint_dict PASSED                                       [ 42%]
test_printer.py::test_pprint_object PASSED                                     [ 57%]
test_printer.py::test_pprint_json_file PASSED                                  [ 71%]
test_printer.py::test_pprint_txt_file PASSED                                   [ 85%]
test_printer.py::test_pprint_nonexistent_file PASSED                           [100%]

============================== 7 passed in 0.12s ===============================
```

### Failing Tests

If a test fails, pytest will display detailed information about the failure, including the test that failed, the expected output, and the actual result. For example:

```
============================= test session starts ==============================
collected 7 items

test_printer.py::test_pprint_string FAILED                                     [ 14%]
...

=================================== FAILURES ====================================
_________________________________ test_pprint_string ____________________________

    def test_pprint_string(capsys):
        """Test pprint with a simple string."""
        pprint("Hello, World!")
        captured = capsys.readouterr()
>       assert captured.out == "Hello, World!\n"
E       AssertionError: assert 'Hello, World!\r\n' == 'Hello, World!\n'
E         - Hello, World!\r\n
E         + Hello, World!

test_printer.py:13: AssertionError
```

In this case, the test failed because the output contained a `\r\n` (Windows-style line ending) instead of just `\n`. You can adjust your function or tests to handle such differences if needed.

## Conclusion

By following this guide, you should be able to set up and run tests for the `pprint` function in your project. The `pytest` framework makes it easy to ensure that your function handles different types of data and scenarios correctly. If any tests fail, use the provided error messages to adjust the `pprint` function or the test cases themselves.


### Заключение
Следуя этому руководству, вы сможете эффективно протестировать функциональность модуля `pprint`. Если у вас возникнут вопросы или проблемы, не стесняйтесь обращаться за помощью к разработчикам проекта.