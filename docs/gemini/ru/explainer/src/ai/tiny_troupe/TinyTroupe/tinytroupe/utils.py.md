## <алгоритм>

### 1. `compose_initial_LLM_messages_with_templates`
   - **Вход:** `system_template_name` (str), `user_template_name` (str, optional), `rendering_configs` (dict, optional)
   - **Шаг 1:** Формирует путь к файлу шаблона системного сообщения (`system_prompt_template_path`), используя `system_template_name` и текущую директорию.
     - *Пример:* Если `system_template_name` равно `"system_task.md"`, путь может быть `/path/to/tinytroupe/prompts/system_task.md`.
   - **Шаг 2:** Создает пустой список `messages`.
   - **Шаг 3:** Читает содержимое файла шаблона системного сообщения и рендерит его с использованием `chevron.render` и `rendering_configs`.
     - *Пример:* Если файл содержит `"The agent's name is {{agent_name}}"` и `rendering_configs` содержит `{'agent_name': 'John'}`, то отрендеренное содержимое будет `"The agent's name is John"`.
   - **Шаг 4:** Добавляет отрендеренное сообщение в список `messages` с ролью `"system"`.
   - **Шаг 5:** Если `user_template_name` не `None`:
     - **Шаг 5.1:** Формирует путь к файлу шаблона пользовательского сообщения (`user_prompt_template_path`), используя `user_template_name` и текущую директорию.
       - *Пример:* Если `user_template_name` равно `"user_query.md"`, путь может быть `/path/to/tinytroupe/prompts/user_query.md`.
     - **Шаг 5.2:** Читает содержимое файла шаблона пользовательского сообщения и рендерит его с использованием `chevron.render` и `rendering_configs`.
     - **Шаг 5.3:** Добавляет отрендеренное сообщение в список `messages` с ролью `"user"`.
   - **Шаг 6:** Возвращает список `messages`.
   - **Выход:** `messages` (list)

### 2. `extract_json`
   - **Вход:** `text` (str)
   - **Шаг 1:** Использует регулярное выражение для удаления всего текста до первой открывающей фигурной или квадратной скобки.
     - *Пример:* Если `text` равно `"some text { "key": "value" }`, то `text` станет `"{ "key": "value" }"`.
   - **Шаг 2:** Использует регулярное выражение для удаления всего текста после последней закрывающей фигурной или квадратной скобки.
     - *Пример:* Если `text` равно `"{ "key": "value" } some text"`, то `text` станет `"{ "key": "value" }"`.
   - **Шаг 3:** Удаляет некорректные escape-последовательности, заменяя `\\'` на `'`.
     - *Пример:* Если `text` равно `"{ \\"key\\": \\"value\\\' }"` , то `text` станет `"{ \\"key\\": \\"value\\" }"`
   - **Шаг 4:** Пытается распарсить `text` как JSON и возвращает словарь.
   - **Шаг 5:** В случае ошибки возвращает пустой словарь.
   - **Выход:** `dict`

### 3. `extract_code_block`
    - **Вход:** `text` (str)
    - **Шаг 1:** Использует регулярное выражение для удаления всего текста до первой открывающей последовательности из трех обратных кавычек (` ``` `).
      - *Пример:* Если `text` равно `"some text ```code block```"`, то `text` станет `"```code block```"`.
    - **Шаг 2:** Использует регулярное выражение для удаления всего текста после последней закрывающей последовательности из трех обратных кавычек (` ``` `).
      - *Пример:* Если `text` равно `"```code block``` some text"`, то `text` станет `"```code block```"`.
    - **Шаг 3:** Возвращает извлеченный блок кода.
    - **Шаг 4:** В случае ошибки возвращает пустую строку.
    - **Выход:** `str`

### 4. `repeat_on_error`
   - **Вход:** `retries` (int), `exceptions` (list)
   - **Шаг 1:** Возвращает декоратор `decorator`
   - **Шаг 2:** Декоратор `decorator` принимает функцию `func`
   - **Шаг 3:** Возвращает функцию-обертку `wrapper`
   - **Шаг 4:** Функция-обертка `wrapper` :
     -  Итерирует `retries` раз.
     -  Пытается выполнить вызов `func(*args, **kwargs)`
        -  Если исключения нет, возвращает результат `func`.
     -  Если возникает исключение из списка `exceptions`
        -  Логирует ошибку.
        -  Если это последняя попытка, выбрасывает исключение.
        -  Иначе, логирует повторную попытку и продолжает цикл.
   - **Выход:** Декорированная функция

### 5. `check_valid_fields`
   - **Вход:** `obj` (dict), `valid_fields` (list)
   - **Шаг 1:** Итерирует по ключам в словаре `obj`.
   - **Шаг 2:** Если ключ не найден в списке `valid_fields`, выбрасывает `ValueError`.
   - **Выход:** `None`

### 6. `sanitize_raw_string`
   - **Вход:** `value` (str)
   - **Шаг 1:** Кодирует строку в UTF-8, игнорируя ошибки, и декодирует обратно.
   - **Шаг 2:** Возвращает строку, обрезанную до максимальной длины строки Python.
   - **Выход:** `str`

### 7. `sanitize_dict`
   - **Вход:** `value` (dict)
   - **Шаг 1:** Преобразует словарь в JSON строку, исключая ASCII.
   - **Шаг 2:** Санитизирует строку, используя `sanitize_raw_string`.
   - **Шаг 3:** Преобразует санитизированную JSON строку обратно в словарь.
   - **Выход:** `dict`

### 8. `add_rai_template_variables_if_enabled`
   - **Вход:** `template_variables` (dict)
   - **Шаг 1:** Импортирует конфигурацию `from tinytroupe import config`.
   - **Шаг 2:** Определяет, включена ли защита от вредоносного контента и нарушения авторских прав, считывая значения из `config.ini`.
   - **Шаг 3:** Формирует путь к файлу с информацией о предотвращении вредоносного контента.
   - **Шаг 4:** Считывает содержимое файла.
   - **Шаг 5:** Добавляет содержимое файла в `template_variables` под ключом `'rai_harmful_content_prevention'`, если соответствующая защита включена, иначе присваивает `None`.
   - **Шаг 6:** Формирует путь к файлу с информацией о предотвращении нарушения авторских прав.
   - **Шаг 7:** Считывает содержимое файла.
   - **Шаг 8:** Добавляет содержимое файла в `template_variables` под ключом `'rai_copyright_infringement_prevention'`, если соответствующая защита включена, иначе присваивает `None`.
   - **Выход:** `template_variables` (dict)

### 9. `inject_html_css_style_prefix`
   - **Вход:** `html` (str), `style_prefix_attributes` (str)
   - **Шаг 1:** Заменяет все вхождения `style="` на `style="{style_prefix_attributes};` в `html`.
   - **Выход:** `html` (str)

### 10. `break_text_at_length`
    - **Вход:** `text` (str | dict), `max_length` (int, optional)
    - **Шаг 1:** Если `text` является словарем, преобразует его в JSON-строку с отступами.
    - **Шаг 2:** Если `max_length` является `None` или длина `text` меньше или равна `max_length`, возвращает `text`.
    - **Шаг 3:** Иначе, обрезает `text` до `max_length`, добавляет " (...) " и возвращает.
    - **Выход:** `str`

### 11. `pretty_datetime`
    - **Вход:** `dt` (datetime)
    - **Шаг 1:** Форматирует `dt` в строку в формате "ГГГГ-ММ-ДД ЧЧ:ММ".
    - **Выход:** `str`

### 12. `dedent`
    - **Вход:** `text` (str)
    - **Шаг 1:** Удаляет общий отступ из `text`.
    - **Шаг 2:** Удаляет пробелы в начале и конце `text`.
    - **Выход:** `str`

### 13. `read_config_file`
    - **Вход:** `use_cache` (bool, default True), `verbose` (bool, default True)
    - **Шаг 1:** Если `use_cache` равно True и глобальная переменная `_config` не None, возвращает кэшированный конфиг.
    - **Шаг 2:** Создает экземпляр `configparser.ConfigParser`.
    - **Шаг 3:** Формирует путь к файлу конфигурации по умолчанию (`config.ini`) в текущей директории модуля.
      -  Пример:  `./tinytroupe/config.ini`
    - **Шаг 4:** Если файл существует, считывает его содержимое, устанавливает `_config` и переходит к шагу 6, если нет, то ошибка.
    - **Шаг 5:** Формирует путь к пользовательскому файлу конфигурации (`config.ini`) в текущей рабочей директории.
      -  Пример: `./config.ini`
    - **Шаг 6:** Если файл существует, считывает его содержимое, устанавливает `_config` и возвращает конфиг, если нет, выводит сообщение и переходит к шагу 8.
    - **Шаг 7:** Если не удалось найти пользовательский конфиг, то выводит сообщение о том, что будут использоваться только значения по умолчанию.
    - **Шаг 8:** Возвращает загруженный конфиг.
    - **Выход:** `configparser.ConfigParser`

### 14. `pretty_print_config`
    - **Вход:** `config` (configparser.ConfigParser)
    - **Шаг 1:** Выводит в консоль текущую конфигурацию с форматированным выводом.
    - **Выход:** `None`

### 15. `start_logger`
    - **Вход:** `config` (configparser.ConfigParser)
    - **Шаг 1:** Получает или создает логгер с именем "tinytroupe".
    - **Шаг 2:** Получает уровень логирования из конфига, по умолчанию 'INFO'.
    - **Шаг 3:** Устанавливает уровень логирования для логгера.
    - **Шаг 4:** Создает обработчик консольного вывода.
    - **Шаг 5:** Устанавливает уровень логирования для обработчика.
    - **Шаг 6:** Создает форматтер лога.
    - **Шаг 7:** Устанавливает форматтер для обработчика.
    - **Шаг 8:** Добавляет обработчик к логгеру.
    - **Выход:** `None`

### 16. `JsonSerializableRegistry`
    - **Класс-миксин** для поддержки сериализации и десериализации JSON.
    - **`to_json`**:
        - **Вход:** `include` (list, optional), `suppress` (list, optional), `file_path` (str, optional).
        - **Шаг 1:** Собирает все атрибуты для сериализации и подавления, основываясь на иерархии классов.
        - **Шаг 2:** Переопределяет атрибуты, если переданы `include` и `suppress`.
        - **Шаг 3:** Создает словарь, включающий имя класса, и итерирует по атрибутам:
            - Если атрибут является экземпляром `JsonSerializableRegistry`, вызывает `to_json` рекурсивно.
            - Если атрибут является списком, рекурсивно вызывает `to_json` для каждого элемента (если они являются экземплярами `JsonSerializableRegistry`).
            - Если атрибут является словарем, рекурсивно вызывает `to_json` для каждого значения (если они являются экземплярами `JsonSerializableRegistry`).
            - Иначе, выполняет глубокое копирование значения.
        - **Шаг 4:** Если передан `file_path`, создает необходимые директории и записывает JSON в файл.
        - **Выход:** `dict`
    - **`from_json`**:
        - **Вход:** `json_dict_or_path` (dict or str), `suppress` (list, optional), `post_init_params` (dict, optional)
        - **Шаг 1:** Читает JSON из файла (если `json_dict_or_path` является строкой) или напрямую (если `json_dict_or_path` является словарем).
        - **Шаг 2:** Получает имя подкласса и класс из `class_mapping`.
        - **Шаг 3:** Создает экземпляр класса без вызова `__init__`.
        - **Шаг 4:** Собирает все атрибуты для сериализации, кастомные инициализаторы и атрибуты для подавления, основываясь на иерархии классов.
        - **Шаг 5:** Итерирует по ключам JSON (или атрибутам для сериализации):
            - Если ключ имеет кастомный инициализатор, вызывает его для значения и устанавливает его.
            - Если значение является словарем с именем класса, десериализует значение рекурсивно, вызывая `from_json`.
            - Если значение является списком, десериализует каждый элемент.
            - Иначе, выполняет глубокое копирование значения и устанавливает его.
        - **Шаг 6:** Если существует метод `_post_deserialization_init`, вызывает его после десериализации.
        - **Выход:** `object` (instance of the class)
    - **`__init_subclass__`**:
        - **Шаг 1:** Регистрирует подкласс в `class_mapping` по имени класса.
        - **Шаг 2:** Расширяет списки сериализуемых атрибутов и кастомных инициализаторов из родительских классов.
    - **`_post_deserialization_init`**:
        - **Шаг 1:** Вызывает метод `_post_init`, если таковой имеется.
        - **Выход:** `None`

### 17. `post_init`
    - **Вход:** `cls` (class)
    - **Шаг 1:** Декоратор, заменяет оригинальный метод `__init__` класса.
    - **Шаг 2:** Новый `__init__` вызывает оригинальный, а затем, если есть `_post_init`, вызывает его.
    - **Выход:** Декорированный класс

### 18. `name_or_empty`
    - **Вход:** `named_entity` (`AgentOrWorld`)
    - **Шаг 1:** Если `named_entity` равен `None`, возвращает пустую строку.
    - **Шаг 2:** Иначе, возвращает атрибут `name` переданного объекта.
    - **Выход:** `str`

### 19. `custom_hash`
    - **Вход:** `obj` (any)
    - **Шаг 1:** Преобразует объект в строку.
    - **Шаг 2:** Вычисляет SHA256-хеш от строки, закодированной в байты.
    - **Шаг 3:** Возвращает хеш в виде шестнадцатеричной строки.
    - **Выход:** `str`

### 20. `fresh_id`
    - **Вход:** `None`
    - **Шаг 1:** Увеличивает глобальную переменную `_fresh_id_counter` на 1.
    - **Шаг 2:** Возвращает текущее значение `_fresh_id_counter`.
    - **Выход:** `int`

## <mermaid>

```mermaid
flowchart TD
    subgraph "tinytroupe/utils.py"
    A[compose_initial_LLM_messages_with_templates] --> B(os.path.join: Construct Prompt Paths)
    B --> C(chevron.render: Render Templates)
    C --> D[Return LLM Messages]
    
    E[extract_json] --> F(re.sub: Remove Pre-JSON Text)
    F --> G(re.sub: Remove Post-JSON Text)
    G --> H(re.sub: Sanitize Escape Sequences)
    H --> I(json.loads: Parse JSON)
    I --> J[Return JSON Dict]
    
    K[extract_code_block] --> L(re.sub: Remove Pre-Code Text)
    L --> M(re.sub: Remove Post-Code Text)
    M --> N[Return Code Block]

    O[repeat_on_error] --> P(decorator: Decorator Function)
    P --> Q(wrapper: Wrapper Function)
    Q --> R{try-except}
    R -- Success --> S[Return Function Result]
    R -- Exception --> T{Retries Left?}
    T -- Yes --> Q
    T -- No --> U[Raise Exception]

    V[check_valid_fields] --> W{Check Keys}
    W -- Invalid Key --> X[Raise ValueError]
    W -- Valid Keys --> Y[Return None]
    
    Z[sanitize_raw_string] --> AA(value.encode: Encode to UTF-8)
    AA --> BB(value.decode: Decode to UTF-8)
    BB --> CC(value[:sys.maxsize]: Limit String Length)
    CC --> DD[Return Sanitized String]

    EE[sanitize_dict] --> FF(json.dumps: Convert to JSON)
    FF --> GG(sanitize_raw_string: Sanitize JSON string)
    GG --> HH(json.loads: Convert back to dict)
    HH --> II[Return Sanitized Dict]

    JJ[add_rai_template_variables_if_enabled] --> KK(config.getboolean: Read Config Flags)
    KK --> LL(open: Read RAI Prompts)
    LL --> MM[Update template_variables]
    MM --> NN[Return template_variables]

    OO[inject_html_css_style_prefix] --> PP(html.replace: Inject Style Prefix)
    PP --> QQ[Return Modified HTML]

    RR[break_text_at_length] --> SS{Is dict?}
    SS -- Yes --> TT(json.dumps: Convert dict to JSON String)
    TT --> UU{Check Max Length}
    SS -- No --> UU
    UU -- Length Check Pass --> VV[Return String]
    UU -- Length Check Fail --> WW(Slice and append "(...)")
    WW --> VV
    
    XX[pretty_datetime] --> YY(dt.strftime: Format Datetime)
    YY --> ZZ[Return Formatted String]

    AAA[dedent] --> BBB(textwrap.dedent: Dedent String)
    BBB --> CCC(strip: Remove Leading/Trailing Spaces)
    CCC --> DDD[Return Dedented String]
    
    EEE[read_config_file] --> FFF{use_cache and config?}
    FFF -- Yes --> GGG[Return cached config]
    FFF -- No --> HHH(configparser.ConfigParser: Init Config)
    HHH --> III(Path: Construct Config Path)
    III --> JJJ{Does config file exist?}
    JJJ -- Yes --> KKK(config.read: Read Default Config)
    KKK --> LLL{Custom config file exist?}
    JJJ -- No --> MMM[Raise ValueError]
    LLL -- Yes --> NNN(config.read: Read Custom Config)
    NNN --> OOO[Return config]
    LLL -- No --> OOO
    
    PPP[pretty_print_config] --> QQQ(Iterate Config Sections)
    QQQ --> RRR(Print Formatted Config)
    
    SSS[start_logger] --> TTT(logging.getLogger: Get Logger)
    TTT --> UUU(config.get: Get Log Level)
    UUU --> VVV(logger.setLevel: Set Log Level)
    VVV --> WWW(logging.StreamHandler: Create Handler)
    WWW --> XXX(logging.Formatter: Create Formatter)
    XXX --> YYY(ch.setFormatter: Set Formatter)
    YYY --> ZZZ(logger.addHandler: Add Handler)
    
    A1[JsonSerializableRegistry]
    subgraph A1
    A11[to_json] --> A12(Gather Serializable Attrs)
    A12 --> A13(Iterate Attributes)
    A13 --> A14{Attribute is JsonSerializableRegistry?}
        A14 -- Yes --> A15(Recursively call to_json)
        A14 -- No --> A16{Attribute is a list?}
            A16 -- Yes --> A17(Recursively call to_json for list elements)
            A16 -- No --> A18{Attribute is a dict?}
                A18 -- Yes --> A19(Recursively call to_json for dict values)
                A18 -- No --> A1A(copy.deepcopy: Copy attribute)
                A19 --> A1A
            A17 --> A1A
        A15 --> A1A
    A1A --> A1B[Build JSON Dict]
    A1B --> A1C{File Path provided?}
        A1C -- Yes --> A1D(os.makedirs: Create directories)
        A1D --> A1E(json.dump: Write to file)
        A1C -- No --> A1E
    A1E --> A1F[Return JSON Dict]

    A1G[from_json] --> A1H{json_dict_or_path is str?}
        A1H -- Yes --> A1I(open/json.load: read file)
        A1I --> A1J[Get subclass, create instance]
        A1H -- No --> A1J
    A1J --> A1K(Gather Serialization Attrs)
    A1K --> A1L(Iterate JSON keys)
    A1L --> A1M{key has custom initializer?}
    A1M -- Yes --> A1N(Call custom Initializer)
    A1M -- No --> A1O{Value is another JsonSerializableRegistry?}
    A1O -- Yes --> A1P(Recursively call from_json)
    A1O -- No --> A1Q{Value is a list?}
        A1Q -- Yes --> A1R(Deserialize list items recursively)
        A1R --> A1S(setattr)
        A1Q -- No --> A1S
    A1P --> A1S
    A1N --> A1S
    A1S --> A1T{has _post_deserialization_init?}
    A1T -- Yes --> A1U(Call _post_deserialization_init)
    A1T -- No --> A1V[Return object]
    A1U --> A1V

    A1W[__init_subclass__] --> A1X(Register the subclass)
    A1X --> A1Y(Extend serializable attributes and custom initializers)

    A1Z[_post_deserialization_init] --> A2A(call _post_init if exists)
    end

    A2B[post_init] --> A2C(Wraps __init__)
    A2C --> A2D(Calls _post_init if exists)

    A2E[name_or_empty] --> A2F{named_entity is None?}
    A2F -- Yes --> A2G[Return empty String]
    A2F -- No --> A2H(Return named_entity.name)

    A2I[custom_hash] --> A2J(str: Convert to string)
    A2J --> A2K(hashlib.sha256: create hash)
    A2K --> A2L[Return Hex String]

    A2M[fresh_id] --> A2N(Increment _fresh_id_counter)
    A2N --> A2O[Return _fresh_id_counter]
    end
```

###  Импорты:

-   `re`: Используется для работы с регулярными выражениями, в основном для извлечения JSON и блоков кода.
-   `json`: Используется для работы с JSON, включая сериализацию и десериализацию.
-   `os`: Используется для взаимодействия с операционной системой, например, для построения путей к файлам.
-   `sys`: Предоставляет доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором Python, используется для определения максимальной длины строки.
-   `hashlib`: Предоставляет алгоритмы хеширования, используется для создания детерминированного хеша.
-   `textwrap`: Используется для форматирования текста, в частности, для удаления отступов.
-   `logging`: Используется для создания логов, записи сообщений и управления уровнем отладки.
-   `chevron`: Используется для рендеринга шаблонов с подстановками переменных.
-   `copy`: Используется для создания глубоких копий объектов, чтобы избежать нежелательных изменений.
-  `typing`: Используется для статической типизации, чтобы улучшить читаемость и облегчить отладку.
-  `datetime`: Используется для работы с датой и временем, форматирование в удобочитаемый формат.
-   `pathlib`: Используется для работы с файловыми путями в объектно-ориентированном стиле.
-   `configparser`: Используется для чтения и обработки файлов конфигурации в формате `.ini`.
-  `AgentOrWorld`:  `Union` type hint для использования типов  `TinyPerson` или `TinyWorld`

###  Функции:

-   `compose_initial_LLM_messages_with_templates(system_template_name: str, user_template_name: str = None, rendering_configs: dict = {}) -> list`:
    -   **Аргументы:**
        -   `system_template_name`: Имя файла шаблона для системного сообщения.
        -   `user_template_name`: Имя файла шаблона для пользовательского сообщения (опционально).
        -   `rendering_configs`: Словарь с переменными для подстановки в шаблоны.
    -   **Возвращает:** Список словарей, представляющих сообщения для LLM, каждое с ключами `"role"` и `"content"`.
    -   **Назначение:** Создает начальные сообщения для языковой модели (LLM), используя шаблоны и конфигурации.
-   `extract_json(text: str) -> dict`:
    -   **Аргументы:** `text`: Строка, из которой нужно извлечь JSON.
    -   **Возвращает:** Словарь, представляющий JSON-объект, или пустой словарь в случае ошибки.
    -   **Назначение:** Извлекает JSON-объект из строки, игнорируя текст до и после JSON.
-   `extract_code_block(text: str) -> str`:
    -   **Аргументы:** `text`: Строка, из которой нужно извлечь блок кода.
    -   **Возвращает:** Строку, представляющую блок кода, или пустую строку в случае ошибки.
    -   **Назначение:** Извлекает блок кода из строки, игнорируя текст до и после блока кода.
-   `repeat_on_error(retries: int, exceptions: list)`:
    -   **Аргументы:**
        -   `retries`: Количество попыток повтора вызова функции в случае ошибки.
        -   `exceptions`: Список типов исключений, которые следует перехватывать.
    -   **Возвращает:** Декоратор.
    -   **Назначение:** Декоратор для повторного вызова функции в случае возникновения исключения.
-   `check_valid_fields(obj: dict, valid_fields: list) -> None`:
    -   **Аргументы:**
        -   `obj`: Словарь, ключи которого нужно проверить.
        -   `valid_fields`: Список допустимых ключей.
    -   **Возвращает:** `None`.
    -   **Назначение:** Проверяет, что все ключи в словаре `obj` присутствуют в списке `valid_fields`.
-   `sanitize_raw_string(value: str) -> str`:
    -   **Аргументы:** `value`: Строка, которую нужно санитизировать.
    -   **Возвращает:** Санитизированная строка.
    -   **Назначение:** Санитизирует строку, удаляя недопустимые символы и обрезая ее до максимальной длины.
-   `sanitize_dict(value: dict) -> dict`:
    -   **Аргументы:** `value`: Словарь, который нужно санитизировать.
    -   **Возвращает:** Санитизированный словарь.
    -   **Назначение:** Санитизирует словарь, удаляя недопустимые символы и обеспечивая отсутствие слишком глубокой вложенности.
-  `add_rai_template_variables_if_enabled(template_variables: dict) -> dict`:
    - **Аргументы:** `template_variables`: Словарь переменных шаблона.
    - **Возвращает:** Обновленный словарь переменных шаблона.
    - **Назначение:** Добавляет переменные шаблона, связанные с RAI (Responsible AI), в словарь переменных шаблона, если соответствующие флаги включены в конфигурации.
-  `inject_html_css_style_prefix(html: str, style_prefix_attributes: str) -> str`:
    -  **Аргументы:** `html` - строка с HTML кодом, `style_prefix_attributes` - строка с css стилями.
    -  **Возвращает:** Модифицированная html строка.
    -  **Назначение:** Добавляет префикс к стилям в HTML строке.
-  `break_text_at_length(text: Union[str, dict], max_length: int = None) -> str`:
    - **Аргументы:** `text` - текст или словарь, `max_length` - максимальная длинна.
    - **Возвращает:** обрезанный текст, если длинна превысила `max_length`.
    - **Назначение:**  Обрезает текст по длинне, если текст - словарь, то преобразует его в JSON.
-  `pretty_datetime(dt: datetime) -> str`:
    - **Аргументы:** `dt` - объект datetime.
    - **Возвращает:** Строка с отформатированной датой.
    - **Назначение:**  Преобразует объект datetime в удобочитаемый формат.
-   `dedent(text: str) -> str`:
    -   **Аргументы:** `text`: Строка, у которой нужно удалить отступы.
    -   **Возвращает:** Строка без отступов.
    -   **Назначение:** Удаляет отступы из многострочного текста.
-   `read_config_file(use_cache: bool = True, verbose: bool = True) -> configparser.ConfigParser`:
    -   **Аргументы:**
        -   `use_cache`: Флаг использования кэшированного файла.
        -   `verbose`: Флаг подробного вывода.
    -   **Возвращает:** Объект `configparser.ConfigParser` с загруженной конфигурацией.
    -   **Назначение:** Читает файл конфигурации, возвращает кэшированный конфиг, если возможно.
-   `pretty_print_config(config: configparser.ConfigParser)`:
    -   **Аргументы:** `config`: Объект `configparser.ConfigParser` с конфигурацией.
    -   **Возвращает:** `None`.
    -   **Назначение:** Выводит текущую конфигурацию в консоль в удобочитаемом виде.
-   `start_logger(config: configparser.ConfigParser)`:
    -   **Аргументы:** `config`: Объект `configparser.ConfigParser` с конфигурацией.
    -   **Возвращает:** `None`.
    -   **Назначение:** Инициализирует логгер с заданным уровнем логирования.
-   `name_or_empty(named_entity: AgentOrWorld) -> str`:
    - **Аргументы:**  `named_entity`: Объект типа `AgentOrWorld`, то есть `TinyPerson` или `TinyWorld`
    - **Возвращает:** Имя объекта, или пустая строка, если объект равен `None`.
    - **Назначение:** Возвращает имя объекта, или пустую строку.
- `custom_hash(obj: Any) -> str`:
    - **Аргументы:** `obj`: Объект, который нужно хешировать.
    - **Возвращает:** Шестнадцатеричная строка хеша.
    - **Назначение:** Создает детерминированный хеш для любого объекта.
-   `fresh_id() -> int`:
    -   **Аргументы:** Нет.
    -   **Возвращает:** Уникальный идентификатор.
    -   **Назначение:** Генерирует уникальный ID для объектов.

###  Классы:

- `JsonSerializableRegistry`:
  -   **Роль:** Класс-миксин для поддержки сериализации и десериализации объектов в JSON.
    -   `class_mapping`: Статический атрибут для хранения соответствия имени класса с самим классом для возможности десериализации.
    -   `to_json(self, include: list = None, suppress: list = None, file_path: str = None) -> dict`:
        -   **Назначение:** Преобразует объект в JSON.
    -   `from_json(cls, json_dict_or_path, suppress: list = None, post_init_params: dict = None)`:
        -   **Назначение:** Создает объект из JSON.
    -   `__init_subclass__(cls, **kwargs)`:
        -   **Назначение:** Регистрирует подкласс и наследует атрибуты для сериализации.
    - `_post_deserialization_init(self, **kwargs)`:
        -