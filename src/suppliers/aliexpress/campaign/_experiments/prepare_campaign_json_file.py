

""" Проверка создания рекламной кампании """



import header
from pathlib import Path
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src import gs
from src.suppliers.aliexpress.campaign import process_campaign_category, process_campaign,  process_all_campaigns
from src.utils import get_filenames, get_directory_names
from src.utils import pprint
from src.logger import logger

#locales = {'EN': 'USD', 'HE': 'ILS', 'RU': 'ILS'}
campaign_name = 'lighting'
campaign_file = 'EN_US.JSON'
campaign_editor = AliCampaignEditor(campaign_name = campaign_name, campaign_file = campaign_file )
campaign_file
#process_campaign(campaign_name)
#process_all_campaigns()
    