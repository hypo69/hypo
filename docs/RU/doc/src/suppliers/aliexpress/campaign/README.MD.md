# Модуль `campaign`

## Обзор

Модуль `campaign` предназначен для управления процессом создания и публикации рекламных кампаний на Facebook. Он включает в себя функциональность для инициализации параметров кампании (название, язык, валюта), создания структуры каталогов, сохранения конфигураций новой кампании, сбора и сохранения данных о продуктах через `ali` или `html`, генерации рекламных материалов, просмотра кампании и публикации ее на Facebook.

## Оглавление

1.  [Обзор](#обзор)
2.  [Диаграмма процесса создания рекламной кампании](#диаграмма-процесса-создания-рекламной-кампании)
3.  [Описание процесса создания рекламной кампании](#описание-процесса-создания-рекламной-кампании)
4.  [Диаграмма редактирования кампании](#диаграмма-редактирования-кампании)
5.  [Диаграмма подготовки кампании](#диаграмма-подготовки-кампании)

## Диаграмма процесса создания рекламной кампании

```mermaid
flowchart TD
    A[Start: Creating an advertising campaign for Facebook placement] --> B[Initialize Campaign Name, Language, and Currency]
    B --> C[Create Campaign and Category Directories]
    C --> D[Save Campaign Configuration]
    D --> E[Collect Product Data]
    E --> F[Save Product Data]
    F --> G[Create Promotional Materials]
    G --> H[Review Campaign]
    H --> I{Is the Campaign Ready?}
    I -- Yes --> J[Publish Campaign on Facebook]
    I -- No --> H
    J --> K[End: Completion of the advertising campaign creation]
```

## Описание процесса создания рекламной кампании

-   **Шаг 1**: Начало - Процесс начинается.
-   **Шаг 2**: Инициализация деталей кампании - Определяются название, язык и валюта кампании. Пример: Название кампании: "Летняя распродажа", Язык: "Русский", Валюта: "RUB".
-   **Шаг 3**: Создание каталогов кампании и категорий - Создаются необходимые каталоги или файлы для кампании. Пример: На файловой системе создается структура папок для хранения ресурсов кампании.
-   **Шаг 4**: Сохранение конфигурации кампании - Сохранются инициализированные детали кампании. Пример: Данные записываются в базу данных или конфигурационный файл.
-   **Шаг 5**: Сбор данных о продуктах - Собираются данные о продуктах, которые будут продвигаться в рамках кампании. Пример: Идентификаторы продуктов, описания, изображения и цены извлекаются из системы инвентаризации.
-   **Шаг 6**: Сохранение данных о продуктах - Сохранются собранные данные о продуктах. Пример: Данные записываются в таблицу базы данных, посвященную продуктам кампании.
-   **Шаг 7**: Создание рекламных материалов - Генерируются или выбираются графики, баннеры и другие рекламные материалы. Пример: Изображения и описания адаптируются для привлечения клиентов.
-   **Шаг 8**: Просмотр кампании - Процесс просмотра подтверждает готовность компонентов кампании. Пример: Проверка человеком или системой оценивает качество и полноту всех компонентов кампании.
-   **Шаг 9**: Готова ли кампания? - Проверка для определения, завершена ли кампания и готова ли к публикации. Пример: Логический флаг сигнализирует "Да", если все на месте, иначе "Нет", вызывая возврат к предыдущему шагу для внесения исправлений.
-   **Шаг 10**: Публикация кампании - Кампания становится активной на платформе, готовой для маркетинговых усилий. Пример: API-вызовы выполняются для публикации кампании на соответствующей платформе.
-   **Шаг 11**: Конец - Процесс создания кампании завершен.

## Диаграмма редактирования кампании

```mermaid
graph LR
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

## Диаграмма подготовки кампании

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