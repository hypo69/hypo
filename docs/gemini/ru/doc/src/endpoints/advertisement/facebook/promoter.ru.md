# Документация модуля Facebook Promoter

## Обзор

Модуль **Facebook Promoter** автоматизирует продвижение товаров и мероприятий AliExpress в группах Facebook. Модуль управляет публикациями рекламных материалов на Facebook, избегая дублирования. Для эффективного продвижения используется WebDriver для автоматизации браузера.

## Подорбней

Модуль предназначен для автоматизации процесса продвижения товаров и мероприятий в группах Facebook. Он позволяет загружать конфигурации групп из файлов, избегать повторных публикаций одного и того же контента и поддерживает различные языки и валюты для продвижения.  Этот код играет важную роль в автоматизации маркетинговых кампаний в социальных сетях, снижая затраты времени и повышая эффективность продвижения. Модуль использует webdriver для эмуляции действий пользователя в браузере, что позволяет автоматически публиковать контент в группах Facebook.

## Содержание

- [Класс `FacebookPromoter`](#класс-facebookpromoter)
    - [Метод `__init__`](#метод-__init__)
    - [Метод `promote`](#метод-promote)
    - [Метод `log_promotion_error`](#метод-log_promotion_error)
    - [Метод `update_group_promotion_data`](#метод-update_group_promotion_data)
    - [Метод `process_groups`](#метод-process_groups)
    - [Метод `get_category_item`](#метод-get_category_item)
    - [Метод `check_interval`](#метод-check_interval)
    - [Метод `validate_group`](#метод-validate_group)

## Классы

### `FacebookPromoter`

**Описание**:
Этот класс управляет процессом продвижения товаров и мероприятий AliExpress в группах Facebook.

**Принцип работы**:
Класс `FacebookPromoter` инициализируется с использованием экземпляра `WebDriver`, имени промоутера и списка путей к файлам с данными групп. Основной метод `process_groups` обрабатывает группы для продвижения, получая данные о группе, проверяя их валидность и продвигая категории или мероприятия в зависимости от конфигурации. Класс также включает методы для обновления данных о группе, логирования ошибок и проверки интервалов между продвижениями.

```mermaid
flowchart TD
    A[Начало] --> B[Инициализация WebDriver]
    B --> C[Создание экземпляра FacebookPromoter]
    C --> D[Обработка групп для продвижения]
    D --> E[Получение данных о группе]
    E --> F{Данные группы валидны?}
    F -- Да --> G[Получение элемента категории для продвижения]
    F -- Нет --> H[Запись ошибки и завершение]
    G --> I{Группа может быть продвинута?}
    I -- Да --> J[Продвижение категории или мероприятия]
    I -- Нет --> K[Ждать интервал между продвижениями]
    J --> L[Обновление данных о группе]
    K --> L
    L --> M[Завершение]
    H --> M
```

#### Методы

- ##### `__init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False)`

    Инициализирует промоутер для Facebook с необходимыми конфигурациями.

    - **Аргументы:**
        - `d (Driver)`: Экземпляр `WebDriver` для автоматизации.
        - `promoter (str)`: Имя промоутера (например, "aliexpress").
        - `group_file_paths (Optional[list[str  |  Path] | str | Path])`: Пути к файлам с данными групп.
        - `no_video (bool)`: Флаг для отключения видео в публикациях. По умолчанию `False`.

- ##### `promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool`

    Продвигает категорию или мероприятие в указанной группе Facebook.

    - **Аргументы:**
        - `group (SimpleNamespace)`: Данные группы.
        - `item (SimpleNamespace)`: Категория или мероприятие для продвижения.
        - `is_event (bool)`: Является ли элемент мероприятием.
        - `language (str)`: Язык публикации.
        - `currency (str)`: Валюта для продвижения.

    - **Возвращает:**
        - `bool`: Успешно ли прошло продвижение.

- ##### `log_promotion_error(self, is_event: bool, item_name: str)`

    Записывает ошибку, если продвижение не удалось.

    - **Аргументы:**
        - `is_event (bool)`: Является ли элемент мероприятием.
        - `item_name (str)`: Название элемента.

- ##### `update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False)`

    Обновляет данные группы после продвижения, добавляя продвигаемый элемент в список продвигаемых категорий или мероприятий.

    - **Аргументы:**
        - `group (SimpleNamespace)`: Данные группы.
        - `item_name (str)`: Название продвигаемого элемента.
        - `is_event (bool)`: Является ли элемент мероприятием.

- ##### `process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None)`

    Обрабатывает группы для текущей кампании или продвижения мероприятия.

    - **Аргументы:**
        - `campaign_name (str)`: Название кампании.
        - `events (list[SimpleNamespace])`: Список мероприятий для продвижения.
        - `is_event (bool)`: Является ли продвижение мероприятий или категорий.
        - `group_file_paths (list[str])`: Пути к файлам с данными групп.
        - `group_categories_to_adv (list[str])`: Категории для продвижения.
        - `language (str)`: Язык публикации.
        - `currency (str)`: Валюта для продвижения.

- ##### `get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace`

    Получает элемент категории для продвижения в зависимости от кампании и промоутера.

    - **Аргументы:**
        - `campaign_name (str)`: Название кампании.
        - `group (SimpleNamespace)`: Данные группы.
        - `language (str)`: Язык для публикации.
        - `currency (str)`: Валюта для публикации.

    - **Возвращает:**
        - `SimpleNamespace`: Элемент категории для продвижения.

- ##### `check_interval(self, group: SimpleNamespace) -> bool`

    Проверяет, прошло ли достаточно времени, чтобы снова продвигать эту группу.

    - **Аргументы:**
        - `group (SimpleNamespace)`: Данные группы.

    - **Возвращает:**
        - `bool`: Можно ли снова продвигать группу.

- ##### `validate_group(self, group: SimpleNamespace) -> bool`

    Проверяет данные группы, чтобы убедиться в их корректности.

    - **Аргументы:**
        - `group (SimpleNamespace)`: Данные группы.

    - **Возвращает:**
        - `bool`: Корректны ли данные группы.

## Лицензия

Модуль является частью пакета **Facebook Promoter** и лицензируется по лицензии MIT.