# Модуль: Редактор рекламной кампании AliExpress

## Обзор

Данный модуль содержит класс `AliCampaignEditor`, предназначенный для редактирования рекламных кампаний на AliExpress. Он расширяет функциональность класса `AliPromoCampaign`, добавляя возможности для управления и настройки рекламных кампаний.

## Содержание

1.  [Классы](#классы)
    *   [`AliCampaignEditor`](#alicampaigneditor)
2.  [Импорты](#импорты)

## Классы

### `AliCampaignEditor`

**Описание**: Класс для редактирования рекламных кампаний AliExpress.

**Наследуется от**: `AliPromoCampaign`

**Методы**:

-   `__init__`: Инициализирует экземпляр класса `AliCampaignEditor`.

#### `__init__`

**Описание**: Инициализирует экземпляр класса `AliCampaignEditor`.

**Параметры**:

-   `campaign_name` (str): Название рекламной кампании.
-   `category_name` (str): Название категории товаров.
-   `language` (str, optional): Язык интерфейса. По умолчанию `EN`.
-   `currency` (str, optional): Валюта. По умолчанию `USD`.

**Возвращает**:

-   `None`

## Импорты

В данном модуле используются следующие импорты:

-   `re`: Для работы с регулярными выражениями.
-   `shutil`: Для высокоуровневых операций с файлами.
-   `pathlib.Path`: Для работы с путями к файлам и директориям.
-   `typing.List`, `typing.Optional`, `typing.Union`: Для аннотации типов.
-   `types.SimpleNamespace`: Для создания простых объектов с атрибутами.
-   `src.gs`: Неизвестный модуль.
-   `src.suppliers.aliexpress.scenarios.campaigns.AliPromoCampaign`: Базовый класс для работы с рекламными кампаниями AliExpress.
-   `src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts`: Для генерации партнерских ссылок.
-   `src.suppliers.aliexpress.utils.extract_product_id.extract_prod_ids`: Для извлечения идентификаторов продуктов.
-   `src.suppliers.aliexpress.utils.set_full_https.ensure_https`: Для обеспечения использования HTTPS.
-   `src.utils.jjson.j_loads_ns`, `src.utils.jjson.j_loads`, `src.utils.jjson.j_dumps`: Для работы с JSON.
-   `src.utils.convertors.list2string`, `src.utils.convertors.csv2dict`: Для преобразования данных.
-   `src.utils.printer.pprint`: Для красивого вывода на экран.
-    `utils.interface.read_text_file`, `utils.interface.get_filenames`: Для работы с файлами.
-    `src.logger.logger.logger`: Для логирования.