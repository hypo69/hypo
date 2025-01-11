# Анализ кода модуля `promoter.ru.md`

**Качество кода**
9
- Плюсы
    - Хорошая структура документации, подробно описаны классы и методы.
    - Присутствуют примеры использования и диаграмма состояний.
    - Имеется описание лицензии.
    - Код хорошо документирован, есть пояснения к каждому методу.

- Минусы
    - Не хватает импортов для корректной работы.
    - Не стандартизованы кавычки в коде.
    - Отсутствует обработка ошибок.
    - Не используется `j_loads_ns` для загрузки данных.
    - Нет описания модуля в начале файла.
    - Не все комментарии соответствуют PEP8.

**Рекомендации по улучшению**

1.  **Импорт модулей:** Добавить необходимые импорты в начало файла: `from src.utils.jjson import j_loads_ns` и `from src.logger import logger`.
2.  **Использование кавычек**: Заменить двойные кавычки на одинарные в коде, кроме случаев вывода в консоль или логирования.
3.  **Обработка ошибок**: Использовать `try-except` блоки с `logger.error` для обработки ошибок.
4.  **Загрузка данных**: Использовать `j_loads_ns` вместо `json.load` при загрузке данных из файлов.
5.  **Документация**: Добавить описание модуля в начале файла, а также  документацию для всех функций, методов и переменных.
6.  **Комментарии**: Добавить комментарии с объяснениями к каждому блоку кода.
7.  **Форматирование**: Привести документацию в соответствие со стандартом RST.

**Оптимизированный код**

```markdown
"""
Модуль для управления промоутером Facebook.
=========================================================================================

Этот модуль содержит класс :class:`FacebookPromoter`, который используется для продвижения товаров и мероприятий
в группах Facebook.

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
        promoter='aliexpress',
        group_file_paths=['path/to/group/file1.json', 'path/to/group/file2.json']
    )

    # Начало продвижения товаров или мероприятий
    promoter.process_groups(
        campaign_name='Campaign1',
        events=[],
        group_categories_to_adv=['sales'],
        language='en',
        currency='USD'
    )
"""
# Документация модуля Facebook Promoter
from src.utils.jjson import j_loads_ns # Импортируем j_loads_ns из src.utils.jjson
from src.logger import logger # Импортируем logger из src.logger.logger
from random import randint # Импортируем randint из random
from datetime import datetime, timedelta # Импортируем datetime и timedelta из datetime
from pathlib import Path # Импортируем Path из pathlib
from urllib.parse import urlparse # Импортируем urlparse из urllib.parse
from types import SimpleNamespace # Импортируем SimpleNamespace из types
from typing import Optional, List, Union # Импортируем Optional, List, Union из typing
from src.webdriver.driver import Driver # Импортируем Driver из src.webdriver.driver


## Обзор
#
# Модуль **Facebook Promoter** автоматизирует продвижение товаров и мероприятий AliExpress в группах Facebook. Модуль управляет публикациями рекламных материалов на Facebook, избегая дублирования. Для эффективного продвижения используется WebDriver для автоматизации браузера.
#
## Особенности модуля
#
# - Продвижение категорий и мероприятий в группах Facebook.
# - Избежание дублирования публикаций через отслеживание уже опубликованных элементов.
# - Поддержка конфигурации данных групп через файлы.
# - Возможность отключения загрузки видео в публикациях.
#
## Требования
#
# - **Python** 3.x
# - Необходимые библиотеки:
#   - `random`
#   - `datetime`
#   - `pathlib`
#   - `urllib.parse`
#   - `types.SimpleNamespace`
#   - `src` (пользовательский модуль)
#
## Использование
#
### Пример использования класса FacebookPromoter
#
# ```python
# from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
# from src.webdriver.driver import Driver
# from src.utils.jjson import j_loads_ns
#
# # Настройка экземпляра WebDriver (замените на реальный WebDriver)
# d = Driver()
#
# # Создание экземпляра FacebookPromoter
# promoter = FacebookPromoter(
#     d=d,
#     promoter="aliexpress",
#     group_file_paths=["path/to/group/file1.json", "path/to/group/file2.json"]
# )
#
# # Начало продвижения товаров или мероприятий
# promoter.process_groups(
#     campaign_name="Campaign1",
#     events=[],
#     group_categories_to_adv=["sales"],
#     language="en",
#     currency="USD"
# )
# ```
#
## Документация классов
#
### Класс `FacebookPromoter`
#
# Этот класс управляет процессом продвижения товаров и мероприятий AliExpress в группах Facebook.
#
# ```mermaid
# flowchart TD
#     A[Начало] --> B[Инициализация WebDriver]
#     B --> C[Создание экземпляра FacebookPromoter]
#     C --> D[Обработка групп для продвижения]
#     D --> E[Получение данных о группе]
#     E --> F{Данные группы валидны?}
#     F -- Да --> G[Получение элемента категории для продвижения]
#     F -- Нет --> H[Запись ошибки и завершение]
#     G --> I{Группа может быть продвинута?}
#     I -- Да --> J[Продвижение категории или мероприятия]
#     I -- Нет --> K[Ждать интервал между продвижениями]
#     J --> L[Обновление данных о группе]
#     K --> L
#     L --> M[Завершение]
#     H --> M
# ```
#
#### Методы
#
##### `__init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False)`
#
# Инициализирует промоутер для Facebook с необходимыми конфигурациями.
#
# - **Аргументы:**
#     - `d (Driver)`: Экземпляр WebDriver для автоматизации.
#     - `promoter (str)`: Имя промоутера (например, "aliexpress").
#     - `group_file_paths (Optional[list[str | Path] | str | Path])`: Пути к файлам с данными групп.
#     - `no_video (bool)`: Флаг для отключения видео в публикациях. По умолчанию `False`.
#
##### `promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool`
#
# Продвигает категорию или мероприятие в указанной группе Facebook.
#
# - **Аргументы:**
#     - `group (SimpleNamespace)`: Данные группы.
#     - `item (SimpleNamespace)`: Категория или мероприятие для продвижения.
#     - `is_event (bool)`: Является ли элемент мероприятием.
#     - `language (str)`: Язык публикации.
#     - `currency (str)`: Валюта для продвижения.
#
# - **Возвращает:**
#     - `bool`: Успешно ли прошло продвижение.
#
##### `log_promotion_error(self, is_event: bool, item_name: str)`
#
# Записывает ошибку, если продвижение не удалось.
#
# - **Аргументы:**
#     - `is_event (bool)`: Является ли элемент мероприятием.
#     - `item_name (str)`: Название элемента.
#
##### `update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False)`
#
# Обновляет данные группы после продвижения, добавляя продвигаемый элемент в список продвигаемых категорий или мероприятий.
#
# - **Аргументы:**
#     - `group (SimpleNamespace)`: Данные группы.
#     - `item_name (str)`: Название продвигаемого элемента.
#     - `is_event (bool)`: Является ли элемент мероприятием.
#
##### `process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None)`
#
# Обрабатывает группы для текущей кампании или продвижения мероприятия.
#
# - **Аргументы:**
#     - `campaign_name (str)`: Название кампании.
#     - `events (list[SimpleNamespace])`: Список мероприятий для продвижения.
#     - `is_event (bool)`: Является ли продвижение мероприятий или категорий.
#     - `group_file_paths (list[str])`: Пути к файлам с данными групп.
#     - `group_categories_to_adv (list[str])`: Категории для продвижения.
#     - `language (str)`: Язык публикации.
#     - `currency (str)`: Валюта для продвижения.
#
##### `get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace`
#
# Получает элемент категории для продвижения в зависимости от кампании и промоутера.
#
# - **Аргументы:**
#     - `campaign_name (str)`: Название кампании.
#     - `group (SimpleNamespace)`: Данные группы.
#     - `language (str)`: Язык для публикации.
#     - `currency (str)`: Валюта для публикации.
#
# - **Возвращает:**
#     - `SimpleNamespace`: Элемент категории для продвижения.
#
##### `check_interval(self, group: SimpleNamespace) -> bool`
#
# Проверяет, прошло ли достаточно времени, чтобы снова продвигать эту группу.
#
# - **Аргументы:**
#     - `group (SimpleNamespace)`: Данные группы.
#
# - **Возвращает:**
#     - `bool`: Можно ли снова продвигать группу.
#
##### `validate_group(self, group: SimpleNamespace) -> bool`
#
# Проверяет данные группы, чтобы убедиться в их корректности.
#
# - **Аргументы:**
#     - `group (SimpleNamespace)`: Данные группы.
#
# - **Возвращает:**
#     - `bool`: Корректны ли данные группы.
#
## Лицензия
#
# Этот модуль является частью пакета **Facebook Promoter** и лицензируется по лицензии MIT.


class FacebookPromoter:
    """
    Класс для управления продвижением в Facebook.

    Этот класс предоставляет методы для продвижения товаров и мероприятий в группах Facebook.
    Использует WebDriver для автоматизации браузера и отслеживает уже опубликованные элементы,
    чтобы избежать дублирования.

    Args:
        d (Driver): Экземпляр WebDriver для управления браузером.
        promoter (str): Название промоутера, например, "aliexpress".
        group_file_paths (Optional[Union[List[Union[str, Path]], str, Path]]): Список путей к файлам с данными групп.
            Может быть как списком строк или объектов Path, так и единичной строкой или Path. По умолчанию None.
        no_video (bool): Флаг, указывающий, следует ли отключать загрузку видео в публикациях. По умолчанию False.

    """
    def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[Union[List[Union[str, Path]], str, Path]] = None, no_video: bool = False):
        """
        Инициализирует промоутер для Facebook.

        Args:
            d (Driver): Экземпляр WebDriver для управления браузером.
            promoter (str): Название промоутера, например, "aliexpress".
            group_file_paths (Optional[Union[List[Union[str, Path]], str, Path]]): Список путей к файлам с данными групп.
                Может быть как списком строк или объектов Path, так и единичной строкой или Path. По умолчанию None.
            no_video (bool): Флаг, указывающий, следует ли отключать загрузку видео в публикациях. По умолчанию False.

        """
        self.driver = d # Инициализируем драйвер
        self.promoter = promoter # Инициализируем имя промоутера
        self.group_file_paths = group_file_paths # Инициализируем пути к файлам групп
        self.no_video = no_video # Инициализируем флаг для отключения видео
        self.group_data = {} # Инициализируем словарь для данных групп

    def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
        """
        Продвигает категорию или мероприятие в указанной группе Facebook.

        Args:
            group (SimpleNamespace): Данные группы.
            item (SimpleNamespace): Категория или мероприятие для продвижения.
            is_event (bool): Флаг, указывающий, является ли элемент мероприятием.
            language (str): Язык публикации.
            currency (str): Валюта для продвижения.

        Returns:
            bool: True, если продвижение прошло успешно, False в противном случае.
        """
        try:
            # Код исполняет проверку, является ли item мероприятием
            item_name = item.event_name if is_event else item.name
            # Код исполняет логирование начала продвижения
            logger.info(f'Начало продвижения {item_name=} в группе {group.name=}')
            # Код исполняет действия по продвижению
            ... # Заглушка для кода продвижения
            # Код исполняет обновление данных группы после продвижения
            self.update_group_promotion_data(group=group, item_name=item_name, is_event=is_event)
            return True
        except Exception as ex:
            # Код исполняет логирование ошибки продвижения
            logger.error(f'Ошибка продвижения {item_name=}', exc_info=ex)
            # Код исполняет логирование ошибки
            self.log_promotion_error(is_event=is_event, item_name=item_name)
            return False

    def log_promotion_error(self, is_event: bool, item_name: str):
        """
        Записывает ошибку, если продвижение не удалось.

        Args:
            is_event (bool): Флаг, указывающий, является ли элемент мероприятием.
            item_name (str): Название элемента, для которого не удалось продвижение.

        """
        # Код исполняет запись ошибки в лог
        logger.error(f'Ошибка продвижения {"мероприятия" if is_event else "категории"} {item_name=}')

    def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
        """
        Обновляет данные группы после продвижения, добавляя продвигаемый элемент в список продвигаемых категорий или мероприятий.

        Args:
            group (SimpleNamespace): Данные группы.
            item_name (str): Название продвигаемого элемента.
            is_event (bool): Флаг, указывающий, является ли элемент мероприятием.
        """
        # Код исполняет добавление элемента в список продвинутых
        if is_event:
            if not hasattr(group, 'promoted_events'):
                group.promoted_events = []
            group.promoted_events.append(item_name)
        else:
            if not hasattr(group, 'promoted_categories'):
                group.promoted_categories = []
            group.promoted_categories.append(item_name)

    def process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None):
        """
        Обрабатывает группы для текущей кампании или продвижения мероприятия.

        Args:
            campaign_name (str): Название кампании.
            events (list[SimpleNamespace]): Список мероприятий для продвижения.
            is_event (bool): Флаг, указывающий, является ли продвижение мероприятий или категорий.
            group_file_paths (list[str]): Список путей к файлам с данными групп.
            group_categories_to_adv (list[str]): Список категорий для продвижения.
            language (str): Язык для публикации.
            currency (str): Валюта для продвижения.
        """
        # Код исполняет проверку наличия путей к файлам групп
        if not group_file_paths:
            if not self.group_file_paths:
                logger.error('Отсутствуют пути к файлам групп')
                return
            group_file_paths = self.group_file_paths if isinstance(self.group_file_paths, list) else [self.group_file_paths]
        # Код исполняет обход файлов групп
        for file_path in group_file_paths:
            try:
                # Код исполняет загрузку данных группы из файла
                file_path = Path(file_path) if isinstance(file_path, str) else file_path
                group_data = j_loads_ns(file_path)
                # Код исполняет обход групп из файла
                for group in group_data.groups:
                   # Код исполняет проверку валидности данных группы
                    if not self.validate_group(group=group):
                        logger.error(f'Группа {group.name=} не прошла валидацию')
                        continue
                    # Код исполняет проверку возможности продвижения
                    if not self.check_interval(group=group):
                        logger.info(f'Группа {group.name=} не может быть продвинута из-за интервала')
                        continue
                    # Код исполняет продвижение категорий
                    if not is_event:
                       # Код исполняет получение элемента категории для продвижения
                        item = self.get_category_item(
                            campaign_name=campaign_name,
                            group=group,
                            language=language,
                            currency=currency
                        )
                        # Код исполняет проверку наличия элемента для продвижения
                        if not item:
                            logger.info(f'Нет элемента для продвижения в группе {group.name=}')
                            continue
                        # Код исполняет продвижение элемента
                        self.promote(
                            group=group,
                            item=item,
                            is_event=is_event,
                            language=language,
                            currency=currency
                        )
                    # Код исполняет продвижение событий
                    else:
                        # Код исполняет проверку наличия событий для продвижения
                        if not events:
                            logger.info(f'Нет событий для продвижения в группе {group.name=}')
                            continue
                        # Код исполняет обход событий
                        for event in events:
                            # Код исполняет продвижение события
                            self.promote(
                                group=group,
                                item=event,
                                is_event=is_event,
                                language=language,
                                currency=currency
                            )

            except Exception as ex:
                # Код исполняет логирование ошибки при обработке файла
                logger.error(f'Ошибка обработки файла {file_path=}', exc_info=ex)

    def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace:
        """
        Получает элемент категории для продвижения в зависимости от кампании и промоутера.

        Args:
            campaign_name (str): Название кампании.
            group (SimpleNamespace): Данные группы.
            language (str): Язык для публикации.
            currency (str): Валюта для публикации.

        Returns:
            SimpleNamespace: Элемент категории для продвижения.
        """
        # Код исполняет получение элемента для продвижения
        ... # Заглушка для получения элемента
        return SimpleNamespace(name='test_category')

    def check_interval(self, group: SimpleNamespace) -> bool:
        """
        Проверяет, прошло ли достаточно времени, чтобы снова продвигать эту группу.

        Args:
            group (SimpleNamespace): Данные группы.

        Returns:
            bool: True, если можно продвигать группу, False в противном случае.
        """
        # Код исполняет проверку интервала между продвижениями
        if not hasattr(group, 'last_promotion_time'):
            group.last_promotion_time = datetime.now()
            return True
        interval = timedelta(minutes=randint(1, 3))
        return datetime.now() - group.last_promotion_time > interval

    def validate_group(self, group: SimpleNamespace) -> bool:
        """
         Проверяет данные группы, чтобы убедиться в их корректности.

        Args:
             group (SimpleNamespace): Данные группы.

        Returns:
             bool: True, если данные группы корректны, False в противном случае.
        """
        # Код исполняет проверку наличия необходимых атрибутов в группе
        if not all([hasattr(group, attr) for attr in ['name', 'url']]):
            return False
        # Код исполняет проверку корректности url группы
        try:
           result = urlparse(group.url)
           return all([result.scheme, result.netloc])
        except:
           return False
```