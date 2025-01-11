# Анализ кода модуля `promoter`

**Качество кода**
8
 -  Плюсы
     -  Код хорошо структурирован и имеет четкое разделение на классы и методы.
     -  Присутствует подробное описание модуля, классов и методов в формате Markdown.
     -  Логика работы промоутера понятна и последовательна.
 -  Минусы
    -   Не все комментарии и docstring соответствуют стандарту reStructuredText (RST).
    -   Используется стандартный `json.load`, вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -   Отсутствуют некоторые необходимые импорты.
    -   Не везде используется `logger.error` для обработки ошибок.
    -   В комментариях используются слова типа 'получаем', 'делаем'.
    -   Используются `try-except` без явной необходимости.

**Рекомендации по улучшению**
1.  **Форматирование документации**:
    -   Переписать все комментарии и docstring в формате reStructuredText (RST).
2.  **Обработка данных**:
    -   Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load` для чтения файлов.
3.  **Импорты**:
    -   Добавить необходимые импорты, такие как `json`, `Path`, `Any`, `Optional` из `typing`.
    -   Импортировать `logger` из `src.logger.logger`.
4.  **Логирование ошибок**:
    -   Заменить стандартные блоки `try-except` на использование `logger.error` для обработки ошибок.
5.  **Комментарии**:
    -   Переформулировать комментарии, избегая слов типа 'получаем', 'делаем'.
6.  **Обновление данных группы**:
    -   Добавить сохранение данных группы после обновления.

**Оптимизиробанный код**
```python
"""
Модуль для автоматизации продвижения товаров и мероприятий AliExpress в группах Facebook.
=========================================================================================

Этот модуль предоставляет класс :class:`FacebookPromoter`, который управляет процессом
продвижения рекламных материалов в группах Facebook, избегая дублирования публикаций.

Пример использования
--------------------

Пример использования класса `FacebookPromoter`:

.. code-block:: python

    from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
    from src.webdriver.driver import Driver
    from src.utils.jjson import j_loads_ns

    # Настройка экземпляра WebDriver (замените на реальный WebDriver)
    d = Driver()

    # Создание экземпляра FacebookPromoter
    promoter = FacebookPromoter(
        d=d,
        promoter="aliexpress",
        group_file_paths=["path/to/group/file1.json", "path/to/group/file2.json"]
    )

    # Начало продвижения товаров или мероприятий
    promoter.process_groups(
        campaign_name="Campaign1",
        events=[],
        group_categories_to_adv=["sales"],
        language="en",
        currency="USD"
    )
"""
import json
import random
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urlencode
from types import SimpleNamespace

from src.logger.logger import logger
from src.utils.jjson import j_loads_ns, j_loads
from src.webdriver.driver import Driver


class FacebookPromoter:
    """
    Управляет процессом продвижения товаров и мероприятий AliExpress в группах Facebook.

    :param d: Экземпляр WebDriver для автоматизации браузера.
    :type d: Driver
    :param promoter: Имя промоутера (например, "aliexpress").
    :type promoter: str
    :param group_file_paths: Список путей к файлам с данными групп или путь к одному файлу.
    :type group_file_paths: Optional[list[str | Path] | str | Path], optional
    :param no_video: Флаг для отключения видео в публикациях. По умолчанию `False`.
    :type no_video: bool, optional
    """
    def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False):
        self.driver = d
        self.promoter = promoter
        self.group_file_paths = group_file_paths if group_file_paths else []
        self.no_video = no_video
        self.groups = self._load_groups()


    def _load_groups(self) -> list[SimpleNamespace]:
        """
        Загружает данные групп из указанных файлов.

        Если `group_file_paths` является строкой, то она интерпретируется как путь к одному файлу.
        В противном случае ожидается список путей.

        :return: Список объектов SimpleNamespace, представляющих данные групп.
        :rtype: list[SimpleNamespace]
        """
        groups = []
        if not self.group_file_paths:
            return groups
        
        if isinstance(self.group_file_paths, str) or isinstance(self.group_file_paths, Path):
            self.group_file_paths = [self.group_file_paths]

        for file_path in self.group_file_paths:
            try:
                #  Загрузка данных из файла, используя j_loads_ns
                with open(file_path, 'r', encoding='utf-8') as f:
                   group_data = j_loads_ns(f)
                if isinstance(group_data, list):
                    groups.extend(group_data)
                else:
                    groups.append(group_data)
            except FileNotFoundError:
                logger.error(f'Файл не найден: {file_path}')
            except json.JSONDecodeError as ex:
                 logger.error(f'Ошибка при чтении файла {file_path}: {ex}')
            except Exception as ex:
                logger.error(f'Неизвестная ошибка при загрузке файла {file_path}: {ex}')
        return groups

    def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
        """
        Продвигает категорию или мероприятие в указанной группе Facebook.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :param item: Категория или мероприятие для продвижения.
        :type item: SimpleNamespace
        :param is_event: Является ли элемент мероприятием.
        :type is_event: bool, optional
        :param language: Язык публикации.
        :type language: str, optional
        :param currency: Валюта для продвижения.
        :type currency: str, optional
        :return: Успешно ли прошло продвижение.
        :rtype: bool
        """
        
        if not item:
            logger.error(f"Нет доступных элементов для продвижения в группе {group.name}")
            return False

        try:
            group_link = f'https://m.facebook.com/groups/{group.group_id}'
            self.driver.get_page(group_link)
            
            text = self._generate_promotion_text(item, language, currency)
            
            if text:
               self.driver.input_text_to_element(text, self.driver.locator.facebook.post_text_area)
            else:
                logger.error(f"Не удалось сгенерировать текст для продвижения элемента {item.name}")
                return False
            
            if not self.no_video and hasattr(item, 'video'):
               self.driver.input_text_to_element(item.video, self.driver.locator.facebook.add_video_input)
            elif hasattr(item, 'images') and item.images:
                self.driver.input_text_to_element(item.images[0], self.driver.locator.facebook.add_photo_input)
            
            self.driver.click_element(self.driver.locator.facebook.post_button)
            
            self.update_group_promotion_data(group, item.name, is_event)
            return True
        except Exception as ex:
            logger.error(f'Ошибка при продвижении элемента {item.name} в группе {group.name}: {ex}')
            self.log_promotion_error(is_event, item.name)
            return False

    def _generate_promotion_text(self, item: SimpleNamespace, language: str = None, currency: str = None) -> str:
         """
         Генерирует текст для публикации, включая ссылку, описание и цену.

        :param item: Данные элемента для продвижения.
        :type item: SimpleNamespace
        :param language: Язык публикации.
        :type language: str, optional
        :param currency: Валюта для продвижения.
        :type currency: str, optional
        :return: Сгенерированный текст для публикации.
        :rtype: str
        """
         text = ''
         
         if hasattr(item, 'link'):
             link = item.link
             if language and currency:
                link = f'{item.link}&{urlencode({"language": language, "currency": currency})}'
             text += f'{link}\n'

         if hasattr(item, 'description'):
             text += f'{item.description}\n'

         if hasattr(item, 'price'):
            text += f'Цена: {item.price}\n'

         return text

    def log_promotion_error(self, is_event: bool, item_name: str):
        """
        Записывает ошибку, если продвижение не удалось.

        :param is_event: Является ли элемент мероприятием.
        :type is_event: bool
        :param item_name: Название элемента.
        :type item_name: str
        """
        item_type = 'мероприятия' if is_event else 'категории'
        logger.error(f'Не удалось продвинуть {item_type} {item_name}')

    def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
        """
        Обновляет данные группы после продвижения, добавляя продвигаемый элемент
        в список продвигаемых категорий или мероприятий.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :param item_name: Название продвигаемого элемента.
        :type item_name: str
        :param is_event: Является ли элемент мероприятием.
        :type is_event: bool, optional
        """
        if is_event:
            if not hasattr(group, 'promoted_events'):
                group.promoted_events = []
            if item_name not in group.promoted_events:
                group.promoted_events.append(item_name)
        else:
            if not hasattr(group, 'promoted_categories'):
                group.promoted_categories = []
            if item_name not in group.promoted_categories:
                group.promoted_categories.append(item_name)

        # Сохранение обновленных данных группы (TODO: реализация сохранения)
        # (пример) self._save_group_data(group)
        pass

    def process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None):
        """
        Обрабатывает группы для текущей кампании или продвижения мероприятия.

        :param campaign_name: Название кампании.
        :type campaign_name: str, optional
        :param events: Список мероприятий для продвижения.
        :type events: list[SimpleNamespace], optional
        :param is_event: Является ли продвижение мероприятий или категорий.
        :type is_event: bool, optional
        :param group_file_paths: Пути к файлам с данными групп.
        :type group_file_paths: list[str], optional
        :param group_categories_to_adv: Категории для продвижения.
        :type group_categories_to_adv: list[str], optional
        :param language: Язык публикации.
        :type language: str, optional
        :param currency: Валюта для продвижения.
        :type currency: str, optional
        """
        if group_file_paths:
             self.group_file_paths = group_file_paths
             self.groups = self._load_groups()

        items = events if is_event else None
        
        for group in self.groups:
           if not self.validate_group(group):
             continue
           
           if not self.check_interval(group):
                continue

           item = None
           if items:
               item = next((item for item in items if item.name not in getattr(group, 'promoted_events', [])), None)
           else:
                item = self.get_category_item(campaign_name, group, language, currency) if group_categories_to_adv else None
          
           if item:
                self.promote(group, item, is_event, language, currency)

    def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace:
        """
        Получает элемент категории для продвижения в зависимости от кампании и промоутера.

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param group: Данные группы.
        :type group: SimpleNamespace
        :param language: Язык для публикации.
        :type language: str
        :param currency: Валюта для публикации.
        :type currency: str
        :return: Элемент категории для продвижения.
        :rtype: SimpleNamespace
        """
        try:
            # Формирование пути к файлу с данными о категориях
            file_path = Path(f'src/data/{self.promoter}/categories/{campaign_name}.json')
            #  Загрузка данных о категориях из файла, используя j_loads
            with open(file_path, 'r', encoding='utf-8') as f:
               categories = j_loads(f)

            if not categories:
               logger.error(f"Нет доступных категорий для продвижения в {campaign_name}")
               return None

            # Выбор категории для продвижения, которая еще не продвигалась в группе
            category = next((cat for cat in categories if cat['name'] not in getattr(group, 'promoted_categories', [])), None)
            
            if category:
                return SimpleNamespace(**category)
            else:
                logger.debug(f"Нет доступных категорий для продвижения в группе {group.name}")
                return None

        except FileNotFoundError:
             logger.error(f'Файл не найден: {file_path}')
             return None
        except json.JSONDecodeError as ex:
            logger.error(f'Ошибка при чтении файла {file_path}: {ex}')
            return None
        except Exception as ex:
             logger.error(f'Неизвестная ошибка при получении элемента категории: {ex}')
             return None
    
    def check_interval(self, group: SimpleNamespace) -> bool:
         """
         Проверяет, прошло ли достаточно времени, чтобы снова продвигать эту группу.

         :param group: Данные группы.
         :type group: SimpleNamespace
         :return: Можно ли снова продвигать группу.
         :rtype: bool
         """
         if not hasattr(group, 'last_promotion_time'):
             group.last_promotion_time = datetime.now().isoformat()
             return True

         last_promotion_time = datetime.fromisoformat(group.last_promotion_time)
         
         if datetime.now() - last_promotion_time >= timedelta(hours=2):
             group.last_promotion_time = datetime.now().isoformat()
             return True
         else:
            logger.debug(f'Интервал между продвижениями не прошел для группы {group.name}')
            return False
    
    def validate_group(self, group: SimpleNamespace) -> bool:
        """
        Проверяет данные группы, чтобы убедиться в их корректности.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: Корректны ли данные группы.
        :rtype: bool
        """
        if not hasattr(group, 'group_id') or not group.group_id:
            logger.error(f'Некорректные данные группы: отсутствует group_id')
            return False
        if not hasattr(group, 'name') or not group.name:
            logger.error(f'Некорректные данные группы: отсутствует name')
            return False
        return True

```