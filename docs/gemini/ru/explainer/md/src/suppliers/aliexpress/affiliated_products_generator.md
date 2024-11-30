# <input code>

```python
## \file hypotez/src/suppliers/aliexpress/affiliated_products_generator.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n
"""
.. module: src.suppliers.aliexpress 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'

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
from src.utils import pprint
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
        """
        ...
        """
        ...
        _promotion_links: list = []
        _prod_urls: list = []
        normilized_prod_urls = ensure_https(prod_ids)
        print_flag = ''


        for prod_url in normilized_prod_urls:
            _links = super().get_affiliate_links(prod_url)
            if _links:
                _links = _links[0]
            if hasattr(_links, 'promotion_link'):
                _promotion_links.append(_links.promotion_link)
                _prod_urls.append(prod_url)
                logger.info(f"found affiliate for {_links.promotion_link}")
                # pprint(...)  # печать в одну строку
            else:
                continue


        if not _promotion_links:
            logger.warning(f'No affiliate products returned {prod_ids=}/n', None, None)
            return

        _affiliated_products: List[SimpleNamespace] = self.retrieve_product_details(
            _prod_urls)
        if not _affiliated_products:
            return

        affiliated_products_list:list[SimpleNamespace] = []
        product_titles:list = []
        for product, promotion_link in zip(_affiliated_products, _promotion_links):
            product_titles.append(product.product_title)
            product.language = self.language
            product.promotion_link = promotion_link
            image_path = Path(category_root) / 'images' / \
                f"{product.product_id}.png"
            await save_png_from_url(product.product_main_image_url, image_path)
            logger.info(f"Saved image for {product.product_id=}")

            product.local_saved_image = str(image_path)
            if len(product.product_video_url) > 1:
                # ... (video saving logic)
            logger.info(f"{product.product_title}")
            j_dumps(product, Path(category_root) / f'{self.language}_{self.currency}' / f'{product.product_id}.json')
            affiliated_products_list.append(product)
        product_titles_path:Path = category_root / f"{self.language}_{self.currency}" / 'product_titles.txt'
        save_text_file(product_titles, product_titles_path)
        return affiliated_products_list
```

# <algorithm>

**Шаг 1**: Принимает список `prod_ids` (продуктовых ID или URL) и путь `category_root`.

**Шаг 2**: Нормализует входные `prod_ids` к `https` URL.

**Шаг 3**:  Итерируется по нормализованным `prod_ids`.

**Шаг 4**: Для каждого `prod_id`, вызывается метод `get_affiliate_links()` родительского класса `AliApi`.

**Шаг 5**: Проверяет, получен ли `promotion_link`. Если да, то добавляет его в `_promotion_links` и соответствующий URL в `_prod_urls`.  Если нет, то переходит к следующему `prod_id`.

**Шаг 6**: Если не найдено ни одного `promotion_link`, выводит предупреждение и возвращает пустой список.

**Шаг 7**: Вызывает метод `retrieve_product_details()` для получения подробных данных о продуктах по `_prod_urls`.

**Шаг 8**: Если нет подробных данных о продуктах (`_affiliated_products`), возвращает пустой список.

**Шаг 9**: Итерируется по парам (`product`, `promotion_link`).

**Шаг 10**: Добавляет `product.title` в список `product_titles`.

**Шаг 11**: Устанавливает `language` и `promotion_link` для каждого продукта.

**Шаг 12**: Сохраняет изображение продукта в `category_root/images` под названием `<product_id>.png`.

**Шаг 13**: Если у продукта есть видео, сохраняет его в `category_root/videos` под названием `<product_id><suffix>`.

**Шаг 14**: Сохраняет данные продукта в `category_root/<language>_<currency>/<product_id>.json` в формате JSON.

**Шаг 15**: Добавляет обработанный продукт в `affiliated_products_list`.

**Шаг 16**: Сохраняет список `product_titles` в `category_root/<language>_<currency>/product_titles.txt`.

**Шаг 17**: Возвращает список обработанных продуктов `affiliated_products_list`.

**Пример**: Если `prod_ids` содержит `['https://example.com/product1', 'https://example.com/product2']`, код получит данные о каждом продукте, сохранит изображения и видео (если они есть), а затем вернет список `SimpleNamespace` с данными продуктов, включая ссылку на партнерскую программу и пути к сохранённым файлам.


# <mermaid>

```mermaid
graph LR
    A[AliAffiliatedProducts] --> B(process_affiliate_products);
    B --> C{prod_ids, category_root};
    C -- Normalize prod_ids to HTTPS --> D[ensure_https];
    D --> E(Loop prod_url);
    E --> F[get_affiliate_links(AliApi)];
    F -- Has promotion_link --> G{Promotion Link Found};
    G -- Yes --> H[Append to _promotion_links, _prod_urls];
    H --> I[Log Info];
    G -- No --> J[Continue];
    E -- No promotion link --> K{Empty _promotion_links?};
    K -- Yes --> L[Log Warning, Return];
    K -- No --> M[retrieve_product_details];
    M --> N{Empty _affiliated_products?};
    N -- Yes --> O[Return];
    N -- No --> P(Loop product, promotion_link);
    P --> Q[Set product.language, product.promotion_link];
    Q --> R[Save product image];
    R --> S[Save product video (if exists)];
    S --> T[Save product data to JSON];
    T --> U[Append to affiliated_products_list];
    P --> V[Save product titles];
    V --> W[Return affiliated_products_list];
    
    subgraph Dependencies
        AliApi --> F;
        ensure_https --> D;
        save_png_from_url --> R;
        save_video_from_url --> S;
        j_dumps --> T;
        save_text_file --> V;
        logger --> I, L;
        pprint --> I (Optional);
    end
```


# <explanation>

**Импорты:**

Код импортирует необходимые библиотеки для работы:
- `asyncio`: Для асинхронных операций.
- `datetime`: Для работы с датами.
- `html`: Для работы с HTML.
- `pathlib`: Для работы с путями к файлам.
- `urllib.parse`: Для работы с URL.
- `types`: Для использования `SimpleNamespace`.
- `typing`: Для указания типов данных.
- `src.logger`: Модуль для логирования.
- `src.gs`: Вероятно, модуль для работы с Google Services (не показано в коде).
- `src.suppliers.aliexpress.AliApi`: Базовый класс для работы с AliExpress API.
- `src.suppliers.aliexpress.campaign.html_generators`: Модуль для генерации HTML шаблонов.
- `src.suppliers.aliexpress.utils.ensure_https`: Функция для приведения URL к `https`.
- `src.product.product_fields`:  Модуль, содержащий определения полей продукта.
- `src.utils.image`: Для сохранения изображений.
- `src.utils.video`: Для сохранения видео.
- `src.utils.file`: Для работы с файлами.
- `src.utils.jjson`: Для работы с JSON.
- `src.utils.pprint`: Вероятно, утилита для красивой печати.


**Классы:**

- `AliAffiliatedProducts(AliApi)`: Наследует от класса `AliApi`, добавляя функциональность для обработки партнерских ссылок и сохранения изображений/видео.
    - `language`: Язык для кампании.
    - `currency`: Валюта для кампании.
    - `__init__`: Инициализирует класс с параметрами языка и валюты, вызывая инициализацию базового класса `AliApi`.
    - `process_affiliate_products`:  Метод для обработки списка продуктовых ID или URL.  
     - Принимает на вход список `prod_ids` (продуктовые ID или URL) и директорию `category_root` для сохранения результатов.
     - Возвращает список обработанных продуктов в виде `SimpleNamespace`.

**Функции:**

- `ensure_https`: Приводит URL к виду `https`.
- `save_png_from_url`: Сохраняет изображение из URL.
- `save_video_from_url`: Сохраняет видео из URL.
- `j_dumps`: Сохраняет объект в JSON файл.
- `save_text_file`: Сохраняет текст в текстовый файл.

**Переменные:**

- `_promotion_links`, `_prod_urls`: Временные списки для хранения партнерских ссылок и URL.
- `normilized_prod_urls`: Список нормализованных URL.
- `print_flag`:  Флаг для печати в консоль (не очень типичный подход, можно улучшить).
- `product_titles`: Список названий продуктов.
- `affiliated_products_list`: Список обработанных продуктов.


**Возможные ошибки и улучшения:**

- **Обработка исключений:** Не хватает обработки возможных исключений (например, при получении данных по URL или сохранении файлов).
- **Проверка корректности ввода:** Нужно проверять `prod_ids` на корректность (валидация URL-адресов и т. д.).
- **Производительность:** Асинхронность используется, но проверьте, что асинхронные операции действительно ускоряют работу с большим количеством данных.
- **Улучшение логирования:** Используйте более детальное и структурированное логирование для отладки и мониторинга.
- **Обработка пустых данных:** Проверки на пустоту `_promotion_links` и `_affiliated_products` могли бы быть более явными.


**Взаимосвязи с другими частями проекта:**

Код зависит от `AliApi` (для получения партнерских ссылок), `save_png_from_url`, `save_video_from_url`, `j_dumps`, `save_text_file`, `logger` и других функций и классов из модулей `src`.  Это указывает на модульную архитектуру проекта, где отдельные части отвечают за конкретные задачи.