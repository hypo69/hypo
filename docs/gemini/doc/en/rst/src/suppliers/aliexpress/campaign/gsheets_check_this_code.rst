gsheets_check_this_code.py
=========================

.. module:: hypotez.src.suppliers.aliexpress.campaign.gsheets_check_this_code
    :platform: Windows, Unix
    :synopsis: Google Sheets редактор рекламной кампании AliExpress.


Module Description
------------------

Этот модуль предоставляет класс `AliCampaignGoogleSheet` для работы с Google Sheets при управлении рекламными кампаниями AliExpress.  Класс наследует `SpreadSheet` и расширяет его функциональность для задач, связанных с загрузкой, записью и форматированием данных кампаний, категорий и продуктов.


Classes
-------

.. autoclass:: AliCampaignGoogleSheet
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

(No functions defined in this file)


Methods
-------

.. automethod:: AliCampaignGoogleSheet.__init__
.. automethod:: AliCampaignGoogleSheet.clear
.. automethod:: AliCampaignGoogleSheet.delete_products_worksheets
.. automethod:: AliCampaignGoogleSheet.set_campaign_worksheet
.. automethod:: AliCampaignGoogleSheet.set_products_worksheet
.. automethod:: AliCampaignGoogleSheet.set_categories_worksheet
.. automethod:: AliCampaignGoogleSheet.get_categories
.. automethod:: AliCampaignGoogleSheet.set_category_products
.. automethod:: AliCampaignGoogleSheet._format_categories_worksheet
.. automethod:: AliCampaignGoogleSheet._format_category_products_worksheet