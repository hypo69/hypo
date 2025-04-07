# Модуль для продвижения в Facebook

## Обзор

Модуль `promoter.py` предназначен для автоматизации процесса продвижения контента, такого как сообщения и события, в группах Facebook. Он обрабатывает кампании и события, публикуя их в группах Facebook, избегая при этом повторных публикаций. Модуль содержит класс `FacebookPromoter`, который использует `webdriver` для автоматизации действий в браузере.

## Подробнее

Этот модуль является частью системы для автоматизации маркетинговых кампаний в Facebook. Он включает в себя функции для получения URL-адреса события, продвижения контента в группах и обновления данных о продвижении. Модуль использует другие модули проекта, такие как `src.gs`, `src.endpoints.advertisement.facebook`, `src.webdriver.driver`, `src.utils.file`, `src.utils.jjson`, `src.utils.cursor_spinner` и `src.logger.logger`.

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
```

**Назначение**: Формирует URL для создания события в Facebook группе на основе предоставленного URL группы.

**Параметры**:
- `group_url` (str): URL Facebook группы, содержащий `group_id`.

**Возвращает**:
- `str`: Модифицированный URL для создания события.

**Как работает функция**:

1.  Извлекает `group_id` из URL группы.
2.  Формирует базовый URL для создания события.
3.  Добавляет параметры запроса, включая `group_id`.
4.  Возвращает полный URL для создания события.

```ascii
    group_url --> Извлечение group_id --> Формирование base_url --> Добавление параметров запроса --> event_url
```

**Примеры**:

```python
group_url = "https://www.facebook.com/groups/123456789"
event_url = get_event_url(group_url)
print(event_url)  # Вывод: https://www.facebook.com/events/create/?acontext=...&dialog_entry_point=group_events_tab&group_id=123456789
```

## Классы

### `FacebookPromoter`

**Описание**: Класс для продвижения товаров AliExpress и событий в группах Facebook.

**Принцип работы**:
Класс `FacebookPromoter` предназначен для автоматизации процесса публикации рекламных материалов в группах Facebook. Он использует экземпляр `WebDriver` для управления браузером и выполнения действий на страницах Facebook. Основная логика класса заключается в выборе подходящих групп, подготовке контента для публикации и отправке этого контента в выбранные группы. Класс также следит за тем, чтобы избежать повторной публикации одного и того же контента в одной и той же группе.

**Атрибуты**:
- `d` (Driver): Экземпляр WebDriver для автоматизации браузера.
- `group_file_paths` (str | Path): Путь к файлу или списку файлов, содержащих данные о группах Facebook.
- `no_video` (bool): Флаг, указывающий, следует ли отключать видео в постах.
- `promoter` (str): Имя промоутера.
- `spinner`: Объект для отображения спиннера в консоли.

**Методы**:

- `__init__`: Инициализирует промоутер для групп Facebook.
- `promote`: Продвигает категорию или событие в группе Facebook.
- `log_promotion_error`: Логирует ошибку продвижения для категории или события.
- `update_group_promotion_data`: Обновляет данные о продвижении группы новой информацией.
- `process_groups`: Обрабатывает все группы для текущей кампании или продвижения события.
- `get_category_item`: Получает элемент категории для продвижения на основе кампании и промоутера.
- `check_interval`: Проверяет, прошло ли достаточно времени для продвижения этой группы.
- `validate_group`: Проверяет, что данные группы корректны.

### `FacebookPromoter.__init__`

```python
def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False):
    """ Initializes the promoter for Facebook groups.

    Args:
        d (Driver): WebDriver instance for browser automation.
        group_file_paths (list[str | Path] | str | Path): List of file paths containing group data.
        no_video (bool, optional): Flag to disable videos in posts. Defaults to False.
    """
```

**Назначение**: Инициализирует экземпляр класса `FacebookPromoter`.

**Параметры**:
- `d` (Driver): Экземпляр `WebDriver` для управления браузером.
- `promoter` (str): Имя промоутера.
- `group_file_paths` (Optional[list[str | Path] | str | Path], optional): Список путей к файлам, содержащим данные о группах Facebook. По умолчанию `None`.
- `no_video` (bool, optional): Флаг для отключения видео в постах. По умолчанию `False`.

**Как работает функция**:

1.  Сохраняет переданные параметры в атрибуты экземпляра класса.
2.  Если `group_file_paths` не указан, получает список файлов из директории `gs.path.google_drive / 'facebook' / 'groups'`.
3.  Инициализирует `spinner` для отображения индикатора загрузки.

```ascii
    d, promoter, group_file_paths, no_video --> Сохранение параметров --> Получение списка файлов (если group_file_paths is None) --> Инициализация spinner
```

**Примеры**:

```python
from src.webdriver.driver import Driver, Chrome
from pathlib import Path

# Пример инициализации с указанием путей к файлам групп
driver = Driver(Chrome)
group_file_paths = [Path('./groups/group1.json'), Path('./groups/group2.json')]
promoter = FacebookPromoter(driver, promoter='test_promoter', group_file_paths=group_file_paths, no_video=True)

# Пример инициализации без указания путей к файлам групп (будет использована директория по умолчанию)
promoter = FacebookPromoter(driver, promoter='test_promoter', no_video=False)
```

### `FacebookPromoter.promote`

```python
def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
    """Promotes a category or event in a Facebook group."""
    ...
```

**Назначение**: Продвигает категорию или событие в группе Facebook.

**Параметры**:
- `group` (SimpleNamespace): Объект, содержащий данные о группе Facebook.
- `item` (SimpleNamespace): Объект, содержащий данные о категории или событии для продвижения.
- `is_event` (bool, optional): Флаг, указывающий, является ли продвигаемый элемент событием. По умолчанию `False`.
- `language` (str, optional): Язык продвижения. По умолчанию `None`.
- `currency` (str, optional): Валюта продвижения. По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если продвижение успешно, `False` в противном случае.

**Как работает функция**:

1.  Проверяет соответствие языка и валюты группы заданным параметрам.
2.  Устанавливает атрибуты события или сообщения.
3.  Вызывает функции `post_event` или `post_message` для публикации контента в группе.
4.  Обновляет данные группы после публикации.
5.  Возвращает `True` в случае успеха, `False` в случае ошибки.

```ascii
    group, item, is_event, language, currency --> Проверка языка и валюты --> Установка атрибутов --> Публикация (post_event или post_message) --> Обновление данных группы --> return True или False
```

### `FacebookPromoter.log_promotion_error`

```python
def log_promotion_error(self, is_event: bool, item_name: str):
    """Logs promotion error for category or event."""
```

**Назначение**: Логирует ошибку продвижения для категории или события.

**Параметры**:
- `is_event` (bool): Флаг, указывающий, является ли продвигаемый элемент событием.
- `item_name` (str): Имя категории или события.

**Как работает функция**:

1.  Логирует отладочное сообщение об ошибке продвижения с использованием `logger.debug`.

```ascii
    is_event, item_name --> Логирование ошибки
```

### `FacebookPromoter.update_group_promotion_data`

```python
def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
    """Updates group promotion data with the new promotion."""
```

**Назначение**: Обновляет данные о продвижении группы новой информацией.

**Параметры**:
- `group` (SimpleNamespace): Объект, содержащий данные о группе Facebook.
- `item_name` (str): Имя категории или события.
- `is_event` (bool, optional): Флаг, указывающий, является ли продвигаемый элемент событием. По умолчанию `False`.

**Как работает функция**:

1.  Получает текущую дату и время.
2.  Обновляет данные о последней отправленной промоакции.
3.  Добавляет имя категории или события в список продвигаемых элементов.

```ascii
    group, item_name, is_event --> Получение текущей даты и времени --> Обновление данных о последней отправленной промоакции --> Добавление имени категории/события в список продвигаемых
```

### `FacebookPromoter.process_groups`

```python
def process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None):
    """Processes all groups for the current campaign or event promotion."""
```

**Назначение**: Обрабатывает все группы для текущей кампании или продвижения события.

**Параметры**:
- `campaign_name` (str, optional): Имя кампании. По умолчанию `None`.
- `events` (list[SimpleNamespace], optional): Список событий для продвижения. По умолчанию `None`.
- `is_event` (bool, optional): Флаг, указывающий, является ли продвижение событием. По умолчанию `False`.
- `group_file_paths` (list[str], optional): Список путей к файлам групп. По умолчанию `None`.
- `group_categories_to_adv` (list[str], optional): Список категорий групп для продвижения. По умолчанию `['sales']`.
- `language` (str, optional): Язык продвижения. По умолчанию `None`.
- `currency` (str, optional): Валюта продвижения. По умолчанию `None`.

**Как работает функция**:

1.  Проверяет, есть ли что продвигать (кампания или события).
2.  Итерируется по файлам групп.
3.  Загружает данные о группах из файлов.
4.  Итерируется по группам.
5.  Проверяет интервал, категории и статус группы.
6.  Получает элемент категории или события для продвижения.
7.  Проверяет, не был ли уже продвинут элемент.
8.  Переходит по URL группы.
9.  Вызывает функцию `promote` для продвижения элемента в группе.
10. Сохраняет обновленные данные о группах.

```ascii
    campaign_name, events, is_event, group_file_paths, group_categories_to_adv, language, currency --> Проверка наличия контента для продвижения --> Итерация по файлам групп --> Загрузка данных о группах --> Итерация по группам --> Проверка интервала, категорий и статуса группы --> Получение элемента категории/события --> Проверка, был ли уже продвинут элемент --> Переход по URL группы --> Продвижение элемента --> Сохранение данных
```

### `FacebookPromoter.get_category_item`

```python
def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace:
    """Fetches the category item for promotion based on the campaign and promoter."""
```

**Назначение**: Получает элемент категории для продвижения на основе кампании и промоутера.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `group` (SimpleNamespace): Объект, содержащий данные о группе Facebook.
- `language` (str): Язык продвижения.
- `currency` (str): Валюта продвижения.

**Возвращает**:
- `SimpleNamespace`: Объект, содержащий данные о категории для продвижения.

**Как работает функция**:

1.  В зависимости от промоутера (`aliexpress` или другого) выбирает способ получения элемента категории.
2.  Для `aliexpress` использует класс `AliCampaignEditor` для получения категорий и продуктов.
3.  Для других промоутеров загружает данные о категориях из JSON-файла и получает описание из текстового файла.
4.  Возвращает объект, содержащий данные о категории.

```ascii
    campaign_name, group, language, currency --> Выбор способа получения элемента категории (в зависимости от промоутера) --> Получение данных о категории --> return item
```

### `FacebookPromoter.check_interval`

```python
def check_interval(self, group: SimpleNamespace) -> bool:
    """Checks if enough time has passed for promoting this group."""
```

**Назначение**: Проверяет, прошло ли достаточно времени для продвижения этой группы.

**Параметры**:
- `group` (SimpleNamespace): Объект, содержащий данные о группе Facebook.

**Возвращает**:
- `bool`: `True`, если прошло достаточно времени, `False` в противном случае.

**Как работает функция**:

1.  Проверяет, прошло ли достаточно времени с момента последней промоакции в группе.
2.  Возвращает `True`, если прошло достаточно времени, `False` в противном случае.

```ascii
    group --> Проверка времени с момента последней промоакции --> return True или False
```

### `FacebookPromoter.validate_group`

```python
def validate_group(self, group: SimpleNamespace) -> bool:
    """Validates that the group data is correct."""
```

**Назначение**: Проверяет, что данные группы корректны.

**Параметры**:
- `group` (SimpleNamespace): Объект, содержащий данные о группе Facebook.

**Возвращает**:
- `bool`: `True`, если данные группы корректны, `False` в противном случае.

**Как работает функция**:

1.  Проверяет наличие атрибутов `group_url` и `group_categories` в объекте группы.
2.  Возвращает `True`, если данные группы корректны, `False` в противном случае.

```ascii
    group --> Проверка наличия атрибутов group_url и group_categories --> return True или False
```