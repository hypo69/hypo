# Анализ кода модуля `promoter.ru.md`

**Качество кода**
8
-   Плюсы
    -   Код содержит подробную документацию в формате Markdown, что облегчает понимание функциональности модуля.
    -   Присутствует описание основных классов, методов и их параметров, что способствует удобству использования модуля.
    -   Представлен Mermaid-граф, наглядно отображающий процесс работы модуля.
    -   Есть пример использования класса `FacebookPromoter`.
-   Минусы
    -   Документация не соответствует формату reStructuredText (RST), что затрудняет интеграцию с инструментами документации Python.
    -   В коде не используются `j_loads` или `j_loads_ns` для загрузки файлов, что является нарушением инструкции.
    -   Не хватает импортов, используемых в коде.
    -   Отсутствует логирование ошибок с использованием `src.logger.logger`.
    -   Некоторые комментарии не достаточно подробные и не соответствуют reStructuredText (RST).

**Рекомендации по улучшению**
1.  Переписать всю документацию в формате reStructuredText (RST).
2.  Заменить `json.load` на `j_loads` или `j_loads_ns`.
3.  Добавить необходимые импорты.
4.  Внедрить логирование ошибок через `src.logger.logger`.
5.  Добавить подробные комментарии в формате RST для каждой функции, метода и класса.
6.  Использовать `try-except` блоки с `logger.error` вместо стандартных.
7.  Унифицировать стиль кода и комментариев.
8.  Переписать все комментарии после `#` в соответствии с инструкцией.
9.  Использовать консистентные наименования переменных и функций.
10. Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.

**Оптимизированный код**
```python
"""
Модуль для автоматизации продвижения товаров и мероприятий AliExpress в группах Facebook.
=====================================================================================

Модуль `FacebookPromoter` управляет публикациями рекламных материалов на Facebook,
избегая дублирования. Для эффективного продвижения используется WebDriver для автоматизации браузера.

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
import random
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import urlencode
from types import SimpleNamespace
from typing import Optional, List, Union, Any

# from src.utils.jjson import j_loads # Исправлено на j_loads_ns
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger
from src.webdriver.driver import Driver # Добавлен импорт
# from src.endpoints.advertisement.base_promoter import BasePromoter # Добавлен импорт (если необходим)


class FacebookPromoter:
    """
    Класс для управления продвижением товаров и мероприятий AliExpress в группах Facebook.

    :param d: Экземпляр WebDriver для автоматизации.
    :type d: Driver
    :param promoter: Имя промоутера (например, "aliexpress").
    :type promoter: str
    :param group_file_paths: Пути к файлам с данными групп.
    :type group_file_paths: Optional[list[str | Path] | str | Path]
    :param no_video: Флаг для отключения видео в публикациях.
    :type no_video: bool
    """
    def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[Union[List[Union[str, Path]], str, Path]] = None, no_video: bool = False):
        self.driver = d
        self.promoter = promoter
        self.group_file_paths = group_file_paths
        self.no_video = no_video
        self.groups = []
        if group_file_paths:
            self.load_groups()

    def load_groups(self):
        """
        Загружает данные групп из файлов.
        """
        if isinstance(self.group_file_paths, (str, Path)):
            self.group_file_paths = [self.group_file_paths]
        for file_path in self.group_file_paths:
           try:
              # код исполняет загрузку данных группы из файла используя j_loads_ns
              group = j_loads_ns(file_path)
              self.groups.append(group)
           except Exception as ex:
                logger.error(f'Ошибка при загрузке данных группы из файла: {file_path}', exc_info=ex)

    def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
        """
        Продвигает категорию или мероприятие в указанной группе Facebook.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :param item: Категория или мероприятие для продвижения.
        :type item: SimpleNamespace
        :param is_event: Является ли элемент мероприятием.
        :type is_event: bool
        :param language: Язык публикации.
        :type language: str
        :param currency: Валюта для продвижения.
        :type currency: str
        :return: Успешно ли прошло продвижение.
        :rtype: bool
        """
        try:
            # Код формирует ссылку для публикации
            link = item.link
            if not link:
               logger.error(f'Не найдена ссылка для продвижения {item=}')
               return False
            if language and currency:
                params = {"language": language, "currency": currency}
                link += f"&{urlencode(params)}"

            # код исполняет переход по ссылке и публикацию
            self.driver.get(link)
            # TODO: Добавить логику публикации
            self.driver.wait(random.randint(2, 5))
            logger.info(f'Успешно продвинута ссылка: {link}')
            return True
        except Exception as ex:
            logger.error(f'Ошибка во время продвижения {item=}', exc_info=ex)
            self.log_promotion_error(is_event, item.name)
            return False

    def log_promotion_error(self, is_event: bool, item_name: str):
        """
        Записывает ошибку, если продвижение не удалось.

        :param is_event: Является ли элемент мероприятием.
        :type is_event: bool
        :param item_name: Название элемента.
        :type item_name: str
        """
        item_type = "мероприятия" if is_event else "категории"
        logger.error(f'Не удалось продвинуть {item_type} {item_name}')

    def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
        """
        Обновляет данные группы после продвижения, добавляя продвигаемый элемент в список продвигаемых категорий или мероприятий.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :param item_name: Название продвигаемого элемента.
        :type item_name: str
        :param is_event: Является ли элемент мероприятием.
        :type is_event: bool
        """
        if is_event:
            if not hasattr(group, 'promoted_events'):
                group.promoted_events = []
            # код добавляет название мероприятия в список продвинутых
            group.promoted_events.append(item_name)
        else:
            if not hasattr(group, 'promoted_categories'):
               group.promoted_categories = []
            # код добавляет название категории в список продвинутых
            group.promoted_categories.append(item_name)
        # TODO: реализовать сохранение данных группы
    def process_groups(self, campaign_name: str = None, events: Optional[List[SimpleNamespace]] = None,
                       is_event: bool = False, group_file_paths: Optional[List[str]] = None,
                       group_categories_to_adv: List[str] = ['sales'], language: str = None, currency: str = None):
        """
        Обрабатывает группы для текущей кампании или продвижения мероприятия.

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param events: Список мероприятий для продвижения.
        :type events: Optional[List[SimpleNamespace]]
        :param is_event: Является ли продвижение мероприятий или категорий.
        :type is_event: bool
        :param group_file_paths: Пути к файлам с данными групп.
        :type group_file_paths: Optional[List[str]]
        :param group_categories_to_adv: Категории для продвижения.
        :type group_categories_to_adv: List[str]
        :param language: Язык публикации.
        :type language: str
        :param currency: Валюта для продвижения.
        :type currency: str
        """
        if group_file_paths:
            self.group_file_paths = group_file_paths
            self.load_groups()

        for group in self.groups:
            if not self.validate_group(group):
                logger.error(f'Группа не прошла валидацию, пропускаем {group=}')
                continue

            if not self.check_interval(group):
                logger.debug(f'Интервал для группы {group.name} еще не прошел, пропускаем')
                continue

            if is_event and events:
                # код продвигает мероприятия если is_event == True и есть список событий
                for event in events:
                    if self.promote(group, event, is_event, language, currency):
                        self.update_group_promotion_data(group, event.name, is_event)
            else:
                # код продвигает категории если is_event == False
                item = self.get_category_item(campaign_name, group, language, currency)
                if item:
                    if self.promote(group, item, is_event, language, currency):
                        self.update_group_promotion_data(group, item.name, is_event)

    def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> Optional[SimpleNamespace]:
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
        :rtype: Optional[SimpleNamespace]
        """
        try:
            # TODO: Реализовать логику выбора категории для продвижения
            # код возвращает случайный элемент из списка категорий
            if not hasattr(group, 'categories'):
                logger.error(f'У группы {group.name} отсутствуют категории')
                return None
            available_categories = [cat for cat in group.categories if cat.name not in getattr(group, 'promoted_categories', [])]
            if not available_categories:
                logger.debug(f'Нет доступных категорий для продвижения в группе {group.name}')
                return None
            return random.choice(available_categories)
        except Exception as ex:
            logger.error(f'Ошибка при получении элемента категории {group=}', exc_info=ex)
            return None

    def check_interval(self, group: SimpleNamespace) -> bool:
        """
        Проверяет, прошло ли достаточно времени, чтобы снова продвигать эту группу.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: Можно ли снова продвигать группу.
        :rtype: bool
        """
        if not hasattr(group, 'last_promotion'):
           return True
        if not group.last_promotion:
            return True
        # код проверяет, прошло ли достаточно времени с последнего продвижения
        last_promotion_time = datetime.fromisoformat(group.last_promotion)
        interval = timedelta(minutes=group.promotion_interval)
        return datetime.now() >= last_promotion_time + interval

    def validate_group(self, group: SimpleNamespace) -> bool:
        """
        Проверяет данные группы, чтобы убедиться в их корректности.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: Корректны ли данные группы.
        :rtype: bool
        """
        # код проверяет, все ли необходимые поля присутствуют в данных группы
        if not all(hasattr(group, attr) for attr in ['name', 'link', 'promotion_interval']):
            logger.error(f'Не все обязательные поля присутствуют в группе {group=}')
            return False
        return True
```