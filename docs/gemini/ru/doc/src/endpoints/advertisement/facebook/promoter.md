# Документация модуля `promoter` для Facebook Promoter

## Обзор

Модуль **Facebook Promoter** автоматизирует процесс продвижения товаров и событий AliExpress в группах Facebook. Модуль отвечает за публикацию рекламных материалов в Facebook, обеспечивая продвижение категорий и событий без дубликатов. Он использует WebDriver для автоматизации работы браузера и эффективного управления рекламными кампаниями.

## Подробнее

Этот модуль предназначен для автоматизации продвижения товаров и событий AliExpress в группах Facebook. Он позволяет настраивать параметры групп, избегать повторных публикаций и управлять процессом продвижения через веб-драйвер.

## Содержание

1.  [Класс `FacebookPromoter`](#класс-facebookpromoter)
    *   [Описание](#описание)
    *   [Методы](#методы)
        *   [`__init__`](#__init__)
        *   [`promote`](#promote)
        *   [`log_promotion_error`](#log_promotion_error)
        *   [`update_group_promotion_data`](#update_group_promotion_data)
        *   [`process_groups`](#process_groups)
        *   [`get_category_item`](#get_category_item)
        *   [`check_interval`](#check_interval)
        *   [`validate_group`](#validate_group)
2.  [Пример использования](#пример-использования)

## Классы

### `FacebookPromoter`

**Описание**:
Этот класс управляет процессом продвижения товаров и событий AliExpress в группах Facebook.

#### Методы

*   `__init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False)`

    **Назначение**: Инициализирует промоутер Facebook с необходимыми конфигурациями.

    **Параметры**:

    *   `d` (Driver): Инстанс WebDriver для автоматизации.
    *   `promoter` (str): Имя промоутера (например, "aliexpress").
    *   `group_file_paths` (Optional[list[str | Path] | str | Path]): Пути к файлам с данными о группах.
    *   `no_video` (bool): Флаг для отключения видео в постах. По умолчанию `False`.

*   `promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool`

    **Назначение**: Продвигает категорию или событие в указанной группе Facebook.

    **Параметры**:

    *   `group` (SimpleNamespace): Данные группы.
    *   `item` (SimpleNamespace): Категория или элемент события для продвижения.
    *   `is_event` (bool): Указывает, является ли продвигаемый элемент событием.
    *   `language` (str): Язык продвижения.
    *   `currency` (str): Валюта для продвижения.

    **Возвращает**:

    *   `bool`: Успешно ли выполнено продвижение.

    **Как работает функция**:

    1.  Функция получает данные о группе и элементе (категории или событии) для продвижения.
    2.  Определяет, является ли продвигаемый элемент событием.
    3.  Выполняет продвижение элемента в указанной группе Facebook.
    4.  Возвращает логическое значение, указывающее на успех или неудачу продвижения.

    **ASCII Flowchart**:

    ```
    A[Начало]
    |
    B[Получение данных группы и элемента]
    |
    C[Определение типа элемента (событие или категория)]
    |
    D[Выполнение продвижения в группе Facebook]
    |
    E[Возврат результата (успех/неудача)]
    |
    F[Конец]
    ```

    **Примеры**:

    ```python
    # Пример вызова функции promote
    group_data = SimpleNamespace(id="12345", name="Test Group")
    item_data = SimpleNamespace(id="67890", title="Test Item")
    result = promoter.promote(group=group_data, item=item_data, is_event=False, language="en", currency="USD")
    print(result)  # Вывод: True или False в зависимости от успеха
    ```

*   `log_promotion_error(self, is_event: bool, item_name: str)`

    **Назначение**: Регистрирует ошибку при неудачном продвижении.

    **Параметры**:

    *   `is_event` (bool): Является ли элемент событием.
    *   `item_name` (str): Название элемента.

    **Как работает функция**:

    1.  Функция получает информацию о том, является ли продвигаемый элемент событием и его название.
    2.  Регистрирует ошибку продвижения в лог.

    **ASCII Flowchart**:

    ```
    A[Начало]
    |
    B[Получение типа элемента и его названия]
    |
    C[Логирование ошибки продвижения]
    |
    D[Конец]
    ```

    **Примеры**:

    ```python
    # Пример вызова функции log_promotion_error
    promoter.log_promotion_error(is_event=True, item_name="Test Event")
    ```

*   `update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False)`

    **Назначение**: Обновляет данные группы после продвижения, добавляя продвинутый элемент в список продвинутых категорий или событий.

    **Параметры**:

    *   `group` (SimpleNamespace): Данные группы.
    *   `item_name` (str): Название продвинутого элемента.
    *   `is_event` (bool): Является ли элемент событием.

    **Как работает функция**:

    1.  Функция получает данные о группе, название продвинутого элемента и информацию о том, является ли элемент событием.
    2.  Обновляет данные группы, добавляя продвинутый элемент в список продвинутых категорий или событий.

    **ASCII Flowchart**:

    ```
    A[Начало]
    |
    B[Получение данных группы, названия элемента и типа элемента]
    |
    C[Обновление данных группы]
    |
    D[Конец]
    ```

    **Примеры**:

    ```python
    # Пример вызова функции update_group_promotion_data
    group_data = SimpleNamespace(id="12345", name="Test Group", promoted_categories=[])
    promoter.update_group_promotion_data(group=group_data, item_name="Test Category", is_event=False)
    ```

*   `process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None)`

    **Назначение**: Обрабатывает группы для текущей кампании или продвижения события.

    **Параметры**:

    *   `campaign_name` (str): Название кампании.
    *   `events` (list[SimpleNamespace]): Список событий для продвижения.
    *   `is_event` (bool): Указывает, нужно ли продвигать события или категории.
    *   `group_file_paths` (list[str]): Пути к файлам с данными о группах.
    *   `group_categories_to_adv` (list[str]): Категории для продвижения.
    *   `language` (str): Язык продвижения.
    *   `currency` (str): Валюта для продвижения.

    **Как работает функция**:

    1.  Функция получает параметры для обработки групп, включая название кампании, список событий, флаг для продвижения событий или категорий, пути к файлам с данными о группах, категории для продвижения, язык и валюту.
    2.  Выполняет обработку групп для продвижения, используя указанные параметры.

    **ASCII Flowchart**:

    ```
    A[Начало]
    |
    B[Получение параметров обработки групп]
    |
    C[Обработка групп для продвижения]
    |
    D[Конец]
    ```

    **Примеры**:

    ```python
    # Пример вызова функции process_groups
    promoter.process_groups(campaign_name="Test Campaign", events=[], is_event=False, group_file_paths=["path/to/group.json"], group_categories_to_adv=["sales"], language="en", currency="USD")
    ```

*   `get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace`

    **Назначение**: Получает элемент категории для продвижения на основе кампании и промоутера.

    **Параметры**:

    *   `campaign_name` (str): Название кампании.
    *   `group` (SimpleNamespace): Данные группы.
    *   `language` (str): Язык для продвижения.
    *   `currency` (str): Валюта для продвижения.

    **Возвращает**:

    *   `SimpleNamespace`: Элемент категории для продвижения.

    **Как работает функция**:

    1.  Функция получает название кампании, данные группы, язык и валюту.
    2.  На основе этих данных получает элемент категории для продвижения.

    **ASCII Flowchart**:

    ```
    A[Начало]
    |
    B[Получение названия кампании, данных группы, языка и валюты]
    |
    C[Получение элемента категории для продвижения]
    |
    D[Возврат элемента категории]
    |
    E[Конец]
    ```

    **Примеры**:

    ```python
    # Пример вызова функции get_category_item
    group_data = SimpleNamespace(id="12345", name="Test Group")
    item = promoter.get_category_item(campaign_name="Test Campaign", group=group_data, language="en", currency="USD")
    print(item)  # Вывод: SimpleNamespace с данными элемента категории
    ```

*   `check_interval(self, group: SimpleNamespace) -> bool`

    **Назначение**: Проверяет, прошло ли достаточно времени для повторного продвижения в этой группе.

    **Параметры**:

    *   `group` (SimpleNamespace): Данные группы.

    **Возвращает**:

    *   `bool`: Может ли группа быть продвинута снова.

    **Как работает функция**:

    1.  Функция получает данные группы.
    2.  Проверяет, прошло ли достаточно времени с момента последнего продвижения в этой группе.
    3.  Возвращает логическое значение, указывающее, можно ли продвигать группу снова.

    **ASCII Flowchart**:

    ```
    A[Начало]
    |
    B[Получение данных группы]
    |
    C[Проверка интервала времени с последнего продвижения]
    |
    D[Возврат результата (можно/нельзя продвигать)]
    |
    E[Конец]
    ```

    **Примеры**:

    ```python
    # Пример вызова функции check_interval
    group_data = SimpleNamespace(id="12345", name="Test Group", last_promotion_time=datetime.now())
    can_promote = promoter.check_interval(group=group_data)
    print(can_promote)  # Вывод: True или False
    ```

*   `validate_group(self, group: SimpleNamespace) -> bool`

    **Назначение**: Проверяет данные группы, чтобы убедиться, что у нее есть необходимые атрибуты.

    **Параметры**:

    *   `group` (SimpleNamespace): Данные группы.

    **Возвращает**:

    *   `bool`: Являются ли данные группы действительными.

    **Как работает функция**:

    1.  Функция получает данные группы.
    2.  Проверяет наличие необходимых атрибутов в данных группы.
    3.  Возвращает логическое значение, указывающее, являются ли данные группы действительными.

    **ASCII Flowchart**:

    ```
    A[Начало]
    |
    B[Получение данных группы]
    |
    C[Проверка наличия необходимых атрибутов]
    |
    D[Возврат результата (действительны/не действительны)]
    |
    E[Конец]
    ```

    **Примеры**:

    ```python
    # Пример вызова функции validate_group
    group_data = SimpleNamespace(id="12345", name="Test Group")
    is_valid = promoter.validate_group(group=group_data)
    print(is_valid)  # Вывод: True или False
    ```

## Пример использования

### Пример использования класса `FacebookPromoter`

```python
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns

# Создание инстанса драйвера (замените на актуальный WebDriver)
d = Driver()

# Создание экземпляра класса FacebookPromoter
promoter = FacebookPromoter(
    d=d,
    promoter="aliexpress",
    group_file_paths=["path/to/group/file1.json", "path/to/group/file2.json"]
)

# Запуск продвижения товаров или событий
promoter.process_groups(
    campaign_name="Campaign1",
    events=[],
    group_categories_to_adv=["sales"],
    language="en",
    currency="USD"
)
```

## Лицензия

Этот модуль является частью пакета **Facebook Promoter** и лицензируется по лицензии MIT.