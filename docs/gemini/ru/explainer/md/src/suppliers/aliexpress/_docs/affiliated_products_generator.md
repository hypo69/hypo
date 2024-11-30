# Анализ кода `affiliated_products_generator.py`

## <input code>

```python
import asyncio
from itertools import count
from math import log
from pathlib import Path
from typing import List, Union, Optional
from types import SimpleNamespace
from urllib.parse import urlparse, parse_qs

from src import gs
from src.suppliers.aliexpress import AliApi
from src.suppliers.aliexpress import Aliexpress
from src.suppliers.aliexpress.affiliate_links_shortener_via_webdriver import AffiliateLinksShortener
from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids
from src.suppliers.aliexpress.utils.set_full_https import ensure_https
from src.utils.convertor.csv2json import csv2dict 
from src.utils import j_dumps
from src.utils import save_png_from_url, save_video_from_url
from src.utils import pprint 
from src.utils.file import read_text_file, save_text_file

from src.logger import logger
```

```python
class AliAffiliatedProducts(AliApi):
    """ Class to collect full product data from URLs or product IDs
    locator_description For more details on how to create templates for ad campaigns, see the section `Managing Aliexpress Ad Campaigns`
    @code
    # Example usage:
    prod_urls = ['123','456',...]
    prod_urls = ['https://www.aliexpress.com/item/123.html','456',...]

    parser = AliAffiliatedProducts(
                                campaign_name,
                                campaign_category,
                                language,
                                currency)

    products = parser._affiliate_product(prod_urls)
    @endcode
    """
    campaign_name: str
    campaign_category: Optional[str]
    campaign_path: Path
    language: str
    currency: str

    def __init__(self,
             campaign_name: str,
             campaign_category: Optional[str] = None,
             language: str = 'EN',
             currency: str = 'USD',
             *args, **kwargs):
        """
        @param campaign_name `str`: Name of the advertising campaign. The directory with the prepared material is taken by name.
        @param campaign_category `Optional[str]`: Category for the campaign (default None).
        @param language `str`: Language for the campaign (default 'EN').
        @param currency `str`: Currency for the campaign (default 'USD').
        @param tracking_id `str`: Tracking ID for Aliexpress API.
        """
        super().__init__(language, currency)

        self.campaign_name = campaign_name
        self.campaign_category = campaign_category
        self.language = language
        self.currency = currency
        self.locale = f"{self.language}_{self.currency}"
        self.campaign_path = gs.path.google_drive / 'aliexpress' / 'campaigns' / self.campaign_name / 'categories' / self.campaign_category
    
    def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
        # ... (rest of the code)
    
    def delete_product(self, product_id: str, exc_info: bool = False):
        # ... (rest of the code)
```

## <algorithm>

**Шаг 1:** Инициализация `AliAffiliatedProducts`.  
    * Принимаются параметры `campaign_name`, `campaign_category`, `language`, `currency`.
    * Создается путь к директории кампании (`self.campaign_path`).
    * Вызывается конструктор родительского класса `AliApi` для инициализации общих параметров.

**Шаг 2:** Обработка списка `prod_urls`.
    * `ensure_https`: Преобразует список `prod_urls` к формату https.
    * Цикл по каждому `prod_url` в списке:
        * `get_affiliate_links`: Получение ссылки аффилиата для каждого `prod_url`.
        * Проверка наличия аффилиатов.
        * Если аффилиат найден, добавляется в `_promotion_links` и `_prod_urls`.
        * Если нет аффилиата, выводится сообщение в лог.
    * Если нет найденных аффилиатов, выводится сообщение об ошибке в лог и завершение работы функции.
    * `retrieve_product_details`: Получение данных о продуктах для ссылок в `_prod_urls`.
    * Если данные не получены, завершение работы функции.
    * Цикл по парам `product` и `promotion_link`:
        * Обработка  `promotion_link`:
            * Если `promotion_link` не существует,  пытается получить `aff_short_key` из URL.
            * Если `aff_short_key` найден, изменяет `promotion_link`.
            * Если `aff_short_key` не найден, удаляет `product` из базы (метод `delete_product`) и переходит к следующей итерации.
        * Сохранение изображения (`save_png_from_url`) в директорию кампании.
        * Сохранение видео (`save_video_from_url`), если есть ссылка.
        * Сохранение данных продукта в JSON-файл (`j_dumps`).
        * Вывод сообщения в лог о сохранении продукта.
    * Вывод сообщения в лог о количестве обработанных продуктов.
    * Возвращение списка обработанных продуктов.

**Шаг 3:**  Метод `delete_product`.
   *  Удаляет `product` из файла ссылок. Если `product_id` не найден - переименовывает соответствующий файл в файловой системе.

**Пример:**

Пусть `prod_urls` = ['url1', 'url2', 'url3']. Алгоритм последовательно обрабатывает каждый URL, получая аффилиативную ссылку и данные продукта, и сохраняет их в соответствующие файлы.

## <mermaid>

```mermaid
graph TD
    A[AliAffiliatedProducts] --> B{process_affiliate_products(prod_urls)};
    B --> C[ensure_https(prod_urls)];
    C --> D(Цикл по prod_urls);
    D --> E[get_affiliate_links(prod_url)];
    E -- аффилиат найден --> F{_promotion_links.append, _prod_urls.append};
    E -- аффилиат не найден --> G[logger.info_red];
    F --> H[retrieve_product_details(_prod_urls)];
    H -- данные получены --> I(Цикл по продуктам);
    I --> J[Обработка promotion_link];
    J -- aff_short_key найден --> K[Изменение promotion_link];
    J -- aff_short_key не найден --> L[delete_product];
    K --> M[save_png_from_url];
    L --> N[delete_product];
    M --> O[save_video_from_url];
    O --> P[j_dumps];
    P --> Q[logger.info_red];
    I -.-> R[logger.info_red(количество продуктов)];
    I --> S[return _affiliate_products];
    D -.-> T[Если нет аффилиатов, logger.error];
    
    subgraph AliApi
        E --> E1[get_affiliate_links(prod_url)];
        E1 -.-> E2;
    end
    subgraph utils
        C --> C1[ensure_https];
        H --> H1[retrieve_product_details];
        M --> M1[save_png_from_url];
        O --> O1[save_video_from_url];
        P --> P1[j_dumps];
        N --> N1[delete_product];
    end
```

**Объяснение зависимостей:**

* `AliAffiliatedProducts` зависит от `AliApi`,  что видно из `super().__init__(language, currency)`.
* Методы `save_png_from_url`, `save_video_from_url`, `j_dumps`,  `read_text_file`, `save_text_file` и т.д. из `src.utils` и `src.utils.file` используются для работы с файлами и данными.
* `extract_prod_ids`, `ensure_https` из `src.suppliers.aliexpress.utils`
* `logger` из `src.logger` используется для логгирования.
* `gs` из `src` используется для доступа к Google Drive.

## <explanation>

**Импорты:**

Код импортирует необходимые библиотеки для работы:
* Стандартные библиотеки Python (например, `asyncio`, `pathlib`, `typing`).
* Модули из проекта `src`: `gs`, `AliApi`, `Aliexpress`, `AffiliateLinksShortener`, утилиты для обработки данных и файлов, `j_dumps`, `logger`. Эти импорты указывают на организацию кода в проекте, где `src` скорее всего корневая директория, и модули вложены по иерархии.

**Классы:**

* `AliAffiliatedProducts`:  Наследуется от `AliApi` и отвечает за получение полной информации о продуктах с Aliexpress и обработку ссылок для аффилиатов, сохранение изображений и видео в локальную файловую систему.  Атрибуты `campaign_name`, `campaign_category`, `language`, `currency`  хранят параметры кампании,  `campaign_path`  путь к директории кампании, `locale` определяет язык и валюту.

**Функции:**

* `process_affiliate_products`:  Главный метод класса, принимающий список URL или ID продуктов и возвращающий обработанные данные.
* `delete_product`:  Удаляет продукт из базы по id, если у продукта нет affiliate ссылки, переименовывает файл продукта в случае отсутствия его в базе.

**Переменные:**

Переменные, использующиеся в методе `process_affiliate_products`: `prod_urls`, `_promotion_links`, `_prod_urls` и другие - хранят данные, относящиеся к обработке продуктов.


**Возможные ошибки и улучшения:**

* **Обработка ошибок:**  Хотя код содержит некоторые проверки (например, `if _link:`), он мог бы быть более устойчивым к ошибкам. Например, проверка на `FileNotFoundError` в `delete_product`,  улучшенная проверка на ошибки в HTTP-запросах и сохранении файлов.
* **Асинхронность:** Обработка запросов к API может быть асинхронной (`asyncio`) для повышения производительности при большом количестве продуктов.
* **Модульность:**  Возможно, некоторые функции, например, `delete_product`, можно выделить в отдельный модуль для повышения читабельности и повторного использования.
* **Документация:** Документация могла бы быть более подробной, особенно для сложных функций и аргументов методов.
* **Производительность:** при большом количестве продуктов, необходимо оптимизировать циклы и запросы к API, чтобы избежать ненужных задержек.
* **Обработка валидных URL:**  необходимо проверять валидность URL-адресов перед обращением к API.


**Взаимосвязи с другими частями проекта:**

Код использует множество модулей из пакета `src`, предполагая, что они содержат функции и классы, связанные с общими утилитами, логгированием, обработкой данных, и работой с файлами.  Это указывает на централизацию логики в `src` и декомпозицию проекта на подмодули.