# Модуль `factory.py`

## Обзор

Модуль `factory.py` содержит классы для создания и управления фабриками, которые генерируют агентов (персонажей) `TinyPerson`. Он обеспечивает базовую функциональность для фабрик, а также реализует фабрику для создания агентов на основе контекста и запросов к OpenAI.

## Оглавление

- [Классы](#Классы)
  - [`TinyFactory`](#TinyFactory)
  - [`TinyPersonFactory`](#TinyPersonFactory)
- [Функции](#Функции)
  - [`set_simulation_for_free_factories`](#set_simulation_for_free_factories)
  - [`add_factory`](#add_factory)
  - [`clear_factories`](#clear_factories)
  - [`encode_complete_state`](#encode_complete_state)
  - [`decode_complete_state`](#decode_complete_state)
  - [`generate_person_factories`](#generate_person_factories)
  - [`generate_person`](#generate_person)
  - [`_aux_model_call`](#_aux_model_call)
  - [`_setup_agent`](#_setup_agent)

## Классы

### `TinyFactory`

**Описание**: Базовый класс для различных типов фабрик. Этот класс обеспечивает основу для расширения системы, особенно в отношении кэширования транзакций.

**Методы**:
- `__init__`: Инициализирует экземпляр `TinyFactory`.
- `__repr__`: Возвращает строковое представление объекта `TinyFactory`.
- `set_simulation_for_free_factories`: Устанавливает симуляцию для свободных фабрик.
- `add_factory`: Добавляет фабрику в список всех фабрик.
- `clear_factories`: Очищает глобальный список всех фабрик.
- `encode_complete_state`: Кодирует полное состояние фабрики.
- `decode_complete_state`: Декодирует полное состояние фабрики.

#### `__init__`
```python
def __init__(self, simulation_id:str=None) -> None
```
**Описание**: Инициализирует экземпляр `TinyFactory`.

**Параметры**:
- `simulation_id` (str, optional): ID симуляции. По умолчанию `None`.

#### `__repr__`
```python
def __repr__(self) -> str
```
**Описание**: Возвращает строковое представление объекта `TinyFactory`.

**Возвращает**:
- `str`: Строковое представление объекта `TinyFactory`.

#### `set_simulation_for_free_factories`
```python
@staticmethod
def set_simulation_for_free_factories(simulation) -> None
```
**Описание**: Устанавливает симуляцию, если она `None`. Это позволяет захватывать свободные среды определенными областями симуляции, если это необходимо.

**Параметры**:
- `simulation`: Объект симуляции.

#### `add_factory`
```python
@staticmethod
def add_factory(factory) -> None
```
**Описание**: Добавляет фабрику в список всех фабрик. Имена фабрик должны быть уникальными, поэтому если фабрика с таким же именем уже существует, возникает ошибка.

**Параметры**:
- `factory`: Объект фабрики, который нужно добавить.

**Вызывает исключения**:
- `ValueError`: Если фабрика с таким же именем уже существует.

#### `clear_factories`
```python
@staticmethod
def clear_factories() -> None
```
**Описание**: Очищает глобальный список всех фабрик.

#### `encode_complete_state`
```python
def encode_complete_state(self) -> dict
```
**Описание**: Кодирует полное состояние фабрики. Если подклассы имеют несериализуемые элементы, они должны переопределить этот метод.

**Возвращает**:
- `dict`: Словарь, представляющий состояние фабрики.

#### `decode_complete_state`
```python
def decode_complete_state(self, state:dict) -> object
```
**Описание**: Декодирует полное состояние фабрики. Если подклассы имеют несериализуемые элементы, они должны переопределить этот метод.

**Параметры**:
- `state` (dict): Словарь с состоянием фабрики.

**Возвращает**:
- `object`: Экземпляр фабрики с восстановленным состоянием.

### `TinyPersonFactory`

**Описание**: Класс фабрики для создания экземпляров `TinyPerson`. Использует OpenAI для генерации параметров персонажей на основе предоставленного контекста.

**Методы**:
- `__init__`: Инициализирует экземпляр `TinyPersonFactory`.
- `generate_person_factories`: Генерирует список экземпляров `TinyPersonFactory` с помощью LLM OpenAI.
- `generate_person`: Генерирует экземпляр `TinyPerson` с помощью LLM OpenAI.
- `_aux_model_call`: Вспомогательный метод для выполнения вызова модели.
- `_setup_agent`: Настраивает агента с необходимыми элементами.

#### `__init__`
```python
def __init__(self, context_text:str, simulation_id:str=None) -> None
```
**Описание**: Инициализирует экземпляр `TinyPersonFactory`.

**Параметры**:
- `context_text` (str): Контекстный текст, используемый для генерации экземпляров `TinyPerson`.
- `simulation_id` (str, optional): ID симуляции. По умолчанию `None`.

#### `generate_person_factories`
```python
@staticmethod
def generate_person_factories(number_of_factories: int, generic_context_text: str) -> list | None
```
**Описание**: Генерирует список экземпляров `TinyPersonFactory` с использованием LLM OpenAI.

**Параметры**:
- `number_of_factories` (int): Количество экземпляров `TinyPersonFactory` для генерации.
- `generic_context_text` (str): Общий контекстный текст, используемый для генерации экземпляров `TinyPersonFactory`.

**Возвращает**:
- `list | None`: Список экземпляров `TinyPersonFactory` или `None`, если не удалось сгенерировать.

#### `generate_person`
```python
def generate_person(self, agent_particularities:str=None, temperature:float=1.5, attepmpts:int=5) -> TinyPerson | None
```
**Описание**: Генерирует экземпляр `TinyPerson`, используя LLM OpenAI.

**Параметры**:
- `agent_particularities` (str, optional): Особенности агента.
- `temperature` (float, optional): Температура, используемая при выборке из LLM. По умолчанию `1.5`.
- `attepmpts` (int, optional): Количество попыток генерации. По умолчанию `5`.

**Возвращает**:
- `TinyPerson | None`: Экземпляр `TinyPerson` или `None`, если не удалось сгенерировать.

#### `_aux_model_call`
```python
@transactional
def _aux_model_call(self, messages:list, temperature:float) -> dict | None
```
**Описание**: Вспомогательный метод для выполнения вызова модели. Необходим для использования декоратора `transactional`, чтобы не пропускать создание агента при повторном использовании кэша.

**Параметры**:
- `messages` (list): Список сообщений для отправки в модель.
- `temperature` (float): Температура, используемая при выборке из LLM.

**Возвращает**:
- `dict | None`: Ответ модели или `None`, если не удалось получить ответ.

#### `_setup_agent`
```python
@transactional
def _setup_agent(self, agent:TinyPerson, configuration:dict) -> None
```
**Описание**: Настраивает агента необходимыми элементами.

**Параметры**:
- `agent` (TinyPerson): Экземпляр агента `TinyPerson`.
- `configuration` (dict): Словарь с конфигурацией агента.

## Функции

### `set_simulation_for_free_factories`

```python
@staticmethod
def set_simulation_for_free_factories(simulation)
```

**Описание**: Устанавливает симуляцию для свободных фабрик (с `simulation_id` равным `None`). Это позволяет связать фабрики, созданные вне симуляции, с конкретной симуляцией.

**Параметры**:
- `simulation`: Экземпляр симуляции, к которой нужно привязать фабрики.

### `add_factory`

```python
@staticmethod
def add_factory(factory)
```

**Описание**: Добавляет фабрику в глобальный реестр `all_factories`. Имена фабрик должны быть уникальными.

**Параметры**:
- `factory`: Экземпляр фабрики для добавления.

**Вызывает исключения**:
- `ValueError`: Если фабрика с таким именем уже существует.

### `clear_factories`

```python
@staticmethod
def clear_factories()
```

**Описание**: Очищает глобальный реестр фабрик `all_factories`.

### `encode_complete_state`

```python
def encode_complete_state(self)
```

**Описание**: Кодирует полное состояние фабрики в виде словаря. Подклассы могут переопределять этот метод для обработки несериализуемых атрибутов.

**Возвращает**:
- `dict`: Словарь, представляющий состояние фабрики.

### `decode_complete_state`

```python
def decode_complete_state(self, state)
```

**Описание**: Декодирует состояние фабрики из словаря. Подклассы могут переопределять этот метод для обработки несериализуемых атрибутов.

**Параметры**:
- `state` (dict): Словарь, содержащий состояние фабрики.

**Возвращает**:
- `self`: Обновлённый экземпляр фабрики.

### `generate_person_factories`

```python
@staticmethod
def generate_person_factories(number_of_factories, generic_context_text)
```

**Описание**: Генерирует несколько фабрик персонажей на основе контекста с использованием LLM.

**Параметры**:
- `number_of_factories` (int): Количество фабрик для генерации.
- `generic_context_text` (str): Общий контекст, используемый для генерации.

**Возвращает**:
- `list | None`: Список сгенерированных фабрик `TinyPersonFactory` или `None` в случае ошибки.

### `generate_person`

```python
def generate_person(self, agent_particularities=None, temperature=1.5, attepmpts=5)
```

**Описание**: Генерирует одного персонажа `TinyPerson` на основе контекста и настроек, используя LLM.

**Параметры**:
- `agent_particularities` (str, optional): Дополнительные особенности агента. По умолчанию `None`.
- `temperature` (float, optional): Температура для LLM. По умолчанию `1.5`.
- `attepmpts` (int, optional): Количество попыток генерации. По умолчанию `5`.

**Возвращает**:
- `TinyPerson | None`: Сгенерированный экземпляр `TinyPerson` или `None` в случае ошибки.

### `_aux_model_call`

```python
@transactional
def _aux_model_call(self, messages, temperature)
```

**Описание**: Вспомогательная функция для выполнения вызова LLM, необходимая для корректной работы кэширования транзакций.

**Параметры**:
- `messages` (list): Сообщения для отправки в LLM.
- `temperature` (float): Температура для LLM.

**Возвращает**:
- `dict | None`: Ответ LLM или `None` в случае ошибки.

### `_setup_agent`

```python
@transactional
def _setup_agent(self, agent, configuration)
```

**Описание**: Настраивает агента `TinyPerson` с помощью заданной конфигурации.

**Параметры**:
- `agent` (TinyPerson): Экземпляр агента.
- `configuration` (dict): Словарь конфигурации агента.