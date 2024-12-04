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
        self.model_output = client().send_message(self.messages, **self.model_params)
        if 'content' in self.model_output:
            return self.model_output['content']
        else:
            logger.error(f"Model output does not contain 'content' key: {self.model_output}")
            return None

# ... (rest of the code)
```

# <algorithm>

**Шаг 1**: Импортирует необходимые библиотеки (`os`, `openai`, `time`, `json`, `pickle`, `logging`, `configparser`, `tiktoken`, `utils`).

**Шаг 2**: Создает логгер `logger` для отслеживания событий.

**Шаг 3**: Читает конфигурацию из файла `config.ini` с помощью `utils.read_config_file()`.

**Шаг 4**: Определяет значения по умолчанию для параметров API OpenAI (`default`). Эти параметры берутся из конфигурации или устанавливаются по умолчанию.

**Шаг 5**: Определяет класс `LLMCall` для работы с вызовами моделей LLM.

    *   `__init__`: Инициализирует объект `LLMCall` с именем шаблона для системы и пользователя, а также параметрами модели.
    *   `call`: Формирует сообщения для LLM на основе шаблонов и параметров рендеринга, вызывает метод `send_message` класса `client` для отправки запроса в API и обрабатывает ответ.
    
**Шаг 6**: Определяет класс `OpenAIClient` для взаимодействия с API OpenAI.

    *   `__init__`: Инициализирует объект с параметрами кеширования API.
    *   `set_api_cache`: Включает/выключает кеширование вызовов API.
    *   `_setup_from_config`: Настраивает параметры OpenAI API из переменных окружения.
    *   `send_message`: Отправляет сообщение в API OpenAI, обращается к кешу при необходимости, и обрабатывает возможные ошибки (invalid_request, rate_limit, NonTerminalError).
    *   `_raw_model_call`, `_raw_model_response_extractor`, `_count_tokens`, `_save_cache`, `_load_cache`: Вспомогательные методы для работы с API.
        
**Шаг 7**: Определяет класс `AzureClient`, наследуемый от `OpenAIClient`, для работы с Azure OpenAI Service. Различия заключаются в настройке `self.client` на основе `AzureOpenAI`.

**Шаг 8**: Функции `register_client`, `_get_client_for_api_type`, `client`: Регистрируют и возвращают клиент OpenAI или Azure, в зависимости от настроек.

**Шаг 9**: Функции `force_api_type`, `force_api_cache`, `force_default_value`: Позволяют переопределить параметры API и кеширования.


# <mermaid>

```mermaid
graph TD
    subgraph OpenAI API Interaction
        A[utils.read_config_file()] --> B(config);
        B --> C{Get Default Parameters};
        C --> D[OpenAIClient/__init__]
        D --> E[OpenAIClient/send_message];
        E --> F[OpenAI API Call];
        F --Success--> G[OpenAI Response];
        G --> H{Response Extraction};
        H --> I[Return Response];
        E --Error--> J[Error Handling];
        J --> K{Retry/Return None};
    end
    subgraph Azure API Interaction
        L[AzureClient/__init__] --> M[AzureClient/send_message];
        M --> N[Azure OpenAI API Call];
        N --Success--> O[Azure Response];
        O --> P[Response Extraction];
        P --> Q[Return Response];
        M --Error--> R[Error Handling];
        R --> S{Retry/Return None};
    end
    subgraph Helper Functions
        A --> T[register_client()];
        C --> T;
    end

    subgraph Config
        B --> U[config.ini];
    end

    
    
    
    C --Fail--> V[Error in get default params];
   
    
```


# <explanation>

**Импорты:**

- `os`: Для взаимодействия с операционной системой, например, получение ключей из переменных окружения.
- `openai`: Основная библиотека для работы с API OpenAI.
- `OpenAI`, `AzureOpenAI`: Классы для работы с API OpenAI и Azure OpenAI.
- `time`: Для управления временем, например, в циклах ожидания.
- `json`: Для работы с JSON-данными.
- `pickle`: Для сохранения и загрузки данных в бинарном формате (кеша API).
- `logging`: Для ведения журнала операций.
- `configparser`: Для работы с конфигурационными файлами.
- `tiktoken`: Для подсчёта токенов в сообщениях.
- `utils`: Модуль из пакета `tinytroupe`, вероятно, для работы с настройками, шаблонами сообщений и другими вспомогательными функциями.

**Классы:**

- `LLMCall`: Представляет вызов модели LLM, содержит входные сообщения, конфигурацию модели и выходные данные. Используется для абстрагирования вызовов API.
- `OpenAIClient`: Класс для взаимодействия с API OpenAI. Содержит логику отправки запросов, кеширования и обработки ошибок. Наследуется от `OpenAIClient`.
- `AzureClient`:  Аналогичный класс для работы с Azure OpenAI Service. Наследуется от `OpenAIClient`, имеет отличия в настройках.
- `InvalidRequestError`, `NonTerminalError`:  Исключения для обработки различных типов ошибок в работе с API.

**Функции:**

- `client()`: Возвращает экземпляр `OpenAIClient` или `AzureClient` в зависимости от настроек в конфигурационном файле.
- `register_client()`: Регистрирует `OpenAIClient` и `AzureClient` для последующего использования.
- `_get_client_for_api_type()`: Возвращает зарегистрированный клиент для заданного типа API.
- `force_api_type()`, `force_api_cache()`, `force_default_value()`: Позволяют переопределить параметры конфигурации для тестирования или особых случаев.

**Переменные:**

- `config`: Словарь с конфигурацией, полученный из `config.ini`.
- `default`: Словарь с параметрами по умолчанию для вызовов API.
- `cache_api_calls`: Флаг, определяющий, нужно ли кешировать вызовы API.
- `api_cache`: Словарь для кеширования вызовов API.
- `client`:  экземпляр класса, используемый для работы с API OpenAI или Azure.

**Возможные ошибки и улучшения:**

- **Обработка ошибок:** Код включает в себя обработку различных ошибок, таких как `InvalidRequestError`, `RateLimitError`, `NonTerminalError`.
- **Кеширование:**  Кеширование вызовов API позволяет ускорить работу, особенно при частых повторениях одних и тех же запросов.
- **Экспоненциальное замедление:** Введена функция `aux_exponential_backoff()` для автоматического увеличения задержки при повторяющихся ошибках `RateLimitError`.  Это помогает предотвратить дальнейшее ограничение от API.
- **Заглушка для `_count_tokens`:** Необходимо реализовать логику подсчёта токенов для некоторых моделей, которые не могут использоваться без корректной реализации подсчета токенов.
- **Доступность:**  Код нуждается в более подробных документах по способам настройки конфигурации.


**Цепочка взаимосвязей:**

Функции и классы в `openai_utils.py` напрямую взаимодействуют с `utils.py` для работы с конфигурацией и шаблонами сообщений.  Они также используют  библиотеку `openai`. Конфигурация (`config.ini`) управляет поведением вызовов API.  Использование `loggin`  обеспечивает возможность отслеживания работы с API и отладку.