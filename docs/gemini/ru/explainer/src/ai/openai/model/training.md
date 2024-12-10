# <input code>

```python
## \file hypotez/src/ai/openai/model/training.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.ai.openai.model 
	:platform: Windows, Unix
	:synopsis: OpenAI Model Class for handling communication with the OpenAI API and training the model

"""
MODE = 'dev'

import time
from pathlib import Path
from types import SimpleNamespace
from typing import List, Dict, Optional
import pandas as pd
from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

from src import gs
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.csv import save_csv_file  
from src.utils.printer import pprint
from src.utils.convertors.base64 import base64encode
from src.utils.convertors.md2dict import md2dict
from src.logger import logger

class OpenAIModel:
    """OpenAI Model Class for interacting with the OpenAI API and managing the model."""

    model: str = "gpt-4o-mini"
    #model: str = "gpt-4o-2024-08-06"
    client: OpenAI
    current_job_id: str
    assistant_id: str 
    assistant = None
    thread = None
    system_instruction: str
    dialogue_log_path: str | Path = gs.path.google_drive / 'AI' / f"{model}_{gs.now}.json"
    dialogue: List[Dict[str, str]] = []
    assistants: List[SimpleNamespace]
    models_list: List[str]

    def __init__(self, system_instruction: str = None, model_name:str = 'gpt-4o-mini', assistant_id: str = None):
        """Initialize the Model object with API key, assistant ID, and load available models and assistants.

        Args:
            system_instruction (str, optional): An optional system instruction for the model.
            assistant_id (str, optional): An optional assistant ID. Defaults to 'asst_dr5AgQnhhhnef5OSMzQ9zdk9'.
        """
        #self.client = OpenAI(api_key = gs.credentials.openai.project_api)
        self.client = OpenAI(api_key = gs.credentials.openai.api_key)
        self.current_job_id = None
        self.assistant_id = assistant_id or gs.credentials.openai.assistant_id.code_assistant
        self.system_instruction = system_instruction

        # Load assistant and thread during initialization
        self.assistant = self.client.beta.assistants.retrieve(self.assistant_id)
        self.thread = self.client.beta.threads.create()

    # ... (other methods)
```

# <algorithm>

(Подробная блок-схема для всех методов здесь не умещается. Приведен пример для `ask` метода)

**Метод `ask`:**

```mermaid
graph TD
    A[Пользовательский ввод] --> B{Проверка системной инструкции};
    B -- Да -- C[Формирование сообщений];
    B -- Нет -- C;
    C --> D[Отправка запроса к OpenAI API];
    D --> E{Получен ответ?};
    E -- Да -- F[Анализ тональности];
    F --> G[Добавление сообщений и тональности в диалог];
    G --> H[Сохранение диалога];
    G --> I[Возврат ответа];
    E -- Нет -- J[Обработка ошибки];
    J --> K[Повтор запроса (если попытки не исчерпаны)];
    K --> D;
    I --> L[Конец];
```

**Пример данных:**

* **A:** "Привет, как дела?"
* **B:** Да (есть системная инструкция)
* **C:**  messages = [{"role": "system", "content": "Вы - полезный помощник"}, {"role": "user", "content": "Привет, как дела?"}]
* **D:** Запрос к OpenAI API с параметрами model, messages, temperature, max_tokens
* **F:** Анализ ответа "Хорошо, спасибо!" на предмет наличия положительных, отрицательных или нейтральных слов.
* **G:** Добавление в массив `dialogue` объекта с ролью, сообщением и определённой тональностью.


# <mermaid>

```mermaid
graph LR
    subgraph OpenAIModel
        OpenAIModel --> list_models;
        OpenAIModel --> list_assistants;
        OpenAIModel --> ask;
        OpenAIModel --> describe_image;
        OpenAIModel --> describe_image_by_requests;
        OpenAIModel --> train;
        OpenAIModel --> save_job_id;
        OpenAIModel --> _save_dialogue;
        OpenAIModel --> determine_sentiment;
    end
    subgraph OpenAI API
        OpenAI API --> chat.completions.create;
    end
    subgraph Utilities
        list_models --> j_loads;
        list_assistants --> j_loads_ns;
        ask --> base64encode;
        ask --> pprint;
        ask --> j_dumps;
        describe_image --> base64encode;
        train --> j_loads;
        train --> j_dumps;
        save_job_id --> j_dumps;
        _save_dialogue --> j_dumps;
        determine_sentiment --> pprint;
    end
    list_models --> logger;
    list_assistants --> logger;
    ask --> logger;
    describe_image --> logger;
    describe_image_by_requests --> logger;
    train --> logger;
    save_job_id --> logger;
    _save_dialogue --> logger;
    determine_sentiment --> logger;

    gs --> OpenAIModel;
    gs --> save_csv_file;
    gs --> Path;
    gs --> j_dumps;
    gs --> j_loads;
    gs --> gs.now;
    gs --> gs.path.google_drive;
    gs --> gs.credentials.openai;
```

# <explanation>

**Импорты:**

Код импортирует необходимые библиотеки, включая `openai`, `requests`, `pandas`, `PIL`, `pathlib` и пользовательские модули, например `src.gs`, `src.utils.jjson`, `src.utils.csv`, `src.utils.printer` и `src.logger`. Импорты из `src` указывают на то, что эти модули находятся в структуре проекта `hypotez/src`. Связь - это структурированное иерархическое использование кода внутри проекта.

**Классы:**

* **`OpenAIModel`:** Этот класс представляет собой модель OpenAI. Атрибуты: `model`, `client`, `current_job_id`, `assistant_id`, `assistant`, `thread`, `system_instruction`, `dialogue_log_path`, `dialogue`, `assistants`, `models_list`. Методы предоставляют функции взаимодействия с API OpenAI и управлением моделью.

**Функции:**

* **`__init__`:** Инициализирует объект модели, устанавливает соединение с API, загружает помощника и диалоговый поток. Принимает необязательные аргументы `system_instruction` и `assistant_id`.
* **`list_models`:** Возвращает список доступных моделей OpenAI. Использует API OpenAI.
* **`list_assistants`:** Возвращает список доступных помощников, загруженных из файла `assistants.json` в папке `src/ai/openai/model`.
* **`set_assistant`:** Устанавливает помощника по его ID.
* **`_save_dialogue`:** Сохраняет диалог в файл.
* **`determine_sentiment`:** Определяет тональность текста (положительная, отрицательная или нейтральная) на основе ключевых слов.
* **`ask`:** Отправляет сообщение модели OpenAI и возвращает ответ, а также выполняет анализ тональности. Обрабатывает возможные ошибки и делает несколько попыток, если запрос не удается.
* **`describe_image`:** Описывает изображение. Принимает путь к изображению и необязательный `prompt`.
* **`describe_image_by_requests`:** Аналогичная функция, но использует библиотеку `requests` для взаимодействия с API OpenAI.
* **`dynamic_train`:** Динамически загружает предыдущий диалог и выполняет дообучение модели.
* **`train`:** Обучает модель на предоставленных данных.
* **`save_job_id`:** Сохраняет ID обучения и описание.


**Переменные:**

Переменные, такие как `MODE`, `positive_words`, `negative_words`, `neutral_words`, хранят константы или наборы данных, используемых другими функциями.

**Возможные ошибки и улучшения:**

* **Обработка ошибок:** Код содержит обработку исключений, но можно добавить более подробную диагностику ошибок.
* **Параллельность:** Для обработки нескольких запросов к API можно использовать асинхронные методы или потоки для повышения производительности.
* **Доступность моделей:** При загрузке моделей можно добавить проверку, чтобы удостовериться, что выбранная модель действительно существует.
* **Документация:** Документация должна быть более подробной для каждого метода.


**Цепочка взаимосвязей:**

Код взаимодействует с `gs` (вероятно, хранилищем конфигурации или файловой системой), файлами настроек и API OpenAI.  Другие модули проекта (`src.utils.jjson`, `src.utils.csv`) помогают в работе с JSON и CSV данными, а `src.logger` предоставляет логирование.  Взаимодействие с этими частями проекта реализовано через импорты и вызовы соответствующих функций/методов.