# Facebook Promoter Module

## Обзор

Модуль **Facebook Promoter** автоматизирует продвижение товаров и событий AliExpress в группах Facebook. Модуль обрабатывает размещение рекламных объявлений в Facebook, гарантируя, что категории и события продвигаются без дубликатов. Он использует WebDriver для автоматизации браузера для эффективной обработки рекламных акций.

## Возможности модуля

- Продвижение категорий и событий в группах Facebook.
- Избежание дублирования продвижений путем отслеживания ранее продвигаемых элементов.
- Поддержка конфигурации данных группы через файлы.
- Возможность отключения загрузки видео в рекламных акциях.

## Требования

- **Python** 3.x
- Необходимые библиотеки:
  - `random`
  - `datetime`
  - `pathlib`
  - `urllib.parse`
  - `types.SimpleNamespace`
  - `src` (пользовательский модуль)

## Блок-схема

```mermaid
flowchart TD
    A[Начало] --> B[Инициализация WebDriver];
    B --> C[Создание экземпляра FacebookPromoter];
    C --> D[Обработка групп для продвижения];
    D --> E[Получение данных группы];
    E --> F{Являются ли данные группы действительными?};
    F -- Да --> G[Получение элемента категории для продвижения];
    F -- Нет --> H[Логирование ошибки и выход];
    G --> I{Можно ли продвигать группу?};
    I -- Да --> J[Продвижение категории или события];
    I -- Нет --> K[Ожидание интервала между продвижениями];
    J --> L[Обновление данных группы];
    K --> L;
    L --> M[Конец];
    H --> M;
```

## Использование

### Пример использования класса FacebookPromoter

```python
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns

# Настройка экземпляра WebDriver (замените на фактический WebDriver)
d = Driver()

# Создание экземпляра FacebookPromoter
promoter = FacebookPromoter(
    d=d,
    promoter="aliexpress",
    group_file_paths=["path/to/group/file1.json", "path/to/group/file2.json"]
)

# Начать продвижение товаров или событий
promoter.process_groups(
    campaign_name="Campaign1",
    events=[],
    group_categories_to_adv=["sales"],
    language="en",
    currency="USD"
)
```

## Документация по классам

### Класс `FacebookPromoter`

Этот класс управляет процессом продвижения товаров и событий AliExpress в группах Facebook.

#### Методы

##### `__init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False)`

Инициализирует продвижение в Facebook необходимыми конфигурациями.

**Параметры**:

- `d (Driver)`: Экземпляр WebDriver для автоматизации.
- `promoter (str)`: Имя промоутера (например, "aliexpress").
- `group_file_paths (Optional[list[str | Path] | str | Path])`: Пути к файлам данных группы.
- `no_video (bool)`: Флаг для отключения видео в постах. По умолчанию `False`.

##### `promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool`

Продвигает категорию или событие в указанной группе Facebook.

**Параметры**:

- `group (SimpleNamespace)`: Данные группы.
- `item (SimpleNamespace)`: Категория или событие для продвижения.
- `is_event (bool)`: Является ли элемент событием или нет.
- `language (str)`: Язык продвижения.
- `currency (str)`: Валюта для продвижения.

**Возвращает**:

- `bool`: Было ли продвижение успешным или нет.

##### `log_promotion_error(self, is_event: bool, item_name: str)`

Регистрирует ошибку при сбое продвижения.

**Параметры**:

- `is_event (bool)`: Является ли элемент событием или нет.
- `item_name (str)`: Название элемента.

##### `update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False)`

Обновляет данные группы после продвижения, добавляя продвигаемый элемент в список продвигаемых категорий или событий.

**Параметры**:

- `group (SimpleNamespace)`: Данные группы.
- `item_name (str)`: Название продвинутого элемента.
- `is_event (bool)`: Является ли элемент событием или нет.

##### `process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None)`

Обрабатывает группы для текущей кампании или продвижения события.

**Параметры**:

- `campaign_name (str)`: Название кампании.
- `events (list[SimpleNamespace])`: Список событий для продвижения.
- `is_event (bool)`: Продвигать ли события или категории.
- `group_file_paths (list[str])`: Пути к файлам данных группы.
- `group_categories_to_adv (list[str])`: Категории для продвижения.
- `language (str)`: Язык продвижения.
- `currency (str)`: Валюта для продвижения.

##### `get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace`

Получает элемент категории для продвижения на основе кампании и промоутера.

**Параметры**:

- `campaign_name (str)`: Название кампании.
- `group (SimpleNamespace)`: Данные группы.
- `language (str)`: Язык для продвижения.
- `currency (str)`: Валюта для продвижения.

**Возвращает**:

- `SimpleNamespace`: Элемент категории для продвижения.

##### `check_interval(self, group: SimpleNamespace) -> bool`

Проверяет, достаточно ли времени прошло для повторного продвижения этой группы.

**Параметры**:

- `group (SimpleNamespace)`: Данные группы.

**Возвращает**:

- `bool`: Имеет ли группа право на продвижение.

##### `validate_group(self, group: SimpleNamespace) -> bool`

Проверяет данные группы, чтобы убедиться, что у нее есть необходимые атрибуты.

**Параметры**:

- `group (SimpleNamespace)`: Данные группы.

**Возвращает**:

- `bool`: Являются ли данные группы действительными.

## Лицензия

Этот модуль является частью более крупного пакета **Facebook Promoter** и лицензируется в соответствии с лицензией MIT.