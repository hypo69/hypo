```python
import pytest
import re
from typing import Dict, Any

# The user-provided code goes here
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
    """Checks correct decoding of a dictionary with unicode escapes."""
    input_dict = {
        'product_name': r'\u05de\u05e7"\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2',
        'category': r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd',
        'price': 123.45
    }
    expected_output = {
        'product_name': 'תַּלְמוּד" חכמה\nH510M K V2',
        'category': 'עברית שפה',
        'price': 123.45
    }
    assert decode_unicode_escape(input_dict) == expected_output

def test_decode_unicode_escape_valid_list():
    input_list = [r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd', r'H510M K V2']
    expected_output = ['עברית שפה', 'H510M K V2']
    assert decode_unicode_escape(input_list) == expected_output

def test_decode_unicode_escape_valid_string():
    input_string = r'\u05de\u05e7"\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2'
    expected_output = 'תַּלְמוּד" חכמה\nH510M K V2'
    assert decode_unicode_escape(input_string) == expected_output

def test_decode_unicode_escape_invalid_string():
    """Tests handling of strings that are not valid unicode escapes."""
    input_string = "This string has no \\u escapes."
    expected_output = "This string has no \\u escapes."
    assert decode_unicode_escape(input_string) == expected_output
    
def test_decode_unicode_escape_no_input():
    assert decode_unicode_escape(None) is None

def test_decode_unicode_escape_int():
    assert decode_unicode_escape(123) == 123

```