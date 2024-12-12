## <алгоритм>

1.  **Инициализация**:
    *   Импортируются необходимые модули, включая `os`, `openai`, `time`, `json`, `pickle`, `logging`, `configparser`, `tiktoken`, и `tinytroupe.utils`.
    *   Настраивается логгер.
    *   Читается конфигурационный файл с помощью `utils.read_config_file()`.
    *   Инициализируются значения параметров по умолчанию из конфигурационного файла, такие как `model`, `max_tokens`, `temperature` и другие параметры для OpenAI API, а также параметры для кеширования.
    
2.  **LLMCall Class**:
    *   При инициализации `LLMCall` сохраняется имя системного шаблона и имя пользовательского шаблона (если есть), а также параметры модели.
        *   Пример: `llm_call = LLMCall(system_template_name="system_template_1", user_template_name="user_template_1", temperature=0.5)`
    *   Метод `call` формирует сообщения для LLM, используя `utils.compose_initial_LLM_messages_with_templates()` с переданными шаблонами и конфигурациями.
        *   Пример: `messages = utils.compose_initial_LLM_messages_with_templates(system_template_name="system_template_1", user_template_name="user_template_1", rendering_configs={"input_text":"Hello"})`
    *   Вызывает LLM модель через `client().send_message()`, передавая сообщения и параметры модели, получая в ответ вывод модели.
        *   Пример: `model_output = client().send_message(messages, model="gpt-4", temperature=0.5)`
    *   Возвращает текстовое содержимое из ответа модели.
        *   Пример: `response = llm_call.call(rendering_configs={"input_text":"Hello"})`

3.  **OpenAIClient Class**:
    *   При инициализации `OpenAIClient` настраивается кэш API вызовов на основе переданных параметров `cache_api_calls` и `cache_file_name`.
    *   Метод `set_api_cache` устанавливает параметры кэширования и загружает кэш, если он включен.
    *   Метод `_setup_from_config` настраивает клиент OpenAI API, используя ключ API из переменной окружения `OPENAI_API_KEY`.
    *   Метод `send_message`:
        *   Принимает список сообщений `current_messages`, а также параметры для вызова модели (модель, температура, максимальное количество токенов и т.д.).
        *   Подготавливает параметры для API-вызова.
        *   Пытается получить ответ из кэша, если включен, иначе вызывает метод `_raw_model_call`.
        *   Обрабатывает возможные ошибки, такие как `InvalidRequestError`, `RateLimitError` и другие, с реализацией экспоненциального отката при ошибках типа `RateLimitError` и `NonTerminalError`.
        *   Возвращает ответ от модели.
    *   Метод `_raw_model_call` вызывает OpenAI API, используя `client.chat.completions.create()`.
        *   Пример: `response = self.client.chat.completions.create(messages=current_messages, model=model, temperature=temperature)`
    *   Метод `_raw_model_response_extractor` извлекает содержимое ответа из API.
        *   Пример: `content = self._raw_model_response_extractor(response)`
    *   Метод `_count_tokens` подсчитывает количество токенов в сообщении, используя `tiktoken`, чтобы оценить стоимость запроса к API.
    *   Методы `_save_cache` и `_load_cache` сохраняют и загружают кэш API вызовов соответственно, используя pickle.
    *  Метод `get_embedding` получает эмбеддинг текста.
        *  Пример: `embedding = client.get_embedding("example text", model="text-embedding-3-small")`
    *  Метод `_raw_embedding_model_call` вызывает API для получения эмбеддинга.
        *  Пример: `response = self.client.embeddings.create(input=["example text"], model=model)`
    *   Метод `_raw_embedding_model_response_extractor` извлекает эмбеддинг из ответа.
    
4.  **AzureClient Class**:
    *   `AzureClient` наследует от `OpenAIClient` и переопределяет методы `_setup_from_config` и `_raw_model_call` для работы с Azure OpenAI Service.
    *   Метод `_setup_from_config` настраивает клиент Azure OpenAI API, используя endpoint, версию API и ключ API из переменных окружения `AZURE_OPENAI_ENDPOINT`, `AZURE_API_VERSION` и `AZURE_OPENAI_KEY`, соответственно.
    *    Метод `_raw_model_call` вызывает Azure OpenAI Service API, используя `client.chat.completions.create()`.
        *   Пример: `response = self.client.chat.completions.create(messages=current_messages, model=model, temperature=temperature)`

5.  **Регистрация и получение клиентов**:
    *   `_api_type_to_client` - это словарь для хранения экземпляров клиентов, связанных с типами API.
    *   `register_client` регистрирует клиентский класс для конкретного типа API, например, "openai" или "azure".
    *   `_get_client_for_api_type` возвращает клиентский класс для определенного типа API.
    *   `client` возвращает экземпляр клиентского класса на основе текущей конфигурации `API_TYPE` или переопределения.
    *   `force_api_type` позволяет принудительно установить тип API.
    *   `force_api_cache` позволяет принудительно установить параметры кэширования API.
    *   `force_default_value` позволяет принудительно установить значения по умолчанию для конфигурации.

6. **Обработка ошибок**:

*   Определены два кастомных исключения:
    *   `InvalidRequestError` вызывается, когда запрос к OpenAI API невалиден и нет смысла повторять запрос.
    *   `NonTerminalError` вызывается при некритических ошибках, когда есть смысл повторить запрос (с экспоненциальным откатом).

## <mermaid>

```mermaid
graph LR
    A[Начало] --> B(Инициализация);
    B --> C{LLMCall Instance};
    C -->|Создание LLMCall| D(LLMCall.__init__);
    D --> E{LLMCall.call()};
    E --> F(utils.compose_initial_LLM_messages_with_templates);
    F --> G(client().send_message);
    G --> H{OpenAIClient Instance};
    H --> I(OpenAIClient.__init__);
    I --> J(OpenAIClient.set_api_cache);
    J --> K(OpenAIClient._setup_from_config);
    K --> L(OpenAIClient.send_message);
    L --> M{Cache Hit?};
    M -- Yes --> N(Retrieve Cached Response);
    N --> O(OpenAIClient._raw_model_response_extractor);
    M -- No --> P(OpenAIClient._raw_model_call);
    P --> Q(openai.chat.completions.create);
    Q --> R(OpenAIClient._raw_model_response_extractor);
     R --> S{Cache Enabled?};
     S -- Yes --> T(Save to Cache);
     T --> O;
     S -- No --> O;
    O --> U(Return Content);
    U --> V[Конец];
     style B fill:#f9f,stroke:#333,stroke-width:2px
     style C fill:#ccf,stroke:#333,stroke-width:2px
    style H fill:#ccf,stroke:#333,stroke-width:2px

    subgraph LLMCall
        D
        E
        F
    end
    
    subgraph OpenAIClient
        I
        J
        K
        L
        M
        N
        P
        Q
        R
        S
        T
    end
    
        subgraph utils
        F
        end
```

**Анализ зависимостей `mermaid`:**

1.  **Начало (`A`)**: Начальная точка выполнения программы.
2.  **Инициализация (`B`)**: Этап, на котором происходит чтение конфигурации, инициализация логгера и установка значений по умолчанию. Зависит от `utils.read_config_file()`.
3.  **LLMCall Instance (`C`)**: Представляет процесс создания и использования экземпляра класса `LLMCall`, который инкапсулирует вызов языковой модели.
4.  **LLMCall.\_\_init\_\_ (`D`)**: Метод инициализации класса `LLMCall`, где сохраняются шаблоны и параметры модели.
5.  **LLMCall.call() (`E`)**: Метод, который вызывает языковую модель, передавая подготовленные сообщения.
6.   **utils.compose\_initial\_LLM\_messages\_with\_templates (`F`)**: Функция, отвечающая за формирование сообщений для модели на основе шаблонов. Эта функция находится в модуле `tinytroupe.utils`.
7.  **client().send\_message (`G`)**: Метод для отправки сообщений к модели, который обращается к классу клиента (например, `OpenAIClient`).
8.  **OpenAIClient Instance (`H`)**: Представляет процесс создания и использования экземпляра класса `OpenAIClient`.
9.  **OpenAIClient.\_\_init\_\_ (`I`)**: Метод инициализации класса `OpenAIClient`.
10. **OpenAIClient.set\_api\_cache (`J`)**: Метод для установки параметров кеширования API.
11. **OpenAIClient.\_setup\_from\_config (`K`)**: Метод для настройки API клиента OpenAI.
12. **OpenAIClient.send\_message (`L`)**: Метод, который отправляет сообщение к API OpenAI и получает ответ.
13. **Cache Hit? (`M`)**: Условный блок, проверяющий, есть ли в кэше ответ на данный запрос.
14. **Retrieve Cached Response (`N`)**: Блок, возвращающий закэшированный ответ, если он найден.
15. **OpenAIClient.\_raw\_model\_response\_extractor (`O`)**: Метод для извлечения содержимого ответа от API.
16. **OpenAIClient.\_raw\_model\_call (`P`)**: Метод, непосредственно вызывающий API OpenAI для получения ответа.
17. **openai.chat.completions.create (`Q`)**: Вызов функции API OpenAI для создания ответа модели.
18. **OpenAIClient.\_raw\_model\_response\_extractor (`R`)**: Метод для извлечения содержимого ответа от API после прямого запроса.
19. **Cache Enabled? (`S`)**: Условный блок, проверяющий, включен ли кэш.
20. **Save to Cache (`T`)**: Блок, сохраняющий ответ API в кэш.
21. **Return Content (`U`)**: Возвращение контента, сгенерированного моделью, пользователю.
22. **Конец (`V`)**: Конечная точка выполнения программы.

Диаграмма `mermaid` наглядно демонстрирует поток вызовов и данных между различными функциями и классами, подчеркивая ключевые этапы взаимодействия с OpenAI API, включая кэширование и обработку ошибок.

## <объяснение>

### Импорты

*   `os`: Предоставляет функции для взаимодействия с операционной системой, используется для получения переменных окружения, например `OPENAI_API_KEY`.
*   `openai`: Основная библиотека для взаимодействия с API OpenAI. Содержит классы `OpenAI` и `AzureOpenAI`, которые используются для создания экземпляров клиентов для OpenAI и Azure соответственно.
*   `time`: Используется для добавления пауз между запросами к API, чтобы избежать ограничений скорости.
*   `json`: Используется для работы с данными в формате JSON, хотя явно не используется в коде, но может быть полезен для сериализации/десериализации.
*   `pickle`: Используется для сериализации и десериализации объектов Python, включая кэш API, в бинарный формат.
*   `logging`: Используется для логирования событий, ошибок и предупреждений.
*   `configparser`: Используется для чтения конфигурационных файлов (например, `config.ini`).
*   `tiktoken`: Используется для подсчета токенов в текстовых сообщениях перед их отправкой в API OpenAI.
*   `tinytroupe.utils`:  Импортируется модуль `utils` из пакета `tinytroupe`, который содержит утилиты, например `read_config_file()`, `compose_initial_LLM_messages_with_templates` и `sanitize_dict`.

### Классы

*   **`LLMCall`**:
    *   **Роль**: Инкапсулирует вызов языковой модели, объединяя шаблоны сообщений, параметры модели и результат вызова.
    *   **Атрибуты**:
        *   `system_template_name` (str): Имя системного шаблона.
        *   `user_template_name` (str): Имя пользовательского шаблона (опционально).
        *   `model_params` (dict): Параметры для вызова модели.
    *   **Методы**:
        *   `__init__`: Конструктор класса.
        *   `call`: Выполняет вызов модели, возвращает результат. Использует `utils.compose_initial_LLM_messages_with_templates` для подготовки сообщений.
        *   `__repr__`: Возвращает строковое представление объекта.
    *   **Взаимодействие**: Создается для каждого конкретного вызова LLM, взаимодействует с классом `OpenAIClient` для выполнения запросов к API.
*   **`OpenAIClient`**:
    *   **Роль**: Клиент для взаимодействия с OpenAI API.
    *   **Атрибуты**:
        *   `cache_api_calls` (bool): Флаг для включения/выключения кеширования API.
        *   `cache_file_name` (str): Имя файла для кеширования.
        *    `api_cache` (dict): словарь для кеширования.
        *   `client` (openai.OpenAI): Экземпляр класса `openai.OpenAI` для выполнения API-запросов.
    *   **Методы**:
        *   `__init__`: Конструктор класса, устанавливает параметры кэширования.
        *   `set_api_cache`: Устанавливает параметры кэширования API-вызовов.
        *   `_setup_from_config`: Настраивает API-клиент OpenAI, используя ключ из переменной окружения.
        *    `send_message`: Отправляет сообщение к API OpenAI, обрабатывает ошибки и кэширует результаты.
        *    `_raw_model_call`: Выполняет запрос к OpenAI API (метод `chat.completions.create`).
        *    `_raw_model_response_extractor`: Извлекает текстовый контент из ответа API.
        *    `_count_tokens`: Подсчитывает количество токенов в списке сообщений.
        *   `_save_cache`: Сохраняет кэш API-вызовов на диск с использованием pickle.
        *   `_load_cache`: Загружает кэш API-вызовов с диска с использованием pickle.
        *    `get_embedding`: Получает эмбеддинг текста через API.
        *    `_raw_embedding_model_call`: Выполняет запрос к OpenAI API для получения эмбеддинга.
        *    `_raw_embedding_model_response_extractor`: Извлекает эмбеддинг из ответа API.
    *   **Взаимодействие**: Используется для отправки сообщений и получения ответов от OpenAI API, взаимодействует с файловой системой для кэширования.
*    **`AzureClient`**:
    *   **Роль**:  Клиент для взаимодействия с Azure OpenAI Service API, наследуется от `OpenAIClient`.
    *   **Атрибуты**:  Наследует атрибуты от `OpenAIClient`.
    *   **Методы**:
        *   `__init__`: Конструктор класса, вызывает конструктор родительского класса.
        *   `_setup_from_config`: Настраивает Azure API-клиент, используя endpoint, версию API и ключ API из переменных окружения.
        *    `_raw_model_call`: Выполняет запрос к Azure API (метод `chat.completions.create`).
    *   **Взаимодействие**: Используется для отправки сообщений и получения ответов от Azure OpenAI Service API.
*   **`InvalidRequestError`**: Пользовательское исключение для случаев, когда запрос к API является невалидным.
*    **`NonTerminalError`**: Пользовательское исключение для случаев, когда API возвращает ошибку, но запрос может быть повторен.

### Функции

*   **`register_client(api_type, client)`**:
    *   **Аргументы**:
        *   `api_type` (str): Тип API ("openai", "azure", или любой пользовательский тип).
        *   `client`: Экземпляр клиентского класса.
    *   **Назначение**: Регистрирует клиентский класс для данного типа API в словаре `_api_type_to_client`.
    *    **Пример**: `register_client("openai", OpenAIClient())`
*    **`_get_client_for_api_type(api_type)`**:
    *    **Аргументы**:
        *    `api_type` (str): Тип API.
    *    **Назначение**: Возвращает клиентский класс для данного типа API из словаря `_api_type_to_client`.
    *    **Возвращаемое значение**: Клиентский класс.
*    **`client()`**:
    *   **Назначение**: Возвращает экземпляр клиентского класса, используя текущий `API_TYPE` из конфигурации или переопределение.
    *   **Возвращаемое значение**: Экземпляр клиентского класса.
*   **`force_api_type(api_type)`**:
    *   **Аргументы**:
        *   `api_type` (str): Тип API.
    *   **Назначение**: Принудительно устанавливает тип API, переопределяя настройку в конфигурационном файле.
*   **`force_api_cache(cache_api_calls, cache_file_name=default["cache_file_name"])`**:
    *   **Аргументы**:
        *   `cache_api_calls` (bool): Включить или выключить кеширование.
        *   `cache_file_name` (str): Имя файла для кэша.
    *   **Назначение**: Принудительно устанавливает параметры кэширования, переопределяя настройки конфигурационного файла.
*   **`force_default_value(key, value)`**:
    *   **Аргументы**:
        *   `key` (str): Ключ для переопределения значения по умолчанию.
        *   `value`: Новое значение.
    *   **Назначение**: Принудительно устанавливает новое значение для ключа по умолчанию.

### Переменные

*   `logger`: Экземпляр логгера для записи сообщений.
*   `config`: Словарь с конфигурационными параметрами, полученными из файла `config.ini`.
*   `default`: Словарь со значениями параметров по умолчанию для API.
*   `_api_type_to_client`: Словарь для хранения экземпляров классов-клиентов (например, `OpenAIClient`, `AzureClient`).
*   `_api_type_override`: Переменная для принудительного переопределения `API_TYPE` из конфигурационного файла.

### Цепочка взаимосвязей с другими частями проекта:

1.  **Конфигурация**: Код зависит от `utils.read_config_file()` для загрузки конфигурации из `config.ini`.
2.  **Утилиты**: Использует `utils.compose_initial_LLM_messages_with_templates` для подготовки сообщений для LLM.
3.  **Логирование**: Используется логгер для записи событий и ошибок, что помогает в отладке и мониторинге.
4.  **Кэширование**: Использует `pickle` для сохранения и загрузки кэша API-вызовов, что повышает эффективность и уменьшает затраты на API.

### Потенциальные ошибки и области для улучшения

1.  **Обработка ошибок**: Обработка ошибок в `send_message` может быть улучшена, например, можно добавить более специфичные исключения для разных типов ошибок API.
2.  **Токенизация**: Токенизация в `_count_tokens` сейчас имеет ряд исключений, для которых используется "костыль" с перенаправлением вызова к другой модели. Было бы лучше использовать `tiktoken` для всех моделей.
3.  **Кэширование**: Можно добавить функциональность для сброса кэша или для его очистки по истечении определенного времени.
4.  **Конфигурация**: Конфигурация переопределений `force_api_type`, `force_api_cache` и `force_default_value` может быть вынесена в отдельный класс или функцию.
5.  **Гибкость**: Можно добавить возможность использования прокси для запросов к API.

В целом, код представляет собой хорошо структурированный и расширяемый способ взаимодействия с OpenAI и Azure OpenAI API, предоставляющий функциональность кэширования, логирования, и настраиваемые параметры.