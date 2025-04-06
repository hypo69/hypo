# Модуль для продвижения в Facebook

## Обзор

Модуль `promoter.py` предназначен для автоматизации процесса продвижения сообщений и событий в группах Facebook. Он обрабатывает кампании и события, публикуя их в группах Facebook, избегая дублирования публикаций. Модуль содержит класс `FacebookPromoter`, который используется для управления процессом продвижения в Facebook.

## Подробнее

Модуль `promoter.py` предоставляет функциональность для продвижения товаров и событий AliExpress в группах Facebook. Он использует WebDriver для автоматизации публикаций в группах, обеспечивая продвижение категорий и событий, избегая дубликатов.

## Классы

### `FacebookPromoter`

**Описание**: Класс для продвижения товаров AliExpress и событий в группах Facebook.

**Принцип работы**: Класс `FacebookPromoter` автоматизирует процесс публикации рекламных материалов в группах Facebook. Он использует WebDriver для взаимодействия с браузером и выполняет следующие шаги:

1.  Инициализация WebDriver и загрузка данных о группах Facebook из файлов.
2.  Проверка интервала между публикациями для каждой группы.
3.  Получение списка категорий товаров или событий для продвижения.
4.  Публикация рекламных материалов в группах Facebook с использованием предопределенных сценариев.
5.  Обновление информации о последней публикации для каждой группы.

**Атрибуты**:

*   `d` (Driver): Инстанс WebDriver для автоматизации браузера.
*   `group_file_paths` (str | Path): Путь к файлу или файлам, содержащим данные о группах.
*   `no_video` (bool): Флаг, указывающий на необходимость отключения видео в постах.
*   `promoter` (str): Имя промоутера.

**Методы**:

*   `__init__`: Инициализирует класс `FacebookPromoter`.
*   `promote`: Продвигает категорию или событие в группе Facebook.
*   `log_promotion_error`: Логирует ошибку продвижения для категории или события.
*   `update_group_promotion_data`: Обновляет данные о продвижении группы.
*   `process_groups`: Обрабатывает все группы для текущей кампании или продвижения события.
*   `get_category_item`: Получает элемент категории для продвижения на основе кампании и промоутера.
*   `check_interval`: Проверяет, достаточно ли времени прошло для продвижения в этой группе.
*   `validate_group`: Проверяет, что данные группы корректны.

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

**Назначение**: Возвращает измененный URL для создания события в Facebook, заменяя `group_id` значением из входного URL.

**Параметры**:

*   `group_url` (str): URL группы Facebook, содержащий `group_id`.

**Возвращает**:

*   `str`: Измененный URL для создания события.

**Как работает функция**:

1.  Извлекает `group_id` из URL группы Facebook.
2.  Формирует базовый URL для создания события.
3.  Добавляет параметры запроса, включая `group_id`, к базовому URL.
4.  Возвращает полный URL для создания события.

```
Извлечение group_id из URL группы Facebook --> Формирование базового URL для создания события --> Добавление параметров запроса, включая group_id --> Возвращение полного URL для создания события
```

**Примеры**:

```python
group_url = "https://www.facebook.com/groups/1234567890/"
event_url = get_event_url(group_url)
print(event_url)
# Вывод: https://www.facebook.com/events/create/?acontext=%7B%22event_action_history%22%3A%5B%7B%22surface%22%3A%22group%22%7D%2C%7B%22mechanism%22%3A%22upcoming_events_for_group%22%2C%22surface%22%3A%22group%22%7D%5D%2C%22ref_notif_type%22%3Anull%7D&dialog_entry_point=group_events_tab&group_id=1234567890
```

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

**Назначение**: Инициализирует промоутер для групп Facebook.

**Параметры**:

*   `d` (Driver): Инстанс WebDriver для автоматизации браузера.
*   `promoter` (str): Имя промоутера.
*   `group_file_paths` (Optional[list[str | Path] | str | Path], optional): Список путей к файлам, содержащим данные о группах. По умолчанию `None`.
*   `no_video` (bool, optional): Флаг для отключения видео в постах. По умолчанию `False`.

**Как работает функция**:

1.  Инициализирует атрибуты класса `FacebookPromoter` с переданными значениями.
2.  Если `group_file_paths` не указан, получает список файлов групп из каталога `gs.path.google_drive / 'facebook' / 'groups'`.
3.  Инициализирует спиннер для отображения процесса выполнения.

```
Инициализация атрибутов класса --> Получение списка файлов групп (если не указаны) --> Инициализация спиннера
```

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.webdriver.firefox import Firefox
from pathlib import Path

driver = Driver(Firefox)
promoter = "aliexpress"
group_file_paths = [Path("/path/to/group1.json"), Path("/path/to/group2.json")]
fb_promoter = FacebookPromoter(driver, promoter, group_file_paths=group_file_paths, no_video=True)
```

### `FacebookPromoter.promote`

```python
def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
    """Promotes a category or event in a Facebook group."""
    ...
```

**Назначение**: Продвигает категорию или событие в группе Facebook.

**Параметры**:

*   `group` (SimpleNamespace): Объект, содержащий данные о группе Facebook.
*   `item` (SimpleNamespace): Объект, содержащий данные о категории или событии для продвижения.
*   `is_event` (bool, optional): Флаг, указывающий, является ли продвигаемый объект событием. По умолчанию `False`.
*   `language` (str, optional): Язык продвижения. По умолчанию `None`.
*   `currency` (str, optional): Валюта продвижения. По умолчанию `None`.

**Возвращает**:

*   `bool`: `True`, если продвижение прошло успешно, `False` в противном случае.

**Как работает функция**:

1.  Проверяет, соответствует ли язык и валюта группы указанным значениям (если они указаны).
2.  Определяет имя продвигаемого объекта (категории или события).
3.  Устанавливает атрибуты события или сообщения.
4.  Вызывает функцию `post_event` или `post_message` для публикации в группе Facebook.
5.  Обновляет данные о продвижении группы после успешной публикации.

```
Проверка языка и валюты группы --> Определение имени продвигаемого объекта --> Установка атрибутов события или сообщения --> Публикация в группе Facebook --> Обновление данных о продвижении группы
```

### `FacebookPromoter.log_promotion_error`

```python
def log_promotion_error(self, is_event: bool, item_name: str):
    """Logs promotion error for category or event."""
    logger.debug(f"Error while posting {'event' if is_event else 'category'} {item_name}", None, False)
```

**Назначение**: Логирует ошибку продвижения для категории или события.

**Параметры**:

*   `is_event` (bool): Флаг, указывающий, является ли продвигаемый объект событием.
*   `item_name` (str): Имя категории или события.

**Как работает функция**:

1.  Формирует сообщение об ошибке, указывающее, что произошла ошибка при публикации события или категории.
2.  Логирует сообщение об ошибке с использованием `logger.debug`.

```
Формирование сообщения об ошибке --> Логирование сообщения об ошибке
```

### `FacebookPromoter.update_group_promotion_data`

```python
def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
    """Updates group promotion data with the new promotion."""
```

**Назначение**: Обновляет данные о продвижении группы новой информацией о продвижении.

**Параметры**:

*   `group` (SimpleNamespace): Объект, содержащий данные о группе Facebook.
*   `item_name` (str): Имя категории или события.
*   `is_event` (bool, optional): Флаг, указывающий, является ли продвигаемый объект событием. По умолчанию `False`.

**Как работает функция**:

1.  Получает текущую метку времени.
2.  Обновляет атрибут `last_promo_sended` группы текущей меткой времени.
3.  Добавляет имя категории или события в список продвигаемых объектов группы (`promoted_events` или `promoted_categories`).

```
Получение текущей метки времени --> Обновление атрибута last_promo_sended --> Добавление имени категории или события в список продвигаемых объектов
```

### `FacebookPromoter.process_groups`

```python
def process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None):
    """Processes all groups for the current campaign or event promotion."""
```

**Назначение**: Обрабатывает все группы для текущей кампании или продвижения события.

**Параметры**:

*   `campaign_name` (str, optional): Имя кампании. По умолчанию `None`.
*   `events` (list[SimpleNamespace], optional): Список событий для продвижения. По умолчанию `None`.
*   `is_event` (bool, optional): Флаг, указывающий, является ли продвижение событием. По умолчанию `False`.
*   `group_file_paths` (list[str], optional): Список путей к файлам групп. По умолчанию `None`.
*   `group_categories_to_adv` (list[str], optional): Список категорий групп для продвижения. По умолчанию `['sales']`.
*   `language` (str, optional): Язык продвижения. По умолчанию `None`.
*   `currency` (str, optional): Валюта продвижения. По умолчанию `None`.

**Как работает функция**:

1.  Проверяет, указаны ли имя кампании или список событий.
2.  Перебирает файлы групп, указанные в `group_file_paths`.
3.  Загружает данные о группах из каждого файла.
4.  Перебирает группы в каждом файле.
5.  Проверяет интервал между продвижениями для каждой группы (если продвигается кампания).
6.  Проверяет, соответствует ли категория группы списку категорий для продвижения и является ли группа активной.
7.  Получает элемент категории или события для продвижения.
8.  Проверяет, не было ли уже продвинуто это событие или категория в группе.
9.  Проверяет соответствие языка и валюты группы указанным значениям.
10. Открывает URL группы в браузере.
11. Вызывает функцию `promote` для продвижения категории или события в группе.
12. Сохраняет изменения в файле группы.
13. Засыпает на случайное время.

```
Проверка имени кампании или списка событий --> Перебор файлов групп --> Загрузка данных о группах --> Перебор групп --> Проверка интервала между продвижениями --> Проверка соответствия категории группы и статуса --> Получение элемента категории или события --> Проверка, не было ли уже продвинуто --> Проверка соответствия языка и валюты --> Открытие URL группы в браузере --> Продвижение категории или события --> Сохранение изменений в файле группы --> Засыпание
```

### `FacebookPromoter.get_category_item`

```python
def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace:
    """Fetches the category item for promotion based on the campaign and promoter."""
```

**Назначение**: Получает элемент категории для продвижения на основе кампании и промоутера.

**Параметры**:

*   `campaign_name` (str): Имя кампании.
*   `group` (SimpleNamespace): Объект, содержащий данные о группе Facebook.
*   `language` (str): Язык продвижения.
*   `currency` (str): Валюта продвижения.

**Возвращает**:

*   `SimpleNamespace`: Объект, содержащий данные о категории для продвижения.

**Как работает функция**:

1.  Проверяет имя промоутера (`self.promoter`).
2.  Если промоутер - `'aliexpress'`, создает экземпляр класса `AliCampaignEditor` и получает случайную категорию и ее продукты.
3.  Если промоутер не `'aliexpress'`, загружает данные о категориях из JSON-файла и выбирает случайную категорию.
4.  Загружает описание категории из текстового файла.
5.  Получает путь к изображению категории.
6.  Возвращает объект, содержащий данные о категории.

```
Проверка имени промоутера --> Получение категории и продуктов (если aliexpress) / Загрузка данных о категориях из JSON (если не aliexpress) --> Загрузка описания категории --> Получение пути к изображению --> Возвращение объекта с данными о категории
```

### `FacebookPromoter.check_interval`

```python
def check_interval(self, group: SimpleNamespace) -> bool:
    """Checks if enough time has passed for promoting this group."""
    ...
```

**Назначение**: Проверяет, достаточно ли времени прошло для продвижения в этой группе.

**Параметры**:

*   `group` (SimpleNamespace): Объект, содержащий данные о группе Facebook.

**Возвращает**:

*   `bool`: `True`, если достаточно времени прошло для продвижения, `False` в противном случае.

### `FacebookPromoter.validate_group`

```python
def validate_group(self, group: SimpleNamespace) -> bool:
    """Validates that the group data is correct."""
```

**Назначение**: Проверяет, что данные группы корректны.

**Параметры**:

*   `group` (SimpleNamespace): Объект, содержащий данные о группе Facebook.

**Возвращает**:

*   `bool`: `True`, если данные группы корректны, `False` в противном случае.

**Как работает функция**:

1.  Проверяет, что объект группы не равен `None`.
2.  Проверяет, что у объекта группы есть атрибуты `group_url` и `group_categories`.
3.  Возвращает `True`, если все условия выполнены, `False` в противном случае.

```
Проверка объекта группы на None --> Проверка наличия атрибутов group_url и group_categories --> Возвращение True или False