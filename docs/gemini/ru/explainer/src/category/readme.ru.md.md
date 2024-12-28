## АНАЛИЗ КОДА: `src/category/readme.ru.md`

### 1. **<алгоритм>**

Модуль `Category` предназначен для работы с категориями товаров, в частности для PrestaShop.  Он предоставляет функционал для сбора иерархической структуры категорий сайта, а также для сравнения полученной структуры с сохраненными данными.

**Класс `Category`**:

1. **`__init__`**:
   - Принимает `api_credentials` (учетные данные для API).
   - Создаёт экземпляр родительского класса `PrestaCategory`.
   - Пример: `category = Category(api_credentials={'api_key': 'your_api_key'})`.

2. **`get_parents`**:
    -   Принимает `id_category` (ID категории) и `dept` (глубина).
    -   Использует метод `get_parents` родительского класса `PrestaCategory`.
    -   Возвращает список родительских категорий для указанной категории.
    -   Пример: `parents = category.get_parents(id_category=123, dept=2)`.

3. **`crawl_categories_async`**:
   - Принимает `url` (начальный URL категории), `depth` (глубина обхода), `driver` (экземпляр Selenium WebDriver), `locator` (XPath для ссылок категорий), `dump_file` (путь к файлу для сохранения), `default_category_id`, `category` (словарь категорий, по умолчанию пустой).
   -   Асинхронно обходит страницы категорий, извлекая ссылки на подкатегории с помощью Selenium.
    -    Если глубина > 0, рекурсивно вызывает себя для каждой подкатегории.
   -   Формирует иерархический словарь категорий, где ключ - ID категории, а значение - словарь с `url`, `subcategories` и `depth`.
   -   Сохраняет полученные данные в JSON-файл.
   -   Пример:
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

4. **`crawl_categories`**:
    - Аналогичен `crawl_categories_async`, но является синхронной функцией.
    -   Рекурсивно обходит категории, используя Selenium для поиска ссылок и постройки иерархического словаря категорий.
    - Пример использования аналогичен `crawl_categories_async`, но без `await`.
5. **`_is_duplicate_url`**:
    - Принимает `category` (словарь категорий) и `url` для проверки.
    - Проверяет, есть ли `url` уже в словаре категорий.
    - Возвращает `True`, если URL является дубликатом, иначе `False`.
    - Пример: `is_duplicate = category._is_duplicate_url(category_data, 'https://example.com/category/123')`

**Функция `compare_and_print_missing_keys`**:

1. Принимает `current_dict` (словарь с текущими данными) и `file_path` (путь к файлу с сохраненными данными).
2. Загружает данные из JSON-файла.
3. Сравнивает ключи текущего словаря с ключами словаря из файла.
4. Выводит на печать ключи, которые есть в файле, но отсутствуют в текущем словаре.
5. Пример:
```python
compare_and_print_missing_keys(current_dict=category_data, file_path='saved_categories.json')
```
### 2. **<mermaid>**

```mermaid
flowchart TD
    Start[Начало] --> InitCategory[Инициализация Category]
    InitCategory --> GetParents[Вызов get_parents()]
    GetParents --> PrestaCategoryGetParents[Вызов get_parents() из PrestaCategory]
    PrestaCategoryGetParents --> ReturnParents[Возврат списка родительских категорий]
    ReturnParents --> CrawlCategoriesAsync[Вызов crawl_categories_async()]
    CrawlCategoriesAsync --> DriverInit[Инициализация Selenium WebDriver]
    DriverInit --> CrawlPage[Переход на страницу категории]
    CrawlPage --> FindCategoryLinks[Поиск ссылок на подкатегории по XPath]
    FindCategoryLinks --> LoopThroughLinks[Цикл по найденным ссылкам]
    LoopThroughLinks --> RecursionCheck{Глубина > 0?}
    RecursionCheck -- Yes --> RecursionCall[Рекурсивный вызов crawl_categories_async()]
    RecursionCall --> CrawlPage
    RecursionCheck -- No --> UpdateCategoryData[Обновление словаря категорий]
    UpdateCategoryData --> SaveCategoryData[Сохранение словаря в JSON]
    SaveCategoryData --> ReturnCategoryData[Возврат словаря категорий]
    ReturnCategoryData --> CompareAndPrintMissingKeys[Вызов compare_and_print_missing_keys()]
    CompareAndPrintMissingKeys --> LoadSavedData[Загрузка данных из файла JSON]
    LoadSavedData --> CompareKeys[Сравнение ключей словарей]
    CompareKeys --> PrintMissingKeys[Вывод отсутствующих ключей]
    PrintMissingKeys --> End[Конец]
    
    
   subgraph PrestaShop
    PrestaCategoryGetParents
  end
    
```

**Объяснение `mermaid` диаграммы:**

*   Диаграмма показывает поток выполнения программы от инициализации класса `Category` до сравнения данных и вывода отсутствующих ключей.
*   `InitCategory`: представляет создание экземпляра класса `Category`.
*   `GetParents`:  вызов метода для получения родительских категорий.
*   `PrestaCategoryGetParents`:  показывает, что метод `get_parents` вызывается из родительского класса `PrestaCategory`.
*   `CrawlCategoriesAsync`: отображает асинхронный обход категорий.
*   `DriverInit`: показывает инициализацию веб-драйвера Selenium.
*   `CrawlPage`:  представляет переход к странице категории с использованием Selenium.
*   `FindCategoryLinks`:  отображает поиск ссылок на подкатегории с использованием XPath-локатора.
*   `LoopThroughLinks`: цикл по найденным ссылкам для их обработки.
*   `RecursionCheck`:  проверка условия для рекурсивного вызова.
*   `RecursionCall`:  рекурсивный вызов функции.
*   `UpdateCategoryData`:  обновление словаря категорий.
*   `SaveCategoryData`: сохранение полученных данных в файл JSON.
*   `CompareAndPrintMissingKeys`:  показывает сравнение текущих данных с сохраненными данными.
*   `LoadSavedData`:  загрузка данных из файла JSON.
*   `CompareKeys`: сравнение ключей словарей.
*   `PrintMissingKeys`: вывод отсутствующих ключей.
*   `End`:  конец выполнения программы.

### 3. **<объяснение>**

**Импорты**:

-   `src.endpoints.prestashop.PrestaShop`: Базовый класс для работы с PrestaShop API. `Category` унаследован от `PrestaCategory` который унаследован от `PrestaShop`.
-   `src.endpoints.prestashop.PrestaCategory`: Класс для работы с API категориями PrestaShop, от которого наследуется класс `Category`.
-   `src.utils.jjson.j_loads`: Функция для загрузки данных из JSON файла.
-   `src.utils.jjson.j_dumps`: Функция для сохранения данных в JSON файл.
-   `src.logger.logger`: Модуль для логирования событий.
-   Сторонние модули, как `requests`, `lxml`, `asyncio`, `selenium`, здесь не указаны напрямую в `import`, но упоминаются в зависимостях и используются внутри методов `crawl_categories_async` и `crawl_categories`.

**Класс `Category`**:

-   **Роль**: Класс предназначен для обработки категорий товаров в PrestaShop, включая обход категорий на сайте иерархически.
-   **Атрибуты**: Класс не имеет явно определенных атрибутов, но использует `self.api` унаследованный от родительского класса `PrestaCategory`, который обеспечивает доступ к API PrestaShop.
-   **Методы**:
    -   `__init__(self, api_credentials, *args, **kwargs)`:  Инициализирует объект `Category` с учетными данными API.
    -   `get_parents(self, id_category, dept)`: Получает список родительских категорий для заданной категории. Вызывает метод родительского класса.
    -   `crawl_categories_async(self, url, depth, driver, locator, dump_file, default_category_id, category=None)`: Асинхронно обходит страницы категорий, извлекая ссылки на подкатегории, и строит иерархический словарь.
    -   `crawl_categories(self, url, depth, driver, locator, dump_file, id_category_default, category={})`: Синхронно обходит страницы категорий, строя иерархический словарь.
    -   `_is_duplicate_url(self, category, url)`:  Проверяет, является ли URL дубликатом.

**Функция `compare_and_print_missing_keys`**:
-   **Роль**: Сравнивает словарь категорий с данными из файла и выводит отсутствующие ключи.
-   **Аргументы**:
    -   `current_dict`: Словарь с текущими данными категорий.
    -   `file_path`: Путь к файлу JSON, содержащему сохраненные данные категорий.
-   **Возвращаемые значения**: Функция ничего не возвращает, а выводит отсутствующие ключи в консоль.

**Переменные**:
-   В классе `Category` переменные используются в основном как параметры методов, такие как `url`, `depth`, `driver`, `locator`, `dump_file`, `id_category`, `category`.
-   В функции `compare_and_print_missing_keys` используются `current_dict` и `file_path`.

**Потенциальные ошибки и области для улучшения**:
-   Обработка ошибок:  В коде нет явной обработки ошибок при работе с Selenium и API запросами. Необходимо добавить try-except блоки.
-   Логирование:  Хотя есть импорт `src.logger.logger`, в коде нет явного использования механизма логирования. Необходимо добавить логирование для отслеживания процесса работы программы, ошибок и предупреждений.
-   Асинхронность: Использование `asyncio` подразумевает асинхронное выполнение. Необходимо убедиться, что весь код, вызываемый внутри `crawl_categories_async`, также является асинхронным.
-   `crawl_categories` дублирует функциональность `crawl_categories_async`, только выполняя её синхронно.  Стоит рассмотреть вариант использования асинхронного подхода для всех операций.
-   Дублирование кода:   Методы `crawl_categories_async` и `crawl_categories` имеют много общего кода, который можно вынести в отдельную функцию.
-   XPath локатор: Жестко заданный XPath локатор `//a[@class="category-link"]` может привести к ошибкам, если структура HTML изменится. Лучше использовать более гибкие локаторы или проверять структуру страницы.

**Взаимосвязи с другими частями проекта**:

-   Модуль `Category` использует классы из `src.endpoints.prestashop` для взаимодействия с PrestaShop API.
-   Для загрузки и сохранения данных используется `src.utils.jjson`.
-   Для логирования используются механизмы из `src.logger`.
-   Используются внешние библиотеки `selenium`, `asyncio`, `requests` (хотя напрямую в коде не импортируются, но используются в методах класса `Category`).

Этот анализ предоставляет полное понимание функциональности и структуры кода, включая его взаимодействие с другими частями проекта.