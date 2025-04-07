# Модуль управления симуляцией `tinytroupe`

## Обзор

Модуль `control.py` предоставляет механизмы управления симуляциями в проекте `tinytroupe`. Он включает в себя классы и функции для запуска, остановки, сохранения состояния симуляции, а также для управления агентами, средами и фабриками внутри симуляции. Модуль также реализует механизм кэширования для оптимизации выполнения симуляций.

## Подробнее

Этот модуль является ключевым компонентом для управления жизненным циклом симуляций, обеспечивая возможность сохранения и восстановления состояния симуляции для повторного использования. Он также предоставляет инструменты для работы с транзакциями, позволяя выполнять атомарные изменения состояния симуляции. Кэширование позволяет ускорить выполнение симуляций за счет повторного использования ранее вычисленных результатов.

## Содержание

1.  [Классы](#Классы)
    *   [Simulation](#Simulation)
    *   [Transaction](#Transaction)
2.  [Исключения](#Исключения)
    *   [SkipTransaction](#SkipTransaction)
    *   [CacheOutOfSync](#CacheOutOfSync)
    *   [ExecutionCached](#ExecutionCached)
3.  [Функции](#Функции)
    *   [reset](#reset)
    *   [_simulation](#_simulation)
    *   [begin](#begin)
    *   [end](#end)
    *   [checkpoint](#checkpoint)
    *   [current_simulation](#current_simulation)
    *   [cache_hits](#cache_hits)
    *   [cache_misses](#cache_misses)
    *   [transactional](#transactional)

## Классы

### `Simulation`

Описание: Класс `Simulation` предназначен для управления состоянием и выполнением симуляции. Он обеспечивает методы для добавления агентов, сред и фабрик, а также для сохранения и восстановления состояния симуляции.

**Атрибуты:**

*   `id` (str): Идентификатор симуляции. По умолчанию `"default"`.
*   `agents` (list): Список агентов, участвующих в симуляции.
*   `name_to_agent` (dict): Словарь, отображающий имена агентов в объекты агентов.
*   `environments` (list): Список сред, в которых происходит симуляция.
*   `factories` (list): Список фабрик, используемых для создания объектов в симуляции.
*   `name_to_factory` (dict): Словарь, отображающий имена фабрик в объекты фабрик.
*   `name_to_environment` (dict): Словарь, отображающий имена сред в объекты сред.
*   `status` (str): Статус симуляции (`"stopped"` или `"started"`).
*   `cache_path` (str): Путь к файлу кэша симуляции.
*   `auto_checkpoint` (bool): Флаг, указывающий, следует ли автоматически сохранять состояние симуляции после каждой транзакции.
*   `has_unsaved_cache_changes` (bool): Флаг, указывающий, есть ли несохраненные изменения в кэше.
*   `_under_transaction` (bool): Флаг, указывающий, находится ли симуляция в состоянии транзакции.
*   `cached_trace` (list): Список состояний симуляции, сохраненных в кэше.
*    `cache_misses` (int): Счетчик промахов кэша.
*   `cache_hits` (int): Счетчик попаданий в кэш.
*   `execution_trace` (list): Список состояний выполнения симуляции.

**Методы:**

*   `__init__(self, id="default", cached_trace: list = None)`: Инициализирует объект симуляции с заданным идентификатором и кэшем.
*   `begin(self, cache_path: str = None, auto_checkpoint: bool = False)`: Начинает симуляцию, загружает кэш и устанавливает параметры.
*   `end(self)`: Завершает симуляцию и сохраняет состояние.
*   `checkpoint(self)`: Сохраняет текущее состояние симуляции в файл.
*   `add_agent(self, agent)`: Добавляет агента в симуляцию.
*   `add_environment(self, environment)`: Добавляет среду в симуляцию.
*   `add_factory(self, factory)`: Добавляет фабрику в симуляцию.
*   `_execution_trace_position(self) -> int`: Возвращает текущую позицию в трассе выполнения.
*   `_function_call_hash(self, function_name, *args, **kwargs) -> int`: Вычисляет хэш вызова функции.
*   `_skip_execution_with_cache(self)`: Пропускает выполнение, используя кэшированное состояние.
*   `_is_transaction_event_cached(self, event_hash) -> bool`: Проверяет, закэшировано ли событие транзакции.
*   `_drop_cached_trace_suffix(self)`: Удаляет суффикс кэшированной трассы.
*   `_add_to_execution_trace(self, state: dict, event_hash: int, event_output)`: Добавляет состояние в трассу выполнения.
*   `_add_to_cache_trace(self, state: dict, event_hash: int, event_output)`: Добавляет состояние в кэшированную трассу.
*   `_load_cache_file(self, cache_path: str)`: Загружает кэш из файла.
*   `_save_cache_file(self, cache_path: str)`: Сохраняет кэш в файл.
*   `begin_transaction(self)`: Начинает транзакцию.
*   `end_transaction(self)`: Завершает транзакцию.
*   `is_under_transaction(self)`: Проверяет, находится ли симуляция в состоянии транзакции.
*   `_clear_communications_buffers(self)`: Очищает буферы обмена данными агентов и сред.
*   `_encode_simulation_state(self) -> dict`: Кодирует текущее состояние симуляции.
*   `_decode_simulation_state(self, state: dict)`: Декодирует состояние симуляции.

### `Transaction`

Описание: Класс `Transaction` предназначен для управления транзакциями в симуляции. Он обеспечивает выполнение функций в контексте транзакции, с возможностью кэширования результатов.

**Атрибуты:**

*   `obj_under_transaction`: Объект, над которым выполняется транзакция.
*   `simulation`: Объект симуляции, в которой выполняется транзакция.
*   `function_name` (str): Имя функции, выполняемой в транзакции.
*   `function`: Функция, выполняемая в транзакции.
*   `args` (tuple): Позиционные аргументы функции.
*   `kwargs` (dict): Именованные аргументы функции.

**Методы:**

*   `__init__(self, obj_under_transaction, simulation, function, *args, **kwargs)`: Инициализирует объект транзакции.
*   `execute(self)`: Выполняет транзакцию, используя кэш, если возможно.
*   `_encode_function_output(self, output) -> dict`: Кодирует результат выполнения функции для кэширования.
*   `_decode_function_output(self, encoded_output: dict)`: Декодирует результат выполнения функции из кэша.

## Исключения

### `SkipTransaction`

Описание: Исключение, используемое для пропуска транзакции.

### `CacheOutOfSync`

Описание: Исключение, возникающее, когда кэшированные и текущие данные рассинхронизированы.

### `ExecutionCached`

Описание: Исключение, возникающее, когда предложенное выполнение уже закэшировано.

## Функции

### `reset`

```python
def reset():
    """
    Resets the entire simulation control state.
    """
```

**Назначение**: Сбрасывает глобальное состояние управления симуляцией.

**Как работает функция**:

1. Устанавливает `_current_simulations` в `{"default": None}`, удаляя все текущие симуляции.
2. Устанавливает `_current_simulation_id` в `None`, отключая текущую активную симуляцию.

```
Начало
 |
 Сброс _current_simulations в {"default": None}
 |
 Сброс _current_simulation_id в None
Конец
```

### `_simulation`

```python
def _simulation(id="default"):
    """

    """
```

**Назначение**: Возвращает объект симуляции с заданным идентификатором, создавая его при необходимости.

**Параметры**:

*   `id` (str): Идентификатор симуляции. По умолчанию `"default"`.

**Возвращает**:

*   Объект `Simulation`.

**Как работает функция**:

1. Проверяет, существует ли уже симуляция с заданным `id` в `_current_simulations`.
2. Если симуляция не существует, создает новый объект `Simulation` и сохраняет его в `_current_simulations`.
3. Возвращает объект симуляции.

```
Начало
 |
Проверка наличия симуляции с id в _current_simulations
 |
Если нет:
  |
  Создание новой симуляции Simulation()
  |
  Сохранение в _current_simulations[id]
 |
Возврат _current_simulations[id]
Конец
```

### `begin`

```python
def begin(cache_path=None, id="default", auto_checkpoint=False):
    """
    Marks the start of the simulation being controlled.
    """
```

**Назначение**: Начинает контролируемую симуляцию.

**Параметры**:

*   `cache_path` (str): Путь к файлу кэша. По умолчанию `None`.
*   `id` (str): Идентификатор симуляции. По умолчанию `"default"`.
*   `auto_checkpoint` (bool): Флаг автоматического сохранения. По умолчанию `False`.

**Вызывает исключения**:

*   `ValueError`: Если симуляция уже запущена под другим идентификатором.

**Как работает функция**:

1. Проверяет, запущена ли уже какая-либо симуляция (`_current_simulation_id` не `None`).
2. Если симуляция не запущена, вызывает метод `begin` объекта `Simulation` с заданными параметрами.
3. Устанавливает `_current_simulation_id` в `id`, указывая, что симуляция запущена.
4. Если симуляция уже запущена, вызывает исключение `ValueError`.

```
Начало
 |
Проверка, запущена ли симуляция (_current_simulation_id is None)
 |
Если да:
  |
  Вызов _simulation(id).begin(cache_path, auto_checkpoint)
  |
  Установка _current_simulation_id = id
 |
Если нет:
  |
  Вызов исключения ValueError
Конец
```

### `end`

```python
def end(id="default"):
    """
    Marks the end of the simulation being controlled.
    """
```

**Назначение**: Завершает контролируемую симуляцию.

**Параметры**:

*   `id` (str): Идентификатор симуляции. По умолчанию `"default"`.

**Как работает функция**:

1. Вызывает метод `end` объекта `Simulation` с заданным `id`.
2. Устанавливает `_current_simulation_id` в `None`, указывая, что симуляция завершена.

```
Начало
 |
Вызов _simulation(id).end()
 |
Установка _current_simulation_id = None
Конец
```

### `checkpoint`

```python
def checkpoint(id="default"):
    """
    Saves current simulation state.
    """
```

**Назначение**: Сохраняет текущее состояние симуляции.

**Параметры**:

*   `id` (str): Идентификатор симуляции. По умолчанию `"default"`.

**Как работает функция**:

1. Вызывает метод `checkpoint` объекта `Simulation` с заданным `id`.

```
Начало
 |
Вызов _simulation(id).checkpoint()
Конец
```

### `current_simulation`

```python
def current_simulation():
    """
    Returns the current simulation.
    """
```

**Назначение**: Возвращает текущую активную симуляцию.

**Возвращает**:

*   Объект `Simulation` или `None`, если симуляция не запущена.

**Как работает функция**:

1. Проверяет, запущена ли какая-либо симуляция (`_current_simulation_id` не `None`).
2. Если симуляция запущена, возвращает объект `Simulation` с идентификатором `_current_simulation_id`.
3. Если симуляция не запущена, возвращает `None`.

```
Начало
 |
Проверка, запущена ли симуляция (_current_simulation_id is not None)
 |
Если да:
  |
  Возврат _simulation(_current_simulation_id)
 |
Если нет:
  |
  Возврат None
Конец
```

### `cache_hits`

```python
def cache_hits(id="default"):
    """
    Returns the number of cache hits.
    """
```

**Назначение**: Возвращает количество попаданий в кэш для заданной симуляции.

**Параметры**:

*   `id` (str): Идентификатор симуляции. По умолчанию `"default"`.

**Возвращает**:

*   Количество попаданий в кэш.

**Как работает функция**:

1.  Вызывает метод `cache_hits` объекта `_simulation(id)`.

```
Начало
 |
Вызов _simulation(id).cache_hits
Конец
```

### `cache_misses`

```python
def cache_misses(id="default"):
    """
    Returns the number of cache misses.
    """
```

**Назначение**: Возвращает количество промахов кэша для заданной симуляции.

**Параметры**:

*   `id` (str): Идентификатор симуляции. По умолчанию `"default"`.

**Возвращает**:

*   Количество промахов кэша.

**Как работает функция**:

1.  Вызывает метод `cache_misses` объекта `_simulation(id)`.

```
Начало
 |
Вызов _simulation(id).cache_misses
Конец
```

### `transactional`

```python
def transactional(func):
    """
    A helper decorator that makes a function simulation-transactional.
    """
```

**Назначение**: Декоратор, делающий функцию транзакционной для симуляции.

**Параметры**:

*   `func`: Функция, которую необходимо сделать транзакционной.

**Возвращает**:

*   Обернутую функцию `wrapper`.

**Как работает функция**:

1.  Определяет внутреннюю функцию `wrapper`, которая будет вызываться вместо декорируемой функции.
2.  Внутри `wrapper`:
    *   Извлекает объект, над которым выполняется транзакция, из аргументов функции (`args[0]`).
    *   Получает текущую симуляцию с помощью `current_simulation()`.
    *   Создает объект `Transaction` с переданными аргументами.
    *   Вызывает метод `execute` объекта `Transaction` для выполнения транзакции.
    *   Возвращает результат выполнения транзакции.
3.  Возвращает функцию `wrapper`.

```
Начало
 |
Определение wrapper(*args, **kwargs)
 |
Получение obj_under_transaction из args[0]
 |
Получение simulation из current_simulation()
 |
Создание transaction = Transaction(obj_under_transaction, simulation, func, *args, **kwargs)
 |
Вызов result = transaction.execute()
 |
Возврат result
Конец