# Анализ кода модуля `promoter.ru.md`

**Качество кода**
7
- Плюсы
    - Код хорошо структурирован и документирован с использованием Markdown.
    - Присутствует описание основных функций и классов.
    - Есть пример использования класса `FacebookPromoter`.
    - Представлена диаграмма `mermaid` для наглядности процесса.
- Минусы
    - Отсутствуют docstring в формате reStructuredText (RST) в коде Python, что является обязательным требованием.
    - Не используются `j_loads` или `j_loads_ns` для чтения файлов.
    - Не добавлены необходимые импорты, такие как `Optional`, `Path`, `Any`.
    - Отсутствует обработка ошибок с использованием `logger.error`.
    - Код не соответствует PEP8.

**Рекомендации по улучшению**
1.  **Переписать документацию в формате reStructuredText (RST)**: Необходимо переписать всю документацию в формате RST, включая docstring для классов и функций.
2.  **Использовать `j_loads_ns` для чтения файлов**: Заменить стандартный `json.load` на `j_loads_ns` из `src.utils.jjson`.
3.  **Добавить импорты**: Добавить недостающие импорты `Optional`, `Path`, `Any`, `List`, `Union` и `SimpleNamespace` из `types`.
4.  **Использовать `logger.error`**: Внедрить `logger.error` для обработки исключений вместо общих блоков `try-except`.
5.  **Рефакторинг кода**: Необходимо провести рефакторинг кода, приведя его к стандартам PEP8.
6.  **Добавить комментарии в стиле reStructuredText (RST)**: Добавить подробные комментарии в стиле RST к каждому блоку кода, включая описания переменных.

**Оптимизированный код**
```python
"""
Модуль для автоматизации продвижения товаров и мероприятий AliExpress в группах Facebook.
=========================================================================================

Этот модуль содержит класс :class:`FacebookPromoter`, который используется для управления
публикациями рекламных материалов на Facebook, избегая дублирования.

Пример использования
--------------------

Пример использования класса `FacebookPromoter`:

.. code-block:: python

    from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
    from src.webdriver.driver import Driver
    from src.utils.jjson import j_loads_ns
    from pathlib import Path

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
from typing import Optional, List, Union, Any
from pathlib import Path
import random
from datetime import datetime, timedelta
from urllib.parse import urlparse, parse_qs
from types import SimpleNamespace

# from src.utils.jjson import j_loads
from src.utils.jjson import j_loads_ns  # Используем j_loads_ns
from src.webdriver.driver import Driver
from src.logger.logger import logger  # Импорт logger


class FacebookPromoter:
    """
    Управляет процессом продвижения товаров и мероприятий AliExpress в группах Facebook.
    """

    def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[Union[List[Union[str, Path]], str, Path]] = None, no_video: bool = False) -> None:
        """
        Инициализирует промоутер для Facebook с необходимыми конфигурациями.

        :param d: Экземпляр WebDriver для автоматизации.
        :type d: Driver
        :param promoter: Имя промоутера (например, "aliexpress").
        :type promoter: str
        :param group_file_paths: Пути к файлам с данными групп.
        :type group_file_paths: Optional[Union[List[Union[str, Path]], str, Path]]
        :param no_video: Флаг для отключения видео в публикациях.
        :type no_video: bool
        """
        self.driver = d  # Экземпляр WebDriver для управления браузером
        self.promoter = promoter  # Название промоутера
        self.group_file_paths = group_file_paths  # Пути к файлам с данными групп
        self.no_video = no_video  # Флаг для отключения загрузки видео
        self.groups = []  # Список для хранения данных групп
        self._load_groups()  # Вызов метода для загрузки данных групп

    def _load_groups(self) -> None:
        """
        Загружает данные групп из указанных файлов.
        """
        if not self.group_file_paths:
            return
        
        # Проверяем, является ли group_file_paths списком
        if isinstance(self.group_file_paths, list):
           
           for file_path in self.group_file_paths:
               # Проверяем, является ли путь строкой или Path
                if isinstance(file_path, (str, Path)):
                    try:
                         #  Загружает данные из файла JSON, используя j_loads_ns.
                        group_data = j_loads_ns(file_path)
                        #  Если group_data существует и не является None, добавляет его в список групп.
                        if group_data:
                             self.groups.append(group_data)
                    except Exception as e:
                        logger.error(f"Ошибка при загрузке файла группы {file_path}: {e}")
                
        elif isinstance(self.group_file_paths, (str, Path)):
            try:
                #  Загружает данные из файла JSON, используя j_loads_ns.
                group_data = j_loads_ns(self.group_file_paths)
                #  Если group_data существует и не является None, добавляет его в список групп.
                if group_data:
                     self.groups.append(group_data)
            except Exception as e:
                logger.error(f"Ошибка при загрузке файла группы {self.group_file_paths}: {e}")


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
        :type language: Optional[str]
        :param currency: Валюта для продвижения.
        :type currency: Optional[str]
        :return: Успешно ли прошло продвижение.
        :rtype: bool
        """
        try:
            #  Код выполняет проверку, является ли элемент мероприятием, и присваивает соответствующее значение переменной item_name.
            item_name = item.event_name if is_event else item.category_name
            logger.info(f'Начинается продвижение {item_name} в группе: {group.group_name}')

            #  Код определяет, нужно ли отключать видео в публикации, основываясь на значении self.no_video.
            no_video = 'no_video' if self.no_video else ''
            #  Код выполняет подготовку URL для публикации, заменяя параметры в url и добавляя параметры языка и валюты, если они заданы.
            url = group.post_url.format(item.url, no_video, language=language or '', currency=currency or '')
            #  Код открывает URL в браузере, используя WebDriver.
            self.driver.get(url)
            
            #  Код ожидает, пока появится элемент с локатором group.post_locator.
            self.driver.wait_for_element(group.post_locator)
            #  Код нажимает на элемент с локатором group.post_locator.
            self.driver.click(group.post_locator)
            #  Код ожидает некоторое время для завершения публикации.
            self.driver.sleep(random.randint(3, 7))
            #  Код регистрирует успешное продвижение.
            logger.info(f'Успешно продвинуто {item_name} в группе: {group.group_name}')
            #  Код возвращает True, указывая на успешное продвижение.
            return True
        except Exception as e:
             #  Код регистрирует ошибку, если продвижение не удалось.
            logger.error(f'Ошибка продвижения {item_name} в группе: {group.group_name}: {e}')
            #  Код вызывает метод для регистрации ошибки продвижения.
            self.log_promotion_error(is_event, item_name)
            return False
    

    def log_promotion_error(self, is_event: bool, item_name: str) -> None:
        """
        Записывает ошибку, если продвижение не удалось.

        :param is_event: Является ли элемент мероприятием.
        :type is_event: bool
        :param item_name: Название элемента.
        :type item_name: str
        """
        item_type = "мероприятия" if is_event else "категории" # Определяет тип элемента
        logger.error(f'Не удалось продвинуть {item_type}: {item_name}') #  Логирует ошибку продвижения с указанием типа и названия элемента.
    
    def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False) -> None:
        """
        Обновляет данные группы после продвижения, добавляя продвигаемый элемент
        в список продвигаемых категорий или мероприятий.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :param item_name: Название продвигаемого элемента.
        :type item_name: str
        :param is_event: Является ли элемент мероприятием.
        :type is_event: bool
        """
        if is_event:
            if not hasattr(group, 'promoted_events'):
                group.promoted_events = [] # Если атрибут 'promoted_events' не существует, он создается как пустой список.
            group.promoted_events.append(item_name) # Добавляет имя элемента в список продвинутых событий.
        else:
            if not hasattr(group, 'promoted_categories'):
                group.promoted_categories = [] # Если атрибут 'promoted_categories' не существует, он создается как пустой список.
            group.promoted_categories.append(item_name) # Добавляет имя элемента в список продвинутых категорий.
        
        logger.debug(f'Обновлены данные группы {group.group_name} после продвижения {item_name}') # Логирует обновление данных группы.

    def process_groups(self, campaign_name: str = None, events: List[SimpleNamespace] = None, is_event: bool = False,
                       group_file_paths: List[str] = None, group_categories_to_adv: List[str] = ['sales'],
                       language: str = None, currency: str = None) -> None:
        """
        Обрабатывает группы для текущей кампании или продвижения мероприятия.

        :param campaign_name: Название кампании.
        :type campaign_name: Optional[str]
        :param events: Список мероприятий для продвижения.
        :type events: Optional[List[SimpleNamespace]]
        :param is_event: Является ли продвижение мероприятий или категорий.
        :type is_event: bool
        :param group_file_paths: Пути к файлам с данными групп.
        :type group_file_paths: Optional[List[str]]
        :param group_categories_to_adv: Категории для продвижения.
        :type group_categories_to_adv: List[str]
        :param language: Язык публикации.
        :type language: Optional[str]
        :param currency: Валюта для продвижения.
        :type currency: Optional[str]
        """
        # Если переданы пути к файлам групп,  обновляет пути к файлам групп.
        if group_file_paths:
            self.group_file_paths = group_file_paths
            self._load_groups()
        
        # Если список групп пуст, выходит из функции
        if not self.groups:
            logger.warning('Нет групп для обработки.')
            return
        
        #  Код обрабатывает каждую группу в списке.
        for group in self.groups:
            #  Код проверяет валидность данных группы.
            if not self.validate_group(group):
                continue
            # Код определяет элементы для продвижения, основываясь на том, являются ли они событиями или категориями.
            items = events if is_event else group_categories_to_adv
            if not items:
                logger.warning(f"Нет элементов для продвижения в группе: {group.group_name}")
                continue
            
            #  Код проходит по каждому элементу для продвижения.
            for item in items:
                  #  Код получает элемент для продвижения.
                item_to_promote = self.get_category_item(campaign_name, group, language, currency) if not is_event else item
                # Если item_to_promote равен None, пропускает текущую итерацию
                if item_to_promote is None:
                      logger.debug(f"Нет элемента для продвижения в группе: {group.group_name}")
                      continue
                #  Код проверяет, можно ли продвигать группу на основе временного интервала.
                if not self.check_interval(group):
                    continue
                #  Код выполняет продвижение элемента.
                if self.promote(group, item_to_promote, is_event, language, currency):
                    #  Код обновляет данные группы после успешного продвижения.
                     self.update_group_promotion_data(group,item_to_promote.category_name if not is_event else item_to_promote.event_name, is_event)
                    

    def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> Optional[SimpleNamespace]:
        """
        Получает элемент категории для продвижения в зависимости от кампании и промоутера.

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param group: Данные группы.
        :type group: SimpleNamespace
        :param language: Язык для публикации.
        :type language: Optional[str]
        :param currency: Валюта для публикации.
        :type currency: Optional[str]
        :return: Элемент категории для продвижения.
        :rtype: Optional[SimpleNamespace]
        """
        #  Код формирует имя файла на основе имени кампании и промоутера.
        file_name = f'{campaign_name}-{self.promoter}-{language}-{currency}.json' if campaign_name else f'{self.promoter}-{language}-{currency}.json'
        #  Код формирует путь к файлу данных категорий.
        file_path = Path('src', 'data', 'categories', file_name)
        try:
            #  Код загружает данные из файла JSON, используя j_loads_ns.
            categories_data = j_loads_ns(file_path)
            if not categories_data:
                logger.warning(f'Нет данных категорий в файле: {file_path}')
                return None

            #  Код фильтрует категории, исключая те, которые уже были продвинуты в этой группе.
            available_categories = [
                cat for cat in categories_data.categories
                if not hasattr(group, 'promoted_categories') or cat.category_name not in group.promoted_categories
            ]
            # Если доступных категорий нет, возвращает None
            if not available_categories:
                  logger.debug(f'Нет доступных категорий для группы: {group.group_name}')
                  return None

            #  Код выбирает случайную категорию из доступных.
            category = random.choice(available_categories)
            logger.debug(f'Выбрана категория {category.category_name} для группы {group.group_name}')
            return category
        except Exception as e:
            logger.error(f'Ошибка при загрузке или выборе категории из файла: {file_path}: {e}')
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
            group.last_promotion_time = datetime.min
        
        #  Код определяет интервал между продвижениями.
        interval = timedelta(seconds=group.interval)
        #  Код вычисляет время, когда можно снова продвигать группу.
        next_promotion_time = group.last_promotion_time + interval
        
        #  Код проверяет, прошло ли достаточно времени с последнего продвижения.
        if datetime.now() >= next_promotion_time:
            group.last_promotion_time = datetime.now()
            logger.debug(f'Интервал продвижения для группы {group.group_name} пройден')
            return True
        else:
           logger.debug(f'Интервал продвижения для группы {group.group_name} не пройден. Следующее продвижение возможно после {next_promotion_time}')
           return False


    def validate_group(self, group: SimpleNamespace) -> bool:
        """
        Проверяет данные группы, чтобы убедиться в их корректности.

        :param group: Данные группы.
        :type group: SimpleNamespace
        :return: Корректны ли данные группы.
        :rtype: bool
        """
        #  Код проверяет наличие необходимых атрибутов в данных группы.
        if not all(hasattr(group, attr) for attr in ['group_name', 'post_url', 'post_locator', 'interval']):
             logger.error(f'Некорректные данные группы: {group}')
             return False

        # Код проверяет корректность URL
        try:
            result = urlparse(group.post_url)
            if not all([result.scheme, result.netloc]):
                logger.error(f'Некорректный URL в данных группы: {group.post_url}')
                return False
        except Exception as e:
             logger.error(f'Ошибка проверки URL {group.post_url}: {e}')
             return False

        #  Код проверяет, является ли интервал числом.
        if not isinstance(group.interval, (int, float)):
            logger.error(f'Некорректный интервал в данных группы: {group.interval}')
            return False
        
        #  Код проверяет, является ли post_locator строкой
        if not isinstance(group.post_locator, str):
            logger.error(f'Некорректный локатор в данных группы: {group.post_locator}')
            return False
        logger.debug(f'Данные группы {group.group_name} валидны') #  Логирует, что данные группы корректны.
        return True
```