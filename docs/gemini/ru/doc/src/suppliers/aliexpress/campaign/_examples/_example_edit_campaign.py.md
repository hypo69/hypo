# Модуль `_example_edit_campaign.py`

## Обзор

Данный модуль представляет собой пример использования редактора рекламной кампании AliExpress. Он включает в себя класс `AliCampaignEditor`, который позволяет редактировать рекламные кампании.

## Оглавление

1.  [Классы](#классы)
    *   [`AliCampaignEditor`](#alicampaigneditor)
2.  [Импорты](#импорты)
   
## Классы

### `AliCampaignEditor`

**Описание**: Редактор рекламной кампании AliExpress.

**Методы**:

-   `__init__`: Инициализация редактора рекламной кампании.

#### `__init__`

**Описание**: Инициализирует объект `AliCampaignEditor`.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `category_name` (str): Название категории.
- `language` (str, optional): Язык кампании. По умолчанию `'EN'`.
- `currency` (str, optional): Валюта кампании. По умолчанию `'USD'`.

**Возвращает**:
- `None`: Метод ничего не возвращает.

## Импорты

Модуль импортирует следующие библиотеки и модули:

- `re`: Для работы с регулярными выражениями.
- `shutil`: Для работы с файлами и каталогами на высоком уровне.
- `pathlib.Path`: Для работы с путями в файловой системе.
- `typing.List, Optional, Union`: Для аннотации типов.
- `types.SimpleNamespace`: Для создания объектов с произвольными атрибутами.
- `src.gs`: Предположительно, глобальные настройки приложения.
- `src.suppliers.aliexpress.scenarios.campaigns.AliPromoCampaign`: Класс для работы с рекламными кампаниями AliExpress.
- `src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts`: Класс для генерации партнерских продуктов AliExpress.
- `src.suppliers.aliexpress.utils.extract_product_id.extract_prod_ids`: Функция для извлечения ID продуктов.
- `src.suppliers.aliexpress.utils.set_full_https.ensure_https`: Функция для обеспечения HTTPS для URL.
- `src.utils.jjson.j_loads_ns`, `src.utils.jjson.j_loads`: Функции для работы с JSON.
- `src.utils.convertors.list2string, src.utils.convertors.csv2dict`: Функции для преобразования данных.
- `src.utils.printer.pprint`: Функция для красивой печати.
- `utils.interface.read_text_file`, `utils.interface.get_filenames`: Функции для работы с файлами.
- `src.logger.logger.logger`: Объект логгера.