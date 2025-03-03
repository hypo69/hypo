## \file /src/suppliers/get_graber_by_supplier.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

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
from src.suppliers.graber import Graber
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


def get_graber_by_supplier_url(driver: 'Driver', url: str, lang_index:int ) -> Graber | None:
    """
    Function that returns the appropriate grabber for a given supplier URL.

    Each supplier has its own grabber, which extracts field values from the target HTML page.

    :param url: Supplier page URL.
    :type url: str
    :param lang_index: Указывает индекс языка в магазине Prestashop
    :return: Graber instance if a match is found, None otherwise.
    :rtype: Optional[object]
    """
    driver.get_url(url)
    if url.startswith(('https://aliexpress.com', 'https://wwww.aliexpress.com')):
        return AliexpressGraber(driver,lang_index)

    if url.startswith(('https://amazon.com', 'https://wwww.amazon.com')):
        return AmazonGraber(driver,lang_index)

    if url.startswith(('https://bangood.com', 'https://wwww.bangood.com')):
        return BangoodGraber(driver,lang_index)

    if url.startswith(('https://cdata.co.il', 'https://wwww.cdata.co.il')):
        return CdataGraber(driver,lang_index)

    if url.startswith(('https://ebay.', 'https://wwww.ebay.')):
        return EbayGraber(driver,lang_index)

    if url.startswith(('https://etzmaleh.co.il','https://www.etzmaleh.co.il')):
        return EtzmalehGraber(driver,lang_index)

    if url.startswith(('https://gearbest.com', 'https://wwww.gearbest.com')):
        return GearbestGraber(driver,lang_index)

    if url.startswith(('https://grandadvance.co.il', 'https://www.grandadvance.co.il')):
        return GrandadvanceGraber(driver,lang_index)

    if url.startswith(('https://hb-digital.co.il', 'https://www.hb-digital.co.il')):
        return HBGraber(driver,lang_index)

    if url.startswith(('https://ivory.co.il', 'https://www.ivory.co.il')):
        return IvoryGraber(driver,lang_index)

    if url.startswith(('https://ksp.co.il', 'https://www.ksp.co.il')):
        return KspGraber(driver,lang_index)

    if url.startswith(('https://kualastyle.com', 'https://www.kualastyle.com')):
        return KualaStyleGraber(driver,lang_index)

    if url.startswith(('https://morlevi.co.il', 'https://www.morlevi.co.il')):
        return MorleviGraber(driver,lang_index)

    if url.startswith(('https://www.visualdg.com', 'https://visualdg.com')):
        return VisualDGGraber(driver,lang_index)

    if url.startswith(('https://wallashop.co.il', 'https://www.wallashop.co.il')):
        return WallaShopGraber(driver,lang_index)

    if url.startswith(('https://www.wallmart.com', 'https://wallmart.com')):
        return WallmartGraber(driver,lang_index)

    logger.debug(f'No graber found for URL: {url}')
    ...
    return