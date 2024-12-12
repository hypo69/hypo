## Анализ кода `affiliated_products_generator.py`

### 1. <алгоритм>

**Блок-схема:**

1.  **Инициализация `AliAffiliatedProducts`:**
    *   Принимает `campaign_name`, `campaign_category`, `language`, `currency`.
    *   Инициализирует `AliApi` (родительский класс).
    *   Формирует `campaign_path` для сохранения данных.

    *Пример:*
    ```python
    parser = AliAffiliatedProducts(
                                campaign_name="test_campaign",
                                campaign_category="electronics",
                                language="EN",
                                currency="USD"
                                )
    ```

2.  **`process_affiliate_products(prod_urls)`:**
    *   Принимает список `prod_urls` (URL-адреса или ID товаров).
    *   Преобразует URL-адреса в HTTPS.
    *   Инициализирует пустые списки `_promotion_links` и `_prod_urls`.
    *   **Цикл по `prod_urls`:**
        *   Получает аффилированную ссылку `_link` с помощью `super().get_affiliate_links(prod_url)`.
        *   **Если `_link` найдена:**
            *   Добавляет `_link.promotion_link` в `_promotion_links`.
            *   Добавляет `prod_url` в `_prod_urls`.
            *   Выводит сообщение о найденной аффилированной ссылке.

            *Пример:*
            ```
             prod_urls = ['https://www.aliexpress.com/item/123.html', '456']
             #_link для первого элемента: SimpleNamespace(promotion_link='https://s.click.aliexpress.com/e/test1')
             #_link для второго элемента: None
             # _promotion_links: ['https://s.click.aliexpress.com/e/test1']
             # _prod_urls: ['https://www.aliexpress.com/item/123.html']
            ```
        *   **Иначе:**
            *   Логирует отсутствие аффилированной ссылки.

    *   **Если `_promotion_links` пуст:**
        *   Логирует ошибку и завершает функцию.
    *   Получает детали продукта с помощью `self.retrieve_product_details(_prod_urls)`.
    *   **Если `_affiliate_products` пуст:**
        *   Завершает функцию.
    *   **Цикл по `_affiliate_products` и `_promotion_links` (параллельно):**
        *   **Если `promotion_link` пуста:**
            *   Извлекает `aff_short_key` из `product.promotion_link`.
            *   **Если `aff_short_key` существует:**
                *   Обновляет `product.promotion_link` на короткую ссылку.
            *   **Иначе:**
                 *   Удаляет продукт с помощью `self.delete_product(product.product_id)`.
        *   **Иначе:**
            *    Устанавливает `product.promotion_link = promotion_link`.

        *   Формирует `image_path` и сохраняет изображение с помощью `save_png_from_url`.
        *   Сохраняет `image_path` в `product.local_saved_image`.
        *    **Если `product.product_video_url` существует:**
            *   Формирует `video_path` и сохраняет видео с помощью `save_video_from_url`.
            *   Сохраняет `video_path` в `product.local_saved_video`.
        *   Сохраняет данные продукта в JSON файл с помощью `j_dumps`.
            *   Если не удалось записать данные, то логирует ошибку.
    *   Выводит количество обработанных продуктов.
    *   Возвращает список обработанных продуктов `_affiliate_products`.
3.  **`delete_product(product_id)`:**
    *   Принимает `product_id` (ID товара).
    *   Извлекает ID товара с помощью `extract_prod_ids(product_id)`.
    *   Формирует путь к файлу `product_path = self.campaign_path / 'sources.txt'`.
    *   Формирует путь к файлу `prepared_product_path = self.campaign_path / '_sources.txt'`.
    *   Читает список `products_list` из `product_path`.
    *   **Если `products_list` не пуст:**
        *   Конвертирует список к однородному виду.
        *   **Цикл по записям `record` в `products_list`:**
            *   **Если `_product_id` не пуст:**
                *   Извлекает ID из `record` с помощью `extract_prod_ids(record)`
                *   **Если `record_id` совпадает с `product_id`:**
                    *   Удаляет `record` из `products_list`
                    *   Сохраняет обновленный список в `prepared_product_path`
            *   **Иначе:**
                *   **Если `record` совпадает с `product_id`:**
                     *   Удаляет `record` из `products_list`
                     *   Сохраняет обновленный список в `product_path`
    *   **Иначе:**
        *   Формирует путь к файлу `product_path = self.campaign_path / 'sources' / f'{product_id}.html'`.
        *   Переименовывает файл.
        *   Логирует результат.

### 2. <mermaid>

```mermaid
graph LR
    A[AliAffiliatedProducts] --> B(process_affiliate_products);
    B --> C{ensure_https(prod_urls)};
    C -->|HTTPS URLs| D[AliApi.get_affiliate_links];
    D -->|Affiliate Links| E{Has Affiliate Link?};
    E -- Yes --> F[Save promotion_link and prod_url];
    E -- No --> G[Log: No Affiliate];
    F --> H{_promotion_links is not empty?};
    H -- Yes --> I[AliApi.retrieve_product_details];
    H -- No --> J[Log: No affiliate products returned];
    I -->|Product Details| K{Loop through products and promotion links};
    K --> L{promotion_link exists?};
    L -- No --> M[Extract aff_short_key];
    M --> N{aff_short_key exists?};
    N -- Yes --> O[Update product.promotion_link];
    N -- No --> P[delete_product(product.product_id)];
    L -- Yes --> Q[Assign promotion link];
    O --> R[save_png_from_url];
    Q --> R
    R --> S[Save image path];
    S --> T{product.product_video_url exists?};
    T -- Yes --> U[save_video_from_url];
    T -- No --> V[j_dumps(product)];
    U --> V
    V --> W{Save JSON Data};
    W --> X[Return _affiliate_products];
    P --> X
    J --> X

    subgraph Methods
    B
    D
    I
    P
    end
    subgraph Utils
    C
    R
    U
    V
    end

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ccf,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333,stroke-width:2px
    style I fill:#ccf,stroke:#333,stroke-width:2px
    style P fill:#ccf,stroke:#333,stroke-width:2px
    style C fill:#afa,stroke:#333,stroke-width:2px
    style R fill:#afa,stroke:#333,stroke-width:2px
    style U fill:#afa,stroke:#333,stroke-width:2px
     style V fill:#afa,stroke:#333,stroke-width:2px
```

**Зависимости:**

*   **`AliAffiliatedProducts`:** Основной класс для обработки аффилированных продуктов.
*   **`process_affiliate_products`:** Метод класса `AliAffiliatedProducts`, который координирует весь процесс сбора данных о продуктах.
*   **`AliApi.get_affiliate_links`:** Метод родительского класса, который получает аффилированные ссылки для продуктов.
*   **`AliApi.retrieve_product_details`:** Метод родительского класса, который получает детальную информацию о продукте.
*   **`ensure_https`:** Функция для преобразования URL в HTTPS.
*  **`save_png_from_url`:** Функция для сохранения изображений с URL.
*  **`save_video_from_url`:** Функция для сохранения видео с URL.
*  **`j_dumps`:** Функция для сохранения данных в JSON.
* **`delete_product`:** Метод, удаляющий информацию о продукте.

### 3. <объяснение>

**Импорты:**

*   `asyncio`: Стандартная библиотека для асинхронного программирования. В данном коде напрямую не используется, но может быть необходима для асинхронных вызовов в других частях проекта.
*   `itertools`: Стандартная библиотека для работы с итераторами. Используется, но в данном коде напрямую не виден.
*   `math`: Стандартная библиотека для математических операций. В данном коде не используется.
*   `pathlib`: Стандартная библиотека для работы с путями в файловой системе.
*   `typing`: Стандартная библиотека для аннотации типов.
*   `types`: Стандартная библиотека для работы с типами. Используется для создания `SimpleNamespace`.
*   `urllib.parse`: Стандартная библиотека для работы с URL. Используется для парсинга URL.
*   `src.gs`: Кастомный модуль для общих настроек. Используется для доступа к путям.
*   `src.suppliers.aliexpress.AliApi`: Кастомный класс для работы с API Aliexpress. Является родительским классом для `AliAffiliatedProducts`.
*    `src.suppliers.aliexpress.Aliexpress`: Кастомный модуль, но в коде не используется.
*   `src.suppliers.aliexpress.affiliate_links_shortener_via_webdriver`: Модуль для сокращения аффилированных ссылок через веб-драйвер, но в данном коде не используется.
*   `src.suppliers.aliexpress.utils.extract_product_id`: Модуль для извлечения ID продукта из URL или строки.
*   `src.suppliers.aliexpress.utils.set_full_https`: Модуль для преобразования URL в HTTPS.
*   `src.utils.convertor.csv2json`: Модуль для конвертации CSV в JSON, но в данном коде не используется.
*   `src.utils.jjson`: Модуль для работы с JSON (сохранение в файл).
*   `src.utils`: Пакет с утилитами, в данном случае `save_png_from_url` и `save_video_from_url`.
*   `src.utils.printer`: Модуль для красивого вывода сообщений.
*   `src.utils.file`: Модуль для работы с файлами `read_text_file` и `save_text_file`.
*   `src.logger.logger`: Модуль для логирования.

**Класс `AliAffiliatedProducts`:**

*   **Роль:** Класс, который инкапсулирует логику для получения данных о товарах AliExpress, включая аффилированные ссылки.
*   **Атрибуты:**
    *   `campaign_name`: Название рекламной кампании.
    *   `campaign_category`: Категория кампании.
    *   `campaign_path`: Путь к директории, где хранятся материалы кампании.
    *   `language`: Язык кампании.
    *   `currency`: Валюта кампании.
    *   `locale`: Локаль кампании (формируется как `язык_валюта`).
*   **Методы:**
    *   `__init__`: Конструктор класса, инициализирует атрибуты и вызывает конструктор родительского класса `AliApi`.
    *   `process_affiliate_products`: Основной метод, обрабатывает список URL-адресов продуктов, получает аффилированные ссылки, сохраняет изображения и видео, сохраняет информацию о товаре в JSON.
    *   `delete_product`: Удаляет информацию о продукте, если он не имеет аффилированной ссылки.

**Функции:**

*   `__init__` (конструктор):
    *   **Аргументы:** `campaign_name`, `campaign_category`, `language`, `currency`.
    *   **Возвращаемое значение:** Нет.
    *   **Назначение:** Инициализирует объект класса `AliAffiliatedProducts` и формирует путь к файлу.
*   `process_affiliate_products`:
    *   **Аргументы:** `prod_urls` (список URL-адресов или ID товаров).
    *   **Возвращаемое значение:** Список объектов `SimpleNamespace`, представляющих обработанные продукты.
    *   **Назначение:** Получает аффилированные ссылки для продуктов, сохраняет изображения и видео, сохраняет информацию о товаре в JSON.
*   `delete_product`:
    *   **Аргументы:** `product_id` (ID товара), `exc_info` (флаг для логирования ошибок).
    *   **Возвращаемое значение:** Нет.
    *   **Назначение:** Удаляет информацию о продукте.

**Переменные:**

*   `_promotion_links`: Список аффилированных ссылок.
*   `_prod_urls`: Список URL-адресов товаров.
*   `_affiliate_products`: Список объектов `SimpleNamespace` с информацией о товарах.
*   `print_flag`: Флаг для управления выводом в консоль.
*   `product`: Объект `SimpleNamespace`, представляющий информацию о продукте.
*   `image_path`, `video_path`: Пути к файлам для сохранения изображений и видео.
*   `aff_short_key`: Короткий ключ аффилированной ссылки.
*    `products_list`: Список товаров.
*   `record`: запись в списке.

**Потенциальные ошибки и области для улучшения:**

*   **Обработка ошибок:**  Улучшить обработку ошибок при запросах к API, сохранении файлов и др.
*   **Асинхронность:**  Использовать асинхронные запросы для ускорения обработки большого количества продуктов.
*   **Тестирование:**  Добавить больше юнит-тестов для покрытия всех сценариев использования.
*   **Логирование:**  Сделать логирование более гибким и настраиваемым.
*  **Удаление файла:** Непонятно почему удаление файла перенесено в переименование, в методе `delete_product`.
*   **Сложная логика поиска:** Сделать более понятной логику удаления продукта через чтение и запись файлов.

**Взаимосвязи с другими частями проекта:**

*   Зависит от `src.gs` для доступа к путям и настройкам.
*   Использует `src.suppliers.aliexpress.AliApi` для работы с API Aliexpress.
*   Использует `src.utils` для сохранения файлов и других утилит.
*   Использует `src.logger.logger` для логирования.

Этот подробный анализ дает полное представление о структуре, функциях и зависимостях кода, что позволяет лучше понять его работу и выявить потенциальные улучшения.