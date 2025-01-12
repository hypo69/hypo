# Модуль `control.py`

## Обзор

Модуль `control.py` предоставляет механизмы управления симуляцией, включая запуск, остановку, управление состояниями, кэширование и выполнение транзакций. Он содержит классы `Simulation` и `Transaction`, а также декоратор `transactional` для обеспечения управления транзакциями. Модуль также включает в себя вспомогательные функции для управления текущей симуляцией.

## Содержание

- [Классы](#Классы)
    - [Класс `Simulation`](#Класс-Simulation)
        - [Метод `__init__`](#Метод-__init__)
        - [Метод `begin`](#Метод-begin)
        - [Метод `end`](#Метод-end)
        - [Метод `checkpoint`](#Метод-checkpoint)
        - [Метод `add_agent`](#Метод-add_agent)
        - [Метод `add_environment`](#Метод-add_environment)
        - [Метод `add_factory`](#Метод-add_factory)
        - [Метод `_execution_trace_position`](#Метод-_execution_trace_position)
        - [Метод `_function_call_hash`](#Метод-_function_call_hash)
        - [Метод `_skip_execution_with_cache`](#Метод-_skip_execution_with_cache)
        - [Метод `_is_transaction_event_cached`](#Метод-_is_transaction_event_cached)
        - [Метод `_drop_cached_trace_suffix`](#Метод-_drop_cached_trace_suffix)
        - [Метод `_add_to_execution_trace`](#Метод-_add_to_execution_trace)
        - [Метод `_add_to_cache_trace`](#Метод-_add_to_cache_trace)
        - [Метод `_load_cache_file`](#Метод-_load_cache_file)
        - [Метод `_save_cache_file`](#Метод-_save_cache_file)
        - [Метод `begin_transaction`](#Метод-begin_transaction)
        - [Метод `end_transaction`](#Метод-end_transaction)
        - [Метод `is_under_transaction`](#Метод-is_under_transaction)
        - [Метод `_clear_communications_buffers`](#Метод-_clear_communications_buffers)
        - [Метод `_encode_simulation_state`](#Метод-_encode_simulation_state)
        - [Метод `_decode_simulation_state`](#Метод-_decode_simulation_state)
    - [Класс `Transaction`](#Класс-Transaction)
        - [Метод `__init__`](#Метод-__init__-1)
        - [Метод `execute`](#Метод-execute)
        - [Метод `_encode_function_output`](#Метод-_encode_function_output)
        - [Метод `_decode_function_output`](#Метод-_decode_function_output)
- [Функции](#Функции)
    - [Функция `transactional`](#Функция-transactional)
    - [Функция `reset`](#Функция-reset)
    - [Функция `_simulation`](#Функция-_simulation)
    - [Функция `begin`](#Функция-begin)
    - [Функция `end`](#Функция-end)
    - [Функция `checkpoint`](#Функция-checkpoint)
    - [Функция `current_simulation`](#Функция-current_simulation)
- [Исключения](#Исключения)
    - [Исключение `SkipTransaction`](#Исключение-SkipTransaction)
    - [Исключение `CacheOutOfSync`](#Исключение-CacheOutOfSync)
    - [Исключение `ExecutionCached`](#Исключение-ExecutionCached)

## Классы

### Класс `Simulation`

**Описание**: Класс `Simulation` управляет состоянием симуляции, включая агентов, окружения и фабрики. Он также отвечает за кэширование и восстановление состояний симуляции.

#### Метод `__init__`

```python
def __init__(self, id="default", cached_trace:list=None)
```

**Описание**: Инициализирует объект `Simulation`.

**Параметры**:

- `id` (str, optional): Идентификатор симуляции. По умолчанию `"default"`.
- `cached_trace` (list, optional): Список кэшированных состояний. По умолчанию `None`.

#### Метод `begin`

```python
def begin(self, cache_path:str=None, auto_checkpoint:bool=False)
```

**Описание**: Начинает симуляцию.

**Параметры**:

- `cache_path` (str, optional): Путь к файлу кэша. По умолчанию `None`.
- `auto_checkpoint` (bool, optional): Флаг автоматического сохранения состояния после каждой транзакции. По умолчанию `False`.

**Вызывает исключения**:

- `ValueError`: Если симуляция уже запущена.

#### Метод `end`

```python
def end(self)
```

**Описание**: Завершает симуляцию.

**Вызывает исключения**:

- `ValueError`: Если симуляция уже остановлена.

#### Метод `checkpoint`

```python
def checkpoint(self)
```

**Описание**: Сохраняет текущее состояние симуляции в файл кэша.

#### Метод `add_agent`

```python
def add_agent(self, agent)
```

**Описание**: Добавляет агента в симуляцию.

**Параметры**:

- `agent`: Агент, который нужно добавить.

**Вызывает исключения**:

- `ValueError`: Если агент с таким именем уже существует.

#### Метод `add_environment`

```python
def add_environment(self, environment)
```

**Описание**: Добавляет окружение в симуляцию.

**Параметры**:

- `environment`: Окружение, которое нужно добавить.

**Вызывает исключения**:

- `ValueError`: Если окружение с таким именем уже существует.

#### Метод `add_factory`

```python
def add_factory(self, factory)
```

**Описание**: Добавляет фабрику в симуляцию.

**Параметры**:

- `factory`: Фабрика, которую нужно добавить.

**Вызывает исключения**:

- `ValueError`: Если фабрика с таким именем уже существует.

#### Метод `_execution_trace_position`

```python
def _execution_trace_position(self) -> int
```

**Описание**: Возвращает текущую позицию в трассе исполнения.

**Возвращает**:
- `int`: Текущая позиция или -1, если трасса пуста.

#### Метод `_function_call_hash`

```python
def _function_call_hash(self, function_name, *args, **kwargs) -> int
```

**Описание**: Вычисляет хеш вызова функции.

**Параметры**:

- `function_name` (str): Имя функции.
- `*args`: Позиционные аргументы.
- `**kwargs`: Именованные аргументы.

**Возвращает**:
- `int`: Хеш вызова функции.

#### Метод `_skip_execution_with_cache`

```python
def _skip_execution_with_cache(self)
```

**Описание**: Пропускает выполнение текущего шага симуляции, используя кэшированное состояние.

**Вызывает исключения**:
- `AssertionError`: Если нет кэшированного состояния для текущей позиции.

#### Метод `_is_transaction_event_cached`

```python
def _is_transaction_event_cached(self, event_hash) -> bool
```

**Описание**: Проверяет, соответствует ли хеш события кэшированному значению.

**Параметры**:
- `event_hash` (str): Хеш события для проверки.

**Возвращает**:
- `bool`: True, если событие кэшировано или кэш отсутствует, иначе False.

**Вызывает исключения**:
- `ValueError`: Если позиция трассы исполнения недопустима.

#### Метод `_drop_cached_trace_suffix`

```python
def _drop_cached_trace_suffix(self)
```

**Описание**: Удаляет суффикс кэшированной трассы, начиная с текущей позиции исполнения.

#### Метод `_add_to_execution_trace`

```python
def _add_to_execution_trace(self, state: dict, event_hash: int, event_output)
```

**Описание**: Добавляет состояние в трассу исполнения.

**Параметры**:
- `state` (dict): Состояние симуляции.
- `event_hash` (int): Хеш события.
- `event_output`: Выход события.

#### Метод `_add_to_cache_trace`

```python
def _add_to_cache_trace(self, state: dict, event_hash: int, event_output)
```

**Описание**: Добавляет состояние в кэшированную трассу.

**Параметры**:
- `state` (dict): Состояние симуляции.
- `event_hash` (int): Хеш события.
- `event_output`: Выход события.

#### Метод `_load_cache_file`

```python
def _load_cache_file(self, cache_path:str)
```

**Описание**: Загружает кэш из файла.

**Параметры**:
- `cache_path` (str): Путь к файлу кэша.

#### Метод `_save_cache_file`

```python
def _save_cache_file(self, cache_path:str)
```

**Описание**: Сохраняет кэш в файл.

**Параметры**:
- `cache_path` (str): Путь к файлу кэша.

#### Метод `begin_transaction`

```python
def begin_transaction(self)
```

**Описание**: Начинает транзакцию.

#### Метод `end_transaction`

```python
def end_transaction(self)
```

**Описание**: Завершает транзакцию.

#### Метод `is_under_transaction`

```python
def is_under_transaction(self)
```

**Описание**: Проверяет, выполняется ли транзакция.

**Возвращает**:
- `bool`: `True`, если транзакция выполняется, иначе `False`.

#### Метод `_clear_communications_buffers`

```python
def _clear_communications_buffers(self)
```

**Описание**: Очищает буферы связи агентов и окружений.

#### Метод `_encode_simulation_state`

```python
def _encode_simulation_state(self) -> dict
```

**Описание**: Кодирует текущее состояние симуляции.

**Возвращает**:
- `dict`: Словарь, представляющий состояние симуляции.

#### Метод `_decode_simulation_state`

```python
def _decode_simulation_state(self, state: dict)
```

**Описание**: Декодирует состояние симуляции.

**Параметры**:
- `state` (dict): Словарь, представляющий состояние симуляции.

**Вызывает исключения**:

- `ValueError`: Если агент или окружение не найдены в симуляции.

### Класс `Transaction`

**Описание**: Класс `Transaction` управляет выполнением транзакций в симуляции. Он обеспечивает кэширование и восстановление состояний симуляции при выполнении функций.

#### Метод `__init__`

```python
def __init__(self, obj_under_transaction, simulation, function, *args, **kwargs)
```

**Описание**: Инициализирует объект `Transaction`.

**Параметры**:

- `obj_under_transaction`: Объект, над которым выполняется транзакция.
- `simulation`: Объект `Simulation`.
- `function`: Функция, которая будет выполнена в рамках транзакции.
- `*args`: Позиционные аргументы функции.
- `**kwargs`: Именованные аргументы функции.

**Вызывает исключения**:
- `ValueError`: Если объект уже принадлежит другой симуляции или если он не является агентом, окружением или фабрикой.

#### Метод `execute`

```python
def execute(self)
```

**Описание**: Выполняет транзакцию.

**Возвращает**:
- Результат выполнения функции в рамках транзакции.

**Вызывает исключения**:
- `ValueError`: Если статус симуляции недействителен.

#### Метод `_encode_function_output`

```python
def _encode_function_output(self, output) -> dict
```

**Описание**: Кодирует выход функции.

**Параметры**:

- `output`: Выход функции.

**Возвращает**:
- `dict`: Закодированный выход функции.

**Вызывает исключения**:
- `ValueError`: Если тип выхода не поддерживается.

#### Метод `_decode_function_output`

```python
def _decode_function_output(self, encoded_output: dict)
```

**Описание**: Декодирует закодированный выход функции.

**Параметры**:

- `encoded_output` (dict): Закодированный выход функции.

**Возвращает**:
- Декодированный выход функции.

**Вызывает исключения**:
- `ValueError`: Если тип закодированного выхода не поддерживается.

## Функции

### Функция `transactional`

```python
def transactional(func)
```

**Описание**: Декоратор, делающий функцию транзакционной.

**Параметры**:

- `func`: Функция, которую нужно сделать транзакционной.

**Возвращает**:
- Обертка над функцией, выполняющая ее в рамках транзакции.

### Функция `reset`

```python
def reset()
```

**Описание**: Сбрасывает состояние управления симуляцией.

### Функция `_simulation`

```python
def _simulation(id="default")
```

**Описание**: Возвращает объект `Simulation` по его идентификатору.

**Параметры**:
- `id` (str, optional): Идентификатор симуляции. По умолчанию `"default"`.

**Возвращает**:
- Объект `Simulation`.

### Функция `begin`

```python
def begin(cache_path=None, id="default", auto_checkpoint=False)
```

**Описание**: Начинает симуляцию.

**Параметры**:
- `cache_path` (str, optional): Путь к файлу кэша. По умолчанию `None`.
- `id` (str, optional): Идентификатор симуляции. По умолчанию `"default"`.
- `auto_checkpoint` (bool, optional): Флаг автоматического сохранения состояния после каждой транзакции. По умолчанию `False`.

**Вызывает исключения**:
- `ValueError`: Если симуляция уже запущена.

### Функция `end`

```python
def end(id="default")
```

**Описание**: Завершает симуляцию.

**Параметры**:
- `id` (str, optional): Идентификатор симуляции. По умолчанию `"default"`.

### Функция `checkpoint`

```python
def checkpoint(id="default")
```

**Описание**: Сохраняет текущее состояние симуляции.

**Параметры**:
- `id` (str, optional): Идентификатор симуляции. По умолчанию `"default"`.

### Функция `current_simulation`

```python
def current_simulation()
```

**Описание**: Возвращает текущую активную симуляцию.

**Возвращает**:
- Объект `Simulation` или `None`, если симуляция не запущена.

## Исключения

### Исключение `SkipTransaction`

**Описание**: Исключение, используемое для пропуска транзакции.

### Исключение `CacheOutOfSync`

**Описание**: Исключение, которое выбрасывается, когда кэш не синхронизирован с выполняемой симуляцией.

### Исключение `ExecutionCached`

**Описание**: Исключение, которое выбрасывается, когда предложенное выполнение уже закэшировано.