## АНАЛИЗ JSON ФАЙЛА

### <алгоритм>

1.  **Чтение файла:** Загружается JSON файл `6pm.json`.
2.  **Анализ структуры JSON:**
    *   Извлекается значение ключа `supplier` (строка, `"6pm"`).
    *   Извлекается значение ключа `supplier_prefix` (строка, `"6pm"`).
    *   Извлекается значение ключа `start_url` (строка, `"https://www.6pm.com/"`).
    *   Извлекается значение ключа `price_rule` (строка, `"+0"`).
    *   Извлекается значение ключа `if_login` (логическое значение, `false`).
    *   Извлекается значение ключа `collect_products_from_categorypage` (логическое значение, `false`).
    *    Извлекается значение ключа `root_category` (число, `3`).
    *   Извлекается значение ключа `scenario_files` (массив строк, `[".json", "ksp_categories_wathces_apple.json"]`).
    *   Извлекается значение ключа `excluded` (массив строк, содержит имена файлов, которые нужно исключить из обработки).
    *   Извлекается значение ключа `last_runned_scenario` (пустая строка, `""`).
3.  **Использование данных:**
    *   Значение `supplier` используется для идентификации поставщика.
    *   Значение `supplier_prefix` может использоваться для формирования идентификаторов товаров или файлов.
    *   Значение `start_url` используется как начальная точка для парсинга сайта.
    *   Значение `price_rule` используется для корректировки цен.
    *   Значение `if_login` определяет, требуется ли авторизация на сайте.
    *   Значение `collect_products_from_categorypage` определяет, нужно ли собирать товары со страниц категорий.
    *   Значение `root_category` определяет корневую категорию для парсинга.
    *   Значение `scenario_files` определяет список дополнительных файлов сценариев для обработки.
    *   Значение `excluded` определяет список исключаемых файлов сценариев.
    *  Значение `last_runned_scenario` хранит имя последнего запущенного сценария (здесь оно пусто).
4.  **Примеры:**
    *   `supplier`: `"6pm"` - Имя поставщика, используется для идентификации сайта.
    *   `start_url`: `"https://www.6pm.com/"` - URL, с которого начинается парсинг сайта.
    *   `price_rule`: `"+0"` - Правило для корректировки цены (в данном случае без изменения).
    *   `excluded`: `["ksp_categories_speakers_google.json", "ksp_categories_speakers_jbl.json", ...]` - Список файлов, которые не должны быть обработаны.

### <mermaid>

```mermaid
flowchart TD
    Start --> LoadJsonFile[Load 6pm.json file]
    LoadJsonFile --> ParseJson[Parse JSON Structure]
    ParseJson --> ExtractSupplier[Extract Supplier: "6pm"]
    ParseJson --> ExtractSupplierPrefix[Extract Supplier Prefix: "6pm"]
    ParseJson --> ExtractStartUrl[Extract Start URL: "https://www.6pm.com/"]
    ParseJson --> ExtractPriceRule[Extract Price Rule: "+0"]
    ParseJson --> ExtractIfLogin[Extract if_login: false]
    ParseJson --> ExtractCollectFromCategoryPage[Extract collect_products_from_categorypage: false]
    ParseJson --> ExtractRootCategory[Extract root_category: 3]
    ParseJson --> ExtractScenarioFiles[Extract Scenario Files: ['.json', 'ksp_categories_wathces_apple.json']]
    ParseJson --> ExtractExcludedFiles[Extract Excluded Files: [...]]
     ParseJson --> ExtractLastRunnedScenario[Extract Last Runned Scenario: ""]
    
    
    ExtractSupplier --> UseSupplierData[Use Supplier Data]
    ExtractSupplierPrefix --> UseSupplierPrefixData[Use Supplier Prefix Data]
    ExtractStartUrl --> UseStartUrl[Use Start URL for Parsing]
    ExtractPriceRule --> UsePriceRule[Use Price Rule for Calculation]
    ExtractIfLogin --> UseIfLogin[Use If Login Flag]
    ExtractCollectFromCategoryPage --> UseCollectFromCategoryPage[Use Collect From Category Flag]
     ExtractRootCategory --> UseRootCategory[Use Root Category Number]
    ExtractScenarioFiles --> UseScenarioFiles[Use List of Scenario Files]
     ExtractExcludedFiles --> UseExcludedFiles[Use List of Excluded Files]
      ExtractLastRunnedScenario --> UseLastRunnedScenario[Use Last Runned Scenario]
     
    UseSupplierData --> End
    UseSupplierPrefixData --> End
    UseStartUrl --> End
    UsePriceRule --> End
     UseIfLogin --> End
     UseCollectFromCategoryPage --> End
     UseRootCategory --> End
    UseScenarioFiles --> End
    UseExcludedFiles --> End
    UseLastRunnedScenario --> End

    End[End]
```

**Зависимости:**

*   Нет явных импортов, так как это JSON файл, а не код Python. Диаграмма представляет собой поток данных, основанный на структуре JSON.

### <объяснение>

**Общая структура:**

Файл `6pm.json` представляет собой конфигурационный файл в формате JSON, который содержит настройки для парсинга веб-сайта 6pm. Он определяет, как именно будет выполняться сбор данных, какие категории будут проанализированы, и какие файлы сценариев будут задействованы или исключены.

**Элементы JSON:**

*   **`supplier`**:
    *   **Тип**: Строка
    *   **Назначение**: Идентификатор поставщика, в данном случае "6pm".
    *   **Пример**: `"6pm"`
*   **`supplier_prefix`**:
    *   **Тип**: Строка
    *   **Назначение**: Префикс поставщика, может использоваться при формировании имен файлов или идентификаторов.
    *   **Пример**: `"6pm"`
*   **`start_url`**:
    *   **Тип**: Строка
    *   **Назначение**: URL начальной страницы, с которой начинается процесс парсинга.
    *   **Пример**: `"https://www.6pm.com/"`
*   **`price_rule`**:
    *   **Тип**: Строка
    *   **Назначение**: Правило изменения цены. Здесь "+0" означает отсутствие изменения цены.
    *   **Пример**: `"+0"`
*   **`if_login`**:
    *   **Тип**: Булево значение
    *   **Назначение**: Указывает, требуется ли авторизация на сайте. `false` означает, что авторизация не требуется.
    *   **Пример**: `false`
*   **`collect_products_from_categorypage`**:
    *   **Тип**: Булево значение
    *   **Назначение**: Определяет, нужно ли собирать товары непосредственно со страниц категорий. `false` означает, что нет.
    *   **Пример**: `false`
* **`root_category`**:
    *   **Тип**: Число
    *   **Назначение**: Идентификатор корневой категории.
    *   **Пример**: `3`

*   **`scenario_files`**:
    *   **Тип**: Массив строк
    *   **Назначение**: Список файлов сценариев, которые нужно использовать для парсинга.
    *   **Пример**: `[".json", "ksp_categories_wathces_apple.json"]`
*   **`excluded`**:
    *   **Тип**: Массив строк
    *   **Назначение**: Список файлов сценариев, которые нужно исключить из процесса парсинга.
    *   **Пример**: `["ksp_categories_speakers_google.json", "ksp_categories_speakers_jbl.json", ...]`
*   **`last_runned_scenario`**:
    *   **Тип**: Строка
    *   **Назначение**: Имя последнего запущенного сценария. В данном случае, строка пуста.
    *   **Пример**: `""`

**Взаимосвязи с другими частями проекта:**

*   Этот файл является частью системы парсинга и используется как конфигурация для конкретного поставщика (`6pm`). Он определяет, как именно будет работать процесс парсинга для данного сайта.
*   Данные, указанные в этом файле, влияют на работу других частей проекта: сбор данных, обработку цен, и т.д. Исключаемые файлы (`excluded`) не будут участвовать в процессе сбора данных.

**Потенциальные области для улучшения:**

*   **Структурирование `excluded`**: Список `excluded` является очень большим, что может усложнить чтение и сопровождение файла. Возможно стоит пересмотреть структуру исключений или перенести их в отдельный файл.
*   **Цена и правила**: `price_rule` может быть более гибким (например, с поддержкой процентов, а не только фиксированной суммы).

**Заключение:**

Файл `6pm.json` является ключевым для настройки процесса парсинга сайта 6pm. Он определяет основные параметры, такие как URL, правила обработки, список файлов сценариев, и исключения. Понимание структуры этого файла важно для сопровождения и настройки системы парсинга.