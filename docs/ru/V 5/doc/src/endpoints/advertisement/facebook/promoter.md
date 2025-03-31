# Модуль Facebook Promoter

## Обзор

Модуль **Facebook Promoter** автоматизирует продвижение товаров и событий AliExpress в группах Facebook. Он отвечает за публикацию рекламных акций в Facebook, обеспечивая продвижение категорий и событий без дубликатов. Для эффективного управления рекламными акциями модуль использует WebDriver для автоматизации браузера.

## Подробней

Этот модуль предназначен для автоматизации процесса продвижения товаров и событий AliExpress в группах Facebook. Он позволяет указывать группы для продвижения, категории товаров и событий, а также обеспечивает отслеживание уже продвинутых элементов, чтобы избежать повторных публикаций. Модуль использует WebDriver для взаимодействия с Facebook через браузер, что позволяет автоматизировать такие задачи, как вход в систему, публикация сообщений и загрузка медиафайлов.

## Содержание

- [Класс `FacebookPromoter`](#класс-facebookpromoter)
    - [Описание](#описание)
    - [Методы](#методы)
        - [`__init__`](#__init__)
        - [`promote`](#promote)
        - [`log_promotion_error`](#log_promotion_error)
        - [`update_group_promotion_data`](#update_group_promotion_data)
        - [`process_groups`](#process_groups)
        - [`get_category_item`](#get_category_item)
        - [`check_interval`](#check_interval)
        - [`validate_group`](#validate_group)
- [Пример использования](#пример-использования)

## Классы

### `FacebookPromoter`

**Описание**: Этот класс управляет процессом продвижения товаров и событий AliExpress в группах Facebook.

**Как работает класс**:
Класс инициализируется с использованием экземпляра WebDriver, имени промоутера и путей к файлам с данными о группах Facebook. Он предоставляет методы для продвижения категорий и событий, ведения журнала ошибок, обновления данных о группах и проверки интервалов между продвижениями.

**Методы**:

- [`__init__`](#__init__): Инициализирует промоутер Facebook с необходимыми конфигурациями.
- [`promote`](#promote): Продвигает категорию или событие в указанной группе Facebook.
- [`log_promotion_error`](#log_promotion_error): Регистрирует ошибку при сбое продвижения.
- [`update_group_promotion_data`](#update_group_promotion_data): Обновляет данные группы после продвижения, добавляя продвигаемый элемент в список продвинутых категорий или событий.
- [`process_groups`](#process_groups): Обрабатывает группы для текущей кампании или продвижения событий.
- [`get_category_item`](#get_category_item): Получает элемент категории для продвижения на основе кампании и промоутера.
- [`check_interval`](#check_interval): Проверяет, достаточно ли времени прошло для повторного продвижения этой группы.
- [`validate_group`](#validate_group): Проверяет данные группы, чтобы убедиться, что у нее есть необходимые атрибуты.

#### `__init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False)`

```python
def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False):
    """
    Args:
        d (Driver): Экземпляр WebDriver для автоматизации.
        promoter (str): Имя промоутера (например, "aliexpress").
        group_file_paths (Optional[list[str  |  Path] | str | Path], optional): Пути к файлам с данными о группах.
        no_video (bool): Флаг для отключения видео в сообщениях. По умолчанию `False`.
    """
    ...
```

**Описание**: Инициализирует промоутер Facebook с необходимыми конфигурациями.

**Как работает функция**:
Метод `__init__` является конструктором класса `FacebookPromoter`. Он принимает экземпляр `Driver` (WebDriver), имя промоутера, пути к файлам с данными о группах и флаг для отключения видео в постах. Он устанавливает атрибуты экземпляра, такие как драйвер, имя промоутера, пути к файлам групп и флаг `no_video`.

**Параметры**:
- `d` (Driver): Экземпляр WebDriver для автоматизации браузера.
- `promoter` (str): Имя промоутера (например, "aliexpress").
- `group_file_paths` (Optional[list[str | Path] | str | Path], optional): Пути к файлам с данными о группах. Может быть списком путей или строкой, представляющей путь к файлу. По умолчанию `None`.
- `no_video` (bool): Флаг для отключения видео в постах. Если `True`, видео не будут загружаться при продвижении. По умолчанию `False`.

#### `promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool`

```python
def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
    """
    Args:
        group (SimpleNamespace): Данные группы.
        item (SimpleNamespace): Категория или событие для продвижения.
        is_event (bool): Является ли элемент событием или нет.
        language (str): Язык продвижения.
        currency (str): Валюта для продвижения.

    Returns:
        bool: Успешно ли продвижение или нет.
    """
    ...
```

**Описание**: Продвигает категорию или событие в указанной группе Facebook.

**Как работает функция**:
Метод `promote` принимает данные группы, элемент (категорию или событие) для продвижения, флаг, указывающий, является ли элемент событием, язык и валюту. Он выполняет продвижение элемента в указанной группе Facebook. Если продвижение успешно, он возвращает `True`, в противном случае - `False`.

**Параметры**:
- `group` (SimpleNamespace): Данные группы Facebook, в которой будет выполняться продвижение.
- `item` (SimpleNamespace): Элемент (категория или событие) для продвижения.
- `is_event` (bool): Флаг, указывающий, является ли элемент событием. По умолчанию `False`.
- `language` (str): Язык, на котором будет выполняться продвижение. По умолчанию `None`.
- `currency` (str): Валюта, используемая в продвижении. По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если продвижение выполнено успешно, `False` в противном случае.

#### `log_promotion_error(self, is_event: bool, item_name: str)`

```python
def log_promotion_error(self, is_event: bool, item_name: str):
    """
    Args:
        is_event (bool): Является ли элемент событием или нет.
        item_name (str): Название элемента.
    """
    ...
```

**Описание**: Регистрирует ошибку при сбое продвижения.

**Как работает функция**:
Метод `log_promotion_error` принимает флаг, указывающий, является ли элемент событием, и имя элемента. Он регистрирует ошибку, когда продвижение не удается.

**Параметры**:
- `is_event` (bool): Флаг, указывающий, является ли элемент событием.
- `item_name` (str): Имя элемента, который не удалось продвинуть.

#### `update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False)`

```python
def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
    """
    Args:
        group (SimpleNamespace): Данные группы.
        item_name (str): Название продвигаемого элемента.
        is_event (bool): Является ли элемент событием или нет.
    """
    ...
```

**Описание**: Обновляет данные группы после продвижения, добавляя продвигаемый элемент в список продвинутых категорий или событий.

**Как работает функция**:
Метод `update_group_promotion_data` принимает данные группы, имя продвигаемого элемента и флаг, указывающий, является ли элемент событием. Он обновляет данные группы после продвижения, добавляя продвинутый элемент в список продвинутых категорий или событий.

**Параметры**:
- `group` (SimpleNamespace): Данные группы Facebook.
- `item_name` (str): Имя элемента, который был продвинут.
- `is_event` (bool): Флаг, указывающий, является ли элемент событием. По умолчанию `False`.

#### `process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None)`

```python
def process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None):
    """
    Args:
        campaign_name (str): Название кампании.
        events (list[SimpleNamespace]): Список событий для продвижения.
        is_event (bool): Продвигать события или категории.
        group_file_paths (list[str]): Пути к файлам с данными о группах.
        group_categories_to_adv (list[str]): Категории для продвижения.
        language (str): Язык продвижения.
        currency (str): Валюта для продвижения.
    """
    ...
```

**Описание**: Обрабатывает группы для текущей кампании или продвижения событий.

**Как работает функция**:
Метод `process_groups` принимает название кампании, список событий для продвижения, флаг, указывающий, следует ли продвигать события или категории, пути к файлам с данными о группах, категории для продвижения, язык и валюту. Он обрабатывает группы для текущей кампании или продвижения событий.

**Параметры**:
- `campaign_name` (str): Название кампании. По умолчанию `None`.
- `events` (list[SimpleNamespace]): Список событий для продвижения. По умолчанию `None`.
- `is_event` (bool): Флаг, указывающий, следует ли продвигать события или категории. По умолчанию `False`.
- `group_file_paths` (list[str]): Пути к файлам с данными о группах. По умолчанию `None`.
- `group_categories_to_adv` (list[str]): Список категорий для продвижения. По умолчанию `['sales']`.
- `language` (str): Язык, на котором будет выполняться продвижение. По умолчанию `None`.
- `currency` (str): Валюта, используемая в продвижении. По умолчанию `None`.

#### `get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace`

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
    ...
```

**Описание**: Получает элемент категории для продвижения на основе кампании и промоутера.

**Как работает функция**:
Метод `get_category_item` принимает название кампании, данные группы, язык и валюту. Он получает элемент категории для продвижения на основе кампании и промоутера.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `group` (SimpleNamespace): Данные группы Facebook.
- `language` (str): Язык, на котором будет выполняться продвижение.
- `currency` (str): Валюта, используемая в продвижении.

**Возвращает**:
- `SimpleNamespace`: Элемент категории для продвижения.

#### `check_interval(self, group: SimpleNamespace) -> bool`

```python
def check_interval(self, group: SimpleNamespace) -> bool:
    """
    Args:
        group (SimpleNamespace): Данные группы.

    Returns:
        bool: Имеет ли группа право на продвижение.
    """
    ...
```

**Описание**: Проверяет, достаточно ли времени прошло для повторного продвижения этой группы.

**Как работает функция**:
Метод `check_interval` принимает данные группы. Он проверяет, достаточно ли времени прошло для повторного продвижения этой группы.

**Параметры**:
- `group` (SimpleNamespace): Данные группы Facebook.

**Возвращает**:
- `bool`: `True`, если группа имеет право на продвижение, `False` в противном случае.

#### `validate_group(self, group: SimpleNamespace) -> bool`

```python
def validate_group(self, group: SimpleNamespace) -> bool:
    """
    Args:
        group (SimpleNamespace): Данные группы.

    Returns:
        bool: Действительны ли данные группы.
    """
    ...
```

**Описание**: Проверяет данные группы, чтобы убедиться, что у нее есть необходимые атрибуты.

**Как работает функция**:
Метод `validate_group` принимает данные группы. Он проверяет, есть ли у группы необходимые атрибуты для продвижения.

**Параметры**:
- `group` (SimpleNamespace): Данные группы Facebook.

**Возвращает**:
- `bool`: `True`, если данные группы действительны, `False` в противном случае.

## Пример использования

### Пример использования класса `FacebookPromoter`

```python
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns

# Setup WebDriver instance (replace with actual WebDriver)
d = Driver()

# Create an instance of FacebookPromoter
promoter = FacebookPromoter(
    d=d, 
    promoter="aliexpress", 
    group_file_paths=["path/to/group/file1.json", "path/to/group/file2.json"]
)

# Start promoting products or events
promoter.process_groups(
    campaign_name="Campaign1",
    events=[], 
    group_categories_to_adv=["sales"],
    language="en",
    currency="USD"
)
```

## Лицензия

Этот модуль является частью более крупного пакета **Facebook Promoter** и лицензируется в соответствии с лицензией MIT.