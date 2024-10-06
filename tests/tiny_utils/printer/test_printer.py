
import pytest
import json
from pathlib import Path
from ..printer import pprint

def test_pprint_string():
    """Test that pprint handles and prints a string correctly."""
    from io import StringIO
    import sys

    captured_output = StringIO()
    sys.stdout = captured_output

    pprint("Test string")
    sys.stdout = sys.__stdout__

    output = captured_output.getvalue().strip()
    assert output == "Test string"

def test_pprint_file():
    """Test that pprint reads and prints the content of a file."""
    from io import StringIO
    import sys

    test_file = 'test_file.txt'
    with open(test_file, 'w', encoding='utf-8') as file:
        file.write("File content for testing")

    captured_output = StringIO()
    sys.stdout = captured_output

    pprint(test_file)
    sys.stdout = sys.__stdout__

    output = captured_output.getvalue().strip()
    assert output == "File content for testing"

    # Clean up
    Path(test_file).unlink()

def test_pprint_dict():
    """Test that pprint handles and prints dictionaries correctly."""
    test_data = {'key1': 'value1', 'key2': Path('/path/to/file')}
    
    from io import StringIO
    import sys

    captured_output = StringIO()
    sys.stdout = captured_output

    pprint(test_data)
    sys.stdout = sys.__stdout__

    expected_output = json.dumps({'key1': 'value1', 'key2': '/path/to/file'}, indent=4, ensure_ascii=False)
    output = captured_output.getvalue().strip()
    
    assert output == expected_output

def test_pprint_list():
    """Test that pprint handles and prints lists correctly."""
    test_data = [1, 2, Path('/path/to/file')]
    
    from io import StringIO
    import sys

    captured_output = StringIO()
    sys.stdout = captured_output

    pprint(test_data)
    sys.stdout = sys.__stdout__

    output = captured_output.getvalue().strip()
    assert output == str([1, 2, '/path/to/file'])

def test_pprint_object():
    """Test that pprint prints class information correctly."""
    class TestClass:
        def __init__(self, var1: str, var2: bool = False):
            self.var1 = var1
            self.var2 = var2

    obj = TestClass("value1", True)

    from io import StringIO
    import sys

    captured_output = StringIO()
    sys.stdout = captured_output

    pprint(obj)
    sys.stdout = sys.__stdout__

    output = captured_output.getvalue().strip().split('\n')
    assert "Class: TestClass" in output
    assert "Methods:" in output
    assert "Properties:" in output
    assert "var1 = value1" in output
    assert "var2 = True" in output
