# Документация модуля `FacebookPromoter`

## Обзор

Модуль `FacebookPromoter` автоматизирует процесс продвижения товаров и событий AliExpress в группах Facebook. Модуль управляет публикацией рекламных материалов в Facebook, обеспечивая продвижение категорий и событий без дубликатов. Он использует WebDriver для автоматизации браузера, что обеспечивает эффективное управление рекламными кампаниями.

## Подробней

Модуль `FacebookPromoter` предназначен для автоматизации продвижения товаров и событий AliExpress в группах Facebook. Он позволяет настраивать параметры продвижения, такие как категории товаров, события, язык и валюту. Модуль также отслеживает уже продвинутые элементы, чтобы избежать дублирования публикаций. Для работы с Facebook используется WebDriver, что позволяет автоматизировать взаимодействие с веб-интерфейсом.

## Содержание

1.  [Классы](#Классы)
    *   [`FacebookPromoter`](#FacebookPromoter)
        *   [`__init__`](#__init__)
        *   [`promote`](#promote)
        *   [`log_promotion_error`](#log_promotion_error)
        *   [`update_group_promotion_data`](#update_group_promotion_data)
        *   [`process_groups`](#process_groups)
        *   [`get_category_item`](#get_category_item)
        *   [`check_interval`](#check_interval)
        *   [`validate_group`](#validate_group)
2.  [Лицензия](#Лицензия)

## Классы

### `FacebookPromoter`

Класс `FacebookPromoter` управляет процессом продвижения товаров и событий AliExpress в группах Facebook.

**Принцип работы**:

Класс инициализируется с драйвером WebDriver, именем промоутера и путями к файлам с данными групп Facebook. Он предоставляет методы для продвижения категорий и событий, обновления данных о продвижении, проверки интервалов между продвижениями и валидации данных групп.

**Методы**:

#### `__init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False)`

Инициализирует промоутер Facebook с необходимыми конфигурациями.

**Параметры**:

*   `d` (Driver): Инстанс WebDriver для автоматизации.
*   `promoter` (str): Имя промоутера (например, "aliexpress").
*   `group_file_paths` (Optional[list[str | Path] | str | Path]): Пути к файлам данных групп.
*   `no_video` (bool): Флаг для отключения видео в постах. По умолчанию `False`.

**Как работает метод**:

1.  Инициализирует атрибуты класса, такие как драйвер, имя промоутера, пути к файлам групп и флаг отключения видео.
2.  Устанавливает текущую дату и время.
3.  Инициализирует пустые списки для отслеживания продвинутых категорий и событий.

```ascii
Инициализация атрибутов класса
↓
Установка текущей даты и времени
↓
Инициализация пустых списков для отслеживания продвинутых категорий и событий
```

**Примеры**:

```python
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver

# Создание инстанса драйвера (пример с Chrome)
driver = Driver()

# Пример инициализации класса с указанием всех параметров
promoter = FacebookPromoter(
    d=driver,
    promoter="aliexpress",
    group_file_paths=["path/to/group/file1.json", "path/to/group/file2.json"],
    no_video=True
)
```

#### `promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool`

Продвигает категорию или событие в указанной группе Facebook.

**Параметры**:

*   `group` (SimpleNamespace): Данные группы.
*   `item` (SimpleNamespace): Категория или событие для продвижения.
*   `is_event` (bool): Является ли элемент событием.
*   `language` (str): Язык продвижения.
*   `currency` (str): Валюта для продвижения.

**Возвращает**:

*   `bool`: Успешно ли прошло продвижение.

**Как работает метод**:

1.  Формирует текст поста для продвижения.
2.  Публикует пост в группе Facebook с использованием WebDriver.
3.  Логирует успешное или неуспешное продвижение.
4.  Обновляет данные группы после успешного продвижения.

```ascii
Формирование текста поста
↓
Публикация поста в группе Facebook
↓
Логирование результата продвижения
↓
Обновление данных группы (если успешно)
```

**Примеры**:

```python
from types import SimpleNamespace
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver

# Создание инстанса драйвера
driver = Driver()

# Создание инстанса класса
promoter = FacebookPromoter(d=driver, promoter="aliexpress")

# Пример данных группы и товара/события
group_data = SimpleNamespace(id="1234567890", name="Test Group", last_promotion_time="2024-01-01 00:00:00")
item_data = SimpleNamespace(name="Test Item", url="https://example.com")

# Продвижение товара в группе
success = promoter.promote(group=group_data, item=item_data, is_event=False, language="en", currency="USD")
print(f"Promotion successful: {success}")
```

#### `log_promotion_error(self, is_event: bool, item_name: str)`

Логирует ошибку при неудачном продвижении.

**Параметры**:

*   `is_event` (bool): Является ли элемент событием.
*   `item_name` (str): Имя элемента.

**Как работает метод**:

1.  Формирует сообщение об ошибке на основе типа элемента (событие или категория) и его имени.
2.  Логирует сообщение об ошибке с использованием `logger.error`.

```ascii
Формирование сообщения об ошибке
↓
Логирование сообщения об ошибке
```

**Примеры**:

```python
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver

# Создание инстанса драйвера
driver = Driver()

# Создание инстанса класса
promoter = FacebookPromoter(d=driver, promoter="aliexpress")

# Логирование ошибки продвижения события
promoter.log_promotion_error(is_event=True, item_name="Test Event")
```

#### `update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False)`

Обновляет данные группы после продвижения, добавляя продвинутый элемент в список продвинутых категорий или событий.

**Параметры**:

*   `group` (SimpleNamespace): Данные группы.
*   `item_name` (str): Имя продвинутого элемента.
*   `is_event` (bool): Является ли элемент событием.

**Как работает метод**:

1.  Определяет, продвигается ли событие или категория.
2.  Добавляет имя продвинутого элемента в соответствующий список (`promoted_categories` или `promoted_events`) в данных группы.
3.  Обновляет время последнего продвижения группы.

```ascii
Определение типа продвигаемого элемента (событие или категория)
↓
Добавление имени элемента в соответствующий список
↓
Обновление времени последнего продвижения группы
```

**Примеры**:

```python
from types import SimpleNamespace
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver

# Создание инстанса драйвера
driver = Driver()

# Создание инстанса класса
promoter = FacebookPromoter(d=driver, promoter="aliexpress")

# Пример данных группы
group_data = SimpleNamespace(id="1234567890", name="Test Group", promoted_categories=[], promoted_events=[])

# Обновление данных группы после продвижения категории
promoter.update_group_promotion_data(group=group_data, item_name="Test Category", is_event=False)

# Обновление данных группы после продвижения события
promoter.update_group_promotion_data(group=group_data, item_name="Test Event", is_event=True)

print(f"Promoted categories: {group_data.promoted_categories}")
print(f"Promoted events: {group_data.promoted_events}")
```

#### `process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None)`

Обрабатывает группы для текущей кампании или продвижения события.

**Параметры**:

*   `campaign_name` (str): Имя кампании.
*   `events` (list[SimpleNamespace]): Список событий для продвижения.
*   `is_event` (bool): Продвигать события или категории.
*   `group_file_paths` (list[str]): Пути к файлам данных групп.
*   `group_categories_to_adv` (list[str]): Категории для продвижения.
*   `language` (str): Язык продвижения.
*   `currency` (str): Валюта для продвижения.

**Как работает метод**:

1.  Загружает данные групп из указанных файлов.
2.  Итерируется по каждой группе и проверяет, можно ли ее продвигать (проверка интервала и валидация данных).
3.  Если группа может быть продвинута, получает категорию или событие для продвижения и выполняет продвижение.
4.  Обрабатывает исключения и логирует ошибки.

```ascii
Загрузка данных групп
↓
Итерация по группам
│
├── Проверка возможности продвижения группы (интервал, валидация)
│   │
│   ├── Получение элемента для продвижения (категория/событие)
│   │   ↓
│   └── Продвижение элемента в группе
│
└── Обработка исключений и логирование ошибок
```

**Примеры**:

```python
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver

# Создание инстанса драйвера
driver = Driver()

# Создание инстанса класса
promoter = FacebookPromoter(d=driver, promoter="aliexpress")

# Продвижение категорий "sales" в группах из файла "groups.json"
promoter.process_groups(
    campaign_name="Summer Sales",
    group_file_paths=["groups.json"],
    group_categories_to_adv=["sales"],
    language="en",
    currency="USD"
)

# Продвижение событий в группах из файла "groups.json"
from types import SimpleNamespace
event1 = SimpleNamespace(name="Event 1", url="https://example.com/event1")
event2 = SimpleNamespace(name="Event 2", url="https://example.com/event2")

promoter.process_groups(
    campaign_name="Summer Events",
    events=[event1, event2],
    is_event=True,
    group_file_paths=["groups.json"],
    language="en",
    currency="USD"
)
```

#### `get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace`

Получает элемент категории для продвижения на основе кампании и промоутера.

**Параметры**:

*   `campaign_name` (str): Имя кампании.
*   `group` (SimpleNamespace): Данные группы.
*   `language` (str): Язык для продвижения.
*   `currency` (str): Валюта для продвижения.

**Возвращает**:

*   `SimpleNamespace`: Элемент категории для продвижения.

**Как работает метод**:

1.  Формирует поисковый запрос на основе имени кампании, языка и валюты.
2.  Выполняет поиск товаров на AliExpress с использованием сформированного запроса.
3.  Выбирает случайный товар из результатов поиска.
4.  Возвращает данные выбранного товара в виде `SimpleNamespace`.

```ascii
Формирование поискового запроса
↓
Поиск товаров на AliExpress
↓
Выбор случайного товара из результатов поиска
↓
Возврат данных товара
```

**Примеры**:

```python
from types import SimpleNamespace
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver

# Создание инстанса драйвера
driver = Driver()

# Создание инстанса класса
promoter = FacebookPromoter(d=driver, promoter="aliexpress")

# Пример данных группы
group_data = SimpleNamespace(id="1234567890", name="Test Group")

# Получение товара для продвижения
category_item = promoter.get_category_item(
    campaign_name="Summer Sales",
    group=group_data,
    language="en",
    currency="USD"
)

print(f"Category item: {category_item}")
```

#### `check_interval(self, group: SimpleNamespace) -> bool`

Проверяет, прошло ли достаточно времени для повторного продвижения в этой группе.

**Параметры**:

*   `group` (SimpleNamespace): Данные группы.

**Возвращает**:

*   `bool`: Может ли группа быть продвинута.

**Как работает метод**:

1.  Извлекает время последнего продвижения из данных группы.
2.  Вычисляет время, прошедшее с момента последнего продвижения.
3.  Сравнивает прошедшее время с минимальным интервалом между продвижениями (например, 24 часа).
4.  Возвращает `True`, если прошло достаточно времени, и `False` в противном случае.

```ascii
Извлечение времени последнего продвижения
↓
Вычисление времени, прошедшего с момента последнего продвижения
↓
Сравнение с минимальным интервалом
↓
Возврат результата
```

**Примеры**:

```python
from types import SimpleNamespace
from datetime import datetime, timedelta
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver

# Создание инстанса драйвера
driver = Driver()

# Создание инстанса класса
promoter = FacebookPromoter(d=driver, promoter="aliexpress")

# Пример данных группы с временем последнего продвижения 2 дня назад
last_promotion_time = datetime.now() - timedelta(days=2)
group_data = SimpleNamespace(id="1234567890", name="Test Group", last_promotion_time=last_promotion_time)

# Проверка интервала
can_promote = promoter.check_interval(group=group_data)
print(f"Can promote: {can_promote}")

# Пример данных группы с временем последнего продвижения 12 часов назад
last_promotion_time = datetime.now() - timedelta(hours=12)
group_data = SimpleNamespace(id="1234567890", name="Test Group", last_promotion_time=last_promotion_time)

# Проверка интервала
can_promote = promoter.check_interval(group=group_data)
print(f"Can promote: {can_promote}")
```

#### `validate_group(self, group: SimpleNamespace) -> bool`

Проверяет данные группы, чтобы убедиться, что у нее есть необходимые атрибуты.

**Параметры**:

*   `group` (SimpleNamespace): Данные группы.

**Возвращает**:

*   `bool`: Являются ли данные группы валидными.

**Как работает метод**:

1.  Проверяет наличие обязательных атрибутов в данных группы, таких как `id`, `name` и `last_promotion_time`.
2.  Возвращает `True`, если все обязательные атрибуты присутствуют, и `False` в противном случае.

```ascii
Проверка наличия обязательных атрибутов (id, name, last_promotion_time)
↓
Возврат результата
```

**Примеры**:

```python
from types import SimpleNamespace
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver

# Создание инстанса драйвера
driver = Driver()

# Создание инстанса класса
promoter = FacebookPromoter(d=driver, promoter="aliexpress")

# Пример валидных данных группы
group_data = SimpleNamespace(id="1234567890", name="Test Group", last_promotion_time="2024-01-01 00:00:00")

# Валидация данных группы
is_valid = promoter.validate_group(group=group_data)
print(f"Is valid: {is_valid}")

# Пример невалидных данных группы (отсутствует атрибут "name")
group_data = SimpleNamespace(id="1234567890", last_promotion_time="2024-01-01 00:00:00")

# Валидация данных группы
is_valid = promoter.validate_group(group=group_data)
print(f"Is valid: {is_valid}")
```

## Лицензия

Этот модуль является частью большего пакета **Facebook Promoter** и лицензирован в соответствии с MIT License.