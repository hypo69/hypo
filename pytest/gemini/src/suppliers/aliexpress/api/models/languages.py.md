```python
import pytest

from hypotez.src.suppliers.aliexpress.api.models.languages import Language


def test_language_constants():
    """
    Test that all language constants are defined and are not empty.
    """
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


def test_language_constants_are_strings():
    """
    Test that all language constants are of type string.
    """
    assert isinstance(Language.EN, str)
    assert isinstance(Language.RU, str)
    assert isinstance(Language.PT, str)
    assert isinstance(Language.ES, str)
    assert isinstance(Language.FR, str)
    assert isinstance(Language.ID, str)
    assert isinstance(Language.IT, str)
    assert isinstance(Language.TH, str)
    assert isinstance(Language.JA, str)
    assert isinstance(Language.AR, str)
    assert isinstance(Language.VI, str)
    assert isinstance(Language.TR, str)
    assert isinstance(Language.DE, str)
    assert isinstance(Language.HE, str)
    assert isinstance(Language.KO, str)
    assert isinstance(Language.NL, str)
    assert isinstance(Language.PL, str)
    assert isinstance(Language.MX, str)
    assert isinstance(Language.CL, str)
    assert isinstance(Language.IW, str)
    assert isinstance(Language.IN, str)

def test_language_constants_are_unique():
    """
    Test that language constants are unique
    """
    all_languages = [
        Language.EN,
        Language.RU,
        Language.PT,
        Language.ES,
        Language.FR,
        Language.ID,
        Language.IT,
        Language.TH,
        Language.JA,
        Language.AR,
        Language.VI,
        Language.TR,
        Language.DE,
        Language.HE,
        Language.KO,
        Language.NL,
        Language.PL,
        Language.MX,
        Language.CL,
        Language.IW,
        Language.IN,
    ]
    assert len(all_languages) == len(set(all_languages))
```