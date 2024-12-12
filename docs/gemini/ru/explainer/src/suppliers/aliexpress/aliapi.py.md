## <алгоритм>

**1. Инициализация `AliApi`:**
   - Создается экземпляр класса `AliApi`.
   - При инициализации:
     - Получает учетные данные (`api_key`, `secret`, `tracking_id`) из глобальных настроек (`gs.credentials.aliexpress`).
     - Инициализирует родительский класс `AliexpressApi` с этими учетными данными и параметрами `language` и `currency`.
     - (закомментировано) Инициализация менеджеров базы данных `CategoryManager` и `ProductCampaignsManager`.

   *Пример:*
   ```python
   ali_api = AliApi(language='ru', currency='rub')
   ```

**2. Получение деталей продукта `retrieve_product_details_as_dict`:**
   - Принимает список `product_ids`.
   - Вызывает метод `retrieve_product_details` (унаследованный из `AliexpressApi`), чтобы получить список объектов `SimpleNamespace` с деталями продуктов.
   - Преобразует каждый объект `SimpleNamespace` в словарь с помощью `vars(ns)` (или `ns.__dict__`).
   - Возвращает список словарей.

   *Пример:*
   ```python
   product_ids = [12345, 67890]
   product_details = ali_api.retrieve_product_details_as_dict(product_ids)
   # product_details будет списком словарей с информацией о продуктах
   ```

**3. Получение партнерских ссылок `get_affiliate_links`:**
   - Принимает строку или список `links` (ссылки на продукты) и `link_type`.
   - Вызывает метод `get_affiliate_links` родительского класса `AliexpressApi`.
   - Возвращает список объектов `SimpleNamespace` с партнерскими ссылками.

   *Пример:*
   ```python
   links = ["https://aliexpress.com/item/12345.html", "https://aliexpress.com/item/67890.html"]
   affiliate_links = ali_api.get_affiliate_links(links, link_type=1)
   # affiliate_links будет списком SimpleNamespace объектов с партнерскими ссылками
   ```

## <mermaid>

```mermaid
graph LR
    A[AliApi Initialization] --> B(Get Credentials from gs.credentials.aliexpress);
    B --> C(Initialize AliexpressApi with API key, secret, language, currency, tracking_id);
    C --> D{Initialize Database Managers (commented out)};
    D --> E[retrieve_product_details_as_dict];
    E --> F(Call AliexpressApi.retrieve_product_details);
    F --> G{Convert SimpleNamespace to dict};
    G --> H[Return list of dicts];
    D --> I[get_affiliate_links];
    I --> J(Call AliexpressApi.get_affiliate_links);
    J --> K[Return list of SimpleNamespace with affiliate links];
    
    classDef classStyle fill:#f9f,stroke:#333,stroke-width:2px
    class A,E,I classStyle
```

**Описание зависимостей:**

- **`AliApi`** зависит от:
    - **`gs`**: для получения учетных данных AliExpress (`api_key`, `secret`, `tracking_id`).
    - **`AliexpressApi`**:  является родительским классом, предоставляющим базовые функции API AliExpress.
    - **`CategoryManager`**: (закомментировано) для управления категориями товаров в базе данных.
    - **`ProductCampaignsManager`**: (закомментировано) для управления кампаниями товаров и купонами в базе данных.
- **`retrieve_product_details_as_dict`** зависит от:
    - **`AliexpressApi.retrieve_product_details`**: для получения данных о продуктах в формате `SimpleNamespace`.
- **`get_affiliate_links`** зависит от:
    - **`AliexpressApi.get_affiliate_links`**: для получения партнерских ссылок.

## <объяснение>

**Импорты:**

-   `re`:  Для работы с регулярными выражениями (используется для обработки строк). В данном контексте не используется.
-   `json`: Для работы с JSON (сериализация и десериализация данных).
-   `asyncio`: Для поддержки асинхронного программирования (здесь не используется напрямую, но может использоваться в `AliexpressApi`).
-   `pathlib`: Для работы с файловыми путями.
-   `typing`: Для аннотации типов (используется `List`, `Dict`).
-   `types`: Для создания  `SimpleNamespace` объектов.
-   `requests`: Для отправки HTTP-запросов.
-   `src`:
    -   `gs`:  Глобальные настройки проекта.
    -   `src.utils.jjson`:  Модуль для работы с JSON, включая загрузку и выгрузку данных (`j_loads_ns`, `j_loads`, `j_dumps`).
    -   `src.utils.printer`:  Модуль для печати данных (`pprint`).
    -    `src.utils.convertors.json`:  Модуль для конвертации `json` в `csv` (`json2csv`).
    -    `src.logger.logger`:  Модуль для логирования событий (`logger`).
-   `.api`:  Модуль `AliexpressApi` из текущего пакета, базовый класс для взаимодействия с API AliExpress.
-   `src.db.manager_categories`:  Модуль `AliexpressCategory` и `CategoryManager` для управления категориями товаров в базе данных.
-    `src.db.manager_coupons_and_sales`:  Модуль `ProductCampaignsManager` для управления кампаниями и купонами.

**Классы:**

-   `AliApi(AliexpressApi)`:
    -   **Роль:**  Кастомный класс для работы с API AliExpress. Наследует функциональность от `AliexpressApi`.
    -   **Атрибуты:**
        -   `manager_categories`: Экземпляр `CategoryManager` (не инициализирован в текущей версии, закомментирован).
        -   `manager_campaigns`: Экземпляр `ProductCampaignsManager` (не инициализирован в текущей версии, закомментирован).
    -   **Методы:**
        -   `__init__(self, language='en', currency='usd', *args, **kwargs)`: Инициализирует объект `AliApi`, устанавливает настройки языка, валюты и учетных данных.
        -    `retrieve_product_details_as_dict(self, product_ids: list) -> dict | None`: Принимает список `product_ids`, вызывает `retrieve_product_details` из родительского класса, преобразует `SimpleNamespace` объекты в `dict` и возвращает список словарей.
        -   `get_affiliate_links(self, links: str | list, link_type: int = 0, **kwargs) -> List[SimpleNamespace]`: Вызывает метод  `get_affiliate_links` родительского класса для получения партнерских ссылок.

**Функции:**

-   `__init__`:
    -   **Аргументы:**
        -   `language` (str, optional): Язык для API запросов (по умолчанию 'en').
        -   `currency` (str, optional): Валюта для API запросов (по умолчанию 'usd').
        -   `*args`, `**kwargs`: Дополнительные аргументы.
    -   **Возвращаемое значение:** None.
    -   **Назначение:** Инициализирует объект класса, получает учетные данные из `gs.credentials.aliexpress`, вызывает конструктор родительского класса `AliexpressApi`.
-    `retrieve_product_details_as_dict`:
    -   **Аргументы:**
        -   `product_ids` (list): Список идентификаторов продуктов.
    -   **Возвращаемое значение:** `dict | None`: Список словарей с данными о продуктах.
    -   **Назначение:** Извлекает данные о продуктах в виде словарей, вызывая метод `retrieve_product_details` родительского класса и преобразуя результаты.
    -   **Пример:** `ali_api.retrieve_product_details_as_dict([12345, 67890])`
-   `get_affiliate_links`:
    -   **Аргументы:**
        -   `links` (str | list): Список ссылок на продукты или отдельная ссылка.
        -   `link_type` (int, optional): Тип партнерской ссылки (по умолчанию 0).
        -   `**kwargs`: Дополнительные аргументы.
    -   **Возвращаемое значение:** `List[SimpleNamespace]`: Список объектов `SimpleNamespace`, содержащих партнерские ссылки.
    -   **Назначение:** Получает партнерские ссылки, вызывая метод `get_affiliate_links` родительского класса.
    -   **Пример:** `ali_api.get_affiliate_links(["https://aliexpress.com/item/12345.html"], link_type=1)`

**Переменные:**

-   `MODE`:  Глобальная переменная, указывающая режим работы (`'dev'`).

**Области для улучшения:**

-   **Инициализация менеджеров БД:** Инициализация `CategoryManager` и `ProductCampaignsManager` закомментирована. Нужно раскомментировать и реализовать корректную инициализацию, когда это будет необходимо.
-   **Обработка ошибок:** Не хватает обработки ошибок при работе с API, например, исключений `requests`.
-   **Асинхронность:** Можно рассмотреть возможность использования асинхронных запросов для ускорения работы с API, особенно если запросов много.
-   **Документация:**  Необходимо добавить docstrings для всех функций и классов.
-   **Конфигурация:** Лучше вынести параметры `language` и `currency` в настройки, чтобы они не были жестко заданы.
-   **Проверка типов:**  Добавить проверки типов для входных параметров функций.

**Взаимосвязь с другими частями проекта:**

-   **`src.gs`**:  Используется для получения учетных данных AliExpress, связывая этот модуль с общими настройками приложения.
-   **`src.db`**: (потенциально) Используется для сохранения и управления данными о категориях и кампаниях товаров.
-   **`src.utils`**:  Используется для вспомогательных функций, таких как работа с JSON, печать и логирование, обеспечивая единообразие в обработке данных.
-   **`AliexpressApi`**:  Базовый класс, предоставляющий основные функции для взаимодействия с API, делая `AliApi` более специализированным.