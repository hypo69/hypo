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

**1. `run_scenario_files(s, scenario_files_list)`**

   - **Вход:** Объект `s` (поставщик, supplier) и список `scenario_files_list` (пути к файлам сценариев) или один путь `Path`.
   - **Проверка:** Если `scenario_files_list` является `Path`, преобразуется в список. Если не список, то ошибка `TypeError`.
   - **Инициализация журнала:** Создаётся словарь `_journal`, где будут хранится результаты выполнения сценариев.
   - **Итерация:** Проходит по каждому файлу сценария в `scenario_files_list`.
      - **Выполнение сценария:** Вызывает `run_scenario_file(s, scenario_file)`.
      - **Обработка результатов:**
        - Если выполнение успешно, добавляет сообщение об успехе в журнал и логирует.
        - Если выполнение неудачно, добавляет сообщение о неудаче в журнал и логирует ошибку.
        - При возникновении исключения, записывает ошибку в журнал и логирует её как критическую.
   - **Возврат:** Возвращает `True` в любом случае (логирование и запись в журнал есть всегда).

   *Пример:*

     - Входные данные: `s`, `[Path('scenario1.json'), Path('scenario2.json')]`
     - Вызывает `run_scenario_file` для каждого файла
     - Записывает результат и логи в `_journal`
     - Возвращает `True`
     
**2. `run_scenario_file(s, scenario_file)`**

   - **Вход:** Объект `s` (поставщик) и `scenario_file` (путь к файлу сценария).
   - **Загрузка сценариев:** Загружает сценарии из JSON-файла (`j_loads(scenario_file)`) по ключу `scenarios`.
   - **Итерация:** Проходит по каждому сценарию в словаре, где ключ - `scenario_name` (имя сценария), значение - `scenario` (словарь сценария).
      - **Настройка текущего сценария:** Записывает в `s.current_scenario` текущий сценарий.
      - **Выполнение сценария:** Вызывает `run_scenario(s, scenario, scenario_name)`.
      - **Обработка результатов:** Логирует успех или неудачу выполнения сценария.
   - **Обработка исключений:** Если файл не найден или JSON недействителен, ловит исключения, логирует и возвращает `False`.
   - **Возврат:** Возвращает `True` при успешном выполнении всех сценариев, иначе `False`.

   *Пример:*

     - Входные данные: `s`, `Path('scenario1.json')`
     - Загружает JSON, получает `scenarios`
     - Вызывает `run_scenario` для каждого сценария
     - Возвращает `True` или `False` в зависимости от результата

**3.  `run_scenarios(s, scenarios, _journal)`**

  - **Вход:** Объект `s` (поставщик), `scenarios` (список или словарь сценариев, по умолчанию - None), `_journal` (словарь журнала, по умолчанию None).
  - **Обработка отсутствия сценариев:** Если `scenarios` не предоставлены, берёт сценарий из `s.current_scenario`.
  - **Преобразование в список:** Если `scenarios` - словарь, преобразует его в список.
  - **Итерация:** Проходит по каждому `scenario` в `scenarios`.
     - **Выполнение сценария:** Вызывает `run_scenario(s, scenario)`.
     - **Запись результата:** Записывает результат выполнения сценария в журнал `_journal` и в файл, вызывая функцию `dump_journal`.
  - **Возврат:** Возвращает результат выполнения последнего сценария.

   *Пример:*

     - Входные данные: `s`, `[{'url': 'url1'}, {'url': 'url2'}]`, `_journal`
     - Вызывает `run_scenario` для каждого сценария
     - Записывает результат в `_journal` и в файл
     - Возвращает результат последнего сценария

**4. `run_scenario(supplier, scenario, scenario_name, _journal)`**

   - **Вход:** Объект `supplier` (поставщик), `scenario` (словарь с информацией о сценарии), `scenario_name` (имя сценария), `_journal` (журнал).
   - **Логирование начала сценария:** Логирует начало выполнения сценария.
   - **Настройка текущего сценария:** Записывает текущий сценарий в `s.current_scenario`.
   - **Переход на URL:** Переходит по URL, указанному в сценарии (`d.get_url(scenario['url'])`).
   - **Сбор списка продуктов:** Получает список URL продуктов в категории с помощью `s.related_modules.get_list_products_in_category(s)`.
   - **Проверка наличия продуктов:** Если список продуктов пуст, логгирует предупреждение и возвращает управление.
   - **Итерация по продуктам:** Проходит по каждому URL продукта в списке `list_products_in_category`.
      - **Переход на страницу продукта:** Переходит на страницу продукта (`d.get_url(url)`).
      - **Сбор данных о продукте:** Собирает данные о продукте с помощью `s.related_modules.grab_product_page(s)`.
      - **Асинхронный сбор полей:** Выполняет асинхронный сбор полей с помощью `asyncio.run(s.related_modules.grab_page(s))`.
      - **Обработка полей:** Если сбор полей не удался, логгирует ошибку и переходит к следующему продукту.
      - **Создание объекта Product:** Создаёт объект `Product` на основе собранных данных.
      - **Вставка данных:** Вставляет собранные данные в PrestaShop, вызывая функцию `insert_grabbed_data(f)`.
      - **Обработка ошибок:** Логгирует ошибки сохранения продукта.
   - **Возврат:** Возвращает список URL продуктов, которые были обработаны.

    *Пример:*

     - Входные данные: `supplier`, `{'url': 'url'}, 'test_scenario'`
     - Логгирует начало
     - Открывает URL
     - Получает список продуктов
     - Собирает данные каждого продукта и вызывает `insert_grabbed_data`
     - Возвращает список URL продуктов

**5. `insert_grabbed_data(product_fields)`**
   - **Вход:** `product_fields` (объект `ProductFields` с данными о продукте).
   - **Выполнение вставки в PrestaShop:** Выполняет асинхронную вставку данных в PrestaShop с помощью `asyncio.run(execute_PrestaShop_insert(product_fields))`.

   *Пример:*
   
    - Входные данные: `ProductFields`
    - Вызывает `execute_PrestaShop_insert` асинхронно

**6.  `execute_PrestaShop_insert_async(f, coupon_code, start_date, end_date)`**
  - **Вход:** `f` (объект `ProductFields`), `coupon_code` (опциональный код купона), `start_date` (опциональная дата начала), `end_date` (опциональная дата окончания).
  - **Асинхронный вызов:** Асинхронно вызывает `execute_PrestaShop_insert` с переданными параметрами.
  - **Возврат:** Возвращает результат работы `execute_PrestaShop_insert`.
  
   *Пример:*
   
    - Входные данные: `ProductFields`, 'coupon123', '01.01.2024', '31.12.2024'
    - Асинхронно вызывает `execute_PrestaShop_insert`
    
**7. `execute_PrestaShop_insert(f, coupon_code, start_date, end_date)`**
    - **Вход:** `f` (объект `ProductFields`), `coupon_code` (опциональный код купона), `start_date` (опциональная дата начала), `end_date` (опциональная дата окончания).
    - **Инициализация PrestaShop:** Создает экземпляр класса `PrestaShop`.
    - **Вставка продукта:** Вызывает метод `post_product_data` объекта `presta` для вставки данных о продукте в PrestaShop.
    - **Обработка ошибок:** Перехватывает исключения и логирует ошибки.
    - **Возврат:** Возвращает `True` в случае успеха и `False` в случае ошибки.
    
    *Пример:*
    
     - Входные данные: `ProductFields`, 'coupon123', '01.01.2024', '31.12.2024'
     - Создает объект `PrestaShop`
     - Вызывает `post_product_data`
     - Возвращает `True` или `False` в зависимости от результата
     
## <mermaid>

```mermaid
flowchart TD
    Start[Start] --> RunScenarioFiles{run_scenario_files<br>(s, scenario_files_list)};
    RunScenarioFiles -- For each scenario file --> RunScenarioFile{run_scenario_file<br>(s, scenario_file)};
    RunScenarioFile --> LoadScenarios{Load scenarios<br>from scenario file}
    LoadScenarios -- For each scenario --> RunScenario{run_scenario<br>(supplier, scenario, scenario_name)};
    RunScenario --> GetURL{d.get_url<br>(scenario['url'])};
    GetURL --> GetProductList{get_list_products_in_category<br>(s)};
    GetProductList -- if Product list is empty --> EmptyCategory[Log warning<br>and return];
    GetProductList -- if Product list is not empty --> LoopProducts{For each product URL<br>in product list};
    LoopProducts -- Get product url--> GetProductURL{d.get_url<br>(url)};
    GetProductURL --> GrabProductPage{grab_product_page<br>(s)};
    GrabProductPage --> GrabPageAsync{asyncio.run<br>(grab_page(s))};
    GrabPageAsync -- if product fields are empty --> LogError[Log error<br>and continue];
    GrabPageAsync -- if product fields are not empty --> CreateProduct{Create Product<br>object};
    CreateProduct --> InsertData{insert_grabbed_data<br>(f)};
    InsertData --> ExecutePrestaShopInsertAsync{execute_PrestaShop_insert_async<br>(f, coupon_code, start_date, end_date)};
    ExecutePrestaShopInsertAsync --> ExecutePrestaShopInsert{execute_PrestaShop_insert<br>(f, coupon_code, start_date, end_date)};
    ExecutePrestaShopInsert --> PrestaShopPost{presta.post_product_data<br>(product_data)};
    PrestaShopPost -- Success --> ReturnTrue[Return True]
    PrestaShopPost -- Error --> LogPrestaShopError[Log error]
    LogPrestaShopError --> ReturnFalse[Return False];
    ReturnFalse --> LoopProducts;
    ReturnTrue --> LoopProducts;
    LogError --> LoopProducts;
    LoopProducts -- End of product list--> ReturnProductList[Return list_products_in_category]
    ReturnProductList --> RunScenarioFile
    EmptyCategory --> RunScenarioFile
    RunScenarioFile -- Success --> LogSuccessScenario[Log scenario success]
    RunScenarioFile -- Failure --> LogFailScenario[Log scenario failure]
    LogSuccessScenario --> RunScenarioFiles
    LogFailScenario --> RunScenarioFiles
    RunScenarioFiles --> End[End]
```
```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]
    
        Header --> import[Import Global Settings: <br><code>from src import gs</code>] 
    ```

### Зависимости `mermaid`:

1.  **`Start`**: Начало процесса выполнения сценариев.
2.  **`RunScenarioFiles`**: Функция `run_scenario_files`, управляющая выполнением файлов сценариев. Она принимает объект `s` (поставщик) и список путей к файлам сценариев `scenario_files_list`.
3.  **`RunScenarioFile`**: Функция `run_scenario_file`, загружающая и выполняющая сценарии из файла. Она принимает объект `s` и путь к файлу сценария `scenario_file`.
4.  **`LoadScenarios`**: Этап загрузки сценариев из файла, который возвращает словарь с `scenarios`.
5.  **`RunScenario`**: Функция `run_scenario`, выполняющая один сценарий. Она принимает объект `supplier`, `scenario` и имя сценария `scenario_name`.
6.  **`GetURL`**: Переход на URL, указанный в сценарии, вызывая `d.get_url(scenario['url'])`, где `d` - объект драйвера.
7.  **`GetProductList`**: Получение списка URL продуктов в категории с помощью `s.related_modules.get_list_products_in_category(s)`.
8.  **`EmptyCategory`**: Логирование предупреждения и выход из сценария, если список продуктов пуст.
9.  **`LoopProducts`**: Цикл, проходящий по списку URL продуктов `list_products_in_category`.
10. **`GetProductURL`**:  Переход на URL продукта с помощью `d.get_url(url)`.
11. **`GrabProductPage`**: Вызов метода для сбора данных со страницы продукта с помощью `s.related_modules.grab_product_page(s)`.
12. **`GrabPageAsync`**:  Асинхронный сбор полей продукта с помощью `asyncio.run(s.related_modules.grab_page(s))`.
13. **`LogError`**: Логирование ошибки, если не удалось собрать поля продукта.
14. **`CreateProduct`**: Создание объекта `Product` на основе собранных данных.
15. **`InsertData`**: Вызов функции `insert_grabbed_data(f)` для вставки данных продукта в PrestaShop.
16.  **`ExecutePrestaShopInsertAsync`**: Вызов асинхронной функции `execute_PrestaShop_insert_async`, которая вызывает `execute_PrestaShop_insert` для вставки данных в PrestaShop.
17.  **`ExecutePrestaShopInsert`**: Функция `execute_PrestaShop_insert`, выполняющая вставку данных о продукте в PrestaShop.
18. **`PrestaShopPost`**: Вызов метода `post_product_data` объекта `presta` для вставки данных в PrestaShop.
19.  **`ReturnTrue`**: Возврат `True` после успешной вставки в PrestaShop.
20. **`LogPrestaShopError`**: Логирование ошибки, если не удалось вставить данные в PrestaShop.
21. **`ReturnFalse`**: Возврат `False` после неудачной вставки в PrestaShop.
22. **`ReturnProductList`**: Возврат списка URL продуктов, которые были обработаны в цикле.
23. **`LogSuccessScenario`**: Логирование успешного выполнения сценария.
24. **`LogFailScenario`**: Логирование неудачного выполнения сценария.
25. **`End`**: Конец процесса выполнения сценариев.
 
Все эти компоненты и зависимости работают вместе, чтобы загрузить, выполнить сценарии и вставить данные о продуктах в PrestaShop.

## <объяснение>

**Импорты:**

*   **`os`, `sys`**: Стандартные модули Python для работы с операционной системой и интерпретатором.
*   **`requests`**: Библиотека для выполнения HTTP-запросов (не используется напрямую в коде, возможно используется в других модулях).
*   **`asyncio`**: Библиотека для асинхронного программирования.
*   **`time`**: Модуль для работы со временем.
*   **`tempfile`**: Модуль для работы с временными файлами.
*   **`datetime`**: Модуль для работы с датами и временем.
*   **`math`**: Модуль для математических функций.
*   **`pathlib.Path`**: Класс для работы с путями файлов.
*   **`typing.Dict`, `typing.List`**: Модули для объявления типов.
*   **`json`**: Модуль для работы с JSON.

*   **`header`**: Локальный модуль для определения корневой директории проекта (инициализирует `gs` глобальные настройки)
*   **`src.gs`**: Глобальные настройки проекта.
*   **`src.utils.printer.pprint`**: Функция для удобного вывода в консоль (для отладки).
*   **`src.utils.jjson.j_loads`, `src.utils.jjson.j_dumps`**: Функции для загрузки и сохранения JSON с помощью `orjson`
*   **`src.product.Product`, `src.product.ProductFields`, `src.product.translate_presta_fields_dict`**: Классы и функции для работы с продуктами.
*   **`src.endpoints.prestashop.PrestaShop`**: Класс для работы с API PrestaShop.
*   **`src.db.ProductCampaignsManager`**: Класс для работы с базой данных (кампании продуктов)
*   **`src.logger.logger.logger`**: Объект для логирования.
*   **`src.logger.exceptions.ProductFieldException`**: Пользовательское исключение для полей продукта.

**Классы:**

*   **`Product`**: Представляет продукт, содержит поля продукта (`fields`, `supplier_prefix`). Используется для создания объектов продуктов из данных.
*   **`ProductFields`**:  Класс для хранения полей продукта.
*   **`PrestaShop`**: Класс для взаимодействия с PrestaShop API. Отвечает за отправку данных о продукте.
*   **`ProductCampaignsManager`**:  Класс для управления кампаниями продуктов в базе данных.

**Функции:**

*   **`dump_journal(s, journal)`**: Сохраняет данные журнала в JSON-файл.
    *   `s`: Объект поставщика.
    *   `journal`: Словарь с данными журнала.
*   **`run_scenario_files(s, scenario_files_list)`**: Запускает сценарии из списка файлов.
    *   `s`: Объект поставщика.
    *   `scenario_files_list`: Список путей к файлам сценариев.
    *   Возвращает `True` в случае успешного выполнения всех сценариев.
*   **`run_scenario_file(s, scenario_file)`**: Загружает и выполняет сценарии из одного файла.
    *   `s`: Объект поставщика.
    *   `scenario_file`: Путь к файлу сценария.
    *   Возвращает `True` при успешном выполнении, `False` при ошибке загрузки.
*   **`run_scenarios(s, scenarios, _journal)`**:  Выполняет список сценариев (не из файлов).
    *    `s`: Объект поставщика.
    *    `scenarios`: Список или словарь сценариев.
    *    `_journal`: Словарь с данными журнала
    *   Возвращает результат последнего выполнения сценария или `False` в случае ошибки.
*   **`run_scenario(supplier, scenario, scenario_name, _journal)`**: Выполняет один сценарий.
    *   `supplier`: Объект поставщика.
    *   `scenario`: Словарь с данными сценария.
    *   `scenario_name`: Имя сценария.
    *    `_journal`: Словарь с данными журнала
    *   Возвращает список URL продуктов.
*   **`insert_grabbed_data(product_fields)`**: Вставляет данные о продукте в PrestaShop.
    *   `product_fields`: Объект `ProductFields` с данными продукта.
*   **`execute_PrestaShop_insert_async(f, coupon_code, start_date, end_date)`**: Асинхронно вставляет данные о продукте в PrestaShop.
     *   `f`: Объект `ProductFields`.
     *   `coupon_code`: Код купона.
     *    `start_date`: Дата начала акции.
     *    `end_date`: Дата окончания акции.
*   **`execute_PrestaShop_insert(f, coupon_code, start_date, end_date)`**: Вставляет данные о продукте в PrestaShop.
     *   `f`: Объект `ProductFields`.
     *   `coupon_code`: Код купона.
     *    `start_date`: Дата начала акции.
     *    `end_date`: Дата окончания акции.
     *    Возвращает `True` или `False` в зависимости от результата.

**Переменные:**

*   **`_journal`**: Словарь для хранения данных о выполнении сценариев (название, список файлов, результат).
*   **`timestamp`**: Текущее время, используется для генерации имени файла журнала.

**Потенциальные ошибки и области для улучшения:**

1.  **Обработка ошибок:**
    *   Хотя код логирует ошибки, стоит добавить более детальную обработку исключений, например, с помощью `try-except-finally` конструкций.
    *   Необходимо проверять наличие всех необходимых полей в данных, прежде чем создавать объект `Product`.
2.  **Асинхронность:**
    *   Необходимо проверить реализацию асинхронности.
    *   `asyncio.run` используется везде.
3.  **Модульность:**
    *   Функцию `insert_grabbed_data` можно вынести в отдельный модуль или в класс `PrestaShop` для лучшей организации кода.
    *   Логику получения данных со страниц и работу с драйвером следует абстрагировать в отдельные классы.
4.  **`run_scenarios`:**
     *   Функция `run_scenarios` может возвращать только результат последнего сценария. Необходимо возвращать список результатов всех сценариев
     *   Реализация когда нет сценариев не отлажена
5. **`run_scenario`:**
     *   Необходимо разобраться с необходимостью `scenario_name`
     *   Необходимо передавать журнал `_journal` в функции для корректной записи.

**Взаимосвязь с другими частями проекта:**

*   **`header.py`**: Определяет корневую директорию проекта, что необходимо для импорта других модулей. Инициализирует `gs`.
*   **`src.gs`**: Содержит глобальные настройки проекта, такие как URL PrestaShop, API-ключи, параметры драйвера, пути к файлам и т.д.
*   **`src.product`**: Содержит классы и функции для работы с данными продуктов, включая структуру данных для вставки в PrestaShop.
*   **`src.endpoints.prestashop`**: Отвечает за взаимодействие с PrestaShop API.
*   **`src.db`**: Может отвечать за взаимодействие с БД.
*   **`src.logger`**: Обеспечивает логирование действий и ошибок.
*   **`src.utils`**:  Предоставляет вспомогательные функции, такие как работа с JSON и вывод в консоль.
*   **`src.related_modules`**: Отвечает за работу драйвера браузера и сбор данных со страниц (отдельный модуль, как правило у поставщика).