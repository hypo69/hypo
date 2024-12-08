```MD
# <input code>

```python
## \file hypotez/src/ai/gemini/generative_ai.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.ai.gemini
   :platform: Windows, Unix
   :synopsis: Google generative AI integration
   https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai.md
"""

MODE = 'dev'
import time
import json
from io import IOBase
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict
from types import SimpleNamespace
import base64

import google.generativeai as genai
import requests

from grpc import RpcError
from google.api_core.exceptions import (
    GatewayTimeout,
    ServiceUnavailable,
    ResourceExhausted,
    InvalidArgument,
)
from google.auth.exceptions import DefaultCredentialsError, RefreshError
from src.logger import logger
from src import gs
from src.utils.printer import pprint
from src.utils.file import read_text_file, save_text_file
from src.utils.date_time import TimeoutCheck
from src.utils.convertors.unicode import decode_unicode_escape
from src.utils.jjson import j_loads, j_loads_ns, j_dumps

timeout_check = TimeoutCheck()

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.
    ... (документация)
    """
    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, ...):
        """
        Инициализация модели GoogleGenerativeAI.
        ... (документация)
        """
        # ... (инициализация атрибутов)
        self.model = genai.GenerativeModel(...)
        self._chat = self._start_chat()


    @property
    def config():
        return j_loads_ns(gs.path.src / 'ai' / 'gemini' / 'generative_ai.json')


    def _start_chat(self):
        return self.model.start_chat(history=[])

    def _save_dialogue(self, dialogue: list):
        # Сохраняет диалоги в текстовые и JSON файлы.
        save_text_file(dialogue, self.history_txt_file, mode='+a')
        for message in dialogue:
            j_dumps(data=message, file_path=self.history_json_file, mode='+a')


    def ask(self, q: str, attempts: int = 15) -> Optional[str]:
        """
        Отправляет запрос модели и возвращает ответ.
        """
        for attempt in range(attempts):
            # ... (обработка запроса, исключений и логирования)
            return response.text
        return

    def chat(self, q: str) -> str:
        # ...
        return response.text

    def describe_image(self, image_path: Path) -> Optional[str]:
        # ...
        return response.text


    def upload_file(self, file: str | Path | IOBase, file_name:Optional[str] = None) -> bool:
        """
        Загрузка файла в Google Cloud Storage.
        """
        # ... (загрузка файла с обработкой возможных ошибок)


if __name__ == "__main__":
    # ... (тестовый код)
```

# <algorithm>

**Шаг 1: Инициализация**

* При создании объекта `GoogleGenerativeAI` устанавливаются API-ключ, имя модели, конфигурация и инструкция для системы.
* Настраивается логирование диалогов и сохранение истории.
* Создается экземпляр `genai.GenerativeModel` с указанными параметрами.
* Инициализируется `self._chat`.

**Шаг 2: Отправка запроса**

* Метод `ask` принимает вопрос (`q`) и отправляет его модели.
* Цикл `for` реализует механизм повторных попыток, если возникла ошибка.
* Внутри цикла выполняется запрос `self.model.generate_content(q)`.
* При успешном ответе сохраняется диалог, и возвращается текст ответа.
* При ошибках (например, сетевые, аутентификации, превышение квоты) выполняется повторная попытка со случайной задержкой.

**Шаг 3: Обработка ответа**

* В случае успешного ответа генерируется список `messages` с ролью пользователя и помощника.
* Метод `_save_dialogue` сохраняет этот список в файлы.
* Если ответ не получен, выполняется задержка.

**Шаг 4: Загрузка файла**

* Метод `upload_file` загружает файл в Google Cloud Storage.
* Обрабатываются возможные ошибки (ошибки запроса, отсутствие файла).
* Возможна повторная загрузка, если произошла ошибка.

**Шаг 5: Описание изображения**

* Метод `describe_image` загружает изображение, кодирует его в base64, и отправляет в модель.
* Возвращает описание изображения.



# <mermaid>

```mermaid
graph TD
    A[GoogleGenerativeAI] --> B(init);
    B --> C{api_key, model_name, config};
    C --> D[genai.GenerativeModel];
    D --> E{_start_chat};
    E --> F[ask(q)];
    F --> G{success?};
    G -- yes --> H[save_dialogue];
    H --> I[return response];
    G -- no --> J{error type?};
    J -- network error --> K[retry(sleep)];
    J -- authentication error --> L[return];
    J -- service unavailable --> K;
    J -- resource exhausted --> K;
    K --> F;
    F --> G;
    A --> M[upload_file(file)];
    M --> N{success?};
    N -- yes --> O[return response];
    N -- no --> P[retry/error handling];
    A --> Q[describe_image(image_path)];
    Q --> R{success?};
    R -- yes --> S[return description];
    R -- no --> T[error handling];
```

**Подключаемые зависимости:**

* `google.generativeai`: Для взаимодействия с API Google Generative AI.
* `requests`: Для отправки HTTP-запросов.
* `grpc`, `google.api_core.exceptions`, `google.auth.exceptions`: Для обработки ошибок и коммуникации с gRPC сервисом.
* `src.logger`, `src.gs`, `src.utils.printer`, `src.utils.file`, `src.utils.date_time`, `src.utils.convertors.unicode`, `src.utils.jjson`: Подключаемые модули из других частей проекта для логирования, работы с файлами, датами, обработкой JSON и т.д.


# <explanation>

**Импорты:**

* `google.generativeai`:  Ключевой импорт для доступа к API Google Generative AI.  Он предоставляет интерфейс для взаимодействия с моделями, такими как Gemini.
* `requests`: Для выполнения HTTP-запросов. Используется для взаимодействия с API.
* `grpc`, `google.api_core.exceptions`, `google.auth.exceptions`: Библиотеки, необходимые для обработки  gRPC запросов и ошибок, возникающих при авторизации.  Это связано с API Google Generative AI, который использует gRPC.
* `src.*`: Импортируются модули из собственной структуры проекта. Это позволяет использовать функции, классы, переменные и конфигурации из других частей проекта, что демонстрирует модульную организацию кода. Например, `src.logger` для логирования, `src.gs` для работы с файловой системой, утилиты для работы с файлами, временем, и конфигурациями.

**Классы:**

* `GoogleGenerativeAI`:  Класс для взаимодействия с Google Generative AI.
    * `MODELS`: Список поддерживаемых моделей.
    * `api_key`, `model_name`, `generation_config`, `system_instruction`:  Параметры, необходимые для инициализации и настройки модели.
    * `dialogue_log_path`, `dialogue_txt_path`, `history_dir`, `history_txt_file`, `history_json_file`:  Пути для сохранения диалогов и истории.
    * `model`: Объект `genai.GenerativeModel` для взаимодействия с моделью.
    * `_chat`: Для работы с чатом.
    * `ask`, `chat`, `describe_image`, `upload_file`:  Методы для выполнения различных операций.


**Функции:**

* `ask`: Отправляет вопрос модели и обрабатывает возможные ошибки. Возвращает ответ или `None`, если запрос не удался. Обрабатывает повторные попытки, задержки и типы исключений.
* `upload_file`: Загружает файл на сервер.  Важно, что функция обрабатывает возможные ошибки и предпринимает действия для восстановления, например, удаляет файл при ошибке.
* `describe_image`: Описывает изображение, отправляя его в модель.
* `_save_dialogue`: Сохраняет диалоги в текстовые и JSON-файлы, используя функции из `src.utils`.
* `_start_chat`: Инициализирует чат с моделью.


**Переменные:**

* `MODE`: Переменная для определения режима работы (например, `'dev'` или `'production'`).
* `timeout_check`: Объект для проверки таймаутов.


**Возможные ошибки и улучшения:**

* **Обработка ошибок:** Код содержит много `try...except` блоков, что полезно для обработки различных исключений (сетевые ошибки, таймауты, ошибки авторизации и др.). Однако, можно добавить более подробные сообщения об ошибках, которые помогут в отладке.
* **Более гибкая конфигурация:** Можно добавить возможность настройки параметров (например, таймауты, максимальное количество попыток) в виде конфигурационного файла.
* **Извлечение логики:** Небольшие повторяющиеся фрагменты кода (обработка ошибок, задержка) можно вынести в отдельные функции для улучшения читаемости.
* **Управление файлами:**  В функции `upload_file` есть рекурсивный вызов, что может быть неоптимальным, необходимо проанализировать и убрать или заменить его на более эффективный метод.
* **Документация:** Документация (внутри класса, функций) может быть более подробной и содержать примеры использования.


**Взаимосвязь с другими частями проекта:**

Код использует функции и классы из других модулей, входящих в `src`, например, `src.logger`, `src.gs` (`gs.now`, `gs.path`), `src.utils`, что указывает на модульную архитектуру проекта.  Это позволяет использовать общие функции и переменные из других модулей.