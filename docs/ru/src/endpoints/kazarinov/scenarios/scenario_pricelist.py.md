# Модуль исполнения сценария создания мехирона для Сергея Казаринова

## Обзор

Модуль предоставляет функциональность для извлечения, разбора и обработки данных о продуктах от различных поставщиков. Модуль обрабатывает подготовку данных, обработку ИИ и интеграцию с Facebook для публикации продуктов.

## Содержание

1.  [Классы](#классы)
    -   [MexironBuilder](#mexironbuilder)
2.  [Функции](#функции)
    -   [get\_graber\_by\_supplier\_url](#get_graber_by_supplier_url)
    -   [convert\_product\_fields](#convert_product_fields)
    -   [save\_product\_data](#save_product_data)
    -   [process\_ai](#process_ai)
    -   [post\_facebook](#post_facebook)
    -  [create\_report](#create_report)
## Классы

### `MexironBuilder`

**Описание**:
    Обрабатывает извлечение, разбор и сохранение данных о продуктах поставщиков.

**Атрибуты**:

-   `driver` (Playwrid): Экземпляр Playwright.
-   `export_path` (Path): Путь для экспорта данных.
-   `mexiron_name` (str): Имя мехирона.
-    `price` (float): Цена мехирона.
-    `timestamp` (str): Временная метка создания мехирона.
-   `products_list` (List): Список обработанных данных о продуктах.
-   `model` (GoogleGenerativeAI): Экземпляр модели Google Gemini AI.
-   `config` (SimpleNamespace): Конфигурация мехирона.
-   `translations` (SimpleNamespace): Переводы.
-   `update` (Update): Telegram Update.
-   `context` (CallbackContext): Telegram CallbackContext.

**Методы**:

-   `__init__`: Инициализирует класс `MexironBuilder`.
-   `run_scenario`: Запускает сценарий обработки данных.

#### `__init__`

```python
def __init__(self, mexiron_name: Optional[str] = None) -> None:
    """
    Args:
        mexiron_name (Optional[str], optional): Название мехирона. По умолчанию `None`.
    
    Returns:
        None
    
    Raises:
        Exception: Если не удается загрузить конфигурацию или создать путь экспорта.
    """
```

**Описание**:
    Инициализирует класс `MexironBuilder` с необходимыми компонентами.

**Параметры**:
-   `mexiron_name` (Optional[str], optional): Пользовательское имя для процесса Mexiron. По умолчанию `None`.

**Возвращает**:
-   `None`

**Вызывает исключения**:
-   `Exception`: Если не удается загрузить конфигурацию или создать путь экспорта.

#### `run_scenario`

```python
async def run_scenario(
    self,
    update: Update,
    context: CallbackContext,
    urls: list[str],
    price: Optional[str] = '',
    mexiron_name: Optional[str] = '',
) -> bool:
    """
    Args:
        update (Update): Telegram update object.
        context (CallbackContext): Telegram context object.
        urls (list[str]): Список URL для парсинга.
        price (Optional[str], optional): Цена продукта. По умолчанию ''.
        mexiron_name (Optional[str], optional): Название мехирона. По умолчанию ''.
    
    Returns:
        bool: True в случае успешного выполнения, иначе False.
    
    Raises:
        Exception: Если во время выполнения возникла ошибка.
    """
```

**Описание**:
    Выполняет сценарий: разбирает продукты, обрабатывает их через AI и сохраняет данные.

**Параметры**:

-   `update` (Update): Telegram update object.
-   `context` (CallbackContext): Telegram context object.
-   `urls` (list[str]): Список URL для парсинга.
-   `price` (Optional[str], optional): Цена для обработки. По умолчанию ''.
-   `mexiron_name` (Optional[str], optional): Пользовательское имя Mexiron. По умолчанию ''.

**Возвращает**:
-   `bool`: `True`, если сценарий выполнен успешно, иначе `False`.

## Функции

### `get_graber_by_supplier_url`

```python
def get_graber_by_supplier_url(self, url: str) -> Optional[object]:
    """
    Args:
        url (str): URL страницы поставщика.
    
    Returns:
        Optional[object]: Экземпляр грабера, если он найден, иначе None.
    """
```

**Описание**:
    Возвращает соответствующий грабер для заданного URL поставщика.
    Для каждого поставщика реализован свой грабер, который извлекает значения полей с целевой html-страницы.

**Параметры**:
-   `url` (str): URL страницы поставщика.

**Возвращает**:
-   `Optional[object]`: Экземпляр грабера, если он найден, иначе `None`.

### `convert_product_fields`

```python
async def convert_product_fields(self, f: ProductFields) -> dict:
    """
    Args:
        f (ProductFields): Объект, содержащий разобранные данные продукта.
    
    Returns:
        dict: Отформатированный словарь данных продукта.
    """
```

**Описание**:
    Преобразует поля продукта в словарь.
    Функция конвертирует поля из объекта `ProductFields` в простой словарь для модели ИИ.

**Параметры**:
-   `f` (ProductFields): Объект, содержащий разобранные данные продукта.

**Возвращает**:
-   `dict`: Отформатированный словарь данных продукта.

### `save_product_data`

```python
async def save_product_data(self, product_data: dict) -> bool:
    """
    Args:
        product_data (dict): Отформатированные данные продукта.

    Returns:
        bool: True, если данные успешно сохранены, иначе None.
    """
```

**Описание**:
    Сохраняет данные об отдельном продукте в файл.

**Параметры**:
-   `product_data` (dict): Отформатированные данные продукта.

**Возвращает**:
-   `bool`: `True`, если данные успешно сохранены, иначе `None`.

### `process_ai`

```python
async def process_ai(self, products_list: List[str], lang:str,  attempts: int = 3) -> dict | bool:
    """
    Args:
        products_list (List[str]): Список словарей с данными о продуктах.
        lang (str): Язык перевода.
        attempts (int, optional): Количество попыток для повтора запроса в случае сбоя. По умолчанию 3.
    
    Returns:
       dict | bool: Обработанный ответ в формате словаря, False в случае неудачи.
    """
```

**Описание**:
    Обрабатывает список продуктов через модель ИИ.

**Параметры**:
-   `products_list` (List[str]): Список словарей с данными о продуктах.
-   `lang` (str): Язык перевода.
-   `attempts` (int, optional): Количество попыток для повтора запроса в случае сбоя. По умолчанию `3`.

**Возвращает**:
-   `dict | bool`: Обработанный ответ в формате словаря, `False` в случае неудачи.

### `post_facebook`

```python
async def post_facebook(self, mexiron: SimpleNamespace) -> bool:
    """
    Args:
        mexiron (SimpleNamespace): Пространство имен с данными о мехироне.
    
    Returns:
        bool: True в случае успеха, False в противном случае.
    """
```

**Описание**:
    Функция выполняет сценарий рекламного модуля `facebook`.

**Параметры**:
-   `mexiron` (SimpleNamespace): Пространство имен с данными о мехироне.

**Возвращает**:
-   `bool`: `True` в случае успеха, `False` в противном случае.

### `create_report`

```python
async def create_report(self, data: dict, lang:str, html_file: Path, pdf_file: Path) -> bool:
    """
    Args:
        data (dict): Словарь с данными о мехироне.
        lang (str): Язык отчета.
        html_file (Path): Путь к html файлу.
        pdf_file (Path): Путь к pdf файлу.

    Returns:
        bool: True если отчет создан и отправлен боту, иначе False.
    """
```

**Описание**:
    Функция отправляет задание на создание мехирона в формате `html` и `pdf`.
    Если мехирон в `pdf` создался (`generator.create_report()` вернул `True`) - отправить его боту.

**Параметры**:
-   `data` (dict): Словарь с данными о мехироне.
-   `lang` (str): Язык отчета.
-   `html_file` (Path): Путь к `html` файлу.
-   `pdf_file` (Path): Путь к `pdf` файлу.

**Возвращает**:
-   `bool`: `True` если отчет создан и отправлен боту, иначе `False`.