# Анализ кода модуля `promoter`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разбит на логические блоки.
    - Присутствует подробная документация в формате Markdown.
    - Используется `SimpleNamespace` для хранения данных, что упрощает доступ к атрибутам.
    - Логика работы модуля понятна из предоставленного описания.
    - Код написан в соответствии с PEP8.
-  Минусы
    - Отсутствуют импорты необходимых модулей в коде.
    - Не используется `j_loads_ns` из `src.utils.jjson` для чтения файлов.
    - Отсутствуют docstring в коде, комментарии не соответсвуют `reStructuredText`.
    - Используется обычный `try-except` без логирования ошибок.
    - Не проводится форматирование даты, времени.
    - Не используются константы в коде.

**Рекомендации по улучшению**

1.  **Добавить недостающие импорты:** Добавить необходимые импорты в начало файла (`src.utils.jjson`, `src.logger.logger`, `os`, `json`, `typing`, `datetime`, `pathlib`, `random`, `urllib.parse`).
2.  **Использовать `j_loads_ns`:** Заменить стандартный `json.load` на `j_loads_ns` для загрузки JSON-файлов.
3.  **Рефакторинг docstring:** Добавить docstring в формате RST ко всем функциям, методам и классам.
4.  **Логирование ошибок:** Использовать `logger.error` для логирования ошибок вместо стандартного `try-except`.
5.  **Форматирование даты/времени:** Реализовать форматирование даты и времени для отслеживания интервалов между публикациями.
6.  **Константы:** Использовать константы для магических значений (`sales` и т.д.).
7.  **Улучшить читаемость:** Добавить пустые строки для лучшего разделения блоков кода.

**Оптимизированный код**

```python
"""
Модуль для автоматизации продвижения товаров и событий AliExpress в Facebook группах.
=========================================================================================

Этот модуль предоставляет класс :class:`FacebookPromoter`, который автоматизирует размещение рекламных постов в группах Facebook,
избегая дублирования и обеспечивая эффективное продвижение категорий и событий.

Пример использования
--------------------

Пример использования класса `FacebookPromoter`:

.. code-block:: python

    from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
    from src.webdriver.driver import Driver
    from src.utils.jjson import j_loads_ns

    # Инициализация WebDriver
    d = Driver()

    # Создание экземпляра FacebookPromoter
    promoter = FacebookPromoter(
        d=d,
        promoter="aliexpress",
        group_file_paths=["path/to/group/file1.json", "path/to/group/file2.json"]
    )

    # Запуск процесса продвижения
    promoter.process_groups(
        campaign_name="Campaign1",
        events=[],
        group_categories_to_adv=["sales"],
        language="en",
        currency="USD"
    )
"""
import os
import json
import random
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, List, Union, Any
from urllib.parse import urlparse
from types import SimpleNamespace

from src.utils.jjson import j_loads_ns
from src.logger.logger import logger
from src.webdriver.driver import Driver  # Предполагается, что импорт Driver существует

# Константы для категорий по умолчанию
DEFAULT_CATEGORIES = ["sales"]
# Константа для интервала между постами (в минутах)
DEFAULT_INTERVAL = 10


class FacebookPromoter:
    """
    Класс для управления процессом продвижения товаров и событий AliExpress в Facebook группах.
    """

    def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[Union[List[Union[str, Path]], str, Path]] = None,
                 no_video: bool = False):
        """
        Инициализирует промоутер Facebook с необходимыми конфигурациями.

        :param d: Экземпляр WebDriver для автоматизации.
        :type d: Driver
        :param promoter: Название промоутера (например, "aliexpress").
        :type promoter: str
        :param group_file_paths: Пути к файлам с данными групп.
        :type group_file_paths: Optional[Union[List[Union[str, Path]], str, Path]]
        :param no_video: Флаг для отключения видео в постах.
        :type no_video: bool
        """
        self.driver = d
        self.promoter = promoter
        self.group_file_paths = group_file_paths if group_file_paths else []
        if isinstance(self.group_file_paths, (str, Path)):
            self.group_file_paths = [self.group_file_paths]
        self.no_video = no_video
        self.group_data = {}

    def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None,
                currency: str = None) -> bool:
        """
        Выполняет продвижение категории или события в указанной группе Facebook.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :param item: Данные категории или события для продвижения.
        :type item: SimpleNamespace
        :param is_event: Флаг, указывающий, является ли продвигаемый объект событием.
        :type is_event: bool
        :param language: Язык продвижения.
        :type language: Optional[str]
        :param currency: Валюта для продвижения.
        :type currency: Optional[str]
        :return: `True`, если продвижение выполнено успешно, `False` в противном случае.
        :rtype: bool
        """
        try:
            # Код выполняет проверку наличия необходимых атрибутов для продвижения
            if not all([getattr(item, 'url', None), getattr(group, 'group_url', None)]):
                logger.error(f"Недостаточно атрибутов для продвижения: {item=}, {group=}")
                self.log_promotion_error(is_event, getattr(item, 'name', "Unknown item"))
                return False

            # Код подготавливает URL для публикации
            url = item.url
            if not urlparse(url).scheme:
                url = f'https://{url}'

            # Код выполняет публикацию
            if is_event:
                logger.info(f"Продвижение события: {item.name} в группе: {group.group_url}")
            else:
                logger.info(f"Продвижение категории: {item.name} в группе: {group.group_url}")

            # TODO: Здесь должна быть логика публикации в Facebook
            ...
            self.update_group_promotion_data(group, item.name, is_event)
            return True
        except Exception as ex:
            # Логирование ошибки продвижения
            logger.error(f"Ошибка продвижения {item.name} в группе {group.group_url}", exc_info=ex)
            self.log_promotion_error(is_event, getattr(item, 'name', 'Unknown item'))
            return False

    def log_promotion_error(self, is_event: bool, item_name: str):
        """
        Логирует ошибку при неудачном продвижении.

        :param is_event: Флаг, указывающий, является ли продвигаемый объект событием.
        :type is_event: bool
        :param item_name: Название объекта.
        :type item_name: str
        """
        if is_event:
            logger.error(f"Ошибка продвижения события: {item_name}")
        else:
            logger.error(f"Ошибка продвижения категории: {item_name}")

    def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
        """
        Обновляет данные группы после успешного продвижения.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :param item_name: Название объекта, который был продвинут.
        :type item_name: str
        :param is_event: Флаг, указывающий, является ли продвигаемый объект событием.
        :type is_event: bool
        """
        if not hasattr(group, 'promoted_categories') or not group.promoted_categories:
            group.promoted_categories = {}

        if not hasattr(group, 'promoted_events') or not group.promoted_events:
            group.promoted_events = {}

        current_time = datetime.now().isoformat()

        if is_event:
            if item_name not in group.promoted_events:
                group.promoted_events[item_name] = current_time
        else:
            if item_name not in group.promoted_categories:
                 group.promoted_categories[item_name] = current_time
        # TODO:  Нужно определить сохранение данных в файл или иной ресурс
        ...

    def process_groups(self, campaign_name: str = None, events: Optional[List[SimpleNamespace]] = None,
                       is_event: bool = False, group_file_paths: Optional[List[str]] = None,
                       group_categories_to_adv: Optional[List[str]] = None, language: str = None,
                       currency: str = None):
        """
        Выполняет обработку групп для текущей кампании или продвижения события.

        :param campaign_name: Название кампании.
        :type campaign_name: Optional[str]
        :param events: Список событий для продвижения.
        :type events: Optional[List[SimpleNamespace]]
        :param is_event: Флаг, указывающий на продвижение событий.
        :type is_event: bool
        :param group_file_paths: Список путей к файлам с данными групп.
        :type group_file_paths: Optional[List[str]]
        :param group_categories_to_adv: Список категорий для продвижения.
        :type group_categories_to_adv: Optional[List[str]]
        :param language: Язык продвижения.
        :type language: Optional[str]
        :param currency: Валюта для продвижения.
        :type currency: Optional[str]
        """
        if not group_file_paths:
            group_file_paths = self.group_file_paths
        if not group_categories_to_adv:
            group_categories_to_adv = DEFAULT_CATEGORIES
        if not group_file_paths:
            logger.error("Не указаны пути к файлам групп")
            return

        for file_path in group_file_paths:
            try:
                # Загрузка данных о группах из файла
                if not os.path.exists(file_path):
                    logger.error(f"Файл не существует {file_path}")
                    continue

                groups = j_loads_ns(file_path)
                if not isinstance(groups, list):
                    logger.error(f"Ожидается список групп в файле {file_path}")
                    continue

                for group in groups:
                    if not self.validate_group(group):
                        logger.error(f"Неверные данные группы: {group}")
                        continue

                    if not self.check_interval(group):
                       continue

                    if is_event:
                        if not events:
                           logger.warning("Нет событий для продвижения")
                           continue
                        for event in events:
                           self.promote(group, event, is_event, language, currency)
                    else:
                        for category in group_categories_to_adv:
                            item = self.get_category_item(campaign_name, group, language, currency)
                            if not item:
                                continue
                            self.promote(group, item, is_event, language, currency)

            except Exception as ex:
                # Логирование ошибки обработки файла группы
                logger.error(f"Ошибка обработки файла: {file_path}", exc_info=ex)

    def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str,
                          currency: str) -> Optional[SimpleNamespace]:
        """
        Получает элемент категории для продвижения на основе кампании и промоутера.

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param group: Данные группы.
        :type group: SimpleNamespace
        :param language: Язык для продвижения.
        :type language: str
        :param currency: Валюта для продвижения.
        :type currency: str
        :return: Элемент категории для продвижения или None, если не найден.
        :rtype: Optional[SimpleNamespace]
        """
        try:
            # Код получает элемент категории
            # TODO: Добавить логику получения элемента категории.
            # Этот пример просто возвращает заглушку
            items = [
                 SimpleNamespace(name=f'item_{random.randint(1,100)}',url='https://example.com/product', category='sales'),
                 SimpleNamespace(name=f'item_{random.randint(101,200)}',url='https://example.com/product2', category='sales'),
            ]
            item =  random.choice(items)
            if not hasattr(item, 'name'):
               logger.error(f"Не найден атрибут name в item={item}")
               return None
            if not hasattr(item, 'category'):
               logger.error(f"Не найден атрибут category в item={item}")
               return None
            if item.category not in group.get('categories', []):
               logger.warning(f"Категория {item.category} не найдена в разрешенных категориях группы {group.get('categories', [])}")
               return None
            logger.debug(f"Получен элемент для продвижения: {item.name}")
            return item
        except Exception as ex:
             logger.error(f"Ошибка при получении элемента категории", exc_info=ex)
             return None

    def check_interval(self, group: SimpleNamespace) -> bool:
        """
        Проверяет, достаточно ли времени прошло для повторного продвижения в этой группе.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: `True`, если группа может быть продвинута, `False` в противном случае.
        :rtype: bool
        """
        if not hasattr(group, 'last_promotion_time') or not group.last_promotion_time:
            return True
        try:
             last_promotion_time = datetime.fromisoformat(group.last_promotion_time)
             time_diff = datetime.now() - last_promotion_time
             if time_diff >= timedelta(minutes=DEFAULT_INTERVAL):
                 return True
             else:
                  logger.debug(f"Группа {group.group_url} еще не готова к продвижению (осталось {timedelta(minutes=DEFAULT_INTERVAL)-time_diff})")
                  return False
        except Exception as ex:
             logger.error(f"Ошибка при проверке интервала {group.group_url}", exc_info=ex)
             return False

    def validate_group(self, group: SimpleNamespace) -> bool:
        """
        Проверяет, являются ли данные группы валидными.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: `True`, если данные группы валидны, `False` в противном случае.
        :rtype: bool
        """
        if not all([hasattr(group, 'group_url'), hasattr(group, 'categories')]):
           logger.error(f"Неверные данные группы: {group}")
           return False
        return True
```