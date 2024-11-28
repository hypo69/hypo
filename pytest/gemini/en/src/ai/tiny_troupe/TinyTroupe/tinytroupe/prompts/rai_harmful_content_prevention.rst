```python
import pytest

def test_harmful_content_prevention_valid_input():
    """Checks if the function correctly rejects harmful content."""
    input_text = "This is a harmless sentence."
    assert not check_harmful_content(input_text)


def test_harmful_content_prevention_hateful_input():
    """Checks if the function rejects hateful content."""
    input_text = "This is a hateful message."
    assert check_harmful_content(input_text)

def test_harmful_content_prevention_racist_input():
    """Checks if the function rejects racist content."""
    input_text = "Racist statement."
    assert check_harmful_content(input_text)


def test_harmful_content_prevention_sexist_input():
    """Checks if the function rejects sexist content."""
    input_text = "Sexist comment."
    assert check_harmful_content(input_text)


def test_harmful_content_prevention_lewd_input():
    """Checks if the function rejects lewd content."""
    input_text = "Lewd remark."
    assert check_harmful_content(input_text)


def test_harmful_content_prevention_violent_input():
    """Checks if the function rejects violent content."""
    input_text = "Violent threat."
    assert check_harmful_content(input_text)


def test_harmful_content_prevention_empty_input():
    """Checks if the function handles empty input correctly."""
    input_text = ""
    assert not check_harmful_content(input_text)  # Empty strings aren't harmful


def test_harmful_content_prevention_numeric_input():
    """Checks if the function handles numerical input."""
    input_text = "12345"
    assert not check_harmful_content(input_text)  # Numbers aren't harmful


def test_harmful_content_prevention_case_insensitive():
    """Checks if the function is case insensitive for harmful keywords."""
    input_text = "hATEFUL message"
    assert check_harmful_content(input_text)

def check_harmful_content(text):
    """
    Checks if the input text contains harmful content.
    
    Args:
        text: The input string to check.
        
    Returns:
        True if the text contains harmful content, False otherwise.  Returns False for empty strings. 
    """
    harmful_keywords = ["hateful", "racist", "sexist", "lewd", "violent"]
    text = text.lower()
    for keyword in harmful_keywords:
        if keyword in text:
            return True
    return False


```