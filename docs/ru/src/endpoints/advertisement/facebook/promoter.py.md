# Модуль для продвижения в Facebook

## Обзор

Модуль `promoter.py` предназначен для автоматизации процесса продвижения сообщений и событий в группах Facebook. Он обрабатывает кампании и события, публикуя их в группах Facebook, избегая при этом дублирования публикаций. Модуль содержит классы и функции для взаимодействия с Facebook через веб-драйвер, чтения данных из файлов, логирования и обработки ошибок.

## Подробней

Этот модуль является частью системы для автоматизации маркетинговых кампаний в Facebook. Он использует веб-драйвер для эмуляции действий пользователя в браузере, таких как публикация сообщений и событий в группах. Модуль также включает функциональность для предотвращения повторной публикации одного и того же контента в одной и той же группе.

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
    ...
```

**Назначение**: Формирует URL для создания события в Facebook группе на основе URL группы.

**Параметры**:
- `group_url` (str): URL Facebook группы, содержащий `group_id`.

**Возвращает**:
- `str`: Модифицированный URL для создания события.

**Как работает функция**:

1. **Извлечение `group_id`**: Извлекает `group_id` из переданного URL группы.
2. **Формирование базового URL**: Создает базовый URL для создания события.
3. **Подготовка параметров**: Формирует словарь с параметрами, необходимыми для создания события, включая `acontext`, `dialog_entry_point` и `group_id`.
4. **Кодирование параметров**: Кодирует параметры в строку запроса.
5. **Объединение URL и параметров**: Объединяет базовый URL и строку запроса для получения полного URL для создания события.

```ascii
    group_url --> Извлечение group_id --> Формирование базового URL --> Подготовка параметров --> Кодирование параметров --> Объединение URL и параметров --> event_url
```

**Примеры**:

```python
group_url = "https://www.facebook.com/groups/1234567890/"
event_url = get_event_url(group_url)
print(event_url)  # Вывод: https://www.facebook.com/events/create/?acontext=%7B%22event_action_history%22%3A%5B%7B%22surface%22%3A%22group%22%7D%2C%7B%22mechanism%22%3A%22upcoming_events_for_group%22%2C%22surface%22%3A%22group%22%7D%5D%2C%22ref_notif_type%22%3Anull%7D&dialog_entry_point=group_events_tab&group_id=1234567890
```

## Классы

### `FacebookPromoter`

**Описание**: Класс для продвижения товаров и событий AliExpress в группах Facebook.

**Принцип работы**:
Класс `FacebookPromoter` автоматизирует процесс публикации рекламных материалов в группах Facebook. Он использует экземпляр веб-драйвера для взаимодействия с Facebook, а также методы для чтения данных о группах и рекламных материалах из файлов. Класс обеспечивает проверку интервалов между публикациями, чтобы избежать спама, и логирование ошибок.

**Атрибуты**:
- `d` (Driver): Экземпляр веб-драйвера для автоматизации браузера.
- `group_file_paths` (str | Path): Путь к файлу или списку файлов, содержащих данные о группах Facebook.
- `no_video` (bool): Флаг, указывающий, следует ли отключать видео в постах.
- `promoter` (str): Имя промоутера.
- `spinner`: Объект для отображения спиннера в консоли во время выполнения операций.

**Методы**:
- `__init__`: Инициализирует промоутер для групп Facebook.
- `promote`: Продвигает категорию или событие в группе Facebook.
- `log_promotion_error`: Логирует ошибку продвижения категории или события.
- `update_group_promotion_data`: Обновляет данные о продвижении группы.
- `process_groups`: Обрабатывает все группы для продвижения кампании или события.
- `get_category_item`: Получает элемент категории для продвижения на основе кампании и промоутера.
- `check_interval`: Проверяет, достаточно ли времени прошло для продвижения этой группы.
- `validate_group`: Проверяет, корректны ли данные группы.

### `FacebookPromoter.__init__`

```python
    def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False):
        """ Initializes the promoter for Facebook groups.

        Args:
            d (Driver): WebDriver instance for browser automation.
            group_file_paths (list[str | Path] | str | Path): List of file paths containing group data.
            no_video (bool, optional): Flag to disable videos in posts. Defaults to False.
        """
        ...
```

**Назначение**: Инициализирует экземпляр класса `FacebookPromoter`.

**Параметры**:
- `d` (Driver): Экземпляр веб-драйвера для автоматизации браузера.
- `promoter` (str): Имя промоутера.
- `group_file_paths` (Optional[list[str | Path] | str | Path], optional): Список путей к файлам, содержащим данные о группах Facebook. По умолчанию `None`.
- `no_video` (bool, optional): Флаг, указывающий, следует ли отключать видео в постах. По умолчанию `False`.

**Как работает функция**:

1. **Инициализация атрибутов**: Инициализирует атрибуты класса значениями, переданными в качестве аргументов.
2. **Определение путей к файлам групп**: Если `group_file_paths` не указан, используется функция `get_filenames` для получения списка файлов из директории `gs.path.google_drive / 'facebook' / 'groups'`.
3. **Инициализация спиннера**: Создает экземпляр класса `spinning_cursor` для отображения спиннера в консоли.

```ascii
    d, promoter, group_file_paths, no_video --> Инициализация атрибутов --> Определение путей к файлам групп --> Инициализация спиннера
```

**Примеры**:

```python
from src.webdriver.driver import Driver, Chrome
from pathlib import Path

# Создание инстанса драйвера (пример с Chrome)
driver = Driver(Chrome)

# Пример инициализации FacebookPromoter с указанием параметров
promoter = FacebookPromoter(d=driver, promoter='aliexpress', group_file_paths=['groups.json'], no_video=True)

# Пример инициализации FacebookPromoter без указания group_file_paths
promoter = FacebookPromoter(d=driver, promoter='aliexpress')
```

### `FacebookPromoter.promote`

```python
    def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
        """Promotes a category or event in a Facebook group.""" 
        ...
```

**Назначение**: Продвигает категорию или событие в группе Facebook.

**Параметры**:
- `group` (SimpleNamespace): Объект, представляющий группу Facebook.
- `item` (SimpleNamespace): Объект, представляющий категорию или событие для продвижения.
- `is_event` (bool, optional): Флаг, указывающий, является ли продвигаемый элемент событием. По умолчанию `False`.
- `language` (str, optional): Язык продвижения. По умолчанию `None`.
- `currency` (str, optional): Валюта продвижения. По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если продвижение прошло успешно, `False` в противном случае.

**Как работает функция**:

1. **Проверка языка и валюты**: Если указаны язык и валюта, проверяется, соответствуют ли они языку и валюте группы. Если нет, функция завершается.
2. **Установка имени элемента**: Определяется имя элемента для продвижения (название события или название категории).
3. **Получение объекта сообщения или события**: Получает объект сообщения или события на языке группы.
4. **Установка атрибутов события**: Если продвигается событие, устанавливаются атрибуты `start`, `end` и `promotional_link`.
5. **Публикация сообщения или события**: В зависимости от типа промоутера и типа продвигаемого элемента вызывается соответствующая функция для публикации сообщения или события.
6. **Обновление данных группы**: После успешной публикации вызывается функция `update_group_promotion_data` для обновления данных о продвижении группы.

```ascii
    group, item, is_event, language, currency --> Проверка языка и валюты --> Установка имени элемента --> Получение объекта сообщения или события --> Установка атрибутов события (если is_event) --> Публикация сообщения или события --> Обновление данных группы --> Возврат True
```

**Примеры**:

```python
from types import SimpleNamespace
from src.webdriver.driver import Driver, Chrome

# Создание инстанса драйвера (пример с Chrome)
driver = Driver(Chrome)

# Пример объекта группы
group = SimpleNamespace(
    group_url='https://www.facebook.com/groups/1234567890/',
    language='ru',
    currency='USD'
)

# Пример объекта товара
item = SimpleNamespace(
    category_name='sale',
    language=SimpleNamespace(ru='Продажа')
)

# Пример объекта события
event = SimpleNamespace(
    event_name='New Year Party',
    language=SimpleNamespace(ru='Новогодняя вечеринка'),
    start='2024-12-31',
    end='2025-01-01',
    promotional_link='https://example.com'
)

# Пример промоутера
promoter = FacebookPromoter(d=driver, promoter='aliexpress')

# Пример продвижения категории
promoter.promote(group=group, item=item)

# Пример продвижения события
promoter.promote(group=group, item=event, is_event=True)
```

### `FacebookPromoter.log_promotion_error`

```python
    def log_promotion_error(self, is_event: bool, item_name: str):
        """Logs promotion error for category or event."""
        logger.debug(f"Error while posting {\'event\' if is_event else \'category\'} {item_name}", None, False)
```

**Назначение**: Логирует ошибку продвижения категории или события.

**Параметры**:
- `is_event` (bool): Флаг, указывающий, является ли продвигаемый элемент событием.
- `item_name` (str): Название элемента (категории или события).

**Как работает функция**:

1. **Формирование сообщения**: Формирует сообщение об ошибке, включающее тип элемента (событие или категория) и его название.
2. **Логирование сообщения**: Логирует сообщение об ошибке с использованием метода `logger.debug`.

```ascii
    is_event, item_name --> Формирование сообщения --> Логирование сообщения
```

**Примеры**:

```python
from src.logger.logger import logger
from src.webdriver.driver import Driver, Chrome
# Создание инстанса драйвера (пример с Chrome)
driver = Driver(Chrome)

# Пример промоутера
promoter = FacebookPromoter(d=driver, promoter='aliexpress')

# Пример логирования ошибки продвижения категории
promoter.log_promotion_error(is_event=False, item_name='sale')

# Пример логирования ошибки продвижения события
promoter.log_promotion_error(is_event=True, item_name='New Year Party')
```

### `FacebookPromoter.update_group_promotion_data`

```python
    def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
        """Updates group promotion data with the new promotion.""" 
        timestamp = datetime.now().strftime("%d/%m/%y %H:%M")
        group.last_promo_sended = gs.now
        if is_event:
            group.promoted_events = group.promoted_events if isinstance(group.promoted_events, list) else [group.promoted_events]
            group.promoted_events.append(item_name)
        else:
            group.promoted_categories = group.promoted_categories if isinstance(group.promoted_categories, list) else [group.promoted_categories]
            group.promoted_categories.append(item_name)
        group.last_promo_sended = timestamp
```

**Назначение**: Обновляет данные о продвижении группы.

**Параметры**:
- `group` (SimpleNamespace): Объект, представляющий группу Facebook.
- `item_name` (str): Название элемента (категории или события).
- `is_event` (bool, optional): Флаг, указывающий, является ли продвигаемый элемент событием. По умолчанию `False`.

**Как работает функция**:

1. **Получение временной метки**: Получает текущую временную метку в формате "%d/%m/%y %H:%M".
2. **Обновление времени последней отправки промо**: Устанавливает время последней отправки промо в группе.
3. **Обновление списка продвигаемых событий или категорий**: В зависимости от типа продвигаемого элемента (событие или категория) добавляет название элемента в список продвигаемых событий или категорий группы.
    - Если список не существует, он создается.
4. **Обновление времени последней отправки промо**: Устанавливает время последней отправки промо в группе.

```ascii
    group, item_name, is_event --> Получение временной метки --> Обновление времени последней отправки промо --> Обновление списка продвигаемых событий или категорий --> Обновление времени последней отправки промо
```

**Примеры**:

```python
from types import SimpleNamespace
from datetime import datetime
from src.webdriver.driver import Driver, Chrome

# Создание инстанса драйвера (пример с Chrome)
driver = Driver(Chrome)

# Пример объекта группы
group = SimpleNamespace(
    group_url='https://www.facebook.com/groups/1234567890/',
    language='ru',
    currency='USD',
    promoted_events=[],
    promoted_categories=[]
)

# Пример промоутера
promoter = FacebookPromoter(d=driver, promoter='aliexpress')

# Пример обновления данных о продвижении категории
promoter.update_group_promotion_data(group=group, item_name='sale')

# Пример обновления данных о продвижении события
promoter.update_group_promotion_data(group=group, item_name='New Year Party', is_event=True)

print(group.promoted_events)
print(group.promoted_categories)
print(group.last_promo_sended)
```

### `FacebookPromoter.process_groups`

```python
    def process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None):
        """Processes all groups for the current campaign or event promotion."""    
        ...
```

**Назначение**: Обрабатывает все группы для продвижения текущей кампании или события.

**Параметры**:
- `campaign_name` (str, optional): Название кампании. По умолчанию `None`.
- `events` (list[SimpleNamespace], optional): Список событий для продвижения. По умолчанию `None`.
- `is_event` (bool, optional): Флаг, указывающий, является ли продвижение событийным. По умолчанию `False`.
- `group_file_paths` (list[str], optional): Список путей к файлам групп. По умолчанию `None`.
- `group_categories_to_adv` (list[str], optional): Список категорий групп для продвижения. По умолчанию `['sales']`.
- `language` (str, optional): Язык продвижения. По умолчанию `None`.
- `currency` (str, optional): Валюта продвижения. По умолчанию `None`.

**Как работает функция**:

1. **Проверка наличия кампании или событий**: Проверяет, есть ли что продвигать. Если нет, функция завершается.
2. **Перебор файлов групп**: Перебирает файлы групп, указанные в `group_file_paths`.
3. **Чтение данных о группах**: Читает данные о группах из файла с использованием функции `j_loads_ns`.
4. **Перебор групп**: Перебирает группы в файле.
5. **Проверка интервала**: Если продвижение не событийное, проверяет, прошло ли достаточно времени с момента последней публикации в группе.
6. **Проверка категорий и статуса группы**: Проверяет, соответствуют ли категории группы категориям для продвижения и является ли группа активной.
7. **Получение элемента для продвижения**: В зависимости от типа продвижения (событие или категория) получает элемент для продвижения.
8. **Проверка, был ли элемент уже продвинут**: Проверяет, был ли элемент уже продвинут в этой группе.
9. **Проверка языка и валюты**: Проверяет, соответствуют ли язык и валюта группы языку и валюте продвижения.
10. **Переход по URL группы**: Открывает URL группы в браузере.
11. **Продвижение элемента**: Продвигает элемент в группе с использованием функции `self.promote`.
12. **Сохранение данных о группах**: Сохраняет обновленные данные о группах в файл.
13. **Ожидание**: Приостанавливает выполнение скрипта на случайное время.

```ascii
    campaign_name, events, is_event, group_file_paths, group_categories_to_adv, language, currency --> Проверка наличия кампании или событий --> Перебор файлов групп --> Чтение данных о группах --> Перебор групп --> Проверка интервала (если не is_event) --> Проверка категорий и статуса группы --> Получение элемента для продвижения --> Проверка, был ли элемент уже продвинут --> Проверка языка и валюты --> Переход по URL группы --> Продвижение элемента --> Сохранение данных о группах --> Ожидание
```

**Примеры**:

```python
from types import SimpleNamespace
from src import gs
from src.webdriver.driver import Driver, Chrome
from pathlib import Path

# Создание инстанса драйвера (пример с Chrome)
driver = Driver(Chrome)

# Пример объекта события
event = SimpleNamespace(
    event_name='New Year Party',
    language=SimpleNamespace(ru='Новогодняя вечеринка'),
    start='2024-12-31',
    end='2025-01-01',
    promotional_link='https://example.com',
    name = "test_event"
)

# Создание файла groups.json
groups_data = {
    "https://www.facebook.com/groups/1234567890/": {
        "language": "ru",
        "currency": "USD",
        "group_categories": ["sales"],
        "status": "active",
        "promoted_events": [],
        "promoted_categories": []
    }
}
import json
file_path = Path("groups.json")
with open(file_path, 'w') as f:
    json.dump(groups_data, f)

# Пример промоутера
promoter = FacebookPromoter(d=driver, promoter='aliexpress')
gs.path.google_drive = Path('.')
# Пример продвижения события
promoter.process_groups(events=[event], is_event=True, group_file_paths=[file_path.name], language='ru', currency='USD')
```

### `FacebookPromoter.get_category_item`

```python
    def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace:\n        """Fetches the category item for promotion based on the campaign and promoter."""    
        ...
```

**Назначение**: Получает элемент категории для продвижения на основе кампании и промоутера.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `group` (SimpleNamespace): Объект, представляющий группу Facebook.
- `language` (str): Язык продвижения.
- `currency` (str): Валюта продвижения.

**Возвращает**:
- `SimpleNamespace`: Объект, представляющий элемент категории для продвижения.

**Как работает функция**:

1. **Определение промоутера**: Определяет, какой промоутер используется (aliexpress или другой).
2. **Для aliexpress**:
    - Импортирует класс `AliCampaignEditor`.
    - Создает экземпляр класса `AliCampaignEditor`.
    - Получает список категорий.
    - Выбирает случайную категорию из списка.
    - Получает элемент категории.
    - Получает продукты категории.
3. **Для другого промоутера**:
    - Формирует путь к файлу с данными о кампаниях.
    - Читает данные о кампаниях из файла с использованием функции `j_loads_ns`.
    - Преобразует категории в список для перемешивания.
    - Перемешивает категории.
    - Перебирает категории.
    - Читает описание категории из файла.
    - Формирует путь к изображениям категории.
    - Получает список изображений категории.
    - Выбирает первое изображение из списка.

```ascii
    campaign_name, group, language, currency --> Определение промоутера --> (aliexpress) Импорт AliCampaignEditor --> Создание экземпляра AliCampaignEditor --> Получение списка категорий --> Выбор случайной категории --> Получение элемента категории --> Получение продуктов категории --> (другой) Формирование пути к файлу кампании --> Чтение данных о кампаниях --> Преобразование категорий в список --> Перемешивание категорий --> Перебор категорий --> Чтение описания категории --> Формирование пути к изображениям --> Получение списка изображений --> Выбор первого изображения
```

**Примеры**:

```python
from types import SimpleNamespace
from src import gs
from src.webdriver.driver import Driver, Chrome
from pathlib import Path

# Создание инстанса драйвера (пример с Chrome)
driver = Driver(Chrome)

# Пример объекта группы
group = SimpleNamespace(
    group_url='https://www.facebook.com/groups/1234567890/',
    language='ru',
    currency='USD',
    promoted_events=[],
    promoted_categories=[]
)

# Пример промоутера
promoter = FacebookPromoter(d=driver, promoter='aliexpress')
gs.path.google_drive = Path('.')

# Пример получения элемента категории
item = promoter.get_category_item(campaign_name='test_campaign', group=group, language='ru', currency='USD')
```

### `FacebookPromoter.check_interval`

```python
    def check_interval(self, group: SimpleNamespace) -> bool:\n        """Checks if enough time has passed for promoting this group."""   
        ...
```

**Назначение**: Проверяет, прошло ли достаточно времени для продвижения этой группы.

**Параметры**:
- `group` (SimpleNamespace): Объект, представляющий группу Facebook.

**Возвращает**:
- `bool`: `True`, если достаточно времени прошло, `False` в противном случае.

**Как работает функция**:
Функция всегда возвращает `True`.

```ascii
    group --> Возврат True
```

**Примеры**:

```python
from types import SimpleNamespace
from src.webdriver.driver import Driver, Chrome

# Создание инстанса драйвера (пример с Chrome)
driver = Driver(Chrome)

# Пример объекта группы
group = SimpleNamespace(
    group_url='https://www.facebook.com/groups/1234567890/',
    language='ru',
    currency='USD',
    promoted_events=[],
    promoted_categories=[]
)

# Пример промоутера
promoter = FacebookPromoter(d=driver, promoter='aliexpress')

# Пример проверки интервала
result = promoter.check_interval(group=group)
print(result)
```

### `FacebookPromoter.validate_group`

```python
    def validate_group(self, group: SimpleNamespace) -> bool:\n        """Validates that the group data is correct."""   
        return group and hasattr(group, \'group_url\') and hasattr(group, \'group_categories\')
```

**Назначение**: Проверяет, корректны ли данные группы.

**Параметры**:
- `group` (SimpleNamespace): Объект, представляющий группу Facebook.

**Возвращает**:
- `bool`: `True`, если данные группы корректны, `False` в противном случае.

**Как работает функция**:

1. **Проверка наличия группы**: Проверяет, существует ли объект группы.
2. **Проверка наличия атрибутов**: Проверяет, есть ли у группы атрибуты `group_url` и `group_categories`.

```ascii
    group --> Проверка наличия группы --> Проверка наличия атрибутов --> Возврат True или False
```

**Примеры**:

```python
from types import SimpleNamespace
from src.webdriver.driver import Driver, Chrome

# Создание инстанса драйвера (пример с Chrome)
driver = Driver(Chrome)

# Пример объекта группы
group = SimpleNamespace(
    group_url='https://www.facebook.com/groups/1234567890/',
    language='ru',
    currency='USD',
    group_categories = []
)

# Пример промоутера
promoter = FacebookPromoter(d=driver, promoter='aliexpress')

# Пример проверки данных группы
result = promoter.validate_group(group=group)
print(result)
```