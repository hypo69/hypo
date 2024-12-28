# <input code>

```python
## \file hypotez/src/endpoints/prestashop/api/api.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.endpoints.prestashop.api 
	:platform: Windows, Unix
	:synopsis:

"""



import os
import sys
from enum import Enum
from http.client import HTTPConnection
from requests import Session
from requests.models import PreparedRequest
from typing import Dict, List
from pathlib import Path
from xml.etree import ElementTree
from xml.parsers.expat import ExpatError

import header
from src import gs
from src.utils.file import save_text_file
from src.utils.convertors.base64 import  base64_to_tmpfile
from src.utils.convertors.dict import dict2xml
from src.utils.convertors.xml2dict import xml2dict
from src.utils.image import save_png_from_url
from src.utils.printer import pprint
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger import logger
from src.logger.exceptions import PrestaShopException, PrestaShopAuthenticationError


class Format(Enum):
    """Data types return (JSON, XML)

    @details
    @param Enum (int): 1 => JSON, 2 => XML
    @deprecated - я предпочитаю JSON 👍 :))
    """
    JSON = 'JSON'
    XML = 'XML'


class PrestaShop:
    # ... (rest of the class)
```

# <algorithm>

**Алгоритм работы класса PrestaShop:**

1. **Инициализация (\_\_init\_\_):**
   - Получает API_DOMAIN и API_KEY из gs.credentials.presta.client.
   - Инициализирует переменные debug, language и data_format.
   - Устанавливает аутентификацию для сессии.
   - Выполняет HEAD запрос к API, чтобы проверить доступность и получить версию PrestaShop.
   - Пример: `API_DOMAIN = "https://example.com/api/"` , `API_KEY = "your_api_key"`.
2. **Проверка соединения (ping):**
   - Выполняет HEAD запрос к API_DOMAIN.
   - Проверяет статус ответа (200 или 201).
   - Возвращает True, если статус успешный, иначе False.
   - Пример: проверяет доступность веб-сервиса.
3. **Обработка ошибок ответа (_check_response):**
   - Анализирует статус ответа.
   - Если статус не 200/201, вызывает _parse_response_error для обработки ошибки.
4. **Обработка ошибок (\_parse_response_error):**
   - Проверяет формат данных (JSON или XML).
   - Если JSON, логгирует ошибки.
   - Если XML, парсит XML ответ и извлекает код ошибки и сообщение.
   - Логгирует ошибки.
   - Пример: логгирование ошибок 404, 500.
5. **Подготовка запроса (_prepare):**
   - Принимает URL и параметры запроса.
   - Подготавливает URL с параметрами.
   - Возвращает подготовленный URL.
   - Пример: `url = "https://example.com/api/products/123?filter=..."`
6. **Выполнение запроса (_exec):**
   - Выполняет HTTP запрос к API.
   - Если debug = True, перенаправляет stderr в файл.
   - Проверяет статус ответа.
   - Если статус не 200/201, обрабатывает ошибки.
   - Парсит ответ в JSON или XML.
   - Возвращает данные или False.
   - Пример: запрос POST, GET, PUT, DELETE.
7. **Парсинг ответа (_parse):**
   - Парсит JSON или XML ответ.
   - Возвращает парсированные данные или False.
   - Пример: `{"PrestaShop": { ... }}` или `XML-дерево`.
8. **CRUD-операции (create, read, write, unlink, search):**
   - Выполняют запросы к API с использованием _exec для соответствующих методов (POST, GET, PUT, DELETE).
   - Примеры: создать новый продукт, прочитать продукт по id, обновить продукт, удалить продукт, найти продукты по фильтру.
9. **Загрузка файлов (create_binary):**
   - Загружает бинарный файл (например, изображение) на сервер.
   - Обрабатывает загрузку изображения.
   - Пример: загрузить изображение продукта.
10. **Сохранение данных (_save):**
    - Сохраняет полученные данные в файл в формате JSON.
    - Пример: сохраняет список продуктов в файл products.json.
11. **Получение данных (get_data):**
    - Выполняет запрос к API для получения данных.
    - Сохраняет полученные данные в файл.
    - Возвращает данные или False.
    - Пример: запрос списка продуктов и сохранение в файл.

Взаимодействие между функциями и классами основано на вызовах методов (\_exec, \_check_response, \...) и передаче данных в качестве аргументов.


# <mermaid>

```mermaid
graph LR
    A[PrestaShop API Client] --> B{Инициализация};
    B --> C[HEAD запрос к API];
    C --> D{Проверка статуса};
    D -- Успешный -- E[CRUD-операции (create, read, write, unlink, search)];
    D -- Ошибка -- F[Обработка ошибки];
    E --> G[Выполнение запроса (_exec)];
    G --> H{Парсинг ответа};
    H -- JSON -- I[Обработка JSON];
    H -- XML -- J[Обработка XML];
    I --> K[Возврат данных];
    J --> K;
    F --> L[Логирование ошибки];
    subgraph "Вспомогательные функции"
        F --> M[_parse_response_error];
        M --> N[Обработка ошибок];
        G --> O[_prepare];
        O --> G;
        H --> P[_parse];
        P --> H;
    end
    K --> Q[Сохранение в файл (_save)]
    Q --> K

    subgraph "Загрузка файлов"
        A --> S[create_binary];
        S --> T[Загрузка бинарного файла];
        T --> U[Обработка ответа];
    end
```

**Объяснение диаграммы:**

Диаграмма описывает основные методы и функции класса `PrestaShop`, отражая их взаимосвязи. `PrestaShop API Client` - это входная точка, которая отвечает за взаимодействие с API. `Инициализация` инициирует все дальнейшие запросы к API. `CRUD-операции` представляют различные методы взаимодействия с ресурсами PrestaShop API, `Выполнение запроса` содержит вызов `HTTP-запроса` к API. `Парсинг ответа` - это процесс анализа ответа, который может быть как в формате JSON, так и в формате XML.  `Обработка ошибок` содержит функцию, которая обрабатывает возможные ошибки при взаимодействии с PrestaShop API. `Загрузка файлов` выделена как отдельная ветка, отражая специализированный метод загрузки бинарных файлов. Завершающий блок `Сохранение в файл` сохраняет полученные данные в файлы.


# <explanation>

**Импорты:**

- `os`, `sys`: Стандартные библиотеки Python для работы с операционной системой и системными параметрами.
- `enum`: Для определения перечисления `Format`.
- `http.client`: Базовый модуль для работы с HTTP-соединениями.
- `requests`: Библиотека для работы с HTTP-запросами, crucial для взаимодействия с API.
- `typing`: Для объявления типов данных.
- `pathlib`: Для работы с путями файлов.
- `xml.etree.ElementTree`, `xml.parsers.expat`: Для работы с XML данными.
- `header`, `gs`, `src.utils.file`, `src.utils.convertors.base64`, `src.utils.convertors.dict`, `src.utils.convertors.xml2dict`, `src.utils.image`, `src.utils.printer`, `src.utils.jjson`, `src.logger`, `src.logger.exceptions`:  Импортирует вспомогательные классы и функции из других модулей проекта (`src`). Это демонстрирует структурированную архитектуру проекта с модулями для обработки файлов, конвертации данных (JSON/XML), логирования и работы с данными.

**Классы:**

- `Format`: Перечисление для определения форматов данных (JSON/XML).  Это вспомогательный класс для обозначения возможных типов данных.
- `PrestaShop`: Основной класс для взаимодействия с PrestaShop API. Хранит API_KEY, API_DOMAIN, настройки debug и language. Методы для всех CRUD операций (create, read, write, unlink, search, upload, etc.).  
  - Атрибуты: `client`, `debug`, `language`, `data_format`, `ps_version`, `API_DOMAIN`, `API_KEY`.
  - Методы: `__init__`, `ping`, `_check_response`, `_parse_response_error`, `_prepare`, `_exec`, `_parse`, `create`, `read`, `write`, `unlink`, `search`, `create_binary`, `_save`, `get_data`, `remove_file`, `get_apis`, `get_languages_schema`, `upload_image_async`, `upload_image`, `get_product_images`.


**Функции:**

- `__init__`: Инициализирует атрибуты класса.
- `ping`: Проверяет работоспособность API.
- `_check_response`: Обрабатывает ответ от API, проверяя статус и логгируя ошибки.
- `_parse_response_error`: Парсит XML ошибки.
- `_prepare`: Подготавливает URL запроса.
- `_exec`: Выполняет HTTP запрос.
- `_parse`: Парсит ответ (JSON/XML) и возвращает данные.
- `create`, `read`, `write`, `unlink`, `search`, `create_binary`, `get_data`, `upload_image`, ...: Обрабатывают соответствующие CRUD-операции с API.

**Переменные:**

- `MODE`:  Возможная конфигурация (не используется в коде).
- `data_format`: Тип данных запроса (JSON или XML).
- `language`: Идентификатор языка.
- `API_KEY`, `API_DOMAIN`: Ключ и домен API PrestaShop.


**Возможные ошибки и улучшения:**

- **Обработка исключений:** Обработка `ExpatError` и `ValueError` при парсинге XML/JSON. Но можно добавить более подробное логирование исключений (с типом и сообщением).
- **Переиспользование кода:** Возможно, некоторые логические блоки (например, проверка статуса ответа) можно вынести в отдельные функции для повторного использования.
- **Документация:** Дополнительные примеры использования методов класса.
- **Типизация:** Добавить более полную типизацию для аргументов и возвращаемых значений функций.
- **Дебаг:** Вместо открытия файла stderr.log можно использовать `logging` для более контролируемого логирования и управления уровнями логов.

**Взаимосвязь с другими частями проекта:**

Класс `PrestaShop` напрямую зависит от:
- `gs.credentials.presta.client`: Для получения API ключей и домена.
- `src.utils.file`: Для сохранения данных.
- `src.utils.convertors.base64`, `src.utils.convertors.dict`, `src.utils.convertors.xml2dict`: Для преобразования данных.
- `src.utils.image`: Для загрузки изображений.
- `src.logger`: Для логирования.
- `src.utils.printer`: Для печати результатов.
- `requests`: Библиотека для HTTP-запросов.


Это показывает, что код является частью более крупного проекта, использующего модули для обработки данных, логирования и взаимодействия с API.