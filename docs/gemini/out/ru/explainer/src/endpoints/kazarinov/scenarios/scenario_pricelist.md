# <input code>

```python
## \file hypotez/src/endpoints/kazarinov/scenarios/scenario_pricelist.py
# -*- coding: utf-8 -*-\

#! venv/bin/python/python3.12

"""
.. module: src.endpoints.kazarinov.scenarios 
	:platform: Windows, Unix
	:synopsis: Provides functionality for extracting, parsing, and processing product data from 
various suppliers. The module handles data preparation, AI processing, 
and integration with Facebook for product posting.

"""


import asyncio
import random
import shutil
from pathlib import Path
from typing import Optional, List
from types import SimpleNamespace
from dataclasses import field

import header
from src import gs
from src.product.product_fields import ProductFields
from src.webdriver.driver import Driver
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.advertisement.facebook.scenarios import (
    post_message_title, upload_post_media, message_publish
)
from src.suppliers.morlevi.graber import Graber as MorleviGraber
from src.suppliers.ksp.graber import Graber as KspGraber
from src.suppliers.ivory.graber import Graber as IvoryGraber
from src.suppliers.grandadvance.graber import Graber as GrandadvanceGraber
from src.endpoints.kazarinov.pricelist_generator import ReportGenerator
from telegram import Update
from telegram.ext import CallbackContext

from src.utils.jjson import j_loads_ns, j_dumps
from src.utils.file import read_text_file, save_text_file, recursively_get_file_path
from src.utils.image import save_png_from_url, save_png
from src.utils.convertors.unicode import decode_unicode_escape
from src.utils.printer import pprint
from src.logger import logger


class Mexiron:
    """
    Handles suppliers' product extraction, parsing, and saving processes.

    Supported suppliers:
    - https://morlevi.co.il
    - https://ivory.co.il
    - https://ksp.co.il
    - https://grandadvance.co.il
    """

    # Class attributes
    driver: Driver
    export_path: Path
    mexiron_name: str
    price: float
    timestamp: str
    products_list: List = field(default_factory=list)
    model: GoogleGenerativeAI
    model_command: str
    config: SimpleNamespace

    def __init__(self, driver: Driver, mexiron_name: Optional[str] = None):
        """
        Initializes Mexiron class with required components.

        Args:
            driver (Driver): Selenium WebDriver instance.
            mexiron_name (Optional[str]): Custom name for the Mexiron process.
        """
        # ... (rest of the __init__ method)
```

# <algorithm>

**Пошаговая блок-схема:**

1. **Инициализация Mexiron:**
    - Загрузка конфигурации из `kazarinov.json`.
    - Получение текущей даты и времени.
    - Установка имени Mexiron (по умолчанию - timestamp).
    - Определение пути для экспорта данных.
    - Загрузка системных инструкций и команд для модели AI.
    - Инициализация модели GoogleGenerativeAI.

2. **Выполнение сценария (run_scenario):**
    - Получение списка URL товаров.
    - Для каждого URL:
        - Получение грабера для конкретного поставщика.
        - Получение данных о товаре с помощью грабера.
        - Преобразование полученных данных в формат, подходящий для модели AI.
        - Сохранение данных о товаре.
    - Обработка данных через AI-модель (process_ai).
    - Сохранение результата модели в `he.json` и `ru.json`.
    - Создание отчетов в HTML и PDF для каждого языка.
    - Публикация сообщений в Facebook для каждого языка.

3. **Получение грабера (get_graber_by_supplier_url):**
    - Определение грабера на основе URL.

4. **Преобразование полей товара (convert_product_fields):**
    - Преобразование данных из `ProductFields` в словарь.

5. **Сохранение данных о товаре (save_product_data):**
    - Сохранение данных о товаре в файл.

6. **Обработка данных через AI (process_ai):**
    - Подача данных о товаре в модель AI для обработки и перевода на `he` и `ru`.
    - Обработка возможных ошибок (повтор попыток, обработка ошибок).
    - Извлечение данных в `he` и `ru` форматах.

7. **Создание отчетов (create_report):**
    - Генерация отчетов в HTML и PDF форматах.

8. **Публикация в Facebook (post_facebook):**
    - Публикация отчетов в Facebook.


**Примеры данных:**

- **`kazarinov.json`**: Содержит настройки для Mexiron (пути к файлам, конфигурация).
- **`ProductFields`**: Объект, содержащий данные о продукте, извлеченные грабером.
- **`products_list`**: Список словарей с данными о товаре, готовыми для обработки AI.
- **Модель AI Output**: Результат обработки AI в формате словарей для `he` и `ru` языков.

**Движение данных:**

Данные о товарах извлекаются из поставщика через граберы, преобразуются в формат, понятный AI-модели, сохраняются. Результаты AI-модели сохраняются в файлы и используются для создания отчетов и публикации в Facebook.

# <mermaid>

```mermaid
graph TD
    A[Инициализация Mexiron] --> B{Загрузка конфигурации};
    B -- success --> C[Определение пути экспорта];
    B -- error --> D[Обработка ошибки];
    C --> E[Загрузка инструкций AI];
    E --> F[Инициализация AI модели];
    F --> G[Выполнение сценария (run_scenario)];
    G --> H[Получение списка URL];
    H --> I[Цикл по URL];
    I --> J[Выбор грабера];
    J --> K[Получение данных товара];
    K --> L[Преобразование в словарь];
    L --> M[Сохранение данных товара];
    I --> N[Обработка через AI (process_ai)];
    N --> O[Сохранение результатов в JSON];
    O --> P[Создание отчетов (create_report)];
    P --> Q[Публикация в Facebook (post_facebook)];
    Q -- success --> R[Завершение];
    Q -- error --> D;
    D --> D1[Обработка ошибки];
    D1 --> R;
```


# <explanation>

**Импорты:**

- `asyncio`: Для асинхронной обработки задач.
- `random`: Вероятно, используется для случайных операций (например, в целях тестирования или генерации данных).
- `shutil`: Для работы с файлами (скорее всего, копирования или удаления).
- `pathlib`: Для работы с путями к файлам.
- `typing`: Для указания типов данных (повышает читаемость и надежность кода).
- `types`:  Для работы с `SimpleNamespace`.
- `dataclasses`:  Для `field` атрибута, вероятно, для работы с данными в объектах.
- `header`: Файл с, предположительно, другими импортами или настройками.
- `gs`:  Предположительно, `global_settings` - модуль для глобальных настроек, путей, доступа к данным.
- `ProductFields`: Класс, определяющий структура данных для описания товара.
- `Driver`: Класс для управления WebDriver (Selenium).
- `GoogleGenerativeAI`: Класс для интеграции с моделью AI Gemini.
- `post_message_title`, `upload_post_media`, `message_publish`: Функции для публикации в Facebook.
- `MorleviGraber`, `KspGraber`, `IvoryGraber`, `GrandadvanceGraber`:  Граберы для различных поставщиков (парсеры HTML).
- `ReportGenerator`: Класс для генерации отчетов.
- `telegram`: Библиотека для взаимодействия с Telegram.
- `jjson`, `file`, `image`, `unicode`, `printer`, `logger`:  Утилиты для работы с JSON, файлами, изображениями, кодировками, выводом логов.
- `src.*`: указывают на структуру пакета, где находятся различные модули.


**Классы:**

- `Mexiron`: Обрабатывает загрузку, обработку и сохранение данных о продуктах от разных поставщиков. Имеет `driver`, путь к экспорту, название, цену, дату и т.д.  Инициализируется с `driver` (Selenium WebDriver) и опциональным именем.

**Функции:**

- `__init__`: Инициализирует класс `Mexiron`, загружает конфигурацию, создает путь к экспорту и инициализирует модель AI.
- `run_scenario`: Обрабатывает сценарий, получая данные из URL, обрабатывает их через AI, сохраняет результат и публикует в Facebook.
- `get_graber_by_supplier_url`: Выбирает нужный грабер (парсер HTML) на основе URL.
- `convert_product_fields`: Преобразует данные `ProductFields` в словарь.
- `save_product_data`: Сохраняет данные о товаре в JSON-файл.
- `process_ai`: Обрабатывает данные через AI-модель. Обрабатывает возможные ошибки.  Важно:  функция рекурсивно вызывает себя в случае ошибки, чтобы сделать попыток `attempts`.
- `post_facebook`: Публикует данные в Facebook, использует другие функции из модуля `src.endpoints.advertisement.facebook.scenarios`.
- `create_report`: Создает HTML и PDF отчеты на основе данных.


**Переменные:**

- `MODE`: Переменная для определения режима работы (например, `dev` или `prod`).
- `products_list`: Список данных о товаре.
- `export_path`: Путь для экспорта данных.
- `model`: Экземпляр класса модели AI.


**Возможные ошибки/улучшения:**

- Отсутствует обработка исключений в `__init__` и других местах, где `return` используется для завершения. Нужно использовать `raise` или улучшить обработку `Exception`-ов.
- Логирование ошибок не всегда используется. Рекомендовано логгировать все критические и важные события.
- Рекурсивный вызов `process_ai` потенциально может привести к проблемам (например, слишком большое количество попыток). Нужно ограничить максимальное количество попыток или использовать другую стратегию обработки ошибок.
- Обработка пустых или некорректных ответов от AI-модели не идеальна.
- Можно добавить валидацию входных данных (`urls`, `price`, etc.) для повышения стабильности.
- Код содержит большое количество `...` - нужно доработать логику.

**Связь с другими частями проекта:**

- `src.endpoints.advertisement.facebook.scenarios`: Для публикации в Facebook.
- `src.suppliers.*.graber`: Для извлечения данных от разных поставщиков.
- `src.ai.gemini`: Для обработки данных через AI-модель.
- `src.product.product_fields`: Для определения структуры данных о продукте.


**Общий вывод:**

Код представляет собой асинхронную часть приложения, отвечающую за извлечение, обработку и публикацию данных о товарах. Нужно обратить внимание на обработку ошибок, валидацию входов и потенциальные проблемы рекурсивного вызова функций.