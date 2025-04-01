# Модуль для управления рекламными кампаниями на AliExpress

## Обзор

Модуль `ali_promo_campaign.py` предназначен для управления рекламными кампаниями на платформе AliExpress. Он включает в себя функциональность для обработки данных о категориях и товарах, создания и редактирования JSON-файлов с информацией о кампаниях, а также использования AI для генерации данных о кампаниях.

## Подробнее

Этот модуль предоставляет класс `AliPromoCampaign`, который позволяет загружать и обрабатывать данные рекламных кампаний, управлять категориями и товарами, а также использовать искусственный интеллект для генерации описаний и других данных. Модуль поддерживает различные языки и валюты, обеспечивая гибкость в настройке кампаний.

## Классы

### `AliPromoCampaign`

**Описание**: Класс `AliPromoCampaign` предназначен для управления рекламной кампанией на AliExpress.

**Принцип работы**:
Класс позволяет инициализировать рекламную кампанию, загружать данные о кампаниях из JSON-файлов, обрабатывать категории и товары, использовать AI для генерации контента, а также сохранять результаты в файлы.

**Аттрибуты**:
- `language` (str): Язык, используемый в кампании.
- `currency` (str): Валюта, используемая в кампании.
- `base_path` (Path): Базовый путь к директории кампании в Google Drive.
- `campaign_name` (str): Название кампании.
- `campaign` (SimpleNamespace): Объект, представляющий данные кампании.
- `campaign_ai` (SimpleNamespace): Объект, представляющий AI-генерированные данные кампании.
- `gemini` (GoogleGenerativeAI): Объект для взаимодействия с моделью Gemini.
- `openai` (OpenAIModel): Объект для взаимодействия с моделью OpenAI.

**Методы**:
- `__init__`: Инициализирует объект `AliPromoCampaign`.
- `_models_payload`: Настраивает модели AI.
- `process_campaign`: Итерируется по категориям кампании и обрабатывает товары.
- `process_campaign_category`: Обрабатывает указанную категорию кампании для всех языков и валют.
- `process_new_campaign`: Создает новую рекламную кампанию.
- `process_ai_category`: Обрабатывает AI-генерацию данных для категории.
- `process_category_products`: Обрабатывает товары в указанной категории.
- `dump_category_products_files`: Сохраняет данные о товарах в JSON-файлы.
- `set_categories_from_directories`: Устанавливает категории кампании из названий директорий.
- `generate_output`: Сохраняет данные о товарах в различных форматах.
- `generate_html`: Создает HTML-файл для категории.
- `generate_html_for_campaign`: Генерирует HTML-страницы для рекламной кампании.

## Функции

### `__init__`

```python
def __init__(
    self,
    campaign_name: str,
    language: Optional[str] = None,
    currency: Optional[str] = None,
    model:str = 'openai'
):
    """Инициализация объекта AliPromoCampaign для рекламной кампании.

    Args:
        campaign_file (Optional[str | Path]): Путь к файлу кампании или ссылка для загрузки кампании.
        campaign_name (Optional[str]): Название кампании.
        language (Optional[str | dict]): Язык, используемый в кампании.
        currency (Optional[str]): Валюта, используемая в кампании.

    Returns:
        SimpleNamespace: Объект, представляющий кампанию.

    Example:
        >>> campaign = AliPromoCampaign(campaign_name="SummerSale", language="EN", currency="USD")
        >>> print(campaign.campaign_name)

    """
```

**Назначение**: Инициализирует объект `AliPromoCampaign` для работы с рекламной кампанией.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `language` (Optional[str]): Язык, используемый в кампании. По умолчанию `None`.
- `currency` (Optional[str]): Валюта, используемая в кампании. По умолчанию `None`.
- `model` (str):  Модель AI, используемая в кампании. По умолчанию 'openai'.

**Как работает функция**:

1. **Определение пути к файлу кампании**: Функция строит путь к файлу кампании на Google Drive, основываясь на имени кампании, языке и валюте.
2. **Загрузка данных кампании**: Попытка загрузить данные кампании из JSON-файла. Если файл не найден, начинается процесс создания новой рекламной кампании.
3. **Обработка существующей кампании**: Если файл кампании найден, устанавливаются язык и валюта кампании.
4. **Инициализация AI моделей**: Вызывается метод `_models_payload` для настройки AI моделей.

```ascii
    Определение параметров
    │
    ├─────────────────────────────
    │
    ▼
    Построение пути к файлу кампании
    │
    ├─────────────────────────────
    │
    ▼
    Попытка загрузки данных из JSON
    │
    ├─────────────────────────────
    │
    ▼
    Проверка наличия файла
    ├── Да: Установка языка и валюты
    │   Инициализация AI моделей
    │
    └── Нет: Запуск процесса создания новой кампании
```

**Примеры**:

```python
campaign = AliPromoCampaign(campaign_name="SummerSale", language="EN", currency="USD")
print(campaign.campaign_name)
```

### `_models_payload`

```python
def _models_payload(self):
    """ """
```

**Назначение**: Настраивает AI модели, используемые в кампании.

**Как работает функция**:

1. **Определение пути к системной инструкции**: Функция определяет путь к файлу с системными инструкциями для AI моделей.
2. **Чтение системной инструкции**: Считывает содержимое файла системной инструкции.
3. **Инициализация моделей**: Инициализирует модели Google Gemini и OpenAI с использованием системной инструкции.

```ascii
    Определение пути к системной инструкции
    │
    ├─────────────────────────────
    │
    ▼
    Чтение системной инструкции
    │
    ├─────────────────────────────
    │
    ▼
    Инициализация моделей Google Gemini и OpenAI
```

### `process_campaign`

```python
def process_campaign(self):
    """Функция итерируется по категориям рекламной кампании и обрабатывает товары категории через генератор партнерских ссылок.

    Example:
        >>> campaign.process_campaign()
    """
```

**Назначение**: Итерируется по категориям рекламной кампании и обрабатывает товары категории.

**Как работает функция**:

1. **Получение списка категорий**: Функция получает список названий папок категорий из директории кампании.
2. **Обработка каждой категории**: Для каждой категории вызываются методы `process_category_products` и `process_ai_category`.

```ascii
    Получение списка категорий
    │
    ├─────────────────────────────
    │
    ▼
    Для каждой категории:
    │
    ├── Обработка товаров категории
    │
    └── Обработка AI категории
```

**Примеры**:

```python
campaign.process_campaign()
```

### `process_campaign_category`

```python
def process_campaign_category(
    self, category_name: str
) -> list[SimpleNamespace] | None:
    """
    Processes a specific category within a campaign for all languages and currencies.
    @param campaign_name: Name of the advertising campaign.
    @param category_name: Category for the campaign.
    @param language: Language for the campaign.
    @param currency: Currency for the campaign.
    @return: List of product titles within the category.
    """
```

**Назначение**: Обрабатывает указанную категорию кампании для всех языков и валют.

**Параметры**:
- `category_name` (str): Название категории для обработки.

**Как работает функция**:

1. **Обработка товаров категории**: Вызывается метод `process_category_products` для обработки товаров в указанной категории.
2. **Обработка AI категории**: Вызывается метод `process_ai_category` для обработки AI-генерации данных для указанной категории.

```ascii
    Обработка товаров категории
    │
    ├─────────────────────────────
    │
    ▼
    Обработка AI категории
```

### `process_new_campaign`

```python
def process_new_campaign(
    self,
    campaign_name: str,
    language: Optional[str] = None,
    currency: Optional[str] = None,
):
    """Создание новой рекламной кампании.
    Условия для создания кампании:
    - директория кампании с питоник названием
    - вложенная директория `campaign`, в ней директории с питоник названиями категорий
    - файл sources.txt и/или директория `sources` с файлами `<product)id>.html`

    Args:
        campaign_name (Optional[str]): Название рекламной кампании.
        language (Optional[str]): Язык для кампании (необязательно).
        currency (Optional[str]): Валюта для кампании (необязательно).

    Returns:
        List[Tuple[str, Any]]: Список кортежей с именами категорий и их обработанными результатами.

    Example:
        >>> campaign.process_new_campaign(campaign_name="HolidaySale", language="RU", currency="ILS")

    Flowchart:
    ┌──────────────────────────────────────────────┐
    │ Start                                        │
    └──────────────────────────────────────────────┘
                      │
                      ▼
    ┌───────────────────────────────────────────────┐
    │ Check if `self.language` and `self.currency`  │
    │ are set                                       │
    └───────────────────────────────────────────────┘
                      │
            ┌─────────┴──────────────────────────┐
            │                                    │
            ▼                                    ▼
    ┌─────────────────────────────┐   ┌──────────────────────────────────────┐
    │Yes: `locale` = `{language:  │   │No: `locale` = {                      │
    │currency}`                   │   │     "EN": "USD",                     │
    │                             │   │     "HE": "ILS",                     │
    │                             │   │     "RU": "ILS"                      │
    │                             │   │    }                                 │
    └─────────────────────────────┘   └──────────────────────────────────────┘
                     │                         │
                     ▼                         ▼
    ┌───────────────────────────────────────────────┐
    │ For each `language`, `currency` in `locale`:  │
    │ - Set `self.language`, `self.currency`        │
    │ - Initialize `self.campaign`                  │
    └───────────────────────────────────────────────┘
                     │
                     ▼
    ┌───────────────────────────────────────────────┐
    │ Call `self.set_categories_from_directories()` │
    │ to populate categories                        │
    └───────────────────────────────────────────────┘
                     │
                     ▼
    ┌───────────────────────────────────────────────┐
    │ Copy `self.campaign` to `self.campaign_ai`    │
    │ and set `self.campaign_ai_file_name`          │
    └───────────────────────────────────────────────┘
                     │
                     ▼
    ┌───────────────────────────────────────────────┐
    │ For each `category_name` in campaign:         │
    │ - Call `self.process_category_products`       │
    │ - Call `self.process_ai_category`             │
    └───────────────────────────────────────────────┘
                     │
                     ▼
    ┌──────────────────────────────────────────────┐
    │ End                                          │
    └──────────────────────────────────────────────┘

    """
```

**Назначение**: Создает новую рекламную кампанию.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `language` (Optional[str]): Язык для кампании (необязательно).
- `currency` (Optional[str]): Валюта для кампании (необязательно).

**Как работает функция**:

1. **Определение локали**: Если язык и валюта не указаны, используются значения по умолчанию из `locales`.
2. **Инициализация кампании**: Создается объект `SimpleNamespace` для представления кампании.
3. **Установка категорий**: Вызывается метод `set_categories_from_directories` для установки категорий кампании.
4. **Создание AI кампании**: Создается копия объекта кампании для AI обработки.
5. **Обработка категорий**: Для каждой категории вызываются методы `process_category_products` и `process_ai_category`.

```ascii
    Проверка наличия языка и валюты
    │
    ├── Да: Использовать переданные значения
    │
    └── Нет: Использовать значения по умолчанию
    │
    Инициализация кампании
    │
    Установка категорий
    │
    Создание AI кампании
    │
    Для каждой категории:
    ├── Обработка товаров
    └── Обработка AI
```

**Примеры**:

```python
campaign.process_new_campaign(campaign_name="HolidaySale", language="RU", currency="ILS")
```

### `process_ai_category`

```python
def process_ai_category(self, category_name: Optional[str] = None):
    """Processes the AI campaign for a specified category or all categories.

        This method processes AI-generated data for the specified category in the campaign.
        If no category name is provided, it processes all categories.

        Args:
            category_name (Optional[str]): The name of the category to process. If not provided, all categories are processed.

        Example:
            >>> campaign.process_ai_category("Electronics")
            >>> campaign.process_ai_category()

        Flowchart:
        ┌──────────────────────────────────────────────┐
        │ Start                                        │
        └──────────────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────────────┐
        │ Load system instructions from JSON file       │
        └───────────────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────────────┐
        │ Initialize AI model with system instructions  │
        └───────────────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────────────┐
        │ Check if `category_name` is provided          │
        └───────────────────────────────────────────────┘
                            │
            ┌─────────────────┴───────────────────┐
            │                                     │
            ▼                                     ▼
    ┌─────────────────────────────────────┐   ┌────────────────────────────────────┐
    │ Process specified category          │   │ Iterate over all categories        │
    │ - Load product titles               │   │ - Call `_process_category`         │
    │ - Generate prompt                   │   │   for each category                │
    │ - Get response from AI model        │   └────────────────────────────────────┘
    │ - Update or add category            │
    └─────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────────────┐
        │ Save updated campaign data to file            │
        └───────────────────────────────────────────────┘
                            │
                            ▼
        ┌──────────────────────────────────────────────┐
        │ End                                          │
        └──────────────────────────────────────────────┘

    """
```

**Назначение**: Обрабатывает AI-генерацию данных для указанной категории или для всех категорий.

**Параметры**:
- `category_name` (Optional[str]): Название категории для обработки. Если не указано, обрабатываются все категории.

**Внутренние функции**:
- `_process_category(category_name: str)`: Обрабатывает AI-генерацию данных для конкретной категории и обновляет данные кампании.
    - **Параметры**:
        - `category_name` (str): Название категории для обработки.
    - **Как работает**:
        1. **Чтение названий товаров**: Считывает названия товаров из файла `product_titles.txt` для указанной категории.
        2. **Формирование запроса**: Формирует запрос для AI модели, включающий язык, название категории и список названий товаров.
        3. **Получение ответа от AI модели**: Получает ответ от AI модели (Gemini или OpenAI).
        4. **Обработка ответа**: Преобразует ответ AI модели в объект `SimpleNamespace` и обновляет данные категории в объекте кампании.
    - **Примеры**:

```ascii
    Проверка наличия названия категории
    │
    ├── Да: Обработка указанной категории
    │
    └── Нет: Обработка всех категорий
    │
    Для каждой категории:
    ├── Чтение названий товаров
    │
    ├── Формирование запроса для AI модели
    │
    ├── Получение ответа от AI модели
    │
    └── Обработка ответа и обновление данных кампании
```

**Как работает основная функция**:

1. **Копирование данных кампании**: Создает копию объекта кампании для AI обработки.
2. **Определение категорий для обработки**: Если указано название категории, обрабатывается только она. В противном случае, обрабатываются все категории.
3. **Сохранение результатов**: Сохраняет обновленные данные кампании в JSON-файл.

**Примеры**:

```python
campaign.process_ai_category("Electronics")
campaign.process_ai_category()
```

### `process_category_products`

```python
def process_category_products(
    self, category_name: str
) -> Optional[List[SimpleNamespace]]:
    """Processes products in a specific category.

            Args:
                category_name (str): The name of the category.

            Returns:
                Optional[List[SimpleNamespace]]: A list of `SimpleNamespace` objects representing the products.
                Returns `None` if no products are found.

            Example:
                >>> products: List[SimpleNamespace] = campaign.process_category_products("Electronics")
                >>> print(len(products))
                20
                >>> for product in products:
                >>>     pprint(product)  # Use pprint from `src.utils.pprint`

            Notes:
                The function attempts to read product IDs from both HTML files and text files within the specified category\'s
                `sources` directory. If no product IDs are found, an error is logged, and the function returns `None`.
                If affiliated products are found, they are returned; otherwise, an error is logged, and the function returns `None`.
            Flowchart:
    ┌───────────────────────────────────────────────────────────┐
    │ Start                                                     │
    └───────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌───────────────────────────────────────────────────────────┐
    │ Call `read_sources(category_name)` to get product IDs     │
    │ - Searches for product IDs in HTML files and sources.txt  │
    └───────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌───────────────────────────────────────────────────────────┐
    │ Check if `prod_ids` is empty                              │
    │ - If empty, log an error and return `None`                │
    └───────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌───────────────────────────────────────────────────────────┐
    │ Initialize `AliAffiliatedProducts` with `language`        │
    │ and `currency`                                            │
    └───────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌───────────────────────────────────────────────────────────┐
    │ Call `process_affiliate_products`                         │
    │ - Pass `campaign`, `category_name`, and `prod_ids`        │
    └───────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌───────────────────────────────────────────────────────────┐
    │ Check if `affiliated_products` is empty                   │
    │ - If empty, log an error and return `None`                │
    └───────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌───────────────────────────────────────────────────────────┐
    │ Return `affiliated_products`                              │
    └───────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌───────────────────────────────────────────────────────────┐
    │ End                                                       │
    └───────────────────────────────────────────────────────────┘

    """
```

**Назначение**: Обрабатывает товары в указанной категории, извлекая ID продуктов и генерируя партнерские ссылки.

**Параметры**:
- `category_name` (str): Название категории для обработки.

**Внутренние функции**:
- `read_sources(category_name: str) -> Optional[List[str]]`: Читает источники продуктов и извлекает ID продуктов.
    - **Параметры**:
        - `category_name` (str): Название категории.
    - **Как работает**:
        1. **Поиск HTML файлов**: Ищет HTML файлы в директории `sources` указанной категории.
        2. **Извлечение ID из HTML файлов**: Извлекает ID продуктов из найденных HTML файлов.
        3. **Чтение файла `sources.txt`**: Читает файл `sources.txt` из директории `sources`.
        4. **Извлечение ID из `sources.txt`**: Извлекает ID продуктов из файла `sources.txt`.
        5. **Объединение ID**: Объединяет ID продуктов, полученные из HTML файлов и файла `sources.txt`.
    - **Возвращает**: Список ID продуктов или `None`, если ID не найдены.
    - **Примеры**:

```python
        product_ids: Optional[List[str]] = read_sources("Electronics")
        print(product_ids)
```

**Как работает основная функция**:

1. **Чтение источников**: Вызывает функцию `read_sources` для получения ID продуктов из HTML файлов и файла `sources.txt`.
2. **Проверка наличия ID**: Проверяет, найдены ли ID продуктов. Если ID не найдены, функция логирует ошибку и возвращает `None`.
3. **Инициализация генератора ссылок**: Инициализирует объект `AliAffiliatedProducts` для генерации партнерских ссылок.
4. **Генерация партнерских ссылок**: Вызывает метод `process_affiliate_products` для генерации партнерских ссылок для каждого ID продукта.
5. **Возвращение результатов**: Возвращает список объектов `SimpleNamespace`, представляющих товары с партнерскими ссылками.

**Примеры**:

```python
products: List[SimpleNamespace] = campaign.process_category_products("Electronics")
print(len(products))
for product in products:
    pprint(product)
```

### `dump_category_products_files`

```python
def dump_category_products_files(
    self, category_name: str, products: List[SimpleNamespace]
):
    """Сохранение данных о товарах в JSON файлы.

    Args:
        category_name (str): Имя категории.
        products (List[SimpleNamespace]): Список объектов SimpleNamespace, представляющих товары.

    Example:
        >>> campaign.dump_category_products_files("Electronics", products)
    """
```

**Назначение**: Сохраняет данные о товарах в JSON файлы.

**Параметры**:
- `category_name` (str): Имя категории.
- `products` (List[SimpleNamespace]): Список объектов `SimpleNamespace`, представляющих товары.

**Как работает функция**:

1. **Проверка наличия товаров**: Проверяет, есть ли товары для сохранения. Если список товаров пуст, функция логирует предупреждение и завершает работу.
2. **Создание пути к категории**: Создает путь к директории категории.
3. **Сохранение каждого товара**: Для каждого товара в списке:
    - Извлекает `product_id`.
    - Проверяет, существует ли `product_id`. Если `product_id` не существует, функция логирует предупреждение и переходит к следующему товару.
    - Сохраняет данные товара в JSON файл с именем `<product_id>.json`.

```ascii
    Проверка наличия товаров
    │
    ├── Нет: Завершение работы
    │
    Создание пути к категории
    │
    Для каждого товара:
    ├── Извлечение product_id
    │
    ├── Проверка наличия product_id
    │   ├── Нет: Пропуск товара
    │   ├── Да: Сохранение данных в JSON файл
```

**Примеры**:

```python
campaign.dump_category_products_files("Electronics", products)
```

### `set_categories_from_directories`

```python
def set_categories_from_directories(self):
    """Устанавливает категории рекламной кампании из названий директорий в `category`.

    Преобразует каждый элемент списка категорий в объект `SimpleNamespace` с атрибутами
    `category_name`, `title`, и `description`.

    Example:
        >>> self.set_categories_from_directories()
        >>> print(self.campaign.category.category1.category_name)
    """
```

**Назначение**: Устанавливает категории рекламной кампании, беря названия директорий из папки "category".

**Как работает функция**:

1. **Определение пути к категориям**: Определяет путь к директории "category", где расположены папки категорий.
2. **Получение списка категорий**: Получает список названий директорий в папке "category".
3. **Преобразование категорий в SimpleNamespace**: Для каждой категории создает объект `SimpleNamespace` с атрибутами `category_name`, `title` и `description`.
4. **Присвоение категорий объекту кампании**: Добавляет каждый объект `SimpleNamespace` в качестве атрибута к объекту `self.campaign.category`.

```ascii
    Определение пути к категориям
    │
    Получение списка категорий
    │
    Для каждой категории:
    ├── Создание объекта SimpleNamespace
    │   ├── category_name = название категории
    │   ├── title = ""
    │   └── description = ""
    │
    └── Добавление объекта SimpleNamespace к объекту кампании
```

**Примеры**:

```python
self.set_categories_from_directories()
print(self.campaign.category.category1.category_name)
```

### `generate_output`

```python
async def generate_output(self, campaign_name: str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace):
    """
    Saves product data in various formats:

    - `<product_id>.json`: Contains all product parameters, one file per product.
    - `ai_{timestamp}.json`: A common file for all products with specific keys.
    - `promotion_links.txt`: A list of product links, created in the `save_promotion_links()` function.
    - `category_products_titles.json`: File containing title, `product_id`, `first_category_name`, and `second_category_name` of each product in the category.

    Args:
        campaign_name (str): The name of the campaign for the output files.
        category_path (str | Path): The path to save the output files.
        products_list (list[SimpleNamespace] | SimpleNamespace): List of products or a single product to save.

    Returns:
        None

    Example:
        >>> products_list: list[SimpleNamespace] = [
        ...     SimpleNamespace(product_id="123", product_title="Product A", promotion_link="http://example.com/product_a", 
        ...                     first_level_category_id=1, first_level_category_name="Category1",
        ...                     second_level_category_id=2, second_level_category_name="Subcategory1", 
        ...                     product_main_image_url="http://example.com/image.png", product_video_url="http://example.com/video.mp4"),
        ...     SimpleNamespace(product_id="124", product_title="Product B", promotion_link="http://example.com/product_b",
        ...                     first_level_category_id=1, first_level_category_name="Category1",
        ...                     second_level_category_id=3, second_level_category_name="Subcategory2",
        ...                     product_main_image_url="http://example.com/image2.png", product_video_url="http://example.com/video2.mp4")
        ... ]
        >>> category_path: Path = Path("/path/to/category")
        >>> await generate_output("CampaignName", category_path, products_list)

    Flowchart:
        ┌───────────────────────────────┐
        │  Start `generate_output`      │
        └───────────────────────────────┘
                    │
                    ▼
        ┌───────────────────────────────┐
        │ Format `timestamp` for file   │
        │ names.                        │
        └───────────────────────────────┘
                    │
                    ▼
        ┌───────────────────────────────┐
        │ Check if `products_list` is   │
        │ a list; if not, convert it to │
        │ a list.                       │
        └───────────────────────────────┘
                    │
                    ▼
    ┌─────────────────────────────────────────┐
    │ Initialize `_data_for_openai`,          │
    │ `_promotion_links_list`, and           │
    │ `_product_titles` lists.                │
    └─────────────────────────────────────────┘
                    │
                    ▼
    ┌─────────────────────────────────────────┐
    │ For each `product` in `products_list`:  │
    └─────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────┐
    │ 1. Create `categories_convertor` dictionary   │
    │ for `product`.                                │
    └───────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────┐
    │ 2. Add `categories_convertor` to `product`.   │
    └───────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────┐
    │ 3. Save `product` as `<product_id>.json`.     │
    └───────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────┐
    │ 4. Append `product_title` and                 │
    │ `promotion_link` to their respective lists.   │
    └───────────────────────────────────────────────┘
                    │                                               
                    ▼
        ┌───────────────────────────────┐
        │ Call `save_product_titles`    │
        │ with `_product_titles` and    │
        │ `category_path`.              │
        └───────────────────────────────┘
                    │
                    ▼
        ┌───────────────────────────────┐
        │ Call `save_promotion_links`   │
        │ with `_promotion_links_list`  │
        │ and `category_path`.          │
        └───────────────────────────────┘
                    │
                    ▼
        ┌───────────────────────────────────┐
        │ Call `generate_html` with         │
        │ `campaign_name`, `category_path`, │
        │ and `products_list`.              │
        └───────────────────────────────────┘
                    │
                    ▼
        ┌───────────────────────────────┐
        │  End `generate_output`        │
        └───────────────────────────────┘

    ```

    ### Flowchart Description

    1. **Start `generate_output`**: The function begins execution.
    2. **Format `timestamp` for file names**: Generate a timestamp to use in filenames.
    3. **Check if `products_list` is a list**: Ensure that `products_list` is in list format.
    4. **Initialize `_data_for_openai`, `_promotion_links_list`, and `_product_titles` lists**: Prepare empty lists to collect data.
    5. **For each `product` in `products_list`**: Process each product in the list.
    - **Create `categories_convertor` dictionary for `product`**: Create a dictionary for category conversion.
    - **Add `categories_convertor` to `product`**: Attach this dictionary to the product.
    - **Save `product` as `<product_id>.json`**: Save product details in a JSON file.
    - **Append `product_title` and `promotion_link` to their respective lists**: Collect titles and links.
    6. **Call `save_product_titles` with `_product_titles` and `category_path`**: Save titles data to a file.
    7. **Call `save_promotion_links` with `_promotion_links_list` and `category_path`**: Save promotion links to a file.
    8. **Call `generate_html` with `campaign_name`, `category_path`, and `products_list`**: Generate HTML output for products.
    9. **End `generate_output`**: The function completes execution.

    This flowchart captures the key steps and processes involved in the `generate_output` function.

    """
```

**Назначение**: Сохраняет данные о товарах в различных форматах, включая JSON файлы, списки ссылок и HTML страницы.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `category_path` (str | Path): Путь к директории категории.
- `products_list` (list[SimpleNamespace] | SimpleNamespace): Список объектов `SimpleNamespace`, представляющих товары.

**Как работает функция**:

1. **Форматирование временной метки**: Форматирует текущее время для использования в именах файлов.
2. **Преобразование `products_list` в список**: Убеждается, что `products_list` является списком. Если это не список, он преобразуется в список.
3. **Инициализация списков**: Инициализирует пустые списки `_data_for_openai`, `_promotion_links_list` и `_product_titles`.
4. **Обработка каждого товара**: Для каждого товара в `products_list`:
    - Создает словарь `categories_convertor` для преобразования категорий.
    - Добавляет `categories_convertor` к объекту товара.
    - Сохраняет данные товара в JSON файл с именем `<product_id>.json`.
    - Добавляет название товара и ссылку на промоакцию в соответствующие списки.
5. **Сохранение названий товаров**: Вызывает функцию `save_product_titles` для сохранения списка названий товаров в файл.
6. **Сохранение ссылок на промоакции**: Вызывает функцию `save_promotion_links` для сохранения списка ссылок на промоакции в файл.
7. **Генерация HTML**: Вызывает функцию `generate_html` для генерации HTML страницы с информацией о товарах.

```ascii
    Форматирование временной метки
    │
    Преобразование products_list в список
    │
    Инициализация списков
    │
    Для каждого товара:
    ├── Создание словаря categories_convertor
    │
    ├── Добавление categories_convertor к товару
    │
    ├── Сохранение данных товара в JSON файл
    │
    ├── Добавление названия и ссылки товара в списки
    │
    Сохранение названий товаров
    │
    Сохранение ссылок на промоакции
    │
    Генерация HTML
```

**Примеры**:

```python
products_list: list[SimpleNamespace] = [