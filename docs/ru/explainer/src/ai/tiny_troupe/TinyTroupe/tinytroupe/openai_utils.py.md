## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:  

1.  **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.  
2.  **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,  
    которые импортируются при создании диаграммы.  
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,  
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!  
    
    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
    ```mermaid\
    flowchart TD\
        Start --> Header[<code>header.py</code><br> Determine Project Root]\
    \
        Header --> import[Import Global Settings: <br><code>from src import gs</code>] \
    ```

3.  **<объяснение>**: Предоставьте подробные объяснения:  
    -   **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.  
    -   **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.  
    -   **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.  
    -   **Переменные**: Их типы и использование.  
    -   Выделите потенциальные ошибки или области для улучшения.  

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).  

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

**Общий рабочий процесс:**

1.  **Инициализация:**
    *   Загрузка конфигурации из файла `config.ini` с помощью `utils.read_config_file()`.
    *   Определение дефолтных параметров для OpenAI API (модель, максимальное количество токенов, температура и т.д.)
    *   Инициализация кеша API, если это указано в конфиге.

2.  **Создание запроса к LLM:**
    *   Класс `LLMCall` используется для создания запросов к языковой модели (LLM).
    *   Метод `call` класса `LLMCall` формирует сообщение для модели с использованием шаблонов (`utils.compose_initial_LLM_messages_with_templates`), вызывает модель через `client().send_message` и возвращает ответ.
    *   Пример:
        ```python
        llm_call = LLMCall(system_template_name="summarization_system", user_template_name="summarization_user", model="gpt-4", temperature=0.5)
        response = llm_call.call(text_to_summarize="some very long text...")
        ```

3.  **Взаимодействие с OpenAI API:**
    *   Класс `OpenAIClient` управляет взаимодействием с OpenAI API.
    *   Метод `send_message` отправляет запрос к OpenAI API и возвращает ответ. Этот метод обрабатывает повторные попытки в случае ошибок и кеширует результаты, если это настроено.
        *   Перед отправкой запроса к API, метод проверяет наличие ключа в кеше. Если ключ существует, возвращает кешированный ответ.
        *   В случае отсутствия кешированного ответа, вызывается метод `_raw_model_call()`, который, в свою очередь, вызывает OpenAI API.
        *   В случае успешного запроса, ответ сохраняется в кеше, если это настроено.
        *   После получения ответа, метод извлекает контент из ответа с помощью `_raw_model_response_extractor()` и возвращает его.
    *   Метод `get_embedding` используется для получения векторного представления текста (embedding).
        *   Вызывает метод `_raw_embedding_model_call()`, который вызывает OpenAI API.
        *   После получения ответа, метод извлекает embedding из ответа с помощью `_raw_embedding_model_response_extractor()` и возвращает его.
    *   Пример:
        ```python
        openai_client = OpenAIClient(cache_api_calls=True)
        messages = [{"role": "user", "content": "What is the capital of France?"}]
        response = openai_client.send_message(messages)
        embedding = openai_client.get_embedding("This is a test text.")
        ```
    *  Метод `_count_tokens` используется для подсчета количества токенов в сообщении.
    
4.  **Поддержка Azure:**
    *   Класс `AzureClient` наследуется от `OpenAIClient` и обеспечивает поддержку Azure OpenAI Service API.
    *   `AzureClient` переопределяет метод `_setup_from_config` для установки параметров Azure API.
    *   Также переопределяет метод `_raw_model_call` для вызова Azure API.
    *   Пример:
        ```python
        azure_client = AzureClient()
        messages = [{"role": "user", "content": "Translate 'hello' to French"}]
        response = azure_client.send_message(messages)
        ```

5.  **Регистрация и выбор API:**
    *   Функция `register_client` используется для регистрации различных API клиентов (например, OpenAI или Azure).
    *   Функция `client` возвращает текущего выбранного клиента на основе конфигурации.
        *   Определяет тип API (openai или azure) из конфига.
        *   Возвращает соответствующий клиентский класс.

6.  **Обработка ошибок:**
    *   Обработка ошибок: `InvalidRequestError` для неверных запросов, `NonTerminalError` для ошибок, которые могут быть устранены повторным запросом.
    *   Используется механизм экспоненциального отката `aux_exponential_backoff`, если запрос завершился с ошибкой (например, из-за ограничения скорости).

7.  **Управление кешированием:**
    *   Методы `set_api_cache`, `_save_cache`, `_load_cache` управляют кешированием вызовов API в файле.

8.  **Переопределение параметров:**
    *   Функции `force_api_type`, `force_api_cache` и `force_default_value` позволяют переопределить параметры конфигурации.

**Поток данных:**

1.  Конфигурация загружается из `config.ini` с помощью `utils.read_config_file()`.
2.  Параметры конфигурации используются для создания экземпляров `OpenAIClient` или `AzureClient`.
3.  Класс `LLMCall` использует `utils.compose_initial_LLM_messages_with_templates` для подготовки сообщений, которые затем передаются в `client().send_message`.
4.  `send_message` вызывает `_raw_model_call` для отправки запроса к OpenAI или Azure API.
5.  API возвращает ответ, который обрабатывается `_raw_model_response_extractor`.
6.  Ответ передается обратно в `LLMCall`, а затем возвращается пользователю.
7.  Аналогично, `get_embedding` вызывает `_raw_embedding_model_call` и получает embedding, который затем обрабатывается `_raw_embedding_model_response_extractor` и возвращается пользователю.

## <mermaid>

```mermaid
flowchart TD
    subgraph "Конфигурация и инициализация"
        ConfigLoad[<code>utils.read_config_file()</code> <br> Загрузка конфигурации из config.ini]
        DefaultParams[Определение дефолтных параметров <br> (модель, токены, температура и т.д.)]
        CacheInit[Инициализация кеша API <br> (если cache_api_calls=True)]
        ConfigLoad --> DefaultParams
        DefaultParams --> CacheInit
    end

    subgraph "LLMCall"
    classDef llmcall fill:#f9f,stroke:#333,stroke-width:2px
        LLMCallInit(class llmcall)[Инициализация <br> <code>LLMCall</code> с шаблонами]
        ComposeMessages[<code>utils.compose_initial_LLM_messages_with_templates</code> <br> Составление сообщений для LLM]
        CallModel[<code>client().send_message</code> <br> Вызов LLM модели]
        ProcessResponse[Обработка ответа модели]
        ReturnResponse[Возврат ответа]
        LLMCallInit --> ComposeMessages
        ComposeMessages --> CallModel
        CallModel --> ProcessResponse
        ProcessResponse --> ReturnResponse
    end

    subgraph "OpenAIClient"
        classDef openaic fill:#ccf,stroke:#333,stroke-width:2px
        OpenAIClientInit(class openaic)[Инициализация <code>OpenAIClient</code>]
        SendMessage(class openaic)[<code>send_message</code> <br> Отправка сообщения в API]
        CacheCheck[Проверка наличия в кеше]
        RawModelCall(class openaic)[<code>_raw_model_call</code> <br> Вызов OpenAI API]
        RawResponseExtractor(class openaic)[<code>_raw_model_response_extractor</code> <br> Извлечение ответа]
        CacheSave(class openaic)[<code>_save_cache</code> <br> Сохранение в кеш]
        TokenCount(class openaic)[<code>_count_tokens</code> <br> Подсчет токенов]
        GetEmbedding(class openaic)[<code>get_embedding</code> <br> Получение embedding]
        RawEmbeddingCall(class openaic)[<code>_raw_embedding_model_call</code> <br> Вызов API для embedding]
        RawEmbeddingExtractor(class openaic)[<code>_raw_embedding_model_response_extractor</code> <br> Извлечение embedding]

        OpenAIClientInit --> SendMessage
        SendMessage --> CacheCheck
        CacheCheck -- "Да (в кеше)" --> RawResponseExtractor
        CacheCheck -- "Нет (не в кеше)" --> RawModelCall
        RawModelCall --> CacheSave
        CacheSave --> RawResponseExtractor
        SendMessage --> TokenCount
        
        OpenAIClientInit --> GetEmbedding
        GetEmbedding --> RawEmbeddingCall
        RawEmbeddingCall --> RawEmbeddingExtractor

    end

    subgraph "AzureClient"
        classDef azurec fill:#cff,stroke:#333,stroke-width:2px
        AzureClientInit(class azurec)[Инициализация <code>AzureClient</code>]
        AzureSendMessage(class azurec)[<code>send_message</code> (Azure) <br> Отправка сообщения в Azure API]
        AzureRawModelCall(class azurec)[<code>_raw_model_call</code> (Azure) <br> Вызов Azure API]

        AzureClientInit --> AzureSendMessage
        AzureSendMessage --> CacheCheck
        CacheCheck -- "Нет (не в кеше)" --> AzureRawModelCall
        AzureRawModelCall --> CacheSave
        CacheSave --> RawResponseExtractor
    end
    
    subgraph "Client Registry"
        ClientRegister[<code>register_client</code> <br> Регистрация клиентов API]
        GetClient[<code>client()</code> <br> Получение клиента]

        ClientRegister --> GetClient
        GetClient -- "OpenAI" --> SendMessage
        GetClient -- "Azure" --> AzureSendMessage
        GetClient --> GetEmbedding
    end

     
    ConfigLoad --> ClientRegister
    ReturnResponse --> SendMessage
    RawResponseExtractor --> ReturnResponse
    RawEmbeddingExtractor --> ReturnResponse
    
    
    
    
    classDef client_registry fill:#efe,stroke:#333,stroke-width:2px
    ClientRegister(class client_registry)
    GetClient(class client_registry)
    
    classDef settings fill:#ddd,stroke:#333,stroke-width:2px
    ConfigLoad(class settings)
    DefaultParams(class settings)
    CacheInit(class settings)
    

    
    
```

**Анализ зависимостей `mermaid`:**

*   `Конфигурация и инициализация`:
    *   `ConfigLoad`: Загружает конфигурацию из файла `config.ini`. Использует функцию `utils.read_config_file()`.
    *   `DefaultParams`: Определяет дефолтные значения параметров на основе конфигурации.
    *   `CacheInit`: Инициализирует кеш API, если это включено в конфигурации.

*   `LLMCall`:
    *   `LLMCallInit`: Инициализация класса `LLMCall` с шаблонами `system_template_name`, `user_template_name` и параметрами `model_params`.
    *   `ComposeMessages`: Использует `utils.compose_initial_LLM_messages_with_templates` для формирования сообщений.
    *   `CallModel`: Вызывает метод `send_message` объекта `client()` для отправки запроса к модели.
    *   `ProcessResponse`: Обрабатывает ответ от модели для извлечения необходимой информации.
    *   `ReturnResponse`: Возвращает ответ.

*   `OpenAIClient`:
    *   `OpenAIClientInit`: Инициализирует экземпляр класса `OpenAIClient`.
    *   `SendMessage`: Метод `send_message` для отправки сообщения в OpenAI API.
    *   `CacheCheck`: Проверяет, есть ли запрос в кеше.
    *   `RawModelCall`: Метод `_raw_model_call`, который выполняет запрос к API.
    *   `RawResponseExtractor`: Метод `_raw_model_response_extractor` для извлечения необходимой информации из ответа.
    *   `CacheSave`: Метод `_save_cache` для сохранения ответа в кеш.
    *   `TokenCount`: Метод `_count_tokens` для подсчета токенов в сообщении.
    *   `GetEmbedding`: Метод `get_embedding` для получения векторного представления текста.
    *   `RawEmbeddingCall`: Метод `_raw_embedding_model_call` для вызова API для embedding.
    *   `RawEmbeddingExtractor`: Метод `_raw_embedding_model_response_extractor` для извлечения embedding из ответа.

*   `AzureClient`:
    *   `AzureClientInit`: Инициализирует экземпляр класса `AzureClient`.
    *   `AzureSendMessage`: Метод `send_message` для отправки сообщения в Azure API.
    *   `AzureRawModelCall`: Метод `_raw_model_call`, который выполняет запрос к Azure API.

*   `Client Registry`:
    *   `ClientRegister`: Регистрирует экземпляры классов `OpenAIClient` и `AzureClient`.
    *   `GetClient`: Возвращает текущего выбранного клиента на основе конфигурации.

## <объяснение>

**Импорты:**

*   `os`: Для взаимодействия с операционной системой, например, для чтения переменных окружения.
*   `openai`: Основная библиотека для взаимодействия с OpenAI API.
*   `openai.OpenAI`, `openai.AzureOpenAI`: Классы для создания клиентов OpenAI и Azure OpenAI соответственно.
*   `time`: Для работы со временем, например, для задержек между запросами.
*   `json`: Для работы с JSON (хотя в этом коде напрямую не используется, может использоваться в других частях проекта).
*   `pickle`: Для сохранения и загрузки объектов Python (используется для кеширования).
*   `logging`: Для логирования событий.
*   `configparser`: Для работы с файлами конфигурации (`.ini`).
*   `tiktoken`: Для подсчета токенов в тексте.
*   `tinytroupe.utils`: Пользовательский модуль `utils`, содержащий функции для чтения конфигурации и обработки сообщений.

**Переменные:**

*   `logger`: Объект логгера для записи сообщений.
*   `config`: Словарь с конфигурационными параметрами, прочитанными из файла `config.ini`.
*   `default`: Словарь с дефолтными параметрами для OpenAI API, такими как модель, максимальное количество токенов, температура и т.д.
*   `_api_type_to_client`: Словарь для хранения зарегистрированных API-клиентов.
*   `_api_type_override`: Переменная для принудительного переопределения типа API.

**Классы:**

*   **`LLMCall`**:
    *   **Роль:** Представляет собой абстракцию для вызова языковой модели с использованием шаблонов сообщений.
    *   **Атрибуты:**
        *   `system_template_name`: Название шаблона системного сообщения.
        *   `user_template_name`: Название шаблона пользовательского сообщения.
        *   `model_params`: Параметры для модели (например, `model`, `temperature`).
    *   **Методы:**
        *   `__init__`: Конструктор, принимает имена шаблонов и параметры модели.
        *   `call`: Составляет сообщение из шаблонов, отправляет запрос в модель через `client().send_message` и возвращает ответ.
        *   `__repr__`: Возвращает строковое представление объекта.

*   **`OpenAIClient`**:
    *   **Роль:** Управляет взаимодействием с OpenAI API.
    *   **Атрибуты:**
        *   `cache_api_calls`: Флаг, указывающий, нужно ли кешировать API-вызовы.
        *   `cache_file_name`: Имя файла для кеша.
        *   `api_cache`: Словарь с кешированными ответами.
    *   **Методы:**
        *   `__init__`: Конструктор, инициализирует клиент, устанавливает кеш.
        *   `set_api_cache`: Включает или выключает кеширование API-вызовов.
        *   `_setup_from_config`: Настраивает параметры OpenAI API.
        *   `send_message`: Отправляет запрос к OpenAI API, обрабатывает ошибки, управляет кешированием и повторными попытками.
        *   `_raw_model_call`: Выполняет запрос к OpenAI API.
        *   `_raw_model_response_extractor`: Извлекает контент из ответа API.
        *   `_count_tokens`: Подсчитывает количество токенов в сообщении.
        *   `_save_cache`: Сохраняет кеш в файл.
        *   `_load_cache`: Загружает кеш из файла.
        *  `get_embedding`: Получает векторное представление текста (embedding)
        *  `_raw_embedding_model_call`: Выполняет запрос к OpenAI API для получения embedding.
        *  `_raw_embedding_model_response_extractor`: Извлекает embedding из ответа API.

*   **`AzureClient`**:
    *   **Роль:**  Наследуется от `OpenAIClient` и управляет взаимодействием с Azure OpenAI Service API.
    *   **Атрибуты:** (наследуются от `OpenAIClient`)
    *   **Методы:**
        *   `__init__`: Конструктор, инициализирует клиент Azure.
        *   `_setup_from_config`: Настраивает параметры Azure OpenAI API.
        *   `_raw_model_call`: Выполняет запрос к Azure OpenAI API.

*   **`InvalidRequestError`**:
    *   **Роль:** Пользовательское исключение для невалидных запросов к API.

*   **`NonTerminalError`**:
    *   **Роль:** Пользовательское исключение для ошибок, которые можно исправить повторным запросом.

**Функции:**

*   `register_client(api_type, client)`: Регистрирует API-клиента для определенного типа API.
*   `_get_client_for_api_type(api_type)`: Возвращает API-клиента для заданного типа API.
*   `client()`: Возвращает текущего выбранного API-клиента на основе конфигурации.
*   `force_api_type(api_type)`: Принудительно переключает тип API.
*   `force_api_cache(cache_api_calls, cache_file_name)`: Принудительно устанавливает параметры кеширования.
*  `force_default_value(key, value)`: Принудительно переопределяет дефолтное значение параметра конфигурации.

**Взаимосвязи с другими частями проекта:**

*   Импорт `tinytroupe.utils` указывает на использование пользовательского модуля `utils` из пакета `tinytroupe`. Модуль вероятно содержит функции для работы с конфигурацией и шаблонами.
*   Код использует конфигурацию из файла `config.ini`. Это означает, что проект имеет файл конфигурации, который управляет его поведением.
*   Код использует `logging` для ведения журнала. Это говорит о том, что проект имеет централизованную систему логирования.

**Потенциальные ошибки и области для улучшения:**

*   Обработка ошибок: Код обрабатывает ошибки `InvalidRequestError`, `openai.BadRequestError`, `openai.RateLimitError` и `NonTerminalError`, однако, может потребоваться более детальная обработка других исключений, которые могут возникнуть.
*   Подсчет токенов: Код использует `tiktoken` для подсчета токенов, но в случае если модель не будет поддерживаться `tiktoken`, может возникнуть исключение `NotImplementedError`. Этот момент нужно доработать, добавив поддержку новых моделей, или переписав метод для использования API OpenAI.
*   Кеширование: Кеширование выполняется с использованием `pickle`, что может быть небезопасным для не доверенных данных. Можно рассмотреть использование более безопасного формата для хранения кеша.
*   Управление конфигурацией: Код использует глобальную переменную `default` для хранения дефолтных параметров. Возможно, будет лучше использовать класс или словарь, чтобы избежать конфликтов имен переменных.
*   Повторные попытки: Механизм экспоненциального отката `aux_exponential_backoff` может быть более гибким и настраиваемым.

**Дополнительно:**

*   Код достаточно модульный и позволяет легко добавлять поддержку новых API.
*   Использование классов для API-клиентов улучшает структуру кода и его расширяемость.

В целом, код хорошо структурирован и реализует основные функции для работы с OpenAI и Azure OpenAI API. Однако есть несколько областей, где код можно улучшить для большей надежности и гибкости.