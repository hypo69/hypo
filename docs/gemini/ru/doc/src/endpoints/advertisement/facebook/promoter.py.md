# Модуль `promoter.py`

## Обзор

Модуль `promoter.py` предназначен для автоматизации процесса продвижения (рекламы) контента, такого как сообщения и события, в группах Facebook. Он обеспечивает возможность публикации контента, учитывая заданные временные интервалы и предотвращая дублирование публикаций в одних и тех же группах. Модуль поддерживает различные типы рекламных кампаний, включая кампании AliExpress и другие, и адаптируется к языковым и валютным предпочтениям групп.

## Содержание

1.  [Функции](#функции)
    *   [`get_event_url`](#get_event_url)
2.  [Классы](#классы)
    *   [`FacebookPromoter`](#facebookpromoter)
        *   [`__init__`](#__init__)
        *   [`promote`](#promote)
        *   [`log_promotion_error`](#log_promotion_error)
        *   [`update_group_promotion_data`](#update_group_promotion_data)
        *   [`process_groups`](#process_groups)
        *   [`get_category_item`](#get_category_item)
        *   [`check_interval`](#check_interval)
        *   [`validate_group`](#validate_group)

## Функции

### `get_event_url`

**Описание**:
Возвращает модифицированный URL для создания события в Facebook, заменяя `group_id` значением из входного URL.

**Параметры**:
- `group_url` (str): URL группы Facebook, содержащий `group_id`.

**Возвращает**:
- `str`: Модифицированный URL для создания события.

## Классы

### `FacebookPromoter`

**Описание**:
Класс `FacebookPromoter` предназначен для продвижения товаров и событий AliExpress в группах Facebook. Он автоматизирует публикацию рекламных материалов в группах Facebook с помощью экземпляра WebDriver, обеспечивая продвижение категорий и событий, а также избегая дублирования.

**Методы**:
- [`__init__`](#__init__): Инициализирует промоутер для групп Facebook.
- [`promote`](#promote): Продвигает категорию или событие в группе Facebook.
- [`log_promotion_error`](#log_promotion_error): Логирует ошибку продвижения для категории или события.
- [`update_group_promotion_data`](#update_group_promotion_data): Обновляет данные группы после публикации.
- [`process_groups`](#process_groups): Обрабатывает все группы для текущей кампании или продвижения события.
- [`get_category_item`](#get_category_item): Получает элемент категории для продвижения на основе кампании и промоутера.
- [`check_interval`](#check_interval): Проверяет, прошло ли достаточно времени для продвижения этой группы.
- [`validate_group`](#validate_group): Проверяет корректность данных группы.

#### `__init__`

**Описание**:
Инициализирует промоутер для групп Facebook.

**Параметры**:
- `d` (Driver): Экземпляр WebDriver для автоматизации браузера.
- `promoter` (str): Название промоутера (например, "aliexpress").
- `group_file_paths` (Optional[list[str | Path] | str | Path], optional): Список путей к файлам, содержащим данные групп. По умолчанию `None`.
- `no_video` (bool, optional): Флаг для отключения видео в постах. По умолчанию `False`.

#### `promote`

**Описание**:
Продвигает категорию или событие в группе Facebook.

**Параметры**:
- `group` (SimpleNamespace): Данные группы Facebook.
- `item` (SimpleNamespace): Данные продвигаемой категории или события.
- `is_event` (bool, optional): Флаг, указывающий, является ли продвигаемый элемент событием. По умолчанию `False`.
- `language` (str, optional): Язык продвигаемого контента. По умолчанию `None`.
- `currency` (str, optional): Валюта продвигаемого контента. По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если продвижение прошло успешно, иначе `False`.

#### `log_promotion_error`

**Описание**:
Логирует ошибку продвижения для категории или события.

**Параметры**:
- `is_event` (bool): Флаг, указывающий, является ли продвигаемый элемент событием.
- `item_name` (str): Название продвигаемого элемента (категории или события).

#### `update_group_promotion_data`

**Описание**:
Обновляет данные группы после успешной публикации.

**Параметры**:
- `group` (SimpleNamespace): Данные группы Facebook.
- `item_name` (str): Название продвигаемого элемента (категории или события).
- `is_event` (bool, optional): Флаг, указывающий, является ли продвигаемый элемент событием. По умолчанию `False`.

#### `process_groups`

**Описание**:
Обрабатывает все группы для текущей кампании или продвижения события.

**Параметры**:
- `campaign_name` (str, optional): Название кампании для продвижения. По умолчанию `None`.
- `events` (list[SimpleNamespace], optional): Список событий для продвижения. По умолчанию `None`.
- `is_event` (bool, optional): Флаг, указывающий, продвигаются ли события. По умолчанию `False`.
- `group_file_paths` (list[str], optional): Список путей к файлам с данными групп. По умолчанию `None`.
- `group_categories_to_adv` (list[str], optional): Список категорий групп для продвижения. По умолчанию `['sales']`.
- `language` (str, optional): Язык продвигаемого контента. По умолчанию `None`.
- `currency` (str, optional): Валюта продвигаемого контента. По умолчанию `None`.

#### `get_category_item`

**Описание**:
Получает элемент категории для продвижения на основе кампании и промоутера.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `group` (SimpleNamespace): Данные группы Facebook.
- `language` (str): Язык продвигаемого контента.
- `currency` (str): Валюта продвигаемого контента.

**Возвращает**:
- `SimpleNamespace`: Данные категории для продвижения.

#### `check_interval`

**Описание**:
Проверяет, прошло ли достаточно времени для продвижения этой группы.

**Параметры**:
- `group` (SimpleNamespace): Данные группы Facebook.

**Возвращает**:
- `bool`: `True`, если прошло достаточно времени, иначе `False`.

#### `validate_group`

**Описание**:
Проверяет корректность данных группы.

**Параметры**:
- `group` (SimpleNamespace): Данные группы Facebook.

**Возвращает**:
- `bool`: `True`, если данные группы корректны, иначе `False`.