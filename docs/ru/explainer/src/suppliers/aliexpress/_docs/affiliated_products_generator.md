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
```

## Анализ кода `affiliated_products_generator.py`

### 1. <алгоритм>

**Блок-схема:**

```mermaid
graph TD
    A[Начало: `AliAffiliatedProducts.process_affiliate_products(prod_urls)`] --> B{Инициализация: _promotion_links = [], _prod_urls = []};
    B --> C{Преобразование URL: `promotional_prod_urls = ensure_https(prod_urls)`};
    C --> D{Цикл: `for prod_url in promotional_prod_urls`};
    D --> E{Получение аффилиат-ссылки: `_link = super().get_affiliate_links(prod_url)`};
    E -- `_link` не `None` --> F{Проверка атрибута `promotion_link`: `hasattr(_link, 'promotion_link')`};
    F -- Да --> G{Добавление ссылки в `_promotion_links` и `prod_url` в `_prod_urls`};
    G --> H{Вывод в консоль: `pprint(f'found affiliate for: {_link.promotion_link}')`};
    H --> D;
    F -- Нет --> I{Логирование: `logger.info_red(f'Not found affiliate for {prod_url}')`};
    I --> D;
    D -- Конец цикла --> J{Проверка наличия аффилиат-ссылок: `if not _promotion_links`};
    J -- Нет аффилиат-ссылок --> K{Логирование ошибки и выход: `logger.error('No affiliate products returned'); return`};
    J -- Есть аффилиат-ссылки --> L{Логирование начала получения деталей: `logger.info_red('Start receiving product details...')`};
    L --> M{Получение деталей продуктов: `_affiliate_products = self.retrieve_product_details(_prod_urls)`};
    M --> N{Проверка наличия деталей продуктов: `if not _affiliate_products`};
    N -- Нет деталей продуктов --> O{Выход: `return`};
    N -- Есть детали продуктов --> P{Цикл: `for product, promotion_link in zip(_affiliate_products, _promotion_links)`};
    P --> Q{Проверка `promotion_link`: `if not promotion_link`};
    Q -- `promotion_link` не `None` --> R{Обработка `promotion_link`: извлечение `aff_short_key`};
     R --> S{Проверка `aff_short_key`: `if aff_short_key`};
        S -- Да --> T{Обновление `product.promotion_link`: `product.promotion_link = fr'https://s.click.aliexpress.com/e/{aff_short_key}'`};
        T --> U;
        S -- Нет --> V{Удаление продукта: `self.delete_product(product.product_id)`};
        V --> U;
    Q -- `promotion_link` `None` --> W{Запись `promotion_link`: `product.promotion_link = promotion_link`};
    W --> U;
    U --> X{Сохранение изображения: `save_png_from_url(product.product_main_image_url, image_path)`};
    X --> Y{Обновление `product.local_image_path`: `product.local_image_path = str(image_path)`};
    Y --> Z{Проверка наличия видео: `if len(product.product_video_url) > 1`};
    Z -- Видео есть --> AA{Сохранение видео: `save_video_from_url(product.product_video_url, video_path)`};
     AA --> AB{Обновление `product.local_video_path`: `product.local_video_path = str(video_path)`};
     AB --> AC{Логирование: `pprint(f'caught product - {product.product_id}')`};
     AC --> AD{Сохранение `product` в JSON: `j_dumps(product, ...)`};
    AD -- Ошибка при записи JSON --> AE{Логирование предупреждения: `logger.warning(...)`};
    AE --> P;
    Z -- Видео нет --> AC;
     AD -- Успешно записан JSON --> P;
    P -- Конец цикла --> AF{Логирование количества продуктов и возврат: `pprint(f'caught {len(_affiliate_products)}'); return _affiliate_products`};
    K --> AF;
     O --> AF;
```

**Примеры:**

1.  **Инициализация:**
    *   `prod_urls = ['https://aliexpress.com/item/123.html', '456']`
    *   `_promotion_links = []`, `_prod_urls = []`

2.  **Преобразование URL:**
    *   `promotional_prod_urls` становится `['https://aliexpress.com/item/123.html', 'https://aliexpress.com/item/456.html']`

3.  **Цикл по `promotional_prod_urls`:**
    *   Для `prod_url = 'https://aliexpress.com/item/123.html'`:
        *   `_link` получает аффилиат-ссылку.
        *   Если `_link` имеет `promotion_link`, то она добавляется в `_promotion_links`, а `prod_url` в `_prod_urls`.
        *   Выводится сообщение в консоль.
    *   Для `prod_url = 'https://aliexpress.com/item/456.html'`:
        *   Если аффилиат-ссылка не найдена, то сообщение об этом логируется.

4.  **Получение деталей продуктов:**
    *   `_affiliate_products` получается после запроса к API по списку `_prod_urls`.

5.  **Цикл по `_affiliate_products` и `_promotion_links`:**
    *   Для каждого продукта:
        *   Проверяется наличие аффилиат-ссылки.
            *   Если её нет, то формируется короткая ссылка.
            *   Если `aff_short_key` отсутствует, то продукт удаляется.
        *   Сохраняется изображение продукта.
        *   Сохраняется видео продукта (если есть).
        *   Сохраняется JSON с информацией о продукте.

### 2. <mermaid>

```mermaid
flowchart TD
    Start[Start: `AliAffiliatedProducts.process_affiliate_products`]
    
    Init[_promotion_links = [],<br>_prod_urls = []]
    Start --> Init
    
    ConvertURLs[Ensure HTTPS: <br>`ensure_https(prod_urls)`]
     Init --> ConvertURLs
    
    LoopURLs[Loop through<br> `promotional_prod_urls`]
    ConvertURLs --> LoopURLs
    
    GetAffiliateLink[Get Affiliate Link:<br> `super().get_affiliate_links(prod_url)`]
    LoopURLs --> GetAffiliateLink
     
    CheckAffiliateLink{Affiliate Link Exists?}
     GetAffiliateLink --> CheckAffiliateLink
     
     YesAffiliateLink[Add Link and URL<br> to Lists]
     CheckAffiliateLink -- Yes --> YesAffiliateLink
    
     LogAffiliateLinkFound[Print:<br>Affiliate Found]
     YesAffiliateLink --> LogAffiliateLinkFound
      
     LogAffiliateLinkFound --> LoopURLs
    
     NoAffiliateLink[Log: <br> Affiliate Not Found]
    CheckAffiliateLink -- No --> NoAffiliateLink
    NoAffiliateLink --> LoopURLs
     
    CheckAffiliateLinksList{Is `_promotion_links`<br>empty?}
    LoopURLs -- Loop End --> CheckAffiliateLinksList
    
    NoAffiliateLinksError[Log error: No affiliates, return]
    CheckAffiliateLinksList -- Yes --> NoAffiliateLinksError
     NoAffiliateLinksError --> End
    
    GetProductDetails[Retrieve product details: <br> `self.retrieve_product_details(_prod_urls)`]
    CheckAffiliateLinksList -- No --> GetProductDetails
    
     CheckProductDetails{Are Product <br>Details Empty?}
    GetProductDetails --> CheckProductDetails
    
    NoProductDetailsReturn[Return: No Details Found]
     CheckProductDetails -- Yes --> NoProductDetailsReturn
        NoProductDetailsReturn --> End
    
     LoopProducts[Loop through<br> `_affiliate_products`]
    CheckProductDetails -- No --> LoopProducts
    
    CheckPromotionLink{Is `promotion_link`<br> empty?}
    LoopProducts --> CheckPromotionLink
    
     ProcessPromotionLink[Parse URL<br> extract `aff_short_key`]
     CheckPromotionLink -- Yes --> ProcessPromotionLink
    
    CheckAffShortKey{Is `aff_short_key`<br>present?}
    ProcessPromotionLink --> CheckAffShortKey
    
    UpdatePromotionLink[Update <br> `product.promotion_link`]
    CheckAffShortKey -- Yes --> UpdatePromotionLink
    UpdatePromotionLink --> SaveImage
    
    DeleteProduct[Delete Product <br> `self.delete_product(product.product_id)`]
     CheckAffShortKey -- No --> DeleteProduct
      DeleteProduct --> SaveImage
    
    SavePromotionLink[Save promotion link: <br> `product.promotion_link = promotion_link`]
    CheckPromotionLink -- No --> SavePromotionLink
    SavePromotionLink --> SaveImage
    
    SaveImage[Save Image: <br>`save_png_from_url(...)`]
     SaveImage --> UpdateImagePath
     
     UpdateImagePath[Update<br> `product.local_image_path`]
        UpdateImagePath --> CheckVideoURL
     
     CheckVideoURL{Is `product_video_url` <br> valid?}
    CheckVideoURL --> CheckVideoURL
    
     SaveVideo[Save Video:<br> `save_video_from_url(...)`]
    CheckVideoURL -- Yes --> SaveVideo
     SaveVideo --> UpdateVideoPath
        
    UpdateVideoPath[Update<br>`product.local_video_path`]
       UpdateVideoPath --> LogProductCaught
     
     CheckVideoURL -- No --> LogProductCaught
     
     LogProductCaught[Log: Product Caught]
    LogProductCaught --> SaveProductJSON
    
    SaveProductJSON[Save Product <br>to JSON: `j_dumps(...)`]
    SaveProductJSON --> CheckJSONSaved
     
    CheckJSONSaved{Is JSON Saved?}
    CheckJSONSaved --> CheckJSONSaved
    
     LogJSONError[Log Error<br> JSON Not Saved]
    CheckJSONSaved -- No --> LogJSONError
    LogJSONError --> LoopProducts
    
    CheckJSONSaved -- Yes --> LoopProducts
    
   
   LoopProducts -- Loop End --> LogCaughtCount[Log Count: Products Caught]
   
   LogCaughtCount --> End[Return: `_affiliate_products`]
   End
    
```

**Зависимости (импорты) для диаграммы `mermaid`:**

*   **`src.suppliers.aliexpress.AliApi`**: Базовый класс для работы с Aliexpress API.
*   **`src.suppliers.aliexpress.utils.extract_product_id`**: Для извлечения ID продукта из URL.
*   **`src.suppliers.aliexpress.utils.set_full_https`**: Для преобразования URL в HTTPS.
*   **`src.utils.save_png_from_url`**: Для сохранения изображений.
*   **`src.utils.save_video_from_url`**: Для сохранения видео.
*  **`src.utils.jjson.j_dumps`**: Для сохранения JSON.
*  **`src.utils.printer.pprint`**: Для вывода информации в консоль.
*  **`src.logger.logger`**: Для логирования.
*   **`urllib.parse.urlparse` и `urllib.parse.parse_qs`**: Для работы с URL.
*   **`pathlib.Path`**: Для работы с путями к файлам.
*   `itertools` - не используется в диаграмме, но импортируется в коде
*   `typing` - не используется в диаграмме, но импортируется в коде
*   `types` - не используется в диаграмме, но импортируется в коде
*   `asyncio` - не используется в диаграмме, но импортируется в коде
*   `math` - не используется в диаграмме, но импортируется в коде
* `src.utils.convertor.csv2json` - не используется в диаграмме, но импортируется в коде
* `src.utils.file` - не используется в диаграмме, но импортируется в коде
* `src.suppliers.aliexpress.affiliate_links_shortener_via_webdriver` - не используется в диаграмме, но импортируется в коде
* `src.suppliers.aliexpress.Aliexpress` - не используется в диаграмме, но импортируется в коде

### 3. <объяснение>

**Импорты:**

*   **`asyncio`**: Библиотека для асинхронного программирования. В данном коде не используется, но может быть нужна для будущих расширений.
*   **`itertools`**: Модуль для работы с итераторами, используется для создания итерируемых объектов, хотя в этом коде напрямую не используется.
*   **`math`**: Модуль для математических операций, в данном коде не используется.
*   **`pathlib`**: Модуль для работы с файловыми путями в объектно-ориентированном стиле.
*   **`typing`**: Модуль для аннотации типов, используется для повышения читаемости кода.
*   **`types`**: Модуль для работы с типами, используется для создания SimpleNamespace.
*   **`urllib.parse`**: Модуль для разбора и конструирования URL.
    *   `urlparse`: Разбирает URL на компоненты (протокол, домен, путь и т.д.)
    *   `parse_qs`: Разбирает строку запроса URL в словарь.
*   **`src.gs`**: Глобальные настройки проекта, определенные в `src` пакете. Используется для доступа к путям файлов.
*   **`src.suppliers.aliexpress.AliApi`**: Базовый класс для взаимодействия с API AliExpress, из которого наследуется `AliAffiliatedProducts`.
*  **`src.suppliers.aliexpress.Aliexpress`**: Класс, вероятно, представляющий интерфейс для AliExpress, в этом коде не используется напрямую, но может быть частью структуры проекта.
*   **`src.suppliers.aliexpress.affiliate_links_shortener_via_webdriver`**: Класс для сокращения аффилиатных ссылок через веб-драйвер, в коде не используется.
*   **`src.suppliers.aliexpress.utils.extract_product_id`**: Функция для извлечения идентификатора продукта из URL.
*   **`src.suppliers.aliexpress.utils.set_full_https`**: Функция для обеспечения использования HTTPS в URL.
*   **`src.utils.convertor.csv2json`**: Конвертор CSV в JSON, не используется напрямую, но может быть частью проекта.
*   **`src.utils.jjson`**: Модуль для работы с JSON,  включающий функции для записи данных.
     *   `j_dumps`: Функция для записи JSON данных в файл.
*   **`src.utils`**: Различные утилиты проекта.
    *   `save_png_from_url`: Функция для сохранения изображения из URL.
    *   `save_video_from_url`: Функция для сохранения видео из URL.
*   **`src.utils.printer`**: Модуль для вывода данных в консоль.
     *   `pprint`: Функция для форматированного вывода данных.
*   **`src.utils.file`**: Модуль для работы с файлами.
    *   `read_text_file`: Функция для чтения текстового файла.
    *  `save_text_file`: Функция для сохранения текстового файла.
*   **`src.logger.logger`**: Модуль для логирования событий.

**Классы:**

*   **`AliAffiliatedProducts(AliApi)`**:
    *   **Роль:** Основной класс для получения данных о продуктах Aliexpress, включая аффилиатные ссылки, изображения и видео.
    *   **Атрибуты:**
        *   `campaign_name`: Название рекламной кампании.
        *   `campaign_category`: Категория рекламной кампании.
        *  `campaign_path`: Путь к директории, где хранятся все материалы кампании.
        *   `language`: Язык для рекламной кампании (по умолчанию 'EN').
        *   `currency`: Валюта для рекламной кампании (по умолчанию 'USD').
        *  `locale`:  Локализация, формируемая на основе языка и валюты.
    *   **Методы:**
        *   `__init__(self, campaign_name, campaign_category, language, currency, *args, **kwargs)`: Конструктор класса, инициализирующий атрибуты и вызывающий конструктор родительского класса `AliApi`.
        *   `process_affiliate_products(self, prod_urls)`: Основной метод для обработки списка URL или ID продуктов, получения аффилиатных ссылок, сохранения изображений, видео и JSON-файлов.
        *   `delete_product(self, product_id, exc_info)`: Метод для удаления продукта, если для него не удалось получить аффилиатную ссылку.

**Функции:**

*   **`__init__`**: Конструктор класса, инициализирует атрибуты экземпляра класса `AliAffiliatedProducts`
*   **`process_affiliate_products(self, prod_urls)`**:
    *   **Аргументы:**
        *   `prod_urls` (`List[str]`): Список URL или ID продуктов.
    *   **Возвращает:** `List[SimpleNamespace]` или None, список объектов SimpleNamespace, каждый из которых представляет обработанный продукт или None в случае ошибки.
    *   **Назначение:** Получает аффилиатные ссылки, скачивает изображения и видео, сохраняет данные в JSON.
*  **`delete_product(self, product_id, exc_info)`**:
    *   **Аргументы:**
        *   `product_id` (`str`): ID продукта, который нужно удалить.
        *   `exc_info` (`bool`): Флаг, указывающий, нужно ли логировать дополнительную информацию об исключениях.
    *   **Возвращает:** `None`
    *   **Назначение:** Удаляет информацию о продукте, если для него нет аффилиатной ссылки.

**Переменные:**

*   `_promotion_links`: Список для хранения аффилиатных ссылок.
*  `_prod_urls`: Список для хранения URL-ов продуктов, для которых удалось получить аффилиатную ссылку
*   `promotional_prod_urls`: Список URL, преобразованных в HTTPS.
*  `print_flag`: Флаг для контроля вывода данных в консоль (`new_line` или `inline`).
*  `_link`: Временная переменная для хранения аффилиатной ссылки
*   `_affiliate_products`: Результат работы метода `retrieve_product_details`
*   `product`:  Экземпляр `SimpleNamespace`, представляющий информацию о продукте.
*  `promotion_link`: Аффилиатная ссылка для текущего продукта.
*  `parsed_url`:  Результат разбора URL
* `query_params`: Словарь с параметрами из URL
*  `aff_short_key`: Короткий ключ из аффилиатной ссылки.
*   `image_path`:  Путь для сохранения изображения.
*   `video_path`: Путь для сохранения видео.

**Потенциальные ошибки и области для улучшения:**

*   **Обработка ошибок:** Код имеет базовую обработку ошибок, но её можно улучшить, например, обрабатывать ошибки при загрузке файлов.
*  **Улучшение производительности**: Для обработки большого количества URL можно использовать асинхронные запросы, чтобы ускорить процесс.
*  **Сокращение ссылок:**  Использование `src.suppliers.aliexpress.affiliate_links_shortener_via_webdriver`  пока не реализовано, но было бы полезно добавить для сокращения аффилиатных ссылок.
*  **Удаление файлов:** Код удаляет только записи из файла `sources.txt` и переименовывает `.html` файлы, но не удаляет сами файлы, что может привести к их накоплению.
*   **Логирование:** Добавить логирование всех важных этапов процесса, включая загрузку изображений и видео.
*  **Тестирование:**  Модульные тесты для различных сценариев, включая сбои в сети или ошибки в API, улучшили бы надежность кода.

**Взаимосвязи с другими частями проекта:**

*   Использует `AliApi` для взаимодействия с API Aliexpress, наследуя функциональность получения аффилиатных ссылок.
*   Использует `src.gs` для доступа к путям файлов, что обеспечивает гибкую конфигурацию путей.
*   Использует утилиты из `src.utils` для сохранения медиа и JSON, что способствует повторному использованию кода.
*   Использует `src.logger.logger` для логирования, что упрощает отладку и мониторинг.
*   Интегрирован в структуру проекта `src`, что позволяет ему взаимодействовать с другими частями системы (например, с рекламными кампаниями).