# Модуль: src.endpoints.advertisement.facebook.promoter

## Обзор

Модуль `promoter.py` предназначен для автоматизации продвижения (постинга) рекламных сообщений и событий в группах Facebook. Он включает в себя классы и функции для управления кампаниями, публикации контента и предотвращения дублирования рекламных материалов.

## Подробней

Этот модуль является частью системы автоматизации маркетинга в Facebook. Он использует WebDriver для управления браузером и взаимодействия с Facebook, а также включает функции для чтения данных о группах, создания рекламных постов и обработки исключений.

## Классы

### `FacebookPromoter`

**Описание**: Класс `FacebookPromoter` предназначен для продвижения товаров AliExpress и событий в группах Facebook. Он автоматизирует процесс постинга в группы Facebook, используя WebDriver, и обеспечивает продвижение категорий и событий, избегая дубликатов.

**Как работает класс**:
Класс инициализируется с драйвером WebDriver, списком путей к файлам групп и флагом для отключения видео в постах. Он содержит методы для продвижения контента в группах, логирования ошибок и обновления данных о продвижении.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `FacebookPromoter`.
- `promote`: Продвигает категорию или событие в группе Facebook.
- `log_promotion_error`: Логирует ошибки, возникающие при продвижении категорий или событий.
- `update_group_promotion_data`: Обновляет данные группы после успешной публикации рекламного материала.
- `process_groups`: Обрабатывает группы для текущей кампании или продвижения события.
- `get_category_item`: Получает категорию товара для продвижения на основе кампании и промоутера.
- `check_interval`: Проверяет, достаточно ли времени прошло для продвижения данной группы.
- `validate_group`: Проверяет, корректны ли данные группы.

**Параметры**:
- `d` (Driver): Экземпляр WebDriver для автоматизации браузера.
- `group_file_paths` (Optional[list[str | Path] | str | Path]): Список путей к файлам, содержащим данные о группах.
- `no_video` (bool, optional): Флаг для отключения видео в постах. По умолчанию `False`.

```python
class FacebookPromoter:
    """ Class for promoting AliExpress products and events in Facebook groups.
    
    This class automates the posting of promotions to Facebook groups using a WebDriver instance,
    ensuring that categories and events are promoted while avoiding duplicates.
    """
    d: Driver = None
    group_file_paths: str | Path = None
    no_video: bool = False
    promoter: str

    def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False):
        """ Initializes the promoter for Facebook groups.

        Args:
            d (Driver): WebDriver instance for browser automation.
            group_file_paths (list[str | Path] | str | Path): List of file paths containing group data.
            no_video (bool, optional): Flag to disable videos in posts. Defaults to False.
        """
        self.promoter = promoter
        self.d = d
        self.group_file_paths = group_file_paths if group_file_paths else get_filenames(gs.path.google_drive / 'facebook' / 'groups')
        self.no_video = no_video
        self.spinner = spinning_cursor()
```

### `__init__`

```python
    def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False):
        """ Initializes the promoter for Facebook groups.

        Args:
            d (Driver): WebDriver instance for browser automation.
            group_file_paths (list[str | Path] | str | Path): List of file paths containing group data.
            no_video (bool, optional): Flag to disable videos in posts. Defaults to False.
        """
        self.promoter = promoter
        self.d = d
        self.group_file_paths = group_file_paths if group_file_paths else get_filenames(gs.path.google_drive / 'facebook' / 'groups')
        self.no_video = no_video
        self.spinner = spinning_cursor()
```

**Описание**: Инициализирует экземпляр класса `FacebookPromoter`.

**Как работает функция**:
Метод инициализирует основные атрибуты класса, такие как драйвер WebDriver, пути к файлам групп и флаг отключения видео. Если пути к файлам групп не указаны, они извлекаются из директории Google Drive.

**Параметры**:
- `d` (Driver): Экземпляр WebDriver для автоматизации браузера.
- `promoter` (str): Название промоутера.
- `group_file_paths` (Optional[list[str | Path] | str | Path], optional): Список путей к файлам, содержащим данные о группах. По умолчанию `None`.
- `no_video` (bool, optional): Флаг для отключения видео в постах. По умолчанию `False`.

**Примеры**:

```python
from src.webdriver.driver import Driver
from pathlib import Path

# Пример инициализации FacebookPromoter с указанием путей к файлам групп
driver = Driver()
group_file_paths = [Path('path/to/group1.json'), Path('path/to/group2.json')]
promoter = FacebookPromoter(d=driver, promoter='my_promoter', group_file_paths=group_file_paths, no_video=True)

# Пример инициализации FacebookPromoter без указания путей к файлам групп
promoter = FacebookPromoter(d=driver, promoter='my_promoter', no_video=False)
```

### `promote`

```python
    def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
        """Promotes a category or event in a Facebook group.""" 
        ...
        if language:
           if group.language.upper() != language.upper():
                return
        if currency:
            if group.currency.upper() != currency.upper():
                return

        item_name = item.event_name if is_event else item.category_name
        ev_or_msg = getattr(item.language, group.language) if is_event else item

        # Установка атрибутов события или сообщения
        if is_event:
            ev_or_msg.start = item.start
            ev_or_msg.end = item.end
            ev_or_msg.promotional_link = item.promotional_link

            if not post_event(d=self.d, event=ev_or_msg):
                self.log_promotion_error(is_event, item_name)
                return
        else:
            if 'kazarinov' in self.promoter or 'emil' in self.promoter:
                if not post_ad(self.d, ev_or_msg):
                    return


            elif not post_message(d=self.d, message=ev_or_msg, no_video=self.no_video, without_captions=False):
                return

        # Обновление данных группы после публикации
        self.update_group_promotion_data(group, ev_or_msg.name)
        return True
```

**Описание**: Продвигает категорию или событие в группе Facebook.

**Как работает функция**:
Метод проверяет соответствие языка и валюты группы заданным параметрам. Затем, в зависимости от типа продвигаемого элемента (событие или категория), вызывается соответствующая функция для публикации контента. После успешной публикации данные группы обновляются.

**Параметры**:
- `group` (SimpleNamespace): Данные группы Facebook.
- `item` (SimpleNamespace): Данные о категории или событии для продвижения.
- `is_event` (bool, optional): Флаг, указывающий, является ли продвигаемый элемент событием. По умолчанию `False`.
- `language` (str, optional): Язык продвижения. По умолчанию `None`.
- `currency` (str, optional): Валюта продвижения. По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если продвижение прошло успешно, иначе `False`.

**Примеры**:

```python
from types import SimpleNamespace

# Пример продвижения события
group_data = SimpleNamespace(language='ru', currency='USD')
event_data = SimpleNamespace(event_name='Summer Party', language=SimpleNamespace(ru='Приглашаем на летнюю вечеринку'))
promoter = FacebookPromoter(d=driver, promoter='my_promoter')
success = promoter.promote(group=group_data, item=event_data, is_event=True, language='ru', currency='USD')
print(f"Promotion successful: {success}")

# Пример продвижения категории
category_data = SimpleNamespace(category_name='Shoes', language=SimpleNamespace(ru='Обувь'))
success = promoter.promote(group=group_data, item=category_data, is_event=False, language='ru', currency='USD')
print(f"Promotion successful: {success}")
```

### `log_promotion_error`

```python
    def log_promotion_error(self, is_event: bool, item_name: str):\
        """Logs promotion error for category or event."""
        logger.debug(f"Error while posting {'event' if is_event else 'category'} {item_name}", None, False)
```

**Описание**: Логирует ошибки, возникающие при продвижении категорий или событий.

**Как работает функция**:
Метод использует модуль `logger` для записи отладочного сообщения об ошибке продвижения. Сообщение содержит информацию о типе продвигаемого элемента (событие или категория) и его имени.

**Параметры**:
- `is_event` (bool): Флаг, указывающий, является ли продвигаемый элемент событием.
- `item_name` (str): Имя категории или события.

**Примеры**:

```python
# Пример логирования ошибки продвижения события
promoter = FacebookPromoter(d=driver, promoter='my_promoter')
promoter.log_promotion_error(is_event=True, item_name='Summer Party')

# Пример логирования ошибки продвижения категории
promoter.log_promotion_error(is_event=False, item_name='Shoes')
```

### `update_group_promotion_data`

```python
    def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):\
        """Updates group promotion data with the new promotion.""" 
        timestamp = datetime.now().strftime("%d/%m/%y %H:%M")
        group.last_promo_sended = gs.now
        if is_event:
            group.promoted_events = group.promoted_events if isinstance(group.promoted_events, list) else [group.promoted_events]
            group.promoted_events.append(item_name)
        else:
            group.promoted_categories = group.promoted_categories if isinstance(group.promoted_categories, list) else [group.promoted_categories]
            group.promoted_categories.append(item_name)
        group.last_promo_sended = timestamp
```

**Описание**: Обновляет данные группы после успешной публикации рекламного материала.

**Как работает функция**:
Метод обновляет атрибуты группы, такие как время последней отправки промо-материалов и список продвинутых категорий или событий. Он добавляет имя продвинутого элемента в соответствующий список и фиксирует текущее время.

**Параметры**:
- `group` (SimpleNamespace): Данные группы Facebook.
- `item_name` (str): Имя категории или события.
- `is_event` (bool, optional): Флаг, указывающий, является ли продвигаемый элемент событием. По умолчанию `False`.

**Примеры**:

```python
from types import SimpleNamespace

# Пример обновления данных группы после продвижения события
group_data = SimpleNamespace(promoted_events=['Old Event'], last_promo_sended='')
promoter = FacebookPromoter(d=driver, promoter='my_promoter')
promoter.update_group_promotion_data(group=group_data, item_name='Summer Party', is_event=True)
print(f"Updated group data: {group_data.promoted_events}, {group_data.last_promo_sended}")

# Пример обновления данных группы после продвижения категории
group_data = SimpleNamespace(promoted_categories=['Old Category'], last_promo_sended='')
promoter.update_group_promotion_data(group=group_data, item_name='Shoes', is_event=False)
print(f"Updated group data: {group_data.promoted_categories}, {group_data.last_promo_sended}")
```

### `process_groups`

```python
    def process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None):\
        """Processes all groups for the current campaign or event promotion."""    
        if not campaign_name and not events:
            logger.debug("Nothing to promote!")
            return

        for group_file in group_file_paths:
            path_to_group_file: Path = gs.path.google_drive / 'facebook' / 'groups' / group_file 
            groups_ns: dict = j_loads_ns(path_to_group_file)

            if not groups_ns:
                logger.error(f"Проблема в файле групп {group_file=}")
                return

            for group_url, group in vars(groups_ns).items():
                group.group_url = group_url

                if not is_event and not self.check_interval(group):
                    logger.debug(f"{campaign_name=}\n Interval in group: {group.group_url}", None, False)
                    continue

                if not set(group_categories_to_adv).intersection(group.group_categories if isinstance(group.group_categories, list) else [group.group_categories]) or not 'active' in group.status:
                    continue

                if not is_event:
                    item = self.get_category_item(campaign_name, group, language, currency)
                else:
                    random.shuffle(events)
                    item = events.pop()
                    

                if item.name in (group.promoted_events if is_event else group.promoted_categories):
                    logger.debug(f"Item already promoted")
                    continue

                if not group.language.upper() == language.upper() and group.currency.upper() == currency.upper():
                   continue

                self.driver.get_url(get_event_url(group.group_url) if is_event else group.group_url)

                if not self.promote(group = group, item = item, is_event = is_event, language = language, currency = currency):
                    continue

                j_dumps(groups_ns, path_to_group_file)
                t = random.randint(30, 420)
                print(f"sleeping {t} sec")
                time.sleep(t)
```

**Описание**: Обрабатывает группы для текущей кампании или продвижения события.

**Как работает функция**:
Метод перебирает файлы групп, загружает данные из каждого файла и обрабатывает каждую группу. Для каждой группы проверяется интервал между продвижениями, соответствие категорий и статуса группы. Затем выбирается категория или событие для продвижения, и выполняется продвижение.

**Параметры**:
- `campaign_name` (str, optional): Имя кампании. По умолчанию `None`.
- `events` (list[SimpleNamespace], optional): Список событий для продвижения. По умолчанию `None`.
- `is_event` (bool, optional): Флаг, указывающий, является ли продвижение событием. По умолчанию `False`.
- `group_file_paths` (list[str], optional): Список путей к файлам групп. По умолчанию `None`.
- `group_categories_to_adv` (list[str], optional): Список категорий групп для продвижения. По умолчанию `['sales']`.
- `language` (str, optional): Язык продвижения. По умолчанию `None`.
- `currency` (str, optional): Валюта продвижения. По умолчанию `None`.

**Примеры**:

```python
from types import SimpleNamespace

# Пример обработки групп для продвижения кампании
group_file_paths = ['group1.json', 'group2.json']
promoter = FacebookPromoter(d=driver, promoter='my_promoter')
promoter.process_groups(campaign_name='Summer Sales', group_file_paths=group_file_paths, language='ru', currency='USD')

# Пример обработки групп для продвижения событий
event1 = SimpleNamespace(name='Event 1')
event2 = SimpleNamespace(name='Event 2')
events = [event1, event2]
promoter.process_groups(events=events, is_event=True, group_file_paths=group_file_paths, language='ru', currency='USD')
```

### `get_category_item`

```python
    def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace:\
        """Fetches the category item for promotion based on the campaign and promoter."""    
        if self.promoter == 'aliexpress':
            from src.suppliers.aliexpress.campaign import AliCampaignEditor
            ce = AliCampaignEditor(campaign_name=campaign_name, language=group.language, currency=group.currency)
            list_categories = ce.list_categories
            random.shuffle(list_categories)
            category_name = list_categories.pop()
            item = ce.get_category(category_name)
            item.name = category_name
            item.products = ce.get_category_products(item.category_name)
        else:
            base_path = gs.path.google_drive / self.promoter / 'campaigns' / campaign_name
            adv: SimpleNamespace = j_loads_ns(base_path / f"{language}_{currency}.json")
            adv_categories = list(vars(adv.category).items())  # Преобразуем в список для перемешивания
            random.shuffle(adv_categories)  # Перемешиваем категории

            for ad_name, ad in adv_categories:
                ad.description = read_text_file(base_path / 'category' / ad_name / 'description.txt')
                if not ad.description:
                    logger.error(f"ошибка чтения файла", None, False)
                    continue
                item = ad
                item.name = ad_name
                _img = get_filenames(base_path / 'category' / ad_name / 'images')
                if _img:
                    _img = _img if isinstance(_img, str) else _img[0]  # Беру только первое изображение
                    item.img_path = Path(gs.path.local) / _img
        return item
```

**Описание**: Получает категорию товара для продвижения на основе кампании и промоутера.

**Как работает функция**:
Метод определяет источник кампании (например, AliExpress или другой источник) и загружает данные о категориях товаров. Для AliExpress используется класс `AliCampaignEditor` для получения категорий и продуктов. Для других источников данные загружаются из JSON-файла.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `group` (SimpleNamespace): Данные группы Facebook.
- `language` (str): Язык продвижения.
- `currency` (str): Валюта продвижения.

**Возвращает**:
- `SimpleNamespace`: Данные о категории товара для продвижения.

**Примеры**:

```python
from types import SimpleNamespace

# Пример получения категории товара для AliExpress
group_data = SimpleNamespace(language='ru', currency='USD')
promoter = FacebookPromoter(d=driver, promoter='aliexpress')
category_item = promoter.get_category_item(campaign_name='Summer Sales', group=group_data, language='ru', currency='USD')
print(f"Category item: {category_item}")

# Пример получения категории товара из другого источника
promoter = FacebookPromoter(d=driver, promoter='my_promoter')
category_item = promoter.get_category_item(campaign_name='Summer Campaign', group=group_data, language='ru', currency='USD')
print(f"Category item: {category_item}")
```

### `check_interval`

```python
    def check_interval(self, group: SimpleNamespace) -> bool:\
        """Checks if enough time has passed for promoting this group."""   
        ...
        return True
```

**Описание**: Проверяет, достаточно ли времени прошло для продвижения данной группы.

**Как работает функция**:
Метод проверяет, прошло ли достаточно времени с момента последнего продвижения в группе. Если интервал между продвижениями недостаточен, метод возвращает `False`, иначе `True`.

**Параметры**:
- `group` (SimpleNamespace): Данные группы Facebook.

**Возвращает**:
- `bool`: `True`, если достаточно времени прошло для продвижения, иначе `False`.

**Примеры**:

```python
from types import SimpleNamespace
from datetime import datetime, timedelta

# Пример проверки интервала, когда достаточно времени прошло
group_data = SimpleNamespace(last_promo_sended=datetime.now() - timedelta(days=30))
promoter = FacebookPromoter(d=driver, promoter='my_promoter')
can_promote = promoter.check_interval(group=group_data)
print(f"Can promote: {can_promote}")

# Пример проверки интервала, когда недостаточно времени прошло
group_data = SimpleNamespace(last_promo_sended=datetime.now() - timedelta(hours=1))
promoter = FacebookPromoter(d=driver, promoter='my_promoter')
can_promote = promoter.check_interval(group=group_data)
print(f"Can promote: {can_promote}")
```

### `validate_group`

```python
    def validate_group(self, group: SimpleNamespace) -> bool:\
        """Validates that the group data is correct."""   
        return group and hasattr(group, 'group_url') and hasattr(group, 'group_categories')
```

**Описание**: Проверяет, корректны ли данные группы.

**Как работает функция**:
Метод проверяет, существуют ли необходимые атрибуты (`group_url` и `group_categories`) в данных группы. Если все проверки пройдены, метод возвращает `True`, иначе `False`.

**Параметры**:
- `group` (SimpleNamespace): Данные группы Facebook.

**Возвращает**:
- `bool`: `True`, если данные группы корректны, иначе `False`.

**Примеры**:

```python
from types import SimpleNamespace

# Пример валидации корректных данных группы
group_data = SimpleNamespace(group_url='https://facebook.com/groups/123', group_categories=['sales'])
promoter = FacebookPromoter(d=driver, promoter='my_promoter')
is_valid = promoter.validate_group(group=group_data)
print(f"Is valid: {is_valid}")

# Пример валидации некорректных данных группы
group_data = SimpleNamespace(group_url='https://facebook.com/groups/123')
promoter = FacebookPromoter(d=driver, promoter='my_promoter')
is_valid = promoter.validate_group(group=group_data)
print(f"Is valid: {is_valid}")
```

## Функции

### `get_event_url`

```python
def get_event_url(group_url: str) -> str:
    """
    Returns the modified URL for creating an event on Facebook, replacing `group_id` with the value from the input URL.

    Args:
        group_url (str): Facebook group URL containing `group_id`.

    Returns:
        str: Modified URL for creating the event.
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
```

**Описание**: Возвращает измененный URL для создания события на Facebook, заменяя `group_id` значением из входного URL.

**Как работает функция**:
Функция извлекает `group_id` из URL группы Facebook, формирует параметры запроса и возвращает URL для создания события.

**Параметры**:
- `group_url` (str): URL группы Facebook, содержащий `group_id`.

**Возвращает**:
- `str`: Измененный URL для создания события.

**Примеры**:

```python
# Пример получения URL для создания события
group_url = "https://www.facebook.com/groups/123456789"
event_url = get_event_url(group_url)
print(f"Event URL: {event_url}")
```