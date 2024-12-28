## \file hypotez/src/endpoints/advertisement/facebook/promoter.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.endpoints.advertisement.facebook 
    :platform: Windows, Unix
    :synopsis: module handles the promotion of messages and events in Facebook groups.
It processes campaigns and events, posting them to Facebook groups while avoiding duplicate promotions.
"""


import random
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import urlencode
from types import SimpleNamespace
from typing import Optional

from src import gs
from src.endpoints.advertisement import facebook
from src.webdriver.driver import Driver
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.endpoints.advertisement.facebook.scenarios import (post_message, 
                                                  post_event, 
                                                  post_message_title, 
                                                  upload_post_media,
                                                  message_publish,
                                                  post_ad,
                                                    )

from src.utils.file import (read_text_file,
                        get_filenames,
                        get_directory_names,
                        )
from src.utils.jjson import j_loads_ns, j_dumps
from src.utils.cursor_spinner import spinning_cursor
from src.logger.logger import logger

def get_event_url(group_url: str) -> str:
    """
    Returns the modified URL for creating an event on Facebook, replacing `group_id` with the value from the input URL.

    Args:
        group_url (str): Facebook group URL containing `group_id`.

    Returns:
        str: Modified URL for creating the event.
    """
    group_id = group_url.rstrip('/').split('/')[-1]
    base_url = "https://www.facebook.com/events/create/"
    params = {
        "acontext": '{"event_action_history":[{"surface":"group"},{"mechanism":"upcoming_events_for_group","surface":"group"}],"ref_notif_type":null}',
        "dialog_entry_point": "group_events_tab",
        "group_id": group_id
    }

    query_string = urlencode(params)
    return f"{base_url}?{query_string}"

class FacebookPromoter:
    """ Class for promoting AliExpress products and events in Facebook groups.
    
    This class automates the posting of promotions to Facebook groups using a WebDriver instance,
    ensuring that categories and events are promoted while avoiding duplicates.
    """
    d: Driver = None
    group_file_paths: str | Path = None
    no_video: bool = False
    promoter: str

    def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False):
        """ Initializes the promoter for Facebook groups.

        Args:
            d (Driver): WebDriver instance for browser automation.
            group_file_paths (list[str | Path] | str | Path): List of file paths containing group data.
            no_video (bool, optional): Flag to disable videos in posts. Defaults to False.
        """
        self.promoter = promoter
        self.d = d
        self.group_file_paths = group_file_paths if group_file_paths else get_filenames(gs.path.google_drive / 'facebook' / 'groups')
        self.no_video = no_video
        self.spinner = spinning_cursor()

    def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
        """Promotes a category or event in a Facebook group.""" 
        ...
        if language:
           if group.language.upper() != language.upper():
                return
        if currency:
            if group.currency.upper() != currency.upper():
                return

        item_name = item.event_name if is_event else item.category_name
        ev_or_msg = getattr(item.language, group.language) if is_event else item

        # Установка атрибутов события или сообщения
        if is_event:
            ev_or_msg.start = item.start
            ev_or_msg.end = item.end
            ev_or_msg.promotional_link = item.promotional_link

            if not post_event(d=self.d, event=ev_or_msg):
                self.log_promotion_error(is_event, item_name)
                return
        else:
            if 'kazarinov' in self.promoter or 'emil' in self.promoter:
                if not post_ad(self.d, ev_or_msg):
                    return


            elif not post_message(d=self.d, message=ev_or_msg, no_video=self.no_video, without_captions=False):
                return

        # Обновление данных группы после публикации
        self.update_group_promotion_data(group, ev_or_msg.name)
        return True

    def log_promotion_error(self, is_event: bool, item_name: str):
        """Logs promotion error for category or event."""
        logger.debug(f"Error while posting {'event' if is_event else 'category'} {item_name}", None, False)

    def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
        """Updates group promotion data with the new promotion.""" 
        timestamp = datetime.now().strftime("%d/%m/%y %H:%M")
        group.last_promo_sended = gs.now
        if is_event:
            group.promoted_events = group.promoted_events if isinstance(group.promoted_events, list) else [group.promoted_events]
            group.promoted_events.append(item_name)
        else:
            group.promoted_categories = group.promoted_categories if isinstance(group.promoted_categories, list) else [group.promoted_categories]
            group.promoted_categories.append(item_name)
        group.last_promo_sended = timestamp

    def process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None):
        """Processes all groups for the current campaign or event promotion."""    
        if not campaign_name and not events:
            logger.debug("Nothing to promote!")
            return

        for group_file in group_file_paths:
            path_to_group_file: Path = gs.path.google_drive / 'facebook' / 'groups' / group_file 
            groups_ns: dict = j_loads_ns(path_to_group_file)

            if not groups_ns:
                logger.error(f"Проблема в файле групп {group_file=}")
                return

            for group_url, group in vars(groups_ns).items():
                group.group_url = group_url

                if not is_event and not self.check_interval(group):
                    logger.debug(f"{campaign_name=}\n Interval in group: {group.group_url}", None, False)
                    continue

                if not set(group_categories_to_adv).intersection(group.group_categories if isinstance(group.group_categories, list) else [group.group_categories]) or not 'active' in group.status:
                    continue

                if not is_event:
                    item = self.get_category_item(campaign_name, group, language, currency)
                else:
                    random.shuffle(events)
                    item = events.pop()
                    

                if item.name in (group.promoted_events if is_event else group.promoted_categories):
                    logger.debug(f"Item already promoted")
                    continue

                if not group.language.upper() == language.upper() and group.currency.upper() == currency.upper():
                   continue

                self.driver.get_url(get_event_url(group.group_url) if is_event else group.group_url)

                if not self.promote(group = group, item = item, is_event = is_event, language = language, currency = currency):
                    continue

                j_dumps(groups_ns, path_to_group_file)
                t = random.randint(30, 420)
                print(f"sleeping {t} sec")
                time.sleep(t)

    def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace:
        """Fetches the category item for promotion based on the campaign and promoter."""    
        if self.promoter == 'aliexpress':
            ce = AliCampaignEditor(campaign_name=campaign_name, language=group.language, currency=group.currency)
            list_categories = ce.list_categories
            random.shuffle(list_categories)
            category_name = list_categories.pop()
            item = ce.get_category(category_name)
            item.name = category_name
            item.products = ce.get_category_products(item.category_name)
        else:
            base_path = gs.path.google_drive / self.promoter / 'campaigns' / campaign_name
            adv: SimpleNamespace = j_loads_ns(base_path / f"{language}_{currency}.json")
            adv_categories = list(vars(adv.category).items())  # Преобразуем в список для перемешивания
            random.shuffle(adv_categories)  # Перемешиваем категории

            for ad_name, ad in adv_categories:
                ad.description = read_text_file(base_path / 'category' / ad_name / 'description.txt')
                if not ad.description:
                    logger.error(f"ошибка чтения файла", None, False)
                    continue
                item = ad
                item.name = ad_name
                _img = get_filenames(base_path / 'category' / ad_name / 'images')
                if _img:
                    _img = _img if isinstance(_img, str) else _img[0]  # Беру только первое изображение
                    item.img_path = Path(gs.path.local) / _img
        return item

    def check_interval(self, group: SimpleNamespace) -> bool:
        """Checks if enough time has passed for promoting this group."""   
        ...
        return True

    def validate_group(self, group: SimpleNamespace) -> bool:
        """Validates that the group data is correct."""   
        return group and hasattr(group, 'group_url') and hasattr(group, 'group_categories')
