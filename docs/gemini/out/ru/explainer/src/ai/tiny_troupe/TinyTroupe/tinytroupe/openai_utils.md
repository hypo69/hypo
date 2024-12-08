# <input code>

```python
import os
import openai
from openai import OpenAI, AzureOpenAI
import time
import json
import pickle
import logging
import configparser
import tiktoken
from tinytroupe import utils

logger = logging.getLogger("tinytroupe")

# We'll use various configuration elements below
config = utils.read_config_file()

###########################################################################
# Default parameter values
###########################################################################
default = {}
default["model"] = config["OpenAI"].get("MODEL", "gpt-4")
default["max_tokens"] = int(config["OpenAI"].get("MAX_TOKENS", "1024"))
default["temperature"] = float(config["OpenAI"].get("TEMPERATURE", "0.3"))
default["top_p"] = int(config["OpenAI"].get("TOP_P", "0"))
default["frequency_penalty"] = float(config["OpenAI"].get("FREQ_PENALTY", "0.0"))
default["presence_penalty"] = float(
    config["OpenAI"].get("PRESENCE_PENALTY", "0.0"))
default["timeout"] = float(config["OpenAI"].get("TIMEOUT", "30.0"))
default["max_attempts"] = float(config["OpenAI"].get("MAX_ATTEMPTS", "0.0"))
default["waiting_time"] = float(config["OpenAI"].get("WAITING_TIME", "0.5"))
default["exponential_backoff_factor"] = float(config["OpenAI"].get("EXPONENTIAL_BACKOFF_FACTOR", "5"))

default["embedding_model"] = config["OpenAI"].get("EMBEDDING_MODEL", "text-embedding-3-small")

default["cache_api_calls"] = config["OpenAI"].getboolean("CACHE_API_CALLS", False)
default["cache_file_name"] = config["OpenAI"].get("CACHE_FILE_NAME", "openai_api_cache.pickle")

###########################################################################
# Model calling helpers
###########################################################################

# TODO under development
class LLMCall:
    """
    A class that represents an LLM model call. It contains the input messages, the model configuration, and the model output.
    """
    def __init__(self, system_template_name:str, user_template_name:str=None, **model_params):
        """
        Initializes an LLMCall instance with the specified system and user templates.
        """
        self.system_template_name = system_template_name
        self.user_template_name = user_template_name
        self.model_params = model_params
    
    def call(self, **rendering_configs):
        """
        Calls the LLM model with the specified rendering configurations.
        """
        self.messages = utils.compose_initial_LLM_messages_with_templates(self.system_template_name, self.user_template_name, rendering_configs)
        
        # call the LLM model
        self.model_output = client().send_message(self.messages, **self.model_params)
        if 'content' in self.model_output:
            return self.model_output['content']
        else:
            logger.error(f"Model output does not contain 'content' key: {self.model_output}")
            return None

    def __repr__(self):
        return f"LLMCall(messages={self.messages}, model_config={self.model_config}, model_output={self.model_output})"


###########################################################################
# Client class
###########################################################################
# ... (rest of the code)
```

# <algorithm>

**Блок-схема (фрагмент):**

```mermaid
graph TD
    A[Создается экземпляр OpenAIClient] --> B{Проверка флага cache_api_calls};
    B -- true --> C[Загрузка кэша из файла];
    B -- false --> D[Кэш не используется];
    C --> E[client._setup_from_config()];
    D --> E;
    E --> F[send_message(current_messages, ...)];
    F --> G{Проверка кэша};
    G -- true --> H[Возврат значения из кэша];
    G -- false --> I[Вызов API];
    I --> J[Сохранение ответа в кэш];
    H -- или -- I --> K[Обработка ответа];
    K --> L[Возврат результата];
```

**Описание:**

Функция `send_message` является ядром. Она обрабатывает вызовы к OpenAI API.  Если включена опция кэширования, она проверяет, есть ли запрос в кэше. Если есть, то возвращает сохранённый результат. Если нет, то запрашивает данные у OpenAI API, обрабатывает ответ, записывает его в кэш, и возвращает результат.  Функция использует экспоненциальную схему повторных попыток при ошибках (rate limit).

# <mermaid>

```mermaid
graph LR
    subgraph OpenAIClient
        A[OpenAIClient] --> B(send_message);
        B --> C{Проверка кэша};
        C -- true --> D[Возврат из кэша];
        C -- false --> E[Вызов OpenAI API];
        E --> F[Обработка ответа];
        F --> G[Сохранение в кэш];
        D -- или -- G --> H[Возврат результата];
    end
    subgraph utils
        I[utils.read_config_file()] --> J[config];
    end
    subgraph other
      K[os.getenv] --> A;
      L[configparser] --> J;
      M[time] --> B;
      N[pickle] --> A;
      O[logging] --> A;
      P[tiktoken] --> A;
    end
    B --> Q(LLMCall.call);
    Q --> R[utils.compose_initial_LLM_messages_with_templates];
    subgraph OpenAI
      R --> S[openai.ChatCompletion.create];
    end
    S --> F;
    H --> T[sanitize_dict];
    T --> U[Возврат];
```

**Описание диаграммы:**

Диаграмма показывает основные зависимости и потоки данных в коде.  `OpenAIClient` является центральным классом, взаимодействующим с OpenAI API.  `utils` предоставляет вспомогательные функции для работы с конфигурацией и сообщениями.  Другие модули (например, `os`, `configparser`, `time`, `pickle`, `logging`, `tiktoken`) обеспечивают базовые функциональности.

# <explanation>

**Импорты:**

- `os`, `openai`, `time`, `json`, `pickle`, `logging`, `configparser`, `tiktoken`: стандартные библиотеки Python для работы с операционной системой, API OpenAI, временем, вводом/выводом, сериализацией/десериализацией, логгированием, конфигурацией и обработкой токенов.
- `from tinytroupe import utils`: импортирует утилиты из пакета `tinytroupe`, предполагая, что `tinytroupe` содержит вспомогательные функции для работы с конфигурацией и другими полезными функциями.

**Классы:**

- `LLMCall`: представляет вызов модели LLM. Содержит системный шаблон, пользовательский шаблон, параметры модели, сообщения и результат вызова.  Служит для структурирования данных, передаваемых в API.
- `OpenAIClient`: класс для взаимодействия с OpenAI API. Хранит информацию о кэшировании, API ключ (полученный из переменной окружения `OPENAI_API_KEY`), и методы для работы с API.  Использует `OpenAI` и `AzureOpenAI` для вызовов.
- `AzureClient`: наследует от `OpenAIClient`, добавляя поддержку Azure OpenAI Service API.  Важен для переключения между разными API.
- `InvalidRequestError`, `NonTerminalError`: исключения, используемые для обработки ошибок в API вызовах.


**Функции:**

- `client()`: возвращает соответствующий клиент (OpenAI или Azure), выбирая его на основе настроек в файле конфигурации (`config.ini`).  Это важная функция для работы с API, так как она обеспечивает гибкость выбора.
- `register_client()`: регистрирует клиент для определенного типа API (например, `openai`, `azure`).
- `send_message()`: отправляет сообщение в OpenAI API и возвращает ответ.  Функция  использует `try-except` блоки для обработки различных типов ошибок (RateLimit, InvalidRequest) и управления повторными попытками. Поддержка экспоненциального отступа для управления повторными попытками при ошибках.
- `_raw_model_call()`, `_raw_model_response_extractor()`:  абстрактные методы для обработки вызовов API (OpenAI или Azure). Поддержка разных API.
- `_count_tokens()`: подсчет токенов в списках сообщений для моделирования OpenAI. Использует библиотеку `tiktoken`. Необходима для соблюдения лимитов токенов.

**Переменные:**

- `default`: словарь с параметрами по умолчанию для вызовов OpenAI API, которые могут быть переопределены.
- `config`: структура конфигурации, считываемая из файла `config.ini`.
- `api_type_to_client`: словарь, связывающий тип API с соответствующим клиентом.


**Возможные ошибки и улучшения:**

- Документация. Более подробная документация для классов, функций и параметров была бы полезна.
- Расширение поддержки. Поддержка дополнительных моделей OpenAI (например, gpt-3.5-turbo, gpt-4).
- Обработка исключений. Лучшая обработка исключений, потенциально добавление подробных сообщений об ошибках.
- Простота конфигурации. Возможность упростить методы настройки (force_api_type, force_api_cache).
- Проверка входных данных. Проверка корректности входных данных для предотвращения проблем.


**Цепочка взаимосвязей:**

Код тесно связан с файлом конфигурации (`config.ini`) через `utils.read_config_file()`.  Также с библиотеками OpenAI и Azure OpenAI Service. Функции взаимодействуют друг с другом, передавая данные через аргументы и возвращаемые значения.