# Модуль `campaign`

## Обзор

Модуль `campaign` предназначен для управления процессом создания и публикации рекламных кампаний в Facebook. Он включает в себя функциональность для инициализации параметров кампании (имя, язык, валюта), создания структуры каталогов, сохранения конфигураций для новой кампании, сбора и сохранения данных о продуктах через `ali` или `html`, создания рекламных материалов, просмотра кампании и публикации ее в Facebook.

## Подробней

Модуль `campaign` является ключевым компонентом системы `hypotez`, отвечающим за автоматизацию процесса создания и управления рекламными кампаниями на платформе Facebook. Он упрощает задачи, связанные с настройкой кампании, сбором данных о продуктах и генерацией рекламных материалов, что позволяет пользователям эффективно продвигать свои товары.

## Классы

### `AliCampaignEditor`

**Описание**: Класс `AliCampaignEditor` предназначен для редактирования рекламных кампаний AliExpress. Он предоставляет методы для добавления, удаления и обновления информации о продуктах и категориях в рамках кампании.

**Принцип работы**:
Класс `AliCampaignEditor` инициализируется с использованием параметров кампании и предоставляет интерфейс для выполнения операций редактирования. Он использует другие модули и классы проекта для чтения, записи и обработки данных, связанных с рекламными кампаниями.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliCampaignEditor`.
- `delete_product`: Удаляет продукт из кампании.
- `update_product`: Обновляет информацию о продукте в кампании.
- `update_campaign`: Обновляет параметры кампании, такие как описание.
- `update_category`: Обновляет данные категории в JSON-файле.
- `get_category`: Извлекает категорию по имени.
- `list_categories`: Перечисляет все категории в кампании.
- `get_category_products`: Извлекает продукты для заданной категории.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.

**Примеры**
- Пример создания инстанса класса
```python
campaign_editor = AliCampaignEditor(campaign_name='SummerSale', language='ru', currency='RUB')
```
## Диаграмма Mermaid

```mermaid
flowchart TD
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

```

## Функции

### `prepare_campaign`

**Назначение**: Функция `prepare_campaign` предназначена для подготовки рекламной кампании к запуску, обеспечивая обработку всех необходимых данных и ресурсов.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.
- `categories` (Optional[List[str]], optional): Список категорий для обработки. По умолчанию `None`.
- `all_campaigns` (bool, optional): Флаг, указывающий на необходимость обработки всех кампаний. По умолчанию `False`.

**Возвращает**:
- `None`: Функция не возвращает явного значения.

**Как работает функция**:

1. **Проверка необходимости обработки всех кампаний**:
   Функция проверяет, установлен ли флаг `all_campaigns`. Если флаг установлен, функция переходит к обработке всех кампаний. В противном случае функция продолжает обработку конкретной кампании, указанной в параметре `campaign_name`.

2. **Обработка всех кампаний**:
   Если установлен флаг `all_campaigns`, функция проверяет, предоставлены ли язык и валюта.
   - Если язык и валюта предоставлены, функция обрабатывает каждую кампанию с указанным языком и валютой.
   - Если язык и валюта не предоставлены, функция обрабатывает все локали для каждой кампании.

3. **Обработка конкретной кампании**:
   Если флаг `all_campaigns` не установлен, функция проверяет, указаны ли категории для обработки.
   - Если категории указаны, функция обрабатывает только указанные категории для кампании.
   - Если категории не указаны, функция обрабатывает всю кампанию целиком.

4. **Обработка категорий**:
   В зависимости от указанных параметров, функция вызывает соответствующие методы для обработки категорий кампании.
   - Если указаны конкретные категории, функция обрабатывает только их.
   - Если категории не указаны, функция обрабатывает все категории, связанные с кампанией.

**Примеры**:
- Подготовка конкретной кампании с указанными категориями:
```python
prepare_campaign(campaign_name='SummerSale', language='ru', currency='RUB', categories=['shoes', 'bags'])
```

- Подготовка всех кампаний для определенного языка и валюты:
```python
prepare_campaign(language='en', currency='USD', all_campaigns=True)
```

## Диаграмма Mermaid

```mermaid
flowchart TD
    A[Start] --> B{Process all campaigns?}
    B -->|Yes| C[Process all campaigns]
    B -->|No| D[Process specific campaign]
    
    C --> E{Language and Currency provided?}
    E -->|Yes| F[Process each campaign with provided language and currency]
    E -->|No| G[Process all locales for each campaign]
    
    D --> H{Categories specified?}
    H -->|Yes| I[Process specific categories for the campaign]
    H -->|No| J[Process entire campaign]
    
    F --> K[Process campaign category]
    G --> L[Process campaign for all locales]
    I --> K
    J --> L
    
    K --> M[Return]
    L --> M
```