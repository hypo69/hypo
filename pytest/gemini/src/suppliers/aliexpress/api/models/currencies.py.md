```python
import pytest
from hypotez.src.suppliers.aliexpress.api.models.currencies import Currency


def test_currency_constants():
    """
    Test that all currency constants are defined and are of type str.
    """
    assert isinstance(Currency.USD, str)
    assert isinstance(Currency.GBP, str)
    assert isinstance(Currency.CAD, str)
    assert isinstance(Currency.EUR, str)
    assert isinstance(Currency.UAH, str)
    assert isinstance(Currency.MXN, str)
    assert isinstance(Currency.TRY, str)
    assert isinstance(Currency.RUB, str)
    assert isinstance(Currency.BRL, str)
    assert isinstance(Currency.AUD, str)
    assert isinstance(Currency.INR, str)
    assert isinstance(Currency.JPY, str)
    assert isinstance(Currency.IDR, str)
    assert isinstance(Currency.SEK, str)
    assert isinstance(Currency.KRW, str)
    assert isinstance(Currency.ILS, str)

def test_currency_values():
    """
    Test that the currency constants have the expected values.
    """
    assert Currency.USD == 'USD'
    assert Currency.GBP == 'GBP'
    assert Currency.CAD == 'CAD'
    assert Currency.EUR == 'EUR'
    assert Currency.UAH == 'UAH'
    assert Currency.MXN == 'MXN'
    assert Currency.TRY == 'TRY'
    assert Currency.RUB == 'RUB'
    assert Currency.BRL == 'BRL'
    assert Currency.AUD == 'AUD'
    assert Currency.INR == 'INR'
    assert Currency.JPY == 'JPY'
    assert Currency.IDR == 'IDR'
    assert Currency.SEK == 'SEK'
    assert Currency.KRW == 'KRW'
    assert Currency.ILS == 'ILS'
```