# Модуль hypotez/src/endpoints/advertisement/facebook/promoter.py

## Обзор

Модуль `hypotez/src/endpoints/advertisement/facebook/promoter.py` отвечает за продвижение сообщений и событий AliExpress в группах Facebook. Он обрабатывает рекламные кампании и события, публикуя их в группах Facebook, избегая дублирования продвижения. Модуль использует WebDriver для автоматизации процесса.

## Переменные

### `MODE`

Тип: `str`

Значение: `'dev'`

Описание: Переменная, хранящая режим работы (в данном случае 'dev').


## Функции

### `get_event_url`

**Описание**: Возвращает изменённый URL для создания события в Facebook, заменяя `group_id` значением из входного URL.

**Параметры**:
- `group_url` (str): URL группы Facebook, содержащий `group_id`.
- `event_id` (str): Идентификатор события.

**Возвращает**:
- `str`: Изменённый URL для создания события.

### `FacebookPromoter`

**Описание**: Класс для продвижения продуктов AliExpress и событий в группах Facebook.

**Атрибуты**:
- `d` (Driver): Экземпляр WebDriver для автоматизации браузера.
- `group_file_paths` (str | Path): Пути к файлам, содержащим данные о группах.
- `no_video` (bool): Флаг для отключения видео в постах.
- `promoter` (str): Наименование продвижения.
- `spinner` (spinning_cursor): Экземпляр спиннера для индикации процесса.

**Методы**:

#### `__init__`

**Описание**: Инициализирует продвижение для групп Facebook.

**Параметры**:
- `d` (Driver): Экземпляр WebDriver.
- `promoter` (str): Наименование продвижения.
- `group_file_paths` (list[str | Path] | str | Path, optional): Список путей к файлам с данными о группах. По умолчанию использует данные из папки `facebook/groups`.
- `no_video` (bool, optional): Флаг для отключения видео. По умолчанию `False`.


#### `promote`

**Описание**: Продвигает категорию или событие в группе Facebook.

**Параметры**:
- `group` (SimpleNamespace): Данные о группе.
- `item` (SimpleNamespace): Данные о категории или событии.
- `is_event` (bool, optional): Флаг, указывающий на событие. По умолчанию `False`.
- `language` (str, optional): Язык.
- `currency` (str, optional): Валюта.

**Возвращает**:
- `bool`: `True`, если продвижение выполнено успешно, иначе `False`.

#### `log_promotion_error`

**Описание**: Записывает ошибку продвижения в журнал.

**Параметры**:
- `is_event` (bool): Флаг, указывающий на событие.
- `item_name` (str): Наименование категории или события.


#### `update_group_promotion_data`

**Описание**: Обновляет данные о продвижении группы с новыми данными.

**Параметры**:
- `group` (SimpleNamespace): Данные о группе.
- `item_name` (str): Наименование категории или события.
- `is_event` (bool, optional): Флаг, указывающий на событие. По умолчанию `False`.

#### `process_groups`

**Описание**: Обрабатывает все группы для текущей рекламной кампании или продвижения событий.

**Параметры**:
- `campaign_name` (str, optional): Наименование рекламной кампании.
- `events` (list[SimpleNamespace], optional): Список событий для продвижения.
- `is_event` (bool, optional): Флаг, указывающий на событие. По умолчанию `False`.
- `group_file_paths` (list[str], optional): Список путей к файлам с данными о группах.
- `group_categories_to_adv` (list[str], optional): Список категорий для продвижения. По умолчанию `['sales']`.
- `language` (str, optional): Язык.
- `currency` (str, optional): Валюта.


#### `get_category_item`

**Описание**: Получает элемент категории для продвижения на основе кампании и продвижения.

**Параметры**:
- `campaign_name` (str): Наименование кампании.
- `group` (SimpleNamespace): Данные о группе.
- `language` (str): Язык.
- `currency` (str): Валюта.

**Возвращает**:
- `SimpleNamespace`: Элемент категории.

#### `check_interval`

**Описание**: Проверяет, прошёл ли необходимый интервал для следующего продвижения.

**Параметры**:
- `group` (SimpleNamespace): Данные о группе.

**Возвращает**:
- `bool`: `True`, если интервал прошёл, иначе `False`.

**Возможные исключения**:
- `ValueError`: Если формат интервала некорректен.

#### `parse_interval`

**Описание**: Преобразует строковый интервал в объект `timedelta`.

**Параметры**:
- `interval` (str): Интервал в строковом формате (например, '1H', '6M').

**Возвращает**:
- `timedelta`: Соответствующий объект `timedelta`.

**Возможные исключения**:
- `ValueError`: Если формат интервала некорректен.

#### `run_campaigns`

**Описание**: Выполняет цикл продвижения кампании для всех групп и категорий последовательно.

**Параметры**:
- `campaigns` (list[str]): Список имён кампаний для продвижения.
- `group_file_paths` (list[str], optional): Список путей к файлам с данными о группах.
- `group_categories_to_adv` (list[str], optional): Список категорий для продвижения. По умолчанию `['sales']`.
- `language` (str, optional): Язык.
- `currency` (str, optional): Валюта.
- `no_video` (bool, optional): Флаг для отключения видео.

#### `run_events`

**Описание**: Выполняет продвижение событий во всех группах последовательно.

**Параметры**:
- `events_names` (list[str]): Список имён событий для продвижения.
- `group_file_paths` (list[str]): Список путей к файлам с данными о группах.

#### `stop`

**Описание**: Останавливает процесс продвижения, закрывая экземпляр WebDriver.



## Пример использования

```python
group_files = ["ru_usd.json", "usa.json", "ger_en_eur.json", "he_il.json", "ru_il.json"]
promoter = FacebookPromoter(d=Driver(Chrome), group_file_paths=group_files, no_video=True)

try:
    promoter.run_campaigns(campaigns=["campaign1", "campaign2"], group_file_paths=group_files)
except KeyboardInterrupt:
    print("Campaign promotion interrupted.")
```