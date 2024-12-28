## <алгоритм>

1.  **`get_list_products_in_category(s)`**:
    *   Принимает экземпляр поставщика `s`.
    *   Вызывает `get_prod_urls_from_pagination(s)` для получения списка URL товаров.
    *   Возвращает список URL товаров.

    Пример:
    `s` = экземпляр `Supplier`
    `get_list_products_in_category(s)`  ->  `get_prod_urls_from_pagination(s)` -> `['url1', 'url2', 'url3']`

2.  **`get_prod_urls_from_pagination(s)`**:
    *   Принимает экземпляр поставщика `s`.
    *   Извлекает драйвер `_d` и локаторы `_l` из `s`.
    *   Использует `_d.execute_locator(_l)` для получения списка URL товаров со страницы.
    *   Если список пуст, возвращает пустой список.
    *   В цикле:
        *   Проверяет наличие кнопки "следующая страница" с помощью `_d.execute_locator(s.locators['category']['pagination']['->'])`.
        *   Если кнопки нет, выходит из цикла.
        *   Если кнопка есть, добавляет URL товаров со следующей страницы в общий список.
    *   Возвращает список URL товаров.

    Пример:
    `s` = экземпляр `Supplier`
    Начальная страница: `['url1', 'url2']`
    Кнопка "следующая страница" есть
    Следующая страница: `['url3', 'url4']`
    Результат: `['url1', 'url2', 'url3', 'url4']`

3.  **`update_categories_in_scenario_file(s, scenario_filename)`**:
    *   Принимает экземпляр поставщика `s` и имя файла сценария `scenario_filename`.
    *   Загружает JSON из файла сценария.
    *   Извлекает список категорий из файла сценария (`scenarios_in_file`).
    *   Получает список категорий с сайта (`categoris_on_site`).
    *   Обновляет `all_ids_in_file` из сценария:
        *   Извлекает 'category ID on site' или генерирует его из URL, если отсутствует.
    *   Загружает JSON категорий магазина с сайта.
    *   Сравнивает идентификаторы категорий из файла и с сайта:
        *   Создает `all_ids_on_site` и `all_categories_on_site` из JSON с сайта.
        *   Находит `removed_categories` (категории из файла, которых нет на сайте).
        *   Находит `added_categories` (категории с сайта, которых нет в файле).
    *   Если есть `added_categories`:
        *   Добавляет новые категории в файл сценария.
        *   Отправляет уведомление о добавлении категорий.
    *   Если есть `removed_categories`:
        *   Отключает удаленные категории в файле сценария.
        *   Отправляет уведомление об отключении категорий.
    *   Возвращает `True`.

    Пример:
    `scenario_filename` = "example.json"
    Файл: `{'scenarios': {'cat1': {'category ID on site': 101}, 'cat2': {'category ID on site': 102}}, 'store': {'shop categories json file': 'url'}}`
    С сайта: `{'groups': [{'groupId': 101, 'subGroupList': []}, {'groupId': 103, 'subGroupList': []}]}`
    Результат: `removed_categories = [102], added_categories = [103]`

4.  **`get_list_categories_from_site(s, scenario_file, brand)`**:
    *   Принимает экземпляр поставщика `s`, имя файла сценария `scenario_file` и бренд `brand`.
    *   Загружает JSON из файла сценария.
    *   Переходит на страницу категорий магазина.
    *   Возвращает список категорий

    Пример:
    `s` = экземпляр `Supplier`,
    `scenario_file` = `example.json`,
    `brand` = ""
    Загружает `example.json`
    Переходит на `scenario_json['store']['shop categories page']`

5.  **`DBAdaptor`**:
    *   Содержит методы для взаимодействия с базой данных через `CategoryManager`.
    *   `select()`: Пример запроса на выборку записей.
    *   `insert()`: Пример вставки новой записи.
    *   `update()`: Пример обновления записи.
    *   `delete()`: Пример удаления записи.

    Пример:
    `DBAdaptor.insert()` -> `manager.insert_record(AliexpressCategory, fields)`

## <mermaid>

```mermaid
flowchart TD
    subgraph get_list_products_in_category
        A[Start: get_list_products_in_category(s)] --> B{Call get_prod_urls_from_pagination(s)};
        B --> C[Return product URLs];
        C --> D[End: Return list of product URLs];
    end

    subgraph get_prod_urls_from_pagination
    
        E[Start: get_prod_urls_from_pagination(s)] --> F[Extract driver(_d) and locators(_l) from s];
        F --> G{Execute locator (_d.execute_locator(_l))};
        G --> H{Is result empty?};
        H -- Yes --> I[Return empty list];
        H -- No --> J[While loop: pagination check];
        J --> K{Check for next page button: _d.execute_locator(s.locators['category']['pagination']['->'])};
        K -- No --> L[Break loop];
        K -- Yes --> M{Extend product URL list:  list_products_in_category.extend(_d.execute_locator(_l))};
        M --> J;
        L --> N[Return product URLs];
        N --> O[End: Return list of product URLs];
    end

     subgraph update_categories_in_scenario_file
        P[Start: update_categories_in_scenario_file(s, scenario_filename)] --> Q[Load scenario JSON];
        Q --> R[Get categories from file];
        R --> S[Get categories from site];
        S --> T[Update IDs in file];
         T --> U[Load shop categories JSON from site];
         U --> V{Compare file IDs and site IDs};
         V --> W{Find added categories};
         W --> X{Find removed categories};
         X --> Y{If Added categories: Update File and send msg};
         Y --> Z{If Removed categories: Update File and send msg};
         Z --> AA[Return True];
        AA --> BB[End: Function execution complete];

     end

    subgraph get_list_categories_from_site
        CC[Start: get_list_categories_from_site(s,scenario_file,brand)] --> DD[Load scenario JSON]
        DD --> EE[Go to shop categories page]
        EE --> FF[Return list of categories]
        FF --> GG[End: Return list categories];
    end

 subgraph DBAdaptor
    HH[Start: DBAdaptor operations] --> II[select()]
    II --> JJ[manager.select_record()]
     HH --> KK[insert()]
    KK --> LL[manager.insert_record()]
     HH --> MM[update()]
    MM --> NN[manager.update_record()]
     HH --> OO[delete()]
    OO --> PP[manager.delete_record()]
   PP --> QQ[End: DB operations complete];

end


    classDef green fill:#90EE90,stroke:#333,stroke-width:2px
    class A,E,P,CC,HH green
     class D,O,BB,GG,QQ green
```

**Анализ зависимостей `mermaid`:**

*   `get_list_products_in_category`: Вызывает `get_prod_urls_from_pagination`.
*   `get_prod_urls_from_pagination`: Использует `_d.execute_locator` для навигации по страницам и сбора URL.
*   `update_categories_in_scenario_file`: Загружает JSON, сравнивает данные, обновляет файл и отправляет уведомления.
*    `get_list_categories_from_site`: Загружает JSON и переходит по ссылке.
*   `DBAdaptor`: Использует `CategoryManager` для взаимодействия с базой данных.

## <объяснение>

### Импорты:

*   `from typing import Union`: Используется для аннотации типов, позволяя указывать, что переменная может принимать значение одного из нескольких типов. В данном коде не используется.
*   `from pathlib import Path`:  Предоставляет класс `Path` для работы с путями к файлам и директориям.
*   `from src import gs`: Импортирует глобальные настройки из модуля `src.gs`. `gs` содержит общие настройки проекта, такие как пути к директориям и учетные данные для базы данных.
*   `from src.utils.jjson import j_dumps, j_loads`: Импортирует функции для работы с JSON: `j_dumps` для сериализации объектов в JSON, `j_loads` для десериализации JSON в объекты.
*   `from src.logger.logger import logger`: Импортирует объект `logger` для записи сообщений в лог.
*   `from src.db.manager_categories.suppliers_categories import CategoryManager, AliexpressCategory`: Импортирует `CategoryManager` для работы с категориями в базе данных и `AliexpressCategory` как модель для таблицы категорий aliexpress.
*   `import requests`: Импортирует библиотеку requests для выполнения HTTP-запросов.

### Классы:

*   **`DBAdaptor`**:
    *   **Роль**: Адаптер для работы с базой данных. Предоставляет абстрактный интерфейс для выполнения CRUD-операций (Create, Read, Update, Delete) с таблицей `AliexpressCategory` через `CategoryManager`.
    *   **Методы**:
        *   `select(cat_id, parent_id, project_cat_id)`:  Пример метода выборки записей из базы данных.
        *   `insert()`: Пример метода вставки записей в базу данных.
        *   `update()`: Пример метода обновления записей в базе данных.
        *   `delete()`: Пример метода удаления записей из базы данных.
    *   **Взаимодействие**: Взаимодействует с классом `CategoryManager` для выполнения операций с БД.
    *   **Атрибуты**: Нет.

### Функции:

*   **`get_list_products_in_category(s) -> list[str, str]`**:
    *   **Аргументы**:
        *   `s`: Экземпляр класса `Supplier`, содержащий данные поставщика, включая веб-драйвер и локаторы.
    *   **Возвращаемое значение**:
        *   `list[str, str]`: Список URL-адресов товаров в категории.
    *   **Назначение**: Получает список URL товаров из текущей категории, делегируя работу функции `get_prod_urls_from_pagination`.
    *   **Пример**: `get_list_products_in_category(supplier_instance)`
*   **`get_prod_urls_from_pagination(s) -> list[str]`**:
    *   **Аргументы**:
        *   `s`: Экземпляр класса `Supplier`, содержащий данные поставщика, включая веб-драйвер и локаторы.
    *   **Возвращаемое значение**:
        *   `list[str]`: Список URL-адресов товаров, найденных на страницах категории.
    *   **Назначение**: Собирает все URL товаров со страниц категории, переходя по страницам с пагинацией.
    *   **Пример**: `get_prod_urls_from_pagination(supplier_instance)`
*   **`update_categories_in_scenario_file(s, scenario_filename) -> bool`**:
    *   **Аргументы**:
        *   `s`: Экземпляр класса `Supplier`.
        *   `scenario_filename`: Имя файла сценария.
    *   **Возвращаемое значение**:
        *   `bool`: Возвращает `True` после завершения процесса.
    *   **Назначение**: Сверяет категории в файле сценария с категориями на сайте, добавляет новые и отключает удаленные, отправляя уведомления об изменениях.
    *   **Пример**: `update_categories_in_scenario_file(supplier_instance, "scenario1.json")`
*   **`get_list_categories_from_site(s, scenario_file, brand='')`**:
    *   **Аргументы**:
        *   `s`: Экземпляр класса `Supplier`.
        *    `scenario_file`: Имя файла сценария.
        *   `brand`: Бренд(не используется).
    *   **Возвращаемое значение**:
         *  `None`
    *   **Назначение**: Загружает файл сценария, переходит на страницу категорий магазина.
    *   **Пример**: `get_list_categories_from_site(supplier_instance, "scenario1.json")`

### Переменные:

*   `credentials`: Глобальные учетные данные для базы данных, взятые из `gs`.
*   `manager`: Экземпляр класса `CategoryManager`, используемый для работы с категориями в БД.
*   `_d`:  Вебдрайвер.
*   `_l`: Локаторы.
*   `list_products_in_category`: Список URL товаров.
*    `scenario_json`: JSON данные из файла сценария.
*   `scenarios_in_file`: Список категорий из файла сценария.
*   `categoris_on_site`: Список категорий, полученных с сайта.
*   `all_ids_in_file`: Список ID категорий из файла сценария.
*   `categories_from_aliexpress_shop_json`: JSON данные категорий из магазина aliexpress.
*   `groups`: Список групп категорий с сайта.
*   `all_ids_on_site`: Список ID категорий с сайта.
*   `all_categories_on_site`: Список категорий с сайта в виде словаря.
*   `removed_categories`: Список категорий, удаленных с сайта, но присутствующих в файле.
*   `added_categories`: Список категорий, добавленных на сайт, но отсутствующих в файле.
*    `category_id`: ID категории.
*   `category`: Информация о категории.
*   `category_name`: Название категории.
*   `category_url`: URL категории.
*   `categories_in_file`: Список категорий в файле.
*   `post_subject`: Тема сообщения.
*   `post_message`: Текст сообщения.

### Потенциальные ошибки и области для улучшения:

*   **Бесконечный цикл в `get_prod_urls_from_pagination`**:  В цикле `while True` есть комментарий `@todo Опасная ситуация здесь/ Могу уйти в бесконечный цикл`. Необходимо добавить условие или счетчик для предотвращения бесконечного цикла, если кнопка "следующая страница" перестанет быть доступной, или при возникновении другой ошибки.
*   **Обработка ошибок**: В функции `update_categories_in_scenario_file` существует баг, когда не происходит корректная обработка ошибки чтения json файла категорий магазина.
*   **Исключения при доступе к элементам JSON**: Код предполагает наличие определенных ключей в JSON-объектах. Нужно добавить проверку на существование ключей, прежде чем к ним обращаться, чтобы избежать `KeyError` исключений.
*   **`get_list_categories_from_site` не возвращает значение:** Функция `get_list_categories_from_site` не возвращает никакого значения, только переходит по ссылке.
*    **Типы данных**: В `DBAdaptor`  необходимо устанавливать типы для передаваемых параметров.
*   **Логирование**: Использовать логгер для отладки и мониторинга.

### Взаимосвязи с другими частями проекта:

*   Использует глобальные настройки из `src.gs`.
*   Использует JSON-парсер `j_loads` и `j_dumps` из `src.utils.jjson`.
*   Использует логгер из `src.logger.logger`.
*   Работает с категориями через `CategoryManager` и модель `AliexpressCategory` из `src.db.manager_categories.suppliers_categories`.
*   Взаимодействует с веб-драйвером через экземпляр `Supplier` (предполагается, что этот класс определен в другом месте проекта).
*   Отправка сообщений `send` предполагает наличие функции send вне текущего файла.
*   Использует  библиотеку `requests` для загрузки json с сайта.
*   Использует `Path` из библиотеки `pathlib` для работы с путями к файлам.