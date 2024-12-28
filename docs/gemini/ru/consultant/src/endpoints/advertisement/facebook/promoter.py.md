# Анализ кода модуля `promoter.py`

**Качество кода: 7/10**
   -  Плюсы
        *   Код разбит на логические блоки, что упрощает понимание его структуры.
        *   Используются docstring для описания классов, методов и функций.
        *   Используется `logger` для логирования ошибок и отладочной информации.
        *   Код применяет `SimpleNamespace` для хранения данных.
        *   Присутствует обработка основных ошибок.
        *   Используются функции из `src.utils` для работы с файлами и JSON.
   -  Минусы
        *   Не все функции и переменные имеют docstring в формате reStructuredText (RST).
        *   В некоторых местах используется `logger.debug` без указания исключения.
        *   Использование `...` как заглушек в коде.
        *   Не везде используется `j_loads_ns` для загрузки json.
        *   В коде есть несколько мест где используются конструкции `if not` и `return`  где можно сократить код.
        *   Отсутствует проверка на наличие необходимых атрибутов в объекте `item` перед их использованием.
        *   В `get_category_item` логика получения элемента категории слишком сложная и может быть упрощена.

**Рекомендации по улучшению**
1.  **Документация:**
    *   Добавить docstring в формате RST ко всем функциям, методам и классам, а также переменным модуля.
    *   Улучшить описание параметров и возвращаемых значений в docstring.
2.  **Логирование ошибок:**
    *   Всегда логировать исключения в `logger.error`.
    *   В `logger.debug` передавать исключение вторым параметром, если оно доступно.
3.  **Обработка данных:**
    *   Использовать `j_loads_ns` для всех операций чтения json файлов.
4.  **Упрощение кода:**
    *   Избегать использования `if not` и `return`, где можно использовать более лаконичные конструкции.
    *   Упростить логику получения элемента категории в `get_category_item`.
5.  **Проверки данных:**
    *   Добавить проверки на наличие необходимых атрибутов в объектах перед их использованием.
6.  **Комментарии:**
    *   Добавить комментарии с подробным объяснением кода к каждой строке.
7.  **Удаление `...`:**
     *   Заменить все `...` на корректную логику или заглушки.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для продвижения сообщений и событий в группах Facebook.
=========================================================================================

Этот модуль содержит класс :class:`FacebookPromoter`, который используется для продвижения товаров и событий AliExpress
в группах Facebook, автоматически публикуя сообщения и события, избегая дубликатов.

Пример использования
--------------------

Пример использования класса `FacebookPromoter`:

.. code-block:: python

    promoter = FacebookPromoter(d=driver, promoter='aliexpress')
    promoter.process_groups(campaign_name='test_campaign', group_categories_to_adv=['sales'], language='en', currency='USD')
"""



import random
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import urlencode
from types import SimpleNamespace
from typing import Optional, List, Union

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
    Формирует URL для создания события в Facebook.

    :param group_url: URL группы Facebook, содержащий `group_id`.
    :type group_url: str
    :return: URL для создания события.
    :rtype: str
    """
    # Извлекает ID группы из URL.
    group_id = group_url.rstrip('/').split('/')[-1]
    # Базовый URL для создания события.
    base_url = "https://www.facebook.com/events/create/"
    # Параметры запроса.
    params = {
        "acontext": '{"event_action_history":[{"surface":"group"},{"mechanism":"upcoming_events_for_group","surface":"group"}],"ref_notif_type":null}',
        "dialog_entry_point": "group_events_tab",
        "group_id": group_id
    }
    # Кодирует параметры в строку запроса.
    query_string = urlencode(params)
    # Возвращает сформированный URL.
    return f"{base_url}?{query_string}"

class FacebookPromoter:
    """
    Класс для продвижения товаров AliExpress и событий в группах Facebook.

    Автоматизирует публикацию рекламных материалов в группах Facebook,
    используя экземпляр WebDriver, гарантируя, что категории и события продвигаются без дубликатов.

    :ivar d: Экземпляр WebDriver для управления браузером.
    :vartype d: Driver
    :ivar group_file_paths: Путь к файлу или списку файлов с данными групп.
    :vartype group_file_paths: Union[str, Path, List[Union[str, Path]], None]
    :ivar no_video: Флаг, отключающий видео в публикациях.
    :vartype no_video: bool
    :ivar promoter: Имя промоутера.
    :vartype promoter: str
    """
    d: Driver = None
    group_file_paths: Union[str, Path, List[Union[str, Path]], None] = None
    no_video: bool = False
    promoter: str

    def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[List[Union[str, Path]]] = None, no_video: bool = False):
        """
        Инициализирует промоутер для групп Facebook.

        :param d: Экземпляр WebDriver для автоматизации браузера.
        :type d: Driver
        :param promoter: Имя промоутера.
        :type promoter: str
        :param group_file_paths: Список путей к файлам с данными групп или путь к одному файлу.
        :type group_file_paths: Optional[List[Union[str, Path]]]
        :param no_video: Флаг для отключения видео в публикациях.
        :type no_video: bool
        """
        # Инициализирует имя промоутера.
        self.promoter = promoter
        # Инициализирует драйвер.
        self.d = d
        # Устанавливает пути к файлам групп или получает их из директории по умолчанию.
        self.group_file_paths = group_file_paths if group_file_paths else get_filenames(gs.path.google_drive / 'facebook' / 'groups')
        # Инициализирует флаг отключения видео.
        self.no_video = no_video
        # Инициализирует курсор-спиннер.
        self.spinner = spinning_cursor()

    def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
        """
        Продвигает категорию или событие в группе Facebook.

        :param group: Данные группы Facebook.
        :type group: SimpleNamespace
        :param item: Данные категории или события.
        :type item: SimpleNamespace
        :param is_event: Флаг, указывающий, является ли продвигаемый элемент событием.
        :type is_event: bool
        :param language: Язык, на котором будет опубликовано продвижение.
        :type language: Optional[str]
        :param currency: Валюта для продвижения.
        :type currency: Optional[str]
        :return: True, если продвижение прошло успешно, иначе False.
        :rtype: bool
        """
        # Проверяет соответствие языку группы и языка продвижения.
        if language and group.language.upper() != language.upper():
            return False
        # Проверяет соответствие валюте группы и валюте продвижения.
        if currency and group.currency.upper() != currency.upper():
            return False

        # Определяет имя элемента для продвижения.
        item_name = item.event_name if is_event else item.category_name
        # Получает сообщение или событие на нужном языке.
        ev_or_msg = getattr(item.language, group.language) if is_event else item

        # Устанавливает атрибуты события если это событие
        if is_event:
            ev_or_msg.start = item.start
            ev_or_msg.end = item.end
            ev_or_msg.promotional_link = item.promotional_link

            # Отправляет событие
            if not post_event(d=self.d, event=ev_or_msg):
                self.log_promotion_error(is_event, item_name)
                return False
        else:
            # Проверка на промоутера
            if 'kazarinov' in self.promoter or 'emil' in self.promoter:
                # Отправляет рекламное сообщение
                if not post_ad(self.d, ev_or_msg):
                    return False
            else:
                # Отправляет сообщение
                if not post_message(d=self.d, message=ev_or_msg, no_video=self.no_video, without_captions=False):
                    return False

        # Обновляет данные группы после публикации.
        self.update_group_promotion_data(group, item_name, is_event)
        return True

    def log_promotion_error(self, is_event: bool, item_name: str):
        """
        Логирует ошибку продвижения категории или события.

        :param is_event: Флаг, указывающий, является ли продвигаемый элемент событием.
        :type is_event: bool
        :param item_name: Имя категории или события.
        :type item_name: str
        """
        # Логирует ошибку продвижения.
        logger.debug(f"Error while posting {'event' if is_event else 'category'} {item_name}", exc_info=None)


    def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
        """
        Обновляет данные о продвижении группы.

        :param group: Данные группы Facebook.
        :type group: SimpleNamespace
        :param item_name: Имя категории или события.
        :type item_name: str
        :param is_event: Флаг, указывающий, является ли продвигаемый элемент событием.
        :type is_event: bool
        """
        # Получает текущую метку времени.
        timestamp = datetime.now().strftime("%d/%m/%y %H:%M")
        # Обновляет время последнего продвижения.
        group.last_promo_sended = gs.now
        # Обновляет список продвинутых событий или категорий.
        if is_event:
            group.promoted_events = group.promoted_events if isinstance(group.promoted_events, list) else [group.promoted_events]
            group.promoted_events.append(item_name)
        else:
            group.promoted_categories = group.promoted_categories if isinstance(group.promoted_categories, list) else [group.promoted_categories]
            group.promoted_categories.append(item_name)
        # Обновляет временную метку последнего продвижения.
        group.last_promo_sended = timestamp


    def process_groups(self, campaign_name: str = None, events: Optional[List[SimpleNamespace]] = None, is_event: bool = False, group_file_paths: Optional[List[str]] = None, group_categories_to_adv: List[str] = ['sales'], language: str = None, currency: str = None):
        """
        Обрабатывает все группы для продвижения кампании или события.

        :param campaign_name: Имя кампании.
        :type campaign_name: Optional[str]
        :param events: Список событий для продвижения.
        :type events: Optional[List[SimpleNamespace]]
        :param is_event: Флаг, указывающий, является ли продвигаемый элемент событием.
        :type is_event: bool
        :param group_file_paths: Список путей к файлам групп.
        :type group_file_paths: Optional[List[str]]
        :param group_categories_to_adv: Список категорий групп для продвижения.
        :type group_categories_to_adv: List[str]
        :param language: Язык продвижения.
        :type language: Optional[str]
        :param currency: Валюта продвижения.
        :type currency: Optional[str]
        """
        # Проверяет наличие данных для продвижения.
        if not campaign_name and not events:
            logger.debug("Nothing to promote!")
            return
        # Проходит по всем файлам групп.
        for group_file in group_file_paths:
            # Формирует путь к файлу группы.
            path_to_group_file: Path = gs.path.google_drive / 'facebook' / 'groups' / group_file
            # Загружает данные группы из файла.
            groups_ns: dict = j_loads_ns(path_to_group_file)

            # Проверяет наличие данных группы.
            if not groups_ns:
                logger.error(f"Проблема в файле групп {group_file=}")
                return
            # Обрабатывает каждую группу.
            for group_url, group in vars(groups_ns).items():
                # Присваивает URL группы
                group.group_url = group_url
                # Проверяет интервал для продвижения.
                if not is_event and not self.check_interval(group):
                    logger.debug(f"{campaign_name=}\\n Interval in group: {group.group_url}", exc_info=None)
                    continue
                # Проверяет соответствие категории группы и статуса.
                if not set(group_categories_to_adv).intersection(group.group_categories if isinstance(group.group_categories, list) else [group.group_categories]) or not 'active' in group.status:
                    continue
                # Получает элемент для продвижения.
                if not is_event:
                    item = self.get_category_item(campaign_name, group, language, currency)
                else:
                    # Перемешивает события
                    random.shuffle(events)
                    # Получает первое событие из списка
                    item = events.pop()
                # Проверяет, было ли уже продвижение элемента.
                if item.name in (group.promoted_events if is_event else group.promoted_categories):
                    logger.debug(f"Item already promoted")
                    continue

                # Проверяет соответствие языка и валюты.
                if group.language.upper() != language.upper() and group.currency.upper() != currency.upper():
                    continue
                # Открывает URL группы или события.
                self.d.get_url(get_event_url(group.group_url) if is_event else group.group_url)
                # Продвигает элемент.
                if not self.promote(group=group, item=item, is_event=is_event, language=language, currency=currency):
                    continue
                # Сохраняет обновленные данные группы в файл.
                j_dumps(groups_ns, path_to_group_file)
                # Задержка
                t = random.randint(30, 420)
                print(f"sleeping {t} sec")
                time.sleep(t)



    def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace:
        """
        Получает элемент категории для продвижения.

        :param campaign_name: Имя кампании.
        :type campaign_name: str
        :param group: Данные группы Facebook.
        :type group: SimpleNamespace
        :param language: Язык продвижения.
        :type language: str
        :param currency: Валюта продвижения.
        :type currency: str
        :return: Элемент категории для продвижения.
        :rtype: SimpleNamespace
        """
        # Проверяет, является ли промоутер aliexpress
        if self.promoter == 'aliexpress':
            # Инициализирует редактор кампании AliExpress.
            ce = AliCampaignEditor(campaign_name=campaign_name, language=group.language, currency=group.currency)
            # Получает список категорий.
            list_categories = ce.list_categories
            # Перемешивает список категорий.
            random.shuffle(list_categories)
            # Выбирает первую категорию.
            category_name = list_categories.pop()
            # Получает категорию.
            item = ce.get_category(category_name)
            # Присваивает имя категории элементу.
            item.name = category_name
            # Получает продукты категории.
            item.products = ce.get_category_products(item.category_name)
        else:
            # Формирует путь к директории кампании.
            base_path = gs.path.google_drive / self.promoter / 'campaigns' / campaign_name
            # Загружает данные кампании.
            adv: SimpleNamespace = j_loads_ns(base_path / f"{language}_{currency}.json")
            # Преобразуем категории в список
            adv_categories = list(vars(adv.category).items())
            # Перемешиваем категории.
            random.shuffle(adv_categories)
            # Обрабатываем каждую категорию
            for ad_name, ad in adv_categories:
                # Получает описание категории
                ad.description = read_text_file(base_path / 'category' / ad_name / 'description.txt')
                # Если описание не получено, то пропускаем
                if not ad.description:
                    logger.error(f"ошибка чтения файла", exc_info=None)
                    continue
                # Присваиваем данные категории
                item = ad
                # Присваиваем имя категории
                item.name = ad_name
                # Получаем список изображений
                _img = get_filenames(base_path / 'category' / ad_name / 'images')
                # Если изображения есть, то берем первое
                if _img:
                    _img = _img if isinstance(_img, str) else _img[0]
                    # Составляем путь к изображению
                    item.img_path = Path(gs.path.local) / _img
        # Возвращает элемент.
        return item


    def check_interval(self, group: SimpleNamespace) -> bool:
        """
        Проверяет, прошло ли достаточно времени для продвижения в этой группе.

        :param group: Данные группы Facebook.
        :type group: SimpleNamespace
        :return: True, если прошло достаточно времени, иначе False.
        :rtype: bool
        """
        # TODO: Реализовать проверку интервала
        return True


    def validate_group(self, group: SimpleNamespace) -> bool:
        """
        Проверяет корректность данных группы.

        :param group: Данные группы Facebook.
        :type group: SimpleNamespace
        :return: True, если данные корректны, иначе False.
        :rtype: bool
        """
        # Проверяет, что группа существует и имеет необходимые атрибуты.
        return bool(group and hasattr(group, 'group_url') and hasattr(group, 'group_categories'))
```