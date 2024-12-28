## АНАЛИЗ КОДА `hypotez/src/suppliers/ivory/__morlevi__.py`

### <алгоритм>

1.  **`login(supplier)`**:
    *   Принимает объект `supplier` в качестве аргумента.
    *   Получает WebDriver из `supplier.driver` и загружает главную страницу `https://www.morlevi.co.il`.
    *   Вызывает внутреннюю функцию `_login(supplier)` для выполнения процесса авторизации.
    *   Если авторизация прошла успешно, возвращает `True`.
    *   В случае ошибки, пытается закрыть модальные окна, если они есть:
        *   Обновляет страницу.
        *   Повторно вызывает `_login(supplier)`.
        *   Ищет кнопку закрытия модального окна через `supplier.locators['login']['close_pop_up_locator']`.
        *   Если найдено несколько кнопок, перебирает их и пытается нажать на каждую, после каждой попытки вызывая `_login(supplier)`.
        *   Если найдена одна кнопка, нажимает её и вызывает `_login(supplier)`.
    *   В случае ошибки во время закрытия окон, регистрирует ошибку в логе и возвращает `None`.
2.  **`_login(_s)`**:
    *   Принимает объект `supplier` как `_s`.
    *   Обновляет страницу.
    *   Извлекает локаторы для логина из `_s.locators['login']`.
    *   Находит и заполняет поля email и password, а также нажимает кнопку входа, используя локаторы.
    *   В случае успеха, регистрирует в логе успешный вход и возвращает `True`.
    *   В случае ошибки, регистрирует в логе ошибку и возвращает `None`.
3.  **`grab_product_page(s)`**:
    *   Создает объект `Product` с переданным объектом `supplier`.
    *   Извлекает локаторы для продукта из `s.locators['product']`.
    *   Закрывает модальное окно, если оно есть.
    *   Определяет внутренние функции `set_id()`, `set_sku_suppl()`, `set_sku_prod()`, `set_title()`, `set_summary()`, `set_description()`, `set_cost_price()`, `set_before_tax_price()`, `set_delivery()`, `set_images()`, `set_combinations()`, `set_qty()`, `set_specification()`, `set_customer_reviews()`, `set_supplier()`, `set_rewritted_URL()` для заполнения полей товара.
        *   `set_id()`: Извлекает `id` (артикул) продукта, если он является списком, то берет первый элемент, и так же делает замену пробела в URL.
        *   `set_sku_suppl()`: Записывает `id` в поле `sku suppl`.
        *   `set_sku_prod()`:  Формирует поле `sku` добавив префикс `mlv-` к `id`.
        *   `set_title()`: Извлекает заголовок страницы.
        *   `set_summary()`: Извлекает краткое описание продукта.
        *   `set_description()`: Извлекает полное описание продукта.
        *   `set_cost_price()`: Извлекает цену продукта, очищает её и применяет правило ценообразования из настроек.
        *   `set_before_tax_price()`: устанавливает цену без налога.
        *   `set_delivery()`:  (TODO) перенести в комбинации.
        *   `set_images()`: Извлекает URL изображения продукта.
        *   `set_combinations()`: (TODO)
        *   `set_qty()`: (TODO)
        *    `set_specification()`: Извлекает название товара.
        *   `set_customer_reviews()`:(TODO)
        *   `set_supplier()`:  Устанавливает ID поставщика `2784`.
        *   `set_rewritted_URL()`:(TODO)
    *   Вызывает все внутренние функции для заполнения полей продукта.
    *   Возвращает объект `Product`.
4.  **`list_products_in_category_from_pagination(supplier)`**:
    *   Принимает объект `supplier` в качестве аргумента.
    *   Извлекает локатор для ссылок на товары из `supplier.locators['product']['link_to_product_locator']`.
    *   Извлекает список ссылок на товары со страницы.
    *   Если список пустой или равен `None`, возвращает пустой список.
    *   Если `_product_list_from_page` список - расширяет список ссылок, иначе добавляет в список.
    *   Извлекает ссылки на страницы пагинации из `supplier.locators['pagination']['a']`.
    *   Перебирает страницы пагинации, извлекает ссылки на товары и добавляет их в общий список.
    *   Кликает на следующую страницу.
    *   Если адрес текущей страницы не изменился, прерывает цикл.
    *   Удаляет дубликаты из списка ссылок на товары.
    *   Возвращает список ссылок на товары.
5.  **`get_list_products_in_category(s, scenario, presath)`**:
    *   Принимает объект `supplier`, сценарий и объект `presath`.
    *   Вызывает `list_products_in_category_from_pagination(s,scenario)`  и возвращает результат.
6.  **`get_list_categories_from_site(s,scenario_file,brand='')`**:
    *   (TODO) Функция не имеет тела.

### <mermaid>

```mermaid
flowchart TD
    subgraph login_function
        A[login(supplier)] --> B{_login(supplier)?}
        B -- Yes --> C[Return True]
        B -- No --> D{Popup Exists?}
        D -- Yes --> E[Close Popup and try _login(supplier)]
         E --> B
        D -- No --> F[Return None]
    end

    subgraph _login_function
       G[_login(supplier)] --> H[Find and fill email and password fields]
       H --> I{Login Success?}
       I -- Yes --> J[Return True]
       I -- No --> K[Return None]
    end

    subgraph grab_product_page_function
       L[grab_product_page(supplier)] --> M[Create Product Object]
        M --> N[Close Popup if Exists]
         N --> O[set_id()]
         O --> P[set_sku_suppl()]
         P --> Q[set_sku_prod()]
         Q --> R[set_title()]
        R --> S[set_cost_price()]
        S --> T[set_before_tax_price()]
        T --> U[set_delivery()]
        U --> V[set_images()]
        V --> W[set_combinations()]
        W --> X[set_description()]
        X --> Y[set_summary()]
        Y --> Z[set_supplier()]
        Z --> AA[set_rewritted_URL()]
        AA --> AB[Return Product Object]
    end

    subgraph list_products_in_category_function
        AC[list_products_in_category_from_pagination(supplier)] --> AD[Get product links from page]
        AD --> AE{Links exist?}
         AE -- Yes --> AF[add link to list]
        AE -- No --> AG[Return empty list]
        AF --> AH{Pagination?}
        AH -- Yes --> AI[Loop through pages]
        AI --> AJ[Get product links from page]
        AJ --> AK[Add new links to list]
        AK --> AL[Click next page]
        AL --> AM{URL changed?}
         AM -- Yes --> AI
        AM -- No --> AN[Remove duplicates]
        AN --> AO[Return List of product links]
        AH -- No --> AN

    end

    subgraph get_list_products_in_category_function
        AP[get_list_products_in_category(supplier, scenario, presath)] --> AQ[list_products_in_category_from_pagination()]
        AQ --> AR[Return Links]
    end


    subgraph get_list_categories_from_site_function
      AS[get_list_categories_from_site(s,scenario_file,brand='')] --> AT[ ... ]
    end
```

### <объяснение>

#### Импорты:
- `pathlib.Path`: Используется для работы с путями к файлам и директориям.
- `requests`: Библиотека для отправки HTTP запросов, но в данном коде не используется.
- `pandas as pd`: Используется для работы с табличными данными, но в данном коде не используется.
- `selenium.webdriver.remote.webelement.WebElement`: Используется для представления веб-элементов.
- `selenium.webdriver.common.keys.Keys`:  Используется для взаимодействия с клавишами клавиатуры.
- `settings`: Импортирует настройки проекта.
- `src.settings.StringFormatter`: Импортирует класс для форматирования строк.
- `src.settings.json_loads`: Импортирует функцию для загрузки JSON.
- `src.settings.logger`: Импортирует объект для логирования.
- `src.suppliers.Product`: Импортирует класс `Product`, используемый для представления продукта.

**Взаимосвязь с другими пакетами `src`**:
- `src.settings` предоставляет глобальные настройки, функции и константы проекта.
- `src.suppliers.Product` представляет собой модель данных для продуктов, полученных от поставщиков.

#### Классы:
- `Product`: Класс, представляющий продукт. Содержит поля (атрибуты) для хранения информации о продукте (например, id, sku, title, description, price, images). Используется для хранения и передачи данных о продукте.

#### Функции:
- `login(supplier)`:
    -   **Аргументы**: `supplier` (объект с информацией о поставщике).
    -   **Возвращаемое значение**: `True` при успешной авторизации, `None` при неудачной.
    -   **Назначение**: Осуществляет авторизацию на сайте поставщика.
    -   **Пример**:
    ```python
        supplier_instance = ... # Объект поставщика
        if login(supplier_instance):
           print("Login successful")
        else:
            print("Login failed")
    ```

- `_login(_s)`:
    -   **Аргументы**: `_s` (объект поставщика).
    -   **Возвращаемое значение**: `True` при успешном входе, `None` при неудачном.
    -   **Назначение**: Выполняет фактический процесс авторизации, взаимодействуя с веб-элементами.
     -    **Пример**:
        ```python
        supplier_instance = ... # Объект поставщика
        if _login(supplier_instance):
           print("Login successful")
        else:
            print("Login failed")
    ```

- `grab_product_page(s)`:
    -   **Аргументы**: `s` (объект поставщика).
    -   **Возвращаемое значение**: Объект `Product`.
    -   **Назначение**: Извлекает информацию со страницы продукта и заполняет объект `Product`.
    -   **Пример**:
     ```python
        supplier_instance = ... # Объект поставщика
        product = grab_product_page(supplier_instance)
        print(product.fields['title'])
    ```

- `list_products_in_category_from_pagination(supplier)`:
    -   **Аргументы**: `supplier` (объект поставщика).
    -   **Возвращаемое значение**: Список URL-адресов товаров в категории.
    -   **Назначение**: Получает список URL-адресов товаров из категории, проходя через страницы пагинации.
    -   **Пример**:
         ```python
        supplier_instance = ... # Объект поставщика
        product_urls = list_products_in_category_from_pagination(supplier_instance)
        for url in product_urls:
           print(url)
    ```
- `get_list_products_in_category(s, scenario, presath)`:
    -   **Аргументы**: `s` (объект поставщика), `scenario` (JSON), `presath` (PrestaShopWebServiceDict).
    -   **Возвращаемое значение**: Список URL-адресов товаров в категории.
    -   **Назначение**: Получает список товаров из категории, используя другие функции.
- `get_list_categories_from_site(s, scenario_file, brand='')`:
    -   **Аргументы**: `s` (объект поставщика), `scenario_file` (файл JSON со сценарием), `brand` (бренд).
    -   **Возвращаемое значение**: (не определено, т.к. функция не реализована)
    -   **Назначение**: Получение списка категорий товаров с сайта.

#### Переменные:
-   `_s`:  Используется как временная переменная для объекта `supplier`.
-   `_d`: Используется как временная переменная для объекта WebDriver.
-   `_l`: Используется как временная переменная для словаря локаторов.
-   `_price`: Используется для хранения цены товара, извлеченной со страницы.
-  `_field` :  Используется как временная переменная для полей объекта `Product`
-   `list_products_in_category`:  Список для хранения URL-адресов товаров, найденных в категории.
-   `pages` :  Список элементов пагинации
-   `close_pop_up_btn`: веб элемент для закрытия всплывающего окна

#### Потенциальные ошибки и области для улучшения:
-   **Обработка исключений**: В функциях `login` и `_login`, обработка исключений может быть улучшена, логирование более детальным (например, добавление стектрейса).
-   **Жестко закодированные данные**: ID поставщика `2784` жестко закодирован в `set_supplier`. Следует хранить эту информацию в настройках.
-   **Функции с `...`**: Некоторые функции (`set_combinations`, `set_qty`, `set_customer_reviews`, `set_rewritted_URL`, `get_list_categories_from_site`) имеют заглушку (`...`), нужно их доработать.
-   **Неиспользуемые импорты**: Импорты `requests` и `pandas` не используются в коде и должны быть удалены.
-   **Нелогичный `if str(type(close_pop_up_btn)).execute_locator("class \'list\'") >-1`**: Код пытается проверить тип через `str(type(...)).execute_locator(...)`, что не имеет смысла. Проверка типа должна проводиться через `isinstance(close_pop_up_btn, list)` или `isinstance(close_pop_up_btn, WebElement)`.
-   **Устаревший функционал `click(locator)`**: Использовался устаревший метод, который был заменет `execute_locator`
- **Комментарии**: Много не информативных комментариев.
-  **Дублирование кода**: В функции `list_products_in_category_from_pagination` дублируется код получения списка товаров со страницы. Можно вынести этот код в отдельную функцию.

**Цепочка взаимосвязей с другими частями проекта**:
- Данный модуль зависит от `src.settings` для получения общих настроек проекта и `src.suppliers.Product` для создания экземпляров продуктов. Также он взаимодействует с драйвером Selenium, который управляется на уровне поставщика.
- Данный модуль является частью пакета поставщика `src.suppliers.ivory` и используется для парсинга данных с сайта `morlevi`.