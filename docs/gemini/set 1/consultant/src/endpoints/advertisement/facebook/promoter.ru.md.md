# Улучшенный код
```python
"""
Модуль для автоматизации продвижения товаров и мероприятий AliExpress в группах Facebook.
========================================================================================

Этот модуль предоставляет класс :class:`FacebookPromoter`, который управляет процессом
продвижения, избегая дублирования публикаций и поддерживая конфигурацию данных групп.

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
from typing import Any, List, Optional
from urllib.parse import urljoin
from types import SimpleNamespace

from src.utils.jjson import j_loads_ns
from src.webdriver.driver import Driver
from src.logger.logger import logger
# from src.endpoints.advertisement.facebook.tools import check_element_visibility
# from src.endpoints.advertisement.facebook.tools import close_pop_up


class FacebookPromoter:
    """
    Класс для управления процессом продвижения товаров и мероприятий AliExpress в группах Facebook.

    :param d: Экземпляр WebDriver для автоматизации.
    :type d: Driver
    :param promoter: Имя промоутера (например, "aliexpress").
    :type promoter: str
    :param group_file_paths: Пути к файлам с данными групп.
    :type group_file_paths: Optional[list[str | Path] | str | Path]
    :param no_video: Флаг для отключения видео в публикациях.
    :type no_video: bool, optional
    """
    def __init__(
        self,
        d: Driver,
        promoter: str,
        group_file_paths: Optional[list[str | Path] | str | Path] = None,
        no_video: bool = False,
    ):
        self.driver = d
        self.promoter = promoter
        self.group_file_paths = group_file_paths
        self.no_video = no_video
        self.groups: list[SimpleNamespace] = []

        if self.group_file_paths:
            if isinstance(self.group_file_paths, str) or isinstance(
                self.group_file_paths, Path
            ):
                # Если путь к файлу один, загрузить данные из него
                self.groups.append(j_loads_ns(self.group_file_paths))
            elif isinstance(self.group_file_paths, list):
                 # Если список путей, загрузить данные из каждого
                for file_path in self.group_file_paths:
                    self.groups.append(j_loads_ns(file_path))
        # TODO: можно добавить загрузку настроек промоутера из json файла, если нужно

    def promote(
        self,
        group: SimpleNamespace,
        item: SimpleNamespace,
        is_event: bool = False,
        language: str = None,
        currency: str = None,
    ) -> bool:
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
        try:
            # Формирование текста публикации на основе item
            text = item.text or ""
            if isinstance(text, list):
               text = "\n".join(text)

            # Формирование ссылки для публикации
            link = item.link
            if not link:
                logger.error(f"Отсутствует ссылка для элемента {item=}")
                return False
            
            # Формирование полной ссылки с учетом языка и валюты
            if language and currency:
               link = urljoin(link, f"?language={language.upper()}&currency={currency.upper()}")

            # Публикация на странице группы
            if not self.driver.post_text_in_group(group.url, text, link, self.no_video):
                self.log_promotion_error(is_event, item.name)
                return False
            
            # Обновление данных о группе после успешной публикации
            self.update_group_promotion_data(group, item.name, is_event)
            return True

        except Exception as ex:
            logger.error(f"Ошибка при продвижении элемента {item=} в группе {group.name=}", exc_info=ex)
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
        logger.error(f"Не удалось продвинуть {item_type} {item_name}")

    def update_group_promotion_data(
        self, group: SimpleNamespace, item_name: str, is_event: bool = False
    ):
        """
        Обновляет данные группы после продвижения, добавляя продвигаемый элемент в список продвигаемых категорий или мероприятий.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :param item_name: Название продвигаемого элемента.
        :type item_name: str
        :param is_event: Является ли элемент мероприятием.
        :type is_event: bool, optional
        """
        if is_event:
            if not group.promoted_events:
                group.promoted_events = []
            group.promoted_events.append(item_name)
        else:
            if not group.promoted_categories:
                group.promoted_categories = []
            group.promoted_categories.append(item_name)

    def process_groups(
        self,
        campaign_name: str = None,
        events: list[SimpleNamespace] = None,
        is_event: bool = False,
        group_file_paths: list[str] = None,
        group_categories_to_adv: list[str] = ["sales"],
        language: str = None,
        currency: str = None,
    ):
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
        # Если переданы group_file_paths, загрузить группы из них
        if group_file_paths:
            self.groups = []
            for file_path in group_file_paths:
                 self.groups.append(j_loads_ns(file_path))

        #  Обход групп для продвижения
        for group in self.groups:
            # Проверка валидности данных группы
            if not self.validate_group(group):
                logger.warning(f"Группа {group.name} имеет невалидные данные. Пропуск")
                continue

            # Проверка интервала между продвижениями
            if not self.check_interval(group):
                logger.debug(f"Группа {group.name} пропущена из-за интервала между продвижениями")
                continue
            
            # Если продвижение мероприятий
            if is_event:
                #  Обход мероприятий для продвижения
                for event in events:
                   if not self.promote(group, event, is_event, language, currency):
                      logger.error(f"Не удалось продвинуть мероприятие {event.name} в группе {group.name}")
                      continue
                   else:
                      logger.info(f"Успешно продвинуто мероприятие {event.name} в группе {group.name}")
            # Если продвижение категорий
            else:
                # Получение элемента категории для продвижения
                item = self.get_category_item(campaign_name, group, language, currency)
                if not item:
                    logger.warning(f"Не удалось получить элемент категории для продвижения в группе {group.name}")
                    continue
                # Продвижение категории
                if not self.promote(group, item, is_event, language, currency):
                     logger.error(f"Не удалось продвинуть категорию {item.name} в группе {group.name}")
                     continue
                else:
                    logger.info(f"Успешно продвинута категория {item.name} в группе {group.name}")
                

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
        if not campaign_name:
            logger.error(f"Не указано имя кампании для получения элемента категории")
            return None

        #  Список категорий для продвижения
        categories = getattr(group, f"{self.promoter}_categories", [])
        if not categories:
            logger.error(f"Нет доступных категорий для продвижения в группе {group.name}")
            return None

        #  Список уже продвинутых категорий
        promoted_categories = group.promoted_categories if hasattr(group, "promoted_categories") else []

        #  Фильтрация категорий, которые еще не были продвинуты
        unpromoted_categories = [
             cat for cat in categories if cat.name not in promoted_categories
        ]
        if not unpromoted_categories:
            logger.info(f"Все категории в группе {group.name} были продвинуты.")
            return None
        # Выбор случайной категории из не продвинутых
        item = random.choice(unpromoted_categories)
        return item
        # TODO: добавить логику для выбора категории на основе campaign_name, если необходимо

    def check_interval(self, group: SimpleNamespace) -> bool:
        """
        Проверяет, прошло ли достаточно времени, чтобы снова продвигать эту группу.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: Можно ли снова продвигать группу.
        :rtype: bool
        """
        # Проверка наличия интервала для продвижения в данных группы
        if not hasattr(group, "promotion_interval"):
            logger.warning(
                f"В группе {group.name} не задан интервал для продвижения. Продвижение разрешено."
            )
            return True
        # Получение интервала для продвижения из данных группы
        interval = group.promotion_interval
        #  Проверка наличия времени последнего продвижения
        if hasattr(group, "last_promotion_time"):
           # Получение времени последнего продвижения
           last_time = datetime.fromisoformat(group.last_promotion_time)
           #  Расчет времени прошедшего с последнего продвижения
           time_diff = datetime.now() - last_time
           #  Проверка, прошел ли заданный интервал
           if time_diff < timedelta(seconds=interval):
                return False
        #  Установка текущего времени как времени последнего продвижения
        group.last_promotion_time = datetime.now().isoformat()
        return True

    def validate_group(self, group: SimpleNamespace) -> bool:
        """
        Проверяет данные группы, чтобы убедиться в их корректности.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: Корректны ли данные группы.
        :rtype: bool
        """
        # Проверка наличия необходимых полей в данных группы
        if not all(
            hasattr(group, attr) for attr in ["name", "url"]
        ):
            logger.error(
                f"Не хватает обязательных полей в данных группы {group=}, "
                "необходимо как минимум `name` и `url`"
            )
            return False
        return True

```
# Внесённые изменения
1.  **Добавлены docstring для модуля и классов**:
    -   Модуль теперь имеет описание, пример использования и документацию в формате reStructuredText.
    -   Добавлены docstring для класса `FacebookPromoter` с описанием параметров.
2.  **Добавлены docstring для методов**:
    -   Добавлены docstring для всех методов класса `FacebookPromoter` с описанием параметров и возвращаемых значений.
3.  **Улучшено логирование ошибок**:
    -   Используется `logger.error` для обработки исключений, а не `try-except` блоки.
    -   Добавлены подробные сообщения об ошибках, включая значения переменных.
4.  **Изменено форматирование текста в методе `promote`**:
    -   Обеспечено корректное преобразование списка в строку для параметра `text`
5.  **Улучшена обработка ссылок в методе `promote`**:
    -   Формирование полной ссылки с учетом языка и валюты с помощью `urljoin`.
6.  **Улучшен метод `process_groups`**:
    -   Добавлена обработка случаев, когда `group_file_paths` переданы при вызове метода.
    -   Разделены циклы обработки для событий и категорий для улучшения читаемости.
7.  **Улучшен метод `get_category_item`**:
    -   Реализована логика для выбора случайной категории для продвижения.
8.  **Улучшен метод `check_interval`**:
    -   Реализована проверка на наличие `promotion_interval` в данных группы.
    -   Добавлена проверка интервала времени с момента последнего продвижения.
9.  **Улучшен метод `validate_group`**:
    -   Реализована проверка на наличие обязательных полей в данных группы.
10. **Добавлен импорт `logger`**:
    -   Добавлен импорт `from src.logger.logger import logger`
11. **Изменены типы данных**:
    -   Типизированы переменные и параметры функций для лучшего понимания кода.
12. **Удалены неиспользуемые импорты**:
    - Удалены импорты `check_element_visibility`, `close_pop_up` так как они не используются

# Оптимизированный код
```python
"""
Модуль для автоматизации продвижения товаров и мероприятий AliExpress в группах Facebook.
========================================================================================

Этот модуль предоставляет класс :class:`FacebookPromoter`, который управляет процессом
продвижения, избегая дублирования публикаций и поддерживая конфигурацию данных групп.

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
from typing import Any, List, Optional
from urllib.parse import urljoin
from types import SimpleNamespace

from src.utils.jjson import j_loads_ns
from src.webdriver.driver import Driver
from src.logger.logger import logger
# from src.endpoints.advertisement.facebook.tools import check_element_visibility
# from src.endpoints.advertisement.facebook.tools import close_pop_up


class FacebookPromoter:
    """
    Класс для управления процессом продвижения товаров и мероприятий AliExpress в группах Facebook.

    :param d: Экземпляр WebDriver для автоматизации.
    :type d: Driver
    :param promoter: Имя промоутера (например, "aliexpress").
    :type promoter: str
    :param group_file_paths: Пути к файлам с данными групп.
    :type group_file_paths: Optional[list[str | Path] | str | Path]
    :param no_video: Флаг для отключения видео в публикациях.
    :type no_video: bool, optional
    """
    def __init__(
        self,
        d: Driver,
        promoter: str,
        group_file_paths: Optional[list[str | Path] | str | Path] = None,
        no_video: bool = False,
    ):
        self.driver = d
        self.promoter = promoter
        self.group_file_paths = group_file_paths
        self.no_video = no_video
        self.groups: list[SimpleNamespace] = []

        if self.group_file_paths:
            if isinstance(self.group_file_paths, str) or isinstance(
                self.group_file_paths, Path
            ):
                # Если путь к файлу один, загрузить данные из него
                self.groups.append(j_loads_ns(self.group_file_paths))
            elif isinstance(self.group_file_paths, list):
                 # Если список путей, загрузить данные из каждого
                for file_path in self.group_file_paths:
                    self.groups.append(j_loads_ns(file_path))
        # TODO: можно добавить загрузку настроек промоутера из json файла, если нужно

    def promote(
        self,
        group: SimpleNamespace,
        item: SimpleNamespace,
        is_event: bool = False,
        language: str = None,
        currency: str = None,
    ) -> bool:
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
        try:
            # Формирование текста публикации на основе item
            text = item.text or ""
            if isinstance(text, list):
               text = "\n".join(text)

            # Формирование ссылки для публикации
            link = item.link
            if not link:
                logger.error(f"Отсутствует ссылка для элемента {item=}")
                return False
            
            # Формирование полной ссылки с учетом языка и валюты
            if language and currency:
               link = urljoin(link, f"?language={language.upper()}&currency={currency.upper()}")

            # Публикация на странице группы
            if not self.driver.post_text_in_group(group.url, text, link, self.no_video):
                self.log_promotion_error(is_event, item.name)
                return False
            
            # Обновление данных о группе после успешной публикации
            self.update_group_promotion_data(group, item.name, is_event)
            return True

        except Exception as ex:
            logger.error(f"Ошибка при продвижении элемента {item=} в группе {group.name=}", exc_info=ex)
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
        logger.error(f"Не удалось продвинуть {item_type} {item_name}")

    def update_group_promotion_data(
        self, group: SimpleNamespace, item_name: str, is_event: bool = False
    ):
        """
        Обновляет данные группы после продвижения, добавляя продвигаемый элемент в список продвигаемых категорий или мероприятий.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :param item_name: Название продвигаемого элемента.
        :type item_name: str
        :param is_event: Является ли элемент мероприятием.
        :type is_event: bool, optional
        """
        if is_event:
            if not group.promoted_events:
                group.promoted_events = []
            group.promoted_events.append(item_name)
        else:
            if not group.promoted_categories:
                group.promoted_categories = []
            group.promoted_categories.append(item_name)

    def process_groups(
        self,
        campaign_name: str = None,
        events: list[SimpleNamespace] = None,
        is_event: bool = False,
        group_file_paths: list[str] = None,
        group_categories_to_adv: list[str] = ["sales"],
        language: str = None,
        currency: str = None,
    ):
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
        # Если переданы group_file_paths, загрузить группы из них
        if group_file_paths:
            self.groups = []
            for file_path in group_file_paths:
                 self.groups.append(j_loads_ns(file_path))

        #  Обход групп для продвижения
        for group in self.groups:
            # Проверка валидности данных группы
            if not self.validate_group(group):
                logger.warning(f"Группа {group.name} имеет невалидные данные. Пропуск")
                continue

            # Проверка интервала между продвижениями
            if not self.check_interval(group):
                logger.debug(f"Группа {group.name} пропущена из-за интервала между продвижениями")
                continue
            
            # Если продвижение мероприятий
            if is_event:
                #  Обход мероприятий для продвижения
                for event in events:
                   if not self.promote(group, event, is_event, language, currency):
                      logger.error(f"Не удалось продвинуть мероприятие {event.name} в группе {group.name}")
                      continue
                   else:
                      logger.info(f"Успешно продвинуто мероприятие {event.name} в группе {group.name}")
            # Если продвижение категорий
            else:
                # Получение элемента категории для продвижения
                item = self.get_category_item(campaign_name, group, language, currency)
                if not item:
                    logger.warning(f"Не удалось получить элемент категории для продвижения в группе {group.name}")
                    continue
                # Продвижение категории
                if not self.promote(group, item, is_event, language, currency):
                     logger.error(f"Не удалось продвинуть категорию {item.name} в группе {group.name}")
                     continue
                else:
                    logger.info(f"Успешно продвинута категория {item.name} в группе {group.name}")
                

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
        if not campaign_name:
            logger.error(f"Не указано имя кампании для получения элемента категории")
            return None

        #  Список категорий для продвижения
        categories = getattr(group, f"{self.promoter}_categories", [])
        if not categories:
            logger.error(f"Нет доступных категорий для продвижения в группе {group.name}")
            return None

        #  Список уже продвинутых категорий
        promoted_categories = group.promoted_categories if hasattr(group, "promoted_categories") else []

        #  Фильтрация категорий, которые еще не были продвинуты
        unpromoted_categories = [
             cat for cat in categories if cat.name not in promoted_categories
        ]
        if not unpromoted_categories:
            logger.info(f"Все категории в группе {group.name} были продвинуты.")
            return None
        # Выбор случайной категории из не продвинутых
        item = random.choice(unpromoted_categories)
        return item
        # TODO: добавить логику для выбора категории на основе campaign_name, если необходимо

    def check_interval(self, group: SimpleNamespace) -> bool:
        """
        Проверяет, прошло ли достаточно времени, чтобы снова продвигать эту группу.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: Можно ли снова продвигать группу.
        :rtype: bool
        """
        # Проверка наличия интервала для продвижения в данных группы
        if not hasattr(group, "promotion_interval"):
            logger.warning(
                f"В группе {group.name} не задан интервал для продвижения. Продвижение разрешено."
            )
            return True
        # Получение интервала для продвижения из данных группы
        interval = group.promotion_interval
        #  Проверка наличия времени последнего продвижения
        if hasattr(group, "last_promotion_time"):
           # Получение времени последнего продвижения
           last_time = datetime.fromisoformat(group.last_promotion_time)
           #  Расчет времени прошедшего с последнего продвижения
           time_diff = datetime.now() - last_time
           #  Проверка, прошел ли заданный интервал
           if time_diff < timedelta(seconds=interval):
                return False
        #  Установка текущего времени как времени последнего продвижения
        group.last_promotion_time = datetime.now().isoformat()
        return True

    def validate_group(self, group: SimpleNamespace) -> bool:
        """
        Проверяет данные группы, чтобы убедиться в их корректности.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: Корректны ли данные группы.
        :rtype: bool
        """
        # Проверка наличия необходимых полей в данных группы
        if not all(
            hasattr(group, attr) for attr in ["name", "url"]
        ):
            logger.error(
                f"Не хватает обязательных полей в данных группы {group=}, "
                "необходимо как минимум `name` и `url`"
            )
            return False
        return True
```
```python
# Документация модуля Facebook Promoter
#
# ## Обзор
#
# Модуль **Facebook Promoter** автоматизирует продвижение товаров и мероприятий AliExpress в группах Facebook. Модуль управляет публикациями рекламных материалов на Facebook, избегая дублирования. Для эффективного продвижения используется WebDriver для автоматизации браузера.
#
# ## Особенности модуля
#
# - Продвижение категорий и мероприятий в группах Facebook.
# - Избежание дублирования публикаций через отслеживание уже опубликованных элементов.
# - Поддержка конфигурации данных групп через файлы.
# - Возможность отключения загрузки видео в публикациях.
#
# ## Требования
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
# ## Использование
#
# ### Пример использования класса FacebookPromoter
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
# ## Документация классов
#
# ### Класс `FacebookPromoter`
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
# #### Методы
#
# ##### `__init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False)`
#
# Инициализирует промоутер для Facebook с необходимыми конфигурациями.
#
# - **Аргументы:**
#     - `d (Driver)`: Экземпляр WebDriver для автоматизации.
#     - `promoter (str)`: Имя промоутера (например, "aliexpress").
#     - `group_file_paths (Optional[list[str | Path] | str | Path])`: Пути к файлам с данными групп.
#     - `no_video (bool)`: Флаг для отключения видео в публикациях. По умолчанию `False`.
#
# ##### `promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool`
#
# Продвигает категорию или мероприятие в указанной группе Facebook.
#
# - **Аргументы:**