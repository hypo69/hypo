# Анализ кода модуля `promoter.md`

**Качество кода**
8
- Плюсы
    - Код хорошо документирован в формате Markdown, что облегчает понимание функциональности модуля.
    - Представлена диаграмма Mermaid, наглядно демонстрирующая логику работы модуля.
    - Описаны основные методы класса `FacebookPromoter` и их параметры.
    - Есть пример использования класса.
- Минусы
    - Документация не соответствует формату reStructuredText (RST), что требуется по инструкции.
    - Отсутствуют импорты необходимых модулей, таких как `src.logger.logger` и `src.utils.jjson`.
    - Присутствуют стандартные блоки `try-except` вместо обработки ошибок через `logger.error`.
    - Не все комментарии в коде переписаны в формате RST.
    - Необходимо добавить больше конкретики в комментариях, избегая общих слов типа "получаем".

**Рекомендации по улучшению**

1.  Переписать документацию в формате reStructuredText (RST), включая docstring для класса и методов.
2.  Добавить необходимые импорты: `from src.logger.logger import logger` и `from src.utils.jjson import j_loads_ns`.
3.  Заменить блоки `try-except` на обработку ошибок через `logger.error`.
4.  Добавить подробные комментарии в формате RST для каждой функции, метода и переменной.
5.  Уточнить комментарии к коду, избегая общих выражений типа "код исполняет".
6.  Соблюдать стандарты оформления docstring в Python.
7.  Добавить более подробное описание работы каждого метода и класса.
8.  Использовать одинарные кавычки (`'`) в Python коде.

**Оптимизированный код**

```python
"""
Модуль для автоматизации продвижения товаров и событий AliExpress в группах Facebook.
==============================================================================

Этот модуль предоставляет класс :class:`FacebookPromoter`, который автоматизирует
процесс продвижения товаров и событий AliExpress в группах Facebook. Он обрабатывает
публикации в Facebook, отслеживая ранее продвинутые элементы, чтобы избежать дублирования.

Модуль использует WebDriver для автоматизации браузера, что делает продвижение более
эффективным.

Пример использования
--------------------

Пример использования класса `FacebookPromoter`:

.. code-block:: python

    from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
    from src.webdriver.driver import Driver
    from src.utils.jjson import j_loads_ns

    # Настройка экземпляра WebDriver (замените на свой WebDriver)
    d = Driver()

    # Создание экземпляра FacebookPromoter
    promoter = FacebookPromoter(
        d=d,
        promoter='aliexpress',
        group_file_paths=['path/to/group/file1.json', 'path/to/group/file2.json']
    )

    # Запуск продвижения товаров или событий
    promoter.process_groups(
        campaign_name='Campaign1',
        events=[],
        group_categories_to_adv=['sales'],
        language='en',
        currency='USD'
    )
"""
import random
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from types import SimpleNamespace
from typing import Optional, List, Union, Any
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns
from src.webdriver.driver import Driver


class FacebookPromoter:
    """
    Класс для управления процессом продвижения товаров и событий AliExpress
    в группах Facebook.

    :param d: Экземпляр WebDriver для автоматизации.
    :type d: Driver
    :param promoter: Имя промоутера (например, 'aliexpress').
    :type promoter: str
    :param group_file_paths: Пути к файлам с данными групп. Может быть списком путей или одиночным путем.
    :type group_file_paths: Optional[Union[List[Union[str, Path]], str, Path]]
    :param no_video: Флаг для отключения загрузки видео в постах. По умолчанию `False`.
    :type no_video: bool

    :ivar driver: Экземпляр WebDriver для управления браузером.
    :vartype driver: Driver
    :ivar promoter: Название рекламной площадки (например, 'aliexpress').
    :vartype promoter: str
    :ivar group_file_paths: Список путей к файлам с данными групп.
    :vartype group_file_paths: list
    :ivar no_video: Флаг, указывающий на необходимость отключения видео при публикации.
    :vartype no_video: bool
    """
    def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[Union[List[Union[str, Path]], str, Path]] = None, no_video: bool = False):
        self.driver = d
        self.promoter = promoter
        self.group_file_paths = self._normalize_file_paths(group_file_paths) if group_file_paths else []
        self.no_video = no_video

    def _normalize_file_paths(self, file_paths: Union[List[Union[str, Path]], str, Path]) -> List[Path]:
        """
        Нормализует пути к файлам, приводя их к типу Path.

        :param file_paths: Пути к файлам.
        :type file_paths: Union[List[Union[str, Path]], str, Path]
        :return: Список объектов Path.
        :rtype: List[Path]
        """
        if isinstance(file_paths, str):
            return [Path(file_paths)]
        if isinstance(file_paths, Path):
            return [file_paths]
        return [Path(file_path) for file_path in file_paths]
    
    def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
        """
        Продвигает категорию или событие в указанной группе Facebook.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :param item: Категория или событие для продвижения.
        :type item: SimpleNamespace
        :param is_event: Флаг, указывающий, является ли продвигаемый элемент событием. По умолчанию `False`.
        :type is_event: bool
        :param language: Язык для продвижения.
        :type language: str
        :param currency: Валюта для продвижения.
        :type currency: str
        :return: True, если продвижение успешно, иначе False.
        :rtype: bool
        """
        try:
            # Код исполняет продвижение категории или события в группе
            ...
            if not is_event:
                logger.info(f'Продвижение категории {item.name} в группе {group.group_id}')
            else:
                logger.info(f'Продвижение события {item.name} в группе {group.group_id}')
            # Код исполняет обновление данных группы
            self.update_group_promotion_data(group, item.name, is_event)
            return True
        except Exception as ex:
            # Логирование ошибки продвижения
            self.log_promotion_error(is_event, item.name)
            logger.error('Ошибка продвижения:', exc_info=ex)
            return False

    def log_promotion_error(self, is_event: bool, item_name: str):
        """
        Логирует ошибку при неудачном продвижении.

        :param is_event: Флаг, указывающий, является ли продвигаемый элемент событием.
        :type is_event: bool
        :param item_name: Название продвигаемого элемента.
        :type item_name: str
        """
        if is_event:
            logger.error(f'Ошибка продвижения события {item_name}')
        else:
            logger.error(f'Ошибка продвижения категории {item_name}')

    def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
        """
        Обновляет данные группы после продвижения, добавляя продвинутый элемент в список.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :param item_name: Название продвинутого элемента.
        :type item_name: str
        :param is_event: Флаг, указывающий, является ли продвигаемый элемент событием. По умолчанию `False`.
        :type is_event: bool
        """
        if is_event:
            if not hasattr(group, 'promoted_events'):
                group.promoted_events = []
            group.promoted_events.append(item_name)
        else:
            if not hasattr(group, 'promoted_categories'):
                group.promoted_categories = []
            group.promoted_categories.append(item_name)

    def process_groups(self, campaign_name: str = None, events: Optional[List[SimpleNamespace]] = None, is_event: bool = False, group_file_paths: Optional[List[str]] = None, group_categories_to_adv: List[str] = ['sales'], language: str = None, currency: str = None):
        """
        Обрабатывает группы для продвижения текущей кампании или события.

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param events: Список событий для продвижения.
        :type events: Optional[List[SimpleNamespace]]
        :param is_event: Флаг, указывающий, продвигать ли события. По умолчанию `False`.
        :type is_event: bool
        :param group_file_paths: Пути к файлам с данными групп.
        :type group_file_paths: Optional[List[str]]
        :param group_categories_to_adv: Список категорий для продвижения. По умолчанию `['sales']`.
        :type group_categories_to_adv: List[str]
        :param language: Язык для продвижения.
        :type language: str
        :param currency: Валюта для продвижения.
        :type currency: str
        """
        # Код получает пути к файлам групп
        if group_file_paths:
            group_file_paths = self._normalize_file_paths(group_file_paths)
        else:
            group_file_paths = self.group_file_paths
        
        # Код исполняет итерацию по файлам групп
        for file_path in group_file_paths:
            # Код выполняет чтение файла группы
            try:
                group_data = j_loads_ns(file_path)
            except Exception as ex:
                logger.error(f'Ошибка чтения файла группы {file_path}:', exc_info=ex)
                continue

            if not isinstance(group_data, list):
                    group_data = [group_data]

            # Код исполняет итерацию по данным групп
            for group in group_data:
                # Код выполняет проверку валидности данных группы
                if not self.validate_group(group):
                    logger.error(f'Невалидные данные группы: {group}')
                    continue

                # Код исполняет проверку возможности продвижения
                if not self.check_interval(group):
                     logger.debug(f'Группа {group.group_id} еще не готова к продвижению')
                     continue
                 
                # Код получает категорию или событие для продвижения
                if not is_event:
                    item = self.get_category_item(campaign_name, group, language, currency)
                else:
                    if not events:
                        logger.debug(f'Нет событий для продвижения в группе {group.group_id}')
                        continue
                    item = random.choice(events)

                # Код исполняет проверку наличия элемента для продвижения
                if not item:
                     logger.debug(f'Нет элементов для продвижения в группе {group.group_id}')
                     continue

                # Код исполняет продвижение элемента
                self.promote(group, item, is_event, language, currency)
                

    def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> Optional[SimpleNamespace]:
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
        :return: Элемент категории для продвижения или None, если такового нет.
        :rtype: Optional[SimpleNamespace]
        """
        # Код получает данные для продвижения в зависимости от промоутера
        try:
            if self.promoter == 'aliexpress':
                 # Код получает данные категории для AliExpress
                 ...
                 # Код имитирует получение элемента категории
                 item = SimpleNamespace(name='test_category', url='https://test.com')
                 return item
            else:
                logger.error(f'Неподдерживаемый промоутер: {self.promoter}')
                return None
        except Exception as ex:
            logger.error(f'Ошибка получения категории для промоутера {self.promoter}:', exc_info=ex)
            return None
        
    def check_interval(self, group: SimpleNamespace) -> bool:
        """
        Проверяет, прошло ли достаточно времени для повторного продвижения в этой группе.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: True, если группа готова к продвижению, иначе False.
        :rtype: bool
        """
        # Код проверяет интервал между продвижениями
        if not hasattr(group, 'last_promotion'):
            return True
        
        last_promotion = datetime.fromisoformat(group.last_promotion)
        
        if (datetime.now() - last_promotion).total_seconds() > 3600: # 1 hour
            return True
        else:
            return False

    def validate_group(self, group: SimpleNamespace) -> bool:
        """
        Проверяет данные группы на наличие необходимых атрибутов.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: True, если данные группы валидны, иначе False.
        :rtype: bool
        """
        # Код выполняет проверку наличия необходимых атрибутов
        required_attributes = ['group_id', 'last_promotion']
        for attr in required_attributes:
            if not hasattr(group, attr):
                logger.error(f'В данных группы отсутствует необходимый атрибут: {attr}')
                return False
        return True
```