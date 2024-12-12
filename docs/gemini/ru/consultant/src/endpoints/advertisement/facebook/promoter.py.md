# Анализ кода модуля `promoter.py`

**Качество кода: 7/10**

*   **Плюсы:**
    *   Код структурирован в класс `FacebookPromoter`, что облегчает организацию функциональности.
    *   Используются `SimpleNamespace` для представления данных, что является удобным подходом.
    *   Функции имеют docstring, что упрощает понимание их назначения.
    *   Логирование ошибок осуществляется с помощью `logger`, что помогает в отладке.
    *   Используется `j_loads_ns` для загрузки JSON, что соответствует инструкции.
    *   Код избегает явных `try-except` блоков, полагаясь на `logger.error`.

*   **Минусы:**
    *   Не все функции имеют полное документирование в формате reStructuredText.
    *   В некоторых местах используется `logger.debug` без указания исключения, что может затруднить отладку.
    *   Метод `check_interval` не имеет реализации.
    *   Не все переменные имеют аннотации типов.
    *   Смешение логики в методе `process_groups`, который выполняет несколько задач (подготовка данных, проверка условий, публикация).
    *   В `get_category_item` логика выбора категории для разных промоутеров (aliexpress vs другие) могла бы быть более гибкой.
    *   В методе `get_category_item` смешано чтение текстовых файлов и JSON, что усложняет понимание.
    *   Не везде используется f-строки для форматирования строк.

**Рекомендации по улучшению:**

1.  **Документация:**
    *   Дополнить все docstring в стиле reStructuredText для каждой функции, метода и класса.
    *   Улучшить docstring для `FacebookPromoter`, добавив больше информации о его использовании.
2.  **Логирование:**
    *   В `logger.debug` добавлять исключение, если оно есть, для более подробной информации об ошибках.
    *   Пересмотреть использование `logger.debug` и, возможно, заменить некоторые на `logger.info`.
3.  **Структура:**
    *   Разделить метод `process_groups` на несколько более мелких функций для лучшего управления потоком и переиспользования кода.
    *   Выделить логику выбора категорий в `get_category_item` в отдельный метод или класс для большей гибкости.
4.  **Типизация:**
    *   Добавить аннотации типов для переменных, где это необходимо.
5.  **Обработка ошибок:**
    *   В `get_category_item` добавить обработку исключений при чтении файлов.
6.  **Интервал:**
    *   Реализовать метод `check_interval`.
7.  **Форматирование:**
    *   Использовать f-строки для форматирования строк, где это уместно.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для управления продвижением в Facebook группах.
======================================================

Этот модуль предоставляет класс :class:`FacebookPromoter`,
который автоматизирует процесс публикации сообщений и событий в Facebook группах.
Он обрабатывает кампании и события, публикуя их в Facebook группах, избегая дубликатов продвижения.

:Example:

    .. code-block:: python

        promoter = FacebookPromoter(driver, 'my_promoter')
        promoter.process_groups(campaign_name='my_campaign', is_event=False)
"""
MODE = 'dev'

import random
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode
from types import SimpleNamespace
from typing import Optional, List, Any

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
import time


def get_event_url(group_url: str) -> str:
    """
    Создает URL для создания события в Facebook.

    :param group_url: URL Facebook группы, содержащий идентификатор группы.
    :type group_url: str
    :return: URL для создания события.
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
    Класс для управления продвижением товаров и событий в Facebook группах.

    Этот класс автоматизирует публикацию рекламы в Facebook группах с помощью WebDriver,
    обеспечивая продвижение категорий и событий, избегая дубликатов.

    :ivar d: Экземпляр WebDriver для управления браузером.
    :vartype d: Driver
    :ivar group_file_paths: Пути к файлам с данными групп.
    :vartype group_file_paths: str | Path
    :ivar no_video: Флаг для отключения видео в постах.
    :vartype no_video: bool
    :ivar promoter: Имя промоутера.
    :vartype promoter: str
    """
    d: Driver = None
    group_file_paths: str | Path = None
    no_video: bool = False
    promoter: str

    def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[List[str | Path] | str | Path] = None, no_video: bool = False):
        """
        Инициализирует промоутер для Facebook групп.

        :param d: Экземпляр WebDriver для автоматизации браузера.
        :type d: Driver
        :param promoter: Имя промоутера.
        :type promoter: str
        :param group_file_paths: Список путей к файлам, содержащим данные групп.
        :type group_file_paths: Optional[List[str | Path] | str | Path]
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
        Продвигает категорию или событие в Facebook группе.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :param item: Данные элемента для продвижения (событие или категория).
        :type item: SimpleNamespace
        :param is_event: Флаг, указывающий, является ли продвигаемый элемент событием.
        :type is_event: bool, optional
        :param language: Язык для продвижения.
        :type language: str, optional
        :param currency: Валюта для продвижения.
        :type currency: str, optional
        :return: True, если продвижение прошло успешно, иначе False.
        :rtype: bool
        """
        ...
        if language:
            if group.language.upper() != language.upper():
                return False
        if currency:
            if group.currency.upper() != currency.upper():
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

    def log_promotion_error(self, is_event: bool, item_name: str) -> None:
        """
        Логирует ошибку продвижения категории или события.

        :param is_event: Флаг, указывающий, является ли продвигаемый элемент событием.
        :type is_event: bool
        :param item_name: Название элемента, для которого произошла ошибка.
        :type item_name: str
        """
        logger.debug(f"Ошибка при публикации {'события' if is_event else 'категории'} {item_name}")

    def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False) -> None:
        """
        Обновляет данные о продвижении группы.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :param item_name: Название элемента (событие или категория), который был продвинут.
        :type item_name: str
        :param is_event: Флаг, указывающий, является ли продвигаемый элемент событием.
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

    def process_groups(self, campaign_name: str = None, events: Optional[List[SimpleNamespace]] = None, is_event: bool = False,
                       group_file_paths: Optional[List[str]] = None, group_categories_to_adv: List[str] = ['sales'],
                       language: str = None, currency: str = None) -> None:
        """
        Обрабатывает все группы для текущей кампании или продвижения события.

        :param campaign_name: Название кампании.
        :type campaign_name: str, optional
        :param events: Список событий для продвижения.
        :type events: Optional[List[SimpleNamespace]], optional
        :param is_event: Флаг, указывающий, является ли продвижение событием.
        :type is_event: bool, optional
        :param group_file_paths: Список путей к файлам групп.
        :type group_file_paths: Optional[List[str]], optional
        :param group_categories_to_adv: Список категорий для продвижения.
        :type group_categories_to_adv: List[str], optional
        :param language: Язык для продвижения.
        :type language: str, optional
        :param currency: Валюта для продвижения.
        :type currency: str, optional
        """
        if not campaign_name and not events:
            logger.debug("Нечего продвигать!")
            return

        group_file_paths = group_file_paths or self.group_file_paths
        if isinstance(group_file_paths, str):
            group_file_paths = [group_file_paths]
        for group_file in group_file_paths:
            path_to_group_file: Path = gs.path.google_drive / 'facebook' / 'groups' / group_file
            groups_ns: dict = j_loads_ns(path_to_group_file)

            if not groups_ns:
                logger.error(f"Проблема в файле групп {group_file=}")
                return

            for group_url, group in vars(groups_ns).items():
                group.group_url = group_url

                if not is_event and not self.check_interval(group):
                    logger.debug(f"{campaign_name=}\n Интервал в группе: {group.group_url}")
                    continue

                if not set(group_categories_to_adv).intersection(group.group_categories if isinstance(group.group_categories, list) else [group.group_categories]) or not 'active' in group.status:
                    continue

                item = self._get_promotion_item(campaign_name, events, group, is_event, language, currency)

                if item.name in (group.promoted_events if is_event else group.promoted_categories):
                    logger.debug(f"Элемент уже продвигался: {item.name}")
                    continue

                if language and group.language.upper() != language.upper() or currency and group.currency.upper() != currency.upper():
                   continue

                self.d.get_url(get_event_url(group.group_url) if is_event else group.group_url)

                if not self.promote(group=group, item=item, is_event=is_event, language=language, currency=currency):
                    continue

                j_dumps(groups_ns, path_to_group_file)
                t = random.randint(30, 420)
                print(f"Засыпаю на {t} сек")
                time.sleep(t)

    def _get_promotion_item(self, campaign_name: str, events: Optional[List[SimpleNamespace]], group: SimpleNamespace,
                           is_event: bool, language: str, currency: str) -> SimpleNamespace:
        """
        Получает элемент для продвижения (категорию или событие).

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param events: Список событий для продвижения.
        :type events: Optional[List[SimpleNamespace]]
        :param group: Данные группы.
        :type group: SimpleNamespace
        :param is_event: Флаг, указывающий, является ли продвижение событием.
        :type is_event: bool
        :param language: Язык для продвижения.
        :type language: str
        :param currency: Валюта для продвижения.
        :type currency: str
        :return: Элемент для продвижения (категория или событие).
        :rtype: SimpleNamespace
        """
        if is_event:
            random.shuffle(events)
            return events.pop()
        else:
             return self.get_category_item(campaign_name, group, language, currency)

    def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace:
        """
        Получает категорию для продвижения на основе кампании и промоутера.

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param group: Данные группы.
        :type group: SimpleNamespace
        :param language: Язык для продвижения.
        :type language: str
        :param currency: Валюта для продвижения.
        :type currency: str
        :return: Данные категории для продвижения.
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
                 logger.error(f"Ошибка при загрузке файла {base_path / f'{language}_{currency}.json'}", e)
                 return SimpleNamespace()
            adv_categories = list(vars(adv.category).items())
            random.shuffle(adv_categories)

            for ad_name, ad in adv_categories:
                try:
                     ad.description = read_text_file(base_path / 'category' / ad_name / 'description.txt')
                except Exception as e:
                     logger.error(f"Ошибка при чтении файла {base_path / 'category' / ad_name / 'description.txt'}", e)
                     continue
                if not ad.description:
                     logger.error(f"ошибка чтения файла {base_path / 'category' / ad_name / 'description.txt'}")
                     continue
                item = ad
                item.name = ad_name
                _img = get_filenames(base_path / 'category' / ad_name / 'images')
                if _img:
                     _img = _img if isinstance(_img, str) else _img[0]
                     item.img_path = Path(gs.path.local) / _img
        return item

    def check_interval(self, group: SimpleNamespace) -> bool:
        """
        Проверяет, достаточно ли времени прошло для продвижения этой группы.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: True, если достаточно времени прошло, иначе False.
        :rtype: bool
        """
        # TODO: Реализовать проверку интервала между продвижениями
        ...
        return True

    def validate_group(self, group: SimpleNamespace) -> bool:
        """
        Проверяет, что данные группы корректны.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: True, если данные группы корректны, иначе False.
        :rtype: bool
        """
        return group and hasattr(group, 'group_url') and hasattr(group, 'group_categories')
```