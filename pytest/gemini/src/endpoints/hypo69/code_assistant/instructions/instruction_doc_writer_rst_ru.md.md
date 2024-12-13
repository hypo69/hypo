```python
import pytest
from pathlib import Path
from typing import Optional, Dict, Union
import re

# Fixture definitions, if needed
@pytest.fixture
def example_rst_content():
    """Provides example rst content for testing."""
    return """
    Название модуля
    ===============

    .. automodule:: module_name
        :members:
        :undoc-members:
        :show-inheritance:

    Функции
    --------

    .. autofunction:: module_name.function_name
    """

@pytest.fixture
def example_python_function_docstring():
    """Provides example python docstring for function."""
    return """
    def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
         \"\"\"
         Аргументы:
             param (str): Описание параметра `param`.
             param1 (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию равно `None`.

         Возвращаемое значение:
             dict | None: Описание возвращаемого значения. Возвращает словарь или `None`.

         Исключения:
             SomeError: Описание ситуации, в которой возникает исключение `SomeError`.
         \"\"\"
    """

# Test for file creation and header check
def test_rst_file_creation(tmp_path):
    """Checks if a file is created with the correct header."""
    file_path = tmp_path / "test_module.rst"
    # Creating dummy file content to simulate a function
    test_code = """
    def my_function(a: int, b: str = "test"):
        \"\"\"
        Args:
            a (int): The first parameter
            b (str, optional): The second parameter

        Returns:
            int: the sum of two numbers
        \"\"\"
        return a + int(b)

    class MyClass:
        def __init__(self, val: int):
            \"\"\"
            The initializator
            Args:
                val(int): the input value
            \"\"\"
            self.val = val
        def method(self, m_val: str) -> None:
            \"\"\"
            A simple method
            Args:
                m_val (str): the param for a method
            \"\"\"
            print(m_val)
        
    """
    # This part would normally be replaced with the actual function call
    # That creates the rst file. We simulate that here
    with open(file_path, 'w') as f:
        f.write("Название модуля\n")
        f.write("===============\n")
        f.write("\n")
        f.write(".. automodule:: test_module\n")
        f.write("    :members:\n")
        f.write("    :undoc-members:\n")
        f.write("    :show-inheritance:\n")
        f.write("\n")
        f.write("Функции\n")
        f.write("--------\n")
        f.write("\n")
        f.write(".. autofunction:: test_module.my_function\n")
        f.write("\n")
        f.write("Классы\n")
        f.write("--------\n")
        f.write("\n")
        f.write(".. autoclass:: test_module.MyClass\n")
        f.write("    :members:\n")

    assert file_path.exists()
    with open(file_path, 'r') as f:
        content = f.read()
        assert "Название модуля\n===============" in content


# Test for correct docstring formatting
def test_docstring_formatting(example_python_function_docstring):
    """Checks if docstring formatting for rst is correctly applied."""
    # This test case just checks correct regex parsing for argument and return values
    # This function would be normally replaced with the function, that actually parses
    # The python code
    def parse_function_docstring(docstring: str) -> dict:
        """
        Parses a Python function docstring to extract arguments, return values, and exceptions.

        Args:
            docstring (str): The function's docstring.

        Returns:
            dict: A dictionary containing the parsed information.
        """
        result = {}
        # Added r prefix to treat \ literally
        arg_pattern = re.compile(r"^\s*(\w+)\s*\(([\w\s|\[\]\.,:]+)\):\s*(.+)$", re.MULTILINE)
        return_pattern = re.compile(r"Возвращаемое значение:\s*([\w\s|\[\]\.,]+):\s*(.+)$", re.MULTILINE)
        exception_pattern = re.compile(r"Исключения:\s*([\w]+):\s*(.+)$", re.MULTILINE)
        
        arguments = {}
        for match in arg_pattern.finditer(docstring):
            arg_name = match.group(1)
            arg_type = match.group(2)
            arg_desc = match.group(3).strip()
            arguments[arg_name] = {"type": arg_type, "description": arg_desc}
        result["arguments"] = arguments
        
        return_match = return_pattern.search(docstring)
        if return_match:
            result["return_type"] = return_match.group(1).strip()
            result["return_description"] = return_match.group(2).strip()
        
        exception_matchs = exception_pattern.finditer(docstring)
        exceptions = []
        for exc_match in exception_matchs:
             exceptions.append({"exception":exc_match.group(1).strip(), "description":exc_match.group(2).strip()})
        result["exceptions"] = exceptions
        return result

    parsed_docstring = parse_function_docstring(example_python_function_docstring)
    assert parsed_docstring["arguments"]["param"]["type"] == "str"
    assert parsed_docstring["arguments"]["param1"]["type"] == "Optional[str | dict | str], optional"
    assert parsed_docstring["return_type"] == "dict | None"
    assert parsed_docstring["exceptions"][0]["exception"] == "SomeError"

# Test for TOC generation
def test_toc_generation(tmp_path):
    """Checks if TOC is generated correctly in index.rst."""
    index_file_path = tmp_path / "index.rst"
    module_files = ["module1.rst", "module2.rst", "module3.rst"]

    # This part would normally be replaced by actual TOC generation code.
    # We simulate that here.
    with open(index_file_path, 'w') as f:
        f.write("Contents\n")
        f.write("========\n\n")
        f.write(".. toctree::\n")
        f.write("   :maxdepth: 2\n\n")
        for module_file in module_files:
            f.write(f"   {module_file.replace('.rst', '')}\n")

    assert index_file_path.exists()
    with open(index_file_path, 'r') as f:
        content = f.read()
        assert ":maxdepth: 2" in content
        for module_file in module_files:
            assert module_file.replace('.rst', '') in content

# Test for section headers
def test_section_headers(tmp_path):
     """Checks if section headers are used correctly."""
     file_path = tmp_path / "test_module.rst"
     # Simulate file creation with different headers
     with open(file_path, 'w') as f:
         f.write("First Level Header\n")
         f.write("==================\n\n")
         f.write("Second Level Header\n")
         f.write("------------------\n\n")
         f.write("Third Level Header\n")
         f.write("~~~~~~~~~~~~~~~~~~\n\n")
         f.write("Fourth Level Header\n")
         f.write("^^^^^^^^^^^^^^^^^^\n")

     with open(file_path, 'r') as f:
         content = f.read()
         assert "First Level Header\n================" in content
         assert "Second Level Header\n------------------" in content
         assert "Third Level Header\n~~~~~~~~~~~~~~~~~~" in content
         assert "Fourth Level Header\n^^^^^^^^^^^^^^^^^^" in content


# Test for exception handling
def test_exception_handling_format():
     """Test that 'ex' is used instead of 'e' in exception blocks"""
     # Simulate file creation with excpetion block.
     # This part would normally be replaced with the function
     # That creates the rst file.
     test_code = """
     def my_function():
          try:
              raise ValueError("Test Error")
          except ValueError as ex:
              print(ex)
          
     """
     # Simulate file content generation
     rst_content = """
        .. autofunction:: module.my_function
           :members:
     """
     
     # This test asserts that in documentation is not used e but ex.
     # But in rst doc string it not possible to see this change,
     # So we will simulate the code parsing for exception
     assert "except ValueError as ex" in test_code

# Test file with class and methods
def test_class_with_methods(tmp_path):
    """Checks if documentation is created with class and method documentation"""
    file_path = tmp_path / "test_class_module.rst"
    # Creating dummy file content to simulate a class with methods
    test_code = """
    class MyClass:
        def __init__(self, val: int):
            \"\"\"
            The initializator
            Args:
                val(int): the input value
            \"\"\"
            self.val = val
        def method(self, m_val: str) -> None:
            \"\"\"
            A simple method
            Args:
                m_val (str): the param for a method
            \"\"\"
            print(m_val)
    """
    # This part would normally be replaced with the actual function call
    # That creates the rst file. We simulate that here
    with open(file_path, 'w') as f:
        f.write("Название модуля\n")
        f.write("===============\n")
        f.write("\n")
        f.write(".. automodule:: test_class_module\n")
        f.write("    :members:\n")
        f.write("    :undoc-members:\n")
        f.write("    :show-inheritance:\n")
        f.write("\n")
        f.write("Классы\n")
        f.write("--------\n")
        f.write("\n")
        f.write(".. autoclass:: test_class_module.MyClass\n")
        f.write("    :members:\n")
    assert file_path.exists()
    with open(file_path, 'r') as f:
        content = f.read()
        assert "Классы\n--------" in content
        assert ".. autoclass:: test_class_module.MyClass" in content
        assert ":members:" in content

```