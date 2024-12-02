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
```

# <algorithm>

**Шаг 1:** Получение списка продуктов `prod_ids`.

**Шаг 2:** Нормализация ссылок на продукты (добавление `https://`): `ensure_https(prod_ids)`.

**Шаг 3:** Итерация по нормализованным ссылкам:
    * **Шаг 3.1:** Получение партнерских ссылок с помощью родительского класса `AliApi`: `super().get_affiliate_links(prod_url)`.
    * **Шаг 3.2:** Проверка наличия партнерской ссылки. Если ссылка найдена, сохранение ссылки и исходной ссылки в соответствующие списки. Логирование успешного нахождения ссылки.
    * **Шаг 3.3:** Если партнерская ссылка не найдена, пропускаем текущую ссылку.

**Шаг 4:** Проверка наличия сохраненных партнерских ссылок. Если ссылок нет, логируем предупреждение и возвращаем пустой список.

**Шаг 5:** Получение деталей продукта по партнерским ссылкам `retrieve_product_details(_prod_urls)`.

**Шаг 6:** Итерация по полученным данным и партнерским ссылкам.
    * **Шаг 6.1:** Сохранение заголовка продукта.
    * **Шаг 6.2:** Установка языка и партнерской ссылки для объекта продукта.
    * **Шаг 6.3:** Сохранение изображения продукта в указанную директорию.
    * **Шаг 6.4:** Если у продукта есть видео, сохранение видео в указанную директорию.
    * **Шаг 6.5:** Сохранение данных продукта в файл JSON.

**Шаг 7:** Сохранение списка заголовков продуктов в текстовый файл.

**Шаг 8:** Возвращение списка обработанных продуктов.


# <mermaid>

```mermaid
graph TD
    A[process_affiliate_products] --> B{Нормализация ссылок};
    B -- Да --> C[Итерация по ссылкам];
    B -- Нет --> D[Логирование предупреждения и возврат пустого списка];
    C --> E{Партнерская ссылка найдена?};
    E -- Да --> F[Сохранение ссылки и исходной ссылки];
    E -- Нет --> C;
    F --> G[Получение деталей продукта];
    G --> H[Итерация по продуктам];
    H --> I[Сохранение изображения];
    H --> J[Сохранение видео (если есть)];
    H --> K[Сохранение данных в JSON];
    K --> L[Сохранение списка заголовков];
    H --> M[Возврат списка продуктов];
    D --> M;
    style F fill:#ccf,stroke:#333,stroke-width:2px;
    style G fill:#ccf,stroke:#333,stroke-width:2px;
    style H fill:#ccf,stroke:#333,stroke-width:2px;
    style I fill:#ccf,stroke:#333,stroke-width:2px;
    style J fill:#ccf,stroke:#333,stroke-width:2px;
    style K fill:#ccf,stroke:#333,stroke-width:2px;
    style L fill:#ccf,stroke:#333,stroke-width:2px;
    style M fill:#ccf,stroke:#333,stroke-width:2px;

    subgraph AliApi
        F --> N[get_affiliate_links];
        G --> O[retrieve_product_details];
    end
```

**Зависимости:**

*   `src.logger`:  Модуль для логирования.
*   `src.gs`:  Неизвестная библиотека, предполагается, что используется для работы с Google Cloud Storage.
*   `src.suppliers.aliexpress.AliApi`:  Класс, предоставляющий API для взаимодействия с AliExpress.
*   `src.suppliers.aliexpress.campaign.html_generators`:  Классы для генерации HTML-кода страниц рекламных кампаний.
*   `src.suppliers.aliexpress.utils.ensure_https`:  Функция для приведения ссылок к формату `https`.
*   `src.product.product_fields`:  Модуль для определения полей данных продукта.
*   `src.utils.image`:  Модуль для сохранения изображений.
*   `src.utils.video`:  Модуль для сохранения видео.
*   `src.utils.file`:  Модуль для работы с файлами (чтение, запись).
*   `src.utils.jjson`:  Модуль для работы с JSON.
*   `src.utils.pprint`:  Функция для красивой печати данных.
*   `datetime`, `html`, `pathlib`, `urllib.parse`, `types`, `typing`: Стандартные библиотеки Python.



# <explanation>

**Импорты:**

Код импортирует необходимые библиотеки и модули из проекта `src`.  Это типичный подход для организации кода в Python проектах с использованием пакета `src` в качестве корневого пакета, который содержит все собственные модули.

**Классы:**

*   `AliAffiliatedProducts(AliApi)`:  Этот класс наследуется от класса `AliApi`, расширяя его функциональность для получения и обработки данных о партнерских продуктах AliExpress.  Он содержит методы для работы с API AliExpress и сохранения полученных данных. Атрибуты `language` и `currency` хранят язык и валюту, которые используются для дальнейшей обработки данных.

**Функции:**

*   `process_affiliate_products`: Функция асинхронная, принимает список `prod_ids` (ссылки или id продуктов) и путь к директории `category_root`. Возвращает список объектов `SimpleNamespace`, содержащих данные о продуктах с партнерскими ссылками и сохранёнными изображениями.  Функция обрабатывает полученные ссылки, извлекает партнерские ссылки, сохраняет изображения и видео продуктов, и сохраняет данные о продуктах в json файлы.


**Переменные:**

*   `_promotion_links`, `_prod_urls`: Вспомогательные списки, используемые для хранения партнерских ссылок и исходных ссылок продуктов.
*   `normilized_prod_urls`: Нормализованный список ссылок на продукты.
*   `category_root`: Путь к директории, в которую будут сохраняться изображения и видео продуктов.

**Возможные ошибки и улучшения:**

*   **Обработка ошибок:**  Код содержит проверки на пустые списки, но может быть расширен для обработки других возможных ошибок (например, при сбое загрузки изображения или видео).
*   **Тестирование:**  Необходимо добавить тесты для проверки корректности работы функции `process_affiliate_products`.
*   **Исключения:**  Использование исключений для обработки ошибок может повысить надежность кода.
*   **Типы данных:**  Явное указание типов данных (например, для `prod_ids` и `category_root`) могло бы сделать код более понятным.


**Взаимосвязи с другими частями проекта:**

Класс `AliAffiliatedProducts` использует другие классы и функции из проекта `src`, такие как `AliApi`, `save_png_from_url`, `save_video_from_url`, `j_dumps`, `logger`, `ensure_https`.  Это указывает на то, что данный модуль является частью более широкой инфраструктуры, связанной с обработкой данных о продуктах и созданием рекламных кампаний.