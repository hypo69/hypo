```python
import pytest
import json

# Fixture for loading the html escapes
@pytest.fixture
def html_escapes():
    """Loads the html escape mapping from the JSON file."""
    with open("hypotez/src/utils/string/html_escapes.json", "r") as f:
        return json.load(f)

# Test case to verify that the html_escapes is a dictionary
def test_html_escapes_is_dict(html_escapes):
    """Checks if the loaded data is a dictionary."""
    assert isinstance(html_escapes, dict), "The loaded data should be a dictionary."

# Test case to verify the length of html_escapes
def test_html_escapes_length(html_escapes):
    """Checks the number of items in the dictionary."""
    expected_length = 252
    assert len(html_escapes) == expected_length, f"The dictionary should have {expected_length} items."

# Test case to check the correct mapping for '&'
def test_html_escapes_ampersand(html_escapes):
    """Checks the correct mapping for '&'."""
    assert html_escapes.get('&') == "&amp;", "The '&' should map to '&amp;'"

# Test case to check the correct mapping for '<'
def test_html_escapes_less_than(html_escapes):
    """Checks the correct mapping for '<'."""
    assert html_escapes.get('<') == "&lt;", "The '<' should map to '&lt;'"

# Test case to check the correct mapping for '>'
def test_html_escapes_greater_than(html_escapes):
    """Checks the correct mapping for '>'."""
    assert html_escapes.get('>') == "&gt;", "The '>' should map to '&gt;'"

# Test case to check the correct mapping for '"'
def test_html_escapes_double_quote(html_escapes):
     """Checks the correct mapping for '"'."""
     assert html_escapes.get('"') == "&quot;", "The '\"' should map to '&quot;'"

# Test case to check the correct mapping for '\''
def test_html_escapes_single_quote(html_escapes):
    """Checks the correct mapping for '\''."""
    assert html_escapes.get('\'') == "&#39;", "The '\\'' should map to '&#39;'"

# Test case to verify that the mapping for '¡' is correct
def test_html_escapes_inverted_exclamation(html_escapes):
    """Checks the correct mapping for '¡'."""
    assert html_escapes.get('¡') == "&iexcl;", "The '¡' should map to '&iexcl;'"

# Test case to verify that the mapping for '¢' is correct
def test_html_escapes_cent(html_escapes):
    """Checks the correct mapping for '¢'."""
    assert html_escapes.get('¢') == "&cent;", "The '¢' should map to '&cent;'"

# Test case to verify that the mapping for '£' is correct
def test_html_escapes_pound(html_escapes):
    """Checks the correct mapping for '£'."""
    assert html_escapes.get('£') == "&pound;", "The '£' should map to '&pound;'"

# Test case to verify that the mapping for '¤' is correct
def test_html_escapes_currency(html_escapes):
    """Checks the correct mapping for '¤'."""
    assert html_escapes.get('¤') == "&curren;", "The '¤' should map to '&curren;'"
  
# Test case to verify that the mapping for '¥' is correct
def test_html_escapes_yen(html_escapes):
    """Checks the correct mapping for '¥'."""
    assert html_escapes.get('¥') == "&yen;", "The '¥' should map to '&yen;'"

# Test case to verify that the mapping for a character that is not in the dictionary returns None
def test_html_escapes_non_existent_character(html_escapes):
     """Checks that a non-existent character mapping returns None."""
     assert html_escapes.get('~') is None, "Should return None for a non-existent key."

# Test case for checking the mapping of a random character from the list
def test_html_escapes_random_character(html_escapes):
    """Checks the correct mapping for a random character."""
    random_char = 'Ω'
    assert html_escapes.get(random_char) == "&Omega;", f"The '{random_char}' should map to '&Omega;'"

# Test case to ensure the dictionary contains Greek letters
def test_html_escapes_greek_letters(html_escapes):
     """Verifies that greek letters are mapped correctly."""
     assert html_escapes.get('α') == "&alpha;", "The 'α' should map to '&alpha;'"
     assert html_escapes.get('β') == "&beta;", "The 'β' should map to '&beta;'"
     assert html_escapes.get('γ') == "&gamma;", "The 'γ' should map to '&gamma;'"
     assert html_escapes.get('Δ') == "&Delta;", "The 'Δ' should map to '&Delta;'"

# Test case for mathematical operators
def test_html_escapes_mathematical_operators(html_escapes):
    """Verifies that mathematical operators are mapped correctly."""
    assert html_escapes.get('∀') == "&forall;", "The '∀' should map to '&forall;'"
    assert html_escapes.get('∞') == "&infin;", "The '∞' should map to '&infin;'"
    assert html_escapes.get('∈') == "&isin;", "The '∈' should map to '&isin;'"

# Test case for currency symbols
def test_html_escapes_currency_symbols(html_escapes):
    """Verifies that currency symbols are mapped correctly."""
    assert html_escapes.get('€') == "&euro;", "The '€' should map to '&euro;'"

# Test case for arrows
def test_html_escapes_arrows(html_escapes):
    """Verifies that arrows are mapped correctly."""
    assert html_escapes.get('→') == "&rarr;", "The '→' should map to '&rarr;'"
    assert html_escapes.get('⇐') == "&lArr;", "The '⇐' should map to '&lArr;'"

# Test case for quotation marks and other punctuation
def test_html_escapes_punctuation(html_escapes):
   """Verifies that special punctuation marks are mapped correctly."""
   assert html_escapes.get('‘') == "&lsquo;", "The '‘' should map to '&lsquo;'"
   assert html_escapes.get('”') == "&rdquo;", "The '”' should map to '&rdquo;'"

# Test case for some specific symbols
def test_html_escapes_specific_symbols(html_escapes):
    """Tests some of the specific symbols included in the mapping."""
    assert html_escapes.get('•') == "&bull;", "The '•' should map to '&bull;'"
    assert html_escapes.get('™') == "&trade;", "The '™' should map to '&trade;'"

# Test case to verify the mapping for symbols with special meaning in HTML
def test_html_escapes_special_html_symbols(html_escapes):
    """Verifies the mapping of HTML special symbols."""
    assert html_escapes.get('"') == "&quot;", 'The \'\"\' should map to "&quot;"'
    assert html_escapes.get("'") == "&#39;", "The \' should map to &#39;"
```