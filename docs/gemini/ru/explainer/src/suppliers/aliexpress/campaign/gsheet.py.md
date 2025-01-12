## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1.  **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2.  **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```

3.  **<объяснение>**: Предоставьте подробные объяснения:
    -   **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.
    -   **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.
    -   **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.
    -   **Переменные**: Их типы и использование.
    -   Выделите потенциальные ошибки или области для улучшения.

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

1. **Инициализация `AliCampaignGoogleSheet`**:
    -   Создается экземпляр класса `AliCampaignGoogleSheet` с указанием имени кампании, языка и валюты.
    -   Инициализируется базовый класс `SpreadSheet` с ID Google Sheets.
    ```python
    campaign_sheet = AliCampaignGoogleSheet(campaign_name="test_campaign", language="en", currency="USD")
    ```
2.  **Очистка данных (`clear`)**:
    -   Вызывается метод `clear()`, который удаляет все листы, кроме 'categories', 'product', 'category' и 'campaign'.
    ```python
    campaign_sheet.clear()
    ```
    -   **Пример**: Если в Google Sheets были листы 'products_1', 'products_2', то они будут удалены.
3.  **Запись данных кампании (`set_campaign_worksheet`)**:
    -   Создается `SimpleNamespace` объект с данными кампании.
    ```python
    campaign_data = SimpleNamespace(
        campaign_name="test_campaign",
        title="Test Campaign",
        language="en",
        currency="USD",
        description="This is a test campaign."
    )
    ```
    -   Вызывается метод `set_campaign_worksheet()` с данными кампании.
    -   Данные записываются в лист 'campaign' в вертикальном формате.
        -   **Пример**:
        ```
            | A      | B                |
            |--------|-----------------|
            | A1     | Campaign Name   | test_campaign |
            | A2     | Campaign Title  | Test Campaign  |
            | A3     | Campaign Language| en          |
            | A4     | Campaign Currency| USD          |
            | A5     | Campaign Description| This is a test campaign. |
        ```
4.  **Запись данных о продуктах (`set_products_worksheet`)**:
    -   Получает имя категории, если оно есть
    -   Извлекает продукты из объекта SimpleNamespace.
    -   Копирует шаблон листа 'product' в новый лист с именем категории.
    -   Записывает данные каждого продукта в новую строку листа.
    ```python
    campaign_sheet.set_products_worksheet(category_name="test_category")
    ```
    -   **Пример**: Если есть продукты `product1`, `product2` в категории `test_category`, они будут записаны в лист 'test_category'.
5.  **Запись данных о категориях (`set_categories_worksheet`)**:
     - Получает объект SimpleNamespace с данными о категориях.
     ```python
    categories = SimpleNamespace(
        test_category = SimpleNamespace(
            name="test_category",
            title="Test Category",
            description="This is a test category.",
            tags=["test", "category"],
            products_count=10
        ),
        test_category_2 = SimpleNamespace(
            name="test_category_2",
            title="Test Category 2",
            description="This is a test category 2.",
            tags=["test", "category", "2"],
            products_count=20
        )
    )
    ```
    -   Вызывает метод `set_categories_worksheet()`, передавая объект с категориями.
    -   Данные категорий записываются в лист 'categories'.
        -   **Пример**:
        ```
            | Name           | Title          | Description               | Tags        | Products Count |
            |----------------|----------------|---------------------------|-------------|----------------|
            | test_category  | Test Category  | This is a test category.  | test, category| 10            |
            | test_category_2 | Test Category 2 | This is a test category 2. | test, category, 2 | 20           |
        ```
6.  **Получение данных о категориях (`get_categories`)**:
    -   Вызывает метод `get_categories()`.
    -   Возвращает данные из листа 'categories' в виде списка словарей.
    ```python
    categories_data = campaign_sheet.get_categories()
    ```
7.  **Запись продуктов по категории (`set_category_products`)**:
    -   Принимает имя категории и словарь с продуктами.
    -   Копирует шаблон листа `product` и заполняет его данными о продуктах.
    ```python
    products_data = [
      SimpleNamespace(
          product_id = "123",
          app_sale_price="10",
          original_price="12",
          sale_price="11",
          discount="10",
          product_main_image_url="image_url",
          local_image_path="image_path",
          product_small_image_urls=["url1", "url2"],
          product_video_url="video_url",
          local_video_path="video_path",
          first_level_category_id="111",
          first_level_category_name="cat1",
          second_level_category_id="222",
          second_level_category_name="cat2",
          target_sale_price="9",
          target_sale_price_currency="USD",
          target_app_sale_price_currency="USD",
          target_original_price_currency="USD",
          original_price_currency="USD",
          product_title="product title",
          evaluate_rate="4",
          promotion_link="link",
          shop_url="shop_url",
          shop_id="11",
          tags=["tag1", "tag2"]
        )
    ]

    campaign_sheet.set_category_products(category_name="test_category", products = products_data)
    ```
    -  **Пример**: Если есть продукты, они будут записаны в лист 'test_category'.
8.  **Форматирование листов (`_format_categories_worksheet`, `_format_category_products_worksheet`)**:
    -   Вызываются для форматирования листов 'categories' и листов продуктов, устанавливая ширину столбцов, высоту строк и стиль заголовков.
    -   Эти методы вызываются внутри других методов записи данных.
   
## <mermaid>

```mermaid
flowchart TD
    subgraph AliCampaignGoogleSheet
        Start[Start] --> Init[__init__]
        Init --> Clear[clear]
        Clear --> DeleteProductsWorksheets[delete_products_worksheets]
        Init --> SetCampaignWorksheet[set_campaign_worksheet]
        Init --> SetProductsWorksheet[set_products_worksheet]
        Init --> SetCategoriesWorksheet[set_categories_worksheet]
        Init --> GetCategories[get_categories]
        Init --> SetCategoryProducts[set_category_products]
        SetCategoryProducts --> CopyWorksheet[copy_worksheet]
        
        SetCampaignWorksheet --> GetWorksheetCampaign[get_worksheet(campaign)]
        SetCampaignWorksheet --> UpdateCampaign[ws.batch_update]
        
        SetCategoriesWorksheet --> GetWorksheetCategories[get_worksheet(categories)]
        SetCategoriesWorksheet --> ClearCategoriesWS[ws.clear]
         SetCategoriesWorksheet --> UpdateCategories[ws.update]
         SetCategoriesWorksheet --> FormatCategoriesWS[_format_categories_worksheet]
        
        SetProductsWorksheet --> CopyWorksheetProduct[copy_worksheet(product)]
        SetProductsWorksheet --> UpdateProductsWS[ws.update(product)]
        SetProductsWorksheet --> FormatProductsWS[_format_category_products_worksheet]


        GetCategories --> GetWorksheet[get_worksheet(categories)]
        GetCategories --> GetCategoriesData[ws.get_all_records()]

        SetCategoryProducts --> CopyWorksheetCategoryProducts[copy_worksheet(product)]
         SetCategoryProducts --> UpdateCategoryProducts[ws.update(product)]
         SetCategoryProducts --> FormatCategoryProductsWS[_format_category_products_worksheet]

         DeleteProductsWorksheets --> GetWorksheets[self.spreadsheet.worksheets]
         DeleteProductsWorksheets --> DelWorksheet[self.spreadsheet.del_worksheet_by_id]
         
         FormatCategoriesWS --> SetColumnWidthCategories[set_column_width]
         FormatCategoriesWS --> SetRowHeightCategories[set_row_height]
         FormatCategoriesWS --> FormatCellRangeCategories[format_cell_range]


         FormatProductsWS --> SetColumnWidthProducts[set_column_width]
         FormatProductsWS --> SetRowHeightProducts[set_row_height]
         FormatProductsWS --> FormatCellRangeProducts[format_cell_range]
         
         FormatCategoryProductsWS --> SetColumnWidthCategoryProducts[set_column_width]
         FormatCategoryProductsWS --> SetRowHeightCategoryProducts[set_row_height]
         FormatCategoryProductsWS --> FormatCellRangeCategoryProducts[format_cell_range]
     end

    
    Init --> SpreadSheetInit[SpreadSheet.__init__]
    
    SpreadSheetInit --> GetWorksheet[SpreadSheet.get_worksheet]
    GetWorksheet --> gspreadWorksheet[gspread.worksheet.Worksheet]
    
     CopyWorksheet --> gspreadWorksheetCopy[gspread.worksheet.Worksheet]
    
    
    classDef classStyle fill:#f9f,stroke:#333,stroke-width:2px
    class AliCampaignGoogleSheet classStyle
```

**Описание зависимостей:**

-   `AliCampaignGoogleSheet` является основным классом, который управляет работой с Google Sheets для рекламных кампаний AliExpress.
-   `SpreadSheet` – базовый класс, от которого наследуется `AliCampaignGoogleSheet`, предоставляя основные функции для работы с Google Sheets.
-   `gspread.worksheet.Worksheet` – класс из библиотеки `gspread`, представляющий лист в Google Sheets.
-   `set_column_width`, `set_row_height`, `cellFormat`, `textFormat`, `format_cell_range`, `Color`  - функции для форматирования листов из библиотеки `gspread_formatting`.

## <объяснение>

**Импорты:**

-   `time`: Используется для добавления задержек, но в коде не используется (закомментирован)
-   `types.SimpleNamespace`: Используется для создания простых объектов с атрибутами, используется для хранения данных кампании, категорий и продуктов.
-   `typing.Optional`, `typing.Any`: Используются для аннотации типов, указывая, что переменная может быть `None` или любого типа.
-   `gspread.worksheet.Worksheet`:  Используется для работы с листами Google Sheets.
-   `src.goog.spreadsheet.spreadsheet.SpreadSheet`: Базовый класс для работы с Google Sheets, от которого наследуется `AliCampaignGoogleSheet`.
-   `src.utils.jjson.j_dumps`: Используется для сериализации данных в JSON формат, но в коде не используется.
-   `src.utils.printer.pprint`: Используется для форматированного вывода, но в коде не используется.
-   `src.logger.logger.logger`: Используется для логирования.
-   `src.ai.openai.translate`: Используется для перевода текста, но в коде не используется.
- `typing.List`, `typing.Dict`: Используются для аннотации типов, указывая, что переменная может быть списком или словарем.
- `gspread_formatting`:  Используется для форматирования листов Google Sheets.

**Классы:**

-   `AliCampaignGoogleSheet`:
    -   **Роль:** Класс для управления данными рекламной кампании AliExpress в Google Sheets. Предоставляет методы для записи, чтения и форматирования данных.
    -   **Атрибуты:**
        -   `spreadsheet_id`: ID Google Sheets документа.
        -   `spreadsheet`: Экземпляр класса `SpreadSheet`.
        -   `worksheet`: Экземпляр класса `Worksheet` (лист Google Sheets).
    -   **Методы:**
        -   `__init__(self, campaign_name: str, language: str | dict = None, currency: str = None)`: Инициализация класса с параметрами кампании.
        -   `clear(self)`: Удаляет все листы, кроме основных.
        -   `delete_products_worksheets(self)`: Удаляет все листы продуктов из таблицы.
        -    `set_campaign_worksheet(self, campaign: SimpleNamespace)`: Записывает данные кампании в лист 'campaign'.
        -    `set_products_worksheet(self, category_name: str)`: Записывает данные о продуктах в лист категории.
        -    `set_categories_worksheet(self, categories: SimpleNamespace)`: Записывает данные о категориях в лист 'categories'.
        -   `get_categories(self)`: Получает данные о категориях из листа 'categories'.
        -   `set_category_products(self, category_name: str, products: dict)`: Записывает данные о продуктах в лист категории.
        -   `_format_categories_worksheet(self, ws: Worksheet)`: Форматирует лист 'categories'.
        -   `_format_category_products_worksheet(self, ws: Worksheet)`: Форматирует листы продуктов.
    -   **Взаимодействие:** Наследует от `SpreadSheet`, использует `Worksheet` для операций с листами, использует `SimpleNamespace` для передачи данных, а также логирование и форматирование через другие модули `src`.
   
**Функции:**

-   `__init__(self, campaign_name: str, language: str | dict = None, currency: str = None)`:
    -   **Аргументы:**
        -   `campaign_name` (`str`): Имя кампании.
        -   `language` (`str` | `dict`): Язык кампании.
        -   `currency` (`str`): Валюта кампании.
    -   **Возвращаемое значение:** `None`.
    -   **Назначение:** Инициализация объекта `AliCampaignGoogleSheet` и базового класса `SpreadSheet`.
-   `clear(self)`:
    -   **Аргументы:** `self`
    -   **Возвращаемое значение:** `None`.
    -   **Назначение:** Очистка Google Sheets путем удаления листов продуктов.
-   `delete_products_worksheets(self)`:
     -   **Аргументы:** `self`
    -   **Возвращаемое значение:** `None`.
    -   **Назначение:** Удаляет листы, кроме "categories" и "product_template".
-    `set_campaign_worksheet(self, campaign: SimpleNamespace)`:
      -   **Аргументы:**
           - `campaign`: SimpleNamespace -  объект с данными кампании.
    -   **Возвращаемое значение:** `None`.
    -   **Назначение:** Записывает данные кампании в Google Sheets.
-    `set_products_worksheet(self, category_name: str)`:
      -   **Аргументы:**
           - `category_name` (`str`): Имя категории.
    -   **Возвращаемое значение:** `None`.
    -   **Назначение:** Записывает данные о продуктах в Google Sheets.
-    `set_categories_worksheet(self, categories: SimpleNamespace)`:
      -   **Аргументы:**
           - `categories` (`SimpleNamespace`): Объект с данными о категориях.
    -   **Возвращаемое значение:** `None`.
    -   **Назначение:** Записывает данные о категориях в Google Sheets.
-   `get_categories(self)`:
    -   **Аргументы:** `self`.
    -   **Возвращаемое значение:** `list[dict]` - Список словарей с данными о категориях.
    -   **Назначение:** Получает данные о категориях из Google Sheets.
-    `set_category_products(self, category_name: str, products: dict)`:
        -   **Аргументы:**
            -   `category_name` (`str`): Имя категории.
            -   `products` (`dict`): Словарь с данными продуктов.
    -   **Возвращаемое значение:** `None`.
    -   **Назначение:** Записывает данные продуктов в Google Sheets.
-   `_format_categories_worksheet(self, ws: Worksheet)`:
    -   **Аргументы:**
        -   `ws` (`Worksheet`): Лист Google Sheets.
    -   **Возвращаемое значение:** `None`.
    -   **Назначение:** Форматирует лист с категориями.
-    `_format_category_products_worksheet(self, ws: Worksheet)`:
        -   **Аргументы:**
            -   `ws` (`Worksheet`): Лист Google Sheets.
        -   **Возвращаемое значение:** `None`.
        -   **Назначение:** Форматирует лист с продуктами.

**Переменные:**

-   `spreadsheet_id`: ID Google Sheets документа (строка).
-   `spreadsheet`: Экземпляр класса `SpreadSheet`.
-   `worksheet`: Экземпляр класса `Worksheet`.
-   `campaign_name`: Имя кампании (строка).
-    `language`: Язык кампании (строка).
-    `currency`: Валюта кампании (строка).
-    `campaign`: SimpleNamespace - объект с данными кампании.
-    `categories`: SimpleNamespace -  объект с данными о категориях.
-   `category_name`: Имя категории (строка).
-   `products`: Список словарей с данными о продуктах.
-   `ws`: Экземпляр класса `Worksheet`.
-   `updates`: Список словарей для обновления данных в Google Sheets.
-   `headers`: Список заголовков для Google Sheets.
-    `row_data`: Список данных для записи в Google Sheets.

**Потенциальные ошибки и области для улучшения:**

-   **Обработка ошибок:** В коде есть общие блоки `try...except`, которые ловят все исключения. Желательно обрабатывать конкретные исключения для более точного логирования и отладки.
-   **Унификация форматирования:**  Код содержит дублирование логики форматирования. Можно вынести общие части в отдельные функции.
-   **Использование констант:** Жестко заданные значения, такие как `A1:E1` и `A2:E{1 + len(rows)}` должны быть заменены на константы или вычислены динамически.
-   **Избыточность переменных:** Есть переменные, которые не используются. Их следует удалить.
-   **Проверка входных данных**: Необходимо добавить проверки на входные данные.
-   **Зависимость от структуры SimpleNamespace**: Код сильно зависит от конкретной структуры `SimpleNamespace`, что делает его хрупким.
-   **Комментарии:** Требуется больше комментариев в коде.

**Взаимосвязь с другими частями проекта:**

-   Использует `src.goog.spreadsheet.spreadsheet.SpreadSheet` для базовых операций с Google Sheets.
-   Использует `src.utils.printer` для форматированного вывода, но в коде не используется.
-   Использует `src.logger.logger` для логирования событий.
-   Использует `src.ai.openai.translate`, но в коде не используется.
-   Планируется использование `src.suppliers.aliexpress.campaign.editor`, но в коде закомментирован.
-   Использует `gspread` и `gspread_formatting` для работы с Google Sheets.
-   Данный модуль является частью системы управления рекламными кампаниями для AliExpress.