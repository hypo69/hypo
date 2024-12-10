# Модуль `tinytroupe.control`

## Обзор

Данный модуль предоставляет классы и функции для управления симуляцией, включая инициализацию, сохранение состояния, добавление агентов, сред и фабрик.  Реализует механизмы кэширования и транзакционного управления.


## Классы

### `Simulation`

**Описание**: Класс `Simulation` управляет всей симуляцией. Он хранит информацию о статусе, агентах, средах, фабриках, а также данные о кэшировании и транзакциях.

**Атрибуты**:

- `id` (str): Идентификатор симуляции.
- `agents` (list): Список агентов в симуляции.
- `name_to_agent` (dict): Словарь, сопоставляющий имя агента с объектом агента.
- `environments` (list): Список сред в симуляции.
- `name_to_environment` (dict): Словарь, сопоставляющий имя среды с объектом среды.
- `factories` (list): Список фабрик в симуляции.
- `name_to_factory` (dict): Словарь, сопоставляющий имя фабрики с объектом фабрики.
- `status` (str): Текущий статус симуляции (`"stopped"` или `"started"`).
- `cache_path` (str): Путь к файлу кэша.
- `auto_checkpoint` (bool): Флаг автоматического создания чекпоинтов.
- `has_unsaved_cache_changes` (bool): Флаг наличия несохраненных изменений в кэше.
- `_under_transaction` (bool): Флаг, указывающий, находится ли симуляция в транзакции.
- `cached_trace` (list): Список состояний кэшированных транзакций.
- `execution_trace` (list): Список состояний текущих транзакций.


**Методы**:

- `__init__(self, id="default", cached_trace:list=None)`: Инициализирует симуляцию.
- `begin(self, cache_path:str=None, auto_checkpoint:bool=False)`: Начинает управление симуляцией.
- `end(self)`: Завершает управление симуляцией.
- `checkpoint(self)`: Сохраняет текущее состояние симуляции в кэш.
- `add_agent(self, agent)`: Добавляет агента в симуляцию.
- `add_environment(self, environment)`: Добавляет среду в симуляцию.
- `add_factory(self, factory)`: Добавляет фабрику в симуляцию.
- `_execution_trace_position(self) -> int`: Возвращает текущую позицию в execution trace, или -1 если trace пуста.
- `_function_call_hash(self, function_name, *args, **kwargs) -> int`: Вычисляет хеш для вызова функции.
- `_skip_execution_with_cache(self)`: Пропускает выполнение текущего действия, предполагая, что есть кэшированное состояние.
- `_is_transaction_event_cached(self, event_hash) -> bool`: Проверяет, соответствует ли хеш события кэшированному.
- `_drop_cached_trace_suffix(self)`: Удаляет суффикс кэшированного следа, начиная с текущей позиции выполнения.
- `_add_to_execution_trace(self, state: dict, event_hash: int, event_output)`: Добавляет состояние в execution_trace.
- `_add_to_cache_trace(self, state: dict, event_hash: int, event_output)`: Добавляет состояние в cached_trace.
- `_load_cache_file(self, cache_path:str)`: Загружает кэш из файла.
- `_save_cache_file(self, cache_path:str)`: Сохраняет кэш в файл.
- `begin_transaction(self)`: Начинает транзакцию.
- `end_transaction(self)`: Завершает транзакцию.
- `is_under_transaction(self)`: Проверяет, находится ли симуляция в транзакции.
- `_clear_communications_buffers(self)`: Очищает буферы сообщений всех агентов и сред.
- `_encode_simulation_state(self) -> dict`: Кодирует текущее состояние симуляции.
- `_decode_simulation_state(self, state: dict)`: Декодирует состояние симуляции.


### `Transaction`

**Описание**: Класс `Transaction` управляет транзакциями в симуляции. Он выполняет функцию, используя механизм кэширования и транзакций.

**Методы**:
- `__init__(self, obj_under_transaction, simulation, function, *args, **kwargs)`: Инициализирует транзакцию.
- `execute(self)`: Выполняет заданную функцию, используя кэширование.
- `_encode_function_output(self, output) -> dict`: Кодирует результат функции.
- `_decode_function_output(self, encoded_output: dict)`: Декодирует закодированный результат функции.


## Функции

### `transactional(func)`

**Описание**: Декоратор, который делает функцию транзакционной.

### `reset()`

**Описание**: Сбрасывает состояние управления симуляцией.

### `_simulation(id="default")`

**Описание**: Возвращает объект `Simulation` по идентификатору.

### `begin(cache_path=None, id="default", auto_checkpoint=False)`

**Описание**: Начинает управление симуляцией.

### `end(id="default")`

**Описание**: Завершает управление симуляцией.

### `checkpoint(id="default")`

**Описание**: Сохраняет состояние симуляции в кэш.

### `current_simulation()`

**Описание**: Возвращает текущую симуляцию.


## Исключения

- `SkipTransaction`: Исключение, сигнализирующее о необходимости пропустить транзакцию.
- `CacheOutOfSync`: Исключение, если кэшированное и свежевыполненное состояние не синхронизированы.
- `ExecutionCached`: Исключение, если выполнение уже кэшировано.