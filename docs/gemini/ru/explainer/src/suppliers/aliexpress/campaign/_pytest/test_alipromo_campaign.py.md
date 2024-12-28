## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:  

1. **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.  
2. **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости, 
    которые импортируются при создании диаграммы. 
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`, 
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!  
    
    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
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

1. **Настройка Fixture `campaign`**:
   - Создается экземпляр `AliPromoCampaign` с заданными `campaign_name`, `category_name`, `language`, и `currency`.
   - Пример: `AliPromoCampaign("test_campaign", "test_category", "EN", "USD")`.
   - Этот экземпляр `campaign` используется в каждом тесте для взаимодействия.

2. **Тестирование `test_initialize_campaign`**:
   - Мокируется функция `j_loads_ns`, чтобы вернуть `SimpleNamespace` с данными кампании.
   - Вызывается `campaign.initialize_campaign()`, которая загружает данные кампании.
   - Проверяется, что `campaign.campaign.name` и `campaign.campaign.category.test_category.name` правильно инициализированы.

3. **Тестирование `test_get_category_products_no_json_files`**:
   - Мокируется `get_filenames`, чтобы вернуть пустой список (нет JSON-файлов).
   - Мокируется `fetch_product_data`, чтобы вернуть пустой список (нет данных продукта).
   - Вызывается `campaign.get_category_products(force=True)`.
   - Проверяется, что возвращаемый список продуктов пуст.

4. **Тестирование `test_get_category_products_with_json_files`**:
   - Мокируется `get_filenames`, чтобы вернуть список с именем JSON-файла ("product_123.json").
   - Мокируется `j_loads_ns`, чтобы вернуть `SimpleNamespace` с данными продукта (например, `product_id="123"`).
   - Вызывается `campaign.get_category_products()`.
   - Проверяется, что возвращаемый список содержит один продукт с корректными данными.

5. **Тестирование `test_create_product_namespace`**:
   - Создается словарь `product_data` с данными продукта.
   - Вызывается `campaign.create_product_namespace(**product_data)`.
   - Проверяется, что возвращенный `SimpleNamespace` содержит данные продукта.

6. **Тестирование `test_create_category_namespace`**:
   - Создается словарь `category_data` с данными категории.
   - Вызывается `campaign.create_category_namespace(**category_data)`.
   - Проверяется, что возвращенный `SimpleNamespace` содержит данные категории.

7. **Тестирование `test_create_campaign_namespace`**:
   - Создается словарь `campaign_data` с данными кампании.
   - Вызывается `campaign.create_campaign_namespace(**campaign_data)`.
   - Проверяется, что возвращенный `SimpleNamespace` содержит данные кампании.

8. **Тестирование `test_prepare_products`**:
    - Мокируется метод `get_prepared_products` для возврата пустого списка.
    - Мокируется метод `read_text_file` для возврата "source_data".
    - Мокируется метод `get_filenames` для возврата списка с именем HTML-файла ("source.html").
    - Мокируется метод `process_affiliate_products`.
    - Вызывается `campaign.prepare_products()`.
    - Проверяется, что метод `process_affiliate_products` был вызван один раз.

9. **Тестирование `test_fetch_product_data`**:
   - Создается список `product_ids`.
   - Мокируется метод `process_affiliate_products` для возврата списка `SimpleNamespace` с данными продуктов.
   - Вызывается `campaign.fetch_product_data(product_ids)`.
   - Проверяется, что возвращаемый список содержит продукты с корректными `product_id`.

10. **Тестирование `test_save_product`**:
    - Создается объект `SimpleNamespace` с данными продукта.
    - Мокируется метод `j_dumps` для возврата "{}".
    - Мокируется метод `Path.write_text`.
    - Вызывается `campaign.save_product(product)`.
    - Проверяется, что метод `Path.write_text` был вызван один раз с правильными аргументами.

11. **Тестирование `test_list_campaign_products`**:
    - Создаются два объекта `SimpleNamespace` с `product_title`.
    - `products` устанавливается как атрибут `campaign.category`.
    - Вызывается `campaign.list_campaign_products()`.
    - Проверяется, что возвращаемый список содержит названия продуктов.

## <mermaid>

```mermaid
flowchart TD
    subgraph Fixture `campaign`
        CampaignFixture[Create AliPromoCampaign Instance]
    end

    subgraph Test `test_initialize_campaign`
        T1_Start[Start] --> T1_Mock_j_loads_ns[Mock `j_loads_ns` with campaign data]
        T1_Mock_j_loads_ns --> T1_Initialize[Call `campaign.initialize_campaign()`]
        T1_Initialize --> T1_Assert[Assert initialized data]
        T1_Assert --> T1_End[End]
    end

    subgraph Test `test_get_category_products_no_json_files`
        T2_Start[Start] --> T2_Mock_get_filenames[Mock `get_filenames` to return empty list]
        T2_Mock_get_filenames --> T2_Mock_fetch_product_data[Mock `fetch_product_data` to return empty list]
        T2_Mock_fetch_product_data --> T2_GetProducts[Call `campaign.get_category_products(force=True)`]
        T2_GetProducts --> T2_Assert[Assert empty product list]
        T2_Assert --> T2_End[End]
    end

    subgraph Test `test_get_category_products_with_json_files`
        T3_Start[Start] --> T3_Mock_get_filenames[Mock `get_filenames` with JSON file]
        T3_Mock_get_filenames --> T3_Mock_j_loads_ns[Mock `j_loads_ns` with product data]
        T3_Mock_j_loads_ns --> T3_GetProducts[Call `campaign.get_category_products()`]
        T3_GetProducts --> T3_Assert[Assert product data]
        T3_Assert --> T3_End[End]
    end

    subgraph Test `test_create_product_namespace`
        T4_Start[Start] --> T4_CreateProductData[Create product_data dictionary]
        T4_CreateProductData --> T4_CreateNamespace[Call `campaign.create_product_namespace(**product_data)`]
        T4_CreateNamespace --> T4_Assert[Assert product namespace]
        T4_Assert --> T4_End[End]
    end

    subgraph Test `test_create_category_namespace`
        T5_Start[Start] --> T5_CreateCategoryData[Create category_data dictionary]
        T5_CreateCategoryData --> T5_CreateNamespace[Call `campaign.create_category_namespace(**category_data)`]
        T5_CreateNamespace --> T5_Assert[Assert category namespace]
        T5_Assert --> T5_End[End]
    end

    subgraph Test `test_create_campaign_namespace`
        T6_Start[Start] --> T6_CreateCampaignData[Create campaign_data dictionary]
        T6_CreateCampaignData --> T6_CreateNamespace[Call `campaign.create_campaign_namespace(**campaign_data)`]
        T6_CreateNamespace --> T6_Assert[Assert campaign namespace]
        T6_Assert --> T6_End[End]
    end

   subgraph Test `test_prepare_products`
        T7_Start[Start] --> T7_Mock_get_prepared_products[Mock `get_prepared_products`]
        T7_Mock_get_prepared_products --> T7_Mock_read_text_file[Mock `read_text_file`]
        T7_Mock_read_text_file --> T7_Mock_get_filenames[Mock `get_filenames`]
        T7_Mock_get_filenames --> T7_Mock_process_affiliate_products[Mock `process_affiliate_products`]
        T7_Mock_process_affiliate_products --> T7_PrepareProducts[Call `campaign.prepare_products()`]
        T7_PrepareProducts --> T7_Assert[Assert `process_affiliate_products` called]
        T7_Assert --> T7_End[End]
   end
   
    subgraph Test `test_fetch_product_data`
        T8_Start[Start] --> T8_CreateProductIDs[Create product_ids list]
        T8_CreateProductIDs --> T8_Mock_process_affiliate_products[Mock `process_affiliate_products` with product data]
        T8_Mock_process_affiliate_products --> T8_FetchData[Call `campaign.fetch_product_data(product_ids)`]
        T8_FetchData --> T8_Assert[Assert fetched product data]
        T8_Assert --> T8_End[End]
    end
    
    subgraph Test `test_save_product`
        T9_Start[Start] --> T9_CreateProduct[Create SimpleNamespace product object]
        T9_CreateProduct --> T9_Mock_j_dumps[Mock `j_dumps`]
        T9_Mock_j_dumps --> T9_Mock_Path_write_text[Mock `Path.write_text`]
        T9_Mock_Path_write_text --> T9_SaveProduct[Call `campaign.save_product(product)`]
         T9_SaveProduct --> T9_Assert[Assert `Path.write_text` was called with correct args]
         T9_Assert --> T9_End[End]
    end

   subgraph Test `test_list_campaign_products`
        T10_Start[Start] --> T10_CreateProducts[Create SimpleNamespace product objects]
        T10_CreateProducts --> T10_SetCategoryProducts[Set `campaign.category.products`]
        T10_SetCategoryProducts --> T10_ListProducts[Call `campaign.list_campaign_products()`]
        T10_ListProducts --> T10_Assert[Assert product titles are correct]
        T10_Assert --> T10_End[End]
    end
   
    CampaignFixture --> T1_Start
    CampaignFixture --> T2_Start
    CampaignFixture --> T3_Start
    CampaignFixture --> T4_Start
    CampaignFixture --> T5_Start
    CampaignFixture --> T6_Start
    CampaignFixture --> T7_Start
    CampaignFixture --> T8_Start
    CampaignFixture --> T9_Start
    CampaignFixture --> T10_Start
```

**Импорты:**

- `pytest`: Фреймворк для тестирования в Python.
- `pathlib.Path`: Для работы с путями файлов.
- `types.SimpleNamespace`: Для создания простых объектов с атрибутами.
- `src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign`: Класс для управления кампаниями AliExpress.
- `src.utils.jjson.j_dumps, src.utils.jjson.j_loads_ns`: Функции для работы с JSON.
- `src.utils.file.save_text_file`: Функция для сохранения текста в файл.
- `src.utils.file`: Пакет с утилитами для работы с файлами.
- `src.gs`: Глобальные настройки проекта.

**Классы:**

- `AliPromoCampaign`: Основной класс для управления кампаниями, используемый для тестирования.

**Функции:**

- `campaign()`: Fixture для создания экземпляра `AliPromoCampaign`.
- `test_initialize_campaign(mocker, campaign)`: Тестирует инициализацию данных кампании.
- `test_get_category_products_no_json_files(mocker, campaign)`: Тестирует получение продуктов категории без JSON-файлов.
- `test_get_category_products_with_json_files(mocker, campaign)`: Тестирует получение продуктов категории с JSON-файлами.
- `test_create_product_namespace(campaign)`: Тестирует создание пространства имен продукта.
- `test_create_category_namespace(campaign)`: Тестирует создание пространства имен категории.
- `test_create_campaign_namespace(campaign)`: Тестирует создание пространства имен кампании.
- `test_prepare_products(mocker, campaign)`: Тестирует подготовку продуктов для кампании.
- `test_fetch_product_data(mocker, campaign)`: Тестирует получение данных о продуктах.
- `test_save_product(mocker, campaign)`: Тестирует сохранение данных продукта.
- `test_list_campaign_products(campaign)`: Тестирует получение списка названий продуктов кампании.

**Переменные:**

- `campaign_name`: Имя тестовой кампании ("test_campaign").
- `category_name`: Имя тестовой категории ("test_category").
- `language`: Язык ("EN").
- `currency`: Валюта ("USD").
- `mock_json_data`, `mock_product_data`: Моковые данные для тестов.

## <объяснение>

**Импорты:**
- `pytest`:  Используется для создания тестовых функций и фикстур, а также для мокирования внешних зависимостей.
- `pathlib`: Предоставляет удобный способ работы с файловыми путями, что особенно важно при тестировании операций с файловой системой.
- `types.SimpleNamespace`:  Используется для создания простых объектов, которые ведут себя как обычные объекты, но атрибуты которых можно устанавливать динамически. Это упрощает создание моковых объектов для тестирования.
- `src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign`: Этот импорт подключает класс `AliPromoCampaign`, который является ключевым компонентом для управления рекламными кампаниями AliExpress. Тесты нацелены на проверку корректности его работы.
- `src.utils.jjson`: Этот модуль, вероятно, содержит функции для работы с JSON данными, такие как сериализация и десериализация объектов. Это позволяет сохранять и загружать данные кампаний и продуктов.
- `src.utils.file`: Содержит функции для операций с файлами, такие как чтение и запись файлов, что необходимо для работы с данными кампаний, хранящимися в файлах.
- `src.gs`: Этот модуль, вероятно, содержит глобальные настройки проекта.

**Классы:**
- `AliPromoCampaign`: Класс, который представляет логику управления рекламной кампанией на AliExpress. Он имеет методы для инициализации кампании, получения продуктов, создания пространств имен для продуктов и кампаний, подготовки данных, сохранения продуктов и получения списка продуктов кампании.

**Функции:**
- `campaign()`: Это фикстура pytest, которая создает экземпляр класса `AliPromoCampaign` перед запуском каждого теста. Это позволяет избежать дублирования кода и обеспечивает единообразие окружения для тестов.
- Функции тестирования (`test_...`): Каждая функция тестирования проверяет конкретный метод или аспект класса `AliPromoCampaign`, используя мокирование для изоляции тестируемого кода и создания необходимых условий для теста.
   - `mocker`: Модуль `pytest-mock`, для замены объектов и методов моками.
   -  `campaign`: Экземпляр `AliPromoCampaign` созданный `fixture`.
- `test_initialize_campaign`: Тестирует метод `initialize_campaign` класса `AliPromoCampaign` который загружает данные кампании.
- `test_get_category_products_no_json_files` и `test_get_category_products_with_json_files`: Проверяют логику получения продуктов из JSON-файлов в различных ситуациях (есть или нет файлы).
- `test_create_product_namespace`, `test_create_category_namespace`, `test_create_campaign_namespace`: Проверяют, что методы создания namespace работают корректно, создавая объекты с ожидаемыми атрибутами.
- `test_prepare_products`: Тестирует метод `prepare_products` который обрабатывает HTML-данные.
- `test_fetch_product_data`: Проверяет получение данных продукта.
- `test_save_product`: Тестирует, как сохраняются данные продукта с использованием JSON.
- `test_list_campaign_products`: Проверяет, что метод правильно формирует список названий продуктов.

**Переменные:**
- `campaign_name`, `category_name`, `language`, `currency`: Глобальные переменные, определяющие настройки кампании. Используются в тестах для создания экземпляров `AliPromoCampaign`.
- `mock_json_data`, `mock_product_data`: Эти переменные содержат данные, которые используются для мокирования поведения внешних функций.

**Потенциальные ошибки и области для улучшения:**
- Тесты хорошо охватывают основные функции `AliPromoCampaign`.
- Мокирование помогает изолировать тесты и проверять логику, не завися от внешних факторов.
- Можно добавить больше тестов для крайних случаев или ошибок.
- Можно добавить больше assert для более точных проверок.
- Можно рассмотреть добавление type hints.

**Взаимосвязи с другими частями проекта:**
- `src.suppliers.aliexpress.campaign.ali_promo_campaign`: Данный модуль зависит от пакетов `src.utils.jjson` и `src.utils.file` для работы с данными и файловой системой, что показывает взаимодействие между компонентами проекта.
- `src.gs`: Этот модуль представляет общие настройки, что указывает на общую конфигурацию для разных частей проекта.