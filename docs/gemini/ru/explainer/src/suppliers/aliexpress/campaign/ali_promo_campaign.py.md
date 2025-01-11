## АНАЛИЗ КОДА: `src/suppliers/aliexpress/campaign/ali_promo_campaign.py`

### <алгоритм>
**Общий процесс работы `AliPromoCampaign`:**

1.  **Инициализация (`__init__`)**:
    *   Принимает `campaign_name`, `language`, `currency`, и `model` как параметры.
    *   Формирует путь к файлу кампании на основе `campaign_name`, `language`, и `currency`.
    *   Пытается загрузить существующий файл кампании (`.json`) с помощью `j_loads_ns`.
    *   Если файл не найден, вызывает `process_new_campaign` для создания новой кампании.
    *   Загружает или устанавливает `language` и `currency`.
    *   Инициализирует модели AI (`_models_payload`).

2.  **Создание новой кампании (`process_new_campaign`)**:
    *   Если `language` и `currency` не указаны, обрабатывает все локали (из `locales`).
    *   Для каждой локали создает структуру кампании (объект `SimpleNamespace`).
    *   Вызывает `set_categories_from_directories`, чтобы установить категории из директорий.
    *   Для каждой категории вызывает `process_category_products` и `process_ai_category`.
    *   Сохраняет созданную структуру в JSON-файл.

    **Пример:**

    ```python
    campaign = AliPromoCampaign(campaign_name="NewSale", language="EN", currency="USD")
    # Если файла NewSale_EN_USD.json нет, то вызовется process_new_campaign
    ```

3.  **Установка категорий из директорий (`set_categories_from_directories`)**:
    *   Получает имена директорий в `category` директории.
    *   Создает атрибуты в `self.campaign.category` для каждой директории, преобразуя каждую в объект `SimpleNamespace`.

    **Пример:**
    Предположим, что у нас есть следующие папки: `category/electronics`, `category/clothing`:
    ```
    self.set_categories_from_directories()
    print(self.campaign.category.electronics.category_name)  # Выведет: electronics
    print(self.campaign.category.clothing.category_name)    # Выведет: clothing
    ```

4.  **Обработка кампании (`process_campaign`)**:
    *   Получает список названий категорий из директорий.
    *   Итерируется по каждой категории, вызывая `process_category_products` и `process_ai_category`.

    **Пример:**
    ```python
    campaign.process_campaign() # для каждой папки в `category` вызовет process_category_products и process_ai_category
    ```

5.  **Обработка товаров в категории (`process_category_products`)**:
    *   Вызывает `read_sources` для получения списка `product_id`.
    *   Если `product_id` не найден, возвращает `None`.
    *   Инициализирует `AliAffiliatedProducts` и запускает процесс обработки партнерских продуктов.
    *   Возвращает список `SimpleNamespace`, содержащий данные товаров.

    **Пример:**
    ```python
    products = campaign.process_category_products(category_name="electronics") # вернет все продукты из categories/electronics
    ```

6.  **Чтение источников товаров (`read_sources`)**:
    *   Ищет HTML-файлы в директории `sources`.
    *   Пытается получить ID товаров из HTML.
    *   Также ищет `sources.txt` и извлекает ID товаров из URL.

    **Пример:**
    Предположим, в `category/electronics/sources` есть `product1.html` и `sources.txt`:
    ```python
        prod_ids = self.read_sources(category_name='electronics')
        print(prod_ids) # Выведет список ID товаров, найденных в html и файле sources.txt
    ```

7.  **Обработка AI для категорий (`process_ai_category`)**:
    *   Загружает инструкции для AI из файла.
    *   Инициализирует модель AI (`GoogleGenerativeAI` или `OpenAIModel`).
    *   Если указана категория, обрабатывает только её. В противном случае обрабатывает все категории.
    *   Для каждой категории:
        *   Читает названия товаров из файла `product_titles.txt`.
        *   Генерирует запрос для AI.
        *   Получает ответ от AI, преобразует его в объект `SimpleNamespace`.
        *   Обновляет (или добавляет) атрибуты категории на основе ответа AI.

    **Пример:**
    ```python
    campaign.process_ai_category(category_name="electronics") # вызовется AI для category electronics
    campaign.process_ai_category() # вызовется AI для всех категорий
    ```

8.  **Сохранение данных о товарах в файлы (`dump_category_products_files`)**:
    *   Сохраняет каждый товар из списка в JSON файл (`<product_id>.json`) в директории категории.

    **Пример:**
        ```python
        campaign.dump_category_products_files("electronics", products) # products - список SimpleNamespace
        #  сохранит все product в формате <product_id>.json в папку category/electronics
        ```

9.  **Генерация HTML (`generate_html`)**:
    *   Генерирует HTML-страницу для каждой категории с карточками товаров.
    *   Создает `index.html`, содержащий ссылки на страницы категорий.

    **Пример:**
    ```python
        await campaign.generate_html(campaign_name='test',category_path='/path/to/category', products_list=products)
    ```

10. **Генерация HTML для кампании (`generate_html_for_campaign`)**:
    *   Итерирует по категориям.
    *   Для каждой категории получает список товаров.
    *   Использует `ProductHTMLGenerator` и `CategoryHTMLGenerator` для генерации HTML-страниц.
    *   Использует `CampaignHTMLGenerator` для создания общей HTML-страницы для всей кампании.

    **Пример:**
    ```python
    campaign.generate_html_for_campaign(campaign_name="SummerSale")
    ```

11. **Генерация выходных файлов (`generate_output`)**:
    *   Сохраняет товары в формате `<product_id>.json`.
    *   Сохраняет названия товаров и ссылки на товары.
    *   Вызывает `generate_html`.

    **Пример:**
    ```python
    await campaign.generate_output("CampaignName", category_path, products_list)
    ```
### <mermaid>
```mermaid
flowchart TD
    subgraph AliPromoCampaign
        Start(Start) --> Init[__init__]
        Init --> LoadCampaignData{Load Campaign Data}
        LoadCampaignData -- File Exists --> SetCampaignProps[Set Campaign Properties]
        LoadCampaignData -- File Not Found --> ProcessNewCampaignCall[Call process_new_campaign]
        SetCampaignProps --> ModelsPayload[Call _models_payload]
        ProcessNewCampaignCall --> ProcessNewCampaign[process_new_campaign]
        ModelsPayload --> ProcessCampaignCall[Call process_campaign]
        ProcessCampaignCall --> ProcessCampaign[process_campaign]

    end
    
    subgraph process_new_campaign
        ProcessNewCampaign --> CheckLocale[Check if language and currency]
        CheckLocale -- Not Provided --> SetAllLocales[Set All Locales from locales]
        CheckLocale -- Provided --> SetSingleLocale[Set Language and Currency]
        SetAllLocales --> LoopLocales[Loop for each locale]
        SetSingleLocale -->  LoopLocales
        LoopLocales --> CreateCampaignObject[Create Campaign Object SimpleNamespace]
        CreateCampaignObject --> SetCategoriesFromDirCall[Call set_categories_from_directories]
        SetCategoriesFromDirCall --> SetCategoriesFromDir[set_categories_from_directories]
        SetCategoriesFromDir --> CopyCampaignAICall[Create self.campaign_ai, AI File name]
        CopyCampaignAICall --> CopyCampaignAI[copy.copy(self.campaign)]
        CopyCampaignAI --> LoopCategories[Loop for each category]
        LoopCategories --> ProcessCategoryProductsCall[Call process_category_products]
        ProcessCategoryProductsCall --> ProcessCategoryProducts[process_category_products]
        ProcessCategoryProducts --> ProcessAICategoryCall[Call process_ai_category]
        ProcessAICategoryCall --> ProcessAICategory[process_ai_category]
        ProcessAICategory --> SaveCampaignJSON[Save campaign to JSON]

    end

   subgraph process_campaign
        ProcessCampaign --> GetCategoryNames[Get categories names from directory]
        GetCategoryNames --> LoopCategoriesCampaign[Loop for each category name]
        LoopCategoriesCampaign --> ProcessCategoryProductsCallCampaign[Call process_category_products]
        ProcessCategoryProductsCallCampaign --> ProcessCategoryProductsCampaign[process_category_products]
        ProcessCategoryProductsCampaign --> ProcessAICategoryCallCampaign[Call process_ai_category]
        ProcessAICategoryCallCampaign --> ProcessAICategoryCampaign[process_ai_category]

    end
    
    subgraph process_category_products
        ProcessCategoryProducts --> ReadSourcesCall[Call read_sources]
        ReadSourcesCall --> ReadSources[read_sources]
         ReadSources --> CheckProductIDs{Check if product_ids is empty}
         CheckProductIDs -- Is Empty --> ReturnNone[Return None]
        CheckProductIDs -- Not Empty --> InitAffiliatedProducts[Init AliAffiliatedProducts]
        InitAffiliatedProducts --> ProcessAffiliateProductsCall[Call process_affiliate_products]
        ProcessAffiliateProductsCall --> ProcessAffiliateProducts[process_affiliate_products]
        ProcessAffiliateProducts -->  ReturnProducts[Return affiliated_products]

    end
   
    subgraph process_ai_category
         ProcessAICategory --> LoadSystemInstructions[Load AI System Instructions]
         LoadSystemInstructions --> InitAIModel[Init AI Model]
         InitAIModel --> CheckCategoryName{Check category_name is provided}
        CheckCategoryName -- Yes --> ProcessCategoryAICall[Call _process_category]
        ProcessCategoryAICall --> ProcessCategoryAI[ _process_category(category_name) ]
         CheckCategoryName -- No -->  LoopAllCategories[Loop through all categories]
        LoopAllCategories -->  ProcessCategoryAICall_All[Call _process_category]
        ProcessCategoryAICall_All --> ProcessCategoryAI_All[ _process_category(category_name) ]
        ProcessCategoryAI_All --> SaveAIJSON[Save AI JSON]
         ProcessCategoryAI --> SaveAIJSON
    end
     subgraph _process_category
        ProcessCategoryAI --> LoadProductTitles[Read product titles from file]
        LoadProductTitles --> GenerateAIPrompt[Generate AI prompt]
         GenerateAIPrompt --> GetAIResponseCall[Call get_response]
        GetAIResponseCall --> GetAIResponse[get_response from AI]
        GetAIResponse --> CheckAIResponse{Check AI response}
        CheckAIResponse -- No Response --> ReturnFromProcessCategory[Return]
        CheckAIResponse -- Response  --> LoadAIResponse[Load AI response]
        LoadAIResponse --> UpdateCategory[Update Category Data]
        UpdateCategory -->  ReturnFromProcessCategory[Return]
     end
     
     subgraph read_sources
        ReadSources --> GetHTMLFiles[Get HTML Files]
        GetHTMLFiles --> ExtractIDsFromHTML[Extract Product IDs from HTML]
        ExtractIDsFromHTML --> ReadSourcesTXT[Read sources.txt file]
        ReadSourcesTXT --> ExtractIDsFromTXT[Extract Product IDs from sources.txt]
        ExtractIDsFromTXT --> CombineIDs[Combine IDs]
        CombineIDs --> CheckIDs{Check if product ids is empty}
        CheckIDs -- Is Empty --> ReturnNoneSources[Return None]
        CheckIDs -- Not Empty --> ReturnIDs[Return Product IDs]
     end
     
    subgraph generate_output
        StartOutput(Start) --> FormatTimestamp[Format timestamp]
        FormatTimestamp --> CheckProductsList[Check if products_list is a list]
        CheckProductsList -- No --> ConvertToList[Convert products_list to a list]
        CheckProductsList -- Yes --> InitOutputLists[Init lists: _data_for_openai, _promotion_links_list, _product_titles]
        ConvertToList --> InitOutputLists
        InitOutputLists --> LoopProducts[For each product in products_list]
        LoopProducts --> CreateCategoriesConverter[Create categories_convertor dictionary]
        CreateCategoriesConverter --> AddConverterToProduct[Add categories_convertor to product]
        AddConverterToProduct --> SaveProductJSON[Save product as <product_id>.json]
        SaveProductJSON --> AppendProductInfo[Append product_title and promotion_link to respective lists]
        AppendProductInfo --> SaveProductTitlesCall[Call save_product_titles]
        SaveProductTitlesCall --> SaveProductTitles[save_product_titles]
        SaveProductTitles --> SavePromotionLinksCall[Call save_promotion_links]
        SavePromotionLinksCall --> SavePromotionLinks[save_promotion_links]
        SavePromotionLinks --> GenerateHTMLCall[Call generate_html]
        GenerateHTMLCall --> GenerateHTML[generate_html]
    end
   
    subgraph generate_html
        StartGenerateHtml(Start) --> CheckIsList[Check if products_list is list]
        CheckIsList -- No --> ConvertToListHtml[Convert to list]
        CheckIsList -- Yes --> GetCategoryName[Get category name from category_path]
        ConvertToListHtml --> GetCategoryName
        GetCategoryName --> SetCategoryHTMLPath[Set category html path]
        SetCategoryHTMLPath --> InitCategoryDict[Init category dict]
        InitCategoryDict --> StartHTMLContent[Start html content]
        StartHTMLContent --> LoopProductsHTML[For each product in products_list]
         LoopProductsHTML --> AppendProductToCategory[Append product details to category dict]
        AppendProductToCategory --> AddProductDetailsToHTML[Add product details to HTML content]
        AddProductDetailsToHTML --> EndHTMLContent[End HTML content]
        EndHTMLContent --> SaveHTMLFile[Save HTML file]
        SaveHTMLFile --> GenerateMainIndexHTML[Generate main index.html]
         GenerateMainIndexHTML --> CollectCategoryLinks[Collect all category links]
          CollectCategoryLinks --> GenerateIndexHTML[Generate index.html content]
           GenerateIndexHTML --> SaveIndexHTML[Save index.html file]

    end
    
    
     subgraph header.py
        StartHeader(Start) --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>] 
    end
     
  
```

### <объяснение>

**Импорты:**

*   `header`: Предположительно, модуль для определения корня проекта и настройки среды. Используется для доступа к глобальным настройкам и путям.
*   `asyncio`: Модуль для поддержки асинхронных операций.
*   `time`: Модуль для работы со временем.
*   `copy`: Модуль для создания копий объектов.
*    `html`: Модуль для работы с HTML.
*   `pathlib.Path`: Класс для работы с путями к файлам и директориям.
*   `types.SimpleNamespace`: Класс для создания простых объектов с произвольными атрибутами.
*   `typing.List, Optional, Dict`: Модули для статической типизации.
*   `src.gs`: Глобальные настройки проекта.
*   `src.suppliers.aliexpress.campaign`: Сам модуль, для структурирования проекта.
*   `src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts`: Класс для генерации партнерских ссылок AliExpress.
*   `src.suppliers.aliexpress.utils.locales`: Модуль, содержащий локали для кампаний.
*   `src.ai.gemini.GoogleGenerativeAI`: Класс для работы с AI Gemini.
*   `src.ai.openai.OpenAIModel`: Класс для работы с AI OpenAI.
*   `src.suppliers.aliexpress.campaign.html_generators`: Модули для генерации HTML-страниц.
*   `src.logger.logger`: Модуль для ведения журнала.
*   `src.utils.file_async`: Асинхронные функции для работы с файлами.
*   `src.utils.jjson`: Модуль для работы с JSON.
*   `src.utils.convertors.csv`: Модуль для работы с CSV.
*    `src.utils.file`: Функции для работы с файлами.
*   `src.utils.printer.pprint`: Функция для удобной печати объектов.
*   `src.suppliers.aliexpress.utils.extract_product_id.extract_prod_ids`: Функция для извлечения ID товаров.
*   `datetime`: Модуль для работы с датой и временем.
    
   **header.py:**
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>] 
    ```

**Классы:**

*   `AliPromoCampaign`:
    *   **Роль:** Основной класс для управления рекламными кампаниями AliExpress.
    *   **Атрибуты:**
        *   `language` (str): Язык кампании.
        *   `currency` (str): Валюта кампании.
        *   `base_path` (Path): Базовый путь к директории кампании.
        *   `campaign_name` (str): Имя кампании.
        *   `campaign` (SimpleNamespace): Объект, представляющий структуру кампании.
        *    `campaign_ai` (SimpleNamespace): Объект, представляющий AI-сгенерированную структуру кампании.
        *   `gemini` (GoogleGenerativeAI): Экземпляр модели Gemini.
        *   `openai` (OpenAIModel): Экземпляр модели OpenAI.
    *   **Методы:**
        *   `__init__`: Инициализирует объект, загружает данные кампании или создает новую.
        *   `_models_payload`: Загружает AI модели и настройки.
        *   `process_campaign`: Итерируется по категориям и обрабатывает их.
        *   `process_campaign_category`: Обрабатывает определенную категорию.
        *   `process_new_campaign`: Создает новую кампанию.
        *   `process_ai_category`: Обрабатывает данные AI для категорий.
        *   `process_category_products`: Обрабатывает товары в категории.
        *   `dump_category_products_files`: Сохраняет данные товаров в JSON.
        *   `set_categories_from_directories`: Устанавливает категории из директорий.
        *   `generate_output`: Сохраняет выходные файлы (JSON, TXT, HTML).
         *  `generate_html`: Генерирует HTML файлы для категории.
        *   `generate_html_for_campaign`: Генерирует HTML страницы для всей кампании.

**Функции:**

*   `read_sources(category_name)`:
    *   **Аргументы:** `category_name` (str).
    *   **Возвращает:** `Optional[List[str]]`.
    *   **Назначение:** Читает HTML-файлы и `sources.txt`, извлекает `product_id`.
    *   **Пример:**
        ```python
        product_ids = read_sources(category_name="electronics")
        # -> ['12345', '67890', ...]
        ```
*   `_process_category(category_name)`:
    *   **Аргументы:** `category_name` (str).
    *  **Возвращает:** `None`.
    *   **Назначение:** Обрабатывает AI для конкретной категории.
    *   **Пример:**
        ```python
        _process_category(category_name="electronics")
        # -> обрабатывает AI данные для категории electronics
        ```

*  `generate_html(campaign_name, category_path, products_list)`:
    *   **Аргументы:** `campaign_name` (str), `category_path` (str or Path), `products_list` (list of SimpleNamespace).
    *   **Возвращает:** `None`.
    *   **Назначение:** Генерирует HTML для категории, включая HTML карточки товаров и главный `index.html` файл со ссылками на категории.

*   `generate_output(campaign_name, category_path, products_list)`:
    *   **Аргументы:** `campaign_name` (str), `category_path` (str or Path), `products_list` (list of SimpleNamespace).
    *  **Возвращает:** `None`.
    *   **Назначение:** Сохраняет данные о товарах в различных форматах (JSON, TXT, HTML).

**Переменные:**

*   `language` (str): Язык кампании.
*   `currency` (str): Валюта кампании.
*   `base_path` (Path): Путь к директории кампании.
*   `campaign` (SimpleNamespace): Структура данных кампании.
*   `gemini` (GoogleGenerativeAI): Экземпляр AI модели.
*   `openai` (OpenAIModel): Экземпляр AI модели.
*   `locales` (List[Dict[str, str]]): Список словарей, определяющих локали.
*   `products` (List[SimpleNamespace]): Список объектов `SimpleNamespace` с данными о товарах.
*  `category_name`(str):  Название категории.
* `product_titles`(list): Список названий товаров
* `promotion_links`(list): Список ссылок на товары.

**Потенциальные ошибки и области для улучшения:**

1.  **Обработка ошибок:**
    *   Необходимо более тщательно обрабатывать исключения, особенно при взаимодействии с AI и чтении/записи файлов.
2.  **Асинхронность:**
    *   Не все операции асинхронные, что может замедлять работу. Стоит использовать `async` для всех I/O операций, например чтение файлов.
3.  **Использование SimpleNamespace:**
    *   Хотя `SimpleNamespace` удобен, стоит рассмотреть использование более строгих классов данных для типизации и большей надежности.
4.  **Модульность:**
    *   Некоторые части кода могут быть вынесены в отдельные функции или классы для улучшения читаемости и поддержки.
5.  **Генерация HTML:**
    *   Логика генерации HTML может быть улучшена путем использования шаблонизатора.
6.  **Управление моделями AI:**
    *   Загрузка моделей AI происходит неоптимально, стоит перенести в кэш или переиспользовать.
7.  **Логирование:**
    *   Логирование можно сделать более информативным, добавив больше деталей в журнал.

**Взаимосвязи с другими частями проекта:**

*   **`src.gs`**: Используется для получения глобальных настроек и путей.
*   **`src.ai`**: Используются для интеграции с AI моделями (Gemini, OpenAI).
*   **`src.suppliers.aliexpress`**: Работает с модулями для получения партнерских ссылок и обработки данных AliExpress.
*    **`src.utils`**: Используются утилиты для работы с файлами, JSON, CSV, логированием и печатью.
*  `src.suppliers.aliexpress.campaign.html_generators` : используются модули генерации HTML.
* **`src.logger.logger`**: Модуль ведения журнала.
* **`src.utils.file_async`**: Асинхронные функции для работы с файлами.
* **`src.utils.jjson`**: Модуль для работы с JSON.
* **`src.utils.convertors.csv`**: Модуль для работы с CSV.
* **`src.utils.file`**: Функции для работы с файлами.
* **`src.utils.printer`**: Функция для удобной печати объектов.
* **`src.suppliers.aliexpress.utils.extract_product_id`**: Функция для извлечения ID товаров.
* **`src.suppliers.aliexpress.affiliated_products_generator`**: Модуль генерации партнерских ссылок.

Этот анализ предоставляет полное понимание функциональности `ali_promo_campaign.py`, его взаимосвязей и потенциальных улучшений.