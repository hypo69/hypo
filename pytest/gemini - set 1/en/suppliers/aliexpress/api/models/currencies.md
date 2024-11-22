```python
import pytest

from hypotez.src.suppliers.aliexpress.api.models.currencies import Currency


def test_currency_constants():
    """
    Verifies that all currency constants are defined and have the expected string values.
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


# No functions to test, just constants, so no further tests needed.
# The test above is comprehensive since it verifies all defined constants.
```