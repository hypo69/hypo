## АНАЛИЗ КОДА: `src.category`

### <алгоритм>

1.  **Инициализация `Category`**:
    *   При создании экземпляра класса `Category` (`category = Category(api_credentials={'api_key': 'your_api_key'})`), вызывается конструктор `__init__`, который принимает `api_credentials` и (неиспользуемые) `*args` и `**kwargs`.
    *   **Пример**: `category = Category(api_credentials={'api_key': 'test_key'})`.
    
2.  **Получение родительских категорий (`get_parents`)**:
    *   Метод `get_parents` принимает `id_category` и `dept` в качестве аргументов.
    *   Он используется для получения списка родительских категорий для указанной `id_category` на определенной глубине (`dept`).
    *   **Пример**: `parents = category.get_parents(id_category=123, dept=2)`.
    
3.  **Асинхронный обход категорий (`crawl_categories_async`)**:
    *   Метод `crawl_categories_async` принимает `url`, `depth`, `driver` (экземпляр Selenium WebDriver), `locator` (XPath), `dump_file` (путь к JSON файлу), `default_category_id` и (необязательный) `category` (словарь).
    *   Использует рекурсивный обход, начиная с указанного `url`, и создает иерархический словарь категорий.
    *   Сохраняет результаты в `dump_file`.
    *   **Пример**:
        ```python
        category_data = await category.crawl_categories_async(
            url='https://example.com/categories',
            depth=3,
            driver=driver_instance,
            locator='//a[@class="category-link"]',
            dump_file='categories.json',
            default_category_id=123
        )
        ```

4.  **Синхронный обход категорий (`crawl_categories`)**:
    *   Метод `crawl_categories` похож на `crawl_categories_async`, но выполняет обход синхронно.
    *   Принимает аналогичные параметры.
    *   Строит иерархический словарь, но не использует асинхронность.
    *   **Пример**:
        ```python
        category_data_sync = category.crawl_categories(
            url='https://example.com/categories',
            depth=3,
            driver=driver_instance,
            locator='//a[@class="category-link"]',
            dump_file='categories_sync.json',
            id_category_default=123
        )
        ```
        
5.  **Проверка дубликатов URL (`_is_duplicate_url`)**:
    *   Метод `_is_duplicate_url` проверяет, существует ли данный `url` уже в словаре `category`.
    *   Используется для предотвращения повторного обхода одних и тех же страниц.
    *   **Пример**: `is_duplicate = category._is_duplicate_url(category_data, 'https://example.com/category1')`

6.  **Сравнение и печать отсутствующих ключей (`compare_and_print_missing_keys`)**:
    *   Функция `compare_and_print_missing_keys` сравнивает `current_dict` с данными из файла по пути `file_path`.
    *   Выводит ключи, которые есть в файле, но отсутствуют в `current_dict`.
    *   **Пример**: `compare_and_print_missing_keys(current_dict=category_data, file_path='saved_categories.json')`

### <mermaid>
```mermaid
flowchart TD
    subgraph Category Class
        A[Category Constructor: <br><code>__init__(api_credentials)</code>]
        B[Get Parents: <br><code>get_parents(id_category, dept)</code>]
        C[Async Crawl Categories: <br><code>crawl_categories_async(url, depth, driver, locator, dump_file, default_category_id, category)</code>]
        D[Sync Crawl Categories: <br><code>crawl_categories(url, depth, driver, locator, dump_file, id_category_default, category)</code>]
        E[Check Duplicate URL: <br><code>_is_duplicate_url(category, url)</code>]
    end

    F[Compare and Print Missing Keys:<br><code>compare_and_print_missing_keys(current_dict, file_path)</code>]

    A --> B
    A --> C
    A --> D
    C --> E
    D --> E
    C --> F
    D --> F
    
    subgraph PrestaShop Dependencies
        G[PrestaShop API: <br><code>src.endpoints.prestashop.PrestaShop</code>]
        H[PrestaCategory: <br><code>src.endpoints.prestashop.PrestaCategory</code>]
    end
    
    subgraph Utils Dependencies
        I[Load JSON: <br><code>src.utils.jjson.j_loads</code>]
        J[Dump JSON: <br><code>src.utils.jjson.j_dumps</code>]
    end

    subgraph Logging
        K[Logger: <br><code>src.logger.logger</code>]
    end
    
    A --> H
    B --> H
    C --> G
    D --> G
    C --> I
    C --> J
    D --> I
    D --> J
    C --> K
    D --> K
    F --> I
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style F fill:#ccf,stroke:#333,stroke-width:2px
```
**Объяснение зависимостей `mermaid`:**

*   **`Category Class`**:  Описывает основные методы класса `Category` и их взаимосвязи, включая конструктор `__init__`, методы для получения родительских категорий `get_parents`, асинхронного и синхронного обхода категорий `crawl_categories_async`, `crawl_categories`, и проверки дубликатов URL `_is_duplicate_url`.
*   **`Compare and Print Missing Keys`**: Описывает функцию, которая сравнивает текущий словарь с данными из файла и печатает недостающие ключи.
*   **`PrestaShop Dependencies`**: Описывает зависимости от модулей PrestaShop API `src.endpoints.prestashop.PrestaShop` и `src.endpoints.prestashop.PrestaCategory`. `PrestaCategory` используется как родительский класс.
*   **`Utils Dependencies`**: Описывает зависимости от модулей `j_loads` и `j_dumps` из `src.utils.jjson`, которые используются для работы с JSON.
*   **`Logging`**: Описывает зависимость от модуля `logger` из `src.logger`, который используется для логирования.

### <объяснение>

#### Импорты:

*   `src.endpoints.prestashop.PrestaShop`: Модуль, вероятно, предоставляет класс для взаимодействия с API PrestaShop. Класс `Category` может использовать его для получения данных о категориях через API.
*   `src.endpoints.prestashop.PrestaCategory`: Предоставляет базовый класс для работы с категориями PrestaShop. Класс `Category` наследуется от этого класса, используя его атрибуты и методы.
*   `src.utils.jjson.j_loads`:  Используется для загрузки данных из JSON-файлов. Применяется, когда необходимо сравнить текущие категории с сохраненными данными или когда происходит загрузка данных из сохраненных файлов.
*   `src.utils.jjson.j_dumps`: Используется для сохранения данных в JSON-файл. Применяется для сохранения результатов обхода категорий.
*   `src.logger.logger`: Обеспечивает функциональность логирования. Используется для отслеживания ошибок и шагов выполнения программы, особенно в процессах обхода категорий.

#### Класс `Category`:

*   **Роль**: Управляет категориями товаров, предоставляя методы для получения родительских категорий и обхода страниц категорий.
*   **Атрибуты**:  Имеет атрибуты, унаследованные от `PrestaCategory`, которые могут включать API-ключи и другие необходимые настройки.
*   **Методы**:
    *   `__init__`: Конструктор класса, который инициализирует объект `Category` с API-ключами, необходимыми для взаимодействия с PrestaShop.
    *   `get_parents`: Получает список родительских категорий для указанной категории по ее идентификатору. Этот метод помогает построить иерархию категорий.
    *   `crawl_categories_async`: Асинхронно обходит страницы категорий, строя иерархический словарь категорий и их URL-адресов.
    *   `crawl_categories`: Синхронно обходит страницы категорий, аналогично `crawl_categories_async`, но без использования асинхронности.
    *   `_is_duplicate_url`: Вспомогательный метод, проверяющий, существует ли уже URL-адрес в словаре категорий, для избежания повторных обходов.
*   **Взаимодействие**:
    *   Использует `PrestaShop` для запросов к API.
    *   Наследуется от `PrestaCategory`, расширяя его функциональность методами обхода категорий.
    *   Использует `j_loads` и `j_dumps` для сохранения и загрузки данных в JSON-формате.

#### Функции:

*   `compare_and_print_missing_keys`:
    *   **Аргументы**:  Принимает `current_dict` (словарь) и `file_path` (путь к файлу).
    *   **Возвращаемое значение**: Отсутствует (None).
    *   **Назначение**: Сравнивает `current_dict` с данными из файла и выводит отсутствующие ключи. Это полезно для выявления изменений в структуре категорий.

#### Переменные:

*   `api_credentials`:  Словарь, содержащий API-ключи для доступа к данным PrestaShop.
*   `id_category`: Идентификатор категории.
*   `dept`: Глубина иерархии категорий.
*   `url`: URL-адрес страницы категории для обхода.
*   `depth`: Глубина рекурсии при обходе категорий.
*   `driver`: Экземпляр Selenium WebDriver для управления браузером.
*   `locator`:  XPath-локатор для поиска ссылок на категории.
*   `dump_file`: Путь к файлу для сохранения данных.
*   `default_category_id`: ID категории по умолчанию.
*   `category`: Словарь для хранения категорий.

#### Потенциальные ошибки и улучшения:

*   **Обработка ошибок:** Код не содержит явной обработки ошибок при запросах к API или операциях с файлами.  Рекомендуется добавить блоки `try...except` для обработки исключений.
*   **Неявные зависимости:** Функции `crawl_categories_async` и `crawl_categories` требуют явного экземпляра `driver`, что может приводить к ошибкам, если драйвер не настроен правильно.
*   **Асинхронность**: `crawl_categories_async` использует асинхронность, но неясно, как она обрабатывается за пределами метода. Необходимо убедиться, что асинхронная функциональность используется корректно.
*   **Гибкость**: `locator` задан статично, что может затруднять работу с сайтами с нестандартной разметкой. Рассмотреть возможность передачи пользовательских локаторов.
*   **Логирование**: Логирование могло бы быть более детальным, включая ошибки при парсинге и запросах к API.

#### Взаимосвязь с другими частями проекта:

*   Модуль `category` зависит от модулей `src.endpoints.prestashop` для работы с API PrestaShop.
*   Использует `src.utils.jjson` для работы с JSON-файлами.
*   Использует `src.logger` для логирования событий.
*   Связан с веб-драйвером selenium, для автоматизации просмотра страниц.