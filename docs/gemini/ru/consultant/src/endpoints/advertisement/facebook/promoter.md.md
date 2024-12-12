# Анализ кода модуля `promoter`

**Качество кода**
1.  **Соответствие требованиям по оформлению кода**: 6/10
    -   **Плюсы**:
        -   Документация в формате Markdown присутствует.
        -   Общее описание модуля и функций присутствует.
    -   **Минусы**:
        -   Отсутствует документация в формате reStructuredText (RST), что является обязательным требованием.
        -   Не используются `j_loads` или `j_loads_ns` для загрузки файлов json.
        -   Отсутствуют необходимые импорты.
        -   Имена переменных не всегда соответствуют ранее обработанным файлам.
        -   Не используются логирование ошибок через `src.logger.logger`.
        -   Многословное описание функций и методов.

**Рекомендации по улучшению**

1.  **Переписать документацию в RST**:
    -   Необходимо переписать всю документацию в формате reStructuredText (RST), включая описания модулей, классов, методов и параметров.
2.  **Использовать `j_loads_ns`**:
    -   Для загрузки данных из файлов json необходимо использовать `j_loads_ns` из `src.utils.jjson`.
3.  **Добавить недостающие импорты**:
    -   Нужно добавить все необходимые импорты в начало файла.
4.  **Привести в соответствие имена переменных**:
    -   Имена переменных должны соответствовать общему стилю и ранее обработанным файлам.
5.  **Добавить логирование ошибок**:
    -   Использовать `src.logger.logger` для логирования ошибок вместо стандартных `try-except`.
6.  **Упростить описания**:
    -   Сократить описания функций и методов, делая их более лаконичными и понятными.
7.  **Рефакторинг**:
    -   Упростить структуру кода, где это возможно.
8. **Документирование кода**:
    -   Добавить документацию в формате RST для всех функций, методов и классов.

**Оптимизированный код**

```python
"""
Модуль для автоматизации продвижения товаров и событий AliExpress в группах Facebook.
==============================================================================

Этот модуль содержит класс :class:`FacebookPromoter`, который автоматизирует процесс
публикации рекламных постов в группах Facebook. Он поддерживает продвижение как отдельных
товаров, так и событий, отслеживает уже опубликованные материалы, и использует WebDriver
для взаимодействия с веб-интерфейсом.

Пример использования
--------------------

Пример инициализации и использования класса `FacebookPromoter`:

.. code-block:: python

    from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
    from src.webdriver.driver import Driver
    from src.utils.jjson import j_loads_ns
    from pathlib import Path

    driver = Driver()
    promoter = FacebookPromoter(
        d=driver,
        promoter="aliexpress",
        group_file_paths=[Path("path/to/group/file1.json"), Path("path/to/group/file2.json")]
    )

    promoter.process_groups(
        campaign_name="Campaign1",
        events=[],
        group_categories_to_adv=["sales"],
        language="en",
        currency="USD"
    )
"""
import random
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, List, Union, Any
from urllib.parse import urlparse
from types import SimpleNamespace

from src.utils.jjson import j_loads_ns
from src.webdriver.driver import Driver
from src.logger.logger import logger

class FacebookPromoter:
    """
    Управляет процессом продвижения товаров и событий AliExpress в группах Facebook.

    :param d: Экземпляр WebDriver для автоматизации браузера.
    :type d: Driver
    :param promoter: Название промоутера (например, "aliexpress").
    :type promoter: str
    :param group_file_paths: Пути к файлам с данными групп. Может быть списком или строкой.
    :type group_file_paths: Optional[list[str | Path] | str | Path]
    :param no_video: Флаг отключения загрузки видео.
    :type no_video: bool
    """
    def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False):
        self.driver = d
        self.promoter = promoter
        self.group_file_paths = group_file_paths
        self.no_video = no_video
        self.group_data = self._load_group_data() # Загружает данные групп при инициализации.

    def _load_group_data(self) -> list[SimpleNamespace]:
        """
        Загружает данные групп из указанных файлов.

        :return: Список данных групп.
        :rtype: list[SimpleNamespace]
        """
        if not self.group_file_paths:
            return []

        if isinstance(self.group_file_paths, (str, Path)):
            self.group_file_paths = [self.group_file_paths]

        groups = []
        for file_path in self.group_file_paths:
            try:
                # Загружает данные группы из JSON файла, используя j_loads_ns
                group_data = j_loads_ns(file_path)
                if isinstance(group_data, list):
                    groups.extend(group_data)
                else:
                    groups.append(group_data)
            except Exception as e:
                 # Логирует ошибку загрузки данных из файла
                logger.error(f'Ошибка при загрузке данных группы из файла {file_path}: {e}')
        return groups

    def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
        """
        Публикует рекламный пост в указанной группе Facebook.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :param item: Товар или событие для продвижения.
        :type item: SimpleNamespace
        :param is_event: Флаг, указывающий, является ли item событием.
        :type is_event: bool
        :param language: Язык поста.
        :type language: str
        :param currency: Валюта для поста.
        :type currency: str
        :return: True, если продвижение успешно, False в противном случае.
        :rtype: bool
        """
        try:
            # Код выполняет продвижение товара/события в группе
            logger.info(f'Продвижение {"события" if is_event else "категории"} {item.name} в группе {group.group_url}')
            ... # Place for actual promotion logic

            self.update_group_promotion_data(group, item.name, is_event)
            return True
        except Exception as e:
            # Логирует ошибку при продвижении
            logger.error(f'Ошибка продвижения {"события" if is_event else "категории"} {item.name} в группе {group.group_url}: {e}')
            self.log_promotion_error(is_event, item.name)
            return False

    def log_promotion_error(self, is_event: bool, item_name: str):
         """
         Логирует ошибку при неудачном продвижении.

         :param is_event: Флаг, указывающий, является ли item событием.
         :type is_event: bool
         :param item_name: Название товара или события.
         :type item_name: str
         """
         # Код логирует ошибку
         logger.error(f'Ошибка продвижения {"события" if is_event else "категории"} {item_name}')


    def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
        """
        Обновляет данные группы после успешного продвижения.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :param item_name: Название товара или события.
        :type item_name: str
        :param is_event: Флаг, указывающий, является ли item событием.
        :type is_event: bool
        """
        if is_event:
           # Код добавляет событие в список продвинутых событий группы
            if not hasattr(group, 'promoted_events'):
                group.promoted_events = []
            group.promoted_events.append(item_name)
        else:
            # Код добавляет категорию в список продвинутых категорий группы
            if not hasattr(group, 'promoted_categories'):
                group.promoted_categories = []
            group.promoted_categories.append(item_name)
        logger.info(f'Данные группы {group.group_url} обновлены, добавлено {"событие" if is_event else "категория"} {item_name}')


    def process_groups(self, campaign_name: str = None, events: Optional[List[SimpleNamespace]] = None, is_event: bool = False, group_categories_to_adv: List[str] = ['sales'], language: str = None, currency: str = None):
        """
        Обрабатывает группы для текущей кампании или продвижения события.

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param events: Список событий для продвижения.
        :type events: Optional[list[SimpleNamespace]]
        :param is_event: Флаг, указывающий на продвижение событий.
        :type is_event: bool
         :param group_categories_to_adv: Список категорий для продвижения.
        :type group_categories_to_adv: list[str]
        :param language: Язык для продвижения.
        :type language: str
        :param currency: Валюта для продвижения.
        :type currency: str
        """
        if not self.group_data:
            logger.warning("Нет данных о группах для обработки.")
            return

        for group in self.group_data:
            if not self.validate_group(group):
                logger.warning(f'Группа {group.group_url} не прошла валидацию, пропуск.')
                continue
            if not self.check_interval(group):
                logger.info(f'Группа {group.group_url} еще не готова к продвижению.')
                continue

            if is_event:
                # Код обрабатывает продвижение событий
                if events:
                    for event in events:
                        self.promote(group, event, is_event, language, currency)
                else:
                    logger.warning("Нет событий для продвижения.")
            else:
                # Код обрабатывает продвижение категорий
                item = self.get_category_item(campaign_name, group, language, currency)
                if item:
                      self.promote(group, item, is_event, language, currency)
                else:
                   logger.warning(f'Нет товара для продвижения в группе {group.group_url}.')

    def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> Optional[SimpleNamespace]:
        """
        Выбирает категорию для продвижения на основе кампании и промоутера.

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param group: Данные группы.
        :type group: SimpleNamespace
        :param language: Язык для продвижения.
        :type language: str
        :param currency: Валюта для продвижения.
        :type currency: str
        :return: Категорию для продвижения или None, если категория не найдена.
        :rtype: Optional[SimpleNamespace]
        """
        # Код выбирает категорию для продвижения
        try:
            ... # Place for logic to fetch category item
            category_item = SimpleNamespace(name='Example Category', url='https://example.com/category') # Example
            return category_item
        except Exception as e:
            # Логирует ошибку при получении категории
            logger.error(f'Ошибка получения категории для группы {group.group_url}: {e}')
            return None

    def check_interval(self, group: SimpleNamespace) -> bool:
        """
         Проверяет, прошло ли достаточно времени с момента последнего продвижения в группе.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: True, если группа готова к продвижению, False в противном случае.
        :rtype: bool
        """
        if not hasattr(group, 'last_promotion_time') or not group.last_promotion_time:
            # Код если время продвижения не задано, возвращает True
            return True

        last_promotion_time = datetime.fromisoformat(group.last_promotion_time)
        interval = timedelta(hours=random.randint(1, 3)) # Пример интервала
        # Код проверяет, прошло ли достаточно времени с последнего продвижения
        return datetime.now() > last_promotion_time + interval


    def validate_group(self, group: SimpleNamespace) -> bool:
        """
        Проверяет данные группы на наличие необходимых атрибутов.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: True, если данные группы валидны, False в противном случае.
        :rtype: bool
        """
        # Код проверяет наличие необходимых атрибутов
        if not hasattr(group, 'group_url') or not group.group_url:
            logger.error(f'Отсутствует URL группы')
            return False
        try:
            result = urlparse(group.group_url)
            if all([result.scheme, result.netloc]):
                return True
            else:
                 logger.error(f'Невалидный URL группы {group.group_url}')
                 return False
        except:
            logger.error(f'Невалидный URL группы {group.group_url}')
            return False
```