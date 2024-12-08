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

**Пошаговая блок-схема:**

1. **Вход:** Список `prod_ids` (списки URL или ID продуктов) и `category_root` (путь к директории).
2. **Нормализация URL:** Функция `ensure_https` преобразует URL в `https`-формат.  Пример: `http://example.com/product1` -> `https://example.com/product1`.  Результат: `normilized_prod_urls`.
3. **Получение аффилированных ссылок:** Для каждого `prod_url` вызывается метод `get_affiliate_links`.  Пример: `get_affiliate_links("https://aliexpress.com/item/123456789.html")` -> список ссылок.  Результат: `_promotion_links`, `_prod_urls`.
4. **Проверка на наличие ссылок:** Если `_promotion_links` пуст, выводится предупреждение, и функция возвращает пустой список.
5. **Получение данных продукта:** Используя `retrieve_product_details` с `_prod_urls`, запрашиваются подробности о продуктах. Результат: `_affiliated_products`.
6. **Обработка продуктов:** Для каждой пары `(product, promotion_link)`:
   - Запись `product_title` в список.
   - Запись `language` и `promotion_link` в объект `product`.
   - Сохранение изображения в `images` под именем `product_id.png`. Пример: `product.product_id = 123`, сохранение в `category_root/images/123.png`.
   - Сохранение видео, если есть, в папку `videos`. Пример: `product.product_id = 456`, сохранение в `category_root/videos/456.mp4`.
   - Сохранение `product` в файл JSON в папке `language_currency`, где `language` и `currency` - значения из `self`. Пример: `category_root/en_USD/123.json`.
   - Добавление обработанного `product` в список `affiliated_products_list`.
7. **Сохранение заголовков:** Сохранение списка `product_titles` в файл `product_titles.txt` в папке `language_currency`.
8. **Возврат:** Функция возвращает список `affiliated_products_list`.

# <mermaid>

```mermaid
graph LR
    A[Вход: prod_ids, category_root] --> B{Нормализация URL (ensure_https)};
    B --> C[Получение аффилированных ссылок (get_affiliate_links)];
    C -- Успех --> D[Проверка на наличие ссылок];
    C -- Нет ссылок --> E[Возврат пустого списка];
    D -- Есть ссылки --> F[Получение данных продукта (retrieve_product_details)];
    F --> G[Обработка продуктов];
    G --> H[Сохранение изображения];
    G --> I[Сохранение видео (если есть)];
    G --> J[Сохранение JSON];
    G --> K[Добавление в список];
    K --> L[Сохранение заголовков];
    L --> M[Возврат списка affiliated_products_list];
    E --> M;
```

**Зависимости:**

* `src.logger`: Логирование.
* `src.gs`: Вероятно, Google Cloud Storage (но не критично для понимания).
* `src.suppliers.aliexpress.AliApi`: Базовый класс для работы с AliExpress API.
* `src.suppliers.aliexpress.campaign.html_generators`: Генерация HTML для рекламных кампаний.
* `src.suppliers.aliexpress.utils.ensure_https`: Преобразование URL к https.
* `src.product.product_fields`: Структура данных продукта.
* `src.utils.image`: Сохранение изображений.
* `src.utils.video`: Сохранение видео.
* `src.utils.file`: Работа с файлами.
* `src.utils.jjson`: Работа с JSON.
* `src.utils.printer`: Печать данных.


# <explanation>

**Импорты:**

* `asyncio`: Для асинхронных операций (важно для работы с веб-сервисами).
* `datetime`: Для работы с датами и временем (не используется непосредственно в данном коде).
* `html`: Для работы с HTML-кодом (не используется непосредственно в данном коде).
* `pathlib`: Для работы с путями к файлам.
* `urllib.parse`: Для работы с URL.
* `types`: Для использования `SimpleNamespace`.
* `typing`: Для определения типов данных.
* `src.logger`: Модуль для логирования.
* `src.suppliers.aliexpress`: Модуль с классами для взаимодействия с AliExpress API.
* `src.suppliers.aliexpress.campaign.html_generators`: Модуль для генерации HTML.
* `src.suppliers.aliexpress.utils.ensure_https`: Функция для преобразования URL к https.
* `src.product.product_fields`: Модуль с определениями полей данных продукта.
* `src.utils.image`: Модуль для сохранения изображений.
* `src.utils.video`: Модуль для сохранения видео.
* `src.utils.file`: Модуль для работы с файлами.
* `src.utils.jjson`: Модуль для работы с JSON.
* `src.utils.printer`: Модуль для вывода данных в удобном формате.

**Классы:**

* `AliAffiliatedProducts`: Наследуется от `AliApi`, расширяет функционал для работы с аффилированными продуктами. Содержит данные о языке и валюте кампании.  Метод `__init__` инициализирует язык и валюту, проверяет их наличие и вызывает `super().__init__` для инициализации базового класса.  `process_affiliate_products` - ключевой метод, обрабатывающий получение, сохранение и форматирование данных о продуктах.


**Функции:**

* `process_affiliate_products`: Основная асинхронная функция для обработки списка `prod_ids`.  Принимает `prod_ids` (список URL или ID продуктов) и `category_root` (путь к папке для сохранения данных). Возвращает список `SimpleNamespace`-объектов с обработанными продуктами.

**Переменные:**

* `MODE`, `language`, `currency`: Хранят настройки и конфигурацию.

**Возможные ошибки/улучшения:**

* **Обработка ошибок:** Не хватает явной обработки исключений при работе с внешними ресурсами (веб-сайтом AliExpress).  Нужно добавить обработку `try...except` блоков для предотвращения аварийных остановок.
* **Управление ресурсами:** В случае ошибки при сохранении изображения/видео может остаться неполная информация. Рекомендуется добавить обработку исключений и логов ошибок при взаимодействии с внешними ресурсами.
* **Улучшение логирования:** Более подробное логирование для отладки и диагностики проблем.
* **Проверка на пустые результаты:**  Рекомендуется проверять на пустые результаты `get_affiliate_links()` и `retrieve_product_details()` для избежания ошибок.
* **Тип `category_root`:**  `category_root` может быть как строкой, так и `Path`.  Это может привести к ошибкам.


**Взаимосвязи с другими частями проекта:**

* Зависит от `AliApi` для получения аффилированных ссылок.
* Использует `save_png_from_url`, `save_video_from_url`, `j_dumps`, `save_text_file` из других модулей `src.utils`.
* Использует `logger` из `src.logger`, что указывает на централизованную систему логирования.
* Использует `ProductFields` для доступа к полям продукта.


В целом, код имеет структурированную архитектуру и хорошо документирован.  Добавление обработки ошибок и более подробного логирования значительно улучшит его надёжность и поддержку.