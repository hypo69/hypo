# Документация модуля `promoter`

## Обзор

Модуль **Facebook Promoter** автоматизирует процесс продвижения товаров и событий AliExpress в группах Facebook. Он обеспечивает публикацию рекламных материалов в Facebook, гарантируя, что категории и события продвигаются без дубликатов. Модуль использует WebDriver для автоматизации браузера, что обеспечивает эффективное управление рекламными кампаниями.

## Особенности модуля

- Продвижение категорий и событий в группах Facebook.
- Предотвращение дублирования рекламных материалов путем отслеживания ранее продвигавшихся элементов.
- Поддержка настройки данных групп через файлы конфигурации.
- Возможность отключения загрузки видео в рекламных публикациях.

## Содержание

1. [Класс `FacebookPromoter`](#FacebookPromoter)
   - [`__init__`](#__init__)
   - [`promote`](#promote)
   - [`log_promotion_error`](#log_promotion_error)
   - [`update_group_promotion_data`](#update_group_promotion_data)
   - [`process_groups`](#process_groups)
   - [`get_category_item`](#get_category_item)
   - [`check_interval`](#check_interval)
   - [`validate_group`](#validate_group)
2. [Пример использования](#Пример-использования)

## Классы

### `FacebookPromoter`

**Описание**: Этот класс управляет процессом продвижения товаров и событий AliExpress в группах Facebook.

#### `__init__`

```python
def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False) -> None:
    """
    Args:
        d (Driver): Экземпляр WebDriver для автоматизации.
        promoter (str): Название промоутера (например, "aliexpress").
        group_file_paths (Optional[list[str | Path] | str | Path], optional): Пути к файлам с данными о группах. По умолчанию `None`.
        no_video (bool, optional): Флаг для отключения видео в постах. По умолчанию `False`.
    """
```

**Описание**: Инициализирует промоутер Facebook с необходимыми конфигурациями.

**Параметры**:

- `d` (Driver): Экземпляр WebDriver для автоматизации.
- `promoter` (str): Название промоутера (например, "aliexpress").
- `group_file_paths` (Optional[list[str | Path] | str | Path], optional): Пути к файлам с данными о группах. По умолчанию `None`.
- `no_video` (bool, optional): Флаг для отключения видео в постах. По умолчанию `False`.

#### `promote`

```python
def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
    """
    Args:
        group (SimpleNamespace): Данные группы.
        item (SimpleNamespace): Объект категории или события для продвижения.
        is_event (bool, optional): Указывает, является ли продвигаемый элемент событием. По умолчанию `False`.
        language (str, optional): Язык продвижения. По умолчанию `None`.
        currency (str, optional): Валюта для продвижения. По умолчанию `None`.

    Returns:
        bool: Указывает, было ли продвижение успешным.
    """
```

**Описание**: Продвигает категорию или событие в указанной группе Facebook.

**Параметры**:

- `group` (SimpleNamespace): Данные группы.
- `item` (SimpleNamespace): Объект категории или события для продвижения.
- `is_event` (bool, optional): Указывает, является ли продвигаемый элемент событием. По умолчанию `False`.
- `language` (str, optional): Язык продвижения. По умолчанию `None`.
- `currency` (str, optional): Валюта для продвижения. По умолчанию `None`.

**Возвращает**:

- `bool`: `True`, если продвижение прошло успешно, иначе `False`.

#### `log_promotion_error`

```python
def log_promotion_error(self, is_event: bool, item_name: str) -> None:
    """
    Args:
        is_event (bool): Указывает, является ли элемент событием.
        item_name (str): Название элемента.
    """
```

**Описание**: Регистрирует ошибку при неудачном продвижении.

**Параметры**:

- `is_event` (bool): Указывает, является ли элемент событием.
- `item_name` (str): Название элемента.

#### `update_group_promotion_data`

```python
def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False) -> None:
    """
    Args:
        group (SimpleNamespace): Данные группы.
        item_name (str): Название элемента, который был продвинут.
        is_event (bool, optional): Указывает, является ли элемент событием. По умолчанию `False`.
    """
```

**Описание**: Обновляет данные группы после продвижения, добавляя продвинутый элемент в список продвинутых категорий или событий.

**Параметры**:

- `group` (SimpleNamespace): Данные группы.
- `item_name` (str): Название элемента, который был продвинут.
- `is_event` (bool, optional): Указывает, является ли элемент событием. По умолчанию `False`.

#### `process_groups`

```python
def process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None) -> None:
    """
    Args:
        campaign_name (str, optional): Название кампании. По умолчанию `None`.
        events (list[SimpleNamespace], optional): Список событий для продвижения. По умолчанию `None`.
        is_event (bool, optional): Указывает, нужно ли продвигать события или категории. По умолчанию `False`.
        group_file_paths (list[str], optional): Пути к файлам с данными о группах. По умолчанию `None`.
        group_categories_to_adv (list[str], optional): Список категорий для продвижения. По умолчанию `['sales']`.
        language (str, optional): Язык продвижения. По умолчанию `None`.
        currency (str, optional): Валюта для продвижения. По умолчанию `None`.
    """
```

**Описание**: Обрабатывает группы для продвижения текущей кампании или события.

**Параметры**:

- `campaign_name` (str, optional): Название кампании. По умолчанию `None`.
- `events` (list[SimpleNamespace], optional): Список событий для продвижения. По умолчанию `None`.
- `is_event` (bool, optional): Указывает, нужно ли продвигать события или категории. По умолчанию `False`.
- `group_file_paths` (list[str], optional): Пути к файлам с данными о группах. По умолчанию `None`.
- `group_categories_to_adv` (list[str], optional): Список категорий для продвижения. По умолчанию `['sales']`.
- `language` (str, optional): Язык продвижения. По умолчанию `None`.
- `currency` (str, optional): Валюта для продвижения. По умолчанию `None`.

#### `get_category_item`

```python
def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace:
    """
    Args:
        campaign_name (str): Название кампании.
        group (SimpleNamespace): Данные группы.
        language (str): Язык продвижения.
        currency (str): Валюта для продвижения.

    Returns:
        SimpleNamespace: Элемент категории для продвижения.
    """
```

**Описание**: Получает элемент категории для продвижения на основе кампании и промоутера.

**Параметры**:

- `campaign_name` (str): Название кампании.
- `group` (SimpleNamespace): Данные группы.
- `language` (str): Язык продвижения.
- `currency` (str): Валюта для продвижения.

**Возвращает**:

- `SimpleNamespace`: Элемент категории для продвижения.

#### `check_interval`

```python
def check_interval(self, group: SimpleNamespace) -> bool:
    """
    Args:
        group (SimpleNamespace): Данные группы.

    Returns:
        bool: Указывает, достаточно ли времени прошло для повторного продвижения в этой группе.
    """
```

**Описание**: Проверяет, достаточно ли времени прошло для повторного продвижения в этой группе.

**Параметры**:

- `group` (SimpleNamespace): Данные группы.

**Возвращает**:

- `bool`: `True`, если группа подходит для продвижения, иначе `False`.

#### `validate_group`

```python
def validate_group(self, group: SimpleNamespace) -> bool:
    """
    Args:
        group (SimpleNamespace): Данные группы.

    Returns:
        bool: Указывает, являются ли данные группы валидными.
    """
```

**Описание**: Проверяет данные группы, чтобы убедиться, что они имеют необходимые атрибуты.

**Параметры**:

- `group` (SimpleNamespace): Данные группы.

**Возвращает**:

- `bool`: `True`, если данные группы валидны, иначе `False`.

## Пример использования

### Пример использования класса `FacebookPromoter`

```python
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns

# Настройка экземпляра WebDriver (замените фактическим WebDriver)
d = Driver()

# Создание экземпляра класса FacebookPromoter
promoter = FacebookPromoter(
    d=d, 
    promoter="aliexpress", 
    group_file_paths=["path/to/group/file1.json", "path/to/group/file2.json"]
)

# Запуск продвижения товаров или событий
promoter.process_groups(
    campaign_name="Campaign1",
    events=[], 
    group_categories_to_adv=["sales"],
    language="en",
    currency="USD"
)
```