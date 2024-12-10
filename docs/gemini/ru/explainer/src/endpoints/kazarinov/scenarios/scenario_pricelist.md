```MD
# <input code>

```python
from __future__ import annotations
## \file hypotez/src/endpoints/kazarinov/scenarios/scenario_pricelist.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль исполнения сценария создания мехирона для Сергея Казаринова
==================================================================

```rst
.. module:: src.endpoints.kazarinov.scenarios 
	:platform: Windows, Unix
	:synopsis: Provides functionality for extracting, parsing, and processing product data from 
various suppliers. The module handles data preparation, AI processing, 
and integration with Facebook for product posting.
```

"""
MODE = 'dev'

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

from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.file import read_text_file, save_text_file, recursively_get_file_path
from src.utils.image import save_png_from_url, save_png
from src.utils.convertors.unicode import decode_unicode_escape
from src.utils.printer import pprint
from src.logger import logger


class MexironBuilder:
    """
    Обрабатывает извлечение, разбор и сохранение данных о продуктах поставщиков.

    Attributes:
        driver (Driver): Экземпляр Selenium WebDriver.
        export_path (Path): Путь для экспорта данных.
        products_list (List[dict]): Список обработанных данных о продуктах.
    """

    driver: Driver
    export_path: Path
    mexiron_name: str
    price: float
    timestamp: str
    products_list: List = field(default_factory=list)
    model: GoogleGenerativeAI
    config: SimpleNamespace

    def __init__(self, driver: Driver, mexiron_name: Optional[str] = None):
        """
        Initializes Mexiron class with required components.

        Args:
            driver (Driver): Selenium WebDriver instance.
            mexiron_name (Optional[str]): Custom name for the Mexiron process.
        """
        # ... (rest of the __init__ method)
    
    # ... (rest of the class methods)
```

# <algorithm>

**Блок-схема алгоритма:**

```mermaid
graph TD
    A[Начало] --> B{URL доступны?};
    B -- Да --> C[Обработка URL];
    B -- Нет --> D[Ошибка: Нет URL];
    C --> E[Запрос данных через грабер];
    E --> F{Данные валидны?};
    F -- Да --> G[Конвертация данных];
    F -- Нет --> H[Ошибка: Невалидные данные];
    G --> I[Сохранение данных в файл];
    I --> J[Обработка данных AI (ru)];
    J --> K[Сохранение результатов AI (ru)];
    C --> L[Обработка данных AI (he)];
    L --> M[Сохранение результатов AI (he)];
    I --> N[Создание отчета (html, pdf)];
    N --> O[Отправка на Facebook (опционально)];
    O --> P[Успех];
    H --> Q[Ошибка];
    D --> Q;
    G --> Q;
    J --> Q;
    L --> Q;
    I --> Q;
    M --> Q;
    N --> Q;
    P --> A;
    Q --> A;
```

**Пример:**

Пользователь предоставляет список URL. Код обрабатывает каждый URL, извлекая данные с помощью соответствующего грабера. Полученные данные проверяются на валидность. Если данные валидны, они конвертируются в формат, удобный для AI. Затем данные сохраняются в файлы. AI обрабатывает данные и возвращает результат на русском и иврите. Результаты сохраняются в отдельные файлы. Далее генерируется отчет (html, pdf). Опционально, отчет отправляется на Facebook. Если на каком-либо шаге возникла ошибка, выполнение останавливается.


# <mermaid>

```mermaid
graph LR
    subgraph MexironBuilder
        A[MexironBuilder] --> B(run_scenario);
        B --> C{URL is from OneTab?};
        C -- Yes --> D[Get data from OneTab];
        C -- No --> E[Reply - Try again];
        D --> F{Data valid?};
        F -- Yes --> G[Run Mexiron scenario];
        F -- No --> H[Reply Incorrect data];
        G --> I{Scenario successful?};
        I -- Yes --> J[Reply Done! I will send the link to WhatsApp];
        I -- No --> K[Reply Error running scenario];
        H --> L[Return];
        J --> L;
        E --> L;
        K --> L;
    end
    subgraph Data Processing
        G --> M[process_ai(products_list, 'he')];
        G --> N[process_ai(products_list, 'ru')];
        M --> O[Save 'he' results];
        N --> P[Save 'ru' results];
        O --> Q[Create report (html, pdf)];
        P --> Q;
        M --> R;
        N --> S;
        Q --> T[Post to Facebook (optional)];
    end
    J --> T;
    T --> U[Success];
    L --> V[Error];
    V --> U;
```

**Объяснение зависимостей:**

Диаграмма показывает взаимосвязи между `MexironBuilder` и подключаемыми модулями:
* `gs`: для доступа к глобальным переменным и конфигурации.
* `ProductFields`: для работы с данными о продуктах.
* `Driver`: для работы с Selenium.
* `GoogleGenerativeAI`: для работы с AI моделью Gemini.
* Модули граберов (MorleviGraber, KspGraber, IvoryGraber, GrandadvanceGraber): для извлечения данных с веб-страниц.
* `ReportGenerator`: для создания отчетов.
* Модули `src.utils.*`: для различных вспомогательных функций (работы с файлами, изображениями, кодированием и т. д.).
* `src.logger`: для регистрации сообщений об ошибках и отладочных данных.
* `facebook` модули: для отправки сообщений в Facebook.

# <explanation>

**Импорты:**

Импорты необходимы для использования функций и классов из других модулей, включая те, которые находятся в подпакетах проекта `src`.  Это типичная структура импорта для организации кода Python.


**Классы:**

* **`MexironBuilder`:**  Класс для обработки данных о продуктах.
    * `driver`: Экземпляр `Driver` (Selenium WebDriver) - для взаимодействия с веб-страницами.
    * `export_path`: Путь для сохранения обработанных данных.
    * `products_list`: Список данных о продуктах после обработки.
    * `model`: Экземпляр `GoogleGenerativeAI` - для использования AI модели.
    * `config`: Настройка из файла `kazarinov.json`.
    * `__init__`: Инициализирует класс с данными о поставщиках, путем для сохранения данных, AI моделью.
    * `run_scenario`: Обрабатывает список URL, извлекает данные, отправляет их на обработку AI, сохраняет результаты, отправляет отчет в Facebook (опционально).
    * `get_graber_by_supplier_url`: Выбирает соответствующий грабер для конкретного поставщика.
    * `convert_product_fields`: Преобразует данные, полученные от грабера, в формат, подходящий для модели AI.
    * `save_product_data`: Сохраняет данные о каждом продукте в файл.
    * `process_ai`: Обрабатывает данные с помощью AI модели.
    * `post_facebook`: Отправляет данные в Facebook.
    * `create_report`: Создает отчеты.


**Функции:**

* `run_scenario`:  Основная функция сценария, обрабатывающая полученные URL.
* `get_graber_by_supplier_url`: Выбирает грабер в зависимости от URL поставщика.
* `convert_product_fields`: Форматирует данные о продуктах.
* `save_product_data`: Сохраняет данные о продукте в файл.
* `process_ai`: Обрабатывает данные с помощью модели AI, переводя их на нужные языки.
* `post_facebook`: Отправляет данные в Facebook (если нужно).
* `create_report`: Создаёт отчет в формате html и pdf.



**Переменные:**

Переменные хранят пути к файлам, результаты обработки, параметры, настройки.


**Возможные ошибки и улучшения:**

* **Обработка ошибок:** В коде есть блоки `try...except`, но обработка ошибок могла бы быть более всесторонней. Например, стоит проверять, что файлы `kazarinov.json` и инструкционные файлы существуют и доступны для чтения.
* **Переменная `attempts` в `process_ai`:** Необходимо обеспечить максимальное количество попыток при обращении к AI-модели. Если модель выдает ошибку или не отвечает, необходимо реализовать ограничение по количеству попыток для предотвращения бесконечного цикла.
* **Логирование:** Логирование ошибок имеет определённую структуру, которая позволяет отследить и проанализировать происходящее.


**Взаимосвязи с другими частями проекта:**

Код взаимодействует с различными модулями и классами, которые находятся в пакетах `src.*`. Например, с `gs` для доступа к глобальным переменным, `Driver` для управления браузером, `GoogleGenerativeAI` для обработки данных, граберами для получения данных от поставщиков и т. д.  Это указывает на общую архитектуру проекта, основанную на модульном подходе.