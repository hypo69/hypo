## <алгоритм>

1.  **Инициализация:**
    *   При первом импорте модуля `control.py`, вызывается функция `reset()`, которая сбрасывает глобальные переменные `_current_simulations` (словарь для хранения объектов `Simulation`) и `_current_simulation_id` в начальное состояние:  `_current_simulations = {"default": None}`, `_current_simulation_id = None`. Это гарантирует, что нет активных симуляций при запуске.
    *   Создается класс `Simulation`, который управляет ходом симуляции, хранит агентов, окружения, фабрики, а также кеш трасс и трассу выполнения симуляции.
        *   При создании объекта `Simulation` устанавливаются начальные значения, такие как `id`, `status` (остановлен), списки `agents`, `environments`, `factories`, пустой `cached_trace` и `execution_trace`, путь к кешу и флаги `auto_checkpoint`, `has_unsaved_cache_changes` и `_under_transaction`.

2.  **Начало симуляции:**
    *   Функция `begin(cache_path, id, auto_checkpoint)`:
        *   Проверяет, не запущена ли уже другая симуляция, используя `_current_simulation_id`. Если запущена - выбрасывает ошибку, в противном случае, начинает текущую симуляцию.
        *   Создает или получает существующий объект `Simulation` (если вызывается повторно с тем же `id`).
        *   Устанавливает статус симуляции в "started".
        *   Очищает старые данные агентов, окружений и фабрик, вызывая статические методы `clear_agents()`, `clear_environments()` и `clear_factories()` у соответствующих классов.
        *   Обнуляет счетчик id для новых объектов симуляции.
        *   Загружает данные из кеш-файла, если `cache_path` указан.

3.  **Управление агентами, средами и фабриками:**
    *   Методы `add_agent(agent)`, `add_environment(environment)` и `add_factory(factory)`:
        *   Добавляют агентов, окружения и фабрики в соответствующие списки симуляции.
        *   Проверяют уникальность имен добавляемых объектов и устанавливают `simulation_id`.

4.  **Транзакционное управление:**
    *   Метод `begin_transaction()` устанавливает флаг `_under_transaction` в `True` и очищает буферы коммуникации агентов и сред.
    *   Метод `end_transaction()` устанавливает флаг `_under_transaction` в `False`.
    *   Метод `is_under_transaction()` возвращает текущее состояние флага `_under_transaction`.
    *   Метод `_clear_communications_buffers()` очищает буферы коммуникации всех агентов и сред в симуляции.

5.  **Кеширование и выполнение:**
    *   Метод `_function_call_hash(function_name, *args, **kwargs)`:
        *   Генерирует hash-код для текущего вызова функции, включая имя функции и аргументы.
    *   Метод `_is_transaction_event_cached(event_hash)`:
        *   Проверяет, существует ли сохраненное состояние в `cached_trace` для текущей позиции `execution_trace`, и сравнивает хеш события.
        *   Если кэш существует и хеш события совпадает, то возвращает `True`, иначе `False`.
    *   Метод `_skip_execution_with_cache()`:
        *   Если состояние кэшировано, добавляет это состояние из `cached_trace` в `execution_trace`.
    *   Метод `_drop_cached_trace_suffix()`:
        *   Удаляет все элементы из `cached_trace`, находящиеся за текущей позицией `execution_trace`. Это делается для того, чтобы при повторном выполнении кода можно было обновить кэш.
    *   Метод `_add_to_execution_trace(state, event_hash, event_output)`:
         *   Добавляет текущее состояние в `execution_trace`, включая hash предыдущего состояния, hash события и результат события.
    *   Метод `_add_to_cache_trace(state, event_hash, event_output)`:
        *   Добавляет текущее состояние в `cached_trace`, включая hash предыдущего состояния, hash события и результат события.
    *   Метод `_load_cache_file(cache_path)`:
        *   Загружает сохраненный кеш симуляции из файла.
    *   Метод `_save_cache_file(cache_path)`:
        *   Сохраняет текущую трассу симуляции в файл.
    *   Класс `Transaction`:
        *   Оборачивает вызов функции для управления симуляцией.
        *   Если симуляция не запущена, функция выполняется без кэширования.
        *   Если симуляция запущена, проверяется наличие состояния в кэше. Если кэш совпадает, состояние загружается из кэша, иначе выполняется функция, сохраняется результат и состояние, и записывается в кэш и трассу выполнения.
        *   Функция `execute` также вызывает checkpoint если `auto_checkpoint` установлен.

6.  **Управление состоянием симуляции:**
    *   Метод `_encode_simulation_state()`:
        *   Кодирует состояние всех агентов, окружений и фабрик в словарь.
    *   Метод `_decode_simulation_state(state)`:
        *   Декодирует состояние симуляции из словаря, восстанавливая состояние агентов, окружений и фабрик.
    *   Методы `_encode_function_output(output)` и `_decode_function_output(encoded_output)`:
        *   Кодируют и декодируют результат выполнения функции, что позволяет хранить и восстанавливать объекты `TinyPerson`, `TinyWorld` и `TinyFactory`.

7. **Завершение симуляции:**
    *  Функция `end(id)`:
        * Устанавливает статус симуляции в "stopped".
        * Сохраняет текущую трассу симуляции в файл.

8.  **Декоратор `transactional`**:
    *   Создает обертку для функций, которая автоматически создает объект `Transaction`, передавая ему объект, над которым совершается транзакция, и саму функцию. Это позволяет кэшировать и контролировать выполнение функций в рамках симуляции.

9.  **Утилиты:**
    *   Функция `current_simulation()`:
        *   Возвращает текущий объект симуляции, если он существует, иначе `None`.
    *   Функция `checkpoint(id)`:
        * Сохраняет состояние симуляции в файл.
    *   Классы `SkipTransaction`, `CacheOutOfSync`, `ExecutionCached` представляют собой кастомные исключения, которые используются для обработки определенных ситуаций в процессе симуляции.

## <mermaid>

```mermaid
flowchart TD
    subgraph Simulation Class
        A[<code>__init__</code><br>Initialize Simulation] --> B(Set default values for id, agents, environments, factories, status, cache, traces and flags)
        B --> C{cached_trace is None?}
        C -- Yes --> D[Initialize empty cached_trace list]
        C -- No --> E[Assign given cached_trace list]
        D --> F[Initialize execution_trace list]
        E --> F
        F --> G[End of <code>__init__</code>]


        H[<code>begin</code><br>Start Simulation] --> I(Set status to started)
        I --> J(Assign cache path and auto checkpoint)
        J --> K(Clear agents, environments and factories)
        K --> L(Reset fresh id counter)
        L --> M{cache_path is not None?}
        M -- Yes --> N(Load cache from file)
        M -- No --> O[End of <code>begin</code>]
        N --> O
        
        P[<code>end</code><br>End Simulation] --> Q(Set status to stopped)
        Q --> R(Save current trace via <code>checkpoint</code>)
        R --> S[End of <code>end</code>]

        T[<code>checkpoint</code><br>Save Simulation State] --> U{has_unsaved_cache_changes?}
        U -- Yes --> V(Save cache to file)
        U -- No --> W(Log: "No unsaved cache changes to save")
        V --> X[End of <code>checkpoint</code>]
        W --> X

        Y[<code>add_agent</code><br>Add Agent to Simulation] --> Z{Agent name is unique?}
        Z -- Yes --> AA(Set simulation ID to agent and add agent to lists)
        Z -- No --> AB[Raise ValueError]
        AA --> AC[End of <code>add_agent</code>]

        AD[<code>add_environment</code><br>Add Environment to Simulation] --> AE{Environment name is unique?}
        AE -- Yes --> AF(Set simulation ID to environment and add environment to lists)
        AE -- No --> AG[Raise ValueError]
        AF --> AH[End of <code>add_environment</code>]


         AI[<code>add_factory</code><br>Add Factory to Simulation] --> AJ{Factory name is unique?}
         AJ -- Yes --> AK(Set simulation ID to factory and add factory to lists)
         AJ -- No --> AL[Raise ValueError]
         AK --> AM[End of <code>add_factory</code>]

        AN[<code>_execution_trace_position</code><br>Get Execution Trace Position] --> AO(Get position in the execution trace)
        AO --> AP[End of <code>_execution_trace_position</code>]

        AQ[<code>_function_call_hash</code><br>Get Hash of Function Call] --> AR(Compute the hash of the function call)
        AR --> AS[End of <code>_function_call_hash</code>]

        AT[<code>_skip_execution_with_cache</code><br>Skip Execution with Cached State] --> AU{Cached state exists for current position?}
        AU -- Yes --> AV(Add cached state to execution trace)
        AU -- No --> AW[Assertion Error]
        AV --> AX[End of <code>_skip_execution_with_cache</code>]


        AY[<code>_is_transaction_event_cached</code><br> Check if Transaction is Cached] --> AZ{Cache exists for current execution position?}
        AZ -- Yes --> BA{Execution trace position is valid?}
        BA -- Yes --> BB{Event hash and previous node match?}
        BB -- Yes --> BC[Return True]
        BB -- No --> BD[Return False]
        BA -- No --> BE[Raise ValueError]
        AZ -- No --> BF[Return False]
        BC --> BG[End of <code>_is_transaction_event_cached</code>]
        BD --> BG
        BF --> BG


        BH[<code>_drop_cached_trace_suffix</code><br>Drop Cached Trace Suffix] --> BI(Drop the cached trace suffix starting from current execution trace position)
        BI --> BJ[End of <code>_drop_cached_trace_suffix</code>]

        BK[<code>_add_to_execution_trace</code><br>Add State to Execution Trace] --> BL(Compute the hash of the previous execution pair, if any)
        BL --> BM(Add state to execution trace with previous_hash, event_hash, and event_output)
        BM --> BN[End of <code>_add_to_execution_trace</code>]

        BO[<code>_add_to_cache_trace</code><br>Add State to Cached Trace] --> BP(Compute the hash of the previous cached pair, if any)
        BP --> BQ(Add state to cached trace with previous_hash, event_hash, and event_output)
        BQ --> BR(Set has_unsaved_cache_changes to True)
        BR --> BS[End of <code>_add_to_cache_trace</code>]

        BT[<code>_load_cache_file</code><br>Load Cache File] --> BU{File exists?}
        BU -- Yes --> BV(Load cached trace from file)
        BU -- No --> BW(Log: "Cache file not found")
        BV --> BX[End of <code>_load_cache_file</code>]
        BW --> BX

        BY[<code>_save_cache_file</code><br>Save Cache File] --> BZ(Create temporary file and save cached trace to it)
        BZ --> CA(Replace the original cache file with the temporary file)
        CA --> CB(Set has_unsaved_cache_changes to False)
        CB --> CC[End of <code>_save_cache_file</code>]

        CD[<code>begin_transaction</code><br>Begin Transaction] --> CE(Set _under_transaction flag to True)
        CE --> CF(Clear communication buffers of agents and environments)
        CF --> CG[End of <code>begin_transaction</code>]

        CH[<code>end_transaction</code><br>End Transaction] --> CI(Set _under_transaction flag to False)
        CI --> CJ[End of <code>end_transaction</code>]

        CK[<code>is_under_transaction</code><br>Check if Under Transaction] --> CL(Return _under_transaction flag)
        CL --> CM[End of <code>is_under_transaction</code>]

        CN[<code>_clear_communications_buffers</code><br>Clear Communication Buffers] --> CO(Iterate through agents and environments to clear buffers)
        CO --> CP[End of <code>_clear_communications_buffers</code>]

        CQ[<code>_encode_simulation_state</code><br>Encode Simulation State] --> CR(Encode agents, environments and factories into a state dictionary)
        CR --> CS[End of <code>_encode_simulation_state</code>]

        CT[<code>_decode_simulation_state</code><br>Decode Simulation State] --> CU(Decode factories)
        CU --> CV(Decode environments)
        CV --> CW(Decode agents)
        CW --> CX[End of <code>_decode_simulation_state</code>]
    end

    subgraph Transaction Class
        DA[<code>__init__</code><br>Initialize Transaction] --> DB(Set object under transaction, simulation, function, args, and kwargs)
        DB --> DC{simulation is not None?}
        DC -- Yes --> DD{object has simulation id?}
        DD -- Yes --> DE{simulation id matches?}
        DE -- Yes --> DF[Log: Object is already captured by simulation]
        DE -- No --> DG[Raise ValueError]
        DD -- No --> DH{Object is TinyPerson?}
        DH -- Yes --> DI(Add the agent to the simulation)
        DH -- No --> DJ{Object is TinyWorld?}
        DJ -- Yes --> DK(Add the environment to the simulation)
        DJ -- No --> DL{Object is TinyFactory?}
        DL -- Yes --> DM(Add the factory to the simulation)
        DL -- No --> DN[Raise ValueError]
        DI --> DO[End of <code>__init__</code>]
        DK --> DO
        DM --> DO
        DC -- No --> DO
        DF --> DO

        DP[<code>execute</code><br>Execute Transaction] --> DQ{simulation is None or stopped?}
        DQ -- Yes --> DR(Execute the function without caching)
        DQ -- No --> DS{simulation status is started?}
        DS -- Yes --> DT(Compute event hash)
        DT --> DU{is event cached?}
        DU -- Yes --> DV(Skip execution and load cached state)
        DV --> DW(Decode the function output and return it)
        DU -- No --> DX{is under transaction?}
        DX -- Yes --> DY(Execute function without caching)
        DX -- No --> DZ(Begin Transaction)
        DZ --> EA(Drop cached trace suffix)
        EA --> EB(Execute function and cache the state)
        EB --> EC(End Transaction)
        EC --> ED[End of <code>execute</code>]
        DR --> ED
        DY --> ED
        DW --> ED

        EE[<code>_encode_function_output</code><br>Encode Function Output] --> EF{Output is None?}
        EF -- Yes --> EG[Return None]
        EF -- No --> EH{Output is TinyPerson?}
        EH -- Yes --> EI(Encode TinyPerson to JSON)
        EH -- No --> EJ{Output is TinyWorld?}
        EJ -- Yes --> EK(Encode TinyWorld to JSON)
        EJ -- No --> EL{Output is TinyFactory?}
        EL -- Yes --> EM(Encode TinyFactory to JSON)
        EL -- No --> EN{Output is primitive JSON type?}
        EN -- Yes --> EO(Encode as JSON)
        EN -- No --> EP[Raise ValueError]
        EI --> EQ[End of <code>_encode_function_output</code>]
        EK --> EQ
        EM --> EQ
        EO --> EQ
        EG --> EQ

        ER[<code>_decode_function_output</code><br>Decode Function Output] --> ES{Encoded output is None?}
        ES -- Yes --> ET[Return None]
        ES -- No --> EU{Encoded output is TinyPersonRef?}
        EU -- Yes --> EV(Get TinyPerson by name)
        EU -- No --> EW{Encoded output is TinyWorldRef?}
        EW -- Yes --> EX(Get TinyWorld by name)
        EW -- No --> EY{Encoded output is TinyFactoryRef?}
        EY -- Yes --> EZ(Get TinyFactory by name)
        EY -- No --> FA{Encoded output is JSON?}
        FA -- Yes --> FB(Return JSON value)
        FA -- No --> FC[Raise ValueError]
        ET --> FD[End of <code>_decode_function_output</code>]
        EV --> FD
        EX --> FD
        EZ --> FD
        FB --> FD
     end

    subgraph Global Functions
        GA[<code>reset</code><br>Reset Simulation Control State] --> GB(Reset _current_simulations and _current_simulation_id)
        GB --> GC[End of <code>reset</code>]

        GD[<code>_simulation</code><br>Get Simulation by ID] --> GE{Simulation exists for given id?}
        GE -- Yes --> GF(Return existing Simulation)
        GE -- No --> GG(Create new Simulation instance)
        GG --> GH(Assign it to _current_simulations dictionary)
        GH --> GI(Return newly created Simulation)
        GF --> GJ[End of <code>_simulation</code>]
        GI --> GJ
        
        GK[<code>begin</code><br>Start Simulation] --> GL{Is any simulation already started?}
        GL -- Yes --> GM[Raise ValueError]
        GL -- No --> GN(Start simulation for given id, with optional cache path)
        GN --> GO[Assign current simulation id]
        GO --> GP[End of <code>begin</code>]
        
        GQ[<code>end</code><br>End Simulation] --> GR(End simulation for given id)
        GR --> GS[Clear current simulation id]
        GS --> GT[End of <code>end</code>]

        GU[<code>checkpoint</code><br>Save Current Simulation State] --> GV(Save current simulation state for given id)
        GV --> GW[End of <code>checkpoint</code>]

         GX[<code>current_simulation</code><br>Get Current Simulation] --> GY{Is any simulation currently active?}
         GY -- Yes --> GZ(Get the current active simulation)
         GY -- No --> HA(Return None)
         GZ --> HB[End of <code>current_simulation</code>]
         HA --> HB

     end
     
     subgraph transactional decorator
        HC[<code>transactional</code><br>Decorator for transaction handling] --> HD(Defines a wrapper function)
        HD --> HE(In wrapper function: Get object under transaction and current simulation)
        HE --> HF(Create transaction object)
        HF --> HG(Execute transaction and return result)
        HG --> HH[End of <code>transactional</code>]
     end

    Start --> GA
    Start --> A
    Start --> DA
    Start --> HC
```

## <объяснение>

**Импорты:**

*   `json`: Используется для сериализации и десериализации данных в формате JSON, что необходимо для сохранения и загрузки состояния симуляции в файл.
*   `os`: Предоставляет функции для взаимодействия с операционной системой, например, для работы с файлами и путями.
*  `tempfile`: Используется для создания временных файлов для надежного сохранения данных симуляции.
*   `tinytroupe`: Импортируется для доступа к другим модулям в пакете `tinytroupe`, таким как `tinytroupe.utils`, `tinytroupe.agent`, `tinytroupe.environment` и `tinytroupe.factory`.
*   `tinytroupe.utils as utils`: Импортирует модуль `utils` из пакета `tinytroupe` для использования вспомогательных функций, таких как `custom_hash`, и переименовывает его в `utils`.
*   `logging`: Используется для логирования событий в процессе симуляции.

**Класс `Simulation`:**

*   **Назначение:** Класс `Simulation` является центральным компонентом, который управляет ходом симуляции, включая добавление агентов, сред и фабрик, обработку транзакций, кэширование состояния и сохранение данных.
*   **Атрибуты:**
    *   `id` (str): Идентификатор симуляции.
    *   `agents` (list): Список агентов, участвующих в симуляции.
    *   `name_to_agent` (dict): Словарь, сопоставляющий имена агентов с их объектами.
    *   `environments` (list): Список сред, в которых действуют агенты.
    *   `factories` (list): Список фабрик, которые могут создавать агентов.
    *   `name_to_factory` (dict): Словарь, сопоставляющий имена фабрик с их объектами.
    *   `name_to_environment` (dict): Словарь, сопоставляющий имена сред с их объектами.
    *   `status` (str): Текущий статус симуляции (`stopped` или `started`).
    *   `cache_path` (str): Путь к файлу кэша симуляции.
    *   `auto_checkpoint` (bool): Флаг, определяющий, нужно ли автоматически сохранять состояние после каждой транзакции.
    *   `has_unsaved_cache_changes` (bool): Флаг, показывающий, есть ли несохраненные изменения в кэше.
    *   `_under_transaction` (bool): Флаг, показывающий, находится ли симуляция в процессе транзакции.
    *   `cached_trace` (list): Список сохраненных состояний симуляции (кеш).
    *   `execution_trace` (list): Список выполненных состояний симуляции (трасса выполнения).
*   **Методы:**
    *   `__init__(id="default", cached_trace:list=None)`: Конструктор класса, инициализирует состояние симуляции.
    *   `begin(cache_path:str=None, auto_checkpoint:bool=False)`: Начинает симуляцию, загружает данные из кэша, если есть.
    *   `end()`: Завершает симуляцию, сохраняет состояние.
    *   `checkpoint()`: Сохраняет текущее состояние симуляции в файл.
    *   `add_agent(agent)`, `add_environment(environment)`, `add_factory(factory)`: Добавляют агентов, окружения и фабрики в симуляцию, проверяя их уникальность.
    *   `_execution_trace_position()`: Возвращает текущую позицию в трассе выполнения.
    *  `_function_call_hash(function_name, *args, **kwargs)`: Вычисляет хэш для вызова функции с аргументами.
    *  `_skip_execution_with_cache()`: Пропускает выполнение, если есть кэшированное состояние.
    *  `_is_transaction_event_cached(event_hash)`: Проверяет, есть ли соответствующее кэшированное состояние для события.
    * `_drop_cached_trace_suffix()`: Удаляет кэшированные состояния, следующие за текущей позицией в трассе выполнения.
    *  `_add_to_execution_trace(state: dict, event_hash: int, event_output)`: Добавляет состояние в трассу выполнения.
    *  `_add_to_cache_trace(state: dict, event_hash: int, event_output)`: Добавляет состояние в кэш.
    *  `_load_cache_file(cache_path:str)`: Загружает состояние симуляции из файла.
    *   `_save_cache_file(cache_path:str)`: Сохраняет состояние симуляции в файл.
    *   `begin_transaction()`, `end_transaction()`, `is_under_transaction()`: Методы для управления транзакциями.
    *   `_clear_communications_buffers()`: Очищает буферы сообщений агентов и сред.
    *   `_encode_simulation_state()`: Кодирует состояние симуляции в словарь.
    *   `_decode_simulation_state(state: dict)`: Декодирует состояние симуляции из словаря.

**Класс `Transaction`:**

*   **Назначение:** Класс `Transaction` используется для обертки функций, выполняемых в рамках симуляции, и обеспечивает управление кэшированием и выполнением этих функций.
*   **Атрибуты:**
    *   `obj_under_transaction`: Объект, над которым совершается транзакция (агент, среда или фабрика).
    *   `simulation`: Объект `Simulation`, в рамках которого выполняется транзакция.
    *   `function_name`: Имя функции, выполняемой в транзакции.
    *   `function`: Функция, выполняемая в транзакции.
    *   `args`: Позиционные аргументы функции.
    *   `kwargs`: Именованные аргументы функции.
*   **Методы:**
    *   `__init__(obj_under_transaction, simulation, function, *args, **kwargs)`: Конструктор класса.
    *   `execute()`: Выполняет транзакцию, обеспечивая кэширование и восстановление состояния.
    *   `_encode_function_output(output)`: Кодирует результат выполнения функции.
    *   `_decode_function_output(encoded_output)`: Декодирует результат выполнения функции.

**Декоратор `transactional`:**

*   **Назначение:** Декоратор `transactional` преобразует обычную функцию в функцию, которая может быть выполнена в рамках транзакции.
*   Применение: Оборачивает функции объектов, участвующих в симуляции, что позволяет кэшировать и контролировать их выполнение.

**Глобальные Функции:**

*   `reset()`: Сбрасывает состояние симуляции.
*  `_simulation(id="default")`: Создает или получает существующий объект симуляции по его `id`.
*  `begin(cache_path=None, id="default", auto_checkpoint=False)`: Начинает симуляцию.
*  `end(id="default")`: Завершает симуляцию.
*   `checkpoint(id="default")`: Сохраняет состояние симуляции.
*   `current_simulation()`: Возвращает текущую активную симуляцию.

**Исключения:**

*   `SkipTransaction`:  Исключение, которое может использоваться для пропуска транзакции, если это необходимо.
*   `CacheOutOfSync`:  Исключение, которое выбрасывается, если кэшированное состояние не соответствует текущему состоянию.
*   `ExecutionCached`: Исключение, которое выбрасывается, если выполнение функции было пропущено из-за наличия кэшированного результата.

**Взаимосвязи с другими частями проекта:**

*   Модуль `control.py` активно взаимодействует с другими частями проекта через импорты из `tinytroupe`. Он зависит от классов `TinyPerson`, `TinyWorld` и `TinyFactory`, которые определены в соответствующих модулях `agent.py`, `environment.py` и `factory.py`.
*   Использует модуль `utils` для расчета хешей.
*   Логика работы симуляции строится на основе взаимодействия между агентами и окружениями, чье состояние управляется через транзакции.

**Потенциальные ошибки и области для улучшения:**

*   **Обработка ошибок**: В некоторых местах используется `try-except` для обработки ошибок, но не всегда предоставляется достаточно подробная информация об ошибках в логах.
*   **Параллелизация**: В комментариях указано, что текущая версия поддерживает только одну симуляцию одновременно. В будущих версиях стоит рассмотреть возможность параллелизации.
*   **Очистка ресурсов**: Необходимо явно обрабатывать ошибки при создании и использовании временных файлов, чтобы не допустить утечку ресурсов.

В целом, `control.py` предоставляет мощный механизм для управления симуляциями, обеспечивая возможность кэширования и повторного использования состояний, что может существенно ускорить процесс разработки и отладки симуляций.