## <алгоритм>

1.  **Инициализация**:
    *   Получает список идентификаторов продуктов (`prod_ids`), корневой путь категории (`category_root`), и опционально язык (`language`) и валюту (`currency`).
    *   Создает объект `AliAffiliatedProducts`, используя переданные `language` и `currency`.
    *   Приводит все `prod_ids` к виду `https://aliexpress.com/item/<product_id>.html`

2.  **Поиск партнерских ссылок**:
    *   Итерируется по списку нормализованных URL продуктов (`normilized_prod_urls`).
    *   Для каждого URL вызывает `get_affiliate_links` (родительский метод) для получения партнерской ссылки.
    *   Если партнерская ссылка найдена, извлекает ее URL `promotion_link` и сохраняет в `_promotion_links`, а оригинальный URL в `_prod_urls`.

    *   _Пример: `prod_ids` = ["https://aliexpress.com/item/12345.html", "12346", "https://example.com/item/12347"], после нормализации `normilized_prod_urls` = \["https://aliexpress.com/item/12345.html", "https://aliexpress.com/item/12346.html", "https://aliexpress.com/item/12347.html"\]. Для `12345` найдена `promotion_link = "https://s.click.aliexpress.com/e/_D12345"` , которая добавляется в `_promotion_links` и оригинальный url в `_prod_urls`.

3.  **Получение деталей продукта**:
    *   Если `_promotion_links` пуст, выводит предупреждение и завершает работу.
    *   Если ссылки найдены, вызывает `retrieve_product_details` (родительский метод) со списком оригинальных URL продуктов `_prod_urls`, возвращая список объектов `SimpleNamespace` с информацией о продукте.
    *   Если данные о продуктах не получены, функция завершается.

4.  **Обработка и сохранение данных о продукте**:
    *   Итерируется по спискам деталей продукта `_affiliated_products` и партнерских ссылок `_promotion_links`.
    *   Для каждого продукта добавляет `language`, `promotion_link`.
    *   Сохраняет главное изображение продукта (`product.product_main_image_url`) в `category_root/images/<product_id>.png`.
    *   Сохраняет видео продукта (`product.product_video_url`), если оно есть, в `category_root/videos/<product_id><video_suffix>`.
    *   Сохраняет объект продукта в формате JSON в `category_root/<language>_<currency>/<product_id>.json`
    *   Добавляет продукт в список `affiliated_products_list`.
    *   Добавляет тайтл продукта в список `product_titles`

    *   _Пример:_ Для продукта с `product_id = 12345`, `product.product_main_image_url = "https://example.com/image.png"`,  изображение сохраняется в `category_root/images/12345.png`, если `product.product_video_url = "https://example.com/video.mp4"`, видео сохраняется в `category_root/videos/12345.mp4`. JSON сохраняется в `category_root/<language>_<currency>/12345.json`

5.  **Сохранение списка тайтлов**:
    *   Сохраняет список тайтлов продукта в файл `category_root/<language>_<currency>/product_titles.txt`
6.  **Возврат**:
    *   Возвращает список `affiliated_products_list`.

## <mermaid>

```mermaid
flowchart TD
    Start(Start) --> NormalizeUrls[Normalize Product URLs to 'https://aliexpress.com/item/product_id.html'];
    NormalizeUrls --> GetAffiliateLinks{Get Affiliate Links};
    GetAffiliateLinks -- Found Links --> CollectLinks[Collect promotion_link and original URLs];
    GetAffiliateLinks -- No Links --> NoAffiliateLinks[Log Warning];
    CollectLinks --> RetrieveProductDetails{Retrieve Product Details};
    NoAffiliateLinks --> End(End)
    RetrieveProductDetails -- Success --> ProcessProducts[Process Products and Save Data];
    RetrieveProductDetails -- Fail --> End;
    ProcessProducts --> SaveImage{Save Product Image};
    SaveImage --> SaveVideo{Save Product Video (if available)};
     SaveVideo --> SaveJson{Save Product data to Json};
     SaveJson --> SaveTitles{Save product titles to txt};
    SaveTitles --> End
    
  
    classDef common fill:#f9f,stroke:#333,stroke-width:2px;
    class Start,End common;

```

**Объяснение `mermaid`:**

*   `flowchart TD`:  Определяет, что это блок-схема с направлением сверху вниз.
*   `Start`, `NormalizeUrls`, `GetAffiliateLinks`, `CollectLinks`, `NoAffiliateLinks`, `RetrieveProductDetails`, `ProcessProducts`, `SaveImage`, `SaveVideo`, `SaveJson`, `SaveTitles`, `End`:  Это узлы диаграммы, представляющие отдельные этапы процесса.
*   `-->`:  Указывает направление потока между узлами.
*   `-- Found Links -->` , `-- No Links -->`, `-- Success -->`, `-- Fail -->` : Стрелки с надписями, указывающие условные переходы.
*   `classDef common fill:#f9f,stroke:#333,stroke-width:2px;`: Определяет стиль для классов.
*   `class Start,End common;`: Применяет стиль `common` к узлам `Start` и `End`.

**Зависимости импорта:**

1.  `asyncio`: Используется для асинхронных операций, таких как сохранение изображений и видео.
2.  `datetime`:  Может использоваться для временных меток (хотя не используется в этом коде напрямую).
3.  `html`:  Используется для обработки HTML-данных.
4.  `pathlib.Path`:  Используется для работы с путями файлов и директориями.
5.  `urllib.parse.urlparse`: Используется для разбора URL-адресов.
6.  `types.SimpleNamespace`:  Используется для создания простых объектов для хранения данных.
7.  `typing.List`: Используется для аннотации типов списков.
8.  `src.logger.logger.logger`:  Используется для логирования событий и ошибок.
9.  `src.gs`:  Глобальные настройки проекта (не показаны в коде, но предполагаются).
10. `src.suppliers.aliexpress.AliApi`: Базовый класс для работы с API AliExpress (родительский класс).
11. `src.suppliers.aliexpress.campaign.html_generators`:  Содержит генераторы HTML (не используется в этом конкретном коде).
12. `src.suppliers.aliexpress.utils.ensure_https`: Функция для обеспечения использования HTTPS в URL.
13. `src.endpoints.prestashop.product_fields.ProductFields`: Поля для продуктов PrestaShop. (не используется в данном коде).
14. `src.utils.image.save_image_from_url`:  Функция для асинхронного сохранения изображений из URL.
15. `src.utils.video.save_video_from_url`:  Функция для асинхронного сохранения видео из URL.
16. `src.utils.file_async.*`:  Функции для асинхронной работы с файлами (чтение, запись, получение имен).
17. `src.utils.jjson.*`: Функции для работы с JSON (загрузка и сохранение).
18. `src.utils.printer.pprint`: Функция для форматированного вывода.

## <объяснение>

**Импорты:**

*   `asyncio`: Необходим для асинхронного программирования, позволяет одновременно выполнять несколько операций, таких как загрузка изображений и видео, не блокируя основной поток.
*   `datetime`: Хотя явно не используется в предоставленном коде, обычно применяется для работы со временем и датами, например, для добавления временных меток в логи или файлы.
*   `html`: Используется для работы с HTML-кодом.
*   `pathlib.Path`: Предоставляет более удобный и кроссплатформенный способ работы с путями файлов и директорий по сравнению с обычными строками.
*   `urllib.parse.urlparse`: Позволяет разбирать URL-адреса на составные части (протокол, хост, путь, и т.д.), что полезно для манипуляций с URL.
*   `types.SimpleNamespace`: Создает простые объекты, которые можно использовать для хранения атрибутов, что удобно для передачи и хранения данных без необходимости создания полноценного класса.
*  `typing.List`: Обеспечивает аннотацию типов данных, что улучшает читаемость и поддержку кода.
*   `src.logger.logger.logger`: Пользовательский класс для логирования, используется для записи информации о работе скрипта, а также для отладки. Помогает отслеживать процесс выполнения, сообщать об ошибках и предупреждениях.
*   `src.gs`: Доступ к глобальным настройкам проекта, который, предположительно, хранит общую конфигурацию приложения.
*   `src.suppliers.aliexpress.AliApi`: Базовый класс для взаимодействия с API AliExpress, который реализует основные функции для работы с API, такие как получение партнерских ссылок и информации о продуктах.
*   `src.suppliers.aliexpress.campaign.html_generators`: Содержит классы для генерации HTML-контента, что может быть использовано для создания рекламных кампаний, но напрямую не используется в данном коде.
*   `src.suppliers.aliexpress.utils.ensure_https`: Функция, гарантирующая, что все URL-адреса используют HTTPS, что является важным для безопасности и правильного функционирования.
*   `src.endpoints.prestashop.product_fields.ProductFields`: Предоставляет константы для полей продукта в PrestaShop, но не используется в данном коде, что может указывать на будущую интеграцию или устаревший импорт.
*   `src.utils.image.save_image_from_url`: Асинхронная функция для загрузки и сохранения изображений с использованием URL.
*   `src.utils.video.save_video_from_url`: Асинхронная функция для загрузки и сохранения видео с использованием URL.
*  `src.utils.file_async`: Модуль, содержащий функции для работы с файлами в асинхронном режиме, что повышает производительность при операциях ввода/вывода.
*   `src.utils.jjson`: Модуль для работы с JSON, используется для сохранения и загрузки данных в формате JSON.
*   `src.utils.printer.pprint`: Функция для форматированного вывода данных, которая делает их более читабельными.

**Классы:**

*   `AliAffiliatedProducts`:
    *   **Роль:** Класс для получения данных о товарах AliExpress, включая партнерские ссылки, с сохранением изображений и видео.
    *   **Атрибуты:**
        *   `language`: Язык для кампании.
        *   `currency`: Валюта для кампании.
    *   **Методы:**
        *   `__init__`: Инициализирует класс, получает `language` и `currency` и вызывает `super().__init__(language, currency)`.
        *   `process_affiliate_products`: Основной метод класса, который выполняет получение партнерских ссылок, сбор данных о продукте и их сохранение.
            *   Принимает список идентификаторов продуктов (`prod_ids`), путь к корневой категории (`category_root`), а также `language` и `currency`.
            *   Нормализует URL-адреса, получает партнерские ссылки и детали продуктов, а затем сохраняет изображения, видео и JSON-данные.
            *   Возвращает список объектов `SimpleNamespace`, представляющих обработанные продукты.
    *   **Взаимодействие:**
        *   Наследуется от `AliApi`, получая доступ к методам для работы с API AliExpress.
        *   Использует функции из `src.utils.image`, `src.utils.video`, `src.utils.file_async`, `src.utils.jjson` для асинхронного сохранения данных.
        *   Использует `src.logger.logger` для логирования.

**Функции:**

*   `__init__(self, language: str | dict = 'EN', currency: str = 'USD', *args, **kwargs)`: Конструктор класса `AliAffiliatedProducts`, устанавливает язык и валюту, инициализирует родительский класс `AliApi`.
*   `process_affiliate_products(self, prod_ids: list[str], category_root: Path | str) -> list[SimpleNamespace]`: Основная функция, которая обрабатывает список идентификаторов продуктов, получает партнерские ссылки, информацию о продуктах, сохраняет изображения, видео и JSON-данные.
    *   **Аргументы:**
        *   `prod_ids`: Список идентификаторов или URL продуктов.
        *   `category_root`: Путь к корневой директории категории.
    *   **Возвращает:** Список объектов `SimpleNamespace`, представляющих обработанные продукты.
*   `ensure_https(urls: list[str]) -> list[str]`:  Обеспечивает, что все URL-адреса в списке используют HTTPS.
*   `save_image_from_url(url: str, file_path: Path)`: Асинхронно скачивает и сохраняет изображение из URL по указанному пути.
*  `save_video_from_url(url: str, file_path: Path)`: Асинхронно скачивает и сохраняет видео из URL по указанному пути.
*   `read_text_file(file_path: Path, encoding: str = 'utf-8')`:  Асинхронно читает текстовый файл.
*   `get_filenames_from_directory(dir_path: Path)`: Получает список файлов в директории.
*   `get_directory_names(dir_path: Path)`: Получает список папок в директории.
*   `save_text_file(data: str | list, file_path: Path, encoding: str = 'utf-8')`: Асинхронно сохраняет текст в файл.
*   `j_loads_ns(file_path: Path, encoding: str = 'utf-8')`: Асинхронно читает JSON файл и возвращает данные в виде `SimpleNamespace`.
*   `j_dumps(obj: object, file_path: Path, encoding: str = 'utf-8')`:  Сохраняет объект в JSON файл.
*   `pprint(*args, end='\n')`:  Форматированный вывод в консоль.

**Переменные:**

*   `_promotion_links`: Список партнерских ссылок, полученных от API.
*   `_prod_urls`: Список исходных URL продуктов.
*   `normilized_prod_urls`: Список нормализованных URL продуктов (все URL приведены к виду https://aliexpress.com/item/<product_id>.html).
*   `print_flag`: Флаг для управления выводом в одну строку.
*   `_affiliated_products`: Список объектов `SimpleNamespace`, содержащих детали продуктов.
*    `affiliated_products_list`: Список объектов `SimpleNamespace`, содержащих обработанные продукты.
*   `product_titles`: Список тайтлов продуктов.
*    `product`: Экземпляр класса `SimpleNamespace`, представляющий данные продукта.
*   `promotion_link`: Партнерская ссылка.
*   `image_path`: Путь к файлу изображения продукта.
*   `video_path`: Путь к файлу видео продукта.
*   `suffix`: Расширение файла видео.
*   `parsed_url`: Объект `urlparse`, содержащий результаты парсинга URL видео.
*   `product_titles_path`: Путь к файлу, в который сохраняются тайтлы.
*   `category_root`: Путь к корневой директории категории.

**Потенциальные ошибки и области для улучшения:**

*   **Обработка ошибок**: В коде есть некоторые места, где не обрабатываются возможные исключения. Например, при получении партнерских ссылок или при сохранении изображений/видео. Необходимо добавить обработку ошибок `try-except`, чтобы код не завершался аварийно и логировал ошибки.
*   **Валидация данных**: Код предполагает, что все URL-адреса продуктов будут в правильном формате. Необходимо добавить валидацию входных данных (например, проверить наличие необходимых полей в полученных данных о продуктах).
*   **Управление зависимостями**:  Зависимость от `src.gs` не является явной в предоставленном коде. Необходимо прояснить, как эти глобальные настройки используются и добавить их валидацию.
*   **Логика нормализации URL**: Необходимо более подробно изучить код метода `ensure_https`, чтобы убедится в правильной работе.
*   **Не используется HTML генератор**: Код импортирует `src.suppliers.aliexpress.campaign.html_generators`, но не использует его. Можно рассмотреть его использование в будущем.
*   **Закомментированный код**: В коде присутствуют закомментированные строки, что указывает на то, что код был изменен. Необходимо убрать закомментированный код.

**Цепочка взаимосвязей с другими частями проекта:**

1.  **src.suppliers.aliexpress.AliApi:**  Класс `AliAffiliatedProducts` наследуется от `AliApi`, поэтому он зависит от его реализации методов, например, `get_affiliate_links`, `retrieve_product_details`.
2.  **src.utils.image, src.utils.video, src.utils.file_async:**  Класс `AliAffiliatedProducts` использует эти модули для асинхронного скачивания и сохранения файлов, что делает его зависимым от их функциональности.
3.  **src.utils.jjson:** Используется для загрузки и сохранения данных о товарах в формате JSON.
4.  **src.logger.logger:** Используется для логирования работы скрипта.
5. **src.gs:** Зависит от глобальных настроек проекта, которые предположительно хранят общую конфигурацию.
6. **src.endpoints.prestashop.product_fields:**  Хотя и не используется напрямую, импорт этого модуля предполагает потенциальную интеграцию с PrestaShop.

Таким образом, класс `AliAffiliatedProducts` является частью более крупной системы, включающей взаимодействие с API AliExpress, обработку файлов, асинхронные операции, логирование и потенциально интеграцию с PrestaShop.