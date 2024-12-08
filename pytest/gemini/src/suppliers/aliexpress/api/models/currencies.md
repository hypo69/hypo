```python
import pytest

from hypotez.src.suppliers.aliexpress.api.models.currencies import Currency


def test_currency_constants():
    """Tests the predefined currency constants."""
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


def test_currency_constants_type():
    """Tests that the currency constants are strings."""
    for constant in [
        Currency.USD,
        Currency.GBP,
        Currency.CAD,
        Currency.EUR,
        Currency.UAH,
        Currency.MXN,
        Currency.TRY,
        Currency.RUB,
        Currency.BRL,
        Currency.AUD,
        Currency.INR,
        Currency.JPY,
        Currency.IDR,
        Currency.SEK,
        Currency.KRW,
        Currency.ILS,
    ]:
        assert isinstance(constant, str)


def test_currency_constants_not_equal():
    """Tests that different currency constants are not equal."""
    assert Currency.USD != Currency.GBP
    assert Currency.USD != 'usd'  # Case-sensitive strings


# No methods or functions to test in the given code, so no more tests are needed
# for this particular file.
```