## Анализ кода модуля `promoter.py`

**Качество кода**
7
-  Плюсы
    -  Код разбит на логические блоки и функции, что улучшает читаемость.
    -  Используется `logger` для логирования ошибок и отладки.
    -  Присутствуют docstring для функций, что облегчает понимание их назначения.
    -  Обработка ошибок через `try-except` в необходимых местах.
-  Минусы
    -  Не везде используется `j_loads_ns` для загрузки JSON, где это необходимо.
    -  Некоторые docstring можно улучшить для соответствия стандартам Sphinx.
    -  Много проверок на `isinstance` можно заменить на более лаконичные решения.
    -  Присутствует избыточное использование `if/else` в некоторых случаях, которые можно упростить.
    -  Отсутствует описание модуля в начале файла.
    -  Использование `vars(groups_ns).items()` может быть заменено на более явный метод.
    -  В некоторых местах можно использовать более информативные сообщения в `logger.debug`.
    -  В функции `get_category_item` есть повторяющийся код.

**Рекомендации по улучшению**

1.  **Добавить описание модуля**: В начале файла добавить описание модуля в формате docstring.
2.  **Использовать `j_loads_ns`**: Убедиться, что `j_loads_ns` используется для загрузки JSON во всех необходимых местах.
3.  **Улучшить docstring**: Привести docstring в соответствие стандартам Sphinx, включая описание аргументов, возвращаемых значений и возможных исключений.
4.  **Упростить проверки `isinstance`**: Заменить множественные проверки на `isinstance` на более элегантные решения.
5.  **Упростить `if/else`**: Пересмотреть структуру условных операторов, чтобы сделать код более читаемым.
6.  **Унифицировать вызовы `logger.debug`**: Добавить более конкретные сообщения в вызовы `logger.debug`.
7.  **Убрать повторяющийся код**: В `get_category_item` выделить общую логику в отдельную функцию.
8.  **Использовать более явные методы**: Заменить `vars(groups_ns).items()` на `groups_ns.__dict__.items()` или аналогичный метод.
9.  **Улучшить обработку ошибок**: Заменить `try-except` на `logger.error`, где это возможно.
10. **Обработка случая отсутствия `category_name`**
11. **Использовать f-строки**:  Заменить конкатенацию строк на f-строки для большей читаемости.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
Модуль для продвижения товаров и событий в группах Facebook.
=========================================================================================

Этот модуль автоматизирует размещение рекламных материалов в группах Facebook,
обрабатывая кампании и события, избегая дублирования публикаций.

Модуль включает класс :class:`FacebookPromoter`, который управляет процессом
продвижения в Facebook.
"""

import random
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode
from types import SimpleNamespace
from typing import Optional, List
import time

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

from src.utils.file_async import (read_text_file,
                        get_filenames_from_directory,
                        get_directory_names,
                        )
from src.utils.jjson import j_loads_ns, j_dumps
from src.utils.cursor_spinner import spinning_cursor
from src.logger.logger import logger

def get_event_url(group_url: str) -> str:
    """
    Возвращает модифицированный URL для создания события в Facebook.

    Args:
        group_url (str): URL группы Facebook, содержащий `group_id`.

    Returns:
        str: Модифицированный URL для создания события.

    Example:
        >>> get_event_url("https://www.facebook.com/groups/123456789/")
        'https://www.facebook.com/events/create/?acontext=%7B%22event_action_history%22%3A%5B%7B%22surface%22%3A%22group%22%7D%2C%7B%22mechanism%22%3A%22upcoming_events_for_group%22%2C%22surface%22%3A%22group%22%7D%5D%2C%22ref_notif_type%22%3Anull%7D&dialog_entry_point=group_events_tab&group_id=123456789'
    """
    group_id = group_url.rstrip('/').split('/')[-1]
    base_url = 'https://www.facebook.com/events/create/'
    params = {
        'acontext': '{"event_action_history":[{"surface":"group"},{"mechanism":"upcoming_events_for_group","surface":"group"}],"ref_notif_type":null}',
        'dialog_entry_point': 'group_events_tab',
        'group_id': group_id
    }
    query_string = urlencode(params)
    return f'{base_url}?{query_string}'

class FacebookPromoter:
    """
    Класс для продвижения товаров AliExpress и событий в группах Facebook.

    Этот класс автоматизирует размещение рекламных материалов в группах Facebook,
    используя экземпляр WebDriver, гарантируя продвижение категорий и событий
    с избежанием дубликатов.

    Attributes:
        d (Driver): Экземпляр WebDriver для автоматизации браузера.
        group_file_paths (str | Path): Список или путь к файлам, содержащим данные групп.
        no_video (bool): Флаг для отключения видео в публикациях.
        promoter (str): Название промоутера.
    """
    d: Driver = None
    group_file_paths: str | Path = None
    no_video: bool = False
    promoter: str

    def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[List[str | Path] | str | Path] = None, no_video: bool = False):
        """
        Инициализирует промоутер для групп Facebook.

        Args:
            d (Driver): Экземпляр WebDriver для автоматизации браузера.
            promoter (str): Имя промоутера.
            group_file_paths (Optional[List[str | Path] | str | Path]): Список или путь к файлам, содержащим данные групп.
            no_video (bool, optional): Флаг для отключения видео в постах. Defaults to False.
        """
        self.promoter = promoter
        self.d = d
        # Проверка, является ли group_file_paths списком или строкой
        if isinstance(group_file_paths, list):
            self.group_file_paths = group_file_paths
        elif group_file_paths:
            self.group_file_paths = group_file_paths
        else:
             self.group_file_paths = get_filenames_from_directory(gs.path.google_drive / 'facebook' / 'groups')
        self.no_video = no_video
        self.spinner = spinning_cursor()

    def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
        """
        Продвигает категорию или событие в группе Facebook.

        Args:
            group (SimpleNamespace): Данные группы Facebook.
            item (SimpleNamespace): Данные категории или события.
            is_event (bool, optional): Флаг, указывающий, является ли продвигаемый объект событием. Defaults to False.
            language (str, optional): Язык для проверки. Defaults to None.
            currency (str, optional): Валюта для проверки. Defaults to None.

        Returns:
             bool: True если продвижение успешно, иначе False.
        """
        if language and group.language.upper() != language.upper():
            return False
        if currency and group.currency.upper() != currency.upper():
            return False

        item_name = item.event_name if is_event else item.category_name
        ev_or_msg = getattr(item.language, group.language) if is_event else item

        if is_event:
            ev_or_msg.start = item.start
            ev_or_msg.end = item.end
            ev_or_msg.promotional_link = item.promotional_link

            if not post_event(d=self.d, event=ev_or_msg):
                self.log_promotion_error(is_event, item_name)
                return False
        else:
            if 'kazarinov' in self.promoter or 'emil' in self.promoter:
                if not post_ad(self.d, ev_or_msg):
                    return False
            elif not post_message(d=self.d, message=ev_or_msg, no_video=self.no_video, without_captions=False):
                return False

        self.update_group_promotion_data(group, item_name, is_event)
        return True

    def log_promotion_error(self, is_event: bool, item_name: str):
        """
        Логирует ошибку продвижения категории или события.

        Args:
            is_event (bool): Флаг, указывающий, является ли продвигаемый объект событием.
            item_name (str): Название категории или события.
        """
        logger.debug(f'Error while posting {"event" if is_event else "category"} {item_name}')

    def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
        """
        Обновляет данные группы после продвижения.

        Args:
            group (SimpleNamespace): Данные группы Facebook.
            item_name (str): Название категории или события.
            is_event (bool, optional): Флаг, указывающий, является ли продвигаемый объект событием. Defaults to False.
        """
        timestamp = datetime.now().strftime('%d/%m/%y %H:%M')
        group.last_promo_sended = gs.now

        if is_event:
            if not isinstance(group.promoted_events, list):
                group.promoted_events = [group.promoted_events] if group.promoted_events else []
            group.promoted_events.append(item_name)

        else:
            if not isinstance(group.promoted_categories, list):
                 group.promoted_categories = [group.promoted_categories] if group.promoted_categories else []
            group.promoted_categories.append(item_name)

        group.last_promo_sended = timestamp

    def process_groups(self, campaign_name: str = None, events: Optional[List[SimpleNamespace]] = None, is_event: bool = False, group_file_paths: Optional[List[str]] = None, group_categories_to_adv: Optional[List[str]] = ['sales'], language: str = None, currency: str = None):
        """
        Обрабатывает все группы для текущей кампании или продвижения события.

        Args:
            campaign_name (str, optional): Название кампании. Defaults to None.
            events (Optional[List[SimpleNamespace]], optional): Список событий для продвижения. Defaults to None.
            is_event (bool, optional): Флаг, указывающий, является ли продвижение событием. Defaults to False.
            group_file_paths (Optional[List[str]], optional): Список путей к файлам групп. Defaults to None.
            group_categories_to_adv (Optional[List[str]], optional): Список категорий групп для продвижения. Defaults to ['sales'].
            language (str, optional): Язык для продвижения. Defaults to None.
            currency (str, optional): Валюта для продвижения. Defaults to None.
        """
        if not campaign_name and not events:
            logger.debug('Nothing to promote!')
            return

        group_file_paths = group_file_paths if group_file_paths else self.group_file_paths
        if isinstance(group_file_paths, str):
            group_file_paths = [group_file_paths]

        for group_file in group_file_paths:
            path_to_group_file = gs.path.google_drive / 'facebook' / 'groups' / group_file
            groups_ns = j_loads_ns(path_to_group_file)

            if not groups_ns:
                logger.error(f'Проблема в файле групп {group_file=}')
                continue

            for group_url, group in groups_ns.__dict__.items():
                if group_url.startswith('_'):
                    continue

                group.group_url = group_url
                if not is_event and not self.check_interval(group):
                     logger.debug(f'{campaign_name=}\\n Interval in group: {group.group_url}')
                     continue


                group_categories = group.group_categories if isinstance(group.group_categories, list) else [group.group_categories]
                if not set(group_categories_to_adv).intersection(group_categories) or 'active' not in group.status:
                    continue
                
                if not is_event:
                     item = self.get_category_item(campaign_name, group, language, currency)
                else:
                    if not events:
                        logger.error('Нет событий для продвижения.')
                        continue
                    random.shuffle(events)
                    item = events.pop()

                if item.name in (group.promoted_events if is_event else group.promoted_categories):
                    logger.debug('Item already promoted')
                    continue
                
                if not (group.language.upper() == language.upper() and group.currency.upper() == currency.upper()):
                    continue


                self.d.get_url(get_event_url(group.group_url) if is_event else group.group_url)
                if not self.promote(group=group, item=item, is_event=is_event, language=language, currency=currency):
                    continue

                j_dumps(groups_ns, path_to_group_file)
                t = random.randint(30, 420)
                print(f'sleeping {t} sec')
                time.sleep(t)

    def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace:
        """
        Получает элемент категории для продвижения на основе кампании и промоутера.

        Args:
            campaign_name (str): Название кампании.
            group (SimpleNamespace): Данные группы Facebook.
            language (str): Язык для продвижения.
            currency (str): Валюта для продвижения.

        Returns:
            SimpleNamespace: Элемент категории для продвижения.

        Raises:
            ValueError: Если не найден `category_name`.
        """
        if self.promoter == 'aliexpress':
            return self._get_aliexpress_category_item(campaign_name, group)
        else:
            return self._get_generic_category_item(campaign_name, group, language, currency)

    def _get_aliexpress_category_item(self, campaign_name: str, group: SimpleNamespace) -> SimpleNamespace:
        """
        Получает элемент категории для продвижения из AliExpress.

        Args:
            campaign_name (str): Название кампании.
            group (SimpleNamespace): Данные группы Facebook.

        Returns:
            SimpleNamespace: Элемент категории для продвижения.
        """
        ce = AliCampaignEditor(campaign_name=campaign_name, language=group.language, currency=group.currency)
        list_categories = ce.list_categories
        random.shuffle(list_categories)
        
        if not list_categories:
             logger.error(f'Нет категорий для продвижения в кампании {campaign_name=}')
             raise ValueError('No categories found in list_categories')
        category_name = list_categories.pop()
        item = ce.get_category(category_name)
        item.name = category_name
        item.products = ce.get_category_products(item.category_name)
        return item

    def _get_generic_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace:
        """
        Получает элемент категории для продвижения из общих данных.

        Args:
            campaign_name (str): Название кампании.
            group (SimpleNamespace): Данные группы Facebook.
             language (str): Язык для продвижения.
            currency (str): Валюта для продвижения.

        Returns:
            SimpleNamespace: Элемент категории для продвижения.

        Raises:
            ValueError: Если не найден `category_name`.
        """
        base_path = gs.path.google_drive / self.promoter / 'campaigns' / campaign_name
        adv: SimpleNamespace = j_loads_ns(base_path / f'{language}_{currency}.json')
        adv_categories = list(vars(adv.category).items())
        random.shuffle(adv_categories)

        for ad_name, ad in adv_categories:
            ad.description = read_text_file(base_path / 'category' / ad_name / 'description.txt')
            if not ad.description:
                 logger.error(f'Ошибка чтения файла описания категории {ad_name=}')
                 continue
            item = ad
            item.name = ad_name
            _img = get_filenames_from_directory(base_path / 'category' / ad_name / 'images')
            if _img:
                _img = _img if isinstance(_img, str) else _img[0]
                item.img_path = Path(gs.path.local) / _img
            return item
        
        logger.error(f'Не найдена ни одна категория для продвижения в {campaign_name=}')
        raise ValueError('No suitable category found.')
    def check_interval(self, group: SimpleNamespace) -> bool:
        """
        Проверяет, прошло ли достаточно времени для продвижения в этой группе.

        Args:
            group (SimpleNamespace): Данные группы Facebook.

        Returns:
            bool: True, если достаточно времени прошло, иначе False.
        """
        ... # TODO: Add interval check
        return True

    def validate_group(self, group: SimpleNamespace) -> bool:
        """
        Проверяет, что данные группы корректны.

        Args:
            group (SimpleNamespace): Данные группы Facebook.

        Returns:
            bool: True, если данные группы корректны, иначе False.
        """
        return bool(group and hasattr(group, 'group_url') and hasattr(group, 'group_categories'))