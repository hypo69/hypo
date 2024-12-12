# Модуль `control.py`

## Обзор

Модуль `control.py` содержит классы и функции для управления симуляциями, включая механизмы кэширования и отслеживания состояния. Он обеспечивает возможность запуска, остановки и сохранения состояния симуляции, а также управление транзакциями для объектов симуляции.

## Оглавление

- [Класс `Simulation`](#класс-simulation)
    - [Метод `__init__`](#__init__)
    - [Метод `begin`](#begin)
    - [Метод `end`](#end)
    - [Метод `checkpoint`](#checkpoint)
    - [Метод `add_agent`](#add_agent)
    - [Метод `add_environment`](#add_environment)
    - [Метод `add_factory`](#add_factory)
    - [Метод `_execution_trace_position`](#_execution_trace_position)
    - [Метод `_function_call_hash`](#_function_call_hash)
    - [Метод `_skip_execution_with_cache`](#_skip_execution_with_cache)
    - [Метод `_is_transaction_event_cached`](#_is_transaction_event_cached)
    - [Метод `_drop_cached_trace_suffix`](#_drop_cached_trace_suffix)
    - [Метод `_add_to_execution_trace`](#_add_to_execution_trace)
    - [Метод `_add_to_cache_trace`](#_add_to_cache_trace)
    - [Метод `_load_cache_file`](#_load_cache_file)
    - [Метод `_save_cache_file`](#_save_cache_file)
    - [Метод `begin_transaction`](#begin_transaction)
    - [Метод `end_transaction`](#end_transaction)
    - [Метод `is_under_transaction`](#is_under_transaction)
    - [Метод `_clear_communications_buffers`](#_clear_communications_buffers)
    - [Метод `_encode_simulation_state`](#_encode_simulation_state)
    - [Метод `_decode_simulation_state`](#_decode_simulation_state)
- [Класс `Transaction`](#класс-transaction)
    - [Метод `__init__`](#__init__-1)
    - [Метод `execute`](#execute)
    - [Метод `_encode_function_output`](#_encode_function_output)
    - [Метод `_decode_function_output`](#_decode_function_output)
- [Функция `transactional`](#функция-transactional)
- [Класс `SkipTransaction`](#класс-skiptransaction)
- [Класс `CacheOutOfSync`](#класс-cacheoutofsync)
- [Класс `ExecutionCached`](#класс-executioncached)
- [Функция `reset`](#функция-reset)
- [Функция `_simulation`](#функция-_simulation)
- [Функция `begin`](#функция-begin)
- [Функция `end`](#функция-end)
- [Функция `checkpoint`](#функция-checkpoint)
- [Функция `current_simulation`](#функция-current_simulation)

## Класс `Simulation`

**Описание**:
Класс `Simulation` управляет состоянием и выполнением симуляции, включая управление агентами, средами и фабриками. Он также реализует механизмы кэширования и отслеживания выполнения симуляции.

### `__init__`

```python
def __init__(self, id="default", cached_trace:list=None)
```

**Описание**:
Инициализирует новый экземпляр класса `Simulation`.

**Параметры**:
- `id` (str, optional): Идентификатор симуляции. По умолчанию `"default"`.
- `cached_trace` (list, optional): Начальный кэшированный след симуляции. По умолчанию `None`.

**Возвращает**:
- `None`

### `begin`

```python
def begin(self, cache_path:str=None, auto_checkpoint:bool=False)
```

**Описание**:
Отмечает начало управляемой симуляции.

**Параметры**:
- `cache_path` (str, optional): Путь к файлу кэша. Если не указан, используется путь по умолчанию, определенный в классе.
- `auto_checkpoint` (bool, optional): Флаг автоматического создания контрольной точки в конце каждой транзакции. По умолчанию `False`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если симуляция уже запущена.

### `end`

```python
def end(self)
```

**Описание**:
Отмечает конец управляемой симуляции.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если симуляция уже остановлена.

### `checkpoint`

```python
def checkpoint(self)
```

**Описание**:
Сохраняет текущий след симуляции в файл.

**Параметры**:
- `None`

**Возвращает**:
- `None`

### `add_agent`

```python
def add_agent(self, agent)
```

**Описание**:
Добавляет агента в симуляцию.

**Параметры**:
- `agent` (object): Объект агента, который нужно добавить.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если имя агента уже существует.

### `add_environment`

```python
def add_environment(self, environment)
```

**Описание**:
Добавляет среду в симуляцию.

**Параметры**:
- `environment` (object): Объект среды, который нужно добавить.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если имя среды уже существует.

### `add_factory`

```python
def add_factory(self, factory)
```

**Описание**:
Добавляет фабрику в симуляцию.

**Параметры**:
- `factory` (object): Объект фабрики, который нужно добавить.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если имя фабрики уже существует.

### `_execution_trace_position`

```python
def _execution_trace_position(self) -> int
```

**Описание**:
Возвращает текущую позицию в следе выполнения или -1, если след выполнения пуст.

**Параметры**:
- `None`

**Возвращает**:
- `int`: Текущая позиция в следе выполнения или -1.

### `_function_call_hash`

```python
def _function_call_hash(self, function_name, *args, **kwargs) -> int
```

**Описание**:
Вычисляет хэш заданного вызова функции.

**Параметры**:
- `function_name` (str): Имя функции.
- `*args` (tuple): Позиционные аргументы функции.
- `**kwargs` (dict): Именованные аргументы функции.

**Возвращает**:
- `int`: Хэш вызова функции.

### `_skip_execution_with_cache`

```python
def _skip_execution_with_cache(self)
```

**Описание**:
Пропускает текущее выполнение, предполагая, что в той же позиции есть кэшированное состояние.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если нет кэшированного состояния в текущей позиции выполнения.

### `_is_transaction_event_cached`

```python
def _is_transaction_event_cached(self, event_hash) -> bool
```

**Описание**:
Проверяет, соответствует ли заданный хэш события соответствующему кэшированному хэшу. Если нет соответствующего кэшированного состояния, возвращает `True`.

**Параметры**:
- `event_hash` (int): Хэш события для проверки.

**Возвращает**:
- `bool`: `True`, если событие кэшировано или нет кэша для использования, в противном случае `False`.

**Вызывает исключения**:
- `ValueError`: Если позиция в следе выполнения недействительна.

### `_drop_cached_trace_suffix`

```python
def _drop_cached_trace_suffix(self)
```

**Описание**:
Удаляет суффикс кэшированного следа, начиная с текущей позиции в следе выполнения.

**Параметры**:
- `None`

**Возвращает**:
- `None`

### `_add_to_execution_trace`

```python
def _add_to_execution_trace(self, state: dict, event_hash: int, event_output)
```

**Описание**:
Добавляет состояние в список `execution_trace` и вычисляет соответствующий хэш.

**Параметры**:
- `state` (dict): Текущее состояние симуляции.
- `event_hash` (int): Хэш события, которое привело к этому состоянию.
- `event_output` (any): Выходные данные события, если они есть.

**Возвращает**:
- `None`

### `_add_to_cache_trace`

```python
def _add_to_cache_trace(self, state: dict, event_hash: int, event_output)
```

**Описание**:
Добавляет состояние в список `cached_trace` и вычисляет соответствующий хэш.

**Параметры**:
- `state` (dict): Текущее состояние симуляции.
- `event_hash` (int): Хэш события, которое привело к этому состоянию.
- `event_output` (any): Выходные данные события, если они есть.

**Возвращает**:
- `None`

### `_load_cache_file`

```python
def _load_cache_file(self, cache_path:str)
```

**Описание**:
Загружает файл кэша из заданного пути.

**Параметры**:
- `cache_path` (str): Путь к файлу кэша.

**Возвращает**:
- `None`

### `_save_cache_file`

```python
def _save_cache_file(self, cache_path:str)
```

**Описание**:
Сохраняет файл кэша в заданный путь. Всегда перезаписывает.

**Параметры**:
- `cache_path` (str): Путь к файлу кэша.

**Возвращает**:
- `None`

### `begin_transaction`

```python
def begin_transaction(self)
```

**Описание**:
Начинает транзакцию.

**Параметры**:
- `None`

**Возвращает**:
- `None`

### `end_transaction`

```python
def end_transaction(self)
```

**Описание**:
Завершает транзакцию.

**Параметры**:
- `None`

**Возвращает**:
- `None`

### `is_under_transaction`

```python
def is_under_transaction(self)
```

**Описание**:
Проверяет, находится ли агент в транзакции.

**Параметры**:
- `None`

**Возвращает**:
- `bool`: `True`, если агент находится в транзакции, иначе `False`.

### `_clear_communications_buffers`

```python
def _clear_communications_buffers(self)
```

**Описание**:
Очищает буферы связи всех агентов и сред.

**Параметры**:
- `None`

**Возвращает**:
- `None`

### `_encode_simulation_state`

```python
def _encode_simulation_state(self) -> dict
```

**Описание**:
Кодирует текущее состояние симуляции, включая агентов, среды и другую релевантную информацию.

**Параметры**:
- `None`

**Возвращает**:
- `dict`: Словарь, представляющий закодированное состояние симуляции.

### `_decode_simulation_state`

```python
def _decode_simulation_state(self, state: dict)
```

**Описание**:
Декодирует заданное состояние симуляции, включая агентов, среды и другую релевантную информацию.

**Параметры**:
- `state` (dict): Состояние для декодирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если среда или агент не найдены в симуляции.

## Класс `Transaction`

**Описание**:
Класс `Transaction` управляет выполнением транзакций в симуляции, включая кэширование и отслеживание изменений состояния.

### `__init__`

```python
def __init__(self, obj_under_transaction, simulation, function, *args, **kwargs)
```

**Описание**:
Инициализирует новый экземпляр класса `Transaction`.

**Параметры**:
- `obj_under_transaction` (object): Объект, над которым выполняется транзакция.
- `simulation` (Simulation): Экземпляр симуляции.
- `function` (function): Функция, которая должна быть выполнена в рамках транзакции.
- `*args` (tuple): Позиционные аргументы функции.
- `**kwargs` (dict): Именованные аргументы функции.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если объект уже захвачен другой симуляцией или не является TinyPerson, TinyWorld или TinyFactory.

### `execute`

```python
def execute(self)
```

**Описание**:
Выполняет транзакцию.

**Параметры**:
- `None`

**Возвращает**:
- `any`: Результат выполнения функции.

**Вызывает исключения**:
- `ValueError`: Если статус симуляции недействителен.

### `_encode_function_output`

```python
def _encode_function_output(self, output) -> dict
```

**Описание**:
Кодирует выходные данные функции.

**Параметры**:
- `output` (any): Выходные данные для кодирования.

**Возвращает**:
- `dict`: Закодированные выходные данные.

**Вызывает исключения**:
- `ValueError`: Если тип выходных данных не поддерживается.

### `_decode_function_output`

```python
def _decode_function_output(self, encoded_output: dict)
```

**Описание**:
Декодирует заданные закодированные выходные данные функции.

**Параметры**:
- `encoded_output` (dict): Закодированные выходные данные.

**Возвращает**:
- `any`: Декодированные выходные данные.

**Вызывает исключения**:
- `ValueError`: Если тип закодированных выходных данных не поддерживается.

## Функция `transactional`

```python
def transactional(func)
```

**Описание**:
Декоратор, который делает функцию транзакционной для симуляции.

**Параметры**:
- `func` (function): Функция, которую нужно сделать транзакционной.

**Возвращает**:
- `function`: Обернутая функция.

## Класс `SkipTransaction`

**Описание**:
Исключение, которое можно вызвать для пропуска транзакции.

## Класс `CacheOutOfSync`

**Описание**:
Исключение, которое возникает, когда кэшированный и свежевыполненный элементы рассинхронизированы.

## Класс `ExecutionCached`

**Описание**:
Исключение, которое возникает, когда предложенное выполнение уже кэшировано.

## Функция `reset`

```python
def reset()
```

**Описание**:
Сбрасывает все состояние управления симуляцией.

**Параметры**:
- `None`

**Возвращает**:
- `None`

## Функция `_simulation`

```python
def _simulation(id="default")
```

**Описание**:
Возвращает экземпляр симуляции с заданным идентификатором или создает новый, если он еще не существует.

**Параметры**:
- `id` (str, optional): Идентификатор симуляции. По умолчанию `"default"`.

**Возвращает**:
- `Simulation`: Экземпляр симуляции.

## Функция `begin`

```python
def begin(cache_path=None, id="default", auto_checkpoint=False)
```

**Описание**:
Отмечает начало управляемой симуляции.

**Параметры**:
- `cache_path` (str, optional): Путь к файлу кэша.
- `id` (str, optional): Идентификатор симуляции. По умолчанию `"default"`.
- `auto_checkpoint` (bool, optional): Флаг автоматического создания контрольной точки. По умолчанию `False`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если симуляция уже запущена.

## Функция `end`

```python
def end(id="default")
```

**Описание**:
Отмечает конец управляемой симуляции.

**Параметры**:
- `id` (str, optional): Идентификатор симуляции. По умолчанию `"default"`.

**Возвращает**:
- `None`

## Функция `checkpoint`

```python
def checkpoint(id="default")
```

**Описание**:
Сохраняет текущее состояние симуляции.

**Параметры**:
- `id` (str, optional): Идентификатор симуляции. По умолчанию `"default"`.

**Возвращает**:
- `None`

## Функция `current_simulation`

```python
def current_simulation()
```

**Описание**:
Возвращает текущую активную симуляцию.

**Параметры**:
- `None`

**Возвращает**:
- `Simulation | None`: Текущая активная симуляция или `None`, если нет активной симуляции.