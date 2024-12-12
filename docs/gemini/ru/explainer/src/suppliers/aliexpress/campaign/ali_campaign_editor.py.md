## <алгоритм>

1. **Инициализация `AliCampaignEditor`**:
    - Принимает `campaign_name`, `language`, `currency` и опционально `campaign_file`.
    - Вызывает конструктор родительского класса `AliPromoCampaign` для инициализации основных параметров кампании.
    - Создает объект `AliCampaignGoogleSheet`, который можно использовать для работы с Google Sheets.
2. **`delete_product(product_id, exc_info=False)`**:
    - Принимает `product_id` (ID удаляемого продукта) и флаг `exc_info` для логирования ошибок.
    - Извлекает `_product_id` из `product_id` с помощью `extract_prod_ids`.
    - Проверяет наличие `sources.txt` в директории категории.
        - Если `sources.txt` существует:
            - Читает список продуктов из файла.
            - Итерирует по списку, сравнивая `product_id` с ID продукта в списке.
            - Если найдено совпадение, удаляет запись и сохраняет изменения в `_sources.txt`.
        - Если `sources.txt` не существует, обрабатывает файлы `<product_id>.html` в каталоге `/sources/`.
            - Пытается переименовать файл `product_id.html` в `product_id_.html`.
            - Логирует успешное переименование или ошибку.
3.  **`update_product(category_name, lang, product)`**:
    -   Принимает `category_name`, `lang`, и словарь `product` с данными продукта.
    -   Вызывает `dump_category_products_files` для обновления данных.
4.  **`update_campaign()`**:
    -   Функция заглушка для обновления параметров кампании (например, описания).
5. **`update_category(json_path, category)`**:
   - Принимает `json_path` (путь к файлу JSON) и `category` (объект `SimpleNamespace` с данными категории).
   - Загружает JSON данные из файла.
   - Обновляет данные категории в загруженных данных.
   - Сохраняет обновленные данные в JSON файл.
   - Возвращает `True` при успешном обновлении и `False` в случае ошибки.
6. **`get_category(category_name)`**:
    - Принимает `category_name` (название категории).
    - Пытается получить объект категории из атрибута `campaign.category`.
    - Возвращает `SimpleNamespace` объект, представляющий категорию, или `None`, если категория не найдена.
7. **`list_categories` (property)**:
    - Возвращает список названий категорий из `self.campaign.category`.
    - Проверяет, что `campaign.category` существует и является `SimpleNamespace`.
    - Возвращает `None` в случае, если `campaign.category` не найден или если категории отсутствуют.
8. **`get_category_products(category_name)`**:
    - Принимает `category_name` (название категории).
    - Формирует путь к директории с JSON файлами товаров.
    - Получает список JSON файлов в этой директории.
    - Если JSON файлы найдены:
        - Загружает данные из каждого файла в виде `SimpleNamespace`.
        - Добавляет `SimpleNamespace` объекты в список `products`.
        - Возвращает список `products`.
    - Если JSON файлы не найдены:
        - Логирует ошибку и вызывает `process_category_products` для подготовки продуктов в категории.
        - Возвращает `None`.

## <mermaid>

```mermaid
graph LR
    subgraph AliCampaignEditor
        A[User Input: campaign_name, language, currency] --> B{AliCampaignEditor.__init__};
        B --> C[AliPromoCampaign.__init__];
        C --> D[Initialization: AliCampaignEditor constructor];
        D --> E[AliCampaignEditor];
        
        E --> F[delete_product: Check for affiliate link];
        F --> G[read_text_file sources.txt: Read product list];
        G --> H[Iterate & check product_id: Loop through product list];
        H -- Match --> I[remove & save: Remove product if match found];
        H -- No Match --> J[rename product file: Rename product file if no match];
        
        E --> K[update_product: Update product details];
        K --> L[Call dump_category_products_files: Update category with new product];
        
        E --> M[update_campaign: Update campaign properties like description];
        M --> N[update campaign parameters];
        
        E --> O[update_category: Update category in JSON file];
        O --> P[j_loads JSON file: Read category data];
        P --> Q[Update category: Update category data];
        Q --> R[j_dumps JSON file: Write updated category to file];
        
        E --> S[get_category: Retrieve category by name];
        S --> T[Check if category exists];
        T -- Found --> U[Return SimpleNamespace: Return category details];
        T -- Not Found --> V[Log warning: Category not found in campaign];
        
        E --> W[list_categories: List all categories in the campaign];
        W --> X[Check category attribute: Ensure categories exist in campaign];
        X -- Found --> Y[Return category list: List category names];
        X -- Not Found --> Z[Log warning: No categories found in campaign];
        
        E --> AA[get_category_products: Retrieve products for a category];
        AA --> AB[Get category path: Build path for category products];
        AB --> AC[Get JSON filenames: Retrieve all product JSON files];
        AC --> AD[Read JSON files: Load product data];
        AD --> AE[Create SimpleNamespace: Convert product data to objects];
        AE --> AF[Return products: Return list of products];
        AC -- No JSON files --> AG[Log error: No files found];
        AG --> AH[Process category: Trigger category product preparation];

        E --> AI[Other methods];
    end
```

**Описание зависимостей:**

-   **`header`**: Импортируется, но не используется в текущем коде. Вероятно, это заголовочный файл, содержащий общие метаданные проекта.
-   **`src.gs`**: Импортируется, но не используется в текущем коде. Скорее всего, это модуль для работы с Google сервисами (например, Google Sheets или Drive).
-   **`src.suppliers.aliexpress.campaign.ali_promo_campaign`**: Базовый класс для `AliCampaignEditor`. Содержит общую логику для работы с рекламными кампаниями AliExpress.
-   **`src.suppliers.aliexpress.campaign.gsheet`**: Класс для работы с Google Sheets,  предположительно для управления данными кампании в таблицах Google.
-   **`src.suppliers.aliexpress.utils`**: Модуль с утилитами для работы с AliExpress, такими как извлечение ID продуктов (`extract_prod_ids`) и проверка ссылок (`ensure_https`).
-   **`src.utils.jjson`**: Модуль для работы с JSON файлами, включающий функции `j_loads_ns`, `j_loads` и `j_dumps` для загрузки и сохранения данных.
-   **`src.utils.convertors.csv`**: Модуль для работы с CSV файлами, используемый для конвертации данных из CSV в словарь (`csv2dict`).
-  **`src.utils.printer`**: Модуль для форматированного вывода данных (`pprint`).
-   **`src.utils.file`**: Модуль для работы с файлами, предоставляющий функции `read_text_file`, `save_text_file`, и `get_filenames`.
-   **`src.logger.logger`**: Модуль для логирования событий.

## <объяснение>

**Импорты:**

-   `re`:  Используется для работы с регулярными выражениями, хотя в данном коде не используется явно.
-   `shutil`: Модуль для операций с файлами, в этом коде также не используется.
-   `pathlib.Path`: Используется для работы с путями файлов и каталогов.
-   `types.SimpleNamespace`:  Удобный класс для создания объектов с произвольными атрибутами. Используется для представления данных о категориях и продуктах.
-  `typing`:  Используется для аннотации типов в коде.
-   `header`, `src.gs`, `src.suppliers.aliexpress.campaign.ali_promo_campaign`, `src.suppliers.aliexpress.campaign.gsheet`, `src.suppliers.aliexpress.utils`, `src.utils.jjson`, `src.utils.convertors.csv`, `src.utils.printer`, `src.utils.file`, `src.logger.logger`: Все эти импорты являются частью проекта `hypotez` и обеспечивают функциональность для работы с AliExpress, файловой системой, JSON, CSV,  логированием и общими настройками проекта.

**Классы:**

-   `AliCampaignEditor(AliPromoCampaign)`:
    -   **Роль**: Редактор рекламных кампаний AliExpress. Наследует базовую функциональность от `AliPromoCampaign` и расширяет ее возможностями редактирования.
    -   **Атрибуты**:
        -   `campaign`: Объект кампании, унаследованный от `AliPromoCampaign`.
        -   `base_path`: Базовый путь к директории кампании.
        -   `category_path`: Путь к директории категории.
        -   `language`: Язык кампании.
        -   `currency`: Валюта кампании.
        -   `google_sheet`: Объект для взаимодействия с Google Sheets.
    -   **Методы**:
        -   `__init__(campaign_name, language, currency)`: Конструктор класса, инициализирует параметры кампании и вызывает конструктор родительского класса.
        -   `delete_product(product_id, exc_info=False)`: Удаляет продукт из списка или переименовывает файл, если нет аффилиат ссылки.
        -   `update_product(category_name, lang, product)`: Обновляет информацию о продукте в категории.
        -   `update_campaign()`: Заглушка для обновления параметров кампании.
        -   `update_category(json_path, category)`: Обновляет категорию в JSON файле.
        -  `get_category(category_name)`:  Возвращает объект SimpleNamespace для категории.
        -   `list_categories`: Возвращает список категорий.
        -   `get_category_products(category_name)`: Получает данные о продуктах из JSON файлов категории.

**Функции:**

-   `__init__(self, campaign_name, language, currency)`: Конструктор класса `AliCampaignEditor`.
    -   **Аргументы**: `campaign_name` (название кампании), `language` (язык), `currency` (валюта).
    -   **Возвращаемое значение**: None.
    -   **Назначение**: Инициализирует объект `AliCampaignEditor`, устанавливая базовые параметры кампании. Вызывает конструктор родительского класса `AliPromoCampaign` для установки общих свойств кампании.
-   `delete_product(self, product_id, exc_info=False)`: Удаляет продукт из списка или переименовывает файл.
    -   **Аргументы**: `product_id` (ID продукта для удаления), `exc_info` (флаг для отображения исключений).
    -   **Возвращаемое значение**: None.
    -   **Назначение**: Удаляет продукт из списка `sources.txt`, либо переименовывает HTML файл продукта, если `sources.txt` не существует.
-   `update_product(self, category_name, lang, product)`: Обновляет информацию о продукте.
    -   **Аргументы**: `category_name` (название категории), `lang` (язык кампании), `product` (словарь с данными о продукте).
    -   **Возвращаемое значение**: None.
    -   **Назначение**:  Вызывает метод `dump_category_products_files` для обновления данных о продукте.
-  `update_campaign(self)`: Заглушка для обновления параметров кампании.
    - **Аргументы**: Нет.
    - **Возвращаемое значение**: None.
    - **Назначение**: В текущей реализации не выполняет никаких действий.
-   `update_category(self, json_path, category)`: Обновляет категорию в JSON файле.
    -   **Аргументы**: `json_path` (путь к файлу JSON), `category` (объект `SimpleNamespace` с данными категории).
    -   **Возвращаемое значение**: `True` при успешном обновлении и `False` в случае ошибки.
    -   **Назначение**: Загружает данные из JSON файла, обновляет данные категории и сохраняет изменения.
-   `get_category(self, category_name)`: Возвращает объект категории SimpleNamespace.
    -   **Аргументы**: `category_name` (название категории).
    -   **Возвращаемое значение**: `SimpleNamespace` или `None`, если категория не найдена.
    -   **Назначение**: Получает данные о категории из атрибута `campaign.category`.
-   `list_categories(self)`: Возвращает список категорий.
    - **Аргументы**: Нет.
    - **Возвращаемое значение**: Список названий категорий или `None`, если нет категорий.
    - **Назначение**: Возвращает список названий категорий.
-   `get_category_products(self, category_name)`: Получает данные о продуктах из JSON файлов.
    -   **Аргументы**: `category_name` (название категории).
    -   **Возвращаемое значение**: Список объектов `SimpleNamespace`, представляющих продукты, или `None`.
    -   **Назначение**:  Загружает данные о продуктах из JSON файлов для заданной категории, возвращает их в виде списка. Если файлы не найдены, запускает процесс подготовки продуктов.

**Переменные:**

-   `MODE`: Строка, которая определяет режим работы приложения, по умолчанию установлено значение `'dev'`.
-   `_product_id`: Временная переменная для хранения извлеченного ID продукта.
-   `product_path`: Путь к файлу с информацией о продукте.
-  `prepared_product_path`: Путь к временному файлу с информацией о продукте.
-   `products_list`: Список строк, представляющих продукты.
-   `record`: Временная переменная для итерации по продуктам.
- `data`: Временная переменная для хранения данных JSON.
-   `json_path`: Путь к файлу JSON.
-   `category`: Объект `SimpleNamespace`, содержащий данные о категории.
-   `category_path`: Путь к директории, содержащей файлы категории.
-   `json_filenames`: Список имен файлов JSON в директории категории.
-  `products`: Список объектов `SimpleNamespace` представляющих продукты.
-   `product_data`: Объект `SimpleNamespace` c данными продукта.
- `product`: Объект `SimpleNamespace` представляющий продукт.

**Потенциальные ошибки и области для улучшения:**

1.  **Обработка ошибок**: В методе `delete_product` есть try-except блок, но он может быть более подробным, чтобы обрабатывать различные типы ошибок.
2.  **Функция `update_campaign`**: Сейчас является заглушкой и не выполняет никаких действий. Необходимо добавить функциональность для обновления параметров кампании.
3.  **Логирование**: В некоторых местах, например в методах `update_category` и `get_category`, можно добавить более подробное логирование, чтобы отслеживать ошибки и события.
4.  **Дублирование кода**: В методе `delete_product` есть небольшое дублирование кода, при чтении и удалении из файла, можно вынести в отдельную функцию.
5. **Типизация**: В методах `delete_product`, `update_product` можно сделать более строгую проверку типов входных параметров, например, для product_id и product.
6. **`MODE`**: Глобальная переменная `MODE` объявлена в начале файла, но не используется. Возможно, её стоит убрать или добавить функционал, зависящий от неё.
7. **`shutil` и `re`**: Импортированы, но не используются. Можно убрать лишние импорты.
8. **`update_product`**: Вызывает `dump_category_products_files`, но эта функция не определена в данном коде, предположительно является частью родительского класса.

**Взаимосвязь с другими частями проекта:**

-   `AliCampaignEditor` является частью модуля управления рекламными кампаниями AliExpress.
-   Использует утилиты из `src.suppliers.aliexpress.utils` для работы с данными AliExpress.
-   Взаимодействует с файловой системой через модули `src.utils.file` и `pathlib`.
-   Использует модуль `src.utils.jjson` для загрузки и сохранения данных в формате JSON.
-   Использует `src.logger.logger` для логирования событий.
-   `AliCampaignGoogleSheet` используется для взаимодействия с Google Sheets, что позволяет синхронизировать данные между локальной системой и Google.
-   Родительский класс `AliPromoCampaign` предоставляет базовую функциональность для работы с кампаниями, такую как доступ к базовым настройкам.
-   Метод `get_category_products` вызывает `process_category_products`, предположительно для подготовки данных, если JSON файлы не найдены, что указывает на взаимодействие с другими частями проекта, которые занимаются подготовкой данных для кампаний.

Таким образом, код `ali_campaign_editor.py` является центральной частью системы редактирования рекламных кампаний AliExpress, предоставляя функциональность для управления продуктами, категориями и общими параметрами кампании. Он взаимодействует с другими частями проекта для доступа к данным, их сохранения и синхронизации.