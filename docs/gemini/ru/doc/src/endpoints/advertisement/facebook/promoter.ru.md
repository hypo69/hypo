# Документация модуля Facebook Promoter

## Обзор

Модуль **Facebook Promoter** автоматизирует продвижение товаров и мероприятий AliExpress в группах Facebook. Модуль управляет публикациями рекламных материалов на Facebook, избегая дублирования. Для эффективного продвижения используется WebDriver для автоматизации браузера.

## Оглавление

- [Особенности модуля](#особенности-модуля)
- [Требования](#требования)
- [Использование](#использование)
  - [Пример использования класса FacebookPromoter](#пример-использования-класса-facebookpromoter)
- [Документация классов](#документация-классов)
  - [Класс `FacebookPromoter`](#класс-facebookpromoter)
    - [Методы](#методы)
      - [`__init__`](#__init__self-d-driver-promoter-str-group_file_paths-optionalliststr--path--str--path--none-no_video-bool--false)
      - [`promote`](#promoteself-group-simplenamespace-item-simplenamespace-is_event-bool--false-language-str--none-currency-str--none--bool)
      - [`log_promotion_error`](#log_promotion_errorself-is_event-bool-item_name-str)
      - [`update_group_promotion_data`](#update_group_promotion_dataself-group-simplenamespace-item_name-str-is_event-bool--false)
      - [`process_groups`](#process_groupsself-campaign_name-str--none-events-listsimplenamespace--none-is_event-bool--false-group_file_paths-liststr--none-group_categories_to_adv-liststr--sales-language-str--none-currency-str--none)
      - [`get_category_item`](#get_category_itemself-campaign_name-str-group-simplenamespace-language-str-currency-str--simplenamespace)
      - [`check_interval`](#check_intervalself-group-simplenamespace--bool)
      - [`validate_group`](#validate_groupself-group-simplenamespace--bool)
- [Лицензия](#лицензия)

## Особенности модуля

- Продвижение категорий и мероприятий в группах Facebook.
- Избежание дублирования публикаций через отслеживание уже опубликованных элементов.
- Поддержка конфигурации данных групп через файлы.
- Возможность отключения загрузки видео в публикациях.

## Требования

- **Python** 3.x
- Необходимые библиотеки:
  - `random`
  - `datetime`
  - `pathlib`
  - `urllib.parse`
  - `types.SimpleNamespace`
  - `src` (пользовательский модуль)

## Использование

### Пример использования класса FacebookPromoter

```python
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
```

## Документация классов

### Класс `FacebookPromoter`

**Описание**: Этот класс управляет процессом продвижения товаров и мероприятий AliExpress в группах Facebook.

#### Методы

##### `__init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False)`

```python
def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False):
    """
    Инициализирует промоутер для Facebook с необходимыми конфигурациями.

    Args:
        d (Driver): Экземпляр WebDriver для автоматизации.
        promoter (str): Имя промоутера (например, "aliexpress").
        group_file_paths (Optional[list[str | Path] | str | Path]): Пути к файлам с данными групп.
        no_video (bool): Флаг для отключения видео в публикациях. По умолчанию `False`.
    """
```

**Описание**: Инициализирует промоутер для Facebook с необходимыми конфигурациями.

**Параметры**:
- `d` (Driver): Экземпляр WebDriver для автоматизации.
- `promoter` (str): Имя промоутера (например, "aliexpress").
- `group_file_paths` (Optional[list[str | Path] | str | Path], optional): Пути к файлам с данными групп. По умолчанию `None`.
- `no_video` (bool, optional): Флаг для отключения видео в публикациях. По умолчанию `False`.

**Примеры**:
- Пример инициализации класса:

```python
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver

# Пример использования с минимальными параметрами
d = Driver()
promoter = FacebookPromoter(d=d, promoter='aliexpress')

# Пример использования с указанием путей к файлам групп
group_file_paths = ['path/to/group1.json', 'path/to/group2.json']
promoter = FacebookPromoter(d=d, promoter='aliexpress', group_file_paths=group_file_paths)

# Пример использования с отключением видео
promoter = FacebookPromoter(d=d, promoter='aliexpress', no_video=True)
```

##### `promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool`

```python
def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
    """
    Продвигает категорию или мероприятие в указанной группе Facebook.

    Args:
        group (SimpleNamespace): Данные группы.
        item (SimpleNamespace): Категория или мероприятие для продвижения.
        is_event (bool): Является ли элемент мероприятием.
        language (str): Язык публикации.
        currency (str): Валюта для продвижения.

    Returns:
        bool: Успешно ли прошло продвижение.
    """
```

**Описание**: Продвигает категорию или мероприятие в указанной группе Facebook.

**Параметры**:
- `group` (SimpleNamespace): Данные группы.
- `item` (SimpleNamespace): Категория или мероприятие для продвижения.
- `is_event` (bool, optional): Является ли элемент мероприятием. По умолчанию `False`.
- `language` (str, optional): Язык публикации. По умолчанию `None`.
- `currency` (str, optional): Валюта для продвижения. По умолчанию `None`.

**Возвращает**:
- `bool`: Успешно ли прошло продвижение.

**Примеры**:
- Пример вызова функции:

```python
from types import SimpleNamespace
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver

# Инициализация необходимых объектов (замените на реальные данные)
d = Driver()
promoter = FacebookPromoter(d=d, promoter='aliexpress')
group = SimpleNamespace(id='test_group', name='Test Group')
item = SimpleNamespace(id='test_item', name='Test Item')

# Вызов метода promote
success = promoter.promote(group=group, item=item, is_event=False, language='en', currency='USD')
print(f"Promotion successful: {success}")
```

##### `log_promotion_error(self, is_event: bool, item_name: str)`

```python
def log_promotion_error(self, is_event: bool, item_name: str):
    """
    Записывает ошибку, если продвижение не удалось.

    Args:
        is_event (bool): Является ли элемент мероприятием.
        item_name (str): Название элемента.
    """
```

**Описание**: Записывает ошибку, если продвижение не удалось.

**Параметры**:
- `is_event` (bool): Является ли элемент мероприятием.
- `item_name` (str): Название элемента.

**Примеры**:
- Пример вызова функции:

```python
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver

# Инициализация объекта промоутера
d = Driver()
promoter = FacebookPromoter(d=d, promoter='aliexpress')

# Вызов метода log_promotion_error
promoter.log_promotion_error(is_event=True, item_name='Test Event')
promoter.log_promotion_error(is_event=False, item_name='Test Category')
```

##### `update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False)`

```python
def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
    """
    Обновляет данные группы после продвижения, добавляя продвигаемый элемент в список продвигаемых категорий или мероприятий.

    Args:
        group (SimpleNamespace): Данные группы.
        item_name (str): Название продвигаемого элемента.
        is_event (bool): Является ли элемент мероприятием.
    """
```

**Описание**: Обновляет данные группы после продвижения, добавляя продвигаемый элемент в список продвигаемых категорий или мероприятий.

**Параметры**:
- `group` (SimpleNamespace): Данные группы.
- `item_name` (str): Название продвигаемого элемента.
- `is_event` (bool, optional): Является ли элемент мероприятием. По умолчанию `False`.

**Примеры**:
- Пример вызова функции:

```python
from types import SimpleNamespace
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver

# Инициализация объектов
d = Driver()
promoter = FacebookPromoter(d=d, promoter='aliexpress')
group = SimpleNamespace(promoted_categories=[], promoted_events=[])
item_name = 'Test Item'

# Вызов метода update_group_promotion_data для категории
promoter.update_group_promotion_data(group=group, item_name=item_name, is_event=False)
print(f"Updated group data for category: {group}")

# Вызов метода update_group_promotion_data для мероприятия
promoter.update_group_promotion_data(group=group, item_name=item_name, is_event=True)
print(f"Updated group data for event: {group}")
```

##### `process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None)`

```python
def process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None):
    """
    Обрабатывает группы для текущей кампании или продвижения мероприятия.

    Args:
        campaign_name (str): Название кампании.
        events (list[SimpleNamespace]): Список мероприятий для продвижения.
        is_event (bool): Является ли продвижение мероприятий или категорий.
        group_file_paths (list[str]): Пути к файлам с данными групп.
        group_categories_to_adv (list[str]): Категории для продвижения.
        language (str): Язык публикации.
        currency (str): Валюта для продвижения.
    """
```

**Описание**: Обрабатывает группы для текущей кампании или продвижения мероприятия.

**Параметры**:
- `campaign_name` (str, optional): Название кампании. По умолчанию `None`.
- `events` (list[SimpleNamespace], optional): Список мероприятий для продвижения. По умолчанию `None`.
- `is_event` (bool, optional): Является ли продвижение мероприятий или категорий. По умолчанию `False`.
- `group_file_paths` (list[str], optional): Пути к файлам с данными групп. По умолчанию `None`.
- `group_categories_to_adv` (list[str], optional): Категории для продвижения. По умолчанию `['sales']`.
- `language` (str, optional): Язык публикации. По умолчанию `None`.
- `currency` (str, optional): Валюта для продвижения. По умолчанию `None`.

**Примеры**:
- Пример вызова функции:

```python
from types import SimpleNamespace
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver

# Инициализация объектов
d = Driver()
promoter = FacebookPromoter(d=d, promoter='aliexpress')
events = [SimpleNamespace(id='event1', name='Event 1'), SimpleNamespace(id='event2', name='Event 2')]
group_file_paths = ['path/to/group1.json', 'path/to/group2.json']
group_categories_to_adv = ['sales', 'deals']

# Вызов метода process_groups для продвижения мероприятий
promoter.process_groups(events=events, is_event=True, language='en', currency='USD')

# Вызов метода process_groups для продвижения категорий
promoter.process_groups(campaign_name='SummerSale', group_file_paths=group_file_paths, group_categories_to_adv=group_categories_to_adv, language='en', currency='USD')
```

##### `get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace`

```python
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
```

**Описание**: Получает элемент категории для продвижения в зависимости от кампании и промоутера.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `group` (SimpleNamespace): Данные группы.
- `language` (str): Язык для публикации.
- `currency` (str): Валюта для публикации.

**Возвращает**:
- `SimpleNamespace`: Элемент категории для продвижения.

**Примеры**:
- Пример вызова функции:

```python
from types import SimpleNamespace
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver

# Инициализация объектов (замените на реальные данные)
d = Driver()
promoter = FacebookPromoter(d=d, promoter='aliexpress')
group = SimpleNamespace(id='test_group', name='Test Group')

# Вызов метода get_category_item
category_item = promoter.get_category_item(campaign_name='SummerSale', group=group, language='en', currency='USD')
print(f"Category item to promote: {category_item}")
```

##### `check_interval(self, group: SimpleNamespace) -> bool`

```python
def check_interval(self, group: SimpleNamespace) -> bool:
    """
    Проверяет, прошло ли достаточно времени, чтобы снова продвигать эту группу.

    Args:
        group (SimpleNamespace): Данные группы.

    Returns:
        bool: Можно ли снова продвигать группу.
    """
```

**Описание**: Проверяет, прошло ли достаточно времени, чтобы снова продвигать эту группу.

**Параметры**:
- `group` (SimpleNamespace): Данные группы.

**Возвращает**:
- `bool`: Можно ли снова продвигать группу.

**Примеры**:
- Пример вызова функции:

```python
from types import SimpleNamespace
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver
import datetime

# Инициализация объектов
d = Driver()
promoter = FacebookPromoter(d=d, promoter='aliexpress')
group = SimpleNamespace(last_promotion_time=datetime.datetime.now() - datetime.timedelta(hours=24))

# Вызов метода check_interval
can_promote = promoter.check_interval(group=group)
print(f"Can promote group: {can_promote}")
```

##### `validate_group(self, group: SimpleNamespace) -> bool`

```python
def validate_group(self, group: SimpleNamespace) -> bool:
    """
    Проверяет данные группы, чтобы убедиться в их корректности.

    Args:
        group (SimpleNamespace): Данные группы.

    Returns:
        bool: Корректны ли данные группы.
    """
```

**Описание**: Проверяет данные группы, чтобы убедиться в их корректности.

**Параметры**:
- `group` (SimpleNamespace): Данные группы.

**Возвращает**:
- `bool`: Корректны ли данные группы.

**Примеры**:
- Пример вызова функции:

```python
from types import SimpleNamespace
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver

# Инициализация объектов (замените на реальные данные)
d = Driver()
promoter = FacebookPromoter(d=d, promoter='aliexpress')
group = SimpleNamespace(id='test_group', name='Test Group', url='https://www.facebook.com/groups/test_group')

# Вызов метода validate_group
is_valid = promoter.validate_group(group=group)
print(f"Is group valid: {is_valid}")
```

## Лицензия

Модуль является частью пакета **Facebook Promoter** и лицензируется по лицензии MIT.