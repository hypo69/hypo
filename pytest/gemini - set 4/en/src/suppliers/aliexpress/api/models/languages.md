```python
import pytest

from hypotez.src.suppliers.aliexpress.api.models.languages import Language

# Test cases for the Language class
def test_language_constants():
    """Tests the language constants."""
    assert Language.EN == 'EN'
    assert Language.RU == 'RU'
    assert Language.PT == 'PT'
    assert Language.ES == 'ES'
    assert Language.FR == 'FR'
    assert Language.ID == 'ID'
    assert Language.IT == 'IT'
    assert Language.TH == 'TH'
    assert Language.JA == 'JA'
    assert Language.AR == 'AR'
    assert Language.VI == 'VI'
    assert Language.TR == 'TR'
    assert Language.DE == 'DE'
    assert Language.HE == 'HE'
    assert Language.KO == 'KO'
    assert Language.NL == 'NL'
    assert Language.PL == 'PL'
    assert Language.MX == 'MX'
    assert Language.CL == 'CL'
    assert Language.IW == 'IW'
    assert Language.IN == 'IN'

# This code assumes the Language class only contains the defined constants.
# Additional tests for methods or other functionalities would be added if they exist.


```