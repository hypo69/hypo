# Модуль memory.py

## Обзор

Модуль предоставляет классы для реализации различных типов памяти агента в системе `tinytroupe`. Включает базовый класс `TinyMemory` и его подклассы `EpisodicMemory` и `SemanticMemory`, предназначенные для хранения и извлечения информации, связанной с эпизодическими событиями и семантическими знаниями, соответственно.

## Подробней

Этот модуль является ключевым компонентом в архитектуре агента, позволяя ему сохранять и использовать прошлый опыт и знания для принятия решений и взаимодействия с окружением. `TinyMemory` предоставляет интерфейс для хранения и извлечения данных, в то время как `EpisodicMemory` и `SemanticMemory` реализуют конкретные стратегии управления памятью.

## Классы

### `TinyMemory`

**Описание**: Базовый класс для различных типов памяти.

**Принцип работы**:
`TinyMemory` служит абстрактным базовым классом для реализации различных типов памяти агента. Он определяет интерфейс для хранения и извлечения данных, но не предоставляет конкретной реализации этих методов.

**Методы**:

- `_preprocess_value_for_storage(self, value: Any) -> Any`: Предобрабатывает значение перед сохранением в памяти. По умолчанию не выполняет никаких преобразований.
- `_store(self, value: Any) -> None`: Абстрактный метод для хранения значения в памяти. Должен быть реализован в подклассах.
- `store(self, value: dict) -> None`: Сохраняет значение в памяти, предварительно обработав его.
- `store_all(self, values: list) -> None`: Сохраняет список значений в памяти.
- `retrieve(self, first_n: int, last_n: int, include_omission_info:bool=True) -> list`: Абстрактный метод для извлечения значений из памяти. Должен быть реализован в подклассах.
- `retrieve_recent(self) -> list`: Абстрактный метод для извлечения последних значений из памяти. Должен быть реализован в подклассах.
- `retrieve_all(self) -> list`: Абстрактный метод для извлечения всех значений из памяти. Должен быть реализован в подклассах.
- `retrieve_relevant(self, relevance_target:str, top_k=20) -> list`: Абстрактный метод для извлечения значений, релевантных заданной цели. Должен быть реализован в подклассах.

### `EpisodicMemory`

**Описание**: Предоставляет возможности эпизодической памяти для агента.

**Наследует**:
- `TinyMemory`: `EpisodicMemory` расширяет базовый класс `TinyMemory`, добавляя функциональность, специфичную для эпизодической памяти.

**Принцип работы**:
`EpisodicMemory` позволяет агенту запоминать конкретные события или эпизоды из прошлого. Она хранит сообщения в списке `self.memory` и предоставляет методы для извлечения этих сообщений на основе различных критериев, таких как порядок, количество и временной контекст.

**Аттрибуты**:
- `MEMORY_BLOCK_OMISSION_INFO (dict)`: Сообщение, используемое для обозначения опущенных блоков памяти.
- `fixed_prefix_length (int)`: Длина фиксированного префикса памяти.
- `lookback_length (int)`: Длина ретроспективного обзора памяти.
- `memory (list)`: Список для хранения эпизодических воспоминаний.

**Методы**:

- `__init__(self, fixed_prefix_length: int = 100, lookback_length: int = 100) -> None`: Инициализирует память с заданной длиной фиксированного префикса и ретроспективного обзора.
- `_store(self, value: Any) -> None`: Сохраняет значение в памяти, добавляя его в список `self.memory`.
- `count(self) -> int`: Возвращает количество значений в памяти.
- `retrieve(self, first_n: int, last_n: int, include_omission_info:bool=True) -> list`: Извлекает первые `first_n` и/или последние `last_n` значения из памяти.
- `retrieve_recent(self, include_omission_info:bool=True) -> list`: Извлекает `n` самых последних значений из памяти.
- `retrieve_all(self) -> list`: Извлекает все значения из памяти.
- `retrieve_relevant(self, relevance_target: str, top_k:int) -> list`: Вызывает исключение `NotImplementedError`, так как метод не реализован.
- `retrieve_first(self, n: int, include_omission_info:bool=True) -> list`: Извлекает первые `n` значений из памяти.
- `retrieve_last(self, n: int, include_omission_info:bool=True) -> list`: Извлекает последние `n` значений из памяти.

### `SemanticMemory`

**Описание**: Предоставляет возможности семантической памяти для агента.

**Наследует**:
- `TinyMemory`: `SemanticMemory` расширяет базовый класс `TinyMemory`, добавляя функциональность, специфичную для семантической памяти.

**Принцип работы**:
`SemanticMemory` позволяет агенту хранить и извлекать семантические знания, не связанные с конкретными событиями или эпизодами. Она использует `BaseSemanticGroundingConnector` для индексации и поиска семантической информации.

**Аттрибуты**:

- `serializable_attrs (list)`: Список атрибутов, которые необходимо сериализовать.
- `memories (list)`: Список для хранения семантических воспоминаний.
- `semantic_grounding_connector (BaseSemanticGroundingConnector)`: Коннектор для семантического обоснования.

**Методы**:

- `__init__(self, memories: list=None) -> None`: Инициализирует память с заданным списком воспоминаний.
- `_post_init(self)`: Выполняется после `__init__` и инициализирует `semantic_grounding_connector`.
- `_preprocess_value_for_storage(self, value: dict) -> Any`: Предобрабатывает значение перед сохранением в памяти, форматируя его в виде текста.
- `_store(self, value: Any) -> None`: Сохраняет значение в памяти, добавляя его в `semantic_grounding_connector`.
- `retrieve_relevant(self, relevance_target:str, top_k=20) -> list`: Извлекает значения из памяти, релевантные заданной цели, используя `semantic_grounding_connector`.
- `_build_document_from(memory) -> Document`: Создает документ из воспоминания.
- `_build_documents_from(self, memories: list) -> list`: Создает список документов из списка воспоминаний.

## Функции

### `_preprocess_value_for_storage`
```python
 def _preprocess_value_for_storage(self, value: Any) -> Any:
    """
    Preprocesses a value before storing it in memory.
    """
    # by default, we don\'t preprocess the value
    return value
```

**Назначение**: Предобрабатывает значение перед сохранением в памяти.

**Параметры**:
- `value` (Any): Значение для предобработки.

**Возвращает**:
- `Any`: Предобработанное значение.

**Как работает функция**:

1.  Функция `_preprocess_value_for_storage` принимает значение `value` любого типа.
2.  По умолчанию, функция не выполняет никаких преобразований над входным значением.
3.  Возвращает входное значение `value` без изменений.

```
Предобработка_значения
│
└───> Возврат_значения (без изменений)
```

**Примеры**:

```python
memory = TinyMemory()
value = "some value"
preprocessed_value = memory._preprocess_value_for_storage(value)
print(preprocessed_value)  # Вывод: some value
```

### `_store`
```python
def _store(self, value: Any) -> None:
    """
    Stores a value in memory.
    """
    raise NotImplementedError("Subclasses must implement this method.")
```

**Назначение**: Сохраняет значение в памяти.

**Параметры**:
- `value` (Any): Значение для сохранения.

**Вызывает исключения**:
- `NotImplementedError`: Всегда вызывается, так как метод должен быть реализован в подклассах.

**Как работает функция**:

1.  Функция `_store` принимает значение `value` любого типа.
2.  Функция всегда вызывает исключение `NotImplementedError`, указывая на то, что этот метод должен быть реализован в подклассах, чтобы обеспечить конкретную логику хранения данных.

```
Сохранение_значения
│
└───> Выброс_исключения (NotImplementedError)
```

### `store`
```python
def store(self, value: dict) -> None:
    """
    Stores a value in memory.
    """
    self._store(self._preprocess_value_for_storage(value))
```

**Назначение**: Сохраняет значение в памяти.

**Параметры**:
- `value` (dict): Значение для сохранения.

**Как работает функция**:

1.  Функция `store` принимает значение `value` типа `dict`.
2.  Функция вызывает метод `_preprocess_value_for_storage` для предобработки значения.
3.  Затем функция вызывает метод `_store` для сохранения предобработанного значения в памяти.

```
Сохранение_значения
│
├───> Предобработка_значения (value)
│
└───> Сохранение_предобработанного_значения (_store)
```

**Примеры**:

```python
class MyMemory(TinyMemory):
    def __init__(self):
        self.memory = []

    def _store(self, value: Any) -> None:
        self.memory.append(value)

memory = MyMemory()
value = {"key": "value"}
memory.store(value)
print(memory.memory)  # Вывод: [{'key': 'value'}]
```

### `store_all`
```python
def store_all(self, values: list) -> None:
    """
    Stores a list of values in memory.
    """
    for value in values:
        self.store(value)
```

**Назначение**: Сохраняет список значений в памяти.

**Параметры**:
- `values` (list): Список значений для сохранения.

**Как работает функция**:

1.  Функция `store_all` принимает список значений `values`.
2.  Для каждого значения в списке `values` функция вызывает метод `store` для сохранения значения в памяти.

```
Сохранение_списка_значений
│
└───> Для_каждого_значения_в_списке
│    │
│    └───> Сохранение_значения (store)
```

**Примеры**:

```python
class MyMemory(TinyMemory):
    def __init__(self):
        self.memory = []

    def _store(self, value: Any) -> None:
        self.memory.append(value)

memory = MyMemory()
values = [{"key1": "value1"}, {"key2": "value2"}]
memory.store_all(values)
print(memory.memory)  # Вывод: [{'key1': 'value1'}, {'key2': 'value2'}]
```

### `retrieve`
```python
def retrieve(self, first_n: int, last_n: int, include_omission_info:bool=True) -> list:
    """
    Retrieves the first n and/or last n values from memory. If n is None, all values are retrieved.

    Args:
        first_n (int): The number of first values to retrieve.
        last_n (int): The number of last values to retrieve.
        include_omission_info (bool): Whether to include an information message when some values are omitted.

    Returns:
        list: The retrieved values.
    
    """
    raise NotImplementedError("Subclasses must implement this method.")
```

**Назначение**: Извлекает первые n и/или последние n значений из памяти. Если n равен None, извлекаются все значения.

**Параметры**:
- `first_n` (int): Количество первых значений для извлечения.
- `last_n` (int): Количество последних значений для извлечения.
- `include_omission_info` (bool): Следует ли включать информационное сообщение, когда некоторые значения опущены. По умолчанию `True`.

**Возвращает**:
- `list`: Извлеченные значения.

**Вызывает исключения**:
- `NotImplementedError`: Всегда вызывается, так как метод должен быть реализован в подклассах.

**Как работает функция**:

1.  Функция `retrieve` принимает количество первых `first_n` и последних `last_n` значений для извлечения, а также флаг `include_omission_info`, указывающий, следует ли включать информационное сообщение об опущенных значениях.
2.  Функция всегда вызывает исключение `NotImplementedError`, указывая на то, что этот метод должен быть реализован в подклассах, чтобы обеспечить конкретную логику извлечения данных.

```
Извлечение_значений
│
└───> Выброс_исключения (NotImplementedError)
```

### `retrieve_recent`
```python
def retrieve_recent(self) -> list:
    """
    Retrieves the n most recent values from memory.
    """
    raise NotImplementedError("Subclasses must implement this method.")
```

**Назначение**: Извлекает n самых последних значений из памяти.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `list`: Извлеченные значения.

**Вызывает исключения**:
- `NotImplementedError`: Всегда вызывается, так как метод должен быть реализован в подклассах.

**Как работает функция**:

1.  Функция `retrieve_recent` не принимает параметров.
2.  Функция всегда вызывает исключение `NotImplementedError`, указывая на то, что этот метод должен быть реализован в подклассах, чтобы обеспечить конкретную логику извлечения данных.

```
Извлечение_последних_значений
│
└───> Выброс_исключения (NotImplementedError)
```

### `retrieve_all`
```python
def retrieve_all(self) -> list:
    """
    Retrieves all values from memory.
    """
    raise NotImplementedError("Subclasses must implement this method.")
```

**Назначение**: Извлекает все значения из памяти.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `list`: Извлеченные значения.

**Вызывает исключения**:
- `NotImplementedError`: Всегда вызывается, так как метод должен быть реализован в подклассах.

**Как работает функция**:

1.  Функция `retrieve_all` не принимает параметров.
2.  Функция всегда вызывает исключение `NotImplementedError`, указывая на то, что этот метод должен быть реализован в подклассах, чтобы обеспечить конкретную логику извлечения данных.

```
Извлечение_всех_значений
│
└───> Выброс_исключения (NotImplementedError)
```

### `retrieve_relevant`
```python
def retrieve_relevant(self, relevance_target:str, top_k=20) -> list:
    """
    Retrieves all values from memory that are relevant to a given target.
    """
    raise NotImplementedError("Subclasses must implement this method.")
```

**Назначение**: Извлекает все значения из памяти, релевантные заданной цели.

**Параметры**:
- `relevance_target` (str): Цель, для которой извлекаются релевантные значения.
- `top_k` (int): Максимальное количество извлекаемых значений. По умолчанию 20.

**Возвращает**:
- `list`: Извлеченные значения.

**Вызывает исключения**:
- `NotImplementedError`: Всегда вызывается, так как метод должен быть реализован в подклассах.

**Как работает функция**:

1.  Функция `retrieve_relevant` принимает цель `relevance_target` и максимальное количество извлекаемых значений `top_k`.
2.  Функция всегда вызывает исключение `NotImplementedError`, указывая на то, что этот метод должен быть реализован в подклассах, чтобы обеспечить конкретную логику извлечения данных.

```
Извлечение_релевантных_значений
│
└───> Выброс_исключения (NotImplementedError)
```

### `_store` (EpisodicMemory)
```python
def _store(self, value: Any) -> None:
    """
    Stores a value in memory.
    """
    self.memory.append(value)
```

**Назначение**: Сохраняет значение в памяти, добавляя его в список `self.memory`.

**Параметры**:
- `value` (Any): Значение для сохранения.

**Как работает функция**:

1.  Функция `_store` принимает значение `value` любого типа.
2.  Функция добавляет значение `value` в конец списка `self.memory`.

```
Сохранение_значения
│
└───> Добавление_значения_в_список (self.memory)
```

**Примеры**:

```python
memory = EpisodicMemory()
value = "some value"
memory._store(value)
print(memory.memory)  # Вывод: ['some value']
```

### `count`
```python
def count(self) -> int:
    """
    Returns the number of values in memory.
    """
    return len(self.memory)
```

**Назначение**: Возвращает количество значений в памяти.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `int`: Количество значений в списке `self.memory`.

**Как работает функция**:

1.  Функция `count` не принимает параметров.
2.  Функция возвращает длину списка `self.memory`, что соответствует количеству значений, хранящихся в памяти.

```
Подсчет_значений
│
└───> Возврат_длины_списка (self.memory)
```

**Примеры**:

```python
memory = EpisodicMemory()
memory._store("value1")
memory._store("value2")
print(memory.count())  # Вывод: 2
```

### `retrieve` (EpisodicMemory)
```python
def retrieve(self, first_n: int, last_n: int, include_omission_info:bool=True) -> list:
    """
    Retrieves the first n and/or last n values from memory. If n is None, all values are retrieved.

    Args:
        first_n (int): The number of first values to retrieve.
        last_n (int): The number of last values to retrieve.
        include_omission_info (bool): Whether to include an information message when some values are omitted.

    Returns:
        list: The retrieved values.
    
    """

    omisssion_info = [EpisodicMemory.MEMORY_BLOCK_OMISSION_INFO] if include_omission_info else []

    # use the other methods in the class to implement
    if first_n is not None and last_n is not None:
        return self.retrieve_first(first_n) + omisssion_info + self.retrieve_last(last_n)
    elif first_n is not None:
        return self.retrieve_first(first_n)
    elif last_n is not None:
        return self.retrieve_last(last_n)
    else:
        return self.retrieve_all()
```

**Назначение**: Извлекает первые `first_n` и/или последние `last_n` значения из памяти. Если `n` равен `None`, извлекаются все значения.

**Параметры**:
- `first_n` (int): Количество первых значений для извлечения.
- `last_n` (int): Количество последних значений для извлечения.
- `include_omission_info` (bool): Следует ли включать информационное сообщение, когда некоторые значения опущены. По умолчанию `True`.

**Возвращает**:
- `list`: Извлеченные значения.

**Как работает функция**:

1.  Функция `retrieve` принимает количество первых `first_n` и последних `last_n` значений для извлечения, а также флаг `include_omission_info`, указывающий, следует ли включать информационное сообщение об опущенных значениях.
2.  Функция определяет, какие значения следует извлечь, на основе значений `first_n` и `last_n`.
    - Если оба параметра не равны `None`, функция извлекает первые `first_n` значения, добавляет информационное сообщение (если `include_omission_info` равен `True`), и извлекает последние `last_n` значения.
    - Если только `first_n` не равен `None`, функция извлекает первые `first_n` значения.
    - Если только `last_n` не равен `None`, функция извлекает последние `last_n` значения.
    - Если оба параметра равны `None`, функция извлекает все значения.
3.  Функция возвращает список извлеченных значений.

```
Извлечение_значений
│
├───> Определение_необходимости_включения_информации_об_опущениях
│
├───> Проверка_условий
│    ├───> Если_first_n_и_last_n_не_None
│    │    └───> Извлечение_первых_значений + Информация_об_опущениях + Извлечение_последних_значений
│    ├───> Иначе_если_first_n_не_None
│    │    └───> Извлечение_первых_значений
│    ├───> Иначе_если_last_n_не_None
│    │    └───> Извлечение_последних_значений
│    └───> Иначе
│         └───> Извлечение_всех_значений
│
└───> Возврат_извлеченных_значений
```

**Примеры**:

```python
memory = EpisodicMemory()
memory._store("value1")
memory._store("value2")
memory._store("value3")
print(memory.retrieve(first_n=1, last_n=1))  # Вывод: ['value1', {'role': 'assistant', 'content': 'Info: there were other messages here, but they were omitted for brevity.', 'simulation_timestamp': None}, 'value3']
print(memory.retrieve(first_n=1, last_n=1, include_omission_info=False)) # Вывод: ['value1', 'value3']
print(memory.retrieve(first_n=1, last_n=None)) # Вывод: ['value1']
```

### `retrieve_recent` (EpisodicMemory)
```python
def retrieve_recent(self, include_omission_info:bool=True) -> list:
    """
    Retrieves the n most recent values from memory.
    """
    omisssion_info = [EpisodicMemory.MEMORY_BLOCK_OMISSION_INFO] if include_omission_info else []

    # compute fixed prefix
    fixed_prefix = self.memory[: self.fixed_prefix_length] + omisssion_info

    # how many lookback values remain?
    remaining_lookback = min(
        len(self.memory) - len(fixed_prefix), self.lookback_length
    )

    # compute the remaining lookback values and return the concatenation
    if remaining_lookback <= 0:
        return fixed_prefix
    else:
        return fixed_prefix + self.memory[-remaining_lookback:]
```

**Назначение**: Извлекает n самых последних значений из памяти.

**Параметры**:
- `include_omission_info` (bool): Определяет, включать ли информацию об опущенных значениях. По умолчанию `True`.

**Возвращает**:
- `list`: Список извлеченных значений.

**Как работает функция**:

1.  Функция `retrieve_recent` принимает флаг `include_omission_info`, указывающий, следует ли включать информационное сообщение об опущенных значениях.
2.  Вычисляет фиксированный префикс, беря первые `fixed_prefix_length` значений из памяти и добавляя информационное сообщение (если `include_omission_info` равен `True`).
3.  Вычисляет количество оставшихся значений для ретроспективного обзора, определяя минимум между разницей длины памяти и длины фиксированного префикса и длиной ретроспективного обзора.
4.  Если количество оставшихся значений для ретроспективного обзора меньше или равно 0, возвращает фиксированный префикс.
5.  Иначе возвращает конкатенацию фиксированного префикса и последних `remaining_lookback` значений из памяти.

```
Извлечение_последних_значений
│
├───> Определение_необходимости_включения_информации_об_опущениях
│
├───> Вычисление_фиксированного_префикса
│
├───> Вычисление_количества_оставшихся_значений_для_ретроспективного_обзора
│
├───> Проверка_условия
│    ├───> Если_количество_оставшихся_значений_<=_0
│    │    └───> Возврат_фиксированного_префикса
│    └───> Иначе
│         └───> Возврат_фиксированного_префикса + последних_значений_из_памяти
```

**Примеры**:

```python
memory = EpisodicMemory(fixed_prefix_length=1, lookback_length=1)
memory._store("value1")
memory._store("value2")
memory._store("value3")
print(memory.retrieve_recent())
#  ['value1', [{'role': 'assistant', 'content': 'Info: there were other messages here, but they were omitted for brevity.', 'simulation_timestamp': None}], 'value3']
```

### `retrieve_all` (EpisodicMemory)
```python
def retrieve_all(self) -> list:
    """
    Retrieves all values from memory.
    """
    return copy.copy(self.memory)
```

**Назначение**: Извлекает все значения из памяти.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `list`: Копия списка `self.memory`.

**Как работает функция**:

1.  Функция `retrieve_all` не принимает параметров.
2.  Функция возвращает копию списка `self.memory`, содержащего все значения, хранящиеся в памяти.

```
Извлечение_всех_значений
│
└───> Возврат_копии_списка (self.memory)
```

**Примеры**:

```python
memory = EpisodicMemory()
memory._store("value1")
memory._store("value2")
print(memory.retrieve_all())  # Вывод: ['value1', 'value2']
```

### `retrieve_relevant` (EpisodicMemory)
```python
def retrieve_relevant(self, relevance_target: str, top_k:int) -> list:
    """
    Retrieves top-k values from memory that are most relevant to a given target.
    """
    raise NotImplementedError("Subclasses must implement this method.")
```

**Назначение**: Извлекает top-k значений из памяти, наиболее релевантных заданной цели.

**Параметры**:
- `relevance_target` (str): Цель, для которой извлекаются релевантные значения.
- `top_k` (int): Количество наиболее релевантных значений для извлечения.

**Возвращает**:
- `list`: Список извлеченных значений.

**Вызывает исключения**:
- `NotImplementedError`: Всегда вызывается, так как метод не реализован.

**Как работает функция**:

1.  Функция `retrieve_relevant` принимает цель `relevance_target` и количество наиболее релевантных значений для извлечения `top_k`.
2.  Функция всегда вызывает исключение `NotImplementedError`, указывая на то, что этот метод должен быть реализован в подклассах, чтобы обеспечить конкретную логику извлечения данных.

```
Извлечение_релевантных_значений
│
└───> Выброс_исключения (NotImplementedError)
```

### `retrieve_first`
```python
def retrieve_first(self, n: int, include_omission_info:bool=True) -> list:
    """
    Retrieves the first n values from memory.
    """
    omisssion_info = [EpisodicMemory.MEMORY_BLOCK_OMISSION_INFO] if include_omission_info else []
    
    return self.memory[:n] + omisssion_info
```

**Назначение**: Извлекает первые n значений из памяти.

**Параметры**:
- `n` (int): Количество первых значений для извлечения.
- `include_omission_info` (bool): Определяет, включать ли информацию об опущенных значениях. По умолчанию `True`.

**Возвращает**:
- `list`: Список извлеченных значений.

**Как работает функция**:

1.  Функция `retrieve_first` принимает количество первых значений для извлечения `n` и флаг `include_omission_info`, указывающий, следует ли включать информационное сообщение об опущенных значениях.
2.  Извлекает первые `n` значений из списка `self.memory`.
3.  Добавляет информационное сообщение об опущенных значениях, если `include_omission_info` равен `True`.
4.  Возвращает список извлеченных значений.

```
Извлечение_первых_значений
│
├───> Определение_необходимости_включения_информации_об_опущениях
│
└───> Возврат_первых_значений_из_памяти + Информация_об_опущениях
```

**Примеры**:

```python
memory = EpisodicMemory()
memory._store("value1")
memory._store("value2")
memory._store("value3")
print(memory.retrieve_first(n=2)) # Вывод: ['value1', 'value2', {'role': 'assistant', 'content': 'Info: there were other messages here, but they were omitted for brevity.', 'simulation_timestamp': None}]
```

### `retrieve_last`
```python
def retrieve_last(self, n: int, include_omission_info:bool=True) -> list:
    """
    Retrieves the last n values from memory.
    """
    omisssion_info = [EpisodicMemory.MEMORY_BLOCK_OMISSION_INFO] if include_omission_info else []

    return omisssion_info + self.memory[-n:]
```

**Назначение**: Извлекает последние n значений из памяти.

**Параметры**:
- `n` (int): Количество последних значений для извлечения.
- `include_omission_info` (bool): Определяет, включать ли информацию об опущенных значениях. По умолчанию `True`.

**Возвращает**:
- `list`: Список извлеченных значений.

**Как работает функция**:

1.  Функция `retrieve_last` принимает количество последних значений для извлечения `n` и флаг `include_omission_info`, указывающий, следует ли включать информационное сообщение об опущенных значениях.
2.  Добавляет информационное сообщение об опущенных значениях, если `include_omission_info` равен `True`.
3.  Извлекает последние `n` значений из списка `self.memory`.
4.  Возвращает список извлеченных значений.

```
Извлечение_последних_значений
│
├───> Определение_необходимости_включения_информации_об_опущениях
│
└───> Возврат_информации_об_опущениях + последних_значений_из_памяти
```

**Примеры**:

```python
memory = EpisodicMemory()
memory._store("value1")
memory._store("value2")
memory._store("value3")
print(memory.retrieve_last(n=2))
# Вывод:
#[{'role': 'assistant', 'content': 'Info: there were other messages here, but they were omitted for brevity.', 'simulation_timestamp': None}, 'value2', 'value3']
```

### `_post_init`

```python
def _post_init(self): 
    """
    This will run after __init__, since the class has the @post_init decorator.
    It is convenient to separate some of the initialization processes to make deserialize easier.
    """

    if not hasattr(self, 'memories') or self.memories is None:
        self.memories = []

    self.semantic_grounding_connector = BaseSemanticGroundingConnector("Semantic Memory Storage")
    self.semantic_grounding_connector.add_documents(self._build_documents_from(self.memories))
```

**Назначение**: Инициализирует `semantic_grounding_connector` после `__init__`.

**Как работает функция**:

1.  Функция `_post_init` вызывается после выполнения метода `__init__` благодаря декоратору `@utils.post_init`.
2.  Проверяет, существует ли атрибут `memories` и не равен ли он `None`. Если атрибут отсутствует или равен `None`, инициализирует `self.memories` как пустой список.
3.  Создает экземпляр `BaseSemanticGroundingConnector` с описанием "Semantic Memory Storage" и присваивает его атрибуту `self.semantic_grounding_connector`.
4.  Добавляет документы, построенные из текущих воспоминаний (`self.memories`), в `self.semantic_grounding_connector` для индексации и поиска.

```
Пост_инициализация
│
├───> Проверка_существования_и_значения_memories
│    └───> Если_memories_не_существует_или_None
│         └───> Инициализация_memories_пустым_списком
│
├───> Создание_экземпляра_SemanticGroundingConnector
│
└───> Добавление_документов_из_memories_в_SemanticGroundingConnector
```

### `_preprocess_value_for_storage` (SemanticMemory)

```python
def _preprocess_value_for_storage(self, value: dict) -> Any:
    eng