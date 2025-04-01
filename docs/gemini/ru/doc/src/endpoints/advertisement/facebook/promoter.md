# Документация модуля Facebook Promoter

## Обзор

Модуль **Facebook Promoter** автоматизирует продвижение товаров и событий AliExpress в группах Facebook. Модуль отвечает за публикацию рекламных акций в Facebook, обеспечивая продвижение категорий и событий без дубликатов. Он использует WebDriver для автоматизации браузера, что обеспечивает эффективную обработку рекламных акций.

## Подробнее

Модуль предназначен для автоматизации процесса продвижения товаров и событий AliExpress в группах Facebook. Он позволяет настраивать параметры групп, избегать повторных публикаций и управлять процессом продвижения через WebDriver.

## Содержание

- [Классы](#классы)
    - [`FacebookPromoter`](#facebookpromoter-class)
        - [`__init__`](#__init__)
        - [`promote`](#promote)
        - [`log_promotion_error`](#log_promotion_error)
        - [`update_group_promotion_data`](#update_group_promotion_data)
        - [`process_groups`](#process_groups)
        - [`get_category_item`](#get_category_item)
        - [`check_interval`](#check_interval)
        - [`validate_group`](#validate_group)

## Классы

### `FacebookPromoter` Class

Этот класс управляет процессом продвижения товаров и событий AliExpress в группах Facebook.

**Принцип работы**:
Класс инициализируется с WebDriver, именем промоутера и путями к файлам с данными о группах. Он предоставляет методы для продвижения категорий и событий, логирования ошибок, обновления данных о группах и проверки интервалов между продвижениями.

#### Методы

- `__init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False)`

    Инициализирует промоутер Facebook с необходимыми конфигурациями.

    **Параметры**:
    - `d (Driver)`: Экземпляр WebDriver для автоматизации.
    - `promoter (str)`: Имя промоутера (например, "aliexpress").
    - `group_file_paths (Optional[list[str | Path] | str | Path])`: Пути к файлам с данными о группах.
    - `no_video (bool)`: Флаг для отключения видео в постах. По умолчанию `False`.

- `promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool`

    Продвигает категорию или событие в указанной группе Facebook.

    **Параметры**:
    - `group (SimpleNamespace)`: Данные группы.
    - `item (SimpleNamespace)`: Категория или событие для продвижения.
    - `is_event (bool)`: Является ли элемент событием или нет.
    - `language (str)`: Язык продвижения.
    - `currency (str)`: Валюта для продвижения.

    **Возвращает**:
    - `bool`: Успешно ли прошло продвижение или нет.

- `log_promotion_error(self, is_event: bool, item_name: str)`

    Логирует ошибку при неудачном продвижении.

    **Параметры**:
    - `is_event (bool)`: Является ли элемент событием или нет.
    - `item_name (str)`: Имя элемента.

- `update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False)`

    Обновляет данные группы после продвижения, добавляя продвигаемый элемент в список продвинутых категорий или событий.

    **Параметры**:
    - `group (SimpleNamespace)`: Данные группы.
    - `item_name (str)`: Имя продвинутого элемента.
    - `is_event (bool)`: Является ли элемент событием или нет.

- `process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None)`

    Обрабатывает группы для текущей кампании или продвижения события.

    **Параметры**:
    - `campaign_name (str)`: Имя кампании.
    - `events (list[SimpleNamespace])`: Список событий для продвижения.
    - `is_event (bool)`: Продвигать события или категории.
    - `group_file_paths (list[str])`: Пути к файлам с данными о группах.
    - `group_categories_to_adv (list[str])`: Категории для продвижения.
    - `language (str)`: Язык продвижения.
    - `currency (str)`: Валюта для продвижения.

- `get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace`

    Получает элемент категории для продвижения на основе кампании и промоутера.

    **Параметры**:
    - `campaign_name (str)`: Имя кампании.
    - `group (SimpleNamespace)`: Данные группы.
    - `language (str)`: Язык продвижения.
    - `currency (str)`: Валюта для продвижения.

    **Возвращает**:
    - `SimpleNamespace`: Элемент категории для продвижения.

- `check_interval(self, group: SimpleNamespace) -> bool`

    Проверяет, достаточно ли времени прошло для повторного продвижения в этой группе.

    **Параметры**:
    - `group (SimpleNamespace)`: Данные группы.

    **Возвращает**:
    - `bool`: Может ли группа быть продвинута.

- `validate_group(self, group: SimpleNamespace) -> bool`

    Проверяет данные группы, чтобы убедиться, что у них есть необходимые атрибуты.

    **Параметры**:
    - `group (SimpleNamespace)`: Данные группы.

    **Возвращает**:
    - `bool`: Являются ли данные группы действительными.

## Лицензия

Этот модуль является частью более крупного пакета **Facebook Promoter** и распространяется под лицензией MIT.