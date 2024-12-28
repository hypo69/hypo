from __future__ import annotations
## \file hypotez/src/suppliers/get_graber_by_supplier.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""

```rst
.. module:: src.suppliers.get_graber_by_supplier 
	:platform: Windows, Unix
	:synopsis: Возвращает объект Graber для конкретного поставщика
```  

"""
import header

from src.suppliers.morlevi.graber import Graber as MorleviGraber
from src.suppliers.ksp.graber import Graber as KspGraber
from src.suppliers.ivory.graber import Graber as IvoryGraber
from src.suppliers.grandadvance.graber import Graber as GrandadvanceGraber
from src.suppliers.aliexpress.graber import Graber as AliexpressGraber
from src.suppliers.amazon.graber import Graber as AmazonGraber
from src.suppliers.ebay.graber import Graber as EbayGraber

from src.logger import logger

def get_graber_by_supplier_url(self, url: str):
    """
    Returns the appropriate graber for a given supplier URL.
    Для каждого поставщика реализован свой грабер, который вытаскивает значения полей с целевой html страницы 

    Args:
        url (str): Supplier page URL.

    Returns:
        Optional[object]: Graber instance if a match is found, None otherwise.
    """
    self.driver.get_url(url)
    if url.startswith(('https://morlevi.co.il', 'https://www.morlevi.co.il')):
        return MorleviGraber(self.driver)

    if url.startswith(('https://ksp.co.il', 'https://www.ksp.co.il')):
        return KspGraber(self.driver)

    if url.startswith(('https://grandadvance.co.il', 'https://www.grandadvance.co.il')):
        return GrandadvanceGraber(self.driver)

    if url.startswith(('https://ivory.co.il', 'https://www.ivory.co.il')):
        return IvoryGraber(self.driver)

    if url.startswith('https://aliexpress.com','https://wwww.aliexpress.com' ):
        return AliexpressGraber(self.driver)

    if url.startswith('https://amazon.com','https://wwww.amazon.com' ):
        return AmazonGraber(self.driver)

    logger.debug(f'No graber found for URL: {url}')
    ...
    return 
