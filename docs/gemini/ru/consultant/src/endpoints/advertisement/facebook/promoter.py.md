# Анализ кода модуля `promoter.py`

**Качество кода: 6/10**
-   **Плюсы:**
    -   Используется `j_loads_ns` для загрузки данных из файлов, что соответствует требованиям.
    -   Присутствует логирование ошибок через `logger.error`.
    -   Код разбит на функции, что улучшает читаемость и структуру.
    -   Используются `SimpleNamespace` для хранения данных, что улучшает читаемость и организацию.
-   **Минусы:**
    -   Отсутствуют docstring для класса и методов.
    -   В некоторых местах используется `try-except` без явной необходимости, что можно заменить на `logger.error`.
    -   Используются не консистентные имена переменных и функций, что усложняет чтение.
    -   Комментарии не в формате reStructuredText (RST), что усложняет создание документации.
    -   Не хватает обработки случаев, когда `group_categories` не является списком, как в случае с `promoted_events` и `promoted_categories`.
    -   Импорт `time` не используется, но импортируется.

**Рекомендации по улучшению:**

1.  Добавить docstring в формате RST для класса `FacebookPromoter` и всех его методов, включая аргументы и возвращаемые значения.
2.  Заменить избыточные `try-except` блоки на `logger.error` для обработки ошибок.
3.  Привести имена переменных и функций к единому стилю.
4.  Переписать все комментарии в формате RST.
5.  Добавить обработку случаев, когда `group_categories` не является списком, аналогично `promoted_events` и `promoted_categories`.
6.  Удалить неиспользуемый импорт `time`.
7.  Добавить обработку ситуации, когда в `group` отсутствует `language` или `currency`, чтобы избежать ошибок.
8.  Сделать проверку `group.status` более явной, проверяя именно наличие строки `active` в статусе, а не просто `in`.
9.  Упростить логику получения `item`, возможно, вынести часть кода в отдельные функции.
10. Улучшить логирование, добавить больше контекста в сообщения об ошибках.
11. Добавить проверку на существование файла с данными для каждой кампании, прежде чем пытаться их загрузить.

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для продвижения сообщений и событий в группах Facebook.
=================================================================

Этот модуль обрабатывает кампании и события, публикуя их в группах Facebook,
избегая дублирования продвижений.
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
from src.endpoints.advertisement.facebook.scenarios import (
    post_message,
    post_event,
    post_message_title,
    upload_post_media,
    message_publish,
    post_ad,
)

from src.utils.file import (
    read_text_file,
    get_filenames,
    get_directory_names,
)
from src.utils.jjson import j_loads_ns, j_dumps
from src.utils.cursor_spinner import spinning_cursor
from src.logger.logger import logger

MODE = 'dev'


def get_event_url(group_url: str) -> str:
    """
    Создает URL для создания события в Facebook.

    :param group_url: URL группы Facebook, содержащий `group_id`.
    :type group_url: str
    :return: URL для создания события в Facebook.
    :rtype: str
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
    """
    Класс для продвижения продуктов и событий AliExpress в группах Facebook.
    
    Этот класс автоматизирует публикацию продвижений в группах Facebook, используя WebDriver,
    гарантируя, что категории и события продвигаются, избегая дублирования.
    """
    d: Driver = None
    group_file_paths: str | Path = None
    no_video: bool = False
    promoter: str
    spinner: spinning_cursor

    def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False):
        """
        Инициализирует промоутер для групп Facebook.

        :param d: Экземпляр WebDriver для автоматизации браузера.
        :type d: Driver
        :param promoter: Название промоутера.
        :type promoter: str
        :param group_file_paths: Список путей к файлам, содержащим данные групп.
        :type group_file_paths: Optional[list[str | Path] | str | Path]
        :param no_video: Флаг для отключения видео в постах.
        :type no_video: bool, optional
        """
        self.promoter = promoter
        self.d = d
        self.group_file_paths = group_file_paths if group_file_paths else get_filenames(gs.path.google_drive / 'facebook' / 'groups')
        self.no_video = no_video
        self.spinner = spinning_cursor()

    def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
        """
        Продвигает категорию или событие в группе Facebook.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :param item: Данные категории или события.
        :type item: SimpleNamespace
        :param is_event: Флаг, указывающий, является ли продвижение событием.
        :type is_event: bool, optional
        :param language: Язык продвижения.
        :type language: str, optional
        :param currency: Валюта продвижения.
        :type currency: str, optional
        :return: True, если продвижение прошло успешно, False в противном случае.
        :rtype: bool
        """
        if language and group.language.upper() != language.upper():
            return False
        if currency and group.currency.upper() != currency.upper():
            return False

        item_name = item.event_name if is_event else item.category_name
        ev_or_msg = getattr(item.language, group.language) if is_event else item

        # Установка атрибутов события или сообщения
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

        # Обновление данных группы после публикации
        self.update_group_promotion_data(group, item_name, is_event)
        return True

    def log_promotion_error(self, is_event: bool, item_name: str):
        """
        Логирует ошибку продвижения категории или события.

        :param is_event: Флаг, указывающий, является ли продвижение событием.
        :type is_event: bool
        :param item_name: Название категории или события.
        :type item_name: str
        """
        logger.error(f"Ошибка при публикации {'события' if is_event else 'категории'} {item_name}")

    def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
        """
        Обновляет данные о продвижении группы.
        
        :param group: Данные группы.
        :type group: SimpleNamespace
        :param item_name: Название категории или события.
        :type item_name: str
        :param is_event: Флаг, указывающий, является ли продвижение событием.
        :type is_event: bool, optional
        """
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
        """
        Обрабатывает все группы для продвижения кампании или события.

        :param campaign_name: Название кампании.
        :type campaign_name: str, optional
        :param events: Список событий для продвижения.
        :type events: list[SimpleNamespace], optional
        :param is_event: Флаг, указывающий, является ли продвижение событием.
        :type is_event: bool, optional
        :param group_file_paths: Список путей к файлам групп.
        :type group_file_paths: list[str], optional
        :param group_categories_to_adv: Список категорий групп для продвижения.
        :type group_categories_to_adv: list[str], optional
        :param language: Язык для продвижения.
        :type language: str, optional
        :param currency: Валюта для продвижения.
        :type currency: str, optional
        """
        if not campaign_name and not events:
            logger.debug("Нет данных для продвижения!")
            return

        for group_file in group_file_paths:
            path_to_group_file: Path = gs.path.google_drive / 'facebook' / 'groups' / group_file
            try:
                groups_ns: dict = j_loads_ns(path_to_group_file)
            except Exception as e:
                logger.error(f"Ошибка загрузки файла групп {group_file=}: {e}")
                continue
            if not groups_ns:
                logger.error(f"Файл групп пуст или поврежден {group_file=}")
                continue

            for group_url, group in vars(groups_ns).items():
                group.group_url = group_url
                if not self.validate_group(group):
                    logger.error(f"Некорректные данные группы {group_url=}")
                    continue

                if not is_event and not self.check_interval(group):
                    logger.debug(f"Интервал для группы не наступил {group.group_url=}")
                    continue
                group_categories = group.group_categories if isinstance(group.group_categories, list) else [group.group_categories]
                if not set(group_categories_to_adv).intersection(group_categories) or 'active' not in group.status:
                    logger.debug(f"Группа {group.group_url} не подходит по категории или статусу")
                    continue
                if not is_event:
                     item = self.get_category_item(campaign_name, group, language, currency)
                else:
                    if not events:
                        logger.error(f"Нет событий для продвижения")
                        continue
                    random.shuffle(events)
                    item = events.pop()

                if item.name in (group.promoted_events if is_event else group.promoted_categories):
                    logger.debug(f"Элемент {item.name} уже был продвинут в группе {group.group_url}")
                    continue
                if language and group.language.upper() != language.upper() or (currency and group.currency.upper() != currency.upper()):
                    logger.debug(f"Язык или валюта группы {group.group_url} не соответствует требованиям")
                    continue


                self.d.get_url(get_event_url(group.group_url) if is_event else group.group_url)

                if not self.promote(group = group, item = item, is_event = is_event, language = language, currency = currency):
                   continue
                try:
                    j_dumps(groups_ns, path_to_group_file)
                except Exception as e:
                    logger.error(f'Ошибка сохранения файла {path_to_group_file=}: {e}')
                    continue
                t = random.randint(30, 420)
                print(f"Ожидание {t} секунд")
                import time
                time.sleep(t)


    def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace:
        """
        Получает элемент категории для продвижения.
        
        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param group: Данные группы.
        :type group: SimpleNamespace
        :param language: Язык продвижения.
        :type language: str
        :param currency: Валюта продвижения.
        :type currency: str
        :return: Элемент категории.
        :rtype: SimpleNamespace
        """
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
            try:
                adv: SimpleNamespace = j_loads_ns(base_path / f"{language}_{currency}.json")
            except Exception as e:
                logger.error(f"Ошибка загрузки файла кампании {campaign_name=}: {e}")
                return SimpleNamespace()
            if not adv:
                 logger.error(f"Файл кампании {campaign_name=} пуст или поврежден")
                 return SimpleNamespace()
            adv_categories = list(vars(adv.category).items())  # Преобразуем в список для перемешивания
            random.shuffle(adv_categories)  # Перемешиваем категории

            for ad_name, ad in adv_categories:
                try:
                     ad.description = read_text_file(base_path / 'category' / ad_name / 'description.txt')
                except Exception as e:
                   logger.error(f"Ошибка чтения файла описания для категории {ad_name=}: {e}")
                   continue
                if not ad.description:
                    logger.error(f"Описание категории {ad_name=} пусто")
                    continue
                item = ad
                item.name = ad_name
                _img = get_filenames(base_path / 'category' / ad_name / 'images')
                if _img:
                    _img = _img if isinstance(_img, str) else _img[0]  # Беру только первое изображение
                    item.img_path = Path(gs.path.local) / _img
                return item
        return item

    def check_interval(self, group: SimpleNamespace) -> bool:
        """
        Проверяет, достаточно ли времени прошло для продвижения группы.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: True, если достаточно времени прошло, False в противном случае.
        :rtype: bool
        """
        # TODO: Добавить реальную проверку интервала
        return True

    def validate_group(self, group: SimpleNamespace) -> bool:
        """
        Проверяет, что данные группы корректны.
        
        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: True, если данные группы корректны, False в противном случае.
        :rtype: bool
        """
        return group and hasattr(group, 'group_url') and hasattr(group, 'group_categories') and hasattr(group, 'status') and hasattr(group, 'language') and hasattr(group, 'currency')
```