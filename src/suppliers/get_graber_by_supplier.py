from __future__ import annotations
## \file hypotez/src/suppliers/get_graber_by_supplier.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Module for getting a grabber based on the supplier URL
=========================================================================================

This module provides functionality to retrieve the appropriate grabber object
for a given supplier URL. Each supplier has its own dedicated grabber that
extracts field values from the target HTML page.

Example usage
-------------

.. code-block:: python

    from src.suppliers.get_graber_by_supplier import get_graber_by_supplier_url
    from src.webdriver import WebDriver

    driver = WebDriver()
    url = 'https://www.example.com'
    graber = get_graber_by_supplier_url(driver, url)

    if graber:
        # Use the grabber to extract data
        pass
    else:
        # Handle the case where no grabber is found
        pass
"""
import header

from src.suppliers.aliexpress.graber import Graber as AliexpressGraber
from src.suppliers.amazon.graber import Graber as AmazonGraber
from src.suppliers.bangood.graber import Graber as BangoodGraber
from src.suppliers.cdata.graber import Graber as CdataGraber
from src.suppliers.ebay.graber import Graber as EbayGraber
from src.suppliers.etzmaleh.graber import Graber as EtzmalehGraber
from src.suppliers.gearbest.graber import Graber as GearbestGraber
from src.suppliers.grandadvance.graber import Graber as GrandadvanceGraber
from src.suppliers.hb.graber import Graber as HBGraber
from src.suppliers.ivory.graber import Graber as IvoryGraber
from src.suppliers.ksp.graber import Graber as KspGraber
from src.suppliers.kualastyle.graber import Graber as KualaStyleGraber
from src.suppliers.morlevi.graber import Graber as MorleviGraber
from src.suppliers.visualdg.graber import Graber as VisualDGGraber
from src.suppliers.wallashop.graber import Graber as WallaShopGraber
from src.suppliers.wallmart.graber import Graber as WallmartGraber
from src.logger.logger import logger


MODE = 'dev'


def get_graber_by_supplier_url(self, url: str) -> 'Graber' | None:
    """
    Function that returns the appropriate grabber for a given supplier URL.

    Each supplier has its own grabber, which extracts field values from the target HTML page.

    :param url: Supplier page URL.
    :type url: str
    :return: Graber instance if a match is found, None otherwise.
    :rtype: Optional[object]
    """
    self.driver.get_url(url)
    if url.startswith(('https://aliexpress.com', 'https://wwww.aliexpress.com')):
        return AliexpressGraber(self.driver)

    if url.startswith(('https://amazon.com', 'https://wwww.amazon.com')):
        return AmazonGraber(self.driver)

    if url.startswith(('https://bangood.com', 'https://wwww.bangood.com')):
        return BangoodGraber(self.driver)

    if url.startswith(('https://cdata.co.il', 'https://wwww.cdata.co.il')):
        return CdataGraber(self.driver)

    if url.startswith(('https://ebay.', 'https://wwww.ebay.c')):
        return EbayGraber(self.driver)

    if url.startswith(('https://etzmaleh.co.il','https://www.etzmaleh.co.il')):
        return EtzmalehGraber(self.driver)

    if url.startswith(('https://gearbest.com', 'https://wwww.gearbest.com')):
        return GearbestGraber(self.driver)

    if url.startswith(('https://grandadvance.co.il', 'https://www.grandadvance.co.il')):
        return GrandadvanceGraber(self.driver)

    if url.startswith(('https://hb-digital.co.il', 'https://www.hb-digital.co.il')):
        return HBGraber(self.driver)

    if url.startswith(('https://ivory.co.il', 'https://www.ivory.co.il')):
        return IvoryGraber(self.driver)

    if url.startswith(('https://ksp.co.il', 'https://www.ksp.co.il')):
        return KspGraber(self.driver)

    if url.startswith(('https://kualastyle.com', 'https://www.kualastyle.com')):
        return KualaStyleGraber(self.driver)

    if url.startswith(('https://morlevi.co.il', 'https://www.morlevi.co.il')):
        return MorleviGraber(self.driver)

    if url.startswith(('https://www.visualdg.com', 'https://visualdg.com')):
        return VisualDGGraber(self.driver)

    if url.startswith(('https://wallashop.co.il', 'https://www.wallashop.co.il')):
        return WallaShopGraber(self.driver)

    if url.startswith(('https://www.wallmart.com', 'https://wallmart.com')):
        return WallmartGraber(self.driver)

    logger.debug(f'No graber found for URL: {url}')
    ...
    return