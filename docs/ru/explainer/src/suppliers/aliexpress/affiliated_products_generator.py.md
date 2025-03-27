## АНАЛИЗ КОДА: `affiliated_products_generator.py`

### 1. <алгоритм>

**Блок-схема:**

```mermaid
flowchart TD
    A[Начало процесса] --> B{Получение списка `prod_ids` и `category_root`};
    B --> C{Нормализация `prod_ids` в `https` ссылки};
    C --> D{Итерация по нормализованным ссылкам};
    D -- Для каждой ссылки --> E{Получение аффилиатных ссылок};
     E --> F{Аффилиатная ссылка найдена?};
    F -- Да --> G{Сохранение аффилиатной ссылки и исходной URL};
    G --> D
    F -- Нет --> D
    D -- Все ссылки обработаны --> H{Проверка наличия аффилиатных ссылок};
    H -- Есть аффилиатные ссылки --> I{Получение деталей продуктов по аффилиатным ссылкам};
    H -- Нет аффилиатных ссылок --> J{Лог предупреждения};
    J --> K[Конец процесса с возвратом `None`];
    I --> L{Итерация по продуктам и аффилиатным ссылкам};
    L -- Для каждого продукта --> M{Сохранение изображений};
    M --> N{Сохранение видео (если есть)};
    N --> O{Сохранение JSON данных};
    O --> P{Добавление продукта в список `affiliated_products_list`};
    P --> L
    L -- Все продукты обработаны --> Q{Сохранение заголовков продуктов в файл};
    Q --> R{Возврат списка `affiliated_products_list`};
    R --> K[Конец процесса];
```

**Примеры для блоков:**

1.  **A:** Начало выполнения функции `process_affiliate_products`.
2.  **B:** Входные данные: `prod_ids = ["http://example.com/product1", "example.com/product2", "123456789.html"]`, `category_root = "/path/to/category"`.
3.  **C:** `normilized_prod_urls = ["https://example.com/product1", "https://example.com/product2", "https://aliexpress.com/item/123456789.html"]`.
4.  **D:** Начало цикла по `normilized_prod_urls`.
5.  **E:** Вызов `get_affiliate_links` для URL "https://example.com/product1".
6.  **F:** Проверка, есть ли аффилиатная ссылка.
7.  **G:** Добавление `_links.promotion_link` (например, "https://s.click.aliexpress.com/e/_D123456") в `_promotion_links` и "https://example.com/product1" в `_prod_urls`.
8. **H:** Проверка, не пуст ли список `_promotion_links`.
9.  **I:** Вызов `retrieve_product_details` c `_prod_urls`.
10. **J:** Логирование предупреждения `No affiliate products returned`.
11. **L:** Начало цикла по продуктам.
12. **M:** Загрузка и сохранение изображения продукта.
13. **N:** Загрузка и сохранение видео продукта (если есть).
14. **O:** Сохранение деталей продукта в JSON файл.
15. **P:** Добавление продукта в `affiliated_products_list`.
16. **Q:** Сохранение заголовков продуктов в файл product_titles.txt.
17. **R:** Возврат списка `affiliated_products_list`.
18. **K:** Конец выполнения функции.

**Поток данных:**

*   `prod_ids` (list[str]) -> `normilized_prod_urls` (list[str]) -> цикл `for` -> `_links` (SimpleNamespace) -> `_promotion_links` (list[str]), `_prod_urls` (list[str]) -> `retrieve_product_details` -> `_affiliated_products` (list[SimpleNamespace]) -> цикл `for` -> `product` (SimpleNamespace) -> сохранение изображений, видео, данных в JSON -> `affiliated_products_list` (list[SimpleNamespace]) -> сохранение списка заголовков продуктов -> return `affiliated_products_list`.

### 2. <mermaid>

```mermaid
flowchart TD
    A[Start: process_affiliate_products] --> B{Normalize Product URLs};
    B --> C{Get Affiliate Links};
    C --> D{Check for Affiliate Links};
    D -- Yes --> E{Retrieve Product Details};
    D -- No --> F{Log Warning};
    F --> G[Return None];
    E --> H{Process Products};
    H --> I{Save Product Image};
    I --> J{Save Product Video (if any)};
    J --> K{Save Product JSON};
     K --> L{Add product to list};
     L --> H
    H --> M{Save product titles};
    M --> N[Return affiliated_products_list];
     N --> O[End: process_affiliate_products];
```

**Импорты для `mermaid`:**

*   Нет импортов в коде, которые явно относятся к созданию диаграмм `mermaid`.

### 3. <объяснение>

**Импорты:**

*   `asyncio`: Для асинхронного программирования.
*   `datetime`: Для работы с датой и временем.
*   `html`: Для обработки HTML.
*   `pathlib.Path`: Для работы с путями файлов и директорий.
*   `urllib.parse.urlparse`: Для разбора URL.
*   `types.SimpleNamespace`: Для создания простых объектов.
*   `typing.List`: Для аннотаций типов.
*   `src.logger.logger.logger`: Логгер.
*   `src.gs`: Глобальные настройки проекта.
*   `src.suppliers.aliexpress.AliApi`: Базовый класс для работы с AliExpress API.
*   `src.suppliers.aliexpress.campaign.html_generators`: Модуль для генерации HTML шаблонов.
*    `src.suppliers.aliexpress.utils.ensure_https`: Функция для преобразования URL в https.
*   `src.endpoints.prestashop.product_fields.ProductFields`: Перечисление полей продукта.
*   `src.utils.image.save_image_from_url`: Функция для сохранения изображений из URL.
*   `src.utils.video.save_video_from_url`: Функция для сохранения видео из URL.
*   `src.utils.file_async`: Функции для асинхронной работы с файлами.
*   `src.utils.jjson.j_loads_ns`, `src.utils.jjson.j_dumps`: Функции для работы с JSON.
*    `src.utils.printer.pprint`: Функция для красивого вывода данных.

**Классы:**

*   `AliAffiliatedProducts(AliApi)`:
    *   **Роль:** Класс для сбора данных о товарах, доступных по аффилиатным ссылкам.
    *   **Атрибуты:**
        *   `language` (str): Язык для кампании.
        *   `currency` (str): Валюта для кампании.
    *   **Методы:**
        *   `__init__(self, language: str = 'EN', currency: str = 'USD', *args, **kwargs)`: Инициализирует объект, устанавливая язык и валюту.
        *   `process_affiliate_products(self, prod_ids: list[str], category_root: Path | str) -> list[SimpleNamespace]`:  Основной метод для обработки списка ID или URL продуктов, возвращает список объектов с аффилиатными ссылками и сохраненными данными.

**Функции:**

*   `process_affiliate_products(self, prod_ids: list[str], category_root: Path | str) -> list[SimpleNamespace]`:
    *   **Аргументы:**
        *   `prod_ids` (list[str]): Список URL или ID продуктов.
        *   `category_root` (Path | str): Путь к корневой директории категории.
    *   **Возвращаемое значение:**
        *   `list[SimpleNamespace]`: Список обработанных продуктов с аффилиатными ссылками, сохраненными изображениями и видео.
    *   **Назначение:** Получает аффилиатные ссылки, собирает детали продуктов, сохраняет изображения и видео, и возвращает список продуктов.
        1.  Нормализует список URL продуктов.
        2.  Получает аффилиатные ссылки для каждого URL.
        3.  Извлекает информацию о продукте по аффилиатным ссылкам.
        4.  Сохраняет изображения и видео для каждого продукта.
        5.  Сохраняет данные о продукте в JSON.
        6.  Возвращает список обработанных продуктов.

**Переменные:**

*   `_promotion_links` (list): Список аффилиатных ссылок.
*   `_prod_urls` (list): Список URL продуктов.
*   `normilized_prod_urls` (list): Список нормализованных URL.
*   `print_flag` (str): Флаг для печати в консоль.
*    `_links` (SimpleNamespace): Объект, содержащий аффилиатную ссылку.
*   `_affiliated_products` (List[SimpleNamespace]): Список продуктов с полной информацией.
*   `affiliated_products_list` (list[SimpleNamespace]): Список обработанных продуктов.
*   `product_titles` (list): Список заголовков продуктов.
*   `product` (SimpleNamespace): Объект, содержащий информацию о продукте.
*   `promotion_link` (str): Аффилиатная ссылка.
*   `image_path` (Path): Путь к файлу изображения продукта.
*   `video_path` (Path): Путь к файлу видео продукта.
*   `suffix` (str): Расширение видеофайла.
*    `parsed_url` (Path):  Результат парсинга URL.
*   `product_titles_path` (Path): Путь к файлу для хранения заголовков продуктов.

**Потенциальные ошибки и улучшения:**

1.  **Обработка ошибок:**
    *   В коде есть проверка на отсутствие языка или валюты, но не хватает более детальной обработки исключений, возникающих при обращении к API, сохранении файлов и т. д.
    *   Нужно добавить `try-except` блоки для обработки исключений при запросах к API, записи файлов и т. д.

2.  **Логирование:**
    *   Использовать более информативные сообщения в логах.

3.  **Производительность:**
    *   Асинхронная обработка уже есть, но можно дополнительно оптимизировать операции сохранения изображений и видео, возможно, используя `asyncio.gather`.

4.  **Унификация:**
    *   Метод `process_affiliate_products` очень длинный и делает много всего. Возможно, стоит его разбить на несколько более маленьких методов.

**Взаимосвязи с другими частями проекта:**

*   Использует `src.logger.logger` для ведения логов.
*   Использует `src.gs` для получения глобальных настроек.
*   Наследует `AliApi` из `src.suppliers.aliexpress` для работы с AliExpress API.
*   Использует модули `src.utils.image` и `src.utils.video` для работы с изображениями и видео.
*   Использует модули `src.utils.file_async` для асинхронной работы с файлами.
*   Использует `src.utils.jjson` для работы с JSON.
*   Использует `src.endpoints.prestashop.product_fields` для полей продукта.
*   Использует `src.suppliers.aliexpress.utils.ensure_https` для преобразования URL.

**Заключение:**

Этот код предназначен для получения информации о продуктах AliExpress по аффилиатным ссылкам, сохранения их изображений и видео, а также для сохранения этих данных в JSON файлы. Код структурирован и имеет асинхронную обработку. Но для большей устойчивости к ошибкам и улучшения читаемости можно добавить больше обработки исключений и разбить метод на более мелкие функции.