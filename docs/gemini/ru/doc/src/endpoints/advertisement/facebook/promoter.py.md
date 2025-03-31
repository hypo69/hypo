# src.endpoints.advertisement.facebook.promoter

## Обзор

Модуль `src.endpoints.advertisement.facebook.promoter` предназначен для автоматизации процесса продвижения сообщений и событий в группах Facebook. Он обрабатывает кампании и события, публикуя их в группах Facebook, избегая дублирования публикаций.

## Подробней

Модуль содержит класс `FacebookPromoter`, который использует WebDriver для автоматизации действий в браузере. Он позволяет продвигать категории товаров и события в группах Facebook, проверяя интервалы между публикациями и избегая повторной публикации одного и того же контента в одной и той же группе. Модуль также включает функции для логирования ошибок и обновления данных о продвижении групп.

## Классы

### `FacebookPromoter`

**Описание**: Класс для продвижения товаров AliExpress и событий в группах Facebook.

**Как работает класс**: Класс `FacebookPromoter` автоматизирует публикацию рекламных материалов в группах Facebook, используя экземпляр WebDriver. Он гарантирует, что категории товаров и события продвигаются, избегая дубликатов.

- Инициализация класса `FacebookPromoter` требует передачи экземпляра `Driver` (WebDriver), имени промоутера и путей к файлам, содержащим данные о группах Facebook.
- Метод `promote` отвечает за фактическую публикацию контента в группе Facebook. Он проверяет язык и валюту группы, а также вызывает соответствующие функции для публикации сообщений или событий.
- Метод `process_groups` обрабатывает все группы Facebook для текущей кампании или события. Он загружает данные о группах из файлов, проверяет интервалы между публикациями и вызывает метод `promote` для каждой группы.
- Класс использует модуль `logger` для логирования ошибок и отладочной информации.

**Методы**:

- `__init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False)`
- `promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool`
- `log_promotion_error(self, is_event: bool, item_name: str)`
- `update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False)`
- `process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None)`
- `get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace`
- `check_interval(self, group: SimpleNamespace) -> bool`
- `validate_group(self, group: SimpleNamespace) -> bool`

#### `__init__`

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

**Назначение**: Инициализирует промоутер для групп Facebook.

**Как работает функция**: Конструктор класса `FacebookPromoter` инициализирует объект промоутера, принимая экземпляр WebDriver, имя промоутера, пути к файлам групп и флаг отключения видео. Он также инициализирует спиннер для отображения процесса выполнения.

**Параметры**:

- `d` (Driver): Экземпляр WebDriver для автоматизации браузера.
- `promoter` (str): Имя промоутера.
- `group_file_paths` (Optional[list[str | Path] | str | Path], optional): Список путей к файлам, содержащим данные о группах. По умолчанию `None`.
- `no_video` (bool, optional): Флаг, указывающий, следует ли отключать видео в постах. По умолчанию `False`.

**Возвращает**: None

**Вызывает исключения**: None

#### `promote`

```python
    def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
        """Promotes a category or event in a Facebook group."""
        ...
```

**Назначение**: Продвигает категорию или событие в группе Facebook.

**Как работает функция**: Метод `promote` выполняет продвижение контента (категории или события) в указанной группе Facebook. Он проверяет соответствие языка и валюты группы, устанавливает атрибуты события или сообщения и вызывает соответствующие функции для публикации контента. В случае ошибки при публикации, вызывается метод `log_promotion_error`. После успешной публикации обновляются данные о продвижении группы с помощью метода `update_group_promotion_data`.

Внутри функции происходят следующие действия и преобразования:

A
|
-- B
|
C - D
|
E

Где:

- A: Проверка соответствия языка группы заданному языку.
- B: Проверка соответствия валюты группы заданной валюте.
- C: Установка атрибутов события или сообщения в зависимости от того, является ли продвигаемый элемент событием.
- D: Публикация события или сообщения в группе Facebook.
- E: Обновление данных группы после успешной публикации.

**Параметры**:

- `group` (SimpleNamespace): Объект, содержащий данные о группе Facebook.
- `item` (SimpleNamespace): Объект, содержащий данные о продвигаемом контенте (категории или события).
- `is_event` (bool, optional): Флаг, указывающий, является ли продвигаемый контент событием. По умолчанию `False`.
- `language` (str, optional): Язык, на котором нужно продвигать контент. По умолчанию `None`.
- `currency` (str, optional): Валюта, в которой нужно продвигать контент. По умолчанию `None`.

**Возвращает**:

- `bool`: `True`, если продвижение прошло успешно, `False` в противном случае.

**Вызывает исключения**: None

#### `log_promotion_error`

```python
    def log_promotion_error(self, is_event: bool, item_name: str):\n        """Logs promotion error for category or event."""
        ...
```

**Назначение**: Логирует ошибку продвижения для категории или события.

**Как работает функция**: Метод `log_promotion_error` записывает в журнал отладочное сообщение об ошибке, возникшей при продвижении категории или события. Он использует модуль `logger` для записи сообщения с уровнем `DEBUG`.

**Параметры**:

- `is_event` (bool): Флаг, указывающий, является ли продвигаемый элемент событием.
- `item_name` (str): Название продвигаемого элемента (категории или события).

**Возвращает**: None

**Вызывает исключения**: None

#### `update_group_promotion_data`

```python
    def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
        """Updates group promotion data with the new promotion."""
        ...
```

**Назначение**: Обновляет данные о продвижении группы с новой информацией о продвижении.

**Как работает функция**: Метод `update_group_promotion_data` обновляет данные о продвижении группы, добавляя информацию о новой публикации. Он обновляет временную метку последней публикации, добавляет название продвигаемого элемента (категории или события) в список продвигаемых элементов и сохраняет изменения.

**Параметры**:

- `group` (SimpleNamespace): Объект, содержащий данные о группе Facebook.
- `item_name` (str): Название продвигаемого элемента (категории или события).
- `is_event` (bool, optional): Флаг, указывающий, является ли продвигаемый контент событием. По умолчанию `False`.

**Возвращает**: None

**Вызывает исключения**: None

#### `process_groups`

```python
    def process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None):
        """Processes all groups for the current campaign or event promotion."""
        ...
```

**Назначение**: Обрабатывает все группы для текущей кампании или продвижения события.

**Как работает функция**: Метод `process_groups` обрабатывает все группы Facebook для текущей кампании или события. Он загружает данные о группах из файлов, проверяет интервалы между публикациями, фильтрует группы по категориям и статусу, выбирает элемент для продвижения и вызывает метод `promote` для каждой группы.

Внутри функции происходят следующие действия и преобразования:

A
|
-- B
|
C - D
|
E - F
|
G

Где:

- A: Проверка наличия кампании или событий для продвижения.
- B: Перебор файлов групп.
- C: Загрузка данных о группах из файла.
- D: Перебор групп в файле.
- E: Проверка интервала между публикациями для группы.
- F: Фильтрация групп по категориям и статусу.
- G: Выбор элемента для продвижения и вызов метода `promote`.

**Параметры**:

- `campaign_name` (str, optional): Название кампании. По умолчанию `None`.
- `events` (list[SimpleNamespace], optional): Список событий для продвижения. По умолчанию `None`.
- `is_event` (bool, optional): Флаг, указывающий, является ли продвижение событием. По умолчанию `False`.
- `group_file_paths` (list[str], optional): Список путей к файлам, содержащим данные о группах. По умолчанию `None`.
- `group_categories_to_adv` (list[str], optional): Список категорий групп для продвижения. По умолчанию `['sales']`.
- `language` (str, optional): Язык, на котором нужно продвигать контент. По умолчанию `None`.
- `currency` (str, optional): Валюта, в которой нужно продвигать контент. По умолчанию `None`.

**Возвращает**: None

**Вызывает исключения**: None

#### `get_category_item`

```python
    def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace:
        """Fetches the category item for promotion based on the campaign and promoter."""
        ...
```

**Назначение**: Извлекает элемент категории для продвижения на основе кампании и промоутера.

**Как работает функция**: Метод `get_category_item` извлекает элемент категории для продвижения на основе указанной кампании и промоутера. Если промоутер - 'aliexpress', он использует класс `AliCampaignEditor` для получения информации о категории. В противном случае он загружает данные о категории из JSON-файла.

**Параметры**:

- `campaign_name` (str): Название кампании.
- `group` (SimpleNamespace): Объект, содержащий данные о группе Facebook.
- `language` (str): Язык, на котором нужно продвигать контент.
- `currency` (str): Валюта, в которой нужно продвигать контент.

**Возвращает**:

- `SimpleNamespace`: Объект, содержащий данные о категории для продвижения.

**Вызывает исключения**: None

#### `check_interval`

```python
    def check_interval(self, group: SimpleNamespace) -> bool:
        """Checks if enough time has passed for promoting this group."""
        ...
```

**Назначение**: Проверяет, достаточно ли времени прошло для продвижения этой группы.

**Как работает функция**: Метод `check_interval` проверяет, прошло ли достаточно времени с момента последней публикации в группе, чтобы можно было публиковать снова. Если интервал между публикациями недостаточен, метод возвращает `False`, иначе - `True`.

**Параметры**:

- `group` (SimpleNamespace): Объект, содержащий данные о группе Facebook.

**Возвращает**:

- `bool`: `True`, если достаточно времени прошло для продвижения группы, `False` в противном случае.

**Вызывает исключения**: None

#### `validate_group`

```python
    def validate_group(self, group: SimpleNamespace) -> bool:
        """Validates that the group data is correct."""
        ...
```

**Назначение**: Проверяет, корректны ли данные группы.

**Как работает функция**: Метод `validate_group` проверяет, содержит ли объект группы необходимые атрибуты (`group_url` и `group_categories`). Если группа содержит все необходимые атрибуты, метод возвращает `True`, иначе - `False`.

**Параметры**:

- `group` (SimpleNamespace): Объект, содержащий данные о группе Facebook.

**Возвращает**:

- `bool`: `True`, если данные группы корректны, `False` в противном случае.

**Вызывает исключения**: None

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

**Назначение**: Возвращает измененный URL для создания события на Facebook, заменяя `group_id` значением из входного URL.

**Как работает функция**: Функция `get_event_url` принимает URL группы Facebook в качестве входных данных, извлекает идентификатор группы из URL, а затем создает новый URL для создания события в этой группе. Новый URL содержит параметры, необходимые для создания события, включая идентификатор группы.

Внутри функции происходят следующие действия и преобразования:

A
|
-- B
|
C

Где:

- A: Извлечение `group_id` из URL группы.
- B: Определение базового URL для создания события.
- C: Формирование строки запроса с параметрами, включая `group_id`.

**Параметры**:

- `group_url` (str): URL группы Facebook, содержащий `group_id`.

**Возвращает**:

- `str`: Измененный URL для создания события.

**Вызывает исключения**: None