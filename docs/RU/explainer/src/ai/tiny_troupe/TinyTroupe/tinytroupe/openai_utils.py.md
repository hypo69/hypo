## АНАЛИЗ КОДА: `tinytroupe/openai_utils.py`

### 1. <алгоритм>

**Блок-схема:**

```mermaid
graph LR
    Start[Начало] --> LoadConfig[Загрузка конфигурации из config.ini];
    LoadConfig --> SetDefaults[Установка значений по умолчанию];
    SetDefaults --> DefineLLMCallClass[Определение класса LLMCall];
    DefineLLMCallClass --> DefineOpenAIClient[Определение класса OpenAIClient];
    DefineOpenAIClient --> DefineAzureClient[Определение класса AzureClient];
     DefineAzureClient --> RegisterClients[Регистрация клиентов OpenAI и Azure];
     RegisterClients --> DefineClientAccessFunc[Определение функций доступа к клиентам];
   
    DefineClientAccessFunc --> LLMCallInit[Инициализация LLMCall: system_template_name, user_template_name, model_params];
    LLMCallInit --> ComposeMessages[Составление сообщений с шаблонами];
    ComposeMessages --> CallClientSendMessage[Вызов client.send_message()];
    CallClientSendMessage --> ProcessResponse[Обработка ответа];
    ProcessResponse --> ReturnContent[Возврат содержимого или None];
   
    
    DefineOpenAIClient --> OpenAIClientInit[Инициализация OpenAIClient: cache_api_calls, cache_file_name];
    OpenAIClientInit --> SetCache[Установка кэша API];
    SetCache --> SetupConfig[Настройка API];
    SetupConfig --> SendMessage[Отправка сообщения в OpenAI API];
    SendMessage --> ExponentialBackoff[Реализация экспоненциальной задержки];
    ExponentialBackoff --> RawModelCall[Вызов _raw_model_call() (API)];
        RawModelCall --> CacheLookup[Проверка кэша]
        CacheLookup -- Кэш не найден --> RawModelCallAPI[Вызов OpenAI API];
         CacheLookup -- Кэш найден --> ExtractFromCache[Извлечь ответ из кэша]
          RawModelCallAPI --> SaveCache[Сохранение ответа в кэш]
          SaveCache --> ExtractRawResponse[Извлечение ответа из сырого ответа];
           ExtractFromCache -->ExtractRawResponse
           ExtractRawResponse --> Sanitize[Санитация ответа];
            Sanitize --> ReturnResponse[Возврат ответа];
    SendMessage -- Ошибка --> ErrorHandling[Обработка ошибок];
     ErrorHandling -- Invalid request, BadRequest, etc --> ReturnNoneError[Вернуть None];
     ErrorHandling -- Rate limit, NonTerminal, Exception --> ExponentialBackoff
     ReturnNoneError --> End[Конец];
    ReturnResponse --> End
    DefineAzureClient --> AzureClientInit[Инициализация AzureClient: cache_api_calls, cache_file_name];
    AzureClientInit --> SetCacheAzure[Установка кэша API];
    SetCacheAzure --> SetupConfigAzure[Настройка API Azure];
    SetupConfigAzure --> RawModelCallAzure[Вызов _raw_model_call() Azure API];
    RawModelCallAzure --> ExtractRawResponseAzure[Извлечение ответа из сырого ответа];
     ExtractRawResponseAzure --> SanitizeAzure[Санитация ответа];
      SanitizeAzure --> ReturnResponseAzure[Возврат ответа];

     
      
     OpenAIClientInit --> Embedding[Получение эмбеддинга];
      Embedding --> RawModelCallEmbedding[Вызов API для получения эмбеддинга];
      RawModelCallEmbedding --> ExtractRawResponseEmbedding[Извлечение эмбеддинга из ответа];
      ExtractRawResponseEmbedding --> ReturnEmbedding[Возврат эмбеддинга];

     
     

    RegisterClients --> GetClient[Получение клиента по типу API];
    GetClient --> Client[Возвращение клиента];
    GetClient --> ForceApiType[Принудительная установка типа API];
    GetClient --> ForceApiCache[Принудительная установка параметров кэширования];
    GetClient --> ForceDefaultValue[Принудительная установка значений по умолчанию];
     
```
**Примеры:**

*   **Загрузка конфигурации:** `config = utils.read_config_file()` - Загрузка параметров из `config.ini`, например, `MODEL = gpt-4`.
*   **Установка значений по умолчанию:** `default["model"] = config["OpenAI"].get("MODEL", "gpt-4")` -  Если в конфиге нет `MODEL`, то используется `gpt-4`.
*   **Инициализация `LLMCall`:** `llm_call = LLMCall(system_template_name="system_prompt", user_template_name="user_prompt", model="gpt-4", temperature=0.7)`
*   **Составление сообщений:** `utils.compose_initial_LLM_messages_with_templates(...)` -  Формирование списка сообщений на основе шаблонов и контекста.
*   **Вызов `client.send_message()`:** `client().send_message(messages, model="gpt-4")` -  Отправка сообщений в OpenAI API.
*   **Обработка ответа:** Извлечение контента из JSON ответа `model_output['content']`.
*   **Инициализация `OpenAIClient`:** `openai_client = OpenAIClient(cache_api_calls=True, cache_file_name="my_cache.pickle")`.
*   **Вызов кэша API:** Проверка наличия ключа в `self.api_cache`, если `cache_api_calls=True`.
*   **Вызов _raw_model_call()**: `self.client.chat.completions.create(...)`.
*   **Извлечение ответа из raw response**: `response.choices[0].message.to_dict()`.
*   **Регистрация клиентов**: `register_client("openai", OpenAIClient())` регистрирует класс `OpenAIClient` под ключом `"openai"`.
*   **Получение клиента:** `client()` возвращает экземпляр `OpenAIClient` или `AzureClient`, в зависимости от `config.ini`.

### 2. <mermaid>

```mermaid
flowchart TD
    subgraph Configuration
        LoadConfig(Load Configuration from config.ini) --> SetDefaults(Set Default Parameters)
    end
    
    subgraph LLMCall
        LLMCallClass(Class LLMCall)
        LLMCallInit(Initialize LLMCall) --> ComposeMessages(Compose Messages with Templates)
        ComposeMessages --> CallClientSendMessage(Call client.send_message())
        CallClientSendMessage --> ProcessResponse(Process Response)
        ProcessResponse --> ReturnContent(Return Content or None)
        LLMCallClass --> LLMCallInit
    end
    
    subgraph OpenAI Client
        OpenAIClientClass(Class OpenAIClient)
        OpenAIClientInit(Initialize OpenAIClient) --> SetCache(Set API Cache)
        SetCache --> SetupConfig(Setup OpenAI API)
        SetupConfig --> SendMessage(Send Message to OpenAI API)
        SendMessage --> ExponentialBackoff(Exponential Backoff)
         ExponentialBackoff --> RawModelCall(Call _raw_model_call() API)
          RawModelCall --> CacheLookup(Lookup in Cache)
           CacheLookup -- Cache Not Found --> RawModelCallAPI(Call OpenAI API)
            CacheLookup -- Cache Found --> ExtractFromCache(Extract response from cache)
             RawModelCallAPI --> SaveCache(Save response to cache)
              SaveCache --> ExtractRawResponse(Extract response)
              ExtractFromCache --> ExtractRawResponse
              ExtractRawResponse --> Sanitize(Sanitize Response)
               Sanitize --> ReturnResponse(Return Response)
        SendMessage -- Error --> ErrorHandling(Handle Errors)
          ErrorHandling -- InvalidRequest, BadRequest --> ReturnNoneError(Return None)
         ErrorHandling -- RateLimit, NonTerminal, Exception  --> ExponentialBackoff
         ReturnNoneError --> End(End)
        ReturnResponse --> End

         OpenAIClientInit --> Embedding(Get Embedding)
        Embedding --> RawModelCallEmbedding(Call Embedding API)
        RawModelCallEmbedding --> ExtractRawResponseEmbedding(Extract Embedding)
        ExtractRawResponseEmbedding --> ReturnEmbedding(Return Embedding)

        OpenAIClientClass --> OpenAIClientInit
    end

     subgraph Azure Client
       AzureClientClass(Class AzureClient)
      AzureClientInit(Initialize AzureClient) --> SetCacheAzure(Set API Cache)
       SetCacheAzure --> SetupConfigAzure(Setup Azure API)
       SetupConfigAzure --> RawModelCallAzure(Call _raw_model_call() Azure API)
         RawModelCallAzure --> ExtractRawResponseAzure(Extract Raw Response)
            ExtractRawResponseAzure --> SanitizeAzure(Sanitize Response)
                 SanitizeAzure --> ReturnResponseAzure(Return Response)
          AzureClientClass --> AzureClientInit
    end
    
      
    subgraph Clients Registry
        RegisterClientFunc(Register Client)
        GetClientFunc(Get Client by API Type)
        ClientFunc(Get Client)
        ForceApiTypeFunc(Force API Type)
        ForceApiCacheFunc(Force API Cache)
        ForceDefaultValueFunc(Force Default Value)
        RegisterClientFunc --> GetClientFunc
         GetClientFunc --> ClientFunc
         GetClientFunc --> ForceApiTypeFunc
         GetClientFunc --> ForceApiCacheFunc
          GetClientFunc --> ForceDefaultValueFunc
    end

    SetDefaults --> LLMCallClass
    SetDefaults --> OpenAIClientClass
      SetDefaults --> AzureClientClass
    OpenAIClientClass --> ClientsRegistry
       AzureClientClass --> ClientsRegistry
     LLMCallClass --> ClientsRegistry
   
```

**Импорты для `mermaid` диаграммы:**

*   **`graph TD`:** Определяет тип диаграммы как направленный граф (top-down).
*   **`subgraph ... end`:** Группирует узлы в логические блоки, отображаемые в виде подграфов.
*   **`-->`:** Указывает направление потока выполнения или зависимость между узлами.
*   **`(...)`:**  Отображает текст внутри узла.
*   `-- текст --`:  Добавляет текст к стрелке для описания перехода или действия.

### 3. <объяснение>

**Импорты:**

*   **`os`**:  Предоставляет функции для взаимодействия с операционной системой, например, для получения переменных окружения (API key).
*   **`openai`**, **`OpenAI`**, **`AzureOpenAI`**:  Библиотека OpenAI для взаимодействия с OpenAI API, а также классы для работы с OpenAI и Azure OpenAI.
*   **`time`**:  Используется для задержек при экспоненциальном backoff.
*   **`json`**: Используется для работы с JSON-данными (хотя напрямую не используется, возможно, в будущем пригодится).
*   **`pickle`**:  Используется для сериализации и десериализации объектов Python, в данном случае для кэширования вызовов API.
*   **`logging`**:  Используется для логирования событий (ошибок, предупреждений, отладочной информации).
*   **`configparser`**: Используется для разбора конфигурационных файлов формата `ini` (хотя напрямую не используется, но `utils.read_config_file` внутри использует его).
*   **`tiktoken`**:  Используется для подсчета количества токенов в тексте, необходимых для API OpenAI.
*   **`tinytroupe.utils`**:  Локальный модуль, содержащий вспомогательные функции, такие как `read_config_file`, `compose_initial_LLM_messages_with_templates` и `sanitize_dict`.

**Классы:**

*   **`LLMCall`**:
    *   **Роль:**  Представляет собой вызов языковой модели.
    *   **Атрибуты:**
        *   `system_template_name` (str): Имя шаблона для системного сообщения.
        *   `user_template_name` (str): Имя шаблона для пользовательского сообщения.
        *   `model_params` (dict): Параметры для вызова модели (например, `temperature`).
        *   `messages` (list):  Список сообщений, отправленных в модель.
        *   `model_output` (dict): Ответ модели.
    *   **Методы:**
        *   `__init__(self, system_template_name, user_template_name, **model_params)`: Инициализирует объект `LLMCall` с заданными параметрами.
        *   `call(self, **rendering_configs)`: Выполняет вызов модели с заданными параметрами рендеринга.
        *    `__repr__(self)`: Возвращает строковое представление объекта.
    *   **Взаимодействие:**
         Использует `utils.compose_initial_LLM_messages_with_templates` для создания сообщений и `client().send_message` для отправки сообщений в модель.
*   **`OpenAIClient`**:
    *   **Роль:** Утилита для взаимодействия с OpenAI API.
    *   **Атрибуты:**
        *   `cache_api_calls` (bool): Флаг, определяющий, нужно ли кэшировать вызовы API.
        *   `cache_file_name` (str): Имя файла для кэширования.
        *   `api_cache` (dict): Словарь для хранения кэшированных ответов API.
        *   `client` (OpenAI):  Клиентский объект для работы с OpenAI API.
    *   **Методы:**
        *   `__init__(self, cache_api_calls, cache_file_name)`: Инициализирует клиент.
        *    `set_api_cache(self, cache_api_calls, cache_file_name)`: Устанавливает флаг кэширования и имя файла для кэша.
        *   `_setup_from_config(self)`: Настраивает клиент OpenAI API (устанавливает api_key из переменных окружения).
        *   `send_message(self, current_messages, ...)`: Отправляет сообщение в OpenAI API.
        *    `_raw_model_call(self, model, chat_api_params)`: Выполняет сырой вызов OpenAI API.
        *    `_raw_model_response_extractor(self, response)`: Извлекает ответ из сырого ответа API.
        *   `_count_tokens(self, messages, model)`: Подсчитывает количество токенов в сообщениях.
        *   `_save_cache(self)`: Сохраняет кэш API на диск.
        *   `_load_cache(self)`: Загружает кэш API с диска.
        *    `get_embedding(self, text, model)`: Получает эмбеддинг для заданного текста.
        *    `_raw_embedding_model_call(self, text, model)`: Выполняет сырой вызов API для получения эмбеддингов.
        *    `_raw_embedding_model_response_extractor(self, response)`: Извлекает эмбеддинг из сырого ответа API.
    *   **Взаимодействие:** Взаимодействует напрямую с OpenAI API, кэширует ответы и использует `tiktoken` для подсчета токенов.
*   **`AzureClient`**:
    *   **Роль:** Утилита для взаимодействия с Azure OpenAI API.
    *   **Атрибуты:** Наследует от `OpenAIClient`.
    *   **Методы:**
        *   `__init__(self, cache_api_calls, cache_file_name)`: Инициализирует клиент, вызывая конструктор родительского класса `OpenAIClient`.
        *   `_setup_from_config(self)`: Настраивает клиент Azure OpenAI API (устанавливает `azure_endpoint`, `api_version` и `api_key` из переменных окружения).
        *   `_raw_model_call(self, model, chat_api_params)`: Выполняет сырой вызов Azure OpenAI API.
    *   **Взаимодействие:** Взаимодействует с Azure OpenAI API.
*    **`InvalidRequestError`**: Пользовательское исключение, если запрос к OpenAI API не валиден.
*    **`NonTerminalError`**: Пользовательское исключение, если произошла не фатальная ошибка и можно повторить запрос.

**Функции:**

*   **`register_client(api_type, client)`**:
    *   **Аргументы:**
        *   `api_type` (str): Тип API.
        *   `client`: Клиентский объект (например, `OpenAIClient` или `AzureClient`).
    *   **Назначение:** Регистрирует клиент для определенного типа API.
    *    **Пример:** `register_client("openai", OpenAIClient())`
*   **`_get_client_for_api_type(api_type)`**:
    *   **Аргументы:**
        *   `api_type` (str): Тип API.
    *   **Назначение:** Возвращает клиентский объект, зарегистрированный для заданного типа API.
    *   **Возвращаемое значение:** Клиентский объект или исключение `ValueError`, если тип API не найден.
*   **`client()`**:
    *   **Назначение:** Возвращает клиентский объект на основе текущей конфигурации (из `config.ini`).
    *   **Возвращаемое значение:** Клиентский объект (например, `OpenAIClient` или `AzureClient`).
*   **`force_api_type(api_type)`**:
    *   **Аргументы:**
        *   `api_type` (str): Тип API.
    *   **Назначение:** Принудительно устанавливает тип API для использования, переопределяя конфигурацию.
*  **`force_api_cache(cache_api_calls, cache_file_name)`**:
     * **Аргументы:**
          * `cache_api_calls` (bool): Включить или выключить кэширование
           * `cache_file_name` (str): Имя файла для кэширования
    * **Назначение:** Принудительно устанавливает настройки кэша, переопределяя значения в файле конфигурации
*   **`force_default_value(key, value)`**:
    *   **Аргументы:**
        *   `key` (str): Ключ параметра конфигурации.
        *   `value`: Новое значение параметра.
    *   **Назначение:** Принудительно устанавливает значение по умолчанию для заданного ключа.

**Переменные:**

*   **`default`** (dict): Словарь, содержащий значения параметров по умолчанию (например, `model`, `temperature`, `max_tokens`).
*   **`config`** (dict): Словарь, содержащий параметры конфигурации, загруженные из файла `config.ini` через `utils.read_config_file()`.
*   **`logger`**: Объект логгера, используемый для записи сообщений отладки и ошибок.
*   `_api_type_to_client` (dict): Словарь для хранения зарегистрированных клиентских объектов.
* `_api_type_override` (str):  Переменная для принудительного переопределения типа API.

**Потенциальные ошибки или области для улучшения:**

*   **Обработка ошибок:**  В функции `send_message` обрабатываются `InvalidRequestError`, `RateLimitError` и другие общие исключения. Можно добавить более специфичную обработку ошибок для более точного логирования и обработки.
*   **Синхронизация кэша:** Если приложение работает в многопоточной среде, то необходимо обеспечить потокобезопасность при доступе к `api_cache` и при сохранении/загрузке кэша.
*   **Гибкость конфигурации:** Управление конфигурацией может быть более гибким, например, с помощью отдельных классов конфигурации или инструментов командной строки.
*   **Управление зависимостями**:  Необходимо более тщательно управлять зависимостями, чтобы избежать проблем с версиями библиотек.
*   **Удаление кода, не используемого напрямую**: Модуль `json` импортируется, но не используется. Его можно удалить.

**Цепочка взаимосвязей с другими частями проекта:**

1.  **`utils.py`**: Этот модуль зависит от `tinytroupe.utils` для чтения конфигурации, создания сообщений и очистки ответов.
2.  **`config.ini`**:  Файл конфигурации содержит параметры API, используемые в `openai_utils.py`.
3.  **Шаблоны**:  Используются для форматирования сообщений для LLM (шаблоны хранятся в `templates/` и используются через `utils.compose_initial_LLM_messages_with_templates`).
4.  **Другие модули**:  Другие части проекта, использующие LLM, импортируют и используют классы и функции из этого файла (`openai_utils.py`).

В заключение, код предоставляет гибкий и расширяемый способ взаимодействия с OpenAI API, включая поддержку кэширования, retry-механизмов и различных типов API, таких как OpenAI и Azure OpenAI.