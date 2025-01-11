## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1. **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2. **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```

3. **<объяснение>**: Предоставьте подробные объяснения:
   - **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.
   - **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.
   - **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.
   - **Переменные**: Их типы и использование.
   - Выделите потенциальные ошибки или области для улучшения.

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

1. **Инициализация `AliCampaignGoogleSheet`:**
    *   При создании объекта `AliCampaignGoogleSheet` вызывается конструктор `__init__`.
    *   Вызывается конструктор родительского класса `SpreadSheet` с `spreadsheet_id`.
    *   Сохраняется имя кампании, язык и валюта (если предоставлены).
    *   **Пример**: `campaign_sheet = AliCampaignGoogleSheet(campaign_name="Summer Sale", language="en", currency="USD")`

2.  **Очистка Google Sheets (`clear`):**
    *   Вызывается метод `clear()`.
    *   Вызывается метод `delete_products_worksheets()` для удаления всех листов, кроме `'categories'`, `'product'`, `'category'`, `'campaign'`.
    *   **Пример**: `campaign_sheet.clear()`
    *  Метод `delete_products_worksheets()`:
         *   Получает список всех листов.
        *   Проходит по списку, и если название листа не находится в списке исключений `{'categories', 'product', 'category', 'campaign'}`
        *   Удаляет лист и логирует сообщение об удалении.

3.  **Запись данных о кампании (`set_campaign_worksheet`):**
    *   Вызывается метод `set_campaign_worksheet` с объектом `SimpleNamespace` (или его аналогом) с данными о кампании (имя, заголовок, язык, валюта, описание).
        *    Получает worksheet `campaign`.
    *   Формирует список обновлений для пакетной записи данных в ячейки листа "campaign".
    *   Вызывает `batch_update` для записи данных в Google Sheets.
    *   **Пример:**
        ```python
        campaign_data = SimpleNamespace(
            campaign_name="Summer Sale",
            title="Summer Sale 2024",
            language="en",
            currency="USD",
            description="Summer Sale Campaign Description"
        )
        campaign_sheet.set_campaign_worksheet(campaign_data)
        ```

4.  **Запись данных о продуктах (`set_products_worksheet`):**
    *   Вызывается метод `set_products_worksheet`, принимает название категории.
        *  Получает объект `category` из `self.editor.campaign.category` по имени категории `category_name`
        *  Получает список продуктов `products` из объекта `category`
    *  Копирует шаблонный лист `product` и переименовывает в имя категории `category_name`.
        *  Проходит по списку продуктов и формирует список данных для записи в виде массива.
        *  Записывает данные в соответствующие ячейки.
    *   Вызывает `_format_category_products_worksheet` для форматирования листа.
        * Устанавливает ширину столбцов.
         * Устанавливает высоту заголовка.
         * Форматирует ячейки заголовка.
    *   **Пример:**
        ```python
        products_data = [
            SimpleNamespace(product_id="123", product_title="Product 1", app_sale_price=10.0, original_price=20.0, sale_price=15.0, discount=0.25, product_main_image_url="url1", local_image_path="path1", product_small_image_urls=["url2", "url3"], product_video_url="url4", local_video_path="path2", first_level_category_id="1", first_level_category_name="Category1", second_level_category_id="2", second_level_category_name="Category2", target_sale_price=12.0, target_sale_price_currency="USD", target_app_sale_price_currency="USD", target_original_price_currency="USD", original_price_currency="USD", evaluate_rate="4.5", promotion_link="link1", shop_url="shop1", shop_id="shopid1", tags=["tag1", "tag2"]),
              SimpleNamespace(product_id="456", product_title="Product 2", app_sale_price=20.0, original_price=30.0, sale_price=25.0, discount=0.15, product_main_image_url="url5", local_image_path="path3", product_small_image_urls=["url6", "url7"], product_video_url="url8", local_video_path="path4", first_level_category_id="3", first_level_category_name="Category3", second_level_category_id="4", second_level_category_name="Category4", target_sale_price=22.0, target_sale_price_currency="USD", target_app_sale_price_currency="USD", target_original_price_currency="USD", original_price_currency="USD", evaluate_rate="4.0", promotion_link="link2", shop_url="shop2", shop_id="shopid2", tags=["tag3", "tag4"])
        ]

        category_data = SimpleNamespace(
            products=products_data
        )

        campaign_editor = SimpleNamespace(
           campaign = SimpleNamespace(
                category = SimpleNamespace(
                    test_category = category_data
               )
            )
        )
         campaign_sheet.editor = campaign_editor

        campaign_sheet.set_products_worksheet(category_name="test_category")
        ```

5. **Запись данных о категориях (`set_categories_worksheet`):**
    *   Вызывается метод `set_categories_worksheet` с объектом `SimpleNamespace`, содержащим данные о категориях.
    *   Получает рабочий лист  `'categories'`.
    *   Очищает лист перед записью данных.
    *   Формирует заголовки таблицы и записывает их в первую строку листа.
    *   Проходит по данным категорий, формирует строки для записи и записывает их.
    *   Вызывает `_format_categories_worksheet` для форматирования листа.
        *   Устанавливает ширину столбцов.
        *   Устанавливает высоту строки заголовка.
        *   Форматирует строку заголовка.
    *   **Пример:**
        ```python
        categories_data = SimpleNamespace(
            category1=SimpleNamespace(name="category1", title="Category 1", description="Description 1", tags=["tag1", "tag2"], products_count=10),
            category2=SimpleNamespace(name="category2", title="Category 2", description="Description 2", tags=["tag3", "tag4"], products_count=20)
        )
        campaign_sheet.set_categories_worksheet(categories_data)
        ```

6.  **Получение данных о категориях (`get_categories`):**
    *   Вызывается метод `get_categories`.
    *   Получает данные из листа `'categories'` в виде списка словарей.
    *   Возвращает полученные данные.
    *   **Пример**: `categories = campaign_sheet.get_categories()`

7. **Запись данных о продуктах в лист (`set_category_products`):**
    *   Вызывается метод `set_category_products` с названием категории и словарем продуктов.
    *   Копирует шаблонный лист `product` и переименовывает в имя категории.
    *   Формирует заголовки и записывает их в первую строку листа.
    *   Проходит по данным продуктов, формирует строки для записи и записывает их.
    *  Вызывает `_format_category_products_worksheet` для форматирования листа.
        * Устанавливает ширину столбцов.
         * Устанавливает высоту заголовка.
         * Форматирует ячейки заголовка.
    *   **Пример:**
        ```python
         products_data = [
                SimpleNamespace(product_id="123", product_title="Product 1", app_sale_price=10.0, original_price=20.0, sale_price=15.0, discount=0.25, product_main_image_url="url1", local_image_path="path1", product_small_image_urls=["url2", "url3"], product_video_url="url4", local_video_path="path2", first_level_category_id="1", first_level_category_name="Category1", second_level_category_id="2", second_level_category_name="Category2", target_sale_price=12.0, target_sale_price_currency="USD", target_app_sale_price_currency="USD", target_original_price_currency="USD", original_price_currency="USD", evaluate_rate="4.5", promotion_link="link1", shop_url="shop1", shop_id="shopid1", tags=["tag1", "tag2"]),
                  SimpleNamespace(product_id="456", product_title="Product 2", app_sale_price=20.0, original_price=30.0, sale_price=25.0, discount=0.15, product_main_image_url="url5", local_image_path="path3", product_small_image_urls=["url6", "url7"], product_video_url="url8", local_video_path="path4", first_level_category_id="3", first_level_category_name="Category3", second_level_category_id="4", second_level_category_name="Category4", target_sale_price=22.0, target_sale_price_currency="USD", target_app_sale_price_currency="USD", target_original_price_currency="USD", original_price_currency="USD", evaluate_rate="4.0", promotion_link="link2", shop_url="shop2", shop_id="shopid2", tags=["tag3", "tag4"])
            ]
         campaign_editor = SimpleNamespace(
            campaign = SimpleNamespace(
                category = SimpleNamespace(
                    test_category = SimpleNamespace(
                        products=products_data
                    )
                )
            )
        )
        campaign_sheet.editor = campaign_editor
        campaign_sheet.set_category_products(category_name="test_category", products=products_data)
        ```

## <mermaid>

```mermaid
flowchart TD
    Start[Start] --> Initialize[Initialize AliCampaignGoogleSheet<br><code>__init__(campaign_name, language, currency)</code>]
    Initialize --> ClearSheets{Clear Sheets?<br><code>clear()</code>}
    ClearSheets -- Yes --> DeleteProductSheets[Delete Product Sheets<br><code>delete_products_worksheets()</code>]
    ClearSheets -- No --> SetCampaignData{Set Campaign Data?<br><code>set_campaign_worksheet(campaign_data)</code>}

    DeleteProductSheets --> SetCampaignData
    SetCampaignData -- Yes --> WriteCampaignData[Write Campaign Data]
    SetCampaignData -- No --> SetProductData{Set Product Data?<br><code>set_products_worksheet(category_name)</code>}

    WriteCampaignData --> SetProductData
    SetProductData -- Yes --> CopyProductSheet[Copy Product Template Sheet]
    CopyProductSheet --> WriteProductData[Write Product Data]
    WriteProductData --> FormatProductSheet[Format Product Sheet<br><code>_format_category_products_worksheet(ws)</code>]

    SetProductData -- No --> SetCategoryData{Set Category Data?<br><code>set_categories_worksheet(categories)</code>}
    FormatProductSheet --> SetCategoryData

    SetCategoryData -- Yes --> WriteCategoryData[Write Category Data]
    WriteCategoryData --> FormatCategorySheet[Format Category Sheet<br><code>_format_categories_worksheet(ws)</code>]
     FormatCategorySheet --> GetCategoriesData{Get Category Data?<br><code>get_categories()</code>}
    SetCategoryData -- No --> GetCategoriesData
    GetCategoriesData -- Yes -->  ReadCategoryData[Read Category Data]
     GetCategoriesData -- No -->  SetCategoryProducts{Set Category Products?<br><code>set_category_products(category_name, products)</code>}
   ReadCategoryData --> SetCategoryProducts
    SetCategoryProducts -- Yes --> CopyProductSheet2[Copy Product Template Sheet]
    CopyProductSheet2 --> WriteCategoryProductData[Write Product Data]
      WriteCategoryProductData --> FormatProductSheet2[Format Product Sheet<br><code>_format_category_products_worksheet(ws)</code>]
    FormatProductSheet2 --> End[End]
    SetCategoryProducts -- No --> End


    classDef box fill:#f9f,stroke:#333,stroke-width:2px
    class Initialize,ClearSheets,SetCampaignData,SetProductData,SetCategoryData, GetCategoriesData, SetCategoryProducts box
```

**Анализ зависимостей:**

*   `Start`: Начало выполнения программы.
*   `Initialize`: Создание экземпляра класса `AliCampaignGoogleSheet`, инициализация `spreadsheet_id`.
*   `ClearSheets`: Проверяет, нужно ли очистить данные.
*   `DeleteProductSheets`: Удаляет все листы, кроме `'categories'`, `'product'`, `'category'`, `'campaign'`.
*   `SetCampaignData`: Проверяет, нужно ли записать данные о кампании.
*   `WriteCampaignData`: Записывает данные о кампании в лист `'campaign'`.
*    `SetProductData`: Проверяет, нужно ли записать данные о продуктах.
*   `CopyProductSheet`: Копирует шаблонный лист `'product'`.
*   `WriteProductData`: Записывает данные о продуктах в лист.
*   `FormatProductSheet`: Форматирует лист с продуктами.
*    `SetCategoryData`: Проверяет, нужно ли записать данные о категориях.
*   `WriteCategoryData`: Записывает данные о категориях в лист `'categories'`.
*   `FormatCategorySheet`: Форматирует лист с категориями.
*   `GetCategoriesData`: Проверяет, нужно ли получить данные о категориях.
*   `ReadCategoryData`: Получает данные о категориях из листа `'categories'`.
*   `SetCategoryProducts`: Проверяет, нужно ли записать данные о продуктах в лист категории.
*   `CopyProductSheet2`: Копирует шаблонный лист `'product'`.
*   `WriteCategoryProductData`: Записывает данные о продуктах в лист.
*   `FormatProductSheet2`: Форматирует лист с продуктами.
*   `End`: Конец выполнения программы.

**Импорты:**

*   `time`: Используется для задержки времени. В данном коде не используется.
*   `SimpleNamespace` from `types`: Используется для создания простых объектов с атрибутами (как структуры).
*   `Optional`, `Any`, `List`, `Dict` from `typing`: Используются для аннотации типов данных.
*   `Worksheet` from `gspread.worksheet`: Используется для работы с листами Google Sheets.
*   `SpreadSheet` from `src.goog.spreadsheet.spreadsheet`: Базовый класс для работы с Google Sheets, унаследован `AliCampaignGoogleSheet`.
*   `j_dumps` from `src.utils.jjson`: Используется для преобразования Python объектов в JSON. В данном коде не используется.
*   `pprint` from `src.utils.printer`: Используется для красивого вывода данных.
*   `logger` from `src.logger.logger`: Используется для логирования событий.
*   `translate` from `src.ai.openai`: Используется для перевода текста. В данном коде не используется.
*  `cellFormat`, `textFormat`, `numberFormat`, `format_cell_range`, `set_column_width`, `set_row_height`, `Color` from `gspread_formatting`: Используются для форматирования листов Google Sheets.

## <объяснение>

**Импорты:**

*   `time`: Модуль для работы со временем, но в данном коде не используется. Возможно, планировалось использование для задержек между запросами к API Google Sheets.
*   `SimpleNamespace` from `types`: Позволяет создавать простые объекты, к которым можно обращаться через атрибуты. Удобно для хранения данных.
*   `Optional, Any, List, Dict` from `typing`: Используются для аннотаций типов, что делает код более понятным и помогает инструментам статического анализа.
*   `Worksheet` from `gspread.worksheet`: Класс из библиотеки `gspread` для представления и управления листами в Google Sheets.
*   `SpreadSheet` from `src.goog.spreadsheet.spreadsheet`: Класс, предоставляющий базовые операции для работы с Google Sheets (открытие, создание, удаление листов и т.д.). Этот класс импортируется из пакета `src.goog.spreadsheet`.
*   `j_dumps` from `src.utils.jjson`: Функция для сериализации объектов Python в JSON. В данном коде не используется, но доступна для потенциального использования.
*   `pprint` from `src.utils.printer`: Функция для более удобного вывода данных, чем стандартная функция `print`.
*   `logger` from `src.logger.logger`: Объект для логирования событий. Позволяет отслеживать ошибки и ход выполнения программы.
*    `translate` from `src.ai.openai`: Функция для перевода текста с использованием OpenAI API. В данном коде не используется.
*    `cellFormat`, `textFormat`, `numberFormat`, `format_cell_range`, `set_column_width`, `set_row_height`, `Color` from `gspread_formatting`: Используются для форматирования листов Google Sheets.

**Классы:**

*   `AliCampaignGoogleSheet(SpreadSheet)`:
    *   **Роль:** Класс для управления данными кампаний AliExpress в Google Sheets. Наследуется от `SpreadSheet`, что позволяет использовать его базовые методы для работы с Google Sheets.
    *   **Атрибуты:**
        *   `spreadsheet_id`: Статический идентификатор Google Sheets, к которому обращается класс.
        *   `spreadsheet`: Объект класса `SpreadSheet`, представляющий саму таблицу Google Sheets.
        *   `worksheet`: Объект класса `Worksheet`, представляющий текущий рабочий лист.
    *   **Методы:**
        *   `__init__(self, campaign_name, language, currency)`: Конструктор класса. Инициализирует объект `SpreadSheet` с идентификатором таблицы и сохраняет дополнительные параметры.
        *   `clear(self)`: Очищает содержимое Google Sheets, удаляя все листы с продуктами.
        *   `delete_products_worksheets(self)`: Удаляет все листы, кроме `'categories'`, `'product'`, `'category'`, `'campaign'`.
        *   `set_campaign_worksheet(self, campaign)`: Записывает данные о кампании на лист `'campaign'`.
        *   `set_products_worksheet(self, category_name)`: Записывает данные о продуктах для конкретной категории на отдельный лист, скопированный из шаблона `'product'`.
        *   `set_categories_worksheet(self, categories)`: Записывает данные о категориях на лист `'categories'`.
        *   `get_categories(self)`: Получает данные о категориях с листа `'categories'`.
         *    `set_category_products(self, category_name, products)`: Записывает данные о продуктах в лист категории, скопированный из шаблона `'product'`.
        *   `_format_categories_worksheet(self, ws)`: Форматирует лист с категориями, устанавливая ширину столбцов, высоту строк и форматирование ячеек заголовка.
        *   `_format_category_products_worksheet(self, ws)`: Форматирует лист с продуктами категории, устанавливая ширину столбцов, высоту строк и форматирование ячеек заголовка.

**Функции:**

*   Конструктор `__init__` инициализирует объект класса, создавая соединение с Google Sheets через родительский класс `SpreadSheet`. Сохраняет параметры кампании (имя, язык, валюту).
*   Метод `clear()` вызывает удаление всех листов, кроме основных (категории, шаблон продукта, кампания).
*   Метод `delete_products_worksheets()` удаляет все листы, кроме `'categories'`, `'product'`, `'category'`, `'campaign'`.
*   Метод `set_campaign_worksheet()` принимает объект с данными кампании, форматирует эти данные и записывает их в Google Sheets.
*   Метод `set_products_worksheet()` записывает данные о продуктах в Google Sheets, используя шаблонный лист `'product'`, который копируется и переименовывается в имя категории.
*   Метод `set_categories_worksheet()` принимает объект с данными о категориях, форматирует эти данные и записывает их в Google Sheets.
*   Метод `get_categories()` получает данные из Google Sheets в виде списка словарей.
*   Метод `set_category_products()` записывает данные о продуктах в Google Sheets, используя шаблонный лист `'product'`, который копируется и переименовывается в имя категории.
*   Методы `_format_categories_worksheet()` и `_format_category_products_worksheet()` форматируют листы Google Sheets (ширина столбцов, высота строк, стили ячеек).

**Переменные:**

*   `spreadsheet_id`: Статический ID Google Sheets, с которым работает класс.
*   `spreadsheet`: Объект для работы с Google Sheets.
*   `worksheet`: Объект для работы с конкретным листом Google Sheets.
*   `campaign_name`, `language`, `currency`: Параметры кампании.
*   `updates`: Список для пакетных обновлений Google Sheets.
*   `vertical_data`: Данные для вертикальной записи на листе `'campaign'`.
*   `headers`: Заголовки для таблицы в Google Sheets.
*   `products`: Список данных продуктов.
*   `categories`: Объект, содержащий данные о категориях.
*  `row_data`: Список данных для записи в строку.
*   `ws`: Экземпляр `gspread.worksheet.Worksheet` для работы с листом.
*   `category_data`: Данные о категориях в виде словаря.

**Потенциальные ошибки и улучшения:**

*   **Обработка ошибок:** Код имеет общую обработку исключений `try...except`, но можно сделать более точную обработку, в зависимости от типа исключения.
*   **Задержки между запросами:** При большом количестве операций, стоит добавить задержки между вызовами API Google Sheets, чтобы не превысить лимиты.
*   **Использование `SimpleNamespace`:** Использование `SimpleNamespace` может быть не оптимальным для сложных структур данных. Можно использовать `dataclasses` или `pydantic` для более строгой типизации и валидации.
*   **Форматирование:** Код форматирует листы каждый раз после записи данных. Можно сделать это один раз после записи всех данных, для экономии времени.
*   **Дублирование кода:** Код `set_products_worksheet` и `set_category_products` имеет много общего, можно рефакторить в отдельную функцию.

**Взаимосвязь с другими частями проекта:**

*   `src.goog.spreadsheet.spreadsheet`: Этот модуль предоставляет базовую функциональность для работы с Google Sheets, такую как открытие таблицы, получение доступа к листам. `AliCampaignGoogleSheet` наследуется от него, чтобы использовать эти возможности.
*   `src.logger.logger`: Логирует события, что помогает отслеживать работу модуля и выявлять ошибки.
*   `src.ai.openai`: (не используется) В теории, можно использовать для перевода текста, для данных в Google Sheets.
*   `src.utils.jjson` (не используется)
*   `src.utils.printer`

Этот модуль представляет собой уровень абстракции для работы с Google Sheets, предоставляя удобные методы для управления данными кампаний AliExpress. Его можно интегрировать в другие модули, которые отвечают за получение данных о кампаниях и продуктах, а также для их обработки.