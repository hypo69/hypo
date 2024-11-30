```python
import pytest
import re
from typing import Dict, Any

# The user-provided code goes here
# (Paste the code from the prompt into this block)
import re
from typing import Dict, Any

def decode_unicode_escape(input_data: Dict[str, Any] | list | str) -> Dict[str, Any] | list | str:
    """Функция декодирует значения в словаре, списке или строке, содержащие юникодные escape-последовательности, в читаемый текст.

    Args:
        input_data (dict | list | str): Входные данные - словарь, список или строка, которые могут содержать юникодные escape-последовательности.

    Returns:
        dict | list | str: Преобразованные данные. В случае строки применяется декодирование escape-последовательностей. В случае словаря или списка рекурсивно обрабатываются все значения.
    """
    if isinstance(input_data, dict):
        return {key: decode_unicode_escape(value) for key, value in input_data.items()}
    elif isinstance(input_data, list):
        return [decode_unicode_escape(item) for item in input_data]
    elif isinstance(input_data, str):
        try:
            decoded_string = input_data.encode('utf-8').decode('unicode_escape')
        except UnicodeDecodeError:
            decoded_string = input_data
        
        unicode_escape_pattern = r'\\u[0-9a-fA-F]{4}'
        decoded_string = re.sub(unicode_escape_pattern, lambda match: match.group(0).encode('utf-8').decode('unicode_escape'), decoded_string)
        
        return decoded_string
    else:
        return input_data


def test_decode_unicode_escape_valid_dict():
    """Tests decoding of Unicode escapes in a dictionary."""
    input_dict = {
        'product_name': r'\u05de\u05e7"\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2',
        'category': r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd',
        'price': 123.45
    }
    expected_output = {
        'product_name': 'תַּחַת"\ר ה510M K V2',
        'category': 'עברית ה\u05e9\u05d1\u05d1\u05d9\u05dd',
        'price': 123.45
    }
    assert decode_unicode_escape(input_dict) == expected_output


def test_decode_unicode_escape_valid_list():
    """Tests decoding of Unicode escapes in a list."""
    input_list = [r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd', r'H510M K V2']
    expected_output = ['עברית ה', 'H510M K V2']
    assert decode_unicode_escape(input_list) == expected_output

def test_decode_unicode_escape_valid_string():
    """Tests decoding of Unicode escapes in a string."""
    input_string = r'\u05de\u05e7"\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2'
    expected_output = 'תַּחַת"\ר H510M K V2'
    assert decode_unicode_escape(input_string) == expected_output

def test_decode_unicode_escape_no_escape():
  """Tests that non-escape strings are returned unchanged."""
  input_string = "This string has no escapes."
  assert decode_unicode_escape(input_string) == input_string

def test_decode_unicode_escape_invalid_escape():
  """Tests handling of invalid Unicode escape sequences."""
  input_string = r'\u05de\u05e7\u05x8'  # Invalid escape
  assert decode_unicode_escape(input_string) == r'\u05de\u05e7\u05x8'

```