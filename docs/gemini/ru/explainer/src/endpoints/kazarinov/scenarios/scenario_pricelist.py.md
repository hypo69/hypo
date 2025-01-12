## <алгоритм>

1. **Инициализация `MexironBuilder`**:
   - Загружается конфигурация из `kazarinov.json`.
   - Устанавливается метка времени (`timestamp`) для уникальности.
   - Определяется путь для экспорта данных (`export_path`). Путь зависит от настройки `storage` в конфиге (может быть `external_storage`, `data` или `goog`).
   - Загружается системная инструкция для AI-модели из файла `system_instruction_mexiron.md`.
   - Инициализируется AI-модель `GoogleGenerativeAI` с ключом API, системными инструкциями и конфигурацией.

2. **`run_scenario`**:
   - Принимает список URL-адресов (`urls`), цену (`price`), имя мехирона (`mexiron_name`) и объекты `update` и `context` от Telegram.
   - Итерирует по каждому URL-адресу в списке:
     - Определяет грабер (`graber`) на основе URL-адреса поставщика (Morlevi, KSP, Grandadvance, Ivory).
     - Если грабер не найден, пропускает URL.
     - Вызывает `graber.grab_page()` для извлечения данных о товаре, используя необходимые поля: `id_product`, `name`, `description_short`, `description`, `specification`, `local_image_path`.
     - Конвертирует полученные данные товара с помощью `convert_product_fields` в словарь.
     - Сохраняет данные товара с помощью `save_product_data`.
     - Добавляет обработанные данные товара в `products_list`.
   - После сбора данных для всех URL, переходит к AI-обработке:
     - Итерирует по языкам (`langs_list` - `he`, `ru`).
     - Вызывает `process_ai` для обработки списка товаров с использованием AI-модели, получая переводы.
     - Добавляет цену и валюту в полученный словарь с переводами.
     - Сохраняет результат AI-обработки в JSON-файл.
     - Создает HTML и PDF отчеты (`create_report`), отправляя их в Telegram.

3.  **`get_graber_by_supplier_url`**:
    - Получает URL.
    - Определяет, какой грабер (`MorleviGraber`, `KspGraber`, `GrandadvanceGraber`, `IvoryGraber`) использовать на основе начальной части URL.
    - Возвращает экземпляр соответствующего грабера или `None`, если грабер не найден.

4.  **`convert_product_fields`**:
    - Принимает объект `ProductFields` как аргумент.
    - Извлекает необходимые данные из полей объекта.
    - Форматирует данные в словарь и возвращает его.
        - Извлекает название продукта (`product_title`).
        - Извлекает идентификатор продукта (`product_id`).
        - Извлекает краткое описание (`description_short`).
        - Извлекает полное описание (`description`).
        - Извлекает спецификацию (`specification`).
        - Извлекает путь к локальному изображению (`local_image_path`).
    - Заменяет символы кавычек и переноса строки, чтобы избежать ошибок при парсинге.

5. **`save_product_data`**:
   - Принимает словарь с данными о продукте.
   - Формирует путь к файлу для сохранения JSON-данных.
   - Сохраняет данные товара в формате JSON в файл.

6.  **`process_ai`**:
    - Принимает список словарей с данными о товарах и язык.
    - Загружает инструкцию для модели из файла (`command_instruction_mexiron_{lang}.md`).
    - Отправляет запрос в модель `gemini` с инструкцией и списком товаров.
    - Обрабатывает полученный ответ от AI-модели.
    - Если ответ не получен или не может быть спарсен, повторно вызывает себя (до `attempts` раз).
    - Возвращает результат в виде словаря с переводом.

7. **`post_facebook`**:
   - Выполняет сценарий публикации в Facebook, используя данные `mexiron` .
   - Открывает страницу профиля Facebook.
   - Формирует заголовок сообщения из названия, описания и цены мехирона.
   - Публикует заголовок и медиа через функции `post_message_title`, `upload_post_media`, `message_publish`.
   - Возвращает `True`, если публикация прошла успешно.

8.  **`create_report`**:
    - Принимает данные для отчёта, язык, пути для сохранения HTML и PDF файлов.
    - Инициализирует `ReportGenerator` для создания отчета.
    - Вызывает `generator.create_report` для создания HTML и PDF файлов.
    - Отправляет PDF файл боту, если файл успешно создан и существует.

## <mermaid>

```mermaid
flowchart TD
    Start[Start MexironBuilder] --> Init[Initialize MexironBuilder]
    Init --> LoadConfig{Load Config: kazarinov.json}
    LoadConfig -- Success --> SetTimestamp[Set Timestamp]
    LoadConfig -- Error --> ErrorConfig[Error loading configuration]
    SetTimestamp --> DetermineExportPath{Determine Export Path}
    DetermineExportPath -- Success --> LoadSystemInstruction[Load System Instruction: system_instruction_mexiron.md]
    DetermineExportPath -- Error --> ErrorPath[Error constructing export path]
    LoadSystemInstruction -- Success --> InitAI[Initialize GoogleGenerativeAI]
    LoadSystemInstruction -- Error --> ErrorInstruction[Error loading instructions or API key]
     InitAI --> RunScenario[Run Scenario]

    RunScenario --> LoopURLs{Loop through URLs}
    LoopURLs -- For each URL --> GetGraber{Get Graber by URL}
    GetGraber -- Graber found --> GrabPage{Grab Product Page}
    GetGraber -- No graber --> SkipURL[Skip URL]
     GrabPage -- Success --> ConvertProductData{Convert Product Fields}
      GrabPage -- Error --> ErrorGrab[Error getting product fields]
    ConvertProductData -- Success --> SaveProductData{Save Product Data}
    ConvertProductData -- Error --> SkipProductData[Skip product data]
    SaveProductData -- Success --> AddToProductList[Add product to list]
    SaveProductData -- Error --> ErrorSave[Error saving product data]
    AddToProductList --> LoopURLs
    LoopURLs -- All URLs processed --> AIPorcessing[AI Processing]
    SkipURL --> LoopURLs
    SkipProductData --> LoopURLs
    ErrorGrab --> LoopURLs
     ErrorSave --> LoopURLs

    AIPorcessing --> LoopLangs{Loop through languages (he, ru)}
    LoopLangs -- For each language --> ProcessAI{Process with AI model}
    ProcessAI -- Success --> AddPriceCurrency[Add Price and Currency]
    ProcessAI -- Error --> ErrorModel[Error AI model]
    AddPriceCurrency --> SaveJSON[Save JSON data]
     SaveJSON -- Success --> CreateReport{Create HTML and PDF report}
      SaveJSON -- Error --> ErrorJSON[Error JSON saving]
    CreateReport -- Success --> ReportSuccess[Report Created successfully]
    CreateReport -- Error --> ErrorReport[Error creating report]
    ReportSuccess --> LoopLangs
    ErrorModel --> LoopLangs
    ErrorReport --> LoopLangs
    ErrorJSON --> LoopLangs

    LoopLangs -- All languages processed --> End[End Scenario]
    ErrorConfig --> End
    ErrorPath --> End
    ErrorInstruction --> End

    subgraph "Header Import"
        HeaderStart[Start] --> Header[<code>header.py</code><br> Determine Project Root]
        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    end

    
   
    
  
    
    
    
   
   
```
### Описание зависимостей `mermaid`

1. **Start**: Начало сценария `MexironBuilder`.
2.  **Init**: Инициализация экземпляра класса `MexironBuilder` и его свойств.
3. **LoadConfig**: Загрузка конфигурации из файла `kazarinov.json`.
4. **SetTimestamp**: Установка временной метки для уникальности процесса.
5.  **DetermineExportPath**: Определение пути для экспорта данных на основе конфигурации.
6. **LoadSystemInstruction**: Загрузка системной инструкции для AI-модели из файла `system_instruction_mexiron.md`.
7.  **InitAI**: Инициализация AI-модели `GoogleGenerativeAI`.
8. **RunScenario**: Запуск основного сценария обработки данных.
9.  **LoopURLs**: Цикл обработки списка URL-адресов.
10. **GetGraber**: Получение соответствующего грабера для URL поставщика.
11. **GrabPage**: Извлечение данных со страницы товара с помощью грабера.
12. **ConvertProductData**: Преобразование полученных данных товара в словарь.
13. **SaveProductData**: Сохранение данных о товаре в JSON-файл.
14. **AddToProductList**: Добавление обработанных данных товара в общий список.
15. **AIPorcessing**: AI-обработка собранных данных.
16. **LoopLangs**: Цикл обработки данных для каждого языка.
17. **ProcessAI**: Обработка списка товаров с использованием AI-модели.
18. **AddPriceCurrency**: Добавление цены и валюты к данным после AI-обработки.
19. **SaveJSON**: Сохранение данных в JSON-файл.
20. **CreateReport**: Создание HTML и PDF отчётов.
21. **End**: Завершение сценария.
22. **SkipURL**: Пропуск URL, если для него нет грабера.
23. **SkipProductData**: Пропуск данных товара, если не удалось конвертировать.
24. **ErrorConfig**: Ошибка при загрузке файла конфигурации.
25. **ErrorPath**: Ошибка при определении пути экспорта.
26. **ErrorInstruction**: Ошибка при загрузке системных инструкций.
27.  **ErrorGrab**: Ошибка при получении данных о товаре.
28.  **ErrorSave**: Ошибка при сохранении данных товара.
29.  **ErrorModel**: Ошибка при обработке AI моделью.
30.  **ErrorJSON**: Ошибка при сохранении данных в JSON файл.
31.  **ErrorReport**: Ошибка при создании HTML и PDF отчетов.
32.  **ReportSuccess**: Успешное создание отчета.

**Вспомогательная `mermaid` диаграмма `header.py`:**
-  **HeaderStart**: Начало процесса импорта `header.py`.
-  **Header**: Определение корневой директории проекта.
-  **import**: Импорт глобальных настроек проекта из `src.gs`.

## <объяснение>

### Импорты

-   `asyncio`: Для асинхронного программирования.
-   `random`: Для генерации случайных чисел (не используется напрямую, возможно, используется в других частях проекта).
-   `shutil`: Для работы с файловой системой (не используется напрямую, возможно, используется в других частях проекта).
-   `pathlib.Path`: Для работы с путями файлов и директорий.
-   `typing.Optional, typing.List`: Для аннотации типов (указание необязательных и списочных параметров).
-   `types.SimpleNamespace`: Для создания простых объектов с атрибутами.
-   `dataclasses.field`: Для задания значения по умолчанию для атрибутов в классах данных.
-   `header`: Локальный модуль, вероятно, для определения корня проекта и импорта глобальных настроек.
-   `src.gs`: Глобальные настройки проекта.
-   `src.endpoints.prestashop.product_fields.ProductFields`: Класс для работы с полями товара PrestaShop.
    -   `src.webdriver.playwright.Playwrid`: Класс для управления браузером через Playwright.
-   `src.ai.gemini.GoogleGenerativeAI`: Класс для работы с AI-моделью Google Gemini.
-   `src.endpoints.advertisement.facebook.scenarios.*`: Функции для работы с Facebook API (публикация постов).
-   `src.suppliers.*.graber.Graber`: Классы для парсинга страниц товаров разных поставщиков (Morlevi, KSP, Ivory, Grandadvance).
-   `src.endpoints.kazarinov.pricelist_generator.ReportGenerator`: Класс для генерации отчётов.
-   `telegram.Update, telegram.ext.CallbackContext`: Типы данных для Telegram Bot API.
-   `src.utils.jjson.*`: Функции для работы с JSON.
-   `src.utils.file.*`: Функции для работы с файлами.
-   `src.utils.image.*`: Функции для работы с изображениями.
-   `src.utils.convertors.unicode.decode_unicode_escape`: Функция для декодирования unicode escape последовательностей.
-   `src.utils.printer.pprint`: Функция для красивого вывода данных.
-   `src.logger.logger.logger`: Объект логгера.

### Классы

-   **`MexironBuilder`**:
    -   **Назначение**: Обрабатывает извлечение, разбор и сохранение данных о продуктах от разных поставщиков.
    -   **Атрибуты**:
        -   `driver (Playwrid)`: Экземпляр `Playwrid` для управления браузером.
        -   `export_path (Path)`: Путь к каталогу для экспорта данных.
        -   `mexiron_name (str)`: Имя мехирона.
        -   `price (float)`: Цена.
        -   `timestamp (str)`: Временная метка для уникальности.
        -   `products_list (List[dict])`: Список обработанных данных о товарах.
        -   `model (GoogleGenerativeAI)`: Экземпляр AI-модели.
        -   `config (SimpleNamespace)`: Конфигурация.
        -   `translations (SimpleNamespace)`: Переводы для мехирона.
        -   `update (Update)`: Объект Telegram Update.
        -   `context (CallbackContext)`: Объект Telegram CallbackContext.
    -   **Методы**:
        -   `__init__(self, mexiron_name: Optional[str] = None)`: Инициализирует класс, загружает конфигурации, устанавливает параметры.
        -   `run_scenario(...)`: Выполняет основной сценарий: сбор данных, AI-обработка, сохранение.
        -   `get_graber_by_supplier_url(self, url: str)`: Определяет грабер на основе URL поставщика.
        -   `convert_product_fields(self, f: ProductFields) -> dict`: Конвертирует поля продукта в словарь.
        -   `save_product_data(self, product_data: dict)`: Сохраняет данные товара в JSON-файл.
        -    `process_ai(self, products_list: List[str], lang:str,  attempts: int = 3) -> tuple | bool`: Обрабатывает список продуктов с помощью AI-модели.
        -   `post_facebook(self, mexiron:SimpleNamespace) -> bool`: Публикует данные на Facebook.
        -   `create_report(self, data: dict, lang:str, html_file: Path, pdf_file: Path) -> bool`: Создает HTML и PDF отчёты.

### Функции

-   **`run_scenario(...)`**:
    -   **Аргументы**:
        -   `update (Update)`: Объект Telegram Update.
        -   `context (CallbackContext)`: Объект Telegram CallbackContext.
        -   `urls (list[str])`: Список URL-адресов поставщиков.
        -   `price (Optional[str])`: Цена.
        -   `mexiron_name (Optional[str])`: Имя мехирона.
    -   **Назначение**: Итерирует по URL, извлекает данные, обрабатывает их с помощью AI, генерирует отчёты.
    -   **Возвращает**: `bool` - `True` при успешном выполнении, `False` в противном случае.
    -   **Пример**:
        ```python
        mexiron_builder = MexironBuilder()
        urls = ["https://ksp.co.il/item/12345", "https://morlevi.co.il/product/67890"]
        await mexiron_builder.run_scenario(update, context, urls, "100", "test_mexiron")
        ```
-   **`get_graber_by_supplier_url(url: str)`**:
    -   **Аргумент**: `url (str)` - URL-адрес поставщика.
    -   **Назначение**: Возвращает экземпляр грабера на основе URL.
    -   **Возвращает**: `Optional[object]` - экземпляр грабера или `None`, если грабер не найден.
    -   **Пример**:
        ```python
        url = "https://www.ksp.co.il/item/12345"
        graber = mexiron_builder.get_graber_by_supplier_url(url)
        if graber:
           await graber.grab_page()
        ```
-   **`convert_product_fields(f: ProductFields)`**:
    -   **Аргумент**: `f (ProductFields)` - объект с данными о продукте.
    -   **Назначение**: Конвертирует объект `ProductFields` в словарь.
    -   **Возвращает**: `dict` - словарь с данными о продукте.
    -   **Пример**:
        ```python
        product_fields = ProductFields(name=[{'language': [{'value': 'Product Name'}]}],
                                      description_short=[{'language': [{'value': 'Short description'}]}],
                                      description=[{'language': [{'value': 'Long description'}]}],
                                      specification=[{'language': [{'value': 'Specification'}]}],
                                      local_image_path='/path/to/image.jpg',
                                      id_product='123')
        product_data = await mexiron_builder.convert_product_fields(product_fields)
        ```
-   **`save_product_data(product_data: dict)`**:
    -   **Аргумент**: `product_data (dict)` - словарь с данными о продукте.
    -   **Назначение**: Сохраняет данные товара в JSON-файл.
    -   **Возвращает**: `bool` - `True` при успешном сохранении, `None` в противном случае.
    -   **Пример**:
        ```python
        product_data = {"product_id": "123", "name": "Test Product"}
        await mexiron_builder.save_product_data(product_data)
        ```
-   **`process_ai(products_list: List[str], lang:str,  attempts: int = 3)`**:
    -   **Аргументы**:
        -   `products_list (List[str])`: Список данных о товарах в виде строк.
        -   `lang (str)`: Язык, для которого нужно получить перевод.
        -   `attempts (int)`: Количество попыток, для запроса к модели.
    -   **Назначение**: Запрашивает у AI-модели перевод на указанный язык.
    -   **Возвращает**: `dict` - словарь с переводами.
    -   **Пример**:
         ```python
        products_list = [{"product_id": "123", "name": "Test Product",  "description":"test description"}]
        await mexiron_builder.process_ai(products_list, 'he')
        ```

- **`post_facebook(mexiron: SimpleNamespace)`**:
   -   **Аргументы**: `mexiron (SimpleNamespace)` - Объект с данными для публикации на Facebook.
   -   **Назначение**: Публикует данные на Facebook.
   -   **Возвращает**: `bool` - `True`, если публикация прошла успешно, `None` в противном случае.
   -  **Пример:**
        ```python
        mexiron_data = SimpleNamespace(
                title="Заголовок",
                description="Описание",
                price="100",
                products=["path_to_img1", "path_to_img2"]
        )
       await mexiron_builder.post_facebook(mexiron_data)
        ```

-   **`create_report(data: dict, lang:str, html_file: Path, pdf_file: Path)`**:
    -   **Аргументы**:
        -   `data (dict)`: Данные для отчёта.
        -   `lang (str)`: Язык отчёта.
        -   `html_file (Path)`: Путь к HTML файлу.
        -   `pdf_file (Path)`: Путь к PDF файлу.
    -   **Назначение**: Создаёт HTML и PDF отчёты, отправляет PDF боту.
    -   **Возвращает**: `bool` - `True` при успешном создании, `None` в противном случае.
    -   **Пример**:
        ```python
        report_data = {"product_id": "123", "name": "Test Product", "price":"100"}
        html_file = Path("/path/to/report.html")
        pdf_file = Path("/path/to/report.pdf")
        await mexiron_builder.create_report(report_data, "ru", html_file, pdf_file)
        ```

### Переменные

-   `required_fields (tuple)`: Кортеж с именами обязательных полей товара.
-   `langs_list (list)`: Список языков для AI-обработки.

### Потенциальные ошибки и области для улучшения

1.  **Обработка ошибок**: В коде есть блоки `try-except`, но обработка ошибок может быть улучшена, например, добавление логирования ошибок и возврата более информативных значений.
2.  **AI-модель**: Модель может возвращать невалидный результат. Предусмотрен механизм повторного запроса, но его можно улучшить, возможно, добавив анализ ответа или более сложные условия повторных попыток.
3.  **Зависимости**: Код сильно зависит от внешних модулей и сервисов (Google Gemini, Facebook API, Telegram Bot API), что делает его менее гибким и более уязвимым к изменениям в этих сервисах.
4.  **Логирование**: В коде используются `logger.debug` и `logger.error`, но можно расширить логирование, чтобы отслеживать больше этапов процесса.
5.  **Отсутствие проверок**: Не все функции проверяют входные данные на корректность.
6.  **Жестко заданные пути**: Пути к файлам конфигурации, инструкциям и т.д. прописаны "жестко". Лучше использовать относительные пути и переменные окружения.
7.  **Ошибки при парсинге**: При ошибке парсинга данных, функция просто пропускает товар, не информируя об этом.
8.  **Сложная логика в `run_scenario`**: Функция содержит много логики, что затрудняет ее отладку и модификацию.
9.  **Зависимость от `self.driver`**:  `MexironBuilder` имеет зависимость от `self.driver` в `get_graber_by_supplier_url`, хотя `driver` используется только для перехода по url.
10. **Проблема с кодировкой** Местами используется `encoding='UTF-8'`, но не везде. Нужно убедиться что кодировка везде унифицирована.

### Цепочка взаимосвязей с другими частями проекта
-  **`header`**: определяет корень проекта и импортирует глобальные настройки (`gs`).
-  **`src.gs`**: Глобальные настройки проекта, которые используются для получения путей к файлам, ключей API и т.д.
-  **`src.endpoints.prestashop.product_fields.ProductFields`**: Структура данных для представления полей товара.
-  **`src.webdriver.playwright.Playwrid`**: Управляет браузером для парсинга веб-страниц.
-  **`src.ai.gemini.GoogleGenerativeAI`**: Обрабатывает текстовые данные с помощью AI.
-  **`src.endpoints.advertisement.facebook.scenarios.*`**: Взаимодействует с Facebook API для публикации постов.
-  **`src.suppliers.*.graber.Graber`**: Извлекает данные о товарах с сайтов поставщиков.
-  **`src.endpoints.kazarinov.pricelist_generator.ReportGenerator`**: Генерирует HTML и PDF отчёты.
-  **`telegram.Update, telegram.ext.CallbackContext`**: Используется для обработки сообщений в Telegram.
-  **`src.utils.jjson.*`**: Сериализует и десериализует данные в JSON.
-  **`src.utils.file.*`**: Читает и сохраняет данные в файлы.
-  **`src.utils.image.*`**: Загружает и сохраняет изображения.
-  **`src.utils.convertors.unicode.decode_unicode_escape`**: Декодирует unicode escape последовательности.
- **`src.utils.printer.pprint`**: Выводит данные в удобном формате.
-   **`src.logger.logger.logger`**: Ведет логирование работы скрипта.