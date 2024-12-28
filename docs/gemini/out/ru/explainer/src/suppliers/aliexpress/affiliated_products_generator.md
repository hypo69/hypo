# <input code>

```python
## \file hypotez/src/suppliers/aliexpress/affiliated_products_generator.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers.aliexpress 
	:platform: Windows, Unix
	:synopsis:

"""


import asyncio
from datetime import datetime
import html
from pathlib import Path
from urllib.parse import urlparse
from types import SimpleNamespace
from typing import List

from src.logger import logger
from src import gs
from src.suppliers.aliexpress import AliApi
from src.suppliers.aliexpress.campaign.html_generators import ProductHTMLGenerator, CategoryHTMLGenerator, CampaignHTMLGenerator 
from src.suppliers.aliexpress.utils.ensure_https import ensure_https
from src.product.product_fields import ProductFields as f
from src.utils.image import save_png_from_url 
from src.utils.video import save_video_from_url
from src.utils.file import get_directory_names, get_filenames, read_text_file, save_text_file
from src.utils.jjson import j_loads_ns, j_dumps
from src.utils.printer import pprint
from src.logger import logger


class AliAffiliatedProducts(AliApi):
    """ Class to collect full product data from URLs or product IDs.
    For more details on how to create templates for ad campaigns, see the section `Managing Aliexpress Ad Campaigns`.
    """
    ...
    language:str = None
    currency:str = None
    def __init__(self,
                 language: str | dict = 'EN',
                 currency: str = 'USD',
                 *args, **kwargs):
        """
        Initializes the AliAffiliatedProducts class.
        Args:
            language: Language for the campaign (default 'EN').
            currency: Currency for the campaign (default 'USD').
        """
        ...
        if not language or not currency:
            logger.critical(f"No language, currency !")
            return
        super().__init__(language, currency)
        self.language, self.currency = language, currency


    async def process_affiliate_products(self, prod_ids: list[str], category_root: Path | str) -> list[SimpleNamespace]:
        """ ... """
        ...
```

# <algorithm>

**Алгоритм работы функции `process_affiliate_products`:**

1. **Нормализация URL:** Функция `ensure_https` преобразует список `prod_ids` (списка URL или идентификаторов товаров) к виду `https://aliexpress.com/item/<product_id>.html`
2. **Поиск аффилированных ссылок:** Для каждого `prod_url` из `normilized_prod_urls` вызывается `get_affiliate_links` для получения аффилированных ссылок.
   - Если ссылки найдены, добавляются в `_promotion_links` и `_prod_urls`
   - Если ссылки не найдены, процесс пропускается для текущего URL.
3. **Проверка на наличие аффилированных ссылок:** Если `_promotion_links` пуст, то выводится предупреждение и функция возвращает пустой список.
4. **Получение деталей товара:** Функция `retrieve_product_details`  вызывается для получения данных о товарах из списка `_prod_urls` и сохраняется в `_affiliated_products`.  Возврат пустого списка при ошибках.
5. **Обработка данных о товарах:**  Для каждого продукта из `_affiliated_products` и соответствующей аффилированной ссылки из `_promotion_links`:
    - Сохраняется `product.product_title`
    - Устанавливаются `product.language` и `product.promotion_link`
    - Сохраняется изображение `product.product_main_image_url` в `category_root/images`.
    - Если есть видео (`product.product_video_url`), сохраняется в `category_root/videos`.
    - Сохраняется `product` в `JSON`-файл в формате `self.language_self.currency/<product.product_id>.json` в папке `category_root`.
    - Добавляется `product` в `affiliated_products_list`.
6. **Сохранение названий товаров:**  Название товаров сохраняется в `category_root/product_titles.txt`.
7. **Возврат:** Возвращается список `affiliated_products_list`.


# <mermaid>

```mermaid
graph TD
    A[process_affiliate_products(prod_ids, category_root)] --> B{Нормализация prod_ids};
    B -- OK --> C[Поиск аффилированных ссылок];
    C -- Найдено --> D[Проверка на наличие ссылок];
    D -- OK --> E[Получение деталей товара];
    E -- OK --> F[Обработка данных о товарах];
    F --> G[Сохранение названий товаров];
    G --> H[Возврат affiliated_products_list];
    D -- Нет --> I[Вывод предупреждения];
    I --> H;
    E -- Не найдены --> J[Возврат пустого списка];
    J --> H;

    subgraph AliApi
        C --> K[get_affiliate_links(prod_url)];
        K -- OK --> C;
        K -- Ошибка --> C;
    end
    subgraph Image/Video saving
        F --> L[Сохранение изображения];
        L -- OK --> F;
        F --> M[Сохранение видео];
        M -- OK --> F;
    end
    subgraph JSON saving
        F --> N[Сохранение JSON];
        N -- OK --> F;
    end


```

# <explanation>

**Импорты:**

- `asyncio`:  Для асинхронных операций (вероятно, для работы с сетью).
- `datetime`: Для работы с датами и временем (не используется напрямую в этом коде).
- `html`: Для работы с HTML (не используется напрямую в этом коде).
- `pathlib`: Для работы с путями к файлам.
- `urllib.parse`: Для парсинга URL.
- `types`: Для работы с типом `SimpleNamespace`.
- `typing`: Для использования типов данных.
- `src.logger`: Модуль для логирования.
- `src`:  Корневой пакет проекта, вероятно содержит общие функции и классы.
- `gs`: Вероятно, модуль для работы с Google Cloud Storage (не используется напрямую в этом коде).
- `src.suppliers.aliexpress.AliApi`: Класс для работы с API AliExpress.
- `src.suppliers.aliexpress.campaign.html_generators`: Модуль, содержащий генераторы HTML для кампаний (не используется напрямую в этом коде).
- `src.suppliers.aliexpress.utils.ensure_https`: Модуль для преобразования URL к протоколу HTTPS.
- `src.product.product_fields`: Модуль с определениями полей данных о товарах.
- `src.utils.image`: Модуль для сохранения изображений.
- `src.utils.video`: Модуль для сохранения видео.
- `src.utils.file`: Модуль для работы с файлами (чтение, сохранение).
- `src.utils.jjson`: Модуль для работы с JSON (сериализация/десериализация).
- `src.utils.printer`: Модуль для форматированного вывода.


**Классы:**

- `AliAffiliatedProducts(AliApi)`: Наследует `AliApi`, добавляя функциональность для сбора данных о товарах с аффилированными ссылками.
    - `language`: Язык кампании.
    - `currency`: Валюта кампании.
    - `__init__`: Инициализирует класс, принимая язык и валюту кампании. Важно проверить корректность входных данных.
    - `process_affiliate_products`:  Обрабатывает список идентификаторов продуктов, получая аффилированные ссылки, данные о товарах, сохраняет изображения и видео, и возвращает список продуктов.


**Функции:**

- `ensure_https`: Принимает список URL, возвращает список URL, начинающихся с `https://`.
- `get_affiliate_links`:  Используется для поиска аффилированных ссылок, вызывается из `super()`, предполагается, что она определена в `AliApi`.
- `retrieve_product_details`: Получает подробную информацию о продуктах по заданным URL, возвращает список `SimpleNamespace`-объектов.
- `save_png_from_url`: Сохраняет изображение из URL в файл.
- `save_video_from_url`: Сохраняет видео из URL в файл.
- `j_dumps`: Сохраняет `SimpleNamespace`-объект в JSON-файл.
- `save_text_file`: Сохраняет текст в файл.


**Переменные:**

- `MODE`:  Переменная, вероятно, используемая для управления режимом работы.
- `_promotion_links`, `_prod_urls`: Временные списки для хранения аффилированных ссылок и URL-адресов товаров.
- `normilized_prod_urls`:  Список URL после преобразования к протоколу HTTPS.
- `print_flag`: Флаг для переключения печати в одну строку, потенциал для оптимизации или удаления (не лучшая практика).
- `_affiliated_products`: Список продуктов, полученный из `retrieve_product_details`.
- `affiliated_products_list`: Список для хранения результатов обработки.
- `product_titles`: Список названий продуктов, используемый для сохранения в файл.
- `product_titles_path`: Путь к файлу с названиями продуктов.
- `category_root`: Путь к корневой папке для сохранения данных кампании.

**Возможные ошибки/улучшения:**

- **Обработка ошибок:**  Код содержит проверку на наличие языка и валюты, но не хватает проверки на другие возможные ошибки (например, проблемы с сетевыми запросами, отсутствие необходимых данных на сайте AliExpress).  Добавление блоков `try...except` улучшит надежность.
- **Использование `try...except`:** Добавление обработки исключений для `save_png_from_url`, `save_video_from_url`, и `retrieve_product_details`.
- **Упрощение кода:**  Возможно, некоторые операции можно объединить или переписать для большей читабельности.
- **Документация:**  Добавление более подробной документации к классам и методам улучшит понимание и поддержку кода.
- **Оптимизация логирования:**  Использование более специфичных уровней логирования (debug, info, warning, error, critical) для лучшего отслеживания ошибок.

**Взаимосвязи с другими частями проекта:**

- `AliApi`:  Базовый класс для работы с API AliExpress, содержит необходимые методы для запроса данных.
- `src.logger`:  Зависимость для логирования.
- `gs`, `src.utils.image`, `src.utils.video`, `src.utils.file`, `src.utils.jjson`:  Зависимости для работы с файлами, сохранения данных, и других служебных задач.
- `ProductFields`: Зависимость для доступа к полям данных продукта.


Этот код является фрагментом большего проекта и предполагает наличие дополнительных модулей и классов для работы с данными и API AliExpress.  Чтобы получить полное представление, необходим контекст всего проекта.