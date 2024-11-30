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


def test_decode_unicode_escape_dict():
    """Tests decoding with a dictionary input."""
    input_dict = {
        'product_name': r'\u05de\u05e7"\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2',
        'category': r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd',
        'price': 123.45
    }
    expected_dict = {
        'product_name': 'ת״ו־ ספקים\nH510M K V2',
        'category': 'עברית חדשה',
        'price': 123.45
    }
    assert decode_unicode_escape(input_dict) == expected_dict

def test_decode_unicode_escape_list():
    """Tests decoding with a list input."""
    input_list = [r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd', r'H510M K V2']
    expected_list = ['עברית חדשה', 'H510M K V2']
    assert decode_unicode_escape(input_list) == expected_list


def test_decode_unicode_escape_string():
    """Tests decoding with a string input."""
    input_string = r'\u05de\u05e7"\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2'
    expected_string = 'ת״ו־ ספקים\nH510M K V2'
    assert decode_unicode_escape(input_string) == expected_string

def test_decode_unicode_escape_no_unicode():
    """Tests handling of strings without unicode escapes."""
    input_string = "This is a normal string"
    expected_string = "This is a normal string"
    assert decode_unicode_escape(input_string) == expected_string

def test_decode_unicode_escape_invalid_unicode():
    """Tests handling of strings with invalid unicode escapes."""
    input_string = r"\u05de\u05e7\x00\u05d8"
    expected_string = r"\u05de\u05e7\x00\u05d8" #Should not raise an error if input is invalid
    assert decode_unicode_escape(input_string) == expected_string

```