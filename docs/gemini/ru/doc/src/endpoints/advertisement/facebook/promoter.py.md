# Модуль `promoter.py`

## Обзор

Модуль `promoter.py` предназначен для автоматизации продвижения контента (сообщений, событий, рекламных объявлений) в группах Facebook. Он содержит класс `FacebookPromoter`, который обеспечивает публикацию контента в группах с учетом различных параметров, таких как язык, валюта и интервалы между публикациями. Модуль также включает функции для получения URL-адресов событий и обработки данных групп.

## Подробней

Модуль `promoter.py` является частью системы продвижения в Facebook и выполняет следующие задачи:

1.  **Инициализация промоутера**: Класс `FacebookPromoter` инициализируется с драйвером WebDriver, списком файлов групп и флагом для отключения видео.
2.  **Обработка групп**: Метод `process_groups` обрабатывает группы для продвижения кампаний или событий, проверяя интервалы между публикациями и категории групп.
3.  **Продвижение контента**: Метод `promote` публикует контент (сообщения, события, рекламные объявления) в группах Facebook, учитывая язык и валюту группы.
4.  **Обновление данных группы**: После успешной публикации данных группы обновляются, чтобы избежать повторной публикации одного и того же контента.
5.  **Получение элементов категорий**: Метод `get_category_item` получает элементы категорий для продвижения на основе кампании и промоутера.

Этот модуль используется для автоматизации процесса продвижения в Facebook, что позволяет эффективно достигать целевую аудиторию и избегать рутинных операций.

## Классы

### `FacebookPromoter`

**Описание**: Класс для продвижения товаров AliExpress и событий в группах Facebook.

**Методы**:

*   `__init__`: Инициализирует промоутер для групп Facebook.
*   `promote`: Продвигает категорию или событие в группе Facebook.
*   `log_promotion_error`: Регистрирует ошибку продвижения для категории или события.
*   `update_group_promotion_data`: Обновляет данные группы после продвижения.
*   `process_groups`: Обрабатывает все группы для текущей кампании или продвижения событий.
*   `get_category_item`: Получает элемент категории для продвижения на основе кампании и промоутера.
*   `check_interval`: Проверяет, прошло ли достаточно времени для продвижения этой группы.
*   `validate_group`: Проверяет корректность данных группы.

**Параметры**:

*   `d` (Driver): Экземпляр WebDriver для автоматизации браузера.
*   `group_file_paths` (list[str | Path] | str | Path): Список путей к файлам, содержащим данные группы.
*   `no_video` (bool, optional): Флаг для отключения видео в постах. По умолчанию `False`.
*   `promoter` (str): Имя промоутера.

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from types import SimpleNamespace

# Инициализация драйвера
d = Driver()

# Инициализация промоутера
promoter = FacebookPromoter(d=d, promoter='aliexpress')

# Пример группы
group = SimpleNamespace(
    group_url='https://www.facebook.com/groups/example',
    group_categories=['sales'],
    status='active',
    language='ru',
    currency='RUB',
    promoted_categories=[],
    promoted_events=[],
    last_promo_sended=None
)

# Пример элемента категории
item = SimpleNamespace(
    category_name='example_category',
    language=SimpleNamespace(ru='Описание категории'),
    products=['product1', 'product2']
)

# Продвижение категории в группе
promoter.promote(group=group, item=item)
```

## Функции

### `get_event_url`

```python
def get_event_url(group_url: str) -> str:
    """
    Args:
        group_url (str): Facebook group URL containing `group_id`.

    Returns:
        str: Modified URL for creating the event.
    """
```

**Описание**: Возвращает измененный URL-адрес для создания события на Facebook, заменяя `group_id` значением из входного URL.

**Параметры**:

*   `group_url` (str): URL-адрес группы Facebook, содержащий `group_id`.

**Возвращает**:

*   `str`: Измененный URL-адрес для создания события.

**Примеры**:

```python
group_url = 'https://www.facebook.com/groups/123456789'
event_url = get_event_url(group_url)
print(event_url)  # Вывод: https://www.facebook.com/events/create/?acontext=%7B%22event_action_history%22%3A%5B%7B%22surface%22%3A%22group%22%7D%2C%7B%22mechanism%22%3A%22upcoming_events_for_group%22%2C%22surface%22%3A%22group%22%7D%5D%2C%22ref_notif_type%22%3Anull%7D&dialog_entry_point=group_events_tab&group_id=123456789
```
```python
def log_promotion_error(self, is_event: bool, item_name: str):
    """Logs promotion error for category or event."""
```

**Описание**: Регистрирует ошибку продвижения для категории или события.

**Параметры**:
*    `is_event` (bool): Логическая переменая, определяющая, является ли продвигаемый элемент событием.
*    `item_name` (str): Имя продвигаемого элемента.

**Примеры**:
```python
promoter = FacebookPromoter(d=d, promoter='aliexpress')
promoter.log_promotion_error(True, 'имя_события')
promoter.log_promotion_error(False, 'имя_категории')
```
```python
def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
    """Updates group promotion data with the new promotion."""
```
**Описание**: Обновляет данные группы после продвижения.

**Параметры**:
*    `group` (SimpleNamespace): Пространство имен группы, содержащее данные о группе.
*    `item_name` (str): Имя продвигаемого элемента.
*    `is_event` (bool): Логическая переменая, определяющая, является ли продвигаемый элемент событием.
**Примеры**:
```python
group = SimpleNamespace(
    group_url='https://www.facebook.com/groups/example',
    group_categories=['sales'],
    status='active',
    language='ru',
    currency='RUB',
    promoted_categories=[],
    promoted_events=[],
    last_promo_sended=None
)
promoter = FacebookPromoter(d=d, promoter='aliexpress')
promoter.update_group_promotion_data(group, 'имя_категории', False)
```
```python
def process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None):
    """Processes all groups for the current campaign or event promotion."""
```
**Описание**: Обрабатывает все группы для текущей кампании или продвижения событий.

**Параметры**:
*    `campaign_name` (str): Имя кампании.
*    `events` (list[SimpleNamespace]): Список событий для продвижения.
*    `is_event` (bool): Логическая переменая, определяющая, является ли продвигаемый элемент событием.
*    `group_file_paths` (list[str]): Список путей к файлам групп.
*    `group_categories_to_adv` (list[str]): Список категорий групп для продвижения.
*    `language` (str): Язык для продвижения.
*    `currency` (str): Валюта для продвижения.

**Примеры**:
```python
group_file_paths=['example_groups.json']
events = [SimpleNamespace(
    event_name='example_event',
    language=SimpleNamespace(ru='Описание события'),
    start='2024-01-01',
    end='2024-01-02'
)]

promoter = FacebookPromoter(d=d, promoter='aliexpress')
promoter.process_groups('example_campaign', events, True, group_file_paths, ['sales'], 'ru', 'RUB')
```
```python
def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace:
    """Fetches the category item for promotion based on the campaign and promoter."""
```
**Описание**: Получает элемент категории для продвижения на основе кампании и промоутера.

**Параметры**:
*    `campaign_name` (str): Имя кампании.
*    `group` (SimpleNamespace): Пространство имен группы, содержащее данные о группе.
*    `language` (str): Язык для продвижения.
*    `currency` (str): Валюта для продвижения.

**Возвращает**:
*    `SimpleNamespace`: Элемент категории для продвижения.

**Примеры**:
```python
group = SimpleNamespace(
    group_url='https://www.facebook.com/groups/example',
    group_categories=['sales'],
    status='active',
    language='ru',
    currency='RUB',
    promoted_categories=[],
    promoted_events=[],
    last_promo_sended=None
)
promoter = FacebookPromoter(d=d, promoter='aliexpress')
category_item = promoter.get_category_item('example_campaign', group, 'ru', 'RUB')
```
```python
def check_interval(self, group: SimpleNamespace) -> bool:
    """Checks if enough time has passed for promoting this group."""
```
**Описание**: Проверяет, прошло ли достаточно времени для продвижения этой группы.

**Параметры**:
*    `group` (SimpleNamespace): Пространство имен группы, содержащее данные о группе.

**Возвращает**:
*    `bool`: True, если достаточно времени прошло, иначе False.

**Примеры**:
```python
group = SimpleNamespace(
    group_url='https://www.facebook.com/groups/example',
    group_categories=['sales'],
    status='active',
    language='ru',
    currency='RUB',
    promoted_categories=[],
    promoted_events=[],
    last_promo_sended=None
)
promoter = FacebookPromoter(d=d, promoter='aliexpress')
is_interval_ok = promoter.check_interval(group)
print(is_interval_ok)
```
```python
def validate_group(self, group: SimpleNamespace) -> bool:
    """Validates that the group data is correct."""
```
**Описание**: Проверяет, корректны ли данные группы.

**Параметры**:
*    `group` (SimpleNamespace): Пространство имен группы, содержащее данные о группе.

**Возвращает**:
*    `bool`: True, если данные группы корректны, иначе False.

**Примеры**:
```python
group = SimpleNamespace(
    group_url='https://www.facebook.com/groups/example',
    group_categories=['sales'],
    status='active',
    language='ru',
    currency='RUB',
    promoted_categories=[],
    promoted_events=[],
    last_promo_sended=None
)
promoter = FacebookPromoter(d=d, promoter='aliexpress')
is_group_valid = promoter.validate_group(group)
print(is_group_valid)