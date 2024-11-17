

""" Работа с гугл таблицами """


from unicodedata import category
import header
from types import SimpleNamespace
from gspread import Worksheet, Spreadsheet
from src.suppliers.aliexpress.campaign import AliCampaignGoogleSheet
from src.suppliers.aliexpress.campaign.ttypes import CampaignType, CategoryType, ProductType
from src.utils import pprint
from src.logger import logger


campaign_name = "lighting"
category_name = "chandeliers"
language = 'EN'
currency = 'USD'

gs = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)

gs.set_products_worksheet(category_name)
#gs.save_categories_from_worksheet(False)
gs.save_campaign_from_worksheet()
...
