## Анализ кода `hypotez/src/scenario/executor.py`

### 1. <алгоритм>

**Блок-схема:**

```mermaid
graph LR
    A[Начало] --> B{Запуск сценариев};
    B -- Список файлов сценариев --> C[Обработка списка файлов сценариев];
    B --  Один файл сценария --> C;
    C --> D{Цикл по файлам сценариев};
    D -- Для каждого файла --> E[Выполнение сценария из файла];
    E --> F{Загрузка сценариев из JSON};
    F -- Успешно --> G{Цикл по сценариям};
     F -- Ошибка --> H[Логирование ошибки загрузки файла];
    G -- Для каждого сценария --> I[Выполнение сценария];
    I --> J[Получение URL категории];
    J --> K{Проверка списка продуктов};
    K -- Список есть --> L{Цикл по URL продуктов};
     K -- Списка нет --> M[Логирование предупреждения (пустая категория)];
     M--> D
     L --> N[Получение данных продукта];
    N --> O{Создание объекта Product};
    O -- Успешно --> P[Вставка данных продукта в PrestaShop];
     O -- Ошибка --> Q[Логирование ошибки создания продукта];
    P -- Успешно --> L;
    P -- Ошибка --> R[Логирование ошибки вставки];
    Q --> L
    R --> L
   L-- Конец цикла --> D;
    H --> D
     D--Конец цикла --> S[Сохранение журнала];
    S --> T[Конец];
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
     style T fill:#f9f,stroke:#333,stroke-width:2px
```

**Примеры:**

*   **Блок B:** `run_scenario_files(supplier, ['scenario1.json', 'scenario2.json'])` или `run_scenario_files(supplier, Path('scenario1.json'))`
*   **Блок E:** Загрузка сценариев из файла `scenario1.json`
    ```json
        {
          "scenarios": {
            "scenario_name1": {
              "url": "https://example.com/category1"
            },
            "scenario_name2": {
              "url": "https://example.com/category2"
            }
          }
        }
    ```
*   **Блок I:** Выполнение сценария с URL `https://example.com/category1`
*   **Блок J:** Получение списка URL продуктов из категории, например: `['https://example.com/product1', 'https://example.com/product2']`
*   **Блок N:** Получение данных продукта со страницы `https://example.com/product1`, например: `{'name': 'Product 1', 'price': 100, ...}`
*   **Блок O:** Создание объекта `Product` с полями из блока `N`
*   **Блок P:** Вставка данных продукта в PrestaShop

**Поток данных:**

1.  `run_scenario_files` получает список файлов сценариев или один файл.
2.  `run_scenario_files` вызывает `run_scenario_file` для каждого файла.
3.  `run_scenario_file` загружает JSON, содержащий сценарии.
4.  `run_scenario_file` вызывает `run_scenario` для каждого сценария.
5.  `run_scenario` получает URL категории из сценария, переходит на страницу категории.
6.  `run_scenario` использует модули поставщика для получения списка URL продуктов.
7.  `run_scenario` переходит на каждую страницу продукта.
8.  `run_scenario` использует модули поставщика для извлечения данных продукта.
9.  `run_scenario` создает объект `Product` и вызывает `insert_grabbed_data`
10. `insert_grabbed_data` вызывает `execute_PrestaShop_insert` для вставки данных продукта в PrestaShop.
11. `run_scenario_files` сохраняет журнал выполнения.

### 2. <mermaid>

```mermaid
graph LR
    subgraph src.scenario.executor
    A[run_scenario_files(supplier, scenario_files_list)] --> B(run_scenario_file(supplier, scenario_file));
    B --> C{j_loads(scenario_file)};
    C -- scenarios --> D{Цикл по сценариям};
    D --> E(run_scenario(supplier, scenario, scenario_name));
    E --> F[driver.get_url(scenario['url'])];
    F --> G(related_modules.get_list_products_in_category(supplier));
    G --> H{Цикл по list_products_in_category};
    H --> I[driver.get_url(url)];
    I --> J(related_modules.grab_product_page(supplier));
     I --> K(related_modules.grab_page(supplier));
        K --> L{Product(presta_fields_dict)};
    L --> M(insert_grabbed_data(product_fields));
     M --> N(execute_PrestaShop_insert(product_fields));
    end
    
    subgraph src.endpoints.prestashop
        N --> O[PrestaShop.post_product_data()];
    end
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style O fill:#ccf,stroke:#333,stroke-width:2px
```

**Зависимости:**

*   `src.scenario.executor` зависит от:
    *   `src.utils.printer` для вывода сообщений.
    *   `src.utils.jjson` для загрузки и сохранения JSON.
    *   `src.product` для представления данных продукта.
    *   `src.endpoints.prestashop` для вставки данных в PrestaShop.
    *   `src.db` для управления кампаниями продуктов (не используется напрямую в коде, но импортируется).
    *   `src.logger.logger` для логирования.
    *   `src.logger.exceptions` для обработки исключений, связанных с полями продукта.
    *   `header` для, предположительно, настроек.
    *   `src.gs` для получения текущего времени.
    *   `os`, `sys`, `requests`, `asyncio`, `time`, `tempfile`, `datetime`, `math`, `pathlib`, `typing`, `json`. Это стандартные библиотеки языка Python, необходимые для общей функциональности.
*   `src.endpoints.prestashop` зависит от  библиотеки `requests`.

### 3. <объяснение>

**Импорты:**

*   `os`, `sys`, `requests`, `asyncio`, `time`, `tempfile`, `datetime`, `math`, `pathlib`, `typing`, `json`: Стандартные библиотеки Python для работы с ОС, запросами, асинхронностью, временем, файлами, датами, математикой, путями, типами и JSON.
*   `header`: Предположительно, модуль для работы с заголовками.
*   `src.gs`: Модуль, предоставляющий глобальные параметры, здесь используется `gs.now` для получения текущего времени.
*   `src.utils.printer`: Модуль для форматированного вывода (например, `pprint`).
*   `src.utils.jjson`: Модуль для работы с JSON, включая загрузку (`j_loads`) и сохранение (`j_dumps`).
*   `src.product.Product`, `src.product.ProductFields`, `src.product.translate_presta_fields_dict`: Модуль для представления данных продукта. Классы `Product` и `ProductFields` и функция `translate_presta_fields_dict` используются для работы с полями и форматами продуктов.
*   `src.endpoints.prestashop.PrestaShop`: Класс для взаимодействия с API PrestaShop.
*   `src.db.ProductCampaignsManager`: Класс для управления кампаниями продуктов в базе данных (не используется напрямую в текущем коде, но импортируется).
*   `src.logger.logger`: Модуль для логирования событий.
*   `src.logger.exceptions.ProductFieldException`: Класс исключений, связанных с полями продукта.

**Классы:**

*   **`Product`**: Класс, представляющий товар. Содержит атрибуты для хранения данных о продукте (имя, цена, категория и т.д.). Используется для создания объектов товаров из полученных данных.

*   **`ProductFields`**: Класс для представления полей продукта (атрибуты: `presta_fields_dict`, `assist_fields_dict`).
*   **`PrestaShop`**: Класс для взаимодействия с PrestaShop API, включая метод `post_product_data` для отправки данных о продукте в PrestaShop.

**Функции:**

*   `dump_journal(s, journal: dict)`: Сохраняет журнал в JSON файл. Принимает экземпляр поставщика `s` и словарь `journal` в качестве параметров. Создает путь для журнала, используя атрибуты поставщика.

*   `run_scenario_files(s, scenario_files_list: List[Path] | Path) -> bool`: Выполняет список файлов сценариев.  Принимает экземпляр поставщика `s` и список путей `scenario_files_list` (или одиночный путь) к файлам сценариев. Возвращает `True` если все сценарии выполнены успешно, иначе `False`.

*   `run_scenario_file(s, scenario_file: Path) -> bool`: Загружает сценарии из файла. Принимает экземпляр поставщика `s` и путь `scenario_file` к файлу сценария. Загружает JSON, извлекает сценарии и вызывает `run_scenario` для каждого из них. Возвращает `True` если сценарий выполнен, иначе `False`.

*   `run_scenarios(s, scenarios: List[dict] | dict = None, _journal=None) -> List | dict | False`:  Выполняет список сценариев. Принимает экземпляр поставщика `s` и список сценариев `scenarios` (или один сценарий) в виде словарей.  Если `scenarios` не указаны, берет сценарий из `s.current_scenario`. Вызывает `run_scenario` для каждого сценария. Возвращает результат выполнения сценария, в случае ошибки `False`.
    
*   `run_scenario(supplier, scenario: dict, scenario_name: str) -> List | dict | False`: Выполняет полученный сценарий. Принимает экземпляр поставщика `supplier`, словарь сценария `scenario`, и имя сценария `scenario_name`. Получает URL категории из сценария, получает список URL продуктов из категории,  и  получает данные продукта для каждого URL. Создает объект Product и вставляет данные в PrestaShop. Возвращает результат выполнения сценария.
     
*   `insert_grabbed_data(product_fields: ProductFields)`: Вставляет полученные данные продукта в PrestaShop. Принимает экземпляр `ProductFields`. Вызывает `execute_PrestaShop_insert` для вставки данных.
*   `execute_PrestaShop_insert_async(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool`: Асинхронно вызывает `execute_PrestaShop_insert`.
*    `execute_PrestaShop_insert(f: ProductFields, coupon_code: str = None, start_date: str = None, end_date: str = None) -> bool`: Вставляет данные продукта в PrestaShop. Принимает `ProductFields` и параметры для купонов.

**Переменные:**

*   `_journal: dict`: Словарь для хранения данных о выполнении сценариев (журнал).
*   `timestamp`:  Строка с текущим временем.
*   `s`:  Представляет экземпляр поставщика (`supplier`). Используется для доступа к его данным и методам.
*   `scenario_files_list`: Список путей к файлам сценариев.
*   `scenario_file`:  Путь к отдельному файлу сценария.
*   `scenarios_dict`: Словарь, полученный из JSON файла, содержащий все сценарии.
*   `scenario`: Словарь, представляющий отдельный сценарий.
*   `scenario_name`: Строка, представляющая имя сценария.
*   `d`: Драйвер (браузер) поставщика.
*   `list_products_in_category`: Список URL продуктов в категории.
*  `url`: URL страницы продукта.
*   `grabbed_fields`: Словарь, содержащий полученные поля со страницы продукта.
*   `f`: Объект `ProductFields`, содержащий полученные данные продукта.
*   `presta_fields_dict`: Словарь для полей PrestaShop.
*   `assist_fields_dict`: Словарь для вспомогательных полей.
*   `product`: Объект типа `Product`.
*   `ex`: Исключение.
*    `presta`: Объект класса PrestaShop.

**Цепочка взаимосвязей с другими частями проекта:**

1.  **Загрузка сценариев**: `run_scenario_files` вызывает `run_scenario_file`, который использует `j_loads` из `src.utils.jjson` для загрузки JSON данных.
2.  **Получение данных**: `run_scenario` использует методы `get_list_products_in_category` и `grab_product_page` из модулей поставщика для получения данных с веб-страниц.
3.  **Создание продукта**: `run_scenario` создает экземпляр класса `Product` из `src.product` с полученными данными.
4.  **Вставка в PrestaShop**: `insert_grabbed_data` вызывает `execute_PrestaShop_insert`, который создает экземпляр класса `PrestaShop` из `src.endpoints.prestashop` и вызывает `post_product_data` для отправки данных в PrestaShop.
5.  **Логирование**: Используется `src.logger.logger` для записи сообщений об ошибках и успехах.
6.  **Журналирование**: `dump_journal` сохраняет журнал выполнения в файл, используя `j_dumps` из `src.utils.jjson`.

**Потенциальные ошибки и области для улучшения:**

1.  **Обработка ошибок**: В коде есть блоки `try...except`, но их можно сделать более гранулированными, чтобы обрабатывать конкретные ошибки более точно.
2.  **Модульность**: Логику вставки данных в PrestaShop стоит вынести в отдельный класс или модуль (как указано в TODO).
3.  **Управление сценариями**: Можно добавить проверку на наличие данных в `s.current_scenario`, чтобы не вызывать исключения при отсутствии данных.
4.  **Асинхронность**: Использование `asyncio` ограничено. Можно сделать больше операций асинхронными, чтобы увеличить производительность.
5.  **Общий журнал**: Можно добавить более подробное логирование в журнал, например,  какие данные были отправлены в PrestaShop.
6. **`_journal`**: Переменная `_journal` является глобальной, что может вызвать проблемы в многопоточном окружении.
7.  **Параметр `_journal`**: Использование `_journal` как входного параметра с дефолтным значением `None` во многих функциях может привести к путанице, лучше его либо передавать явно, либо вовсе убрать, если он не нужен для обработки внутри функции.

Этот подробный анализ дает полное представление о функциональности и взаимосвязях кода `hypotez/src/scenario/executor.py`.